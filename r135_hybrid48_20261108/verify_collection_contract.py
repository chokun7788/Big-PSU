import copy,json,time
from types import SimpleNamespace
from verification_support import R,index
from app.knowledge.common.domain_flow.collection_contract import verify
i=index();fs=[f for f in i.bycat['C04'] if f['facet']=='game_catalog'];members=sorted({rid for f in fs for rid in f.get('member_ids',[])})
claims=[{'fact_id':f['id'],'record_id':f['record_id']} for f in fs];task=SimpleNamespace(category='C04',facet='game_catalog',target_span=None,source_span=None)
r={'claims':claims,'plan':{'metadata':{'catalog_member_ids':members,'complete_set':False}}};checks={}
p=verify(i,task,r);checks['member_list_does_not_prove_completeness']=p['kind']=='confirmed_subset' and p['verified'] is False
r['plan']['metadata']['complete_set']=True;p=verify(i,task,r);checks['declared_complete_recorded_set_all_members_checked']=p['verified'] and p['scope_verified']
bad=copy.deepcopy(r);bad['claims']=claims[:1];bad['plan']['metadata']['catalog_member_ids']=fs[0].get('member_ids',[]);checks['top_k_cannot_impersonate_whole_source_set']=not verify(i,task,bad)['verified']
bad=copy.deepcopy(r);bad['plan']['metadata']['catalog_member_ids']=['invented_member'];checks['invented_member_identity_rejected']=not verify(i,task,bad)['membership_verified']
from app.knowledge.common.domain_flow.service_calendar import plan
from app.knowledge.common.domain_flow.scope import reference_time
q='What days is play service open weekly?';clock=reference_time('2026-10-26T12:00:00+07:00');p=plan(i,q,clock)
t=SimpleNamespace(category='C11',facet='open_periods',operation='list');r={'claims':[{'fact_id':fid,'record_id':i.byid[fid]['record_id']} for fid in p.ids],'plan':{'metadata':p.metadata}}
checks['actual_requested_recorded_weekday_set_verified']=verify(i,t,r,q,clock)['verified'];r['claims']=r['claims'][:1];checks['weekday_count_metadata_alone_is_not_proof']=not verify(i,t,r,q,clock)['verified']
bad=copy.deepcopy(r);bad['plan']['metadata']={'complete_set':True,'weekday_count':7};checks['old_unscoped_seven_day_marker_not_accepted']=not verify(i,t,bad,q,clock)['verified']
out=R/('collection_verification_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'inferences':0,'source_changes':0,'physical_world_completeness_claimed':False};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(R/'COLLECTION_VERIFICATION_LATEST.json').write_text(json.dumps({'output':str(out),'all_passed':report['all_passed'],'checks':len(checks)},indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
