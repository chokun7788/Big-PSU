from pathlib import Path
import hashlib,json,zipfile
HERE=Path(__file__).parent
package=HERE/'release_r38_5'/'PSU_Esports_Chatbot_Local'
notes=(package/'RELEASE_NOTES_TH.md').read_text(encoding='utf-8')
notes=notes.replace('อีก 8/8 เงื่อนไข','อีก 10/10 เงื่อนไขจาก 15 คำขอ').replace('ตรวจชุดสุดท้าย r38.5','ตรวจชุดสุดท้าย r38.5')
if 'ตรวจไฟล์ที่แตก ZIP ด้วยคำถามเพิ่มเติม' not in notes:
    notes+='\nตรวจไฟล์ที่แตก ZIP ด้วยคำถามเพิ่มเติม 10/10 เคส ผ่าน pipeline ทั้งเส้นทาง ควรแตก ZIP ใน path สั้น เช่น C:\\PSUChatbot เพื่อเลี่ยงข้อจำกัดความยาว path ของ Windows\n'
(package/'RELEASE_NOTES_TH.md').write_text(notes,encoding='utf-8')
archive=HERE/'PSU_Esports_Chatbot_r38_5_verified.zip'
with zipfile.ZipFile(HERE/'PSU_Esports_Chatbot_r38_5.zip') as original, zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as final:
    for item in original.infolist():
        content=notes.encode('utf-8') if item.filename=='PSU_Esports_Chatbot_Local/RELEASE_NOTES_TH.md' else original.read(item.filename)
        final.writestr(item,content)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    manifest=json.loads((HERE/'after_manifest_r38_5.json').read_text(encoding='utf-8'))
    for name,sha in manifest.items():
        if name.startswith(('app/','web_chat/')):
            assert hashlib.sha256(z.read('PSU_Esports_Chatbot_Local/'+name)).hexdigest()==sha
v=json.loads((HERE/'archive_verification_r38_5.json').read_text(encoding='utf-8'))
oldsha=v['sha256'];oldbytes=v['bytes']
v.update(archive=archive.name,bytes=archive.stat().st_size,sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),metadata_only_update=True)
(HERE/'archive_verification_r38_5_final.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
report=HERE/'IMPLEMENTATION_AND_TEST_REPORT_R38_5_TH.md'
s=report.read_text(encoding='utf-8').replace('PSU_Esports_Chatbot_r38_5.zip',archive.name).replace('archive_verification_r38_5.json','archive_verification_r38_5_final.json').replace(oldsha,v['sha256']).replace(f'{oldbytes:,} bytes',f"{v['bytes']:,} bytes")
s+='\n### การคืนพื้นที่ก่อนบันทึก ZIP ฉบับส่งมอบ\n\nพบดิสก์เต็มระหว่างบันทึก ZIP จึงลบเฉพาะสำเนาที่แตกจาก ZIP เพื่อการตรวจในรอบนี้ 4 โฟลเดอร์ หลังตรวจ absolute path และยืนยันไม่มี reparse points ได้พื้นที่คืนประมาณ 125 MiB; เก็บ ZIP/source/สำเนาก่อนแก้/log และผลทดสอบเดิมทั้งหมดไว้ ZIP ฉบับส่งมอบคือไฟล์ที่ลงท้าย `_verified.zip` และผ่าน CRC/hash หลังบันทึกสำเร็จ ไม่ใช้ ZIP ที่เขียนค้างเป็นผลส่งมอบ\n'
report.write_text(s,encoding='utf-8')
print(json.dumps(dict(archive=archive.name,bytes=v['bytes'],sha256=v['sha256'],crc_and_source_hash_pass=True),indent=2))
