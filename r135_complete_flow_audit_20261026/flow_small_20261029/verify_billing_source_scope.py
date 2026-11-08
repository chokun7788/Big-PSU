"""Exercise billing selection against actual edits to an isolated source copy."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow import financial
from app.knowledge.common.domain_flow.contracts import Plan
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
o=R/('billing_source_scope_'+str(time.time_ns()));o.mkdir()
src=sqlite3.connect((R.parent/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
dst=sqlite3.connect(o/'source.sqlite');src.backup(dst);dst.close();src.close()
store=CommonStore(o/'source.sqlite');view=DraftSnapshotView(store)
lo='migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student'
hi='migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student'
other='migrated_rate_nintendo_switch_60_1_2_psu_student_staff'
def change(bounds):
    snap=view.snapshot();r=copy.deepcopy(snap['release']['records'][hi]);low=snap['release']['records'][lo]
    for key,value in [('amount_minor',low['fields']['amount_minor']['value']),('persons_min',bounds[0]),('persons_max',bounds[1])]:
        r['fields'][key]['value']=value
    save_owner_record(store,r,r['revision'],'isolated-billing-scope')
def run():
    e=Engine.from_snapshot(view.snapshot())
    facts=[next(f for f in e.index.byid.values() if f['record_id']==rid and f['category']=='C06' and f['facet']=='amount') for rid in (lo,hi,other)]
    groups={financial.value(e.index.records[rid],'audience_id') for rid in (lo,other)}
    with patch.object(financial,'audience_mentions',return_value=(groups,set())), patch.object(financial,'person_counts',return_value={k:1 for k in groups}):
        return financial.billing(e.index,'1 person and 1 person',facts)
# A real owner save invalidates the previous confirmation. Save both records
# so the comparison does not accidentally hinge on one stale confirmation.
original=copy.deepcopy(view.snapshot()['release']['records'][lo])
original['fields']['amount_minor']['value']+=100
save_owner_record(store,original,original['revision'],'isolated-billing-confirmation-reset')
change((3,4));x=run()
checks={'edited_different_bounds_not_collapsed':isinstance(x,Plan) and x.reason=='per_audience_counts_or_service_required'}
change((1,2));x=run()
checks['edited_same_bounds_deduped']=isinstance(x,list) and len(x)==2
report={'checks':checks,'all_passed':all(checks.values()),'scope':'copied owner source edits and forced audience/count binding; not end-to-end billing or authority'}
(o/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),**report}))
assert report['all_passed']
