"""Renderer controls using captured source-backed PC rate claims."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.customer_render import render
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
folder=R/'pc_assessment_1794228133221331100'
row=json.loads((folder/'DETAILS.json').read_text('utf8'))[0]
idx=Engine.from_snapshot(DraftSnapshotView(CommonStore(folder/'source.sqlite')).snapshot()).index
claims=row['claims'];facts=[idx.byid[c['fact_id']] for c in claims];computations=row['computations']
def show(index,selected,cs,lang='th'):
 return '\n'.join(render(index,'C06','PC ราคาเท่าไหร่',lang,selected,cs,computations,{},[]))
answer=show(idx,facts,claims);checks={'different_services_displayed':'PC #01-#02' in answer and 'PC #03-#10' in answer,'six_source_citations_retained':all('[S'+str(i)+']' in answer for i in range(1,7))}
checks['english_labels_from_source']='PC #01-#02' in show(idx,facts,claims,'en') and 'PC #03-#10' in show(idx,facts,claims,'en')
single=show(idx,facts[:3],claims[:3]);checks['single_service_keeps_platform_label']='PC #01-#02' not in single and '**PC /' in single
changed=copy.deepcopy(idx);changed.records['availability_pc_01_02']['fields']['name']['value']={'th':'เครื่องทดสอบ A','en':'Fixture A'}
checks['edited_source_name_used']='เครื่องทดสอบ A' in show(changed,facts,claims)
changed.records['availability_pc_01_02']['fields']['name']['status']='unknown'
checks['unknown_source_name_not_invented']='เครื่องทดสอบ A' not in show(changed,facts,claims)
out=R/('pc_service_labels_'+str(time.time_ns()));out.mkdir();report={'checks':checks,'all_passed':all(checks.values()),'scope':'source-index mutation and renderer only; not owner edit, model, HTTP, or authority','model_calls':0}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
