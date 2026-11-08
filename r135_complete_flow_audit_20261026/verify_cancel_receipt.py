import copy,json,sqlite3,time
from verification_support import R
from app.knowledge.common.domain_flow.task_execution import _cancel_procedure_receipt_matches as verify
D=R/"cancel_future_source_controls_1793222909000077800";a=json.loads((D/"RESULT.json").read_text(encoding="utf8"))["artifact"];receipt=a["execution_contract"]["tasks"][0]["receipts"][0];claims=a["domain_flow"]["typed_claims"]
c=sqlite3.connect((D/"source.sqlite").resolve().as_uri()+"?mode=ro",uri=True);c.row_factory=sqlite3.Row;row=c.execute("SELECT r.payload FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.record_id=? AND r.version=h.head",("procedure_change_time",)).fetchone();record=json.loads(row[0]);c.close()
checks={"actual_receipt":verify(record,receipt,claims)}
def mutation(name,fn):
 x=copy.deepcopy(receipt);fn(x);checks[name]=not verify(record,x,claims)
mutation("wrong_revision",lambda x:x.__setitem__("record_revision",x["record_revision"]+1))
mutation("forged_steps_source",lambda x:[r.__setitem__("source_id","FORGED") for r in x["evidence_refs"] if r["locator"].endswith("/steps")])
mutation("forged_topic_source",lambda x:[r.__setitem__("source_id","FORGED") for r in x["evidence_refs"] if r["locator"].endswith("/topic")])
mutation("wrong_action",lambda x:x["requested_scope"]["policy_action"].__setitem__("source_actions",["studio_cancel"]))
mutation("unverified_scope",lambda x:x["requested_scope"].__setitem__("verified",False))
mutation("wrong_fact",lambda x:x.__setitem__("fact_id","forged"))
mutation("wrong_validation",lambda x:x.__setitem__("value_validation","unchecked"))
checks["missing_claim"]=not verify(record,receipt,[])
o=R/("cancel_receipt_controls_"+str(time.time_ns()));o.mkdir();report={"checks":checks,"all_passed":all(checks.values()),"basis":"actual isolated-owner record and delivered receipt; mutated in memory","limitations":"field refs and scope are bounded checks, not semantic entailment"};(o/"RESULT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8");print(json.dumps({"path":str(o),**report}));assert report["all_passed"]
