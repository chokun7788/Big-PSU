"""Execute the unchanged 1,400 questions through a real isolated chat server."""
import collections,hashlib,json,os,socket,subprocess,sys,time,traceback,urllib.request,urllib.error,uuid
from datetime import datetime
from pathlib import Path
from native_grader import grade,claims_from
R=Path(__file__).resolve().parent;S=R/'system';MODEL='scb10x/typhoon2.5-qwen3-4b:latest';DIGEST='b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text('utf8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def tags():
    with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as h:x=json.load(h)
    assert next(m['digest'] for m in x['models'] if m['name']==MODEL)==DIGEST
def get(url):
    with urllib.request.urlopen(url,timeout=2) as h:return json.load(h)
def events(response):
    found={}
    def visit(x):
        if isinstance(x,dict):
            if 'transport_ok' in x and 'schema_ok' in x and x.get('id'):found[x['id']]=x
            for v in x.values():visit(v)
        elif isinstance(x,list):
            for v in x:visit(v)
    visit(response.get('decision_artifact',{}));return list(found.values())
out=R/'runs'/sys.argv[1];out.mkdir(parents=True,exist_ok=False)
jobs=list(map(json.loads,(R/'EXISTING_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()));assert len(jobs)==1400
expected={j['id']:j for j in read(R/'NATIVE_EXPECTATIONS.json')['questions']}
reference=read(R/'NATIVE_SOURCE_REFERENCE.json');allowed_refs={(r['source_id'],r['locator']) for f in reference['facts'] for r in f.get('evidence_refs',[])+f.get('confirmation_evidence_refs',[])}
files=[p for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix in {'.py','.js','.html','.css','.json','.sqlite'}]
files += [R/x for x in ['EXISTING_QUESTIONS_1400.jsonl','NATIVE_EXPECTATIONS.json','NATIVE_SOURCE_REFERENCE.json','SOURCE_ALIGNMENT.json','native_grader.py','run_http.py']]
freeze={str(p.resolve()):sha(p) for p in files};write(out/'RUN_FREEZE.json',{'files':freeze,'model':MODEL,'model_digest':DIGEST,'new_questions':0,'category_hints_sent':False,'endpoint':'actual /api/chat','started_at':datetime.now().astimezone().isoformat()})
def progress(v):
    tmp=out/'progress.new';tmp.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
    for i in range(6):
        try:os.replace(tmp,out/'PROGRESS.json');return
        except PermissionError:time.sleep(.05*(i+1))
    write(out/('PROGRESS_IO_'+str(time.time_ns())+'.json'),v)
proc=None;log=None;count=0;stats=collections.defaultdict(collections.Counter);seen=set();latencies=[]
try:
    tags()
    with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
    env=os.environ.copy();env.update(PYTHONPATH=str(S),PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_COMMON_CHAT_PROFILE='r69-migration-preview',
      PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r115-native-http-validation',PSU_RUNTIME_VERSION='R115',PSU_ESPORTS_NOW=jobs[0]['reference_time'],
      PSU_CHAT_LOG_DIR=str(out/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(out/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(out/'conversation.sqlite'),
      PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',PSU_CHATBOT_OLLAMA_MODEL=MODEL,
      PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='30',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='32')
    log=(out/'SERVER.log').open('x',encoding='utf8');proc=subprocess.Popen([sys.executable,'-B','-X','utf8','-m','app.web_api.server','--host','127.0.0.1','--port',str(port)],
        cwd=S,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    url='http://127.0.0.1:'+str(port)
    for _ in range(100):
        if proc.poll() is not None:raise RuntimeError('Candidate server exited during startup')
        try:health=get(url+'/health');break
        except (OSError,ValueError):time.sleep(.4)
    else:raise RuntimeError('Candidate startup timed out')
    assert health['runtime']['knowledge_draft_preview'] and health['features']['local_llm_assist']
    write(out/'HEALTH_BEFORE.json',health);write(out/'PROCESS.json',{'server_pid':proc.pid,'runner_pid':os.getpid(),'url':url,'candidate_only':True,'reference_time':jobs[0]['reference_time']})
    started=time.monotonic()
    with (out/'RESULTS.jsonl').open('x',encoding='utf8') as f,(out/'MODEL_EVENTS.jsonl').open('x',encoding='utf8') as ef:
        for j in jobs:
            assert j['id'] not in seen
            payload={'question':j['question'],'locale':j['locale'],'debug':True,'experimental_allow_llm':True,
              'client_session_id':out.name+'-'+j['id'],'client_turn_id':uuid.uuid4().hex}
            req=urllib.request.Request(url+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
            before=time.monotonic();http=0;error=None
            try:
                with urllib.request.urlopen(req,timeout=60) as h:http=h.status;response=json.load(h)
            except urllib.error.HTTPError as exc:
                http=exc.code
                try:response=json.loads(exc.read())
                except (ValueError,TypeError):response={}
                error='HTTP '+str(http)
            except (OSError,ValueError) as exc:response={};error=type(exc).__name__+': '+str(exc)
            elapsed=time.monotonic()-before;latencies.append(elapsed);g=grade(expected[j['id']],response,http,allowed_refs)
            row={'question_id':j['id'],'category':j['category'],'question':j['question'],'locale':j['locale'],'stratum':j['stratum'],'fixture':j['fixture'],
                 'http_status':http,'elapsed_sec':round(elapsed,4),'error':error,'response':response,'grade':g}
            f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
            for e in events(response):ef.write(json.dumps({**e,'question_id':j['id']},ensure_ascii=False)+'\n');ef.flush()
            c=stats[j['category']];c['questions']+=1;c['strict_passed']+=g['passed'];c['content_exact']+=g['content_exact'];c['matched_claims']+=g['matched_claims'];c['expected_claims']+=g['expected_claims']
            c['http_ok']+=g['http_ok'];c['validation_ok']+=g['validation_ok'];c['safe_abstentions']+=g['safe_abstention'];c[g['classification']]+=1
            count+=1;seen.add(j['id'])
            if count%10==0:
                progress({'completed':count,'total':1400,'running':True,'pid':os.getpid(),'server_pid':proc.pid,'elapsed_sec':round(time.monotonic()-started,2),
                  'last_question_id':j['id'],'updated_at':datetime.now().astimezone().isoformat(),'scores':{k:dict(v) for k,v in stats.items()}})
            if count%100==0:print(json.dumps({'completed':count,'elapsed_sec':round(time.monotonic()-started,1),'category':j['category'],**dict(c)},ensure_ascii=False),flush=True)
    assert count==len(seen)==1400
    tags();after=get(url+'/health');assert after['common_loaded_build']==health['common_loaded_build'];write(out/'HEALTH_AFTER.json',after)
    changed=[p for p,h in freeze.items() if sha(Path(p))!=h];assert not changed,changed
    ordered=sorted(latencies)
    summary={'complete':True,'unique_question_keys':len(seen),'requests':count,'new_questions_added':0,'category_hints_sent':False,'actual_chat_http':True,
      'model_enabled':True,'model_identity_verified':True,'source_code_inputs_unchanged':True,'elapsed_sec':round(time.monotonic()-started,2),
      'latency_median_sec':ordered[len(ordered)//2],'latency_p95_sec':ordered[int(len(ordered)*.95)],'scores':{k:dict(v) for k,v in stats.items()},
      'semantic_accuracy_claimed':False,'completed_at':datetime.now().astimezone().isoformat()}
    write(out/'TEST_COMPLETE.json',summary);progress({'completed':1400,'total':1400,'running':False,'complete':True})
except BaseException as exc:
    write(out/'FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),'completed':count,'expected':1400,'runner_pid':os.getpid(),'complete':False});raise
finally:
    if proc is not None:
        proc.terminate()
        try:proc.wait(timeout=10)
        except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=5)
        write(out/'SERVER_STOPPED.json',{'pid':proc.pid,'exit_code':proc.returncode,'stopped_by_runner':True})
    if log:log.close()
