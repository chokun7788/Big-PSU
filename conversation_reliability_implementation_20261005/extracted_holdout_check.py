"""New conversation variants against the actual extracted release."""
import json, os, sys, zipfile, time
from pathlib import Path
HERE=Path(__file__).resolve().parent
# Windows extraction may hit the legacy 260-character limit in the deep evidence path.
EXTRACT=Path(r'C:\Users\Chokhun\Documents\Codex\psu_r38_archive_check_20261005')
if EXTRACT.exists(): raise SystemExit('Use a fresh verification directory; do not overwrite evidence.')
with zipfile.ZipFile(HERE/'PSU_Esports_Chatbot_r38_3.zip') as z:
    for item in z.infolist():
        assert not Path(item.filename).is_absolute() and '..' not in Path(item.filename).parts
    z.extractall(EXTRACT)
ROOT=EXTRACT/'PSU_Esports_Chatbot_Local'
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
os.environ.update(PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_CHAT_LOG_DIR=str(HERE/'extracted_smoke_logs'))
from app.session.conversation_plan import resolve_request_plan as plan
from app.pipeline.engine import answer_question_pipeline_debug as answer
from app.pipeline.conversation_rules import build_full_rule_answer
rows=[]
cases=[
 ('th','คอมพิวเตอร์ที่เป็น PC ครับ',['pc'],2),
 ('th','ขอ VR แทน ไม่เอา PC',['vr'],4),
 ('th','เอาบริการครบทุกโซนเลยครับ',['pc','ps5','nintendo_switch','cockpit','vr'],14),
 ('en',"I'd like the cockpit rate instead",['cockpit'],2),
 ('en','Show me each service',['pc','ps5','nintendo_switch','cockpit','vr'],14),
 ('en','the Nintendo Switch option thanks',['nintendo_switch'],4),
]
for locale,q,targets,count in cases:
    pending=plan('ขอค่าบริการสำหรับบุคคลภายนอก' if locale=='th' else 'Prices for external users',locale=locale)
    p=plan(q,active_task=pending['tasks'][0],locale=locale)
    r=answer(q,locale=locale,request_plan=p,experimental_allow_llm=False)
    metadata=next((t.metadata for t in r.trace if t.stage=='conversation_contract'),{})
    actual=p['tasks'][0]['targets'] if p and p.get('tasks') else []
    ok=set(actual)==set(targets) and len(metadata.get('returned_ids',[]))==count and not any(i.endswith(':psu_student_staff') for i in metadata.get('returned_ids',[]))
    rows.append(dict(question=q,locale=locale,expected_targets=targets,actual_targets=actual,expected_rows=count,metadata=metadata,answer=r.answer,passed=ok))
for locale,q in [('th','ขออ่านกติกา CS2 ทุกหัวข้อแบบละเอียด'),('en','Please show every section of the CS2 tournament rulebook')]:
    r=build_full_rule_answer(q,locale)
    rows.append(dict(question=q,locale=locale,answer=r['answer'] if r else None,passed=bool(r and r['trace'][0].metadata.get('returned_ids'))))
summary=dict(extracted_root=str(ROOT),cases=len(rows),passed=sum(r['passed'] for r in rows),records=rows)
(HERE/'extracted_holdout_results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(cases=len(rows),passed=summary['passed'],failures=[r['question'] for r in rows if not r['passed']]),ensure_ascii=False,indent=2))
if summary['passed']!=len(rows): raise SystemExit(1)
