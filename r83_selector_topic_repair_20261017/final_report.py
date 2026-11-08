"""Freeze focused evidence, distinguish routing proposals from factual truth."""
import hashlib,json,statistics
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
T=B/'web_results/20261017T081212Z-751801'
summary=json.loads((T/'SUMMARY.json').read_text(encoding='utf8'))
rows=[json.loads(s) for s in (T/'TURNS.jsonl').read_text(encoding='utf8').splitlines()]
install=json.loads((B/'INSTALLATION.json').read_text(encoding='utf8'));baseline=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
models=[]
for row in rows:
 p=(row['body'].get('decision_artifact') or {}).get('query_plan') or {};a=p.get('entity_selection') or {}
 if a.get('attempted'):
  models.append({'question':row['question'],'locale':row['locale'],'http_seconds':row['elapsed_seconds'],'transport_ok':a.get('transport_ok'),'schema_accepted':a.get('schema_accepted'),'topic_proposal_only':a.get('topic_proposal_only'),'topic_proposal_accepted':a.get('topic_proposal_accepted'),'binding_verified':a.get('profile_binding_accepted',False),'timing_ms':a.get('timing_ms'),'model_request':a.get('model_request'),'model_metrics':a.get('model_metrics')})
qa={'installed_source_matches_tested_candidate':all(digest(S/name)==expected and (S/name).read_bytes()==(B/'candidate'/name).read_bytes() for name,expected in install['installed_files'].items()),'database_unchanged':digest(S/'data/knowledge/common.sqlite')==baseline['data/knowledge/common.sqlite'],'strict_binding_validator_unchanged':digest(S/'app/knowledge/common/semantic_profile.py')==baseline['app/knowledge/common/semantic_profile.py'],'opening_reply_module_unchanged':digest(S/'app/knowledge/common/open_day.py')==baseline['app/knowledge/common/open_day.py'],'focused_web_24_of_24':summary['count']==summary['expected_count']==summary['passed']==24,'no_selector_timeout_or_binding_failure_in_focused_web_run':not summary['model_failures'],'actual_selector_model_calls_7_of_7':len(models)==7 and all(m['transport_ok'] and m['schema_accepted'] and m['topic_proposal_only'] for m in models)}
evidence={'checks':qa,'evidence_checks_passed':all(qa.values()),'full_test_executed':False,'full_test_requires_new_user_instruction':True,'web_summary':summary,'actual_model_proposals':models,'important_limit':'24/24 checks include negative cases that only require withholding wrong facts. They do not prove every suggested clarification is the best topic or every user intent is understood.'}
with (B/'DELIVERY_QA.json').open('x',encoding='utf8') as f:json.dump(evidence,f,ensure_ascii=False,indent=2)
lines=['# R83 — แก้ selector และทดสอบเฉพาะส่วน','',
 '## สถานะ','',
 'ติดตั้งใน R78 เดิม พอร์ต 8115 แล้ว LLM ยังเปิดอยู่ เทสใหญ่/full corpus ยังไม่ได้รัน และจะรอคำสั่งใหม่ของผู้ใช้','',
 '## สิ่งที่เปลี่ยน','',
 '1. ย้าย independent-topic guard เดิมมาคัด candidate ก่อนเรียกโมเดล ไม่ตัดแหล่งจากคะแนนต่ำอย่างเดียว ตัวอย่างคำถามไทยเดิมลดจาก 8 เหลือ 3 รายการ',
 '2. เฉพาะขั้นที่ยังต้องถามยืนยัน: ให้ LLM เสนอ topic indices แบบสั้น ไม่ให้สร้าง quote/binding ที่ยังไม่จำเป็น ไม่สร้างคำตอบข้อเท็จจริงจากการเสนอหัวข้อ',
 '3. กรณีโมเดลเลือก profile หรือเลือก profile ปนรายการทั่วไป จะถามยืนยันหัวข้อด้วย state/fingerprint เดิมก่อนอ่าน source revision ปัจจุบัน',
 '4. คง strict quote/binding validator เดิมสำหรับผู้เรียกที่ยังต้องใช้ ไม่ยอมรับคำที่ไม่มีใน input และคง HTTP cap 6 วินาที/context 3072; ลด output cap ของ topic proposal จาก 420 เหลือ 70 tokens',
 '5. หาก named FAQ ตอบไม่ครอบคลุมและ validation ปฏิเสธด้วย unresolved_query_clause ให้กู้กลับไปถามยืนยัน declared topic ที่เข้าเงื่อนไข โดยเก็บ rejected candidate ไว้และไม่แสดง facts ที่ถูกปฏิเสธ','',
 '## เหตุของสองปัญหาเดิม','',
 '- ไทย: candidate ที่ไม่ผ่านเงื่อนไขรับเดิมยังถูกส่งเข้า prompt และต้องสร้าง binding ยาว ก่อนถามผู้ใช้ยืนยันอยู่ดี ทำให้คำขอเดิมรอ Ollama ถึง deadline',
 '- อังกฤษ: model เลือก source ขั้นตอนสลิปถูก แต่คัด task_span ไม่ผ่าน exact-input และใส่ subject span “slip” ซึ่งไม่มีในคำถาม การคืน JSON ได้จึงไม่ได้แปลว่า binding ใช้ได้',
 '- การแก้ลดงานโมเดลในขั้นเสนอหัวข้อ คงการตรวจ source และการยืนยัน ไม่เพิ่ม alias ของคำถามตัวอย่าง และไม่เปลี่ยนนโยบาย','',
 '## การทดสอบและ loop','',
 '| ชุด | ผล | วิธี |','|---|---:|---|',
 '| selector/protocol/recovery guards | 31/31 | controlled outputs, strict validator และ trusted state |',
 '| ยืนยันพร้อมเงื่อนไขเพิ่มเติม | 41/41 | fixtures แยก ตรวจขอบเขต/ownership/competition/revision |',
 '| ปฏิเสธแล้วเปลี่ยนเรื่อง/ถามต่อ | 34/34 | fixtures แยกและ handler ในหน่วยความจำ |',
 '| candidate กับ LLM จริง รอบสุดท้าย | 24/24 ข้อความ | real dispatcher, candidate overlay, ไม่ใช่ TCP ของเว็บ |',
 '| ติดตั้งแล้วผ่านเว็บจริง | 24/24 ข้อความ | session จริงแยก, HTTP /api/chat, LLM ON |','',
 'ชุดตรวจภายใน 106 ข้อไม่ใช่ 106 คำถามไม่ซ้ำ ไม่รวมเป็นคะแนนความแม่นยำของ LLM; เว็บจริงแยกไทย 10/10 อังกฤษ 14/14','',
 '### รอบที่พบปัญหาและเก็บไว้','',
 '- live_candidate_1: Ollama ไม่เปิดรับการเชื่อมต่อ 10061 ยังไม่ส่งคำถาม',
 '- live_candidate_2: เปิด Ollama เบื้องหลังได้ แต่ GPU discovery ใช้ประมาณ 45.8 วินาที เกินเวลา readiness 30 วินาทีของตัวรัน ปรับเฉพาะเวลาเตรียมบริการเป็น 90 วินาที ไม่เปลี่ยนเวลาตอบคำถาม',
 '- live_candidate_3: 12 เทิร์นแรกผ่าน จากนั้น harness สมมุติว่า state ต้องเป็น dict แล้วหยุดเมื่อได้ None แก้ harness ให้เก็บผลกรณีไม่มี state เป็น failure แทน crash',
 '- live_candidate_4: 22/24 ผ่าน พบ alias “โอนเงิน” ดึง FAQ เลขบัญชีแทนคำถามรูปหลักฐานผิด ทำให้ validation ปฏิเสธ และตอบ “ใช่” ต่อไม่ได้',
 '- live_candidate_5: หลังเพิ่ม rejected-coverage recovery ผ่าน 24/24 พร้อม selector proposal จริง 7 ครั้ง ไม่มี timeout/binding failure ในชุดนั้น',
 '- หลังติดตั้ง ตรวจเว็บจริง 24/24 ผ่าน selector proposal จริง 7/7 ครั้ง ไม่มี timeout/binding failure ในเส้นทางที่ทดสอบ','',
 '## ผลผ่านเว็บและเวลา','',
 '| ภาษา | ข้อความผ่าน | มัธยฐาน HTTP (วินาที) |','|---|---:|---:|']
