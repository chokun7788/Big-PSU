"""Audit the just-appended replay against exact R132 per-request receipts and saved wire."""
import gzip,json,hashlib,time
from pathlib import Path
root=Path(__file__).resolve().parent;out=root/'paired_source01';parent=root.parent/'r132_flow_repairs_20261025';results=[json.loads(x) for x in (out/'RESULTS.jsonl').read_text('utf8').splitlines()];batch=results[-100:];keys={x['key'] for x in batch};events={};digest=lambda x:hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
for path in sorted((parent/'sample01').glob('RESULTS_*.jsonl.gz')):
 try:
  with gzip.open(path,'rt',encoding='utf8') as f:
   for line in f:
    try:row=json.loads(line)
    except ValueError:break
    if row['key'] in keys:events[row['key']]=[e for e in (row.get('result',{}).get('decision_artifact',{}).get('request_context',{}).get('events',[])) if e.get('stage')=='R129_model_gateway']
 except (EOFError,UnicodeError):pass
raw={};log=root.parent/'r129_full_plan_completion_20261024/model_1792867147669903000/REQUESTS.jsonl'
for line in log.open(encoding='utf8'):
 try:x=json.loads(line)
 except ValueError:continue
 if x.get('started_at',0)<1792937415 or not x.get('transport_ok'):continue
 prov=x.get('provenance') or {};key=(prov.get('stage'),prov.get('effective_profile'),digest(x['input_messages']),digest(x.get('schema')));raw.setdefault(key,[]).append(x)
invalid=[];verified=0
for row in batch:
 for call in row.get('replay_calls',[]):
  if call.get('status')!='verified_actual_raw_reused':continue
  k=(call['stage'],call['profile'],call['messages_sha256'],call['schema_sha256']);prior=[e for e in events.get(row['key'],[]) if (e.get('model_stage'),e.get('profile'),e.get('wire_messages_sha256'),e.get('schema_sha256'))==k and e.get('transport_ok')];matches=[v for v in raw.get(k,[]) if any(v.get('provenance')==e.get('returned_provenance') for e in prior) and v.get('provenance',{}).get('effective_max_new_tokens')==call.get('generation_cap')]
  if not matches or not prior or call.get('new_inference') is not False:invalid.append(row['key'])
  else:verified+=1
report={'batch_rows':len(batch),'existing_total_rows':len(results),'per_request_success_receipt_mismatch_keys':sorted(set(invalid)),'verified_reused_calls':verified,'all_batch_keys_have_parent_record':set(events)==keys,'raw_results_untouched':True,'semantic_review_complete':False,'new_inferences':0,'created_at':time.time()};p=out/('BATCH_337_RECEIPT_AUDIT_'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(p),'verified':verified,'invalid':len(invalid),'parent_keys':report['all_batch_keys_have_parent_record']}));assert not invalid and report['all_batch_keys_have_parent_record']
