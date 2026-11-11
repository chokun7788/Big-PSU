"""Build the retrospective issue appendix from saved ledgers; no inference/DB writes."""
from pathlib import Path
import collections, datetime, hashlib, json, re, subprocess

ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent
AUDIT=PROJECT/'r135_complete_flow_audit_20261026'

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def cell(value):
    return str(value or '').replace('|',r'\|').replace('\n',' ')

def paths(value):
    found=[]
    if isinstance(value,dict):
        for key,item in value.items():
            if key in {'path','report','script'} and isinstance(item,str):found.append(item)
            else:found.extend(paths(item))
    elif isinstance(value,list):
        for item in value:found.extend(paths(item))
    return sorted(set(found))

document=ROOT/'ALL_KNOWN_ISSUES_TH.md'
main=document.read_text(encoding='utf8').split('<!-- GENERATED_APPENDIX -->')[0].rstrip()
gaps=read(AUDIT/'AUDIT_GAPS.json')['gaps']
ledger=read(AUDIT/'COMPLETION_LEDGER.json')['requirements']
status=read(AUDIT/'STATUS.json')
by_id={r['id']:r for r in ledger}
selected=status.get('requirement_specific_review_ids',[])
selected_states=collections.Counter(by_id[x]['implementation_state'] for x in selected if x in by_id)
issue_ids=re.findall(r'^\| ((?:D|T|I|L|F|V|O|Q)\d{2}) /',main,re.M)
assert len(issue_ids)==len(set(issue_ids))
assert len(gaps)==len({g['id'] for g in gaps})
assert len(ledger)==76
parts=[main,'','<!-- GENERATED_APPENDIX -->',
       '## ภาคผนวก A — Audit gaps เดิมทุก ID โดยไม่ตัดรายการที่เคยแก้แล้ว','',
       f'คัดจาก AUDIT_GAPS.json จำนวน **{len(gaps)} รายการ** ตัวทะเบียนเองระบุว่าไม่ใช่ exhaustive list จึงต้องอ่านร่วมกับรายการปัญหารุ่นใหม่ด้านบน รายการที่ state เป็น implemented_component_verification_final_audit_pending หมายถึงมี component repair รอ final audit ไม่ใช่รับรองครบทั้ง requirement หรือยืนยันว่า patch นั้นถูก port และตรวจในรุ่นผสมล่าสุดแล้ว','',
       'คง finding ภาษาอังกฤษต้นฉบับเพื่อไม่ทำรายละเอียดเชิงสัญญาหาย บทวิเคราะห์ภาษาไทยอยู่หัวข้อ 4–12; ข้อความ finding เป็นอาการที่พบ ณ รอบนั้น ไม่ใช่การยืนยันว่าทั้ง 143 อาการยังเกิดอยู่วันนี้','',
       '| state ที่บันทึกไว้ | จำนวน |','|---|---:|']
for state,n in collections.Counter(g.get('state') for g in gaps).items():parts.append(f'| `{cell(state)}` | {n} |')
parts.append('')
for gap in gaps:
    parts.extend([f"### {gap['id']} — {', '.join(gap.get('requirements',[]))}",'',
                  f"- **สถานะที่บันทึก:** `{gap.get('state','unknown')}`",
                  f"- **ปัญหาที่พบเดิม:** {gap.get('finding','ไม่บันทึก')}"])
    if gap.get('review_note'):parts.append(f"- **ผลทบทวน/ขอบเขตที่บันทึก:** {gap['review_note']}")
    code=gap.get('candidate_code') or gap.get('code')
    if code:parts.append(f'- **จุดโค้ดที่อ้าง:** `{code}`')
    refs=paths(gap.get('evidence',{}))
    if refs:parts.append('- **หลักฐานเดิมใต้ r135_complete_flow_audit_20261026:** '+', '.join(f'`{p}`' for p in refs))
    parts.append('')
parts.extend(['## ภาคผนวก B — Requirement ledger ครบ 76 ข้อ','',
              'ตารางนี้คงสถานะต้นฉบับของ full R135 ไม่เลื่อนสถานะเพราะมี controls รุ่นผสมผ่าน และไม่ใช้เพื่อสร้าง completion percentage ใหม่','',
              f"ชุด requirement_specific_review_ids ที่บันทึกมี {len(selected)} IDs; state ภายในชุดนี้ ณ ledger ที่อ่าน: "+', '.join(f'{s} = {n}' for s,n in selected_states.items())+'. ตัวเลขอาจต่างจากแผน 36/11/1 ที่เขียนก่อนหน้า จึงห้ามใช้ตารางเก่าแทน ledger โดยไม่มีวันที่','',
              '| ID | ข้อกำหนด | อยู่ในชุด review IDs ที่เลือก | implementation state | acceptance state | gap IDs ที่ผูก |',
              '|---|---|---|---|---|---|'])
for row in ledger:
    associated=[g['id'] for g in gaps if row['id'] in g.get('requirements',[])]
    parts.append('| '+' | '.join([cell(row['id']),cell(row.get('title')), 'ใช่' if row['id'] in selected else 'ไม่ใช่',cell(row.get('implementation_state')),cell(row.get('behavior_acceptance_state')),', '.join(associated)])+' |')
