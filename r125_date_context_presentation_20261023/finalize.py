import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';P=R.parent/'r124_legacy_guided_parity_20261023'
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def link(p,label):return '['+label+'](<'+str(Path(p).resolve()).replace('\\','/')+'>)'
parent=read(R/'PARENT_FREEZE.json');changed=[p for p,h in parent.items() if sha(Path(p))!=h];assert not changed
assert sha(S/'data/knowledge/common.sqlite')==sha(P/'revision05_system/data/knowledge/common.sqlite')
current={str(p.resolve()):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
target=R/'FINAL_SOURCE_FREEZE.json'
if target.exists():assert read(target)==current
else:target.write_text(json.dumps(current,indent=2),'utf8')
gates=[]
for pattern,label in [('verification_*','foundation'),('source_guard_verification_*','source guards'),('live_verification_*','live bindings'),('exact_faq_verification_*','stable FAQ'),('date_verification_*','date/context/presentation')]:
 paths=sorted(R.glob(pattern),key=lambda p:p.stat().st_mtime,reverse=True);path=next(p/'VERIFICATION.json' for p in paths if (p/'VERIFICATION.json').exists())
 data=read(path);assert data['all_passed'];gates.append({'name':label,'assertions':len(data['checks']),'file':str(path)})
temp=read(R/'PRE_PROMOTION_API.json');tempout=Path(temp['output']);api=read(tempout/'API_VERIFICATION.json');assert api['all_passed']
active=read(R/'LIVE_API_PROCESS.json');activation=read(Path(active['output'])/'ACTIVATION_VERIFICATION.json');assert activation['all_passed']
before=read(R/'BEFORE_DATE_FAILURES.json')[0]['summary'];after=api['latencies'];count=sum(x['assertions'] for x in gates)
updates=[]
for p,h in current.items():
 rel=Path(p).relative_to(S.resolve());old=P/'revision05_system'/rel
 if not old.exists() or sha(old)!=h:updates.append(str(rel))
summary={'status':'implemented_verified_active_on_existing_url','active':active,'protected_parent_unchanged':True,'database_unchanged':True,'modified_or_added_files':updates,'invariant_assertions':count,'gates':gates,'api_test':str(tempout/'API_VERIFICATION.json'),'activation_test':str(Path(active['output'])/'ACTIVATION_VERIFICATION.json'),'model_generation_calls_in_13_clear_requests':api['model_generation_calls'],'fresh_accuracy':None,'full_test_started':False,'production_installed':False}
(R/'FINAL_REVIEW.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');(R/'STATUS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
md=['# R125 — วันที่ บริบทเดือน ความเร็ว และรูปแบบคำตอบ','', '## 1. สาเหตุจากคำถามจริง','', f"คำถาม `{before['question']}` ใช้ {before['elapsed']:.3f} วินาที โดย context model ใช้17.079วินาทีและตีC11ถูกแล้ว แต่ตัวอ่าน `service_calendar.plan` รองรับเฉพาะISO/วันนี้/พรุ่งนี้/ชื่อวัน ยังไม่ต่อ Thai month resolver จึงจบ `entity_not_bound` ไม่ใช่เพราะไม่มีตารางวันจันทร์",'',
'มี `/api/calendar` และ `app.calendar.service_calendar` อยู่แล้ว รอบนี้ใช้ resolver เดิมกับนาฬิกา Asia/Bangkok ใน backend โดยตรง ไม่ต้อง HTTP เรียก API ของตัวเองเพื่อคำนวณวันในสัปดาห์ ส่วนเครื่องว่างยังเรียก WordPress จริงตามวัน/เครื่องที่ถาม', '',link(R/'BEFORE_DATE_FAILURES.json','คำถามและtraceก่อนแก้'),'',
'## 2. กติกาวันที่ที่ใช้จริง','', '| คำถาม เมื่อวันนี้20ตุลาคม2026 | วิธีจัดการ |','|---|---|','| วันที่26ตุลาเปิดไหม | 26ตุลาคม2026 → วันจันทร์ → ตารางบริการ13:00–16:00 |','| วันที่25เปิดไหม | วันที่ตั้งแต่วันนี้ขึ้นไป → เดือนปัจจุบัน → 25ตุลาคม |','| วันที่20เปิดไหม | วันนี้ในเดือนปัจจุบัน |','| วันที่15เปิดไหม | ถาม “วันที่15ของเดือนไหนครับ?” |','| ตอบ “พฤศจิกายน/เดือน11/เดือนหน้า” | เติมเดือนให้คำถามเดิมและอ่านsourceใหม่ |','| 27ศูนย์เปิดไหม | รองรับเลขวันนำหน้าคำถาม ใช้เดือนปัจจุบันถ้ายังไม่ผ่าน |','| วันที่31ในเดือนที่ไม่มี31 | ถามเดือน ไม่เลื่อนวัน/เดือนเอง |','| เดือน13/วันที่31กุมภาพันธ์ | ขอข้อมูลใหม่พร้อมคงpendingที่ถูกต้อง |','',
'รองรับชื่อเดือนเต็ม/ย่อไทย เลขไทย ISO slash dates ปีพ.ศ. และปีค.ศ. ใช้วันจริงจากdatetime ไม่ให้โมเดลเดาวันในสัปดาห์. เดือน/วันที่ในคำถามไม่ถูกใช้เป็นเลขเวลา', '',
'### บริบทต่อเนื่อง','', 'บันทึกเฉพาะวันและข้อความที่ลูกค้าถามใน server-delivered state ไม่เก็บคำตอบธุรกิจเป็นfactในhistory. อ่านเฉพาะข้อความที่serverยืนยันว่าส่งแล้ว; client-providedstateที่ไม่ยืนยันไม่ถูกนำมาใช้. เปลี่ยนหัวข้อไม่บังคับกลับไปคำถามเดิม', '',
'“วันที่15ว่างไหม → พฤศจิกายน → PC2” ตรวจทั้ง3turnจริงแล้ว เก็บวันที่2026-11-15และproviderID15. ถ้าคำถามยังไม่ระบุเครื่อง จะถามเฉพาะเครื่อง ไม่ถามวันที่ซ้ำ. ถ้าถามวันอื่นโดยไม่ระบุเวลา อ่านรอบจองของทั้งวัน ไม่เอาเวลา20:xxของวันนี้ไปใช้กับวันนั้น', '',
'## 3. ทางทำงานใหม่','', '```mermaid','flowchart TD',' A[คำถาม + นาฬิกา Bangkok] --> B[ตัวอ่านวันที่เดิม + กติกาวันที่ไม่มีเดือน]',' B --> C{วันหรือเดือนชัดหรือไม่}',' C -->|ยังไม่ชัด| D[ถามเดือนและเก็บ pending ใน server]',' D --> B',' C -->|ชัด| E{ถามเปิดบริการหรือเครื่องว่าง}',' E -->|เปิดบริการ| F[คำนวณ weekday + native play calendar + special closure]',' E -->|เครื่องว่าง| G[เลือกเครื่อง + วัน + ช่วงเวลา → WordPress]',' F --> H[คำตอบสั้น วันที่ สถานะ ช่วงเวลา]',' G --> H',' I[คำถามข้อมูลกลุ่มอื่น] --> J[อ่าน typed source โดยตรงเมื่อเจตนาชัด]',' J --> K[ใช้โมเดลเมื่อยังต้องตีความ]',' K --> L[จัดหัวข้อ/รายการโดยไม่เปลี่ยนclaims]','```','',
'## 4. ความเร็วที่วัดจริง','', '| คำถาม | ก่อนแก้ | R125 API รอบตรวจ |','|---|---:|---:|']
for q,oldtime in [('วันที่ 26 ตุลาเปิดไหม',before['elapsed']),('27ศูนย์เปิดไหม',15.9442439),('วันนี้มีตารางว่างรึเปล่า',19.3157946),('มีเกมอะไรมั่ง',15.5824348)]:
 found=next(x for x in after if x['question']==q);md.append(f"| {q} | {oldtime:.3f}s | {found['wall_sec']:.3f}s |")
md += ['', 'คำถามแรกหลังเปิดprocessอาจใช้ประมาณ3–4วินาทีในการเริ่มอ่านชุดข้อมูล; หลังอุ่นระบบคำถามตรงกลุ่มที่ตรวจส่วนใหญ่อยู่ระดับต่ำกว่าหนึ่งวินาที ดูเวลาจริงรายข้อในJSON ไม่รับประกันเวลาคำถามอื่นทั้งหมด', '',
'ตัด context-model round trip สำหรับวันที่ เกมในรายการ และคำถามตรงที่native readerพิสูจน์scopeได้ รวมถึงprice lookupที่เป็นตัวเลขชัดและnativeplanพร้อม. คำถามซับซ้อน/หลายเงื่อนไข/เทียบราคา/ภาษาที่ยังต้องตีความยังเรียกโมเดลและอาจใช้เวลานานได้ ไม่บังคับปิดLLMทั้งระบบ', '',
'## 5. รูปแบบคำตอบ','', '- วันเปิด: แสดงวันที่เต็มและวันในสัปดาห์ พร้อมเปิด/ปิดและเวลาที่เกี่ยวข้องในข้อความสั้นเดียว','- อุปกรณ์/เกม: ชื่อขึ้นครั้งเดียว ตามด้วยหัวข้อและbulletจากsource','- Controls: ชื่อเกม/แพลตฟอร์มครั้งเดียว ตามด้วยแต่ละactionกับbinding ไม่เอาชื่อเกมซ้ำทุกบรรทัด','- กติกา: แยกชื่อรายการกับเนื้อหาclause ลดlabelที่ซ้ำกับประโยค','- ราคา: แยกบริการ/กลุ่มผู้ใช้กับจำนวนเงิน คงหน่วย/วันยืนยันและเงื่อนไข','- รายการเกม: แยกแต่ละบริการและเกมเป็นbullet','',
'การจัดรูปแบบไม่ใช้โมเดลเขียนคำตอบใหม่ คงclaim values/source refs/computationsและคำเตือนpartial/secondary-sourceตามเดิม. แก้เลขcitationให้นับตามclaims ไม่ใช่จำนวนหัวข้อ/บรรทัด. รูปแบบนำหลักการเดิมมาใช้ แต่ไม่ได้อ้างว่าเหมือนข้อความlegacyทุกตัวอักษร', '',
'### ภาพตรวจหน้าเว็บจริง','', '![คำตอบวันที่](<'+(R/'UI_DATE_ANSWER.png').as_posix()+'>)', '', '![คำตอบอุปกรณ์](<'+(R/'UI_EQUIPMENT_ANSWER.png').as_posix()+'>)', '',
'## 6. การตรวจ','', f'- ผ่าน {count} invariant assertions รวมกรณีวันสิ้นเดือน ปีพ.ศ. บริบทเดือน ความสดlive ช่วงเวลาต่อเนื่อง และcitation','- APIชุดเฉพาะ13คำขอผ่าน รวมบทสนทนา3turnและWordPressจริง; 0 model generation callsในชุดคำถามชัดนี้ แม้ระบบอนุญาตLLM','- ตรวจ3คำขอหลังสลับURLเดิม12422 ผ่านอีกครั้ง','- เก็บattemptที่third-turnพลาดไว้ แล้วแก้exactstationaliasและset-indexingก่อนตรวจซ้ำ ไม่แก้logย้อนหลัง','- ตรวจhash R124ทุกไฟล์และDBเท่าเดิม ไม่แก้production/R78/approvals/frozen/logsเดิม','- ไม่มีFullTestใหม่ และจำนวนassertionsไม่ใช่เปอร์เซ็นต์semanticaccuracy','']
for g in gates:md.append('- '+link(g['file'],g['name']+': '+str(g['assertions'])+' checks'))
md += ['',link(tempout/'API_VERIFICATION.json','APIก่อนสลับURL')+' · '+link(Path(active['output'])/'ACTIVATION_VERIFICATION.json','ตรวจURLเดิมหลังสลับ')+' · '+link(R/'FINAL_REVIEW.json','สถานะและhash checks'),'',
'## 7. ใช้งาน','', 'เว็บเดิม: http://127.0.0.1:12422/ (R125). เปิดใหม่/รีเฟรชหน้าเพื่อรับชื่อรุ่นและfrontendล่าสุด. ใช้ข้อมูลกลางชุดเดิม ไม่ติดตั้งทับR78','',
'ยังตอบตามตารางบริการที่บันทึกและspecialclosureที่มี ไม่ตีวันหยุดประเทศเป็นวันปิดศูนย์โดยอัตโนมัติ และไม่เอาservice scheduleไปอ้างว่าเครื่องว่างจริง. แหล่งข้อมูลที่ยังขัดกัน/ผังปุ่มที่ยังไม่ครบคงข้อจำกัดเดิมไว้']
(R/'REPORT_TH.md').write_text('\n'.join(md),'utf8')
print(json.dumps({'protected_unchanged':True,'database_unchanged':True,'assertions':count,'changed_files':updates,'active_url':active['url'],'report':str(R/'REPORT_TH.md')},ensure_ascii=False,indent=2))
