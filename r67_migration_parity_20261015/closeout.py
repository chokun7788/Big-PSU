"""Assemble an honest reviewable delivery and verify preserved production inputs."""
import collections,hashlib,json,sqlite3,sys,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import CATALOG,value,validate
def read(n):return json.loads((B/n).read_text('utf8'))
def dump(n,x):(B/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
root=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
manifest=[{'path':p.relative_to(B/'system').as_posix(),'sha256':sha(p)} for p in (B/'system/app').rglob('*') if p.is_file() and '__pycache__' not in p.parts];dump('FROZEN_CODE_MANIFEST_final06.json',manifest)
delivery=B/'DELIVERY_final06';delivery.mkdir(exist_ok=False)
changes=[];old=B.parent/'r66_common_repair_20261014/system'
for item in manifest:
 rel=Path(item['path']);p=B/'system'/rel;previous=sha(old/rel) if (old/rel).is_file() else None
 if previous==item['sha256']:continue
 actual=sha(root/rel) if (root/rel).is_file() else None
 changes.append({'path':rel.as_posix(),'expected_old_sha256':previous,'actual_root_sha256':actual,'new_sha256':item['sha256'],'conflict':actual!=previous})
 if actual:
  dst=delivery/'before'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/rel,dst)
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(delivery/'candidate.sqlite') as dst:src.backup(dst)
def tables(path):
 with sqlite3.connect(path.as_uri()+'?mode=ro',uri=True) as c:
  result={}
  for (name,) in c.execute("select name from sqlite_master where type='table' order by name").fetchall():
   # SQLite identifiers originate from sqlite_master, never user-supplied SQL.
   quoted='"'+name.replace('"','""')+'"';rows=c.execute('select * from '+quoted).fetchall()
   encoded=sorted(json.dumps(row,ensure_ascii=False,default=lambda x:x.hex() if isinstance(x,bytes) else str(x)) for row in rows)
   result[name]={'rows':len(rows),'sha256':hashlib.sha256('\n'.join(encoded).encode()).hexdigest()}
  return result
common_tables=tables(B/'common.sqlite');candidate_tables=tables(delivery/'candidate.sqlite');assert common_tables==candidate_tables
protected=[]
for rel in ['data/knowledge/approved.sqlite','data/knowledge/migration_r63_20261013/approved.sqlite','data/knowledge/migration_r66_20261015/candidate.sqlite']:
 p=root/rel
 if p.is_file():protected.append({'path':rel,'sha256':sha(p)})
inputs=read('SOURCE_MANIFEST.json');changed_inputs=[x['path'] for x in inputs if not (root/x['path']).is_file() or sha(root/x['path'])!=x['sha256']]
store=CommonStore(delivery/'candidate.sqlite')
with store.connect() as c:
 rs=store.heads(c);sources=store.sources(c);meta=dict(c.execute('select key,value from cc_meta'));approvals=c.execute('select count(*) from cc_approvals').fetchone()[0]
errors={rid:err for rid,r in rs.items() if (err:=validate(r,rs,sources))};assert not errors
publication={rid:errs for rid,r in rs.items() if (errs:=validate(r,rs,sources,publish=True))}
dump('PUBLICATION_BLOCKERS_final06.json',publication)
out={
 'date_th':'2026-10-16','records':len(rs),'changed_code_files':len(changes),'code_conflicts':[x for x in changes if x['conflict']],
 'source_files_checked':len(inputs),'changed_production_inputs':changed_inputs,'protected_databases':protected,
 'candidate_sha256':sha(delivery/'candidate.sqlite'),'candidate_logically_identical_to_test_database':True,'candidate_table_hashes':candidate_tables,
 'schema_errors':errors,'active_release':meta['active'],'approvals':approvals,'publication_blocked_records':len(publication),
 'network_permission_granted':False,'project_write_permission_granted':False,'deployed':False,
 'scope':'common content migration and focused validation; no legacy rerun, no new live booking oracle, no full sweep; actual local model/socket and project deployment blocked by permissions',
 'changes':changes}
