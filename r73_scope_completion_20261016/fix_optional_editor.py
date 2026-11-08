from pathlib import Path
p=Path(__file__).resolve().parent/'system/app/knowledge/common/ui/owner.js'
text=p.read_text('utf8')
old="let unit=r.fields[f.key]||{status:'unknown',value:null,evidence_refs:[],note:''};"
new="let unit=r.fields[f.key]||{status:'unknown',value:null,evidence_refs:[],note:'ยังไม่กำหนดข้อมูลสำหรับช่องทางเลือกนี้'};"
assert text.count(old)==1
p.write_text(text.replace(old,new),encoding='utf8')
print('Old records retain a valid unknown envelope for new optional fields in owner editor.')
