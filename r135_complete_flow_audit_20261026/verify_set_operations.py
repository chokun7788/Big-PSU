import copy,json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.collection_scopes import rules,policies
from app.knowledge.common.domain_flow.collection_contract import verify
from app.knowledge.common.domain_flow.capabilities import resolve,matrix
from app.knowledge.common.domain_flow.projection import value,title
e=Engine.from_snapshot(snapshot());idx=e.index;at=reference_time('2026-10-26T12:00:00+07:00');checks={};rows=[]
def run(q,cat,op,facet):
 domain={'C03':'equipment','C04':'games','C10':'rules','C13':'competition_rules'}[cat];u=Understanding([MeaningTask(q,domain,cat,op,facet)],True,'controlled_operation',{'model_called':False})
 r=e.answer(q,'en',at=at,allow_llm=False,understanding=u);rows.append({'question':q,'result':r});return r
r=run('Group recorded games by zone','C04','group_list','zone')
checks['zone_group_list_reads_actual_source_relations']=bool(r['claims']) and r['needs'][0]['plan']['metadata'].get('grouping_kind')=='zone'
checks['zone_group_list_does_not_claim_world_complete']=r['status']=='partial' and not r['needs'][0]['execution_contract']['collection_proof']['verified']
r=run('Count recorded games grouped by zone','C04','group_count','zone');need=r['needs'][0];proof=need['execution_contract']['collection_proof']
expected={}
for claim in need['claims']:
 for zid in idx.byid[claim['fact_id']].get('zone_ids',[]):expected.setdefault(zid,set()).add(claim['record_id'])
checks['zone_counts_recomputed_from_distinct_members']=proof['group_membership_verified'] and all(c['result_count']==len(expected[c['group']]) for c in need['executor_result']['calculation_receipts']) and bool(need['executor_result']['calculation_receipts'])
bad=copy.deepcopy(need);bad['plan']['metadata']['group_member_ids']={'invented_zone':['invented_game']};task=r['execution_contract']['request_plan']['tasks'][0]
from types import SimpleNamespace
t=SimpleNamespace(category='C04',facet='zone',source_span=SimpleNamespace(text='Count recorded games grouped by zone'),target_span=None)
checks['invented_group_membership_not_proof']=verify(idx,t,bad)['group_membership_verified'] is False
r=run('PC and PS5 count recorded games by platform','C04','group_count','game_catalog');need=r['needs'][0];proof=need['execution_contract']['collection_proof'];expected={}
for c in need['claims']:
 f=idx.byid[c['fact_id']];key=str(value(idx.records.get(f['record_id'],{}),'platform') or f['subject']['en']);expected.setdefault(key,set()).update(f.get('member_ids',[]))
checks['catalog_group_counts_union_members_across_services']=proof['group_membership_verified'] and proof['groups']=={key:sorted(ids) for key,ids in expected.items()}
checks['catalog_counts_remain_recorded_subset']=proof['kind']=='confirmed_subset' and all(c['scope']=='confirmed_subset' for c in need['executor_result']['calculation_receipts'])
r=run('List all recorded studio policies','C10','list','owner_policy')
checks['policy_list_not_top_k']={c['fact_id'] for c in r['claims']}=={f['id'] for f in policies(idx,'List all recorded studio policies')}
checks['policy_conditions_not_silently_complete']=r['status']=='partial' and 'conditions' in r['answer'].casefold()
event=next(f for f in idx.bycat['C13'] if f.get('event_id') and f.get('game_id'));q='List all recorded rules for '+event['subject']['en'];r=run(q,'C13','list','rule_clause')
checks['rule_list_all_bound_source_entries']={c['fact_id'] for c in r['claims']}=={f['id'] for f in rules(idx,q)} and bool(r['claims'])
checks['rule_list_has_collection_receipts']=r['needs'][0]['execution_contract']['collection_proof']['verified']
checks['unsupported_operation_never_becomes_detail']=resolve('C03','recommendation','specifications')['status']=='unsupported_operation'
checks['scalar_field_not_advertised_as_list']=resolve('C03','list','specifications')['status']=='unsupported_operation'
checks['matrix_fourteen_actual_dispatch_groups']=len(matrix())==14 and all(row['executor']=='capabilities.dispatch' for cat in matrix() for row in cat['adapter_rows'])
out=R/('set_operations_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_source_changes':0};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
