import json,sys,time,copy,sqlite3
from pathlib import Path
from datetime import datetime
from unittest.mock import patch
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'system'));sys.path.insert(0,str(W))
from verification_support import snapshot
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
q='นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท'
out=W/('forced_unknown_bounds_'+str(time.time_ns()));out.mkdir()
a=sqlite3.connect((W.parent/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(out/'source.sqlite');a.backup(b);b.close();a.close()
store=CommonStore(out/'source.sqlite');v=DraftSnapshotView(store);rid='migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student';record=copy.deepcopy(v.snapshot()['release']['records'][rid])
for field in ('persons_min','persons_max'):
 record['fields'][field].update(status='unknown',value=None,evidence_refs=[])
save_owner_record(store,record,record['revision'],'isolated-unknown-bounds')
e=Engine.from_snapshot(v.snapshot());u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'test',{'model_called':False});orig=e.plan

def single(category,question,at=None,meaning=None):
 p=orig(category,question,at,meaning)
 candidates=[x for x in p.ids if 'nintendo_switch_60_1_2_psu_alumni_general_student' in x]
 if candidates:p.ids=candidates[:1]
 return p
with patch.object(e,'plan',side_effect=single):r=e.answer(q,'th',at=datetime.fromisoformat('2026-03-16T12:00:00+07:00'),allow_llm=False,understanding=u)
claims=[c for n in r.get('needs',[]) for c in n.get('claims',[])];checks={'unknown_bounds_not_delivered':not any('nintendo_switch_60_1_2_psu_alumni_general_student' in c.get('record_id','') for c in claims)}
(out/'RESULT.json').write_text(json.dumps({'checks':checks,'all_passed':all(checks.values()),'scope':'forced plan, isolated actual owner edit with both bounds unknown; no HTTP or model'},indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'path':str(out),'checks':checks,'answer':r.get('answer')},ensure_ascii=False))
