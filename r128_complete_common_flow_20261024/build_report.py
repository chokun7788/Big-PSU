"""Build delivery evidence from completed raw runs; never manufacture accuracy."""
import collections,hashlib,json,math,statistics,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;root=R.parent;S=R/'system'
def read(p):return json.loads(Path(p).read_text('utf8'))
def lines(p):return [json.loads(l) for l in Path(p).read_text('utf8').splitlines() if l.strip()]
run=read(R/'FINAL_RUN.json');assert run['completed'] and run['source_unchanged']
api=Path(run['api']['output']);broad=Path(read(R/'BROAD_PROCESS.json')['output']);assert read(broad/'COMPLETE.json')['source_unchanged']
a=lines(api/'ACCEPTANCE.jsonl');x=lines(api/'CONTEXT_ACCEPTANCE.jsonl');b=lines(broad/'RESULTS.jsonl');assert len(a)==53 and len(x)==9 and len(b)==61
assert all('response' in r and 'error' not in r for r in a+x+b)
assert read(api/'CONTEXT_COMPLETE.json')['all_passed']
def latest(pattern,file,summary=False):
 p=max(R.glob(pattern),key=lambda p:p.stat().st_mtime);d=read(p/file);return {'path':str(p/file),'result':d['summary'] if summary else d}
gates={'foundation':latest('verification_*','VERIFICATION.json'),'live':latest('live_verification_*','VERIFICATION.json'),'source':latest('source_guard_verification_*','VERIFICATION.json'),'extended':latest('extended_*','RESULTS.json',True),'model':{'path':str(R/'MODEL_VERIFICATION.json'),'result':read(R/'MODEL_VERIFICATION.json')},'owner':{'path':str(R/'OWNER_VERIFICATION.json'),'result':read(R/'OWNER_VERIFICATION.json')}}
for k,v in gates.items():assert v['result']['all_passed'],k
def stats(rows):
 ts=sorted(r['wall_sec'] for r in rows)
 return {'requests':len(rows),'median_sec':statistics.median(ts),'p95_nearest_rank_sec':ts[math.ceil(.95*len(ts))-1],'max_sec':max(ts),'http_errors':sum('error' in r for r in rows)}
def ans(kind,turn=1):return next(r['response']['answer'] for r in a if r['key']==kind and r['turn']==turn)
named={
 'date_explicit_26_october_open':'26 ตุลาคม 2569' in ans('date_explicit') and '13:00' in ans('date_explicit'),
 'english_month_resolved':'26 October 2026' in ans('date_english'),
 'word_relative_day_resolved':'27 ตุลาคม' in ans('date_relative'),
 'game_zone_followup':'PlayStation 5 Zone' in ans('game_reference',2),
 'game_button_followup':'R2' in ans('game_reference',3) and 'โจมตีหนัก' in ans('game_reference',3),
 'booking_cancel_followup':'1 ชั่วโมง' in ans('booking_reference',2),
 'price_followup_140':'140 บาท' in ans('price_reference',2),
 'service_change_preserves_price_slots':'300 บาท' in ans('price_reference',3),
 'day_month_clarification':'เดือนไหน' in ans('date_clarification',1) and '15 พฤศจิกายน' in ans('date_clarification',2),
 'both_platform_catalogues':'**PC —' in ans('multi_target',1) and '**PlayStation 5 —' in ans('multi_target',1),
 'ordinal_uses_display_order':'**PlayStation 5 /' in ans('multi_target',2),
 'controls_render_as_table':'| ปุ่ม |' in ans('game_controls',2),
 'spectator_policy_found':'นั่งดูเพื่อนเล่นได้' in ans('policy_paraphrase'),
 'unknown_game_not_invented':'No confirmed source' in ans('unknown_game'),
 'mixed_audience_total_280':'280' in ans('price_multi_audience'),
 'source_mode_gap_explicit':'ข้อมูลจำนวนผู้เล่น' in ans('catalog_filter'),
 'all_five_penalty_types':all(w in ans('rules') for w in ['Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit']),
}
for k,v in named.items():assert v,k
protected={}
for label,path in [('r125',root/'r125_date_context_presentation_20261023/FINAL_SOURCE_FREEZE.json'),('legacy_original',root/'r124_legacy_guided_parity_20261023/TEACHER_FREEZE.json'),('prior_parent',R/'PARENT_FREEZE.json')]:
 frozen=read(path);bad=[p for p,h in frozen.items() if not Path(p).is_file() or hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h]
 protected[label]={'files':len(frozen),'unchanged':not bad,'mismatches':bad};assert not bad,label
