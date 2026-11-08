import json,hashlib,difflib
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
before={r['id']:r for r in map(json.loads,(report/'pipeline31_A_details.jsonl').read_text(encoding='utf-8').splitlines())}
after={r['id']:r for r in map(json.loads,(report/'pipeline31_C_details.jsonl').read_text(encoding='utf-8').splitlines())}
guard=json.loads((report/'candidate_C_guard100.json').read_text(encoding='utf-8'))['records']
scopes={
 'MASTER-GT-TH-04585':('P1 ชื่อเต็มผิดสองตำแหน่ง','resolver เดิมยอมรับชื่อเต็มตรงหรือส่วนชื่อที่ตรง; เมื่อทั้งชื่อและนามสกุลผิดจึงไม่พบคน แม้ capability structured.members ได้ .872 ก็ไม่ใช่หลักฐานยืนยันบุคคล','เทียบชื่อเต็มกับ directory เดิมได้ระยะ OSA=2 และห่างอันดับสองมากพอ; ตอบเงื่อนไข “หากหมายถึง…” ด้วยชื่อ/ตำแหน่งจากต้นฉบับ ไม่แก้ชื่อใน input'),
 'MASTER-GT-TH-03100':('P1 สถานะหลักฐานหายข้ามเส้นทาง','structured path มี coverage_status note แต่ vector path ไม่ใส่หมายเหตุ; legacy contract ไม่บังคับให้มีสถานะ manual verification','ใส่ note จาก source rows ก่อน metadata ถูกลดเหลือ hit; ทุกปุ่มเดิมคงอยู่ ไม่อ้างว่าคนตรวจเครื่องจริงแล้ว'),
 'MASTER-GT-EN-00205':('P1 กลุ่มลูกค้าตกหล่น','Slumni ไม่ตรง alumni จึงไม่เลือกกลุ่มและแสดงราคาทุกกลุ่ม; route/status ผ่านไม่พิสูจน์ eligibility ถูก','syntax/resource/price frame รองรับ alumni ระยะ 1; คืนราคา 50/100 THB เฉพาะกลุ่มตามตาราง'),
 'MASTER-GT-EN-01933':('P1 คำบอกการจองตกหล่น','ook ไม่ตรง book ทำให้ game_detail ชนะ; เกมถูกชื่อแต่ operation ผิด; legacy contract ยังให้ผ่าน','recover book เฉพาะกรอบ what do you need to ... to play; ได้ขั้นตอนจองเหมือน clean; ความหมาย “ต้องจองอุปกรณ์อะไร” ยังต้องเสริม'),
 'MASTER-GT-EN-00110':('P1 คำราคาหายสองจุด','muc/xost ไม่ถูกคืนเป็น much/cost; entity price_intent=False; ตัวเลือก no_answer จึงชนะ ไม่ใช่เพราะไม่มีราคาต้นฉบับ','คืนคำราคาแต่ละ span ใน frame how ... does it ... for + resource; 1 edit/คำ; PSU student, VR, 1 hour ไม่เปลี่ยน; ตอบ 0 THB/60 นาที'),
 'MASTER-GT-EN-04950':('P1 ราคา/กลุ่ม/ระยะเวลาในคำถามหลายหัวข้อ','cot + stydent ทำให้หัวข้อราคากลับเป็นทุกกลุ่มและแสดงราคา 1 session ทั้งที่ถาม 2 hours; legacy route multi_question ผ่านจึงซ่อน defect','คืน cost จากไวยากรณ์ราคาและ student หลัง PSU; ก่อน splitter/calculator; คง 2 hours และหัวข้อ booking; ได้ 120 นาที/2 sessions/PSU 0 THB'),
 'MASTER-GT-EN-01849':('P1 คำบอกการจองตกหล่น','bok ไม่ตรง book จึงตอบรายละเอียด Uncharted แทนขั้นตอนจอง; legacy ตรวจเพียง domain กว้าง','recover operation ใน syntax frame เดียวกัน ไม่เพิ่ม alias ของทั้งคำถามหรือชื่อเกม'),
 'MASTER-GT-EN-01841':('P1 คำบอกการจองตกหล่น','ook ไม่ตรง book จึงตอบว่ามีเกมบน PS5 แทนขั้นตอนจอง; legacy ตรวจเกม/หมวดจึงให้ผ่าน','recover book แบบ bounded 1 edit; ชื่อ The Last of Us Part I ไม่เปลี่ยน'),
}
analysis=[];lines=['# วิเคราะห์สาเหตุ r29 — แยก guard, operation และความถูกต้องของเนื้อหา','','## ขอบเขตผล','',
'ชุดเดิมที่ถูก block 36 ข้อมี ordinary noisy 31 ข้อและ intentional keyboard-layout 5 ข้อ ไม่ใช่ false rejection 36 ข้อทั้งหมด. หลังแก้: guard31/31 ต่อได้ และ layout5/5ยังขอพิมพ์ใหม่. ชุด guard100/100; regression4,283ไม่มี newly blocked. 4,283 เป็นการทดสอบตัวกรอง ไม่ใช่การรันตอบครบทั้งหมด.', '',
'Pipeline62 responses (clean/noisy31คู่): legacy31/31 แต่เนื้อหา clean/noisyเหมือน29คู่. สองคู่ที่ต่างคือ conditional name suggestion และรูปแบบหัวข้อcontrolsที่ยังคงทุกปุ่ม/หมายเหตุ. จำนวนนี้ไม่รับรองว่าคำตอบ clean ครบทุกความหมายที่ผู้ใช้ตั้งใจ. ผล fixture booking แยกจาก live API จริง.', '',
'## ทำไมมีข้อมูลครบแล้วยังผิด','',
'1. Guard ทำงานก่อนค้นข้อมูล: score layout สูงจาก ngram ของ candidate ที่ลบเลข/เครื่องหมายออกจนเหลืออักษรไม่กี่ตัว หรือคำอังกฤษ typo; จึงไม่ถึงฐานข้อมูลเลย.',
'2. ผ่าน guard แล้ว operation words ยังผิด: มีข้อมูลเกม/ราคาแต่เส้นทางเลือกตอบจาก cue ที่เหลือ เช่นชื่อเกม จึงตอบข้อมูลจริงคนละเรื่อง.',
'3. เครื่องคิดราคาใช้ group/duration ที่ parser ตรวจพบ: group หายทำให้คืนทุกกลุ่ม; duration หายทำให้คืนแพ็กเกจ 1 session. การตรวจว่า route เป็น service_fee ไม่พอ.',
'4. Formatter แต่ละเส้นทางรักษา provenance ไม่เหมือนกัน: มีคำตอบปุ่มตรงจากแหล่งรองแต่หมายเหตุ manual verification หาย.',
'5. เกณฑ์ legacy อ่อน: ยอมรับ domain/status/บางคำ ทำให้ 6 จาก8คำตอบที่ต่างได้ pass แม้เนื้อหาขาด. ต้องดู operation,group,duration,complete clauses,source statusแยก.', '',
'## หลักการคะแนน','',
'คะแนน guard/capability/confidence เป็นค่าประเมินตามกฎของโค้ด ไม่ใช่เปอร์เซ็นต์ความถูกต้อง. Layout thresholdยังเป็น .39; scoreต่ำลงเมื่อ sourceอ่านได้แข็งแรงกว่า keyboard projection หรือ English typoมี 1-edit dictionary neighbor และ ≥3 known English words/สัดส่วน≥.55. การเป็น neighbor ไม่แก้ input. ชื่อบุคลากรเปรียบเทียบได้เฉพาะ full span/role frame, ≤2 edits, ratio≤.16 และ margin≥2; ตอบแบบเงื่อนไข ไม่ถือว่ารู้เจตนาผู้ใช้แน่นอน.', '',
'## รายกรณีที่ตอบต่างหลังปลด guard','']
for identifier,(category,cause,fix) in scopes.items():
    a,b=before[identifier],after[identifier]
    relevant=[t for t in a['noisy']['trace'] if t['stage'] in ('intent_cue_preflight','entities','candidate_selection','structured_tool','validation')]
    record={'id':identifier,'category':category,'cause':cause,'fix':fix,'before':a,'after':b,'decision_trace_before':relevant}
    analysis.append(record)
    lines += [f'### {identifier} — {category}','',f"คำถาม: `{a['noisy']['question']}`",'',f"สาเหตุ: {cause}",'',f"การแก้และสิ่งที่ควรตอบ: {fix}",'',f"เส้นทางเดิม: `{a['noisy']['mode']}` → ใหม่: `{b['noisy']['mode']}`",'', 'คำตอบเดิม:', '',a['noisy']['answer'],'','คำตอบใหม่:', '',b['noisy']['answer'],'']
