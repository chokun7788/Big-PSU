import sys,shutil,json,hashlib,time
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');OLD=BASE.parents[1]/'PSU_Esports_Share_R50_20261009_66d96bb7'
NEW=BASE.parents[1]/'PSU_Esports_Share_R56_20261010';NEW.mkdir();VERSION='2026.10.10-service-r56.5';records=[]
assert shutil.disk_usage(OUT).free>12*1024**3
def ignore(p,names):
    path=Path(p);ignored=[n for n in names if n in ('__pycache__','.git') or n.endswith('.pyc')]
    if path.name=='runtime':ignored += [n for n in names if n=='state']
    if path.name=='data':ignored += [n for n in names if n in ('logs','chat_logs')]
    return ignored
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
for variant in ('01_Download_Models','02_With_Models'):
    dest=NEW/variant;shutil.copytree(OLD/variant,dest,ignore=ignore);app=dest/'system/PSU_Esports_Chatbot_Local'
    for folder in ('app','web_chat','booking_dashboard'):
        shutil.copytree(ROOT/folder,app/folder,dirs_exist_ok=True,ignore=ignore)
    pm=json.loads((app/'package_manifest.json').read_text(encoding='utf-8'))
    for folder in pm['included_data_directories']:
        shutil.copytree(ROOT/'data'/folder,app/'data'/folder,dirs_exist_ok=True,ignore=ignore)
    pm.update(runtime_version=VERSION,parent_runtime_version='2026.10.09-flow-r50.2',source_revision='r56.4',original_package_kept=True)
    (app/'package_manifest.json').write_text(json.dumps(pm,ensure_ascii=False,indent=2),encoding='utf-8')
    ready=json.loads((dest/'ready_manifest.json').read_text(encoding='utf-8-sig'));ready.update(runtime_version=VERSION,parent_runtime_version='2026.10.09-flow-r50.2')
    (dest/'ready_manifest.json').write_text(json.dumps(ready,ensure_ascii=False,indent=2),encoding='utf-8')
    p=app/'Start-PSU-Esports-Chatbot.ps1';t=p.read_text(encoding='utf-8-sig')
    import re
    t=re.sub(r'\$env:PSU_RUNTIME_VERSION = "[^"\n]+"', "$env:PSU_RUNTIME_VERSION = (Get-Content -LiteralPath (Join-Path $projectRoot 'package_manifest.json') -Raw | ConvertFrom-Json).runtime_version",t,count=1)
    assert 'Get-Content -LiteralPath' in t
    t=t.replace('$env:PSU_PIPELINE_WORKER_SUPERVISOR = "1"','$env:PSU_PIPELINE_WORKER_SUPERVISOR = "1"\n$env:PSU_CHAT_JOBS_ENABLED = "1"\n$env:PSU_LLM_MAX_CONCURRENCY = "1"\n$env:PSU_PIPELINE_WORKERS = "2"')
    p.write_text(t,encoding='utf-8-sig')
    (dest/'README_R56_TH.md').write_text(f'''# PSU Esports Chatbot r56

รุ่น {VERSION} · Windows x64 · เปิด `Start-Chatbot.cmd` ในโฟลเดอร์นี้

- 01_Download_Models: ดาวน์โหลดโมเดลครั้งแรกประมาณ 3.65 GB แล้วใช้โมเดลในเครื่อง
- 02_With_Models: มีไฟล์โมเดลแล้ว เปิดใช้ได้เมื่อเครื่องผ่านข้อกำหนด runtime
- สถานะจองต้องใช้อินเทอร์เน็ตเพื่อดึง WordPress; การมีโมเดลไม่ได้ทำให้สถานะจองใช้ออฟไลน์ได้
- เปิด Start แล้วรอพร้อม / หยุดด้วย Stop-Chatbot.cmd / ดู log ด้วย View-Chat-Logs.cmd
- เก็บทั้งโฟลเดอร์ด้วยกัน; สำเนานี้ไม่รวมประวัติสนทนาและ state ของเครื่องผู้พัฒนา
- กฎ RoV แสดงคำแปลข้อความที่อ่านได้ แต่ 6.1.5/6.1.5.1 ต้นฉบับที่บันทึกไว้ยังไม่ครบ; ไม่มีการยืนยันบทลงโทษส่วนที่ขาด
- ข้อมูลนโยบายที่เจ้าของยังไม่ได้ตอบยังแสดงว่าไม่ยืนยัน; ราคา non-PC เป็นอัตราในตารางที่มีวันสิ้นสุดเดิม

รายงาน R50/เก่าที่ติดมาคือหลักฐานรุ่นก่อน การตรวจรุ่นนี้ดู `R56_BUILD_CHECKS.json` และรายงานรอบ r56
การทดสอบบนเครื่องพัฒนาครั้งนี้ยังไม่ใช่การรับรอง clean Windows/VM ทุกเครื่อง
''',encoding='utf-8')
    files={str(p.relative_to(app)):sha(p) for p in app.rglob('*') if p.is_file() and ('app'==p.relative_to(app).parts[0] or 'web_chat'==p.relative_to(app).parts[0]) and '__pycache__' not in p.parts}
    owner=json.loads((OUT/'owner_hashes_before.json').read_text(encoding='utf-8'))
    owner_match=all((app/k).is_file() and sha(app/k)==v for k,v in owner.items())
    weights=[dict(sha256=b['sha256'],exists=(dest/'runtime/models/blobs'/('sha256-'+b['sha256'])).exists()) for b in ready['model_blobs']]
    check=dict(variant=variant,runtime=VERSION,path=str(dest),owner_files=len(owner),owner_hashes_match=owner_match,model_weights=weights,source_hashes=files,total_bytes=sum(p.stat().st_size for p in dest.rglob('*') if p.is_file()),clean_machine_tested=False)
    assert owner_match;records.append(check)
    (dest/'R56_BUILD_CHECKS.json').write_text(json.dumps(check,indent=2),encoding='utf-8');print(variant,check['total_bytes'],'owner',owner_match,flush=True)
(OUT/'packages.json').write_text(json.dumps(records,indent=2),encoding='utf-8');print(NEW)
