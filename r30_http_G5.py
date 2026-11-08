import sys,os,json,urllib.request,time,uuid,collections
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p))
r=Path(Path('r30_report_path.txt').read_text().strip());run=sys.argv[1];base='http://127.0.0.1:'+sys.argv[2]
from tools.run_master_ground_truth_eval import actual_status
from tools.run_competition_contract_r27 import check_content_contract
from tools.run_competition_composition_r28 import check
health=json.load(urllib.request.urlopen(base+'/health',timeout=5));assert health['runtime']['version']=='2026.10.02-full-improvement-r30-G5'
with (r/(run+'_health_before.json')).open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
tasks=[('source_G5',json.loads((r/'focused_fixture_G5_source.json').read_text(encoding='utf-8'))['cases']),('focused79',json.loads((r/'focused_fixture_v2.json').read_text(encoding='utf-8'))['cases']),('competition_G53',json.loads((r/'focused_fixture_G_new_v2.json').read_text(encoding='utf-8'))['cases']),('mixed_title8',json.loads((r/'mixed_title_fixture_G3.json').read_text(encoding='utf-8'))['cases'])]
for name in ['competition_composition_r28_280_20261001.json','competition_content_contract_r27_320_20261001.json','competition_new_questions_r27_128_20261001.json']:
    d=json.loads((p/'data/eval'/name).read_text(encoding='utf-8'));tasks.append((name,d if isinstance(d,list) else d['cases']))
counts=collections.defaultdict(collections.Counter);start=time.perf_counter();done=0
with (r/(run+'_http_results.jsonl')).open('x',encoding='utf-8') as out:
    for suite,cases in tasks:
        for c in cases:
            payload={'question':c['question'],'locale':c['locale'],'recent_history':[],'client_session_id':'r30-'+uuid.uuid4().hex,'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
            t=time.perf_counter()
            try:
                raw=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30))
                response={'answer':raw.get('answer',''),'mode':raw.get('mode',''),'category':raw.get('route_category',''),'hits':raw.get('sources',[]),'valid':raw.get('validation_ok',True),'raw':raw}
                if suite in ('focused79','competition_G53','mixed_title8','source_G5'):
                    errors=['missing:'+s for s in c['must_contain'] if s.casefold() not in response['answer'].casefold()]+['forbidden:'+s for s in c['must_not_contain'] if s.casefold() in response['answer'].casefold()]
                    status=actual_status(response['mode'],response['answer'],response['category'])
                    if c['outcome'] and c.get('group')!='true_wrong_layout' and status!=c['outcome']:errors.append('wrong_outcome:'+status)
                    if not response['valid']:errors.append('validation_rejected')
                    required_mode='pipeline:live_booking_status' if c.get('group')=='live_required' else c.get('mode_prefix')
                    if required_mode and not response['mode'].startswith(required_mode):errors.append('mode_contract:'+response['mode'])
                    if c.get('not_mode_prefix') and response['mode'].startswith(c['not_mode_prefix']):errors.append('forbidden_mode:'+response['mode'])
                    if c.get('required_source') and not any(c['required_source'] in str(h) for h in response['hits']):errors.append('wrong_source')
                    if c.get('not_category') and c['not_category']==response['category']:errors.append('false_competition_context')
                    if c.get('group')=='ingress_locale' and raw.get('language',{}).get('effective')!='th':errors.append('incorrect_english_locale')
                    if c.get('group')=='true_wrong_layout' and (raw.get('mode')!='input_guard_layout_retype' or 'keyboard_layout_mismatch' not in raw.get('input_quality',{}).get('flags',[])):errors.append('missed_true_layout')
                    if c.get('group')=='english_mixed_locale' and raw.get('language',{}).get('effective')!='en':errors.append('incorrect_thai_locale')
                elif 'required_clauses' in c:errors=check_content_contract(c,response)
                else:errors=check(c,response)
            except Exception as e:response={'error':type(e).__name__+':'+str(e)};errors=['http_or_transport_failure']
            elapsed=time.perf_counter()-t;done+=1;counts[suite]['total']+=1;counts[suite]['passed']+=not errors
            out.write(json.dumps({'suite':suite,'case':c,'response':response,'elapsed':elapsed,'passed':not errors,'failures':errors},ensure_ascii=False)+'\n');out.flush()
            if errors or done%50==0:print(json.dumps({'completed':done,'suite':suite,'id':c['id'],'failures':errors,'elapsed':round(elapsed,3)},ensure_ascii=False),flush=True)
with (r/(run+'_http_summary.json')).open('x',encoding='utf-8') as f:json.dump({'url':base,'by_suite':counts,'elapsed_sec':time.perf_counter()-start,'llm_enabled':True,'runtime':'r30-G5'},f,ensure_ascii=False,indent=2)
print(json.dumps({'completed':done,'by_suite':counts}),flush=True)