lines += ['## ปัญหาที่พบในการทดลองแต่ไม่ใช่ defect runtime ใหม่','',
'- Unit candidate_C เคยใส่ fallback ชื่อผิดฟังก์ชัน (game resolver); testsพบและย้ายให้ถูกฟังก์ชันแล้ว. เก็บไฟล์ intermediateไว้ ไม่เคยใช้เป็นเว็บให้ผู้ใช้.',
'- หมายเหตุ control ตอนแรกใช้ reduced hits ซึ่งไม่มี coverage_status; ย้ายไป source rows ก่อน reductionแล้ว. Unit candidate_D168/168ผ่าน.',
'- HTTPครั้งแรก graderไม่รู้จัก mode input_guard_layout_retype ทั้งที่ expected5ข้อควรblock; แก้ grader ไม่แก้ expectation/runtime และเก็บ rawผลไว้.',
'- HTTP English video-policy ต่างจาก directเพราะ liveเปิดLLM/semantic. ตรวจ cleanคู่ผ่านเว็บได้ข้อความเดียวกับ noisy: เป็น safe unknown แต่เหตุผลว่าไม่มีคำแปลยังไม่ตรงช่องว่างข้อมูลนโยบาย. เก็บเป็นงานแก้คำอธิบาย ไม่อ้างว่าต้นฉบับมีนโยบายหรือเจ้าของอนุมัติ.', '',
'## ลำดับงานที่ยังพบจาก clean answers (ยังไม่รวมเป็นผลผ่านเชิงความหมาย)','',
'1. P1 คำถามราคา “1 hour or 2 hours” ตอบเพียง60นาที. ต้องคำนวณ/แสดงแต่ละทางเลือกและตรวจ contract ทุก duration; ไม่เปลี่ยนราคา/สิทธิ์ลูกค้า.',
'2. P1 คำถามปุ่มเฉพาะ: Little Nightmares II OptionsมีCircleปน และอังกฤษ D-Padคืนทุกปุ่ม. ให้ explicit button identifier ชนะคำอธิบายกว้างและตรวจก่อน render. Source controlsยังรอคนเทียบเครื่องจริง.',
'3. P1 “What do you need to book to play [game]” อาจหมายถึงอุปกรณ์/บริการที่ต้องเลือก; ปัจจุบันทั้งclean/noisyตอบขั้นตอน. ต้องเติมgame→service mappingจากข้อมูลเดิม แล้วให้ตอบบริการพร้อมขั้นตอน หรือถามแยกเมื่อกำกวม.',
'4. P2 safe unknown อังกฤษเมื่อไม่มี policy ต้องระบุ missing evidence ไม่ใช่ missing translation โดยอ้างhomepageที่ไม่รองรับกฎ. ไม่เดาว่าถ่ายรูป/วิดีโอได้หรือไม่ได้.',
'5. P2 short/mixed layout และ valid-word collisionsยังมี tradeoff. ไม่ลด thresholdจากเคสเดียวหรือแก้คำจริง/ชื่อ/เลขทั่วทั้ง input.', '',
'## ยังรอเจ้าของ/ข้อมูลจริง','',
'Tekken pause s03/s07ขัดกัน, RoV6.1.5.1ขาด, rulebook/version/scopeและ104หัวข้อ, official English names, PS5 controller counts/models, photo/video policy, public/food policy formal signoff, minimum age/registration fee ที่ไม่มีข้อมูล. Oracleการจองจริงยังพักตามผู้ใช้. การผ่าน testไม่ใช่การอนุมัติเหล่านี้. แบบฟอร์มคำถามเจ้าของอยู่ชุด outputs/owner_information_request_20261001_225453_48f6a2 เดิม.']
with (report/'DETAILED_CAUSE_ANALYSIS_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
with (report/'downstream_changed_cases_analysis.json').open('x',encoding='utf-8') as f:json.dump(analysis,f,ensure_ascii=False,indent=2)
manifest={}
for name in ['before_manifest.json','before_downstream_manifest.json','before_vector_manifest.json']:manifest.update(json.loads((report/name).read_text(encoding='utf-8')))
changed={};snapshots={}
for name,oldsha in manifest.items():
    data=(project/name).read_bytes();snapshots[name]=hashlib.sha256((report/'before'/name).read_bytes()).hexdigest()==oldsha
    if hashlib.sha256(data).hexdigest()!=oldsha:
        diff=''.join(difflib.unified_diff((report/'before'/name).read_text(encoding='utf-8').splitlines(True),data.decode('utf-8').splitlines(True),fromfile='before/'+name,tofile='after/'+name))
        changed[name]={'before_sha256':oldsha,'after_sha256':hashlib.sha256(data).hexdigest(),'text_changed':bool(diff)}
        p=report/'changes'/(name+'.diff');p.parent.mkdir(parents=True,exist_ok=True);p.open('x',encoding='utf-8').write(diff)
with (report/'change_audit.json').open('x',encoding='utf-8') as f:json.dump({'changed':changed,'snapshots_verified':snapshots},f,indent=2)
print(json.dumps({'analysis_cases':len(analysis),'changed':changed,'snapshots_verified':all(snapshots.values())},ensure_ascii=False))