dump('DELIVERY_final06/PLAN.json',out)
bundle={'schema_version':'studio-content-3.0','records':list(rs.values()),'sources':[{'source':pair[0],'snapshot':pair[1]} for pair in sources.values()],'mode':'draft_only','build_id':'common-r67-source-parity','approvals_included':False}
dump('DELIVERY_final06/migration.bundle.json',bundle)
counts=collections.Counter(r['kind'] for r in rs.values())
spec=['# Format กลาง R67 — คู่มือหมวดและช่องข้อมูล','','สถานะ: ข้อมูลจริงที่ย้ายมาเป็นร่างสำหรับตรวจและทดลอง ยังไม่ใช่ release production','',
 '## วิธีเริ่มใช้งาน','','เปิด Open-R67-Drafts.cmd ในโฟลเดอร์นี้ เลือกหมวดและรายการเดิมเพื่อแก้ไข หรือเพิ่มรายการใหม่ ทดสอบในช่องทดลองร่าง ข้อมูลที่กรอกยังไม่เปลี่ยนเว็บแชทปกติจนกว่าจะผ่านการตรวจและเผยแพร่','',
 '## ตัวอย่างสำคัญ','','### เพิ่ม/แก้เกม','','ใช้รายการเดิมเมื่อแก้คำอธิบายเกม เพิ่มชื่อ/ชื่อเรียก แนวเกม วิธีเล่น และคำบรรยายต้นฉบับ หากเปลี่ยนเป็นอีกภาคหรือ edition ต้องแยกตัวตนให้ชัด การมีรายละเอียดเกมไม่เท่ากับศูนย์ติดตั้ง ต้องเชื่อมเกมกับบริการในหมวด game_service','',
 '### เพิ่ม/แก้ปุ่ม','','เลือกเกมและแพลตฟอร์มก่อน เพิ่มทีละแถว เช่น ชื่อปุ่ม A, รายการปุ่ม [A], action เร่งเครื่อง, notes กดค้างไว้เพื่อเร่งเครื่อง ถ้าแถวหนึ่งมีหลายการกระทำหรือไม่ทราบ gesture ให้เลือก unknown และเก็บคำอธิบายตามต้นฉบับ ห้ามเลือก press แทนข้อมูลที่ไม่ทราบ ชื่อ A / B ไม่รับรองว่ากดพร้อมกัน','',
 '### เพิ่ม/แก้ราคา','','เลือกบริการและกลุ่มผู้ใช้ กรอกบาทในหน้าเจ้าของ ระบบเก็บหน่วยย่อยเอง ระบุเวลา หน่วยคิด สูตร และวันมีผลตามประกาศ ไม่คูณราคาหรือกำหนดวันเอง การแก้สร้าง revision ใหม่ เก็บราคาเดิมในประวัติ ไม่เปลี่ยนราคาที่หมดอายุให้เป็นปัจจุบัน','',
 '### เพิ่ม/แก้กติกา','','เลือกรายการแข่งขันและเกม แยกหัวข้อ ข้อความเต็ม และข้อที่ต้องอ่านร่วมกัน อย่าตัดข้อยกเว้นหรือท้ายข้อ ใช้ source_order รักษาลำดับเมื่อเลขหัวข้อซ้ำ facets เป็นการจัดหมวดค้นหา ไม่ใช่กฎใหม่ และไม่ได้รับรองว่าข้อความครอบคลุมทุกกรณี','',
 '### ข้อมูลหลายภาษา','','ใส่ไทย/อังกฤษแยกกัน ช่องที่ไม่มีคำแปลจะระบุรอแปล ไม่ใช้คำตอบสั้นภาษาอังกฤษแทนรายละเอียดไทยที่ยาวกว่า คำแปลโดย agent ยังแยกจากการยืนยันโดยเจ้าของ','',
 '## ทุกหมวดที่ระบบรองรับ','','★ คือช่องหลักตาม schema สำหรับเผยแพร่ การทดลองร่างอ่านส่วนที่มีหลักฐานได้ แม้ส่วนอื่นยังไม่ทราบ ไม่มีการเติมข้อเท็จจริงให้ผ่านเกณฑ์โดยเดา','']
for kind,cat in CATALOG.items():
 spec += ['## '+cat['owner_form']+' (`'+kind+'`)','','รายการในร่างนี้: '+str(counts[kind]),'','| ช่อง | ความหมาย | ก่อนเผยแพร่ |','|---|---|---|']
 for f in cat['fields']:spec.append('| '+f['key']+' | '+f['meaning_th'].replace('|','/')+' | '+('★' if f['publish_core'] else 'เมื่อมีข้อมูล')+' |')
 spec += ['']