parts.extend(['','## ภาคผนวก C — ขอบเขตการตรวจเอกสารครั้งนี้','',
              f'- รายการปัญหาร่วมในหัวข้อ 4–11 มี {len(issue_ids)} IDs เป็นการจัดกลุ่มใหม่ ไม่ใช่จำนวน bugs ที่ไม่ซ้ำกับ {len(gaps)} historical gaps',
              '- อ่านสถานะ/แผน/ผลตรวจที่ระบุใน manifest พร้อมโค้ดเส้นทางคำผิดและ input derivation ที่เกี่ยวข้อง ไม่ได้ semantic review คำตอบดิบทุกแถวใหม่ในรอบนี้',
              '- ไม่เรียกโมเดล ไม่เปิด benchmark ใหม่ ไม่เปลี่ยน runtime/DB/approval/frozen evaluation และไม่แก้คะแนนเก่า',
              '- การพบเอกสารเก่าที่ขัดกับรายงานใหม่ถูกระบุว่าเป็น historical state ไม่ใช้เป็นหลักฐานว่าระบบอยู่สองสถานะพร้อมกัน',
              '- ไม่สรุปว่าข้อมูลรก, ไม่มีลิงก์, โมเดลล่ม, พื้นที่เต็ม หรือ intent ละเอียดเกิน เป็น root cause ทั้งระบบโดยไม่มี receipt',
              '- SHA256 ของไฟล์ประกอบ ณ ตอนสร้างอยู่ ISSUE_AUDIT_MANIFEST.json ใช้ตรวจว่าฐานหลักฐานเปลี่ยนหรือไม่ ไม่ใช่ semantic proof',''])
document.write_text('\n'.join(parts),encoding='utf8')
sources=[
 'AGENTS.md',
 'r135_bounded_response_20261111/STATUS.json',
 'r135_bounded_response_20261111/flow.md',
 'r135_bounded_response_20261111/TYPO_RECOVERY_TH.md',
 'r135_bounded_response_20261111/UNAVAILABLE_ATTRIBUTION_TH.md',
 'r135_bounded_response_20261111/VERIFIED_SOURCE_FLOW_TH.md',
 'r135_bounded_response_20261111/PUBLIC_CITATIONS_TH.md',
 'r135_bounded_response_20261111/typo_research_20261111/RESEARCH_TH.md',
 'r135_verified_eval200_20261111/evaluation/REPORT_TH.md',
 'r135_verified_eval200_20261111/evaluation/UNAVAILABLE_GROUPS.json',
 'r135_hybrid_eval10_20261110/evaluation/ANALYSIS_SUMMARY.json',
 'r135_hybrid_eval10_20261110/evaluation/SCORES_LITERAL.json',
 'r135_hybrid48_intent_round02_20261108/DATA_LAYOUT_AUDIT_TH.md',
 'r135_hybrid48_intent_round02_20261108/PC_COMPOUND_INTENT_DIAGNOSIS_TH.md',
 'r135_hybrid48_intent_round02_20261108/NEXT_STEPS_FLOW_HYBRID_TH.md',
 'r135_hybrid48_intent_round02_20261108/AFTER_EVAL_TIMEOUT_PLAN.md',
 'r135_hybrid48_20261108/GATES.json',
 'r135_hybrid48_20261108/evaluation/DETAILED_INTENT_FAILURE_ANALYSIS_TH.md',
 'r135_complete_flow_audit_20261026/AUDIT_GAPS.json',
 'r135_complete_flow_audit_20261026/COMPLETION_LEDGER.json',
 'r135_complete_flow_audit_20261026/STATUS.json',
 'r135_complete_flow_audit_20261026/EVAL5_OPERATOR_DIAGNOSIS_20261107.json',
 'r135_bounded_response_20261111/system/app/knowledge/common/typo_recovery.py',
 'r135_bounded_response_20261111/system/app/knowledge/common/answer.py',
 'r135_bounded_response_20261111/system/app/knowledge/common/domain_flow/input_derivation.py',
]
manifest={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'code_head_at_review':subprocess.check_output(['git','rev-parse','HEAD'],cwd=PROJECT,text=True).strip(),
          'grouped_issue_ids':issue_ids,'grouped_issue_count':len(issue_ids),'historical_gap_count':len(gaps),
          'requirements':len(ledger),'selected_review_ids':selected,'selected_implementation_states':dict(selected_states),
          'new_inference_calls':0,'new_benchmark_runs':0,'semantic_accuracy_established':False,
          'scope':'retrospective saved-evidence inventory; not a new exhaustive runtime audit',
          'files':{p:hashlib.sha256((PROJECT/p).read_bytes()).hexdigest() for p in sources},
          'report_sha256':hashlib.sha256(document.read_bytes()).hexdigest()}
(ROOT/'ISSUE_AUDIT_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'report':str(document),'grouped_issue_count':len(issue_ids),'historical_gaps':len(gaps),'requirements':len(ledger),'selected_review_ids':len(selected),'lines':len(parts)},ensure_ascii=False))
