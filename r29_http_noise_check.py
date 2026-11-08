import json,time,sys,urllib.request,uuid
from pathlib import Path
root=Path(__file__).parent;report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
base='http://127.0.0.1:'+sys.argv[1];run=sys.argv[2]
health=json.load(urllib.request.urlopen(base+'/health',timeout=5))
assert health['runtime']['version']=='2026.10.02-input-context-r29-verified'
fixtures=json.loads((report/'blocked36_fixture.json').read_text(encoding='utf-8'))['cases']
reference={r['id']:r for r in map(json.loads,(report/'pipeline31_C_details.jsonl').read_text(encoding='utf-8').splitlines())}
records=[]
with (report/(run+'_details.jsonl')).open('x',encoding='utf-8') as out:
    for c in fixtures:
        payload={'question':c['question'],'locale':c['locale'],'recent_history':[],
                 'client_session_id':'r29-'+uuid.uuid4().hex,'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
        start=time.perf_counter()
        response=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30))
        elapsed=time.perf_counter()-start;answer=response.get('answer') or '';mode=response.get('mode') or '';errors=[]
        blocked='input_quality' in mode or 'keyboard_layout' in mode or mode=='input_guard_layout_retype'
        if blocked!=c['expected_blocked']:errors.append('wrong_guard_outcome:'+mode)
        scope='guard_only'
        if not c['expected_blocked']:
            old=reference[c['id']]['noisy'];expected=old['answer'];scope='static_answer_reference_parity'
            if 'live_booking' in old['mode']:
                scope='live_transport_and_path_only_no_real_oracle'
                if 'live_booking' not in mode:errors.append('wrong_live_path:'+mode)
                if response.get('route_category')!='schedule':errors.append('wrong_live_route')
            elif c['id']=='MASTER-GT-TH-04585':
                scope='published_name_role_and_conditional_suggestion'
                for term in ('หากหมายถึง ผศ.ดร.ณัฐพงศ์ ทองเทพ','ผู้ช่วยอธิการบดีฝ่ายวิชาการ','https://esports.phuket.psu.ac.th/about-us/Members'):
                    if term not in answer:errors.append('missing_source_fact:'+term)
            elif c['id']=='MASTER-GT-TH-03100':
                scope='published_controls_and_secondary_source_note'
                for line in expected.splitlines()[1:]:
                    if line and line not in answer:errors.append('missing_complete_control_or_review_note:'+line)
            elif c['id']=='MASTER-GT-EN-03708':
                # The live profile enables semantic/LLM recovery. Compare its
                # clean counterpart, not an LLM-disabled direct reference.
                probe=json.loads((report/'http_safe_unknown_clean_probe.json').read_text(encoding='utf-8'))
                clean_response=probe['clean_response']
                scope='live_clean_noisy_parity_safe_unknown_explanation_issue_retained'
                if answer!=clean_response['answer'] or mode!=clean_response['mode']:
                    errors.append('live_clean_noisy_outcome_differs')
                if mode not in ('pipeline:missing_english_localization','pipeline:english_no_answer'):
                    errors.append('unsafe_policy_assertion')
            elif answer!=expected:errors.append('answer_differs_from_verified_direct_reference')
        if response.get('validation_ok') is False:errors.append('validation_rejected')
        record={'id':c['id'],'question':c['question'],'scope':scope,'elapsed_sec':elapsed,'failures':errors,'response':response}
        records.append(record);out.write(json.dumps(record,ensure_ascii=False)+'\n');out.flush()
        print(json.dumps({'id':c['id'],'mode':mode,'failures':errors,'elapsed_sec':round(elapsed,3)},ensure_ascii=False),flush=True)
summary={'total':len(records),'passed':sum(not r['failures'] for r in records),'health':health,
         'static_answer_checks':sum('live_transport' not in r['scope'] and r['scope']!='guard_only' for r in records),
         'real_live_correctness_not_tested':sum('live_transport' in r['scope'] for r in records),
         'true_layout_controls':sum(r['scope']=='guard_only' for r in records)}
with (report/(run+'_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False));sys.exit(summary['passed']!=summary['total'])
