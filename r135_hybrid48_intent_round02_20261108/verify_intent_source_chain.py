"""Direct price chain checks using actual captured PC source claims."""
import copy,json,time
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.intent_source_binding import price_chain
folder=R/'pc_assessment_1794228133221331100';row=json.loads((folder/'DETAILS.json').read_text('utf8'))[0]
idx=Engine.from_snapshot(DraftSnapshotView(CommonStore(folder/'source.sqlite')).snapshot()).index
claims=row['claims'];checks={}
proof=price_chain(idx,'C06','PC ราคาเท่าไหร่',claims)
checks['actual_PC_source_chains']=not proof['errors'] and len(proof['chains'])==6
checks['wrong_platform_rejected']='intent_price_requested_platform_mismatch' in price_chain(idx,'C06','PS5 ราคาเท่าไหร่',claims)['errors']
bad=copy.deepcopy(idx);rid=claims[0]['record_id'];bad.records[rid]['fields']['service_id']['value']='missing_service'
checks['missing_service_rejected']='intent_price_source_chain_invalid' in price_chain(bad,'C06','PC ราคาเท่าไหร่',claims)['errors']
bad=copy.deepcopy(claims);bad[0]['evidence_refs']=[r for r in bad[0]['evidence_refs'] if not r['locator'].endswith('/service_id')]
checks['missing_relation_locator_rejected']='intent_price_relation_evidence_missing' in price_chain(idx,'C06','PC ราคาเท่าไหร่',bad)['errors']
checks['other_categories_not_price_bound']=not price_chain(idx,'C05','PC ปุ่มอะไร',[])['applicable']
out=R/('intent_source_chain_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'scope':'bounded direct source price-chain checks, not whole semantic/model/HTTP/authority proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
