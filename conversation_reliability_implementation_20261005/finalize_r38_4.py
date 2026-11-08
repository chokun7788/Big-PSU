import ast, hashlib, json, subprocess, zipfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
PACKAGE=HERE/'release_r38_4'/'PSU_Esports_Chatbot_Local'

notes='''# ชุดปรับบริบทการสนทนา r38.4 — 5 ตุลาคม 2026

เปิด `Open-PSU-Esports-Background.cmd` เพื่อใช้แชทบอท ตัวเปิดจะค้นหาชุดนี้ที่กำลังรันอยู่หรือเลือกพอร์ตว่าง 8090–8099 และรอให้พร้อมก่อนเปิดเว็บ

เครื่องนี้มี Python, Ollama และโมเดลที่ต้องการอยู่แล้ว ชุดนี้ไม่ได้บรรจุ Python หรือโมเดลสำหรับเครื่องอื่น ตรวจ README และใช้ Setup-Local-Models.cmd หลังติดตั้ง Python/Ollama หากย้ายไปเครื่องอื่น

ลอง: “ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก” แล้วตอบ “PC” / “ทั้งหมด” / “แล้ว VR ล่ะ”; ภาษาอังกฤษใช้ “Service prices for external users” แล้ว “PC” / “all of them” ได้

ลองกติกา: “กติกาการแข่งขัน CS2” → “ขอรายละเอียดทั้งหมด” → “ต่อ” เพื่ออ่านทีละส่วน ระบบแสดงแหล่งข้อมูลและเก็บส่วนที่ส่งแล้วแยกจากคำตอบสรุป

ราคาเป็นอัตราจากข้อมูลที่บันทึกไว้ ภาพราคาหลายบริการมีช่วงสิ้นสุด 2026-03-31 และราคา PC มีข้อมูลปรับปรุง 2026-07-27 ต้องให้เจ้าของยืนยันการใช้ในปัจจุบัน กติกา RoV ภาษาอังกฤษยังขาดเนื้อหาหนึ่งส่วน ระบบจะแจ้งส่วนที่ขาด

รอบนี้ผ่านชุดใหม่ 23 test methods, regression เดิม 70 tests, เว็บ r38.2 30/30 เงื่อนไข และตรวจชุดสุดท้าย r38.4 อีก 8/8 เงื่อนไข ไม่ใช่การรับรองทุกคำถามหรือสถานะจองจริงใน WordPress

ความจำบทสนทนาอยู่ในกระบวนการหลัก อายุ 30 นาที เปลี่ยน worker ได้แต่การหยุด/เปิด server ใหม่ไม่เก็บความจำทั้งหมดถาวร การล้างแชทเริ่ม session ใหม่
'''
(PACKAGE/'RELEASE_NOTES_TH.md').write_text(notes,encoding='utf-8')

changed=(HERE/'changed_paths_r38_4.txt').read_text(encoding='utf-8-sig').splitlines()
added=(HERE/'added_paths_r38_4.txt').read_text(encoding='utf-8-sig').splitlines()
after={name:hashlib.sha256((SOURCE/name).read_bytes()).hexdigest() for name in sorted(set(changed+added)) if (SOURCE/name).is_file()}
(HERE/'after_manifest_r38_4.json').write_text(json.dumps(after,indent=2),encoding='utf-8')
for name in after:
    if name.endswith('.py'): ast.parse((SOURCE/name).read_text(encoding='utf-8-sig'))

archive=HERE/'PSU_Esports_Chatbot_r38_4.zip'
entries=[]
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for file in sorted(PACKAGE.rglob('*')):
        if not file.is_file(): continue
        relative=file.relative_to(PACKAGE)
        if '__pycache__' in relative.parts or file.suffix=='.pyc': continue
        if relative.parts[:2]==('data','logs') and relative.as_posix()!='data/logs/.gitkeep': continue
        z.write(file,arcname='PSU_Esports_Chatbot_Local/'+relative.as_posix())
        entries.append(relative.as_posix())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    compared=[]
    for name in after:
        if not name.startswith(('app/','web_chat/')): continue
        expected=hashlib.sha256((SOURCE/name).read_bytes()).hexdigest()
        actual=hashlib.sha256(z.read('PSU_Esports_Chatbot_Local/'+name)).hexdigest()
        assert expected==actual,name
        compared.append(name)
    assert all(n=='data/logs/.gitkeep' or not n.startswith('data/logs/') for n in entries)
    assert 'RELEASE_NOTES_TH.md' in entries
    manifest=json.loads(z.read('PSU_Esports_Chatbot_Local/package_manifest.json'))
    assert manifest['runtime_version']=='2026.10.05-conversation-r38.4'
verification=dict(archive=archive.name,bytes=archive.stat().st_size,sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),entries=len(entries),crc_pass=True,log_exclusion_pass=True,runtime_version=manifest['runtime_version'],source_hash_compared=compared,changed_source_files=len(after))
(HERE/'archive_verification_r38_4.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(verification,ensure_ascii=False,indent=2))
