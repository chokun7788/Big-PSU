"""Hide importer bookkeeping while preserving it unchanged on ordinary edits."""
from pathlib import Path
R=Path(__file__).resolve().parent
p=R/'system/app/knowledge/common/ui/owner.js';s=p.read_text('utf8')
marker=";let box=node('div');box.className='field';box.append(node('h3'"
insert=""";if(f.key==='scope_note'&&unit.status==='known'){try{let meta=JSON.parse(unit.value?.th||unit.value?.en||'{}');if(meta.r114_fact||meta.r114_confirmation){let description=meta.r114_fact?.subject?.th;let hint=node('p',description?'ข้อมูลนี้ใช้กับ: '+description+' — แก้คำถามและคำตอบด้านล่างได้ หากเป็นคนละเรื่องให้สร้างรายการใหม่':'คำยืนยันอัตราที่เจ้าของให้ไว้ ใช้ประกอบตารางราคา');hint.className='import-scope-note';$('fields').append(hint);continue;}}catch{}};let box=node('div');box.className='field';box.append(node('h3'"""
if "className='import-scope-note'" not in s:
    assert s.count(marker)==1;s=s.replace(marker,insert);p.write_text(s,'utf8')
print('Importer metadata remains in the saved record but is hidden from ordinary form fields.')
