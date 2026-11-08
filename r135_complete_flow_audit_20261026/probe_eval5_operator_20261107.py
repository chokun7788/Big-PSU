"""Paired score follow-up: source-only observations, not semantic grading."""
import json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
o=R/('eval5_operator_probe_'+str(time.time_ns()));o.mkdir()
src=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
dst=sqlite3.connect(o/'source.sqlite');src.backup(dst);dst.close();src.close()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(o/'sessions.sqlite')
v=DraftSnapshotView(CommonStore(o/'source.sqlite'));rows=[]
for q in ['Who operates PSU Esports Studio? Could you check this for me','Who operates PSU Esports Studio?','What is the studio contact email?']:
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):
  a=CommonAnswerer(v).answer(q,locale='en',at='2026-10-31T12:00:00+07:00',planner=None)
 rows.append({'question':q,'answer':a.answer if a else None,'artifact':a.decision_artifact if a else None})
(o/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),'answers':[r['answer'] for r in rows]},ensure_ascii=False))