for lang,r in summary['by_language'].items():lines.append('| '+lang+' | '+str(r['passed'])+'/'+str(r['count'])+' | '+str(round(r['median_seconds'],3))+' |')
lines+=['','เวลาเป็นตัวอย่างชุดเล็กหลังเตรียมโมเดล ไม่ใช่ความเร็วที่รับประกันทุกครั้งหรือผลทดสอบความจุหลายคน','',
 '### คำถามไทยเดิมที่เคย timeout','']
original=next(r for r in rows if r['case']=='th-personal' and r['expect']=='pending');a=original['body']['decision_artifact']['query_plan']['entity_selection']
lines += ['- HTTP ทั้งคำถาม '+str(original['elapsed_seconds'])+' วินาที; selector รวม '+str(a['timing_ms']['total_ms'])+' ms; HTTP รอโมเดล '+str(a['timing_ms']['http_wait_and_read_ms'])+' ms',
 '- payload '+str(a['model_request']['payload_bytes'])+' bytes; '+str(a['model_metrics']['prompt_eval_count'])+' prompt tokens และ '+str(a['model_metrics']['eval_count'])+' output tokens',
 '- โมเดลเสนอหัวข้อแบบ ambiguous จาก source ที่เกี่ยวข้อง ระบบจึงถามยืนยัน และตอบจาก source ได้เมื่อผู้ใช้ยืนยันว่าเป็นเมาส์ส่วนตัว',
 '- รอบ R82 คำถามเดียวกัน timeout หลังรอโมเดลประมาณ 6.0–6.4 วินาที ครั้งนี้รอโมเดลต่ำกว่า 1 วินาที แต่ไม่ใช้เป็น controlled speedup benchmark เพราะสภาพ cache/startup และภาระเครื่องต่างกัน','',
 '## สิ่งที่ผลนี้ยังไม่ได้พิสูจน์','',
 '- 7/7 คือ model transport/JSON topic-proposal protocol ผ่าน ไม่ใช่การพิสูจน์ semantic equivalence โดยอิสระ ยังต้องยืนยันก่อนอ่าน facts',
 '- เคส proof of identity / wrong amount ผ่านในเกณฑ์ “ไม่ยืนยันขั้นตอนสลิปให้สิ่งอื่น” แต่ยังอาจเสนอหัวข้อสลิปให้ผู้ใช้ยืนยัน ทั้งที่ไม่ใช่หัวข้อที่ดีที่สุด จึงยังมีงานปรับความเกี่ยวข้องของ clarification; ไม่อ้างว่าสองเคสนี้เข้าใจความหมายสมบูรณ์',
 '- ตัวอย่างการยืนยันมี ?? ซ้ำจาก title เดิม และข้อความอังกฤษบางส่วนยังมีป้าย steps/preconditions แบบ schema เป็นประเด็นการนำเสนอแยกจากการแก้รอบนี้',
 '- direct/scoped callers ที่ต้องใช้ strict binding จริงยังคงโปรโตคอลเดิม ไม่อ้างว่าทุกเส้นทางของ LLM ถูกทำให้เร็วแล้ว',
 '- ไม่ได้ทดสอบทุกหมวดหรือเต็ม corpus และไม่อนุมัติข้อมูลเจ้าของ/ราคา/วันมีผลแทนเจ้าของ','',
 '## สิ่งที่รักษาไว้','',
 '- เปลี่ยนเฉพาะ entity_search.py, answer.py, migrated_chat.py ใน R78 มี before/ และ CHANGESET.patch',
 '- ไฟล์แอป/UI อื่น '+str(install['other_application_ui_files_unchanged'])+' ไฟล์ไม่เปลี่ยน strict semantic validator กับ open_day.py ของ R80 ไม่เปลี่ยน',
 '- DB SHA256: `'+install['database_sha256']+'` ก่อน/หลังเท่ากัน ไม่มีการแก้ facts/ราคา/นโยบาย/approvals/releases',
 '- raw log ทุก attempt อยู่ครบ ไม่ทับไฟล์เก่าหรือรีเซ็ต Git','',
 '## ไฟล์หลักฐาน','',
 '- FLOW_R83_TH.md: Flow และการตรวจทาน',
 '- CANDIDATE_AUDIT.json: ผู้สมัครก่อน/หลังพร้อมเหตุผล',
 '- verification/candidate_2/RESULTS.json, qualified_final/RESULTS.json, rephrase_1/RESULTS.json',
 '- verification/live_candidate_5/SUMMARY.json และ TURNS.jsonl',
 '- web_results/20261017T081212Z-751801/SUMMARY.json, TURNS.jsonl และ health/launcher/model response',
 '- INSTALLATION.json, SOURCE_INVENTORY_BEFORE.json, DELIVERY_QA.json','',
 '## สถานะเทสใหญ่','',
 '**รอผู้ใช้สั่งเพิ่มเติมเท่านั้น ยังไม่เริ่ม full test และไม่ได้ตั้งงานให้รัน full test อัตโนมัติ**','']
with (B/'REPORT_R83_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines))
print(json.dumps({'checks':qa,'web_summary':summary,'report':str(B/'REPORT_R83_TH.md')},ensure_ascii=False));assert all(qa.values())
