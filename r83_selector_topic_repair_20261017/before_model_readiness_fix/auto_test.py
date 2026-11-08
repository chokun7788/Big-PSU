"""One-entry Windows runner: real Ollama + real R78 HTTP, no network bypass.

Starts installed local services only when connection-refused is established.
Permission denial aborts before launching or restarting anything.
"""
from __future__ import annotations
import hashlib,importlib.util,json,os,subprocess,sys,time,uuid
from datetime import datetime,timezone
from pathlib import Path

B=Path(__file__).resolve().parent
R81=B.parent/'r81_selector_latency_20261017'
R78=B.parent/'r78_web_session_check_20261016'
S=R78/'system'
spec=importlib.util.spec_from_file_location('r81_live',R81/'check_live.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

class StopCheck(RuntimeError):pass

def permission_denied(row):
    return any(s in str(row.get('error','')).casefold() for s in ('10013','forbidden by its access permissions','permission denied','access is denied'))

def refused(row):
    return not row.get('http_reachable') and any(s in str(row.get('error','')).casefold() for s in ('10061','connection refused','actively refused'))

def same_installation(body):
    identity=hashlib.sha256(os.path.normcase(os.path.realpath(S)).encode()).hexdigest()[:16]
    runtime=body.get('runtime',{}) if isinstance(body,dict) else {}
    return runtime.get('installation_id')==identity and runtime.get('knowledge_profile')=='r69-migration-preview'

def installed_model(tags,configured):
    body=tags.get('body') or {}
    models=body.get('models',[]) if isinstance(body,dict) else []
    return next((m.get('name') or m.get('model') for m in models if isinstance(m,dict) and str(m.get('name') or m.get('model') or '').removesuffix(':latest')==configured.removesuffix(':latest')),None)

def selected_audit(body):
    if not isinstance(body,dict):return {}
    return ((body.get('decision_artifact') or {}).get('query_plan') or {}).get('entity_selection') or {}

def call_verified(body):
    a=selected_audit(body)
    return a.get('attempted') is True and a.get('transport_ok') is True and a.get('schema_accepted') is True

def binding_rejection(body):
    a=selected_audit(body)
    return a.get('reason') if a.get('semantic_selection_accepted') is False and a.get('reason') else None

def save(path,value):
    with path.open('x',encoding='utf8') as f:json.dump(value,f,ensure_ascii=False,indent=2)

class Runner:
    def __init__(self,out):self.out=out;self.steps=[];self.rows=[];self.owned_model=None
    def record(self,name,row):
        self.steps.append({'step':name,**row});save(self.out/(str(len(self.steps)).zfill(2)+'_'+name+'.json'),row)
        return row
    def get(self,name,url,**kw):
        row=self.record(name,c.http_json(url,**kw))
        if permission_denied(row):raise StopCheck('Socket permission denied (10013). No alternate connection path or privilege change was attempted. Open this runner from ordinary Windows.')
        return row
    def powershell(self,name,path):
        # Existing launchers perform installation/PID/token ownership checks.
        with (self.out/(name+'.out.log')).open('x',encoding='utf8') as stdout,(self.out/(name+'.err.log')).open('x',encoding='utf8') as stderr:
            try:
                # Includes Windows/PowerShell startup as well as app startup.
                # This service-readiness wait is separate from chat deadlines.
                p=subprocess.run(['powershell.exe','-NoProfile','-ExecutionPolicy','Bypass','-File',str(path)],stdout=stdout,stderr=stderr,timeout=180 if name=='start_r78' else 100,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            except subprocess.TimeoutExpired:raise StopCheck(name+' exceeded its wait limit; inspect saved launcher logs before restarting again.')
        self.record(name,{'returncode':p.returncode})
        if p.returncode:raise StopCheck(name+' failed; see saved launcher logs. No forced process termination was used.')
    def ensure_chat(self):
        health=self.get('chat_health_before','http://127.0.0.1:8115/health')
        if health.get('http_ok'):
            body=health.get('body')
            if not same_installation(body):raise StopCheck('Port 8115 belongs to another application/profile. It was left running.')
            if c.verify_health(body,c.fingerprint()):return health
            print('Reloading the recorded R78 chat to use the current source and LLM ON...',flush=True)
            self.powershell('stop_r78',R78/'Stop-New-Chat.ps1')
            ended=False
            for i in range(20):
                # Windows may report refused only after a connection timeout
                # longer than one second. Do not mistake a short probe timeout
                # for an app that is still running.
                row=c.http_json('http://127.0.0.1:8115/health',timeout=4)
                self.record('shutdown_wait_'+str(i),row)
                if permission_denied(row):raise StopCheck('Permission denied while waiting for R78 shutdown.')
                if refused(row):ended=True;break
                if row.get('http_ok') and not same_installation(row.get('body')):raise StopCheck('Port 8115 changed ownership during restart.')
                time.sleep(.5)
            if not ended:raise StopCheck('R78 shutdown was not confirmed; startup was not attempted.')
        elif not refused(health):raise StopCheck('R78 endpoint could not be diagnosed safely; inspect chat_health_before.')
        print('Starting the installed R78 chat...',flush=True)
        self.powershell('start_r78',R78/'Start-New-Chat.ps1')
        health=self.get('chat_health_after','http://127.0.0.1:8115/health')
        if not health.get('http_ok') or not c.verify_health(health.get('body'),c.fingerprint()):raise StopCheck('Current R78 source fingerprint and LLM ON could not be verified.')
        return health
    def ensure_model(self,tags,configured):
        if not tags.get('http_ok'):
            if not refused(tags):raise StopCheck('Ollama endpoint is unavailable for an unconfirmed reason. Nothing was started.')
            options=[Path(os.getenv('LOCALAPPDATA',''))/'Programs/Ollama/ollama.exe']
            exe=next((p for p in options if p.is_file()),None)
            if exe is None:raise StopCheck('The installed Ollama executable was not found. No installer or model download was run.')
            print('Starting installed Ollama in the background...',flush=True)
            with (self.out/'ollama.out.log').open('x',encoding='utf8') as stdout,(self.out/'ollama.err.log').open('x',encoding='utf8') as stderr:
                self.owned_model=subprocess.Popen([str(exe),'serve'],stdout=stdout,stderr=stderr,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            self.record('ollama_started',{'pid':self.owned_model.pid,'executable':str(exe),'kept_running_after_test':True})
            waiting_deadline=time.monotonic()+30
            for i in range(30):
                if self.owned_model.poll() is not None:raise StopCheck('Started Ollama exited; inspect saved Ollama logs.')
                tags=c.http_json('http://127.0.0.1:11434/api/tags',timeout=4)
                if permission_denied(tags):raise StopCheck('Permission denied after starting Ollama. No alternate connection path was attempted.')
                if tags.get('http_ok'):break
                if not refused(tags) and tags.get('error_type')!='TimeoutError':raise StopCheck('Ollama startup returned an unexpected connection error.')
                if time.monotonic()>=waiting_deadline:break
                time.sleep(.5)
            self.record('model_list_after_start',tags)
        model=installed_model(tags,configured)
        if not tags.get('http_ok') or not model:raise StopCheck('Configured model is not confirmed installed. No model download was run.')
        gen=self.get('real_model_generation','http://127.0.0.1:11434/api/generate',payload={'model':model,'stream':False,'think':False,'keep_alive':'30m','prompt':'Reply with only READY.','options':{'temperature':0,'num_ctx':3072,'num_predict':48}},timeout=60)
        envelope=gen.get('body')
        if not (gen.get('http_ok') and isinstance(envelope,dict) and envelope.get('done') is True and isinstance(envelope.get('response'),str) and envelope['response'].strip()):raise StopCheck('Real model generation did not complete. Chat answer tests have not started.')
        return gen
    def chat_cases(self):
        for case,lang,turns in c.CASES:
            sid='r82-'+uuid.uuid4().hex
            for question,expect in turns:
                row=c.http_json('http://127.0.0.1:8115/api/chat',payload={'question':question,'locale':lang,'client_session_id':sid,'client_turn_id':uuid.uuid4().hex,'debug':True},timeout=30)
                errors=c.grade(row.get('body'),expect) if row.get('http_ok') else ['http_unavailable']
                body=row.get('body') if isinstance(row.get('body'),dict) else {}
                audit=selected_audit(body)
                result={'case':case,'locale':lang,'question':question,'expected':expect,'passed':not errors,'errors':errors,'selector_model_call_verified':call_verified(body),'selector_binding_rejection':binding_rejection(body),'selector_failure':audit.get('availability_failure'),**row}
                self.rows.append(result)
                with (self.out/'CHAT_TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(result,ensure_ascii=False)+'\n')
                print(json.dumps({'case':case,'passed':not errors,'http_seconds':row['elapsed_seconds'],'selector_model_call_verified':result['selector_model_call_verified'],'selector_failure':result['selector_failure']},ensure_ascii=False),flush=True)
                if permission_denied(row):raise StopCheck('Permission denied during chat tests; partial results retained.')
                if not row.get('http_ok'):raise StopCheck('Chat HTTP failed; partial results retained.')

def execute(out):
    runner=Runner(out);result={'started_utc':datetime.now(timezone.utc).isoformat(),'completed':False,'llm_enabled_verified':False,'real_model_generation_verified':False,'full_test':False,'production_data_modified':False,'settings_modified':False,'model_downloaded':False,'network_bypass_attempted':False}
    db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
    try:
        installation=json.loads((R81/'INSTALLATION.json').read_text(encoding='utf8'))
        if not all(hashlib.sha256((S/name).read_bytes()).hexdigest()==v for name,v in installation['installed_files'].items()):raise StopCheck('Installed source differs from verified R81. Review changes before benchmarking.')
        # Probe both existing services before launching anything. A tool-context
        # socket restriction must not be mistaken for an absent local service.
        tags=runner.get('model_list_before','http://127.0.0.1:11434/api/tags')
        health=runner.ensure_chat();result['llm_enabled_verified']=True
        configured=health['body']['runtime']['local_llm']['model']
        probe=runner.ensure_model(tags,configured);result['real_model_generation_verified']=True
        result['ready_probe_exact']=probe['body']['response'].strip()=='READY'
        result['ready_probe_seconds']=probe['elapsed_seconds']
        runner.chat_cases();result['completed']=True
    except (StopCheck,OSError,ValueError,KeyError,TypeError) as error:
        result['obstacle']={'type':type(error).__name__,'message':str(error)}
        print('Stopped: '+str(error),flush=True)
    finally:
        result.update(count=len(runner.rows),expected_count=sum(len(x[2]) for x in c.CASES),passed=sum(r['passed'] for r in runner.rows),database_unchanged=before==hashlib.sha256(db.read_bytes()).hexdigest())
        result['by_language']={lang:{'count':sum(r['locale']==lang for r in runner.rows),'passed':sum(r['locale']==lang and r['passed'] for r in runner.rows)} for lang in ('th','en')}
        result['chat_selector']={'actual_calls_attempted':sum(selected_audit(r.get('body') or {}).get('attempted') is True for r in runner.rows),'calls_with_valid_schema':sum(r['selector_model_call_verified'] for r in runner.rows),'failures':[{'case':r['case'],'question':r['question'],'failure':r['selector_failure']} for r in runner.rows if r['selector_failure']]}
        result['chat_selector']['binding_rejections']=[{'case':r['case'],'question':r['question'],'reason':binding_rejection(r.get('body'))} for r in runner.rows if binding_rejection(r.get('body'))]
        result['all_answer_contracts_passed']=result['completed'] and result['count']==result['expected_count'] and result['passed']==result['count']
        result['all_attempted_selector_calls_returned_valid_schema']=bool(result['chat_selector']['actual_calls_attempted']) and result['chat_selector']['actual_calls_attempted']==result['chat_selector']['calls_with_valid_schema'] and not result['chat_selector']['failures']
        result['all_selector_protocol_checks_passed']=result['all_attempted_selector_calls_returned_valid_schema'] and not result['chat_selector']['binding_rejections']
        save(out/'RESULTS.json',result)
        (out/'SUMMARY.md').write_text('# R82 automated local LLM + chat check\n\n```json\n'+json.dumps(result,ensure_ascii=False,indent=2)+'\n```\n\nAnswer contracts, direct model generation and model selector calls are separate results. The model was explicitly warmed before chat timings. A valid schema is not independent proof of semantic accuracy. No full corpus was run.\n',encoding='utf8')
        print('Results saved: '+str(out),flush=True)
    return result

def main():
    out=B/'results'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]);out.mkdir(parents=True,exist_ok=False)
    result=execute(out)
    return 0 if result['all_answer_contracts_passed'] and result['all_selector_protocol_checks_passed'] else 1
if __name__=='__main__':raise SystemExit(main())
