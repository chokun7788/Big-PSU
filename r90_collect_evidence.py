"""Read-only code/result audit. No chatbot request, model call or data edit."""
import ast,collections,gzip,hashlib,json,re,sqlite3,sys
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;R=B/'r90_full_flow_analysis_20261018';N=B/'r88_full_common_llm_20261017';S=N/'system'
sys.path[:0]=[str(S),str(N)]
from analyze import rows
counts=collections.Counter();reasons=collections.Counter();field_audits=collections.Counter();bindings=collections.Counter();methods=collections.Counter();stage_examples=collections.defaultdict(list);seen=set()
for file,line,row in rows(N/'full01'):
 key=row['key'];assert key not in seen;seen.add(key);result=row.get('result') or {};art=result.get('decision_artifact') or {};plan=art.get('query_plan') or {};method=plan.get('method');response=art.get('response_type');methods[str(method)]+=1;counts['requests']+=1
 if method=='exact':counts['exact_entity_requests']+=1
 if 'clarification' in result.get('mode','') or response=='clarification':counts['clarification_requests']+=1
 if plan.get('record_ids') and not plan.get('requested_fields'):counts['selected_entity_without_requested_fields']+=1
 if plan.get('semantic_review_needed'):counts['semantic_review_needed']+=1
 if plan.get('semantic_plan_accepted'):counts['semantic_plan_accepted']+=1
 if method=='exact' and (not plan.get('requested_fields')):counts['exact_entity_but_no_fields']+=1
 if art.get('rejected_candidate'):counts['rejected_candidate_returned_as_safe_response']+=1
 if result.get('confidence')==.8:counts['fixed_point_eight_confidence']+=1
 if art.get('confidence_calibrated') is False or plan.get('confidence_calibrated') is False:counts['explicit_uncalibrated_confidence']+=1
 selector=plan.get('entity_selection') or {}
 if selector.get('reason'):reasons[selector['reason']]+=1
 if selector.get('attempted'):counts['entity_selector_request_attempted']+=1
 if selector.get('transport_ok'):counts['entity_selector_transport_ok']+=1
 if selector.get('schema_accepted'):counts['entity_selector_schema_accepted']+=1
 if selector.get('semantic_selection_accepted') is False:counts['entity_selector_semantic_binding_rejected']+=1
 for audit in art.get('planner_audits') or []:
  for k in ['attempted','transport_ok','schema_accepted','final_plan_accepted']:
   if audit.get(k) is True:field_audits[k]+=1
  sem=audit.get('semantic') or {}
  if sem.get('semantic_status'):field_audits['semantic:'+sem['semantic_status']]+=1
  if audit.get('gate_reason'):field_audits['gate:'+str(audit['gate_reason'])]+=1
  if audit.get('schema_accepted') is True and audit.get('final_plan_accepted') is False:field_audits['schema_pass_but_final_rejected']+=1
  if len(stage_examples[sem.get('semantic_status','none')])<3 and sem.get('semantic_status'):
   stage_examples[sem['semantic_status']].append({'key':key,'question':row['question'],'answer':result.get('answer'),'audit':audit,'query_plan':plan,'file':file,'line':line})
 for event in art.get('query_resolution') or []:
  if event.get('stage'):bindings['stage:'+str(event['stage'])]+=1
assert len(seen)==20554
# Read current data without calling answer(), planner, approval or publication.
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import value,CATALOG
snap=MigratedView(S/'data/knowledge/common.sqlite').snapshot();records=snap['release']['records'];kinds=collections.Counter(r['kind'] for r in records.values());localization=collections.Counter();field_status=collections.Counter();validity=collections.Counter();missing=[];thai_in_en=[]
def localized(v,path):
 if isinstance(v,dict):
  if 'th' in v and isinstance(v.get('th'),str) and v.get('th'):
   if not isinstance(v.get('en'),str) or not v.get('en'):missing.append(path)
   elif re.search(r'[\u0e00-\u0e7f]',v['en']):thai_in_en.append(path)
  for k,x in v.items():localized(x,path+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):localized(x,path+'/'+str(i))
for rid,r in records.items():
 localization[r.get('localization',{}).get('en_status','unset')]+=1;validity[r['validity']['state']]+=1
 for k,f in r['fields'].items():
  field_status[f['status']]+=1
  if f['status']=='known':localized(f['value'],rid+'/'+k)
# Symbol citations for all actual pipeline stages.
source_refs={}
for mode,root in [('legacy',B/'r64_full_comparison_20261013/system'),('common',S)]:
 for rel in ['app/web_api/server.py','app/pipeline/engine.py','app/pipeline/preprocess.py','app/pipeline/capability_registry.py','app/pipeline/llm_tool_router.py','app/pipeline/universal_intent.py','app/pipeline/structured.py','app/pipeline/retrieval.py','app/booking/live_status.py','app/booking/wordpress_status.py','app/session/conversation_plan.py','app/session/context_resolver.py','app/knowledge/common/owner_server.py','app/knowledge/common/store.py','app/knowledge/common/query_scope.py','app/knowledge/common/answer.py','app/knowledge/common/planner.py','app/knowledge/common/entity_search.py','app/knowledge/common/profile_confirmation.py','app/pipeline/migrated_chat.py','app/knowledge/common/rental_bridge.py','app/knowledge/common/competition_bridge.py','app/knowledge/common/legacy_intent_bridge.py','app/knowledge/common/registry.py','app/knowledge/common/migrated_view.py']:
  p=root/rel
  if not p.exists():continue
  tree=ast.parse(p.read_text('utf-8-sig'));source_refs[mode+':'+rel]={'path':str(p),'symbols':{n.name:n.lineno for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.ClassDef))}}
