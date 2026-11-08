"""Honor the owner's deferred topic before C13 executes; retain frozen inputs."""
import copy,hashlib,json
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
rows=[json.loads(x) for x in (R/'main_natural/RESULTS.jsonl').read_text('utf8').splitlines()]
assert not any(x['category']=='C13' for x in rows)
jobs=[json.loads(x) for x in (R/'NATURAL_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()]
replacements=[
 'การแข่งขัน VALORANT ปี 2030 รับสมัครได้สูงสุดกี่ทีมแน่นอน',
 'รายการ CS2 ปี 2030 ให้เงินรางวัลชนะเลิศกี่บาทแน่นอน',
 'การแข่งขัน RoV ปี 2030 เปิดรับสมัครวันไหนแน่นอน',
 'รายการ VALORANT ปี 2029 กำหนดค่าสมัครทีมละเท่าไร',
 'การแข่งขัน CS2 ปี 2029 จะจัดที่อาคารใดแน่นอน',
 'รายการ RoV ปี 2029 ใช้วันแข่งขันวันไหนแน่นอน',
 'การแข่งขัน VALORANT ปี 2031 ใช้แผนที่อะไรแน่นอน',
]
changes=[];effective=[]
for j in jobs:
 if j['category']=='C13' and 'หน่วยโทษ' in j['question']:
  new=copy.deepcopy(j);new['id']=j['id']+'-OWNER-REPLACEMENT';new['question']=replacements[len(changes)]
  new['oracle_basis']='No confirmed rules for this future event/year in the frozen source; same missing_source stratum. Owner deferred penalty-unit topic excluded before C13 execution.'
  changes.append({'excluded':j,'replacement':new});effective.append(new)
 else:effective.append(j)
assert len(changes)==7 and len(effective)==1400 and len({j['id'] for j in effective})==1400
p=R/'EFFECTIVE_QUESTIONS_1400.jsonl';assert not p.exists()
p.write_text('\n'.join(json.dumps(j,ensure_ascii=False) for j in effective)+'\n','utf8')
write(R/'EXCLUSION_ADDENDUM.json',{'applied_at':datetime.now().astimezone().isoformat(),'owner_instruction_source':'r109_owner_answers_20261020/FUTURE_TEST_EXCLUSIONS.json','owner_question_id':'R108_TEKKEN_PENALTY','owner_instruction':'อันนี้ข้ามไปทีไม่ต้องเทสอันนี้ ไม่มีข้อมูล','reason':'Enforce prior explicit owner exclusion before the affected category is executed, independent of model outputs. Original frozen cases preserved.','c13_executions_before_addendum':0,'retained_pairs_before_addendum':len(rows),'retained_results_sha256':sha(R/'main_natural/RESULTS.jsonl'),'original_workload_sha256':sha(R/'NATURAL_QUESTIONS_1400.jsonl'),'effective_workload_sha256':sha(p),'original_excluded_questions':7,'replacements':7,'changes':changes})
prior=R/'resume_benchmark.py';new=prior.read_text('utf8')
new=new.replace("R/'NATURAL_QUESTIONS_1400.jsonl'","R/'EFFECTIVE_QUESTIONS_1400.jsonl'")
new=new.replace("atomic('RESUME_CONTROL.json'","atomic('RESUME_CONTROL_EXCLUSION.json'")
new=new.replace("WinError 5 replacing STATUS.json; previous failure retained in FAILED.json","Control restart to enforce owner topic exclusion before C13; prior failure/recovery records retained")
new=new.replace("manifest=read(R/'DATA_MANIFEST.json')","addendum=read(R/'EXCLUSION_ADDENDUM.json');assert sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl')==addendum['effective_workload_sha256']\n manifest=read(R/'DATA_MANIFEST.json')")
new=new.replace("'evaluation_control_resumed_after_status_io_failure':True","'effective_workload_sha256':sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl'),'owner_exclusion_applied_before_category_execution':True,'evaluation_control_resumed_after_status_io_failure':True")
new=new.replace("assert sha(db)==manifest['sha256']\n with urllib", "assert sha(db)==manifest['sha256']\n assert sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl')==addendum['effective_workload_sha256']\n with urllib")
new=new.replace("atomic('RESUME_FAILED.json'","atomic('RESUME_EXCLUSION_FAILED.json'")
(R/'resume_after_exclusion.py').write_text(new,'utf8')
write(R/'main_natural/INTERRUPTION_EXCLUSION.json',{'verified_owned_process_stopped':52624,'reason':'Owner exclusion audit before C13 executes','retained_pairs':len(rows),'c13_already_executed':0,'prior_control_sha256':sha(prior),'new_control_sha256':sha(R/'resume_after_exclusion.py'),'in_flight_http_result_at_interrupt':'No orphan persisted model event; an in-flight HTTP call may have had no persisted response. Only missing result pairs will execute.'})
print(json.dumps({'retained_pairs':len(rows),'excluded':7,'effective_questions':1400,'c13_executed':0},ensure_ascii=False))
