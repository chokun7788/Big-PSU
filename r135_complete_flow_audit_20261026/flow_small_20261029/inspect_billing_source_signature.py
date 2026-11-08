import sys,json
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path('flow_small_20261029/system').resolve()))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow import financial
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
v=DraftSnapshotView(CommonStore(Path('flow_small_20261029/billing_source_scope_1793314435655910700/source.sqlite')));e=Engine.from_snapshot(v.snapshot()); ids=['migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student','migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student','migrated_rate_nintendo_switch_60_1_2_psu_student_staff']; f=[next(f for f in e.index.byid.values() if f['record_id']==rid and f['category']=='C06' and f['facet']=='amount') for rid in ids];groups={financial.value(e.index.records[rid],'audience_id') for rid in (ids[0],ids[2])}
for x in f:
 r=e.index.records[x['record_id']];svc=e.index.records.get(financial.value(r,'service_id'),{});print(json.dumps({'id':x['record_id'],'platform':financial.value(svc,'platform'),'calc':financial.unit_calculation(e.index,x,'1 person and 1 person'),'unit':x.get('billing_unit'),'validity':r.get('validity'),'confirmation':x.get('confirmation_as_of'),'bounds':[financial.value(r,'persons_min'),financial.value(r,'persons_max')]},ensure_ascii=False))
with patch.object(financial,'audience_mentions',return_value=(groups,set())), patch.object(financial,'person_counts',return_value={k:1 for k in groups}):
 x=financial.billing(e.index,'1 person and 1 person',f);print('result',repr(x))
