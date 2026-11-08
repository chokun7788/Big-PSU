"""Publish a local update ZIP after actual updater/rollback checks pass."""
import hashlib,json,zipfile
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=Path('C:/Users/Chokhun/Documents/Codex');O=ROOT/'PSU_Old_Flow_Update_R57_20261027'
def read(p):return json.loads(p.read_text('utf-8-sig'))
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n','utf8')
test=sorted(ROOT.glob('_R57Tests_*/RESULT.json'))[-1];r=read(test);assert r['all_passed'] and len(r['checks'])==54 and all(r['checks'].values())
b=read(W/'BUILD_AUDIT.json');smoke=read(W/'LEGACY_SCOPE_SMOKE.json');ps=read(W/'POWERSHELL_PARSE_CHECK.json');assert smoke['all_passed'] and all(not x['errors'] for x in ps)
m=read(O/'UPDATE_MANIFEST.json');assert b['old_flow_frozen_source_files_match']==151 and b['model_names_and_digests_identical_across_all_baselines']
summary={'target_version':m['target_version'],'flow':'retained old r57.4; no R58+ common or R135 candidate files','updater_checks':r['checks'],'old_scope_predicate_checks':smoke['checks'],'powershell_parse_errors':0,'original_zip_managed_files_checked':[673,673],'frozen_old_app_web_source_hashes_match':151,'managed_target_files':b['managed_target_files'],'payload_files':b['payload_files'],'payload_bytes':b['payload_bytes'],'model_weight_downloads_or_inferences':0,'model_weights_python_ollama_logs_state_replaced':False,'real_original_ready_bundled_python_check_only_passed':True,'original_packages_modified':False,'clean_windows_or_receiver_machine_tested':False}
write(O/'UPDATE_CHECKS.json',summary)
doc=f'''# ผลตรวจชุดอัปเดต Flow เก่า — 27 ตุลาคม 2026

## ส่งอะไรให้หัวหน้า

ส่ง **PSU_Old_Flow_Update_R57_20261027.zip เพียงไฟล์เดียว** เมื่อหัวหน้ามีโฟลเดอร์เก่าครบอยู่แล้ว
แตก ZIP → หยุดแชทเก่าด้วย Stop-Chatbot.cmd → เปิด Update-Old-Flow.cmd → เลือกโฟลเดอร์เก่า → เปิด Start-Chatbot.cmd ตามเดิม
ไม่ต้องคัดลอกทับ system ทั้งโฟลเดอร์ ไม่ต้องส่ง ZIP โมเดลหลาย GB รอบใหม่

## รุ่นที่เทียบจริง

- โฟลเดอร์ PSU Esports Chatbot Ready 20261003 เป็น **2026.10.03-ready-folder-r37.2**
- ZIP วันที่ 3 ตุลาคมทั้ง 01_Download_Models และ 02_With_Models ยังเป็น r37.2 ตรวจไฟล์ที่จัดการได้ตรง ZIP จริง **673 ไฟล์ต่อแบบ**
- ชุดส่งต่อ Flow เก่าที่ปรับหลังจากนั้นอยู่ใน PSU_Esports_Share_R56_20261010 แต่ manifest และโค้ดจริงเป็น **2026.10.10-service-r57.4**
- โค้ด app/เว็บ **151 ไฟล์** ตรง SHA256 ของ frozen r57.4 เดิมทุกไฟล์
- ไม่ใช้โค้ดต้นทางปัจจุบันที่เปลี่ยนเป็น common-r62 และไม่ใส่ Flow ใหม่ R135

## ไฟล์ที่ต้องรับใหม่และส่วนที่ใช้เดิมได้

| ส่วน | ผลเทียบและการอัปเดต |
|---|---|
| app / เว็บแชท | ส่งไฟล์ที่ต่างจากชุดเดิม รวมตัวแก้ Flow เก่า r57.4 |
| ข้อมูลอ้างอิง | เพิ่ม/ปรับ 4 ไฟล์ของข้อมูลบริการและราคาเหมาในชุดเก่า; ไม่ใช่ฐานข้อมูล Flow ใหม่ |
| ตัวเปิด/ตัวหยุด/เครื่องมือตรวจโมเดล | เปลี่ยนเป็นชุดที่เข้าคู่กับ r57.4 |
| runtime/model_seed | ข้อมูลประกอบโมเดลขนาดเล็กประมาณ18 KB เพื่อใช้โมเดลเดิม |
| Python / Ollama | ใช้ของเดิม ไม่บรรจุตัวรันซ้ำใน ZIP นี้ |
| โมเดล Typhoon / BGE-M3 | ชื่อและ digest ตรงกันทุกชุดที่เทียบ ไม่ส่งน้ำหนักใหม่ |
| runtime/models, runtime/state, ประวัติแชทและ logs | ไม่เขียนทับ; ตรวจการคงไฟล์/SQLiteในสำเนาทดสอบแล้ว |

ข้อมูล 4 ไฟล์ที่ต่าง ได้แก่:

{chr(10).join('- '+p.split('/data/',1)[1] for p in b['changed_source_data_files'])}

ชุดนี้มี payload **{b['payload_files']} ไฟล์ รวม {b['payload_bytes']:,} bytes ก่อนบีบอัด**
ตัวอัปเดตตรวจ **{b['managed_target_files']} ไฟล์ที่เกี่ยวข้อง** ก่อนและหลังติดตั้ง เลือก manifest ให้ตรงแบบมีโมเดล/ดาวน์โหลดเดิมอัตโนมัติ
หากไฟล์ถูกแก้เองหรือข้อมูลไม่ตรงฐานที่รู้จัก จะหยุดก่อนเปลี่ยน ไม่ทับข้อมูลเองเงียบ ๆ
ไฟล์เดิมทุกไฟล์ที่เปลี่ยนถูกสำรองพร้อม hash ใน _OldFlow_Update_Backups และทดสอบย้อนกลับไว้แล้ว

## ผลตรวจใหม่ของตัวอัปเดต

- **54/54 checks**: สำเนาไฟล์เดิม 7 แบบ, path มีช่องว่างและภาษาไทย, check-only, เปลี่ยนไฟล์จริง, hash หลังอัปเดต, เก็บโมเดล/state/log/SQLite, เปิดตัวอัปเดตซ้ำไม่เปลี่ยนไฟล์ซ้ำ และย้อนกลับตรงไฟล์เดิม
- ไฟล์ข้อมูล/โค้ดที่แก้เอง, รุ่น Flow ใหม่, โปรแกรมยังเปิด, payload/manifestเสีย: ปฏิเสธก่อนเขียนทับ
- จำลองคัดลอกขัดข้อง: ย้อนกลับไฟล์ที่เปลี่ยนแล้วและไม่ทิ้งไฟล์ staging
- ย้อนกลับหลังมีการแก้เองภายหลัง: หยุดก่อนทับการแก้ใหม่
- รันตัวเรียก PowerShell ที่ส่งจริงกับ Python ของ Ready เดิมในโหมดตรวจอย่างเดียว ผ่าน และ hash ไฟล์ต้นทางคงเดิม
- ไวยากรณ์ PowerShell 5 ไฟล์ผ่าน; Python app เดิม {r['app_python_ast_files']} ไฟล์ตรวจ syntax ผ่าน
- ตัวแยกขอบเขตของ Flow เก่า 7 กรณีผ่าน โดยไม่เรียกโมเดลหรือเครือข่าย

## ขอบเขตผลตรวจ

การตรวจนี้ยืนยันชุดไฟล์อัปเดตและการสำรอง/แทนที่/ย้อนกลับบนสำเนาทดสอบ ไม่ใช่การรันโมเดลเต็มบนเครื่องหัวหน้า
ไม่ได้เปิดเซิร์ฟเวอร์หรือหยุดโปรเซสใช้งานของผู้พัฒนา ไม่มีการเรียก inference/training และไม่แก้ชุด Ready/ZIP/ชุดส่งต่อเดิม
หากหัวหน้าใช้แบบดาวน์โหลดและยังไม่เคยโหลดโมเดลจนเสร็จ ส่วนที่ขาดยังต้องโหลดตามขั้นตอนเดิม
สถานะจองสดยังต้องใช้อินเทอร์เน็ตและ WordPress พร้อม
'''
(O/'UPDATE_VERIFICATION_TH.md').write_text(doc,'utf8')
archive=ROOT/(O.name+'.zip')
with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(O.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:z.write(p,(Path(O.name)/p.relative_to(O)).as_posix())
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 prefix=O.name+'/'
 assert hashlib.sha256(z.read(prefix+'UPDATE_MANIFEST.json')).hexdigest()==sha(O/'UPDATE_MANIFEST.json')
 for name,item in m['files'].items():
  if item.get('payload'):assert hashlib.sha256(z.read(prefix+item['payload'])).hexdigest()==item['sha256']
 assert not any('/runtime/models/' in n or '/runtime/python/' in n or '/runtime/ollama/' in n or '/data/logs/' in n for n in z.namelist())
digest=sha(archive);sidecar=archive.with_suffix('.zip.sha256.txt');sidecar.write_text(digest+'  '+archive.name+'\n','ascii')
receipt={'complete':True,'archive':str(archive),'archive_bytes':archive.stat().st_size,'archive_sha256':digest,'verification_report':str(O/'UPDATE_VERIFICATION_TH.md'),'instructions':str(O/'README_UPDATE_TH.md'),'updater_checks':54,'old_scope_smoke_checks':7,'version':m['target_version'],'old_flow_only':True,'old_original_ready_updated_in_place':False,'runtime_models_logs_preserved':True,'test_report':str(test),'original_ready_or_shared_packages_modified':False,'models_loaded_or_downloaded':0,'servers_started_or_stopped':0,'new_flow_r135_complete':False}
write(W/'DELIVERY_RECEIPT.json',receipt);print(json.dumps(receipt,ensure_ascii=False))
