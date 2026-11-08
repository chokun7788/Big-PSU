"""Paired actual weight-profile comparison on frozen retained questions."""
import collections,hashlib,json,os,statistics,sys,time,traceback,urllib.request
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
D=R/'training_v2'
os.environ.update(OLLAMA_URL='http://127.0.0.1:12921',PSU_CHATBOT_OLLAMA_MODEL='psu-r129:latest',PSU_ESPORTS_NOW='2026-10-24T12:00:00+07:00',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='180')
from app.knowledge.common.domain_flow.graph_protocol import messages,adapt
from app.knowledge.common.domain_flow.understanding import parse,schema
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.context_guard import apply as scope_guard
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.contracts import RequestBudget
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.domain_flow.model_gateway import digest
OUT=R/'three_arm01';OUT.mkdir(exist_ok=False)
def write(n,v):(OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze={str(p.resolve()):sha(p) for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.sqlite-wal','.sqlite-shm'}}
for p in [D/'test.jsonl',R/'compare_planners.py',R/'EVALUATION_PROTOCOL.json',R/'serve_model.py']:freeze[str(p.resolve())]=sha(p)
write('RUN_FREEZE.json',freeze)
jobs=[json.loads(s) for s in (D/'test.jsonl').read_text('utf8').splitlines()];engine=Engine.from_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot())
def slots(ts):return {(i,c['slot'],c['quote'].casefold(),c.get('scope','local' if c['quote'] in t['quote'] else 'shared')) for i,t in enumerate(ts) for c in t['constraints']}
METRICS=['schema_ok','task_count_exact','task_boundary_exact','domain_exact','operation_exact','field_exact','focus_exact','operation_field_exact','target_exact','slot_f1','clarification_exact','shared_edges_exact']
def metric(value,gold,q,validate_wire=True):
 valid=parse(json.dumps(value,ensure_ascii=False),q).accepted if validate_wire else True
 if not valid:return {k:0. if k=='slot_f1' else False for k in METRICS}
 ts=value['tasks'];gs=gold['tasks'];a,b=slots(ts),slots(gs);f1=2*len(a&b)/(len(a)+len(b)) if a or b else 1.
 ops=lambda xs:[(t['domain'],t['operation'],t['facet']) for t in xs]
 targets=lambda xs:[t['target'].casefold() for t in xs]
 edges=lambda p:{(e['source_task_id'],e['target_task_id'],e['slot'],e['quote'].casefold(),e['basis']) for e in p.get('shared_bindings',[])}
 return {'schema_ok':True,'task_count_exact':len(ts)==len(gs),'task_boundary_exact':[t['quote'] for t in ts]==[t['quote'] for t in gs],'domain_exact':[t['domain'] for t in ts]==[t['domain'] for t in gs],'operation_exact':[t['operation'] for t in ts]==[t['operation'] for t in gs],'field_exact':[t['facet'] for t in ts]==[t['facet'] for t in gs],'focus_exact':value.get('focus')==gold['focus'],'operation_field_exact':ops(ts)==ops(gs),'target_exact':targets(ts)==targets(gs),'slot_f1':f1,'clarification_exact':[t['ambiguous'] for t in ts]==[t['ambiguous'] for t in gs],'shared_edges_exact':edges(value)==edges(gold)}
all_rows=[];start=time.time();clock=datetime.fromisoformat('2026-10-24T12:00:00+07:00')
with (OUT/'RESULTS.jsonl').open('x',encoding='utf8') as f:
 for arm in ['base','retained','new']:
  os.environ['PSU_PLANNER_PROFILE']=arm
  for i,x in enumerate(jobs):
   before=time.monotonic();wire=messages(x['question']);sch=schema();row={'arm':arm,'key':x['key'],'question':x['question'],'locale':x['locale'],'family':x['review_family'],'transport_ok':False,'source_fatal_count':0}
   row['raw_metrics']={k:0. if k=='slot_f1' else False for k in METRICS}
   try:
    payload={'model':'psu-r129:latest','stage':'context_understanding','planner_profile':arm,'messages':wire,'format':sch,'stream':False,'think':False,'options':{'temperature':0,'seed':117,'num_ctx':8192,'num_predict':900},'request_timeout_sec':90}
    req=urllib.request.Request('http://127.0.0.1:12921/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=100) as response:raw=json.load(response)
    prov=raw['provenance'];assert raw['model']==payload['model'] and prov['effective_profile']==arm and prov['effective_messages_sha256']==digest(wire) and prov['effective_schema_sha256']==digest(sch)
    row.update(transport_ok=True,identity_verified=True,provenance=prov,raw_output=raw['message']['content'])
    value=json.loads(raw['message']['content']);row['raw_metrics']=metric(value,x['label'],x['question']);u=parse(raw['message']['content'],x['question'])
    row['wire_version']=u.event.get('wire_version');u=review(x['question'],engine.index,u);u=scope_guard(x['question'],engine.index,u)
    if u.accepted:
     after={'tasks':[t.as_dict() for t in u.tasks]};row['compiled_metrics']=metric({'focus':value.get('focus'),'context_quotes':value.get('context_quotes',[]),'tasks':[{k:t[k] for k in ['quote','domain','operation','facet','target','constraints','ambiguous']} for t in after['tasks']]},x['label'],x['question'],validate_wire=False)
    # Same compiled engine and budget for all arms, including identical base
    # selector when interpretation leaves an unresolved source choice.
    with request_context() as ctx:
     ctx.input={'raw_question':x['question']};result=engine.answer(x['question'],x['locale'],at=clock,allow_llm=True,budget=RequestBudget(),understanding=u)
    row['execution']=result;contract=result.get('execution_contract',{});ledgers=contract.get('tasks',[])
    row['source_fatal_count']=sum(len(t.get('fatal',[])) for t in ledgers)
    obs=[o for t in ledgers for o in t.get('obligations',[])];row['typed_obligation_completion']=sum(o.get('fulfilled') is True for o in obs)/len(obs) if obs else None
   except Exception as exc:row.update(error=repr(exc),traceback=traceback.format_exc())
   row['elapsed_sec']=time.monotonic()-before;all_rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
   write('PROGRESS.json',{'phase':'paired_inference','arm':arm,'completed':len(all_rows),'total':len(jobs)*3,'elapsed_sec':time.time()-start,'pid':os.getpid(),'last_key':x['key']})
summary={}
for arm in ['base','retained','new']:
 rs=[r for r in all_rows if r['arm']==arm];lat=sorted(r['elapsed_sec'] for r in rs)
 summary[arm]={'questions':len(rs),'transport_success_rate':sum(r['transport_ok'] for r in rs)/len(rs),'source_fatal_count':sum(r['source_fatal_count'] for r in rs),'latency_p50':statistics.median(lat),'latency_p95':lat[min(len(lat)-1,int(len(lat)*.95))],**{k:sum(r['raw_metrics'][k] for r in rs)/len(rs) for k in rs[0]['raw_metrics']}}
a,b=summary['new'],summary['retained'];gates={'source_fatal_zero':a['source_fatal_count']==0,'operation_noninferior':a['operation_field_exact']>=b['operation_field_exact'],'slot_f1_noninferior':a['slot_f1']>=b['slot_f1'],'transport_noninferior':a['transport_success_rate']>=b['transport_success_rate']}
gates['strict_improvement_required']=a['operation_field_exact']>b['operation_field_exact'] or a['slot_f1']>b['slot_f1']
gates['target_and_clarification_noninferior']=a['target_exact']>=b['target_exact'] and a['clarification_exact']>=b['clarification_exact']
gates['all_identity_receipts_verified']=all(r.get('identity_verified') for r in all_rows)
obligations={arm:[r['typed_obligation_completion'] for r in all_rows if r['arm']==arm and r.get('typed_obligation_completion') is not None] for arm in summary}
means={arm:statistics.mean(v) if v else 0 for arm,v in obligations.items()};gates['typed_obligation_completion_noninferior']=means['new']>=means['retained']
bykey={arm:{r['key']:r for r in all_rows if r['arm']==arm} for arm in summary};paired={};grouped={}
for m in ['operation_field_exact','target_exact','clarification_exact']:
 gains=[k for k in bykey['new'] if bykey['new'][k]['raw_metrics'][m] and not bykey['retained'][k]['raw_metrics'][m]];losses=[k for k in bykey['new'] if not bykey['new'][k]['raw_metrics'][m] and bykey['retained'][k]['raw_metrics'][m]];n=len(jobs);delta=(len(gains)-len(losses))/n;se=max(0,(len(gains)+len(losses))/n-delta*delta)**.5/n**.5
 paired[m]={'gains':gains,'regressions':losses,'paired_difference':delta,'descriptive_normal_95_interval':[max(-1,delta-1.96*se),min(1,delta+1.96*se)],'small_group_intervals_not_causal':True}
for axis in ['domain','locale','operation']:
 buckets=collections.defaultdict(list)
 for job in jobs:
  values={job['locale']} if axis=='locale' else {t[axis] for t in job['label']['tasks']}
  for value in values:buckets[value].append(job['key'])
 grouped[axis]={value:{arm:{'denominator':len(keys),**{m:sum(bykey[arm][k]['raw_metrics'][m] for k in keys)/len(keys) for m in METRICS}} for arm in summary} for value,keys in buckets.items()}
for domain in ['service_fee','reservation','payment','rules','competition_rules']:
 if domain in grouped['domain']:gates['critical_'+domain+'_operation_noninferior']=grouped['domain'][domain]['new']['operation_field_exact']>=grouped['domain'][domain]['retained']['operation_field_exact']
unchanged=all(sha(p)==h for p,h in freeze.items());assert unchanged,'Frozen source changed during paired comparison'
selection='new' if all(gates.values()) else 'retained'
write('SUMMARY.json',{'arms':summary,'promotion_gates':gates,'selected_profile':selection,'typed_obligation_completion_mean':means,'paired_new_vs_retained':paired,'by_category_locale_operation':grouped,'source_unchanged':unchanged,'coverage_keys_identical':all({r['key'] for r in all_rows if r['arm']==arm}=={x['key'] for x in jobs} for arm in summary),'semantic_answer_accuracy':None,'historically_exposed_questions':True,'fresh_holdout':False,'complete':True})
if selection=='new':
 (R/'PLANNER_REVIEW_NEEDED.json').write_text(json.dumps({'paired_results_ready':True,'agent_source_adjudication_required':True,'human_user_approval_required':False,'provisional_profile':'new','production_approvals_untouched':True},indent=2),'utf8')
 while not (R/'PLANNER_ADJUDICATION.json').exists():
  write('PROGRESS.json',{'phase':'paired_results_ready_agent_review_required','pid':os.getpid(),'completed':len(all_rows),'total':len(all_rows),'selected_profile_provisional':'new'});time.sleep(15)
 decision=json.loads((R/'PLANNER_ADJUDICATION.json').read_text('utf8'));assert decision['source_execution_review_complete'] and decision['profile'] in {'new','retained'}
 selection=decision['profile']
 final_summary=json.loads((OUT/'SUMMARY.json').read_text('utf8'));final_summary['selected_profile']=selection;final_summary['agent_adjudication']=decision;write('SUMMARY.json',final_summary)
write('SELECTED_PROFILE.json',{'profile':selection,'reason':'predeclared_noninferiority_gates','new_adapter_promoted':selection=='new','gates':gates})
write('COMPLETE.json',{'complete':True,'rows':len(all_rows),'questions_per_arm':len(jobs),'source_unchanged':True});print(json.dumps(summary))
