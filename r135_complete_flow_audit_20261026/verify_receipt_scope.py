import copy,json,time
from types import SimpleNamespace
from verification_support import R,index
from app.knowledge.common.domain_flow.receipt_scope import check
from app.knowledge.common.domain_flow.projection import value,title
idx=index();checks={};details=[]
def task(cat,text=''):return SimpleNamespace(category=cat,target_span=SimpleNamespace(text=text) if text else None)
people={f['record_id']:f for f in idx.bycat['C02'] if idx.records[f['record_id']]['kind']=='person'}
a,b=list(people.values())[:2];target=title(idx.records[a['record_id']])['en'];t=task('C02',target)
checks['right_person_allowed']=check(idx,t,a,target)['verified']
wrong=check(idx,t,b,target);checks['same_category_wrong_person_rejected']='source_receipt_bound_target_mismatch' in wrong['errors'];details.append(wrong)
service=next(f for f in idx.bycat['C03'] if idx.records[f['record_id']]['kind']=='service')
checks['legitimate_service_capacity_source_kind']=check(idx,task('C03'),service,'capacity')['verified']
forged=copy.deepcopy(a);idx.records['forged']={'kind':'rate'};forged['record_id']='forged'
checks['wrong_kind_rejected']='source_receipt_kind_outside_executor_contract' in check(idx,task('C02'),forged,'role')['errors']
rate=next(f for f in idx.bycat['C06'] if f['facet']=='amount' and value(idx.records[f['record_id']],'audience_id'))
audience=value(idx.records[rate['record_id']],'audience_id');label=title(idx.records[audience])['en'];q='not '+label
checks['negative_audience_rejects_rate']='source_receipt_audience_scope_mismatch' in check(idx,task('C06'),rate,q)['errors']
gid=next(rid for rid,r in idx.records.items() if r['kind']=='game' and idx.bind('C04',title(r)['en']))
# The real frozen owner source has no game_mode rows: a controlled in-memory
# relation tests implementation without pretending missing business data exists.
mode={'record_id':'fixture_mode','game_id':gid};idx.records['fixture_mode']={'kind':'game_mode'};idx.bycat['C04'].append(mode)
game=title(idx.records[gid])['en'];checks['typed_game_mode_relation_allowed']=check(idx,task('C04',game),mode,game)['verified']
rules=[f for f in idx.bycat['C13'] if f.get('game_id') in idx.records]
one=rules[0];other=next(f for f in rules if f['game_id']!=one['game_id']);q=title(idx.records[one['game_id']])['en']+' tournament rules'
checks['cross_game_rule_rejected']='source_receipt_game_scope_mismatch' in check(idx,task('C13'),other,q)['errors']
checks['same_game_rule_allowed']=check(idx,task('C13'),one,q)['verified']
report={'all_passed':all(checks.values()),'checks':checks,'details':details,'actual_inferences':0,'real_source_changes':0};out=R/('receipt_scope_verification_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
