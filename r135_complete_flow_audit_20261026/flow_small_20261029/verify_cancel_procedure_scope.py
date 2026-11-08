"""Bounded source-only cancellation intent controls; no HTTP or inference."""
import json,os,sqlite3,time,re
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
o=R/("cancel_procedure_scope_controls_"+str(time.time_ns()));o.mkdir();os.environ["PSU_CONVERSATION_STATE_PATH"]=str(o/"sessions.sqlite")
a=sqlite3.connect((R.parent/"system/data/knowledge/common.sqlite").resolve().as_uri()+"?mode=ro",uri=True);b=sqlite3.connect(o/"source.sqlite");a.backup(b);b.close();a.close(); view=DraftSnapshotView(CommonStore(o/"source.sqlite")); rows=[];checks={}
def run(q):
 with patch("urllib.request.urlopen",side_effect=AssertionError("HTTP forbidden")):
  r=CommonAnswerer(view).answer(q,locale="auto",at="2026-10-16T12:00:00+07:00",planner=None)
 rows.append({"question":q,"answer":r.answer if r else None,"artifact":r.decision_artifact if r else None});return r
def claims(r):return {x.get("record_id") for x in r.decision_artifact.get("domain_flow",{}).get("typed_claims",[])} if r else set()
def disclosed(r):return bool(r and re.search(r"(?:procedure|steps?|method).{0,55}(?:unconfirmed|unavailable|unknown|not (?:confirmed|available))|(?:unconfirmed|unavailable|unknown|not (?:confirmed|available)).{0,55}(?:procedure|steps?|method)|(?:ขั้นตอน|วิธี).{0,55}(?:ไม่ยืนยัน|ยังไม่|ไม่มีข้อมูล)|(?:ยังไม่|ไม่มีข้อมูล).{0,55}(?:ขั้นตอน|วิธี)",r.answer,re.I))
x=run("How do I cancel my booking?");checks["english_procedure_unknown_explicit"]=disclosed(x)
x=run("วิธียกเลิกการจองทำอย่างไร");checks["thai_procedure_unknown_explicit"]=disclosed(x)
x=run("ยกเลิกการจองอย่างไร และราคา PC เท่าไหร่");checks["compound_retains_price_and_procedure_disclosure"]=bool(disclosed(x) and any("rate" in i for i in claims(x)))
x=run("ต้องยกเลิกการจองล่วงหน้ากี่ชั่วโมง");checks["deadline_only_retains_policy"]=bool(x and any("cancel" in i for i in claims(x)) and not disclosed(x))
x=run("How can I change my booking time?");checks["change_time_retains_scoped_procedure"]=bool(x and "procedure_change_time" in claims(x) and "email" in x.answer.lower())
x=run("How do I book a PC?");checks["booking_remains_separate"]=bool(x and any("booking" in i for i in claims(x)) and "procedure_change_time" not in claims(x))
report={"checks":checks,"all_passed":all(checks.values()),"http_attempted":False,"model_called":False,"scope":"baseline focused observations; no assertion of source absence or authority; further source edit and forgery controls required"};(o/"DETAILS.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n",encoding="utf8");(o/"RESULT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8");print(json.dumps({"path":str(o),**report}));assert report["all_passed"]
