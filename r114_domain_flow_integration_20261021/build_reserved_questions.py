"""Freeze fresh source-grounded questions before candidate score inspection.

These paraphrases use the same source snapshot, not independent new facts or a
human-adjudicated customer holdout. End-to-end lifecycle cases are separate.
"""
import hashlib,json,random
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r113_multi_flow_benchmark_20261021'
data=json.loads((B/'COMMON_READ_MODEL.json').read_text('utf8'));rng=random.Random(114)
old={json.loads(x)['question'] for x in (B/'EFFECTIVE_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()}
wording={
 'address':'จะเดินทางไป {s} ขอที่อยู่ที่มีหลักฐานยืนยันหน่อย',
 'building':'ถ้าจะไป {s} ต้องไปที่อาคารอะไร', 'floor':'{s} อยู่ชั้นใดของอาคาร',
 'role':'ช่วยอธิบายว่า {s} รับผิดชอบหน้าที่อะไร', 'display_name':'บุคคลในรายการ {s} มีชื่อว่าอะไร','team':'{s} สังกัดทีมใด',
 'specifications':'อยากทราบสเปกที่บันทึกไว้ของ {s}', 'location':'{s} อยู่ในโซนไหน',
 'quantity':'ขอจำนวนเครื่องจริงของ {s}', 'controllers':'ถ้าใช้ {s} หนึ่งเครื่อง มีจอยให้กี่อัน',
 'summary':'ช่วยเล่าให้เข้าใจว่าเกม {s} เกี่ยวกับอะไร','genre':'{s} จัดเป็นเกมแนวไหน','how_to_play':'เริ่มเล่น {s} ต้องทำอะไรบ้างตามวิธีเล่น',
 'supported_platforms':'{s} มีแพลตฟอร์มที่รองรับอะไรบ้าง','game_catalog':'ขอรายชื่อเกมทั้งหมดที่ใช้บริการ {s} แล้วเล่นได้','studio_services':'ถ้าอยากเล่น {s} มีบริการไหนในศูนย์รองรับ',
 'amount':'สำหรับ {s} เล่น 3 รอบ ขอราคาที่คิดต่อคน', 'amount_thb':'อยากจองเหมา {s} ขอราคาแพ็กเกจนี้',
 'duration_minutes':'{s} มีระยะเวลาใช้งานกี่นาที','equipment_included':'ถ้าจองเหมา {s} จะมีอุปกรณ์อะไรรวมให้',
 'room_seats':'{s} ระบุจำนวนที่นั่งห้องไว้เท่าไร','bookable_periods':'วัน{s} สามารถจองเล่นช่วงเวลาใดได้บ้าง',
 'maintenance_periods':'ขอดูช่วงบำรุงรักษาในวัน{s}', 'description':'อยากอ่านรายละเอียดกิจกรรม {s}',
 'date':'งาน {s} ระบุวันที่จัดไว้เมื่อไร','registration':'ขอช่องทางสมัครหรือลิงก์ลงทะเบียนของ {s}','status':'ตอนนี้งาน {s} มีสถานะรับสมัครอย่างไร',
 'live_status':'ช่วยตรวจสถานะว่างของ {s} จากข้อมูลตามช่วงเวลาที่ระบุ',
}
gaps={
 'C01':'ศูนย์มีแฟกซ์หมายเลขใดที่ยืนยันได้', 'C02':'ขอทราบเงินเดือนส่วนตัวของผู้จัดการ',
 'C03':'อยากทราบ serial number ที่ไม่ได้บันทึกของเครื่อง', 'C04':'แพตช์ที่ติดตั้งของเกมนี้เลขอะไรแน่นอน',
 'C05':'ปุ่มเปิดระบบ Auto Win ที่ไม่ได้มีในคู่มือคือปุ่มใด', 'C06':'อัตราค่าบริการสำหรับปี 2091 ยืนยันแล้วกี่บาท',
 'C07':'ค่าโอทีตายตัวของการเช่าเหมาเป็นกี่บาทต่อนาที', 'C08':'รับประกันเครื่องสำรองส่วนตัวสำหรับทุกการจองหรือไม่',
 'C09':'เครดิตจากเงินโอนเกินหมดอายุแน่นอนกี่วัน', 'C10':'กำหนดอายุขั้นต่ำแบบตัวเลขแน่นอนไว้กี่ปี',
 'C11':'ปี 2091 วันปิดพิเศษที่ยืนยันแล้วมีวันใดบ้าง', 'C12':'PC99 / 2026-10-21 09:00 ว่างหรือไม่',
 'C13':'การแข่งขัน CS2 ปี 2091 ใช้แผนที่อะไรที่ยืนยันแล้ว', 'C14':'โปรโมชันลับปี 2091 ลดราคาแน่นอนกี่เปอร์เซ็นต์',
}
out=[]
for cat in [f'C{i:02}' for i in range(1,15)]:
    facts=[f for f in data['facts'] if f['category']==cat and (f['facet'] in wording or cat in {'C05','C13'} or f['facet']=='owner_policy')]
    rng.shuffle(facts);selected=facts[:6]
    for i,f in enumerate(selected):
        s=f['subject']['th'];facet=f['facet']
        if facet.startswith('binding_'):q=f"ในเกม {s} ถ้าจะ{f['label']['th']} ต้องใช้ปุ่มใด"
        elif facet=='rule_clause':q=f"กติกาของ {s} หัวข้อ {f['label']['th']} ระบุเงื่อนไขไว้อย่างไร"
        elif facet=='owner_policy':q=f"ขอทราบเงื่อนไขหรือวิธีปฏิบัติเรื่อง {s} ที่เจ้าของยืนยันไว้"
        else:q=wording[facet].format(s=s)
        numeric=f.get('numeric');sessions=3 if facet=='amount' else 1
        expected={'fact_id':f['id'],'value':f['value']['th'],'numeric':numeric*sessions if numeric is not None else None,'evidence_refs':f['evidence_refs']}
        state='unavailable' if f.get('provider_state') in {'unavailable','stale'} else 'answer'
        out.append({'id':cat+'-NEW-'+str(i+1).zfill(3),'category':cat,'question':q,'locale':'th','reference_time':'2026-10-21T12:00:00+07:00',
          'fixture':f.get('fixture',False),'stratum':'single_need','expected':{'claims':[expected],'status':state,'sessions':sessions},'origin':'fresh source-grounded wording; same facts, not human semantic holdout'})
    for i,prefix in enumerate(['ขอถามเพิ่มว่า ','ช่วยตรวจจากหลักฐานว่า ','ยังไม่มีคำตอบเรื่องนี้: ','ขอตอบตรงประเด็นนี้: ']):
        out.append({'id':cat+'-NEW-'+str(i+7).zfill(3),'category':cat,'question':prefix+gaps[cat],'locale':'th','reference_time':'2026-10-21T12:00:00+07:00',
          'fixture':cat in {'C12','C14'},'stratum':'missing_source','expected':{'claims':[],'status':'not_current' if cat=='C06' else 'missing_source','sessions':1},'origin':'fresh unsupported-scope question with source-backed abstention expectation'})
assert len(out)==140 and len({j['question'] for j in out})==140 and not old.intersection(j['question'] for j in out)
target=R/'RESERVED_QUESTIONS_140.jsonl'
if target.exists():raise SystemExit('Reserved cases already frozen')
target.write_text('\n'.join(json.dumps(j,ensure_ascii=False) for j in out)+'\n','utf8')
(R/'RESERVED_MANIFEST.json').write_text(json.dumps({'questions':140,'per_category':10,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'source_sha256':hashlib.sha256((B/'COMMON_READ_MODEL.json').read_bytes()).hexdigest(),'frozen_before_candidate_score_inspection':True,
 'limits':'Same source facts; independently expected source claims, fresh wording. Not human-adjudicated generalization accuracy.'},indent=2),'utf8')
print('Frozen 140 fresh questions, ten per category.')
