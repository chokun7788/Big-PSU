import hashlib,json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
paths=['reports/master_ground_truth_eval/master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl','review_ui/intent_trap_400_template.html']
results=[]
for rel in paths:
 p=ROOT/rel;dest=B/'system'/rel
 if p.exists() and not dest.exists():dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 results.append({'path':rel,'original_exists':p.exists(),'stage_exists':dest.exists(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None,'use':'reference-fixture-dependent unit tests; NOT a current answer result'})
(B/'REFERENCE_FIXTURE_REPAIR.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(results,ensure_ascii=False))