(B/'FORMAT_SPEC_R67_TH.md').write_text('\n'.join(spec),encoding='utf8')
report=f'''# R67 — ผลตรวจและย้ายข้อมูลเดิมเข้า Format กลาง

จัดทำวันที่ 16 ตุลาคม 2026 (ประเทศไทย) เริ่มงานในโฟลเดอร์ชื่อ 20261015

## สถานะใช้งาน

โค้ดและฐานร่างอยู่ใน workspace นี้ ข้อมูล {len(rs)} รายการ ยังไม่มี active release หรือ approval ใหม่ **ยังไม่ได้นำเข้าโปรเจกต์จริง** ระบบไม่ให้สิทธิ์เขียนโฟลเดอร์ Downloads และไม่ให้สิทธิ์เชื่อม socket ของ Ollama หลังขอผ่าน request_permissions แล้ว ไม่ใช่ความผิดของโมเดลที่พิสูจน์ได้

เปิดทดลองได้ด้วย [Open-R67-Drafts.cmd](Open-R67-Drafts.cmd) ซึ่งใช้ Python ที่มีอยู่ใน r58 และพอร์ต 8099 ตัว launcher ผ่านการตรวจ syntax แต่ยังไม่ได้เปิด HTTP จริงจากรอบนี้ เพราะ socket ถูกจำกัด หน้าทดลองเรียก reader ตัวเดียวกับ common chat และติดป้าย DRAFT PREVIEW ข้อมูลนี้ยังไม่ถูกใช้ในเว็บแชทเดิมที่เปิดค้าง

## สิ่งที่ตกหล่นและย้ายเพิ่ม

- ตรวจ canonical 270 รายการทุกช่องข้อความ TH/EN ไม่ใช้จำนวน record แทนความครบของข้อมูล
- เติมสังกัดบุคลากร 12 รายการ วาระ 5 รายการ หมายเหตุบริการ 8 รายการ สรุปชุดปุ่ม 38 รายการ ชื่อหัวเอกสารการแข่งขัน 4 รายการ ลำดับข้อความ 104 หัวข้อ และจัดหมวดกฎจาก source ที่จับคู่ได้โดยไม่บังคับหมวดที่ไม่ทราบ
- เปลี่ยนปุ่มเก่าจากข้อความใน limitations เป็น bindings ที่อ่านได้แยกปุ่ม/action/notes/section/order 427 แถว โดยไม่เดา gesture/context
- พบแหล่งก่อน canonical ที่ย้ายไม่ครบ: กู้คำบรรยายเกม 31 รายการ และปุ่ม eFootball/Overcooked! 2/THE FINALS อีก 21 แถว รวมผังปุ่มทั้ง 43 กลุ่ม / 448 แถว + 43 สรุป = 491 รายการต้นทาง
- Delta Force และ Pokémon Champions มีเพียงข้อมูลว่ายังไม่มีผังปุ่มที่ตรวจได้ ไม่สร้างปุ่มขึ้นเอง
- รักษาหมายเหตุความน่าเชื่อถือ/เวอร์ชันชุดปุ่มเดิม พร้อมแปลให้ไทย/อังกฤษ 31 คำบรรยายและ 21 คำอธิบายปุ่มที่กู้เพิ่มมีภาษาอังกฤษแล้ว การแปลครั้งนี้ตรวจโดย agent จากต้นฉบับ ไม่ใช่ owner approval หรือการตรวจแพตช์เกมจริง
- เพิ่ม source listing profiles 3 รายการสำหรับชื่อ edition/รายการรวมตามต้นฉบับ ไม่มีการสร้าง game_service/เครื่อง/การติดตั้งเพิ่ม จำนวนเกมที่ offered ตาม source เดิมยัง 42 เกม แม้จำนวน profile รวมเป็น 51
- เก็บหัวข้อ intent เดิมของ FAQ 73 รายการเป็นข้อมูล เพื่อเลือกหัวข้อร่วมกันโดยไม่เพิ่ม alias รายประโยค
- คืนกฎทั่วไปภาษาอังกฤษฉบับเต็มจากไฟล์เดิม พร้อมแปลไทยตรงกัน และเก็บ source variants เรื่องความรับผิดชอบค่าเสียหายที่ไทย/อังกฤษระบุเงื่อนไขไม่เท่ากัน

## ตรวจความครบและการรักษาต้นฉบับ

- ตรวจ original lineage 1,933 ช่อง: ทุก source hash และ source pointer ตรงเดิม ส่วนที่แปล/ขยายจาก source แยกบัญชี ไม่เรียกว่า byte-identical ทุกช่อง
- canonical localized nonempty leaves 3,487 จุด: 3,442 ตรงข้อความในช่องอ่านโดยตรง, 3 เป็น revision ที่มีหลักฐานและต้องอ่านคู่ source/ประวัติ, 42 เป็น refusal/language configuration ที่เก็บไว้ ไม่เผยแพร่เป็นข้อเท็จจริงของศูนย์ ไม่มี missing_readable_field ในขอบเขตนี้
- ตัวเลข direct-field coverage ไม่ใช่คะแนนความถูกต้อง 100% ก่อนแก้ปุ่มบางส่วนอ่านผ่าน adapter ได้อยู่แล้ว จึงไม่ตีความ 2,615 จุดก่อนแก้ว่าเป็นคำตอบที่หายทั้งหมด
- raw-row/FK/source/revision checks 2,840/2,840 ผ่าน เก็บ original revisions 1,140 และ original sources 1,144 ทุกชุด unchanged
- source inputs ที่ snapshot {len(inputs)} ไฟล์ ตรวจโปรเจกต์จริงอีกครั้ง: เปลี่ยน {len(changed_inputs)} ไฟล์
- จัดเตรียมโค้ดเปลี่ยน {len(changes)} ไฟล์ สำรองไฟล์เดิมไว้ใน DELIVERY_final06/before ไม่มี conflict กับฐาน R66 ในโปรเจกต์ ณ ตอนตรวจ
- candidate.sqlite ที่เตรียมส่งเทียบทุกตารางกับฐานที่ทดสอบแล้วตรงกัน ไฟล์ SQLite backup อาจมี hash ทั้งไฟล์ต่างกันเพราะ header จึงเก็บทั้ง file hash และ logical table hashes ไม่อ้างว่า byte-identical

## สิ่งที่แก้ในตัวอ่านและหน้าเจ้าของ

1. ชื่อ Counter-Strike 2 เคยทำให้เลข 2 ถูกใช้เลือกปุ่ม 2 แม้ถามปุ่มทั้งหมด แก้ให้ projection ใช้คำถามหลังแยก entity
2. ข้อมูลที่ตอบได้เพียงบางขอบเขต เช่น อาหารภายนอก แสดง source ที่มีและบอกส่วนที่ยังไม่ยืนยัน ไม่ปัดตกเป็น validation error และไม่สร้างสิทธิ์นำอาหารใหม่
3. DraftView ของหน้าเจ้าของขาด connect/sources ทำให้ FAQ และกฎบางคำถามล้ม เพิ่ม read-only evidence access และแก้ป้ายข้อมูลจริงร่างที่เคยถูกมองเป็น synthetic demo
4. FAQ heading ที่มาจากคำค้น เช่น Afternoon — Close ไม่ถูกนำมาแสดงเป็นหัวข้อยืนยันสถานะ ใช้หัวข้อกลางและแสดงคำตอบจาก source
5. เปลี่ยนรหัส coverage ภายในเป็นคำอธิบายไทย/อังกฤษ และไม่แสดง metadata ค้นหา/ลำดับในคำตอบ “ทั้งหมด” โดยอัตโนมัติ เก็บข้อมูลครบในแบบฟอร์ม/trace
6. สืบ field เดิมเมื่อผู้ใช้เปลี่ยน entity แบบสั้นและ entity ใหม่รองรับ field นั้น เช่น PC notes → PS5 ไม่ต้องเขียน handler ใหม่ให้แต่ละช่องข้อมูล

## ผลทดสอบและข้อจำกัด

- Source-focused behavior: 210/210 เมื่อปิด LLM และ 210/210 เมื่อเปิด flag ON ทั้งสองภาษารวมอยู่ในชุดนี้ **ไม่มี model call** เพราะเป็นคำถามที่ reader ตีความได้ จึงไม่ใช่หลักฐานว่า LLM inference/transport ผ่าน
- Owner draft preview function และ backward compatibility 7/7 รวม payload เก่า 588 รายการ ตรวจผ่านก่อน patch เฉพาะ history ขั้นสุดท้าย ไม่มี actual HTTP/socket test ในรอบนี้
- Follow-up 6 บทสนทนา / 12 เทิร์นหลัง patch history ดู FOLLOWUPS_final06.json แยกจากตัวทดสอบเดิมที่ oracle อ่อน/ตั้งสมมติฐานกลุ่มผู้ใช้ผิด
- ชุดเดิม common OFF: 223 คำถาม / 503 grades เปรียบ R66 final20 ที่เก็บไว้กับ R67 final05; ไม่รัน legacy หรือ full 20,554 ซ้ำ ตัวเลขดูหัวข้อถัดไป
- การเปลี่ยนสุดท้ายหลัง final05 อยู่ใน resolve_state เมื่อมี previous_state เท่านั้น ตรวจ targeted followups เพิ่ม ผล 210 และ 223 เป็นรอบก่อน patch history นี้ ไม่อ้างว่าเป็น full rerun ของ final06

## คะแนนชุดเดิมไม่ได้ดีขึ้นทั้งหมด

R66 → R67: strict 133/503 → **123/503**; ไทย 90/324 → 90/324; อังกฤษ 43/179 → 33/179 มี 1 repair และ 11 regressions ตามเกณฑ์เดิม ต้องเก็บตัวเลขนี้ไว้คู่ผล targeted tests

11 regressions เกิดจาก 4 unique questions: เวลา afternoon, นำอาหาร, เครื่องดื่ม, อาหารภายนอก โดยส่วนใหญ่เพิ่ม route:knowledge ต่างจาก route เดิม; อาหารภายนอกมี literal “พื้นที่ที่ศูนย์กำหนด” ต่างจาก “พื้นที่ที่กำหนด” อีกเกณฑ์หนึ่ง คำตอบใหม่ยังระบุข้อจำกัดเรื่องอาหารภายนอกตาม source จึงไม่ได้แก้ wording/source ให้ตรง gold เพียงเพื่อผ่านคะแนน

ยังมี content-contract failed grades 31, source-alignment 39, presentation 30 และ protocol-only 294 กลุ่มซ้อนกันได้ ห้ามนับเป็นจำนวนคำถามผิดจริงทั้งหมดหรืออ้างว่าที่เหลือถูกหมด เก็บคำถาม คำตอบจริง และเหตุผลครบใน ALL_FAILED_GRADES_final05.md

ชุดนี้ไม่มี exception หรือ validation rejection; mean 0.434 s, p50 0.209 s, p95 1.152 s, max 16.917 s เป็น serial sample บนเครื่องนี้ ไม่ใช่ concurrency/SLA และไม่รับรอง production ที่ยังไม่ได้ restart/deploy

## สิ่งที่ยังต้องทำก่อนใช้แทนฐานจริง

- สิทธิ์เขียนโปรเจกต์และเครือข่าย: request_permissions คืน grant ว่างทั้งสองรายการ จึงยังไม่ deploy และยังทดสอบ actual local LLM/HTTP ไม่ได้ ไม่ใช้ช่องทางอื่นหลบข้อจำกัด
- อ่าน residual content/source contracts ต่อเป็นรายข้อ และปรับ behavioral coverage ของคำถามใหม่/คำถามหลายเจตนา ไม่ใช้ 210 source-focused cases แทนการพิสูจน์ทุก paraphrase
- Publication ยัง blocked {len(publication)} รายการ แยก metadata ที่เติมจาก source ได้ออกจาก facts ที่ยังไม่ทราบ ไม่เปิด draft override ใน production
- วันมีผลของราคา PC และตารางหลัง 31 มีนาคม, ระยะเวลาราคาเหมา, เวลาเปิดพื้นที่ และความต่างนโยบายเดิมยังต้องใช้หลักฐาน/คำยืนยันเฉพาะ อ่าน OWNER_CONFIRMATION_REQUIRED_R67_TH.md
- ไม่อ้างว่า preset/version/gameplay/current installation ยืนยันแล้วเพราะผังปุ่มย้ายครบ ไม่ใช้ source listing แทนสถานะจองสด ผู้ใช้ยืนยันสถานะจองจริงเดิมแล้ว ไม่ถาม lunch/VR occupancy ซ้ำ

## ไฟล์หลัก

- [คู่มือ Format ทุกหมวด](FORMAT_SPEC_R67_TH.md)
- [Flow และทบทวนแผน](FLOW_R67_TH.md)
- [ผลเทียบ R66/R67](PAIRED_R66_R67.json)
- [รายการเกณฑ์ที่ยังไม่ผ่านทั้งหมด](ALL_FAILED_GRADES_final05.md)
- [แผนนำเข้าและหลักฐานรักษาไฟล์เดิม](DELIVERY_final06/PLAN.json)
- [ฐานร่างที่เตรียมส่ง](DELIVERY_final06/candidate.sqlite)
'''
(B/'FINAL_REPORT_R67_TH.md').write_text(report,encoding='utf8')
print(json.dumps({'records':len(rs),'changed_code_files':len(changes),'code_conflicts':len(out['code_conflicts']),'changed_production_inputs':len(changed_inputs),'blocked_publication':len(publication),'schema_errors':errors,'candidate_logically_equal':True,'deployed':False},ensure_ascii=False))