oldp=B/'r65_detailed_failure_analysis_20261014/evidence.sqlite';old=sqlite3.connect(oldp.resolve().as_uri()+'?mode=ro',uri=True);legacy_reasons=collections.Counter();exceptions={str(e):n for e,n in old.execute("SELECT exception,count(*) FROM results WHERE arm='legacy_llm' AND exception IS NOT NULL GROUP BY exception")}
for payload, in old.execute("SELECT reasons_json FROM grades WHERE arm='legacy_llm' AND passed=0"):
 for reason in json.loads(payload):legacy_reasons[str(reason)]+=1
def esc(x):return str(x).replace('|','/').replace('\r',' ').replace('\n',' ')
newdb=sqlite3.connect((N/'FAILURE_EVIDENCE.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
for filename,query,con,caption in [
 ('COMMON_FAILURE_INDEX_ALL.md','SELECT key,locale,diagnostic,question,failed_grade_count FROM request_failures ORDER BY diagnostic,key',newdb,'R88 ทุก request ที่ไม่ผ่านอย่างน้อยหนึ่งเกณฑ์ กลุ่ม diagnosis เป็นสมมติฐานอัตโนมัติ ไม่เท่ากับคำตอบผิดสาระทุกข้อ'),
 ('LEGACY_FAILURE_INDEX_ALL.md',"SELECT r.key,r.locale,CASE WHEN r.exception IS NOT NULL THEN 'execution_exception' ELSE r.mode END,r.question,count(*) FROM results r JOIN grades g ON r.arm=g.arm AND r.key=g.key WHERE r.arm='legacy_llm' AND g.passed=0 GROUP BY r.key ORDER BY r.key",old,'R64 legacy ON ทุก request ที่ไม่ผ่านอย่างน้อยหนึ่งเกณฑ์จากผลเดิม ไม่ได้รันทดสอบใหม่')]:
 total=0
 with (R/filename).open('x',encoding='utf8') as f:
  f.write('# ดัชนีคำถามที่ไม่ผ่านทั้งหมด\n\n'+caption+'\n\nkey ใช้ค้นใน SQLite/raw logs ที่ระบุใน README; จำนวนเกณฑ์ไม่ใช่จำนวนคำถามไม่ซ้ำ\n\n| key | locale | กลุ่ม/เส้นทาง | คำถามเต็ม | เกณฑ์ไม่ผ่าน |\n|---|---|---|---|---:|\n')
  for row in con.execute(query):f.write('| '+' | '.join(esc(v) for v in row)+' |\n');total+=1
  f.write('\nรวม '+str(total)+' requests\n')
 counts[filename+'_rows']=total
new_reasons=json.loads((N/'FAILURE_COUNTS_FINAL.json').read_text('utf8'))
with (R/'ALL_FAILURE_REASON_TYPES.md').open('x',encoding='utf8') as f:
 f.write('# เหตุไม่ผ่านทุกชนิดจาก logs\n\nเป็น literal reason ที่ evaluator บันทึก ไม่ใช่ root cause ทุกข้อความ เหตุเดียวเกิดได้หลายเกณฑ์ในคำถามเดียว\n\n## ใหม่ R88 common ON\n\n| เหตุ | Grade events |\n|---|---:|\n')
 for reason,n in new_reasons:f.write('| '+esc(reason)+' | '+str(n)+' |\n')
 f.write('\n## เดิม R64 legacy ON\n\n| เหตุ | Grade events |\n|---|---:|\n')
 for reason,n in legacy_reasons.most_common():f.write('| '+esc(reason)+' | '+str(n)+' |\n')
old.close();newdb.close()
result={'observed_at_utc':datetime.now(timezone.utc).isoformat(),'chatbot_requests_executed':0,'model_calls_made':0,'code_data_approval_log_modified':False,'pipeline_counts':counts,'methods':methods,'entity_selector_reasons_on_final_plan':reasons,'field_planner_audit_events':field_audits,'resolution_stages':bindings,'data_inventory':{'records':len(records),'by_kind':kinds,'known_field_statuses':field_status,'localization_status_by_record':localization,'validity_status_by_record':validity,'known_localized_objects_with_th_but_missing_en_count':len(missing),'missing_en_paths':missing,'localized_en_objects_containing_thai_count':len(thai_in_en),'en_thai_paths':thai_in_en,'scanner_note':'Known nested objects with a nonempty th string; unknown fields not treated as missing translation. Thai in en is a review flag, not automatic translation failure.'},'legacy_exception_types':exceptions,'legacy_failure_reason_types':len(legacy_reasons),'common_failure_reason_types':len(new_reasons),'planner_examples':stage_examples}
with (R/'DETAILED_METRICS.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
with (R/'SOURCE_REFERENCES.json').open('x',encoding='utf8') as f:json.dump(source_refs,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k not in {'planner_examples','data_inventory','legacy_exception_types'}},ensure_ascii=False))
print(json.dumps({k:v for k,v in result['data_inventory'].items() if not k.endswith('_paths')},ensure_ascii=False))
print(json.dumps(exceptions,ensure_ascii=False))
