"""Package only the retained r57.4 old Flow, never the r58+ common/new Flow."""
import hashlib,json,shutil,zipfile,collections
from pathlib import Path

WORK=Path(__file__).resolve().parent;PROJECT=WORK.parent;ROOT=Path('C:/Users/Chokhun/Documents/Codex')
TARGET=ROOT/'PSU_Esports_Share_R56_20261010/02_With_Models';APP='system/PSU_Esports_Chatbot_Local'
OUTPUT=ROOT/'PSU_Old_Flow_Update_R57_20261027'
BASES=[ROOT/'PSU Esports Chatbot Ready 20261003',ROOT/'PSU_Esports_Share_20261003/01_Download_Models',ROOT/'PSU_Esports_Share_20261003/02_With_Models',ROOT/'PSU_Esports_Share_R50_20261009_66d96bb7/01_Download_Models',ROOT/'PSU_Esports_Share_R50_20261009_66d96bb7/02_With_Models',ROOT/'PSU_Esports_Share_R56_20261010/01_Download_Models',TARGET]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(p):return json.loads(p.read_text('utf-8-sig'))
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n','utf-8')
def inventory(root):
 pm=read(root/APP/'package_manifest.json');files={}
 top=['Start-Chatbot.cmd','Start-Chatbot.ps1','Stop-Chatbot.cmd','Stop-Chatbot.ps1','View-Chat-Logs.cmd','View-Chat-Logs.ps1','Setup-Models.cmd','Runtime-Process-Identity.ps1','README_TH.md','README_R56_TH.md','R57_SCOPE_CHECKS.json']
 for name in top:
  p=root/name
  if p.is_file():files[name]=p
 app=root/APP
 for p in app.iterdir():
  if p.is_file() and p.suffix.lower() in {'.md','.json','.ps1','.cmd'}:files[p.relative_to(root).as_posix()]=p
 folders=[app/n for n in ['app','web_chat','booking_dashboard','tools']]+[app/'data'/n for n in pm['included_data_directories']]+[root/'tools',root/'runtime/model_seed']
 for folder in folders:
  for p in folder.rglob('*'):
   if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.pyo'} and not any(x in p.relative_to(folder).parts for x in ['logs','chat_logs','.git']):files[p.relative_to(root).as_posix()]=p
 return files
if OUTPUT.exists():raise RuntimeError('Delivery output already exists; preserve it and choose a new release path.')
OUTPUT.mkdir()
sources=read(PROJECT/'r57_studio_scope_20261010_174001/source_hashes.json');assert len(sources)==151 and all(sha(TARGET/APP/k)==v for k,v in sources.items())
model=read(TARGET/'ready_manifest.json')['models'];assert all(read(p/'ready_manifest.json')['models']==model for p in BASES)
catalogs=[inventory(p) for p in BASES];target=catalogs[-1]
newreadme=WORK/'CURRENT_OLD_FLOW_README_TH.md'
newreadme.write_text('''# PSU Esports Chatbot — Flow เก่า r57.4

รุ่นที่เปิด: **2026.10.10-service-r57.4** · ชุดอัปเดตจัดทำ 27 ตุลาคม 2026

เปิด `Start-Chatbot.cmd` รอระบบพร้อมแล้วเว็บจะเปิดเอง ปิดด้วย `Stop-Chatbot.cmd`
ดูประวัติด้วย `View-Chat-Logs.cmd` ปิดแท็บเว็บอย่างเดียวไม่ได้หยุดโปรแกรม

ชุดนี้ใช้ Flow เก่าที่เก็บไว้ในชุดส่งต่อ r57.4 ไม่รวม Flow กลาง/Flow ใหม่ตั้งแต่ R58 ขึ้นไป
ชื่อโฟลเดอร์ต้นทางมี R56 แต่ ready_manifest และโค้ดตรงหลักฐาน r57.4 จริง
โมเดลสองตัวและ Python/Ollama ใช้ชุดเดิม ไม่ต้องโหลดโมเดลซ้ำหากไฟล์เดิมครบและไม่เสียหาย
สถานะจองสดยังต้องใช้อินเทอร์เน็ตและแหล่ง WordPress พร้อม ระบบไม่ได้จองหรือชำระเงินแทนผู้ใช้

การอัปเดตสำรองไฟล์ที่เปลี่ยนไว้ใน `_OldFlow_Update_Backups` ประวัติแชทอยู่ใน
`system/PSU_Esports_Chatbot_Local/data/logs` และคงไฟล์เดิมไว้
ถ้าพบข้อมูล/โค้ดที่แก้เองไม่ตรงชุดเดิม ตัวอัปเดตจะหยุดก่อนเปลี่ยนไฟล์และแจ้งรายการที่ต้องตรวจ

ผล R50/เอกสาร DELIVERY_CHECK ปี 2026-10-03 ที่อาจคงอยู่เป็นหลักฐานรุ่นก่อน
ขอบเขต r57.4 อ่าน README_R56_TH.md และ R57_SCOPE_CHECKS.json
การตรวจชุดอัปเดตนี้ไม่ใช่การยืนยันว่าเปิดได้บนเครื่องหัวหน้าหรือ Windows ใหม่ทุกเครื่องแล้ว
''','utf-8')
target=dict(target);target['README_TH.md']=newreadme
baseline_hashes={name:sorted({sha(cat[name]) for cat in catalogs if name in cat}) for name in set().union(*(set(c) for c in catalogs))}
files={};payload_bytes=0
for name,source in sorted(target.items()):
 wanted=sha(source);allowed=baseline_hashes.get(name,[])
 if any(name not in c for c in catalogs):allowed=allowed+[None]
 need=any(name not in c or sha(c[name])!=wanted for c in catalogs)
 item={'sha256':wanted,'bytes':source.stat().st_size,'allowed_before':allowed}
 if need:
  relative='payload/'+name;dest=OUTPUT/relative;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest);item['payload']=relative;payload_bytes+=source.stat().st_size
 files[name]=item
