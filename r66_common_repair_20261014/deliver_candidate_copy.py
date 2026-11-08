"""Copy the verified, unpublished candidate to a NEW project folder only."""
import sys,json,sqlite3,hashlib,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1]
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data').resolve()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
verified=read(B/('VERIFIED_'+tag+'.json'));assert verified.get('complete')
deployed=read(B/('DEPLOY_'+tag)/'APPLIED.json');assert deployed['protected_database_hashes_equal']
source=B/('FINAL_'+tag)/'common_end.sqlite';digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(source)==verified['database_sha256']
with sqlite3.connect(source.as_uri()+'?mode=ro',uri=True) as c:
 meta=dict(c.execute('SELECT key,value FROM cc_meta'));count=c.execute('SELECT count(*) FROM cc_heads WHERE withdrawn=0').fetchone()[0];approvals=c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0];synthetic=sum(json.loads(row[0]).get('trust')=='synthetic' for row in c.execute('SELECT payload FROM cc_sources'))
assert not meta['active'] and meta['demo']=='0' and count==588 and approvals==0 and synthetic==0
out=(ROOT/'data/knowledge/migration_r66_20261015').resolve();assert out.is_relative_to(ROOT/'data/knowledge') and not out.exists()
protected={p:digest(Path(p)) for p in deployed['protected_databases'] if Path(p).is_file()}
out.mkdir();target=out/'candidate.sqlite';shutil.copy2(source,target);assert digest(target)==verified['database_sha256']
guide=r'''# ร่าง Format กลาง R66 — ยังไม่เผยแพร่

candidate.sqlite เป็นร่างข้อมูลจริง 588 รายการ: เก็บ 582 รายการเดิม และ PC rates จาก source เดิม 6 รายการ ไม่มี synthetic fixtures ไม่มี approvals และ active release ว่าง ไม่ได้แทนฐานข้อมูลที่ Chatbot ใช้งานอยู่

การแก้คำแปล/ฟิลด์เป็น revision ใหม่พร้อม source lineage เก็บต้นฉบับเดิม วันมีผลหรือกฎที่ไม่ทราบยังเป็น unknown ต้องจัดการ release gates ก่อนเผยแพร่ ไม่เปิด evaluation draft override ใน production

เปิดร่างนี้ด้วยตัวเปิดแยก โดยใช้ runtime ของโปรเจกต์:

```powershell
.\data\knowledge\migration_r66_20261015\Open-R66-Draft.ps1
```

หากเครื่องเลือก Python ไม่ตรง ให้ส่ง -PythonPath เป็น Python 3.12 ตัวเดียวกับที่ใช้เปิด Chatbot ตัวเปิดจะส่งฐานข้อมูลร่างเฉพาะไปยัง Owner editor และคืนค่า environment เดิมเมื่อเปิดเสร็จ ไม่เปลี่ยน default DB ของ launcher หลัก

ถ้าต้องการเปิดร่างนี้ใน Owner editor ให้รันจากโฟลเดอร์โปรเจกต์ด้วย Python environment ของโปรเจกต์:

```powershell
python -m app.knowledge.common.owner_server --db "data/knowledge/migration_r66_20261015/candidate.sqlite" --port 8099
```

เลือกทดสอบร่างเพื่อดูข้อมูลในไฟล์นี้ การทดสอบร่างไม่ใช่การเผยแพร่ ห้ามอ้างว่าไฟล์ชื่อ candidate ได้รับอนุมัติแล้ว

รายงาน Flow และคำถามที่ต้องใช้ข้อมูลจริงเพิ่มเติมอยู่ในโฟลเดอร์งาน R66 ตาม delivery manifest ด้านล่าง โค้ดมี before backups แยกต่างหาก ไม่ได้อัปเดต portable packages หรือ restart Chatbot ที่เปิดค้างโดยอัตโนมัติ
'''
(out/'README_DRAFT_TH.md').write_text(guide,encoding='utf-8')
launcher='''param([int]$Port=8099,[string]$PythonPath='', [switch]$NoBrowser)
$ErrorActionPreference='Stop'
$r66ProjectRoot=(Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\\..\\..')).Path
$r66Candidate=Join-Path $PSScriptRoot 'candidate.sqlite'
if(-not (Test-Path -LiteralPath $r66Candidate)){throw 'R66 candidate.sqlite is missing.'}
$r66PreviousDatabase=$env:PSU_KNOWLEDGE_DB
try {
    $env:PSU_KNOWLEDGE_DB=$r66Candidate
    & (Join-Path $r66ProjectRoot 'Open-Owner-Content.ps1') -Port $Port -PythonPath $PythonPath -NoBrowser:$NoBrowser
} finally {
    $env:PSU_KNOWLEDGE_DB=$r66PreviousDatabase
}
'''
(out/'Open-R66-Draft.ps1').write_text(launcher,encoding='utf-8-sig')
assert all(digest(Path(p))==v for p,v in protected.items())
manifest={'tested_tag':tag,'candidate_path':str(target),'sha256':digest(target),'records':count,'active_release':meta['active'],'approvals':approvals,'synthetic_sources':synthetic,'default_production_database_changed':False,'protected_database_hashes_unchanged':True,'analysis_directory':str(B),'code_deployment_manifest':str(B/('DEPLOY_'+tag)/'APPLIED.json')}
(out/'DELIVERY.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(B/('CANDIDATE_DELIVERED_'+tag+'.json')).write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(manifest,ensure_ascii=False,indent=2))