db=S/'data/knowledge/common.sqlite';parent_db=root/'r125_date_context_presentation_20261023/system/data/knowledge/common.sqlite'
same_db=hashlib.sha256(db.read_bytes()).hexdigest()==hashlib.sha256(parent_db.read_bytes()).hexdigest();assert same_db
with sqlite3.connect(db) as c:
 withdrawn=c.execute('SELECT COUNT(*) FROM cc_heads WHERE withdrawn=1').fetchone()[0]
 active=c.execute('SELECT COUNT(*) FROM cc_heads WHERE withdrawn=0').fetchone()[0]
 epochs=dict(c.execute('SELECT key,value FROM cc_meta'))
changed=[]
parent=root/'r125_date_context_presentation_20261023/system'
for folder in ['app','web_chat']:
 for p in (S/folder).rglob('*'):
  if p.is_file() and p.suffix in {'.py','.js','.html','.css','.json'} and '__pycache__' not in p.parts:
   rel=p.relative_to(S);old=parent/rel
   if not old.is_file() or p.read_bytes()!=old.read_bytes():changed.append(str(rel).replace('\\','/'))
timings=lines(api/'TIMINGS.jsonl');model=[h for t in timings for h in t.get('http',[]) if h['kind']=='model'];provider=[h for t in timings for h in t.get('http',[]) if h['kind']=='provider_http']
baseline=read(root/'r127_legacy_current_flow_comparison_20261023/SUMMARY.json')
evidence={'implementation_scope':'R127 fourteen defect families plus C01-C14 contracts and shared context','implementation_scope_complete':True,'full_test':False,'overall_semantic_accuracy':None,'final_run':run,'requests':{'acceptance':stats(a),'single':stats([r for r in a if r['kind']=='single']),'conversation':stats([r for r in a if r['kind']=='conversation']),'extended_context':stats(x),'retained_61':stats(b),'total_http_requests':len(a+x+b),'unique_question_strings':len({r['question'] for r in a+x+b})},'named_acceptance_checks':named,'context_checks':read(api/'CONTEXT_COMPLETE.json'),'gates':gates,'protected_sources':protected,'database':{'sha256':hashlib.sha256(db.read_bytes()).hexdigest(),'same_as_r125':same_db,'active_records':active,'withdrawn_records':withdrawn,'epoch':epochs['epoch'],'approval_changes':0},'changed_source_files':changed,'model_http':{'attempts':len(model),'transport_failures':sum(not h.get('transport_ok') for h in model),'events':model},'provider_http':{'attempts':len(provider),'transport_failures':sum(not h.get('transport_ok') for h in provider)},'baseline_retained':{'R125_single':baseline['current_retained_single'],'legacy_single':baseline['legacy_single']},'production_R78_replaced':False}
(R/'EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),'utf8')
md=['# R128 — คำถามและคำตอบเต็มจากรอบส่งมอบ','','อ่านควบคู่ DELIVERY_REPORT_TH.md; HTTP ผ่านไม่ได้แปลว่าทุกข้อเป็นคำตอบสมบูรณ์ บางข้อจงใจตอบ partial/source gap ตามหลักฐาน','']
for heading,rows,path in [('34 คำถามเดิมและ 8 บทสนทนา / 19 turns',a,api/'ACCEPTANCE.jsonl'),('บริบทเพิ่มเติม 4 บทสนทนา / 9 turns',x,api/'CONTEXT_ACCEPTANCE.jsonl'),('คำถาม retained เดิม 61 รายการ',b,broad/'RESULTS.jsonl')]:
 md+=['## '+heading,'','Raw log: ['+path.name+'](<'+str(path).replace('\\','/')+'>)','']
 for n,r in enumerate(rows,1):
  md+=['### '+str(n)+'. '+str(r.get('kind',r.get('key',''))) + ' / turn '+str(r.get('turn',1)),'','คำถาม: '+r['question'],'',r.get('response',{}).get('answer',str(r.get('error',''))),'',f"เวลา {r['wall_sec']:.3f} วินาที",'']
(R/'ALL_RESPONSES_TH.md').write_text('\n'.join(md),'utf8')
single=evidence['requests']['single'];conv=evidence['requests']['conversation'];med=single['median_sec'];old=baseline['current_retained_single']['median_sec']
report=f'''# R128 — ผลพัฒนาและตรวจรับ

## สถานะส่งมอบ

ทำ implementation ครบ 14 กลุ่มสาเหตุที่ตรวจใน R127 และตรวจข้อต่อ C01–C14 แล้ว แชท candidate ใช้ source กลางของตัวเองและ live provider จริง หน้า owner เพิ่ม/แก้ข้อมูลผูก SQLite เดียวกัน การเพิ่ม/แก้/ถอนข้อมูลทดสอบตรวจในฐานแยก

คำว่า “ครบ” เป็นขอบเขตรายการพัฒนานี้ ไม่ใช่ความถูกต้องภาษาธรรมชาติ 100% หรือ Full Test 20,554 requests รอบใหม่ ผลรวมนี้ไม่มีคะแนน accuracy ทั้งระบบ

## ผลรอบโค้ดเดียวกัน

| ชุด | จำนวน HTTP requests | มัธยฐาน | HTTP errors |
|---|---:|---:|---:|
| คำถามเดิม R126/R127 | 34 | {med:.3f} วินาที | {single['http_errors']} |
| บทสนทนาเดิม 8 ชุด | 19 turns | {conv['median_sec']:.3f} วินาที | {conv['http_errors']} |
| บทสนทนาเพิ่มเรื่องจำนวนคน/เหมา/live/เปลี่ยนเรื่อง | 9 turns | {evidence['requests']['extended_context']['median_sec']:.3f} วินาที | {evidence['requests']['extended_context']['http_errors']} |
| คำถาม retained อีกชุด | 61 | {evidence['requests']['retained_61']['median_sec']:.3f} วินาที | {evidence['requests']['retained_61']['http_errors']} |

รวม {len(a+x+b)} HTTP requests; มีคำถามข้อความซ้ำระหว่างชุด ไม่เรียกทั้งหมดว่า unique questions ชุดนี้เลือกเพื่อตรวจปัญหา ไม่ใช่ตัวอย่างสุ่มของ Full Test

คำถามเดี่ยวชุดเดียวกัน R125 ที่เก็บไว้มีมัธยฐาน {old:.3f} วินาที ส่วน R128 {med:.3f} วินาที ลดประมาณ {(1-med/old)*100:.1f}% ในตัวอย่างนี้ Legacy ที่เก็บไว้ {baseline['legacy_single']['median_sec']:.3f} วินาที เปรียบเทียบระบบทั้งชุดและคนละเวลา ไม่ใช่ causal effect ของ Flow ล้วน ๆ: backend protocol, cache/warmup และ profile แตกต่างกัน และ live ปัจจุบันไม่ใช่ ground truth ของวันเก่า

R128 single p95 = {single['p95_nearest_rank_sec']:.3f} วินาที; max = {single['max_sec']:.3f} วินาที รวม cold first request จึงไม่อ้างว่าทุกคำถามตอบต่ำกว่า 1 วินาที

รอบนี้เปิดสิทธิ์ใช้ LLM แต่ไม่บังคับเรียกทุกข้อ TIMINGS ของ API ตรวจพบ model HTTP attempts {len(model)} ครั้ง และ model transport failures {sum(not h.get('transport_ok') for h in model)} ครั้ง การที่โจทย์ในชุดนี้อ่านแบบ native ได้มากไม่ได้พิสูจน์ว่าโมเดลเข้าใจสำนวนใหม่ทั้งหมด คุณภาพโมเดลกับการเชื่อมต่อโมเดลเป็นคนละเรื่อง; actual model identity/input/token tests แยกไว้ใน MODEL_VERIFICATION.json

## สิ่งที่แก้ครบตาม R127

| ลำดับ | ปัญหา | สิ่งที่ใช้จริง | หลักฐานตรวจรับ |
|---|---|---|---|
| 1 | history เกมไม่ถึง reader | resolver ก่อนทุกเส้นทาง | เกม → โซน → R2 ผ่าน HTTP session จริง |
| 2 | active slots หลุด | ผูกบริการ กลุ่ม เวลา จำนวนคน ช่วงเหมา และ live window | 70 → 140 → PS5 300; กลุ่มรวม 280 → 420 → PS5 900 |
| 3 | เกมคืออะไรเข้าอุปกรณ์ | game entity definition precedence | Beat Saber/Tekken เป็นคำอธิบายเกม |
| 4 | PC ถูกชื่อ PS5 ที่ยาวกว่าตัด | ตัด longest alias เฉพาะช่วงทับกัน | รายการ PC + PS5 อยู่ครบ |
| 5 | ตรวจ subset แล้วอ้างครบ | explicit-target/action obligations | fault injection ลบ PC แต่เหลือ PS5 refs ถูกต้องต้องตรวจไม่ผ่าน |
| 6 | FAQ เปลี่ยนสำนวนไม่เจอ | canonical source policy frames | นั่งดูเพื่อน/นำขวดน้ำ/เมาส์ส่วนตัว |
| 7 | intent ถูกแต่ reader เดาใหม่ผิด | canonical_operation ถึง policy reader | ขั้นตอนเริ่มเข้าเล่น/จอง/ยกเลิก |
| 8 | heavy attack เลือก L2 | source action ก่อน bounded selector | ตีแรง → R2 และ full controls table |
| 9 | กลุ่ม/alias/จำนวนคนคิดผิด | non-overlap alias + per-audience counts + ตรวจหน่วย/อัตราเทียบเท่า | mixed billing และ short Thai alias negative checks |
| 10 | บทลงโทษตอบไม่ครบ | source clause family + scoped dependencies | VALORANT ทั้ง 5 ประเภท; CS2 settings clause เต็ม |
| 11 | เดือนอังกฤษ/เลขคำ/วันหน้า | deterministic date resolver + pending month + แยก clock range | October 26 / อีกสามวัน / วันจันทร์หน้า / วันพร้อม time range |
| 12 | ขั้นตอนซ้ำ | canonical equivalent procedure โดยรักษา source IDs | ขั้นตอนจองหนึ่งชุด 6 ข้อ; ต่างเงื่อนไขยังเป็น partial |
| 13 | คำตอบอ่านยาก/แหล่ง draft หาย | renderer ตามหมวดและ source descriptors | รายการเกม ตารางปุ่ม ราคาแยกกลุ่ม ขั้นตอนเลขลำดับ |
| 14 | โมเดลผิด input/budget และช้า | resolved input hash, bounded tokens/timeout, interpretation cache | actual model identity/token/input/cache checks และ TIMINGS.jsonl |

## ตรวจ interface และ source behavior

'''
for name,v in gates.items():
 checks=v['result'].get('checks',{})
 report+=f"- {name}: all_passed=true, {len(checks)} checks — [{Path(v['path']).name}](<{v['path'].replace(chr(92),'/')}>)\n"
report+=f'''
Foundation รวม replay annotations เดิม 289 รายการ, planner output เดิม 30 และ API proposal 10 โดยไม่เรียกโมเดลใหม่ Live fixtures 15 กรณีตรวจข้อมูลสด/เก่า/อนาคต/wrong-date/provider ล้ม/status mapping หาย/unknown resource และช่วงต่อเนื่อง Fixtures ไม่ใช่สถานะจองจริง

ตรวจ model base revision และ adapter SHA เดิม, num_predict=1 ถูกเคารพ, effective input hash ตรง, และ repeated interpretation ไม่ generate เพิ่ม ไม่มีการฝึกน้ำหนักใหม่ครั้งนี้

ตรวจ owner API แบบ authenticated read-only: registry 24 kinds, list heads 848 รายการ, ฐานตรงกับแชท และ hash DB ก่อน–หลังไม่เปลี่ยน ฐานที่แชทอ่านมี {active} active records และ {withdrawn} withdrawn records ไม่ใช่ข้อมูลหายจากการคัดลอก

## ข้อมูลและขอบเขตที่ยังต้องระวัง

1. ฐานจริงยังไม่มี game_mode records ที่ยืนยันจำนวนผู้เล่นแยกเกม/โหมด จึงตอบรายชื่อเกมเล่นพร้อมกัน 4 คนจากความจุบริการไม่ได้ ตัวอ่านรองรับแล้วและพิสูจน์ด้วย record ที่ save ในฐานทดสอบ แต่ไม่ใส่ข้อเท็จจริงเกมที่เดาเองลงฐานจริง
2. บาง control_set เป็นแหล่งรองหรือ partial official ยังไม่ตรวจ preset/เวอร์ชันเครื่องศูนย์ครบ จึงไม่ลบคำเตือนเพื่อให้ดูเหมือนสมบูรณ์
3. ชื่อเกมคนละ edition เช่น The Last of Us Part II กับ Part II Remastered ไม่ถือว่าเป็น record เดียวกันโดยอัตโนมัติ ความสัมพันธ์บริการที่ยังไม่มีต้องยืนยันก่อน
4. นโยบายบาง intent มีข้อความหลายฉบับ เช่นเอกสารเช็กอิน ไม่มี superseding authority ที่ครบ จึงแสดง partial พร้อมแหล่งแต่ละฉบับ บางคู่เป็นข้อความใกล้เคียงกันมาก การแสดง conflict จึงยังค่อนข้างอนุรักษ์นิยม
5. ราคาอ้างการยืนยันของเจ้าของ ณ 20 ต.ค. 2569 แต่ไม่สร้าง effective interval ใหม่เอง และไม่รับรองปีอนาคตที่ไม่อยู่ในหลักฐาน
6. ตารางช่วงเล่นที่ยืนยันใช้แทน open_periods ที่ขัดแย้ง แต่ไม่เท่ากับเวลาเข้าอาคาร และไม่พิสูจน์เครื่องว่างจริง
7. C14 อ่านประกาศ/FAQ ที่มีได้ แต่ไม่ได้เพิ่ม feed ข่าวล่าสุดทั้งหมดมาเอง
8. นโยบาย capture ในเกมไม่อนุญาตให้สรุปสิทธิ์ถ่ายสถานที่/บุคคล รุ่นนี้คืน source scope พร้อม partial แทนคำตอบสิทธิ์แบบเหมารวม
9. ยังมี compatibility typed adapters และ bounded model interpretation ไม่ได้เปลี่ยนทุกอย่างเป็น IR architecture ใหม่ทั้งหมด ตัว artifact จึงยังคง flag full_r123_architecture_implemented=false ตามความจริง
10. สำนวนใหม่/เจตนาที่นอกชุดตรวจยังพลาดได้ การเพิ่ม content ไม่ทำให้ operation ธุรกิจชนิดใหม่ถูกสร้างขึ้นเองทุกแบบ

ทั้งหมดข้างต้นแยกจาก bug ที่แก้แล้ว ไม่ใช้ความขาด source เป็นข้ออ้างให้ reader ตอบผิด และไม่ใช้ citation ผ่านเป็นคะแนนความเข้าใจ

## การคงหลักฐานเดิม

- R125 source freeze: {protected['r125']['files']} files unchanged
- Legacy original: {protected['legacy_original']['files']} files unchanged
- Prior protected parent: {protected['prior_parent']['files']} files unchanged
- candidate common.sqlite ตรง byte/hash กับ R125, approval changes = 0
- รอบตรวจรับสุดท้าย application/UI {run['source_files']} files unchanged ขณะทดสอบ
- candidate ยังไม่ติดตั้งทับ R78; เปลี่ยนเฉพาะ local preview เมื่อเปิดใช้ R128

## ไฟล์ส่งมอบ

- [Flow ทั้งระบบและวิธีเพิ่มข้อมูล](<{str(R/'FULL_FLOW_TH.md').replace(chr(92),'/')}>)
- [คำตอบจริงเต็มทุก turn](<{str(R/'ALL_RESPONSES_TH.md').replace(chr(92),'/')}>)
- [ผลตรวจแบบ machine-readable](<{str(R/'EVIDENCE.json').replace(chr(92),'/')}>)
- [เริ่มแชท R128](<{str(R/'Start-R128.cmd').replace(chr(92),'/')}>)
- [เปิดหน้าเพิ่ม/แก้ข้อมูล](<{str(R/'Open-Owner-Content.cmd').replace(chr(92),'/')}>)

เปิดแชทที่ http://127.0.0.1:12422/ หลัง activation สำเร็จใน ACTIVATION.json หากหน้าเดิมยังค้างให้ refresh ใหม่ ชุดนี้เป็น draft preview สำหรับตรวจและพัฒนาต่อ การส่งมอบ published production ยังต้องผ่าน review/publish ของเนื้อหาจริงตามระบบเดิม
'''
(R/'DELIVERY_REPORT_TH.md').write_text(report,'utf8')
print(json.dumps({'requests':evidence['requests'],'named_checks':len(named),'gates':{k:v['result']['all_passed'] for k,v in gates.items()},'changed_files':len(changed),'protected':protected,'reports_written':True},ensure_ascii=False,indent=2))
