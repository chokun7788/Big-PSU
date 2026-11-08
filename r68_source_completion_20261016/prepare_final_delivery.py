import collections,hashlib,json,shutil,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import CATALOG,validate,value
R=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');D=B/'DELIVERY_final';D.mkdir(exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf8')
base=B.parent/'r66_common_repair_20261014/system';previous=B.parent/'r67_migration_parity_20261015/system'
manifest=[];changes=[];r67changes=[]
for p in sorted((B/'system/app').rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts:continue
 rel=p.relative_to(B/'system');h=sha(p);manifest.append({'path':rel.as_posix(),'sha256':h})
 if sha(previous/rel)!=h:r67changes.append(rel.as_posix())
 if sha(base/rel)==h:continue
 actual=sha(R/rel);expected=sha(base/rel)
 changes.append({'path':rel.as_posix(),'expected_old_sha256':expected,'actual_root_sha256':actual,'new_sha256':h,'conflict':actual!=expected})
 if actual:
  t=D/'before'/rel;t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/rel,t)
dump(B/'FROZEN_CODE_MANIFEST_final.json',manifest)
with sqlite3.connect((B/'candidate06.sqlite').as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(D/'candidate.sqlite') as b:a.backup(b)
def logical(p):
 with sqlite3.connect(p.as_uri()+'?mode=ro',uri=True) as c:
  out={}
  for (table,) in c.execute("select name from sqlite_master where type='table' order by name").fetchall():
   q='"'+table.replace('"','""')+'"';rows=sorted(json.dumps(row,ensure_ascii=False,default=lambda v:v.hex() if isinstance(v,bytes) else str(v)) for row in c.execute('select * from '+q).fetchall());out[table]={'rows':len(rows),'sha256':hashlib.sha256('\n'.join(rows).encode()).hexdigest()}
  return out
tables=logical(B/'candidate06.sqlite');assert tables==logical(D/'candidate.sqlite')
store=CommonStore(D/'candidate.sqlite')
with store.connect() as c:rs=store.heads(c);sources=store.sources(c);meta=dict(c.execute('select key,value from cc_meta'));approvals=c.execute('select count(*) from cc_approvals').fetchone()[0]
errors={rid:e for rid,r in rs.items() if (e:=validate(r,rs,sources))};assert not errors
blocked={rid:e for rid,r in rs.items() if (e:=validate(r,rs,sources,publish=True))}
dump(B/'PUBLICATION_BLOCKERS_final.json',blocked)
dump(D/'migration.bundle.json',{'schema_version':'studio-content-3.0','records':list(rs.values()),'sources':[{'source':pair[0],'snapshot':pair[1]} for pair in sources.values()],'mode':'draft_only','build_id':'common-r68-source-completion','approvals_included':False})
protected=[{'path':rel,'sha256':sha(R/rel)} for rel in ['data/knowledge/approved.sqlite','data/knowledge/migration_r63_20261013/approved.sqlite','data/knowledge/migration_r66_20261015/candidate.sqlite'] if (R/rel).is_file()]
plan={'date':'2026-10-16','root':str(R),'candidate_target':'data/knowledge/migration_r68_20261016/candidate.sqlite','heads':len(rs),'candidate_sha256':sha(D/'candidate.sqlite'),'logical_tables':tables,'backup_matches_test_database':True,'changes':changes,'changed_code_files_since_r67':r67changes,'conflicts':[x for x in changes if x['conflict']],'protected_databases':protected,'schema_errors':errors,'active_release':meta.get('active'),'approvals':approvals,'publication_blocked_records':len(blocked),'deployed':False,'project_write_permission_granted':False,'network_permission_granted':False}
dump(D/'PLAN.json',plan)
spec=['# คู่มือช่องข้อมูลเพิ่มเติม R68','','ใช้ candidate06.sqlite หรือ DELIVERY_final/candidate.sqlite เท่านั้น เปิดทดลองร่างด้วย Open-R68-Drafts.cmd พอร์ต 8100 ต้องมี runtime ของ r58 อยู่ข้างโฟลเดอร์นี้ ผลยังไม่ใช่ production release และยังไม่เปลี่ยนเว็บเดิม','',
'## ช่องใหม่และช่องที่คืนข้อมูล','','- เกม: official_description เก็บข้อความฉบับเต็ม; description_captured_at เป็นเวลาจับข้อมูล; description_scope_note เก็บข้อจำกัด แยกจาก summary ที่เป็นคำอธิบายสั้น','- เกม: venue_zone_ids เลือกโซนของศูนย์ตามไฟล์ inventory; supported_platforms ใช้ความเข้ากันได้ทั่วไปของเกม ห้ามใช้สองช่องนี้แทนกัน','- บริการ: inventory_verified_on และ inventory_basis ใช้ระบุที่มา/วันที่ของรายการเกมและเครื่อง ไม่ใช่ผลว่างหรือถูกจองสด','- อุปกรณ์: device_type ใช้จัดประเภท; specifications มี key/value/unit เช่น CPU / Intel Core i5-14400 / null ส่วนคำแนะนำใช้งานเก็บใน usage ตามเดิม','- การแข่งขัน: source_title ใช้ชื่อหัวเอกสารจริง; division ใช้เฉพาะที่ระบุจริง เช่น ประเภททีมชาย; facet เป็นหมวดค้นหาจากฉบับเก่า ไม่ใช่การรับรองความครบของกติกา','- ติดต่อ/ขั้นตอน: name เป็นชื่อแสดงไทยและอังกฤษ; contact.value เป็นลิงก์จริง ส่วน procedure.topic เป็นรหัสหัวข้อภายในและ steps เป็นลำดับให้ผู้ใช้ทำ','',
'## ตัวอย่างแก้ข้อมูลเดิม','','1. ค้นหาเกม/บริการเดิม แล้วเลือกแก้รายการเดิม ไม่ตั้งรหัสใหม่สำหรับการแก้คำบรรยาย','2. กรอกช่องที่ทราบตามแหล่งต้นฉบับ ใส่ source และ locator; ไม่ทราบจำนวนผู้เล่น วันมีผล หรือตัวตนเครื่อง ให้เก็บ unknown','3. ถ้าเกมเป็นคนละภาค/edition ให้แยกรายการ อย่าเพิ่มเป็น alias ของอีกภาค','4. ใช้หน้า “ทดลองร่าง” ถามทั้งไทยและอังกฤษ แล้วตรวจข้อความปลายคำตอบและเงื่อนไข ไม่ตรวจแค่มีชื่อเกม','5. บันทึก revision และผ่านขั้นตอนตรวจ/เผยแพร่เดิมก่อนเปลี่ยนข้อมูล production','',
'## ทุกหมวดใน registry','','| หมวด | รายการในฐานร่าง | ช่องที่รู้ค่า / ช่องที่มีอยู่ |','|---|---:|---:|']
for kind in CATALOG:
 rows=[r for r in rs.values() if r['kind']==kind];known=sum(f['status']=='known' for r in rows for f in r['fields'].values());total=sum(len(r['fields']) for r in rows);spec.append(f"| {CATALOG[kind]['owner_form']} ({kind}) | {len(rows)} | {known}/{total} |")
spec+=['','จำนวนช่องที่รู้ค่าไม่ใช่คะแนนความถูกต้องหรือการอนุมัติ หมวดที่ยังไม่มีข้อมูลจริงจะไม่สร้างรายการตัวอย่างปนในฐานนี้ อ่าน R67/FORMAT_SPEC_R67_TH.md สำหรับความหมายช่องเดิมและ OWNER_CONFIRMATION_REQUIRED_R67_TH.md สำหรับขอบเขตนโยบายที่ยังต้องยืนยัน']
(B/'FORMAT_GUIDE_R68_TH.md').write_text('\n'.join(spec)+'\n',encoding='utf8')
print(json.dumps({'heads':len(rs),'changed_code_files_vs_actual_base':len(changes),'changed_code_files_since_r67':len(r67changes),'conflicts':len(plan['conflicts']),'publication_blocked':len(blocked),'candidate_sha256':plan['candidate_sha256']},ensure_ascii=False))
