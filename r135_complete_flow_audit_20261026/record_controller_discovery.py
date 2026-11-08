"""Preserve a new source-scope audit finding without pretending it is repaired."""
import hashlib,json,time
from pathlib import Path
R=Path(__file__).resolve().parent;B=R/'controller_catalog_audit_1793051119685377500'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n','utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=read(B/'DETAILS.json');source=read(B/'SOURCE_FIELD_AUDIT.json');first=rows[0];other=rows[1];claims=first['artifact']['domain_flow']['typed_claims']
assert first['question']=='เกมที่ใช้จอย PS5 มีอะไร' and other['question']=='เกมบนเครื่อง PS5 มีอะไร'
assert claims and [(x['record_id'],x['facet']) for x in claims]==[(x['record_id'],x['facet']) for x in other['artifact']['domain_flow']['typed_claims']]
assert first['artifact']['response_type']=='partial_answer' and '**คำตอบที่ยืนยัน**' in first['answer']
assert len(source['records'])==43 and all(x['input_device']=='unknown' and x['model_fields']==['input_device'] for x in source['records'])
report={'complete':False,'implementation_gap_confirmed':True,'case':'controller-specific game catalog was answered from a console catalog','baseline':{'path':str((B/'DETAILS.json').relative_to(R)),'sha256':sha(B/'DETAILS.json')},'source_field_audit':{'path':str((B/'SOURCE_FIELD_AUDIT.json').relative_to(R)),'sha256':sha(B/'SOURCE_FIELD_AUDIT.json')},'delivered_record_ids':[x['record_id'] for x in claims],'source_scope':'All43 retained control_set.input_device fields are unknown; schema models only device class, not an exact controller model. Console offering is not independent proof of controller compatibility.','internal_state':'partial_answer/unaccepted_wire_compatibility with unrecognised factual predicate, no observed controller constraint','customer_delivery_gap':'Confirmed-answer prefix displays the console game list without an explicit controller-compatibility limitation.','no_claim_games_are_unplayable':True,'semantic_accuracy_benchmark':False,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'next':'Implement source-bound device/controller scope, independent delivered-receipt checks and positive/negative controls; keep source unknown distinct from unsupported interpretation. Preserve console catalog control. Do not fabricate compatibility or merely relabel a partial result.'};write(B/'FINDING.json',report)
gaps=read(R/'AUDIT_GAPS.json');gid='G106';g=next((g for g in gaps['gaps'] if g['id']==gid),None)
if g is None:
 g={'id':gid,'requirements':['C04','CONTRACT-05','CONTRACT-09','CONTRACT-11'],'finding':'The actual normal Common request เกมที่ใช้จอย PS5 มีอะไร returns the same PS5-console game FAQ as เกมบนเครื่อง PS5 มีอะไร. The result is internally partial but its customer text says confirmed without identifying the unverified controller constraint. All43 retained control sets have input_device unknown; console/platform is not an independent controller compatibility proof.','code':'system/app/knowledge/common/domain_flow/request_verifier.py;source_decisions.py;game_scope.py;dialogue_task.py;typed/compatibility catalog paths'};gaps['gaps'].append(g)
g.update(state='identified_pending_source_bound_controller_scope_and_delivery_fix',evidence={'path':str((B/'FINDING.json').relative_to(R)),'sha256':sha(B/'FINDING.json'),'passed':False,'scope':'actual source/read/customer-delivery audit, no model or provider HTTP; source unknown alone is not the implementation failure'},remaining=report['next'])
gaps['last_recorded_at']=time.time();write(R/'AUDIT_GAPS.json',gaps)
ledger=read(R/'COMPLETION_LEDGER.json')
for x in ledger['requirements']:
 if x['id'] in g['requirements']:
  if gid not in x['gaps']:x['gaps'].append(gid)
  x.update(implementation_state='implementation_gap_open',behavior_acceptance_state='not_closed_open_gap');x.setdefault('diagnostic_evidence',[]).append(g['evidence'])
write(R/'COMPLETION_LEDGER.json',ledger);print(json.dumps({'new_gap':gid,'state':g['state'],'baseline':str(B.relative_to(R)),'whole_flow_complete':False}))
