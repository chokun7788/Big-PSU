"""Allowlisted portable packages. Never copy operator logs, sessions or test DBs."""
import os,json,hashlib,shutil,sqlite3,urllib.request,zipfile,sys,time
from pathlib import Path
B=Path(__file__).resolve().parent
SYSTEM=B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
ENGINE=Path(os.environ['LOCALAPPDATA'])/'Programs/Ollama'
MODELSTORE=Path(os.environ['USERPROFILE'])/'.ollama/models'
OUT=B/'delivery'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while x:=f.read(4*1024*1024):h.update(x)
 return h.hexdigest()
def longpath(p):
 s=os.path.abspath(str(p))
 return Path(s if s.startswith('\\\\?\\') else '\\\\?\\'+s) if os.name=='nt' else Path(s)
def tree(src,dst):
 src=longpath(src);dst=longpath(dst)
 for p in src.rglob('*'):
  if not p.is_file() or '__pycache__' in p.parts or p.suffix in {'.pyc','.pyo'}:continue
  if any(x in p.parts for x in ('logs','common_test_tmp','sample_data','.git','.pytest_cache')):continue
  q=dst/p.relative_to(src)
  # The caller's workspace is long. Extended paths preserve every engine library.
  source=p;target=q
  if target.is_file() and source.stat().st_size==target.stat().st_size and sha(source)==sha(target):continue
  target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
