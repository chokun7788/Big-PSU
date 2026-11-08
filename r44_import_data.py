import json,shutil,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r44_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
x=json.loads((OUT/'WORKBOOK_EXTRACTION.json').read_text(encoding='utf-8'));sheet=x['sheets'][0];cells={c['cell']:c['value'] for row in sheet['rows'] for c in row}
assert len(x['sheets'])==1 and cells['B1']=='หน่วยงานภายนอก' and cells['D1']=='หน่วยงานภายใน'
assert cells['B2']==cells['D2']=='ราคาต่อวัน (บาท)' and cells['C2']==cells['E2']=='ราคาต่อครึ่งวัน (บาท)'
equipment_en=['All gaming equipment','2 Cockpit units','1 VR unit','1 Nintendo Switch unit','2 PlayStation 5 units','10 PC units']
keys=['all_zones','cockpit','vr','nintendo_switch','ps5','pc'];labels=['All Zones','Cockpit Zone','VR Zone','Nintendo Switch Zone','PlayStation 5 Zone','PC Zone']
rows=[]
for i,(key,label) in enumerate(zip(keys,labels),3):
 rows.append(dict(id=key,label=label,original_label=cells[f'A{i}'],seats=int(cells[f'F{i}']),equipment_th=cells[f'G{i}'].strip(),equipment_en=equipment_en[i-3],
  prices_thb=dict(external=dict(full_day=int(cells[f'B{i}']),half_day=int(cells[f'C{i}'])),internal=dict(full_day=int(cells[f'D{i}']),half_day=int(cells[f'E{i}']))),
  source_row=i,source_cells={name:f'{col}{i}' for name,col in [('external_full_day','B'),('external_half_day','C'),('internal_full_day','D'),('internal_half_day','E'),('seats','F'),('equipment','G')]}))
data=dict(schema_version=1,source_id='zone_rental_fees_user_workbook_20261006',source_url='local://service_fee/zone_rental_fees_20261006',source_file='data/sources/zone_rental_fees_20261006.xlsx',source_original_filename=Path(x['source']).name,source_sha256=x['sha256'],source_sheet=sheet['sheet'],received_on='2026-10-06',effective_from=None,effective_until=None,
 price_scope='zone_rental_for_organizations',currency='THB',period_hours=dict(half_day=None,full_day=None),customer_groups=dict(internal='หน่วยงานภายใน',external='หน่วยงานภายนอก'),
 source_notes=[dict(text_th=cells['H3'],text_en='Staff overtime compensation is reimbursed according to university regulations.',cell='H3',scope='all_zones_row')],rows=rows)
dest=ROOT/'data/curated/zone_rental_fees_20261006.json';assert not dest.exists()
dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
src=ROOT/data['source_file'];src.parent.mkdir(parents=True,exist_ok=True);assert not src.exists();shutil.copy2(OUT/data['source_original_filename'],src)
assert hashlib.sha256(src.read_bytes()).hexdigest()==x['sha256']
with (OUT/'FLOW_R44_INITIAL.md').open('x',encoding='utf-8') as f:f.write('''# Flow r44: นำเข้าราคาเช่าเหมาจากไฟล์ผู้ใช้

1. อ่านทุก sheet/cell/formula/merged header; เก็บต้นฉบับและ SHA256; 1 sheet ไม่มีสูตร/ภาพ
2. แมป 6 โซน × 2 หน่วยงาน × 2 ระยะ = 24 อัตรา พร้อมที่นั่ง/อุปกรณ์และ cell provenance
3. แยก zone rental for organizations จากราคาเล่นต่อเครื่อง/ชั่วโมงของบุคคล; ไม่ทับ hourly fee data หรือแปลงนักศึกษาเป็นหน่วยงานภายใน
4. รักษา period ครึ่งวัน/เต็มวันตามไฟล์ ไม่กำหนด 3/4/6/8 ชั่วโมงเอง ไม่สร้างวันเริ่มใช้หรือส่วนลด/รวมค่าเจ้าหน้าที่
5. เพิ่ม source registry + structured answer ที่อ่านไฟล์ normalized; ข้อมูลใหม่มี precedence เฉพาะราคาเช่าเหมา ไม่ใช้ no-answer เหมาทั้งวันเก่าปฏิเสธราคาที่มีแล้ว
6. รองรับ TH/EN และ short follow-up ที่ส่งถึงผู้ใช้แล้ว เก็บ target/group/period ใน typed rental plan; explicit hourly/topic shift ต้องออกจาก rental
7. คำถาม booking/current availability/day definition/overtime inclusion บอกข้อที่ไฟล์ไม่มีอย่างตรงประเด็น ไม่ใช้กฎ 3 sessions ของการเล่นทั่วไปกำหนดการเช่าเหมา
8. ทดสอบ 24 cell values + capacity/equipment + broad/specific/สองรอบ + typo/paraphrase ที่เกี่ยวข้อง + negative hourly/live queries; เปรียบเทียบ output จริง
9. Freeze local candidate ใหม่ ไม่ทับรุ่นเก่า; start/readiness/HTTP source parity + dataset/source workbook hashes
10. วิเคราะห์ failures แก้เฉพาะหลักฐาน สรุปคำถามเจ้าของที่ยังขาด และเก็บ raw/failed log ทุกครั้ง

## คำถามข้อมูลที่ไม่อยู่ในไฟล์

- ครึ่งวัน/เต็มวันนับกี่ชั่วโมงและใช้ช่วงเวลาใด? การเช่าเหมาจัดช่วง Maintenance/นอกเวลาปกติได้อย่างไร?
- อัตรานี้เริ่มใช้/หมดอายุเมื่อไร?
- ค่าตอบแทนเจ้าหน้าที่นอกเวลารวมในค่าเช่าหรือคิดแยก ใครจ่ายและคิดเท่าไร?
- การเช่าเหมาจองผ่านช่องทางใด และบุคคลทั่วไป/นักศึกษาใช้ราคาใดเมื่อไม่ได้เป็นหน่วยงาน?
''')
print(dest,'24 rates',len(rows),'rows','xlsx hash',x['sha256'])
