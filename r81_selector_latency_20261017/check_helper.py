"""Offline checker contracts; never sends network requests."""
import copy,hashlib,json,os
from pathlib import Path
from unittest.mock import patch
import check_live as c
B=Path(__file__).resolve().parent
checks=[]
def check(name,ok):checks.append({'case':name,'passed':bool(ok)})
for p in [B/'check_live.py',B/'test_selector.py',B/'run_existing.py',*(B/'candidate').rglob('*.py')]:
    compile(p.read_text(encoding='utf8'),str(p),'exec')
check('Candidate and helper syntax',True)
identity=hashlib.sha256(os.path.normcase(os.path.realpath(c.S)).encode()).hexdigest()[:16]
body={'runtime':{'installation_id':identity,'knowledge_profile':'r69-migration-preview','local_llm':{'enabled':True}},'common_loaded_build':{'loaded_source_sha256':'fixture-hash'}}
check('Current expected fingerprint accepted',c.verify_health(body,'fixture-hash'))
check('Old loaded fingerprint rejected',not c.verify_health(body,'new-hash'))
for path,val in [('installation_id','wrong'),('knowledge_profile','wrong')]:
    bad=copy.deepcopy(body);bad['runtime'][path]=val
    check('Wrong '+path+' rejected',not c.verify_health(bad,'fixture-hash'))
bad=copy.deepcopy(body);bad['runtime']['local_llm']['enabled']=False
check('LLM OFF rejected',not c.verify_health(bad,'fixture-hash'))
for url in ['https://example.com','http://localhost:8115/health','http://127.0.0.1:8000/health']:
    with patch.object(c.helper.request,'build_opener',side_effect=AssertionError('Unexpected network')):
        try:c.http_json(url);ok=False
        except ValueError:ok=True
    check('Non-allowlisted endpoint rejected '+url,ok)
p={'validation_ok':True,'answer':'Do you mean this topic?', 'common_read_state':{'profile_confirmation':{'version':1}},'decision_artifact':{'query_plan':{'entity_selection':{'attempted':False,'model_call_avoided':True}}}}
check('Fast clarification contract accepted',not c.grade(p,'pending_fast'))
bad=copy.deepcopy(p);bad['decision_artifact']['query_plan']['entity_selection']={'attempted':True,'availability_failure':'timeout'}
check('Slow fallback remains a topic clarification',not c.grade(bad,'pending'))
check('Slow fallback does not pass fast-path contract',bool(c.grade(bad,'pending_fast')))
bad=copy.deepcopy(p);bad['common_read_state']={}
check('Missing server state rejected',bool(c.grade(bad,'pending')))
bad=copy.deepcopy(p);bad['answer']='Hours table\nlong';bad['decision_artifact']['query_plan']={'day_status':'closed'}
check('Verbose old opening reply rejected',bool(c.grade(bad,'open_day')))
result={'count':len(checks),'passed':sum(x['passed'] for x in checks),'network_called':False,'checks':checks}
with (B/'HELPER_QA.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False));raise SystemExit(any(not x['passed'] for x in checks))