obsolete={name:hashes for name,hashes in baseline_hashes.items() if name not in target and name.startswith(APP+'/')}
manifests={}
for variant,folder in [('download_models',BASES[-2]),('with_models',TARGET)]:
 source=folder/'ready_manifest.json';rel='manifests/'+variant+'.json';dest=OUTPUT/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest)
 manifests[variant]={'sha256':sha(dest),'payload':rel,'allowed_before':sorted({sha(p/'ready_manifest.json') for p in BASES})}
versions=sorted({read(p/'ready_manifest.json')['runtime_version'] for p in BASES})
manifest={'version':1,'target_version':'2026.10.10-service-r57.4','source_revision':'r57.4','flow':'retained_old_flow_only','supported_versions':versions,'models':model,'files':files,'obsolete':obsolete,'ready_manifests':manifests,'weights_python_ollama_logs_state_in_payload':False}
write(OUTPUT/'UPDATE_MANIFEST.json',manifest)
updater=(WORK/'update_old_flow.py').read_text('utf-8').replace('MANIFEST_SHA256_PLACEHOLDER',sha(OUTPUT/'UPDATE_MANIFEST.json'));(OUTPUT/'update_old_flow.py').write_text(updater,'utf-8')
for name in ['Update-Old-Flow.ps1','Update-Old-Flow.cmd','README_UPDATE_TH.md']:
 shutil.copy2(WORK/name,OUTPUT/name)
# Verify the old ZIPs directly; these are the archives the receiver may have.
zip_checks=[]
for archive in (ROOT/'PSU_Esports_Share_20261003').glob('*.zip'):
 with zipfile.ZipFile(archive) as z:
  prefix=archive.stem+'/';cat=catalogs[1 if archive.stem.startswith('01_') else 2];checked=0
  for name,path in cat.items():
   actual=hashlib.sha256(z.read(prefix+name)).hexdigest();assert actual==sha(path),(archive.name,name);checked+=1
  zip_checks.append({'archive':str(archive),'managed_files_verified_against_archive':checked,'all_match':True})
sizes=collections.Counter();changed=[]
for name,item in files.items():
 if item.get('payload'):
  sizes['runtime_metadata' if name.startswith('runtime/model_seed') else 'application' if name.startswith(APP+'/app') else 'source_data' if name.startswith(APP+'/data') else 'web' if name.startswith(APP+'/web_chat') else 'launchers_and_docs']+=item['bytes'];changed.append(name)
proof={'target_version':manifest['target_version'],'old_flow_frozen_source_files_match':151,'new_flow_files_added':False,'model_names_and_digests_identical_across_all_baselines':True,'baseline_versions':versions,'source_packages':[str(p) for p in BASES],'original_zip_checks':zip_checks,'managed_target_files':len(files),'payload_files':len(changed),'obsolete_files':len(obsolete),'payload_bytes':payload_bytes,'payload_bytes_by_group':dict(sizes),'changed_source_data_files':[n for n in changed if n.startswith(APP+'/data')],'runtime_large_files_sent':[],'actual_inference_or_process_stops':0,'original_ready_or_shared_packages_modified':False}
write(WORK/'BUILD_AUDIT.json',proof);print(json.dumps({'output':str(OUTPUT),**proof},ensure_ascii=False))
