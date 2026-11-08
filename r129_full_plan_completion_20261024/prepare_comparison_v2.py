"""Preserve the invalid pilot; correct only its experimental harness."""
from pathlib import Path
import ast
R=Path(__file__).resolve().parent;s=(R/'compare_planners.py').read_text('utf8')
s=s.replace("OUT=R/'three_arm01'","OUT=R/'three_arm02'")
s=s.replace("all_rows=[];start=time.time();clock=", "cached_transport={}\nprior=R/'three_arm01/RESULTS.jsonl'\nif prior.exists():\n for line in prior.read_text('utf8').splitlines():\n  record=json.loads(line)\n  if record.get('transport_ok') and record.get('identity_verified'):cached_transport[(record['arm'],record['key'])]=record\nall_rows=[];start=time.time();clock=")
begin=s.index("    req=urllib.request.Request('http://127.0.0.1:12921/api/chat'")
end=s.index("    prov=raw['provenance']",begin)
s=s[:begin]+'''    previous=cached_transport.get((arm,x['key']))
    if previous:
     raw={'model':'psu-r129:latest','provenance':previous['provenance'],'message':{'content':previous['raw_output']}}
     row['raw_transport_reused_from']='three_arm01/RESULTS.jsonl';row['planner_elapsed_sec']=previous['elapsed_sec']
    else:
     req=urllib.request.Request('http://127.0.0.1:12921/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
     with urllib.request.urlopen(req,timeout=100) as response:raw=json.load(response)
     row['planner_elapsed_sec']=time.monotonic()-before
'''+s[end:]
old="    value=json.loads(raw['message']['content']);row['raw_metrics']=metric(value,x['label'],x['question']);u=parse(raw['message']['content'],x['question'])"
new="""    try:value=json.loads(raw['message']['content'])
    except (ValueError,TypeError):value={};row['protocol_error']='invalid_json_but_runtime_fallback_still_executed'
    row['raw_metrics']=metric(value,x['label'],x['question']);u=parse(raw['message']['content'],x['question'])"""
assert old in s;s=s.replace(old,new)
s=s.replace("     ctx.input={'raw_question':x['question']};result=engine.answer(x['question'],x['locale'],at=clock,allow_llm=True,budget=RequestBudget(),understanding=u)","     ctx.input={'raw_question':x['question']};ctx.model_calls_reserved=1\n     execution_started=time.monotonic();result=engine.answer(x['question'],x['locale'],at=clock,allow_llm=True,budget=RequestBudget(model_calls=1),understanding=u);row['execution_elapsed_sec']=time.monotonic()-execution_started")
s=s.replace("if obs else None","if obs else 0.")
s=s.replace("row['elapsed_sec']=time.monotonic()-before", "row['elapsed_sec']=row.get('planner_elapsed_sec',time.monotonic()-before)+row.get('execution_elapsed_sec',0.)")
s=s.replace("R/'compare_planners.py'","R/'compare_planners_v2.py'")
# Every completed arm needs source/semantic review before any downstream run,
# including a conservative decision to retain the previous adapter.
s=s.replace("if selection=='new':\n (R/'PLANNER_REVIEW_NEEDED.json')", "if True:\n (R/'PLANNER_REVIEW_NEEDED.json')")
s=s.replace("'provisional_profile':'new'", "'provisional_profile':selection")
s=s.replace("'selected_profile_provisional':'new'", "'selected_profile_provisional':selection")
s=s.replace("'human_user_approval_required':False", "'human_user_approval_required':False,'harness_version':'r129-paired-v2-invalid-wire-fallback-and-shared-budget'")
ast.parse(s);(R/'compare_planners_v2.py').write_text(s,'utf8');print('Prepared corrected paired harness; frozen system and original trial preserved.')
