"""Isolated source-only baseline for the reduced center/price/booking flow."""
import json, os, sqlite3, sys, time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(Path(__file__).parent/'system'))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
out=Path(__file__).parent/('baseline_'+str(time.time_ns()));out.mkdir()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite')
src=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
dst=sqlite3.connect(out/'source.sqlite');src.backup(dst);dst.close();src.close()
view=DraftSnapshotView(CommonStore(out/'source.sqlite'))
questions=['นักศึกษาต่างมหาลัย 4 คนเล่น Nintendo Switch เครื่องเดียว 1 ชั่วโมง ราคาเท่าไหร่','นักศึกษาต่างมหาลัย 4 คนแบ่งเป็น 2 เครื่อง เครื่องละ 2 คน เล่น Nintendo Switch 1 ชั่วโมง ราคาเท่าไหร่','What is the price for four people playing Nintendo Switch for one hour?','ราคา PC เท่าไหร่ และจองอย่างไร']
results=[]
for q in questions:
 try:
  with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):
   r=CommonAnswerer(view).answer(q,locale='auto',at='2026-10-29T17:30:00+07:00',planner=None)
  results.append({'question':q,'answer':r.answer if r else None,'decision_artifact':r.decision_artifact if r else None})
 except Exception as e:results.append({'question':q,'error':repr(e)})
(out/'DETAILS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'output':str(out),'questions':len(results),'errors':sum('error' in x for x in results),'scope':'observations only; no model or HTTP; no semantic acceptance'},ensure_ascii=False))
