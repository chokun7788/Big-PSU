"""Source-bound CS2 map-selection controls; no model calls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('nonstudent_audience_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def claims(r):return {c['record_id'] for c in r.decision_artifact.get('domain_flow',{}).get('typed_claims',[])} if r else set()



x=run("Can a non-student access the Cockpit?");checks["ambiguous_nonstudent_not_classified_external"]=not bool(x and "external visitors:" in x.answer.lower())
x=run("Can a PSU staff member who is not a student access the Cockpit?");checks["staff_audience_not_personnel_directory"]=not bool(x and any(c.startswith("member_") for c in claims(x)))
x=run("Can an external visitor access the Cockpit?");checks["explicit_external_visitor_policy_preserved"]=bool(x and "r114_q037_owner_policy" in claims(x))
x=run("Who are the studio staff?");checks["personnel_directory_request_preserved"]=bool(x and any(c.startswith("member_") for c in claims(x)))
x=run("Can a PSU staff member access the Cockpit?");checks["staff_access_without_negation_not_personnel_directory"]=not bool(x and any(c.startswith("member_") for c in claims(x)))
x=run("Can a PSU staff member access the Cockpit, and who are the studio staff?");checks["compound_explicit_directory_retained"]=bool(x and any(c.startswith("member_") for c in claims(x)))
# The directory alone is not evidence that access eligibility was addressed.
checks["compound_access_has_separate_scope_or_disclosure"]=bool(x and any(t in x.answer.lower() for t in ("eligib", "access", "permission", "use the cockpit", "สิทธิ", "เข้าใช้")))
x=run("Can a non-student access the Cockpit, and how much is PC use?");checks["compound_nonstudent_price_preserved"]=bool(x and any(c.startswith("rate_") or "price" in c for c in claims(x)))
report={"checks":checks,"all_passed":all(checks.values()),"scope":"source-only routing and audience scope, no model"};(O/"RESULT.json").write_text(json.dumps(report,indent=2),encoding="utf8");(O/"DETAILS.json").write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(O),**report}));assert report["all_passed"]