def build():
 OUT.mkdir(exist_ok='--resume' in sys.argv)
 with_models=OUT/'PSU_Chatbot_With_Models';download=OUT/'PSU_Chatbot_Download_Models'
 download.mkdir(exist_ok='--resume' in sys.argv);manifest=json.loads((SYSTEM/'package_manifest.json').read_text(encoding='utf-8'))
 for folder in ['app','web_chat','booking_dashboard','runtime/python','docs','owner_content_docs']:
  tree(SYSTEM/folder,download/folder)
 for name in manifest['included_data_directories']:
  tree(SYSTEM/'data'/name,download/'data'/name)
 for p in SYSTEM.iterdir():
  if p.is_file() and (p.suffix.lower() in {'.ps1','.cmd','.md'} or p.name=='Model-Manifest-Check.py'):shutil.copy2(p,download/p.name)
 (download/'models').mkdir(exist_ok=True);shutil.copy2(SYSTEM/'models/Modelfile.bge-m3-1024',download/'models/Modelfile.bge-m3-1024')
 db=download/'data/knowledge/approved.sqlite';db.parent.mkdir(parents=True,exist_ok=True)
 with sqlite3.connect((SYSTEM/'data/knowledge/approved.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as src:
  with sqlite3.connect(db) as dst:src.backup(dst)
 (download/'runtime/ollama').mkdir(parents=True,exist_ok=True)
 shutil.copy2(ENGINE/'ollama.exe',download/'runtime/ollama/ollama.exe');tree(ENGINE/'lib',download/'runtime/ollama/lib')
 licenses=download/'licenses';licenses.mkdir(exist_ok=True)
 sources={
  'Ollama-LICENSE.txt':'https://raw.githubusercontent.com/ollama/ollama/main/LICENSE',
 }
 for name,url in sources.items():
  with urllib.request.urlopen(url,timeout=30) as response:body=response.read(100000)
  if b'MIT License' not in body:raise RuntimeError('Unexpected Ollama license response')
  (licenses/name).write_bytes(body)
 model_names=['registry.ollama.ai/scb10x/typhoon2.5-qwen3-4b/latest','registry.ollama.ai/library/bge-m3/latest','registry.ollama.ai/library/psu-bge-m3/q8_0']
 digest_set={}
 expected={}
 for name in model_names:
  m=json.loads((MODELSTORE/'manifests'/name).read_text())
  expected[name]={'config':m['config']['digest'],'layers':[{'digest':x['digest'],'size':x['size']} for x in m['layers']]}
  for layer in [m['config'],*m['layers']]:
   digest_set[layer['digest']]=layer['size']
   if layer['mediaType']=='application/vnd.ollama.image.license':
    (licenses/('Typhoon-LICENSE.txt' if 'typhoon' in name else 'BGE-M3-LICENSE.txt')).write_bytes((MODELSTORE/'blobs'/layer['digest'].replace(':','-')).read_bytes())
 shutil.copy2(SYSTEM/'runtime/python/LICENSE.txt',licenses/'Python-LICENSE.txt')
 (licenses/'SOURCES.md').write_text('# Included runtime and model license sources\n\n- Ollama: https://github.com/ollama/ollama/blob/main/LICENSE\n- Typhoon: https://huggingface.co/typhoon-ai/typhoon2.5-qwen3-4b\n- BGE-M3: https://huggingface.co/BAAI/bge-m3\n- Python: bundled LICENSE.txt\n\nModel license texts are copied from the installed model manifests. Engine libraries and their included notices are retained.\n',encoding='utf-8')
 (download/'models/expected_manifests.json').write_text(json.dumps(expected,indent=2),encoding='utf-8')
 with_models.mkdir(exist_ok='--resume' in sys.argv);tree(download,with_models)
 verified=[]
 for name in model_names:
  dst=with_models/'models/ollama/manifests'/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(MODELSTORE/'manifests'/name,dst)
 for digest,size in digest_set.items():
  source=MODELSTORE/'blobs'/digest.replace(':','-')
  if source.stat().st_size!=size or sha(source)!=digest.split(':')[1]:raise RuntimeError('Model digest mismatch '+digest)
  dst=with_models/'models/ollama/blobs'/source.name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dst)
  if sha(dst)!=digest.split(':')[1]:raise RuntimeError('Copied model digest mismatch')
  verified.append({'digest':digest,'size':size})
 for root,mode in [(download,'download_models'),(with_models,'models_included')]:
  m=dict(manifest);m.update(package_variant=mode,portable_ollama=True,portable_python=True,models_required=['scb10x/typhoon2.5-qwen3-4b','psu-bge-m3:q8_0'],fact_review_state='41 inherited drafts; no common release auto-approved by agent')
  m['excluded']=[x for x in m['excluded'] if x!='Ollama model weights']
  if mode=='download_models':m['excluded'].append('model weights; run Setup-Local-Models.cmd once')
  (root/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
  (root/'START_HERE_TH.md').write_text('''# เริ่มใช้ PSU Esports Chatbot

1. แตก ZIP ทั้งหมดลงโฟลเดอร์ที่เขียนไฟล์ได้ เช่น Documents ของผู้ใช้ Windows 64-bit อย่ารันจากใน ZIP หรือ Program Files
2. เปิด Open-PSU-Esports-Background.cmd แล้วรอระบบตรวจความพร้อมก่อนเปิดเว็บ
3. แบบ With_Models มีโมเดลแล้ว แบบ Download_Models ต้องเปิด Setup-Local-Models.cmd พร้อมอินเทอร์เน็ตครั้งแรก
4. เจ้าของเปิด Open-Owner-Content.cmd เพื่อเพิ่มหรือแก้ข้อมูลเดิม เลือกหมวด กรอกช่องพร้อมตัวอย่าง บันทึกร่าง ทดสอบร่าง ตรวจข้อเท็จจริง อนุมัติและเผยแพร่
5. ข้อมูลร่างยังไม่ใช้ตอบลูกค้า หลังเผยแพร่ แชทอ่าน release ใหม่อัตโนมัติ ไม่ต้องแก้โค้ดตามชื่อเกม
6. เกมที่เพิ่มเฉพาะรายละเอียด ยังไม่ได้ยืนยันว่ามีให้เล่น ต้องเพิ่มข้อมูลเกมกับบริการ/แพลตฟอร์มที่เกี่ยวข้องด้วย
7. ปิดหน้าต่างเว็บไม่หยุดบริการ เครื่องที่รันต้องเปิดอยู่ ข้อมูลการจองสดต้องมีอินเทอร์เน็ตและแหล่ง WordPress ที่เข้าถึงได้
8. ดูคู่มือ OWNER_CONTENT_GUIDE_TH.md และ PRODUCTION_OPERATION_TH.md การเปลี่ยนราคาใช้รหัสรายการเดิม แก้ revision แล้วเผยแพร่ ไม่สร้างรายการราคาซ้ำ

ชุดนี้เปิดบนเครื่อง Windows ของผู้ใช้ผ่าน 127.0.0.1 หากจะให้ลูกค้าบนอินเทอร์เน็ตเข้าเว็บเดียวกัน ต้องจัด host, HTTPS และระบบผู้ดูแลตามเอกสาร Deploy; ห้ามเปิด owner editor ออกสาธารณะ

ข้อมูลเดิมและ draft ที่ส่งมาจากเจ้าของยังคงสถานะเดิม ไม่มีการอนุมัติข้อเท็จจริงแทนเจ้าของ ข้อมูลทดลองและประวัติแชทจากเครื่องพัฒนาไม่ได้รวมในชุดนี้
''',encoding='utf-8')
 receipt={'variants':[str(download),str(with_models)],'verified_model_blobs':verified,'synthetic_databases_included':False,'operator_logs_or_capabilities_included':False,'owner_db_snapshot':'SQLite read-only backup of inherited facts, same approval state'}
 (B/'PACKAGE_BUILD.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(receipt,ensure_ascii=False),flush=True)
def archives():
 receipts=[]
 for root in sorted(OUT.iterdir()):
  if not root.is_dir():continue
  target=OUT/(root.name+'.zip')
  with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
   for p in longpath(root).rglob('*'):
    if p.is_file() and not any(x in p.parts for x in ('logs','runtime_state')) and p.name not in {'owner-session.json','model-service.json'} and not (p.parent.name=='runtime' and p.parent.parent.name=='data'):
     z.write(p,(Path(root.name)/p.relative_to(longpath(root))).as_posix())
  with zipfile.ZipFile(target) as z:
   assert z.testzip() is None
   names=z.namelist()
   assert not any('/logs/' in n or 'owner-session.json' in n or 'DEMO_' in n for n in names)
  receipts.append({'path':str(target),'bytes':target.stat().st_size,'sha256':sha(target),'archive_integrity':'all CRC passed'})
  print(receipts[-1],flush=True)
 (B/'ARCHIVES.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':build() if sys.argv[1]=='build' else archives()
