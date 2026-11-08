"""Controlled orchestration contracts; no real service startup or inference."""
import hashlib,json,os,sys,tempfile
from pathlib import Path
from unittest.mock import Mock,patch
import auto_test as a
B=Path(__file__).resolve().parent;tag=sys.argv[1] if len(sys.argv)>1 else 'run';T=B/('verification_'+tag);T.mkdir(exist_ok=False)
checks=[]
def check(name,ok):
    checks.append({'case':name,'passed':bool(ok)});print(json.dumps(checks[-1]),flush=True)
def runner(name):
    out=T/name;out.mkdir();return a.Runner(out)
def failure(error):return {'http_ok':False,'http_reachable':False,'error':error,'elapsed_seconds':.01}
DENIED=failure('[WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions')
REFUSED=failure('[WinError 10061] No connection could be made because the target machine actively refused it')
check('Permission denial is not missing service',a.permission_denied(DENIED) and not a.refused(DENIED))
check('Confirmed refusal is recognized',a.refused(REFUSED) and not a.permission_denied(REFUSED))
check('Unexplained timeout is not permission to start a service',not a.refused(failure('timed out')))
out=T/'permission';out.mkdir()
with patch.object(a.c,'http_json',return_value=DENIED),patch.object(a.subprocess,'Popen') as model,patch.object(a.subprocess,'run') as ps:
    result=a.execute(out)
check('Permission denial aborts before service mutation',not model.called and not ps.called and result['count']==0 and 'permission denied' in result['obstacle']['message'].lower())
check('Permission denial preserves partial report',(out/'RESULTS.json').is_file() and not result['completed'] and result['network_bypass_attempted'] is False)
identity=hashlib.sha256(os.path.normcase(os.path.realpath(a.S)).encode()).hexdigest()[:16]
health={'http_ok':True,'body':{'runtime':{'installation_id':identity,'knowledge_profile':'r69-migration-preview','local_llm':{'enabled':True,'model':'fixture-model'}},'common_loaded_build':{'loaded_source_sha256':'current'}}}
r=runner('already_current')
with patch.object(a.c,'http_json',return_value=health),patch.object(a.c,'fingerprint',return_value='current'),patch.object(r,'powershell') as ps:
    response=r.ensure_chat()
check('Current app reused without restart',response is health and not ps.called)
r=runner('wrong_app');wrong={'http_ok':True,'body':{'runtime':{'installation_id':'wrong'}}}
with patch.object(a.c,'http_json',return_value=wrong),patch.object(r,'powershell') as ps:
    try:r.ensure_chat();blocked=False
    except a.StopCheck:blocked=True
check('Other app on port is never stopped',blocked and not ps.called)
r=runner('uncertain_endpoint')
with patch.object(a.c,'http_json',return_value=failure('timed out')),patch.object(r,'powershell') as ps:
    try:r.ensure_chat();blocked=False
    except a.StopCheck:blocked=True
check('Uncertain endpoint does not cause app restart',blocked and not ps.called)
r=runner('start_missing_app')
with patch.object(a.c,'http_json',side_effect=[REFUSED,health]),patch.object(a.c,'fingerprint',return_value='current'),patch.object(r,'powershell') as ps:
    response=r.ensure_chat()
check('Missing R78 starts via existing launcher',response is health and ps.call_count==1 and ps.call_args.args[0]=='start_r78')
r=runner('reload_stale_app');stale=json.loads(json.dumps(health));stale['body']['common_loaded_build']['loaded_source_sha256']='old'
with patch.object(a.c,'http_json',side_effect=[stale,REFUSED,health]),patch.object(a.c,'fingerprint',return_value='current'),patch.object(r,'powershell') as ps:
    response=r.ensure_chat()
check('Stale R78 stops then restarts and verifies new code',response is health and [x.args[0] for x in ps.call_args_list]==['stop_r78','start_r78'])
models={'http_ok':True,'body':{'models':[{'name':'fixture-model:latest'}]}}
check('Installed configured model is matched exactly',a.installed_model(models,'fixture-model')=='fixture-model:latest' and a.installed_model(models,'another') is None)
r=runner('missing_model')
with patch.object(a.subprocess,'Popen') as proc,patch.object(a.c,'http_json') as http:
    try:r.ensure_model(models,'missing');blocked=False
    except a.StopCheck:blocked=True
check('Missing configured model is not downloaded or called',blocked and not proc.called and not http.called)
r=runner('model_probe')
probe={'http_ok':True,'body':{'done':True,'response':'READY'},'elapsed_seconds':.25}
with patch.object(a.c,'http_json',return_value=probe) as http:
    response=r.ensure_model(models,'fixture-model')
    request=http.call_args
check('Readiness uses actual HTTP generation endpoint with selector context',response is probe and request.args[0].endswith('/api/generate') and request.kwargs['payload']['options']['num_ctx']==3072)
check('Readiness does not call a model download endpoint','pull' not in request.args[0])
r=runner('probe_fail')
with patch.object(a.c,'http_json',return_value={'http_ok':True,'body':{'done':False,'response':'partial'}}):
    try:r.ensure_model(models,'fixture-model');blocked=False
    except a.StopCheck:blocked=True
check('Partial generation is not model readiness',blocked)
r=runner('start_missing_ollama');model_process=Mock();model_process.pid=12345;model_process.poll.return_value=None
with patch.object(a.Path,'is_file',return_value=True),patch.object(a.subprocess,'Popen',return_value=model_process) as start,patch.object(a.c,'http_json',side_effect=[models,probe]),patch.object(a.time,'sleep'):
    response=r.ensure_model(REFUSED,'fixture-model')
check('Missing Ollama starts installed serve process without download',response is probe and start.call_count==1 and start.call_args.args[0][-1]=='serve')
check('Started model stays available for chat',not model_process.terminate.called and not model_process.kill.called)
body={'decision_artifact':{'query_plan':{'entity_selection':{'attempted':False,'model_call_avoided':True}}}}
check('LLM ON or shortcut does not count as an actual selector call',not a.call_verified(body))
body['decision_artifact']['query_plan']['entity_selection']={'attempted':True,'transport_ok':False,'availability_failure':'timeout'}
check('Selector timeout does not count as success',not a.call_verified(body))
body['decision_artifact']['query_plan']['entity_selection']={'attempted':True,'transport_ok':True,'schema_accepted':True}
check('Completed schema-valid selection is tracked separately',a.call_verified(body))
body['decision_artifact']['query_plan']['entity_selection'].update(semantic_selection_accepted=False,reason='unsupported_task_span')
check('Schema-valid but rejected binding is not semantic success',a.call_verified(body) and a.binding_rejection(body)=='unsupported_task_span')
check('Abstention without an error is not a fabricated binding rejection',a.binding_rejection({'decision_artifact':{'query_plan':{'entity_selection':{'semantic_selection_accepted':False}}}}) is None)
check('Malformed chat response has no fabricated inference',not a.call_verified([]))
for p in [B/'auto_test.py',B/'test_runner.py']:compile(p.read_text(encoding='utf8'),str(p),'exec')
check('Runner syntax valid',True)
result={'count':len(checks),'passed':sum(x['passed'] for x in checks),'controlled_service_fixtures':True,'real_network_calls':False,'real_model_inference_verified':False,'checks':checks}
with (B/('RUNNER_QA_'+tag+'.json')).open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not x['passed'] for x in checks))
