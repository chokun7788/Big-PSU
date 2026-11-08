import json,sys,time
from pathlib import Path
from datetime import datetime
from unittest.mock import patch
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'system'));sys.path.insert(0,str(W))
from verification_support import snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
q='นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท';e=Engine.from_snapshot(snapshot());u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'test',{'model_called':False});orig=e.plan

def single(category,question,at=None,meaning=None):
 p=orig(category,question,at,meaning)
 candidates=[x for x in p.ids if 'nintendo_switch_60_1_2_psu_alumni_general_student' in x]
 if candidates:p.ids=candidates[:1]
 return p
with patch.object(e,'plan',side_effect=single):r=e.answer(q,'th',at=datetime.fromisoformat('2026-03-16T12:00:00+07:00'),allow_llm=False,understanding=u)
out=W/('forced_single_rate_'+str(time.time_ns()));out.mkdir();claims=[c for n in r.get('needs',[]) for c in n.get('claims',[])];checks={'forced_single_rate_not_delivered':not any('nintendo_switch_60_1_2_psu_alumni_general_student' in c.get('record_id','') for c in claims)}
(out/'RESULT.json').write_text(json.dumps({'checks':checks,'all_passed':all(checks.values()),'scope':'forced plan, actual draft snapshot, no HTTP or model'},indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'path':str(out),'checks':checks,'answer':r.get('answer')},ensure_ascii=False))
