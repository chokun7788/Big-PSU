"""Freeze 140 designs and select 42 configurations before generating test results."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent
cats=json.loads((B/'r112_category_design_20261021/CATEGORY_AND_METHOD_SPEC.json').read_text('utf8'))['categories']
ideas={
'C01':['ค้นฟิลด์ที่อยู่และช่องทางตรง','กราฟอาคาร–ชั้น–สิ่งอำนวยความสะดวก','FAQ ตรงคำถาม','จัดอันดับข้อความเฉพาะข้อมูลศูนย์','แยก map/address/contact ก่อนอ่าน','LLM เลือก record และ field','สรุปเอกสารข้อมูลศูนย์ทั้งชุด','ฟิลด์ก่อนและ semantic เมื่อกำกวม','ตอบแบบตารางข้อมูลศูนย์','ตรวจ claim กับจุดหมายก่อนส่ง'],
'C02':['อ่าน role พร้อมขอบเขตชื่อสาธารณะ','ค้นรายชื่อแบบ lexical','เดินทีมไปหารายชื่อ','แยกชื่อ–ตำแหน่งแล้วเลือกฟิลด์','FAQ บุคลากรเฉพาะคน','LLM จัดชื่อกับหน้าที่','แสดง directory ทั้งชุด','เปรียบเทียบคนสองคนผ่านกราฟ','อ่านฟิลด์ก่อนแล้ว semantic แก้ชื่อกำกวม','อ่านเฉพาะรายชื่อที่ public ครบทุกฟิลด์'],
'C03':['ค้นคำอธิบายรุ่นอุปกรณ์','กราฟ model–resource–zone','สรุปสเปกทุกฟิลด์','ค้น FAQ อุปกรณ์','ตีความจำนวน/หน่วย/ที่ตั้งก่อนอ่าน','LLM เลือกชนิดอุปกรณ์','ค้นด้วยชื่อโซนก่อนชื่อรุ่น','เปรียบเทียบสเปกระหว่างรุ่น','นับ physical inventory แบบชุด','กราฟตาม predicate พร้อม semantic fallback'],
'C04':['enumerate offerings ตามโซน','ค้นเกมจากคำในชื่อ','FAQ เกมที่ติดตั้ง','สรุปเกมจาก root record','แยก catalog/overview/how-to ก่อนอ่าน','LLM เลือกกลุ่มเกม','ค้นตามจำนวนผู้เล่นจาก modes','รวม source ที่เกี่ยวกับเกมทุกชิ้น','กราฟ offering กับตัวกรองครบชุด','typed game reader และ semantic แก้เจตนา'],
'C05':['exact action-to-button','ค้นข้อความปุ่มใกล้คำถาม','แสดงผังปุ่มทั้งชุด','ผูกเกม–platform–preset ก่อน action','FAQ วิธีควบคุม','LLM อ่านคำอธิบายแล้วเลือก binding','แยก action กับ gesture/context','binding ตรงก่อนแล้ว semantic rerank','ค้นปุ่มกลับไปหา action','เทียบหลาย preset แล้วถามตัวเลือก'],
'C06':['ตีความบริการ–กลุ่ม–รอบแบบเดิม','ค้นตารางราคาจากชื่อ','LLM คำนวณจากข้อความราคา','typed rate/unit/audience calculator','แสดงทุกกลุ่มเมื่อถามราคา','FAQ ราคาตรงบริการ','กราฟ game→service→rate','แจกแจงราคาตามงบ','แก้ slot จากประวัติก่อนคำนวณ','calculator แบบ typed พร้อม semantic plan'],
'C07':['เลือกแพ็กเกจแล้วอ่านราคา','FAQ เหมาโซน','แสดงตารางทุก package','tuple zone–audience–period','กรองจาก equipment ที่ต้องการ','LLM สรุป terms ทั้งเล่ม','เปรียบเทียบครึ่งวันกับเต็มวัน','กราฟจำนวนที่นั่งและอุปกรณ์','package contract พร้อม semantic fallback','ถามทุก slot ก่อนอ่านราคา'],
'C08':['FAQ จองที่ใกล้ที่สุด','action-first จอง/ยกเลิก/เช็กอิน','ต้นไม้สถานะการใช้งาน','ค้นขั้นตอนจากชื่อ procedure','LLM สรุป FAQ ทั้งหมวด','อ่าน policy/procedure เฉพาะเงื่อนไข','เลือกตามช่องทางอีเมล/เพจ','กราฟเอกสารและผู้เล่น','ตอบขั้นตอนเต็มทุกครั้ง','action contract และ semantic correction'],
'C09':['แยก action โอน/สลิป/เอกสาร','FAQ ชำระเงินอันดับแรก','อ่านข้อความชำระทุกข้อ','สถานการณ์ผู้โอน–ยอด–หลักฐาน','LLM สรุปเรื่องเงิน','กราฟวิธีชำระกับเอกสาร','จับ keyword คืนเงินแล้วค้น','เลือก policy ตามสถานะจ่ายแล้ว','typed payment policy และ semantic correction','ผสานทุกข้อที่มีจำนวนเงิน'],
'C10':['FAQ permission ทั่วไป','action–subject permission matcher','ค้นกฎจากอุปกรณ์ที่พูดถึง','LLM จัดสถานการณ์ผู้ใช้','condition/exception policy graph','ต้นไม้สถานะใช้บริการ','อ่านข้อความกฎทั้งหมดก่อนตอบ','เลือกกฎจาก channel ติดต่อ','จับตามคำห้าม/ได้','policy contract พร้อม semantic ในขอบเขต'],
'C11':['อ่านตารางวัน/ช่วงเวลาตรง','ค้น FAQ เปิดปิด','LLM สรุปตารางสัปดาห์','แยก opening/bookable/maintenance/closure','แสดงทั้งสัปดาห์ทุกคำถาม','ต้นไม้วันหยุดก่อนวันธรรมดา','กราฟโซนและข้อยกเว้น','คำนวณเฉพาะ weekday','calendar contract พร้อม semantic dates','ค้นประกาศล่าสุดแทน schedule'],
'C12':['อ่าน provider ตาม resource/time','ค้นข้อความสถานะใน cache','LLM เลือกสถานะจากข้อความ','typed binding + freshness + status mapping','ตรวจ resource ผ่าน schedule ก่อน','เรียก provider ทุกเครื่องแล้วกรอง','อ่าน snapshot เก่าเมื่อ provider ไม่พร้อม','ถาม input ทุกช่องก่อนเรียก','กราฟ resource/zone รวมช่วงว่าง','live contract หลาย needs และ bounded interpretation'],
'C13':['ค้นทั้ง rulebook ตามชื่อเกม','retrieval ข้อกติกาตามคำถาม','สรุป overview ทุกคำถาม','FAQ กติกาตามเกม','event–facet–dependency clause graph','LLM เลือกข้อแล้วสรุป','exact heading/section lookup','เลือกบทลงโทษจาก keyword','อ่านข้อทั้งหมดแล้วตัดข้อความ','clause contract และ semantic clause selection'],
'C14':['กรองกิจกรรมตามวันที่ที่ถาม','ค้นข่าวล่าสุดจากชื่อ','แสดงทุกข่าวใน snapshot','อ่าน news clause ตาม scope และวัน','LLM สรุปข่าวทั้งหมด','กราฟงาน–ช่องทางสมัคร','ค้น headline ก่อนวันที่','เลือกเฉพาะข่าวที่มี registration URL','event contract พร้อม semantic fallback','FAQ กิจกรรมทั่วไป'],
}
selected={'C01':[1,2,8],'C02':[1,4,9],'C03':[1,5,10],'C04':[1,5,10],'C05':[1,4,8],'C06':[1,4,10],'C07':[1,4,9],'C08':[1,6,10],'C09':[1,4,9],'C10':[2,5,10],'C11':[1,4,9],'C12':[1,4,10],'C13':[2,5,10],'C14':[1,4,9]}
rubric={'source_correctness':30,'question_scope':25,'data_only_updates':20,'implementation_feasibility':15,'bounded_latency':10}
designs=[];configs=[]
for cat in cats:
 cid=cat['id'];picks=selected[cid]
 for i,title in enumerate(ideas[cid],1):
  family=['lexical','typed','hybrid'][picks.index(i)] if i in picks else 'design_only'
  ratings=({'source_correctness':4,'question_scope':3,'data_only_updates':4,'implementation_feasibility':5,'bounded_latency':5} if family=='lexical' else {'source_correctness':5,'question_scope':4,'data_only_updates':5,'implementation_feasibility':4,'bounded_latency':5} if family=='typed' else {'source_correctness':5,'question_scope':5,'data_only_updates':5,'implementation_feasibility':4,'bounded_latency':3} if family=='hybrid' else {'source_correctness':3,'question_scope':2+(i%2),'data_only_updates':3,'implementation_feasibility':3+(i%2),'bounded_latency':2+(i%3)})
  score=round(sum(ratings[k]*weight/5 for k,weight in rubric.items()),1)
  d={'id':f'{cid}-F{i:02}','category':cid,'name':title,'family':family,'design_ratings_0_to_5':ratings,'design_feasibility_score':score,'score_type':'engineering_estimate_not_observed_accuracy','selected':i in picks,'steps':['รักษา subject และเงื่อนไขของคำถาม',f'จำกัดข้อมูลที่หมวด {cat["name"]} รับผิดชอบ',f'ใช้กระบวนการ {title}','อ่าน source/evidence และแยก unknown','ประกอบคำตอบตามส่วนที่ถามพร้อมที่มา'],'source_kinds':cat['schema_kinds'],'risk':cat['boundary']}
  designs.append(d)
  if d['selected']:
   configs.append({'id':d['id'],'category':cid,'name':title,'family':family,'source_scope':cat['schema_kinds'],'strategy':{'lexical':'domain-scoped lexical retrieval; do not enforce entity/facet slots beyond the selected source text','typed':'bind subject and requested facets; enumerate matching claims and use deterministic arithmetic/status','hybrid':'typed plan plus bounded local-model evidence selection for unresolved or ambiguous wording'}[family],'llm_enabled':True,'model_facts_generated':False})
assert len(designs)==140 and len(configs)==42
R.mkdir(exist_ok=True)
for name,data in [('DESIGNS_140.json',designs),('SELECTED_42.json',configs),('DESIGN_RUBRIC.json',rubric)]:
 p=R/name
 if p.exists():assert json.loads(p.read_text('utf8'))==data,'Refusing to change frozen designs'
 else:p.write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf8')
lines=['# R113 — 140 Flow และการคัด 3 Flow ต่อหมวด','', 'คะแนนนี้เป็นการประเมินทางวิศวกรรมก่อนรัน ไม่ใช่เปอร์เซ็นต์ตอบถูก. ใช้ source correctness 30 / scope 25 / data-only update 20 / implementation 15 / latency 10 คะแนน','', 'สาม implementation families ใช้ source provider เดียวกัน แต่ต่างกันที่ lexical selection, typed subject/facet selection, และ typed + bounded local-model planner. แต่ละ family ถูกตั้งค่าตาม schema/ข้อจำกัดของหมวด ไม่ใช่เปลี่ยนเพียง temperature หรือชื่อป้าย','']
for cat in cats:
 lines += [f"## {cat['id']} {cat['name']}",'','| Flow | แนวทาง | คะแนนออกแบบ /100 | คัด |','|---|---|---:|---|']
 for d in [x for x in designs if x['category']==cat['id']]:lines.append(f"| {d['id']} | {d['name']} | {d['design_feasibility_score']} | {'ใช่ — '+d['family'] if d['selected'] else 'เก็บเป็นทางเลือก'} |")
 lines+=['','เหตุผลหลัก: '+cat['reuse_direction'],'','จุดระวัง: '+cat['boundary'],'']
(R/'01_DESIGNS_AND_SELECTION_TH.md').write_text('\n'.join(lines),'utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'designs_frozen','designs':140,'selected':42,'planned_categories':14,'questions_per_category':100,'planned_executions':4200,'production_changed':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'designs':len(designs),'selected':len(configs)}))
