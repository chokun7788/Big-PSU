"""Loopback diagnostics. No service/firewall/config/model-download changes."""
from __future__ import annotations
import argparse,csv,hashlib,io,json,os,re,subprocess,time,uuid
from datetime import datetime,timezone
from pathlib import Path
from urllib import request,error

B=Path(__file__).resolve().parent
SYSTEM=B.parent/'r78_web_session_check_20261016/system'
MODEL='scb10x/typhoon2.5-qwen3-4b'

def emit_json(path,data):
    with path.open('x',encoding='utf8') as f:json.dump(data,f,ensure_ascii=False,indent=2)

def inventory():
    result={'method':'read-only netstat and tasklist','ports':{},'errors':[]}
    try:
        p=subprocess.run(['netstat.exe','-ano','-p','tcp'],capture_output=True,text=True,timeout=8,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        result['netstat_exit_code']=p.returncode
        if p.returncode:result['errors'].append('netstat failed: '+p.stderr[:500])
        for line in p.stdout.splitlines():
            parts=line.split()
            if len(parts)!=5 or parts[0].upper()!='TCP':continue
            port=parts[1].rsplit(':',1)[-1]
            if port in {'11434','8115'} and parts[3].upper()=='LISTENING':result['ports'].setdefault(port,[]).append({'local_address':parts[1],'pid':parts[4]})
        # Process names only for those listeners, not a dump of unrelated apps.
        for rows in result['ports'].values():
            for row in rows:
                proc=subprocess.run(['tasklist.exe','/FI','PID eq '+row['pid'],'/FO','CSV','/NH'],capture_output=True,text=True,timeout=5,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
                parsed=list(csv.reader(io.StringIO(proc.stdout)))
                if parsed and len(parsed[0])>=2 and parsed[0][1]==row['pid']:row['process_name']=parsed[0][0]
    except (OSError,subprocess.TimeoutExpired) as exc:result['errors'].append(type(exc).__name__+': '+str(exc))
    result['absence_conclusive']=result.get('netstat_exit_code')==0 and not result['errors']
    return result

def http_json(url,*,payload=None,timeout=4):
    # Never accept an endpoint supplied by model output or a remote host.
    from urllib.parse import urlparse
    p=urlparse(url)
    if p.scheme!='http' or p.hostname!='127.0.0.1' or p.port not in {11434,8115}:raise ValueError('Only the two local diagnostic services are allowed')
    row={'url':url,'http_reachable':False,'http_ok':False,'json_valid':False}
    body=json.dumps(payload,ensure_ascii=False).encode('utf8') if payload is not None else None
    req=request.Request(url,data=body,headers={'Content-Type':'application/json'} if body else {})
    start=time.perf_counter()
    try:
        # Direct loopback only; never send the diagnostic prompt through a proxy.
        opener=request.build_opener(request.ProxyHandler({}))
        with opener.open(req,timeout=timeout) as response:
            row.update(http_reachable=True,http_ok=200<=response.status<300,status=response.status)
            text=response.read(4_000_001)
            if len(text)>4_000_000:raise ValueError('Response exceeds diagnostic size limit')
            row['body']=json.loads(text.decode('utf8'));row['json_valid']=True
    except error.HTTPError as exc:
        row.update(http_reachable=True,status=exc.code,error_type='HTTPError',error=str(exc))
    except (OSError,ValueError) as exc:row.update(error_type=type(exc).__name__,error=str(exc))
    row['elapsed_seconds']=round(time.perf_counter()-start,3)
    return row

def diagnostic(out,*,generation=True,chat=True):
    r={'started_utc':datetime.now(timezone.utc).isoformat(),'launch_context_declared':'ordinary Windows launch requested','context_independently_verified':False,
       'settings_changed':False,'model_downloaded':False,'model_generation_verified':False,'chat_session_contract_passed':False,'checks':[]}
    inv=inventory();emit_json(out/'LISTENERS.json',inv)
    health=http_json('http://127.0.0.1:8115/health');r['checks'].append({'name':'r78_health',**health})
    body=health.get('body');runtime=body.get('runtime',{}) if isinstance(body,dict) else {}
    identity=hashlib.sha256(os.path.normcase(os.path.realpath(SYSTEM)).encode()).hexdigest()[:16]
    expected=bool(health['http_ok'] and runtime.get('installation_id')==identity and runtime.get('knowledge_profile')=='r69-migration-preview')
    r['r78_identity_verified']=expected
    configured=(runtime.get('local_llm',{}).get('model') if expected else None) or os.getenv('PSU_CHATBOT_OLLAMA_MODEL',MODEL)
    r['configured_model']=configured
    tags=http_json('http://127.0.0.1:11434/api/tags');r['checks'].append({'name':'model_list',**tags})
    models=(tags.get('body') or {}).get('models',[]) if isinstance(tags.get('body'),dict) else []
    installed=next((m.get('name') or m.get('model') for m in models if isinstance(m,dict) and str(m.get('name') or m.get('model') or '').removesuffix(':latest')==configured.removesuffix(':latest')),None)
    if generation and installed and tags['http_ok']:
        gen=http_json('http://127.0.0.1:11434/api/generate',payload={'model':installed,'prompt':'Reply with only READY.','stream':False,'options':{'temperature':0,'num_predict':48}},timeout=60)
        body=gen.get('body');valid=bool(gen['http_ok'] and isinstance(body,dict) and body.get('done') is True and isinstance(body.get('response'),str) and body['response'].strip())
        r['model_generation_verified']=valid
        r['checks'].append({'name':'model_generate','generation_nonempty_done':valid,'ready_exact':valid and body['response'].strip()=='READY',**gen})
    else:r['checks'].append({'name':'model_generate','skipped':True,'reason':'not requested' if not generation else 'model list not accessible' if not tags['http_ok'] else 'configured model not present; nothing downloaded'})
    # Use only a verified R78 endpoint, never a different app occupying the port.
    if chat and expected:
        sid='connection-check-'+uuid.uuid4().hex
        turns=[]
        for q in ['Can I bring my own input peripheral?','Yes, but it is my own keyboard.','And my mouse?']:
            turn=http_json('http://127.0.0.1:8115/api/chat',payload={'question':q,'locale':'en','client_session_id':sid,'client_turn_id':uuid.uuid4().hex,'debug':True},timeout=45)
            turns.append({'question':q,**turn})
            if not turn['http_ok']:break
        final=turns[-1].get('body',{}) if turns else {}
        r['chat_session_contract_passed']=bool(len(turns)==3 and isinstance(final,dict) and final.get('validation_ok') is True and 'not allowed' in final.get('answer','').lower())
        emit_json(out/'CHAT_TURNS.json',turns)
        r['checks'].append({'name':'three_turn_chat','turn_count':len(turns),'contract_passed':r['chat_session_contract_passed']})
    else:r['checks'].append({'name':'three_turn_chat','skipped':True,'reason':'not requested' if not chat else 'R78 endpoint not reachable or identity not verified'})
    text=' '.join(str(x.get('error','')) for x in r['checks'])
    forbidden=bool(re.search(r'10013|forbidden by its access permissions|access.+denied',text,re.I))
    absent=[]
    if inv['absence_conclusive']:
        absent=[p for p in ['11434','8115'] if p not in inv['ports']]
    r['summary']={'socket_permission_error_observed':forbidden,'confirmed_listener_absence':absent,
       'comparison_with_assistant_tool':'If this user-launched check succeeds where TOOL_NETWORK_PROBES failed, the contexts behave differently. This does not identify the exact security component.',
       'chat_answer_accuracy_generally_verified':False,'wordpress_tested':False}
    emit_json(out/'RESULTS.json',r)
    lines=['# Local connection diagnostic results','',
       '- Model list reachable: '+str(tags['http_ok']),
       '- Model generated a nonempty completed response: '+str(r['model_generation_verified']),
       '- R78 identity verified: '+str(expected),
       '- Three-turn chat contract passed: '+str(r['chat_session_contract_passed']),
       '- Socket permission error observed: '+str(forbidden),
       '- Confirmed listener absence: '+(', '.join(absent) or 'none confirmed'),'',
       'See RESULTS.json, LISTENERS.json and CHAT_TURNS.json (if created).',
       'A failed list call does not prove that the model is missing. A successful generation does not prove chatbot answer accuracy.',
       'If 11434 has no listener, start the installed Ollama app. If 8115 has no listener, open Open-New-Chat.cmd in r78_web_session_check_20261016.',
       'This checker does not start services, download models or alter firewall/security settings.']
    (out/'SUMMARY.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    return r

def main():
    p=argparse.ArgumentParser();p.add_argument('--skip-generation',action='store_true');p.add_argument('--skip-chat',action='store_true');args=p.parse_args()
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]
    out=B/'user_results'/stamp;out.mkdir(parents=True,exist_ok=False)
    print('Checking local services. No settings will be changed.',flush=True)
    print('Generation can take up to 60 seconds; chat calls up to 45 seconds each.',flush=True)
    try:
        result=diagnostic(out,generation=not args.skip_generation,chat=not args.skip_chat)
        print(json.dumps({'model_generation_verified':result['model_generation_verified'],'r78_identity_verified':result['r78_identity_verified'],'chat_contract_passed':result['chat_session_contract_passed']},ensure_ascii=False),flush=True)
    except Exception as exc:
        emit_json(out/'CHECKER_ERROR.json',{'error_type':type(exc).__name__,'error':str(exc)});print('Checker stopped: '+str(exc),flush=True)
    print('Results saved: '+str(out),flush=True)
if __name__=='__main__':main()
