"""Produce a design coverage index. This does not import/run the chatbot."""
import hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parent;W=R.parent
spec_path=W/'r97_flow_reassessment_20261019/FLOW_SPEC.json'
catalog_path=W/'r101_complete_flow_20261019/system/app/knowledge/common/catalog.json'
flow_path=W/'r101_complete_flow_20261019/IMPLEMENTED_FLOW_TH.md'
spec=json.loads(spec_path.read_text('utf8'));catalog=json.loads(catalog_path.read_text('utf8'))
task_lines=[s for s in flow_path.read_text('utf8').splitlines() if s.startswith('| `')]
routes={
 'C01':('S05/S07/S08/S13','ทั้ง service set และ audience; สมาชิกไม่มีราคาต้องไม่หาย'),
 'C02':('S03/S05/S08','PC เติม service พร้อมราคา/audience เดิม'),
 'C03':('S03/S07','ทั้งหมดใช้ displayed scope เดิมและอ่าน release ใหม่'),
 'C04':('S04/S06/S10','wrapper ไม่ปิด policy ที่ source รองรับ; actor/action ตรง'),
 'C05':('S05/S08/S13','เวลาเย็น/วันต่างกันคง closing periods ไม่ตอบ now แทน'),
 'C06':('S07/S08/S10','reverse game_mode FK และ required claims เฉพาะจำนวนผู้เล่น'),
 'C07':('S05/S12','ถาม context เมื่อทั่วไปกับแข่งขันให้ผลต่างจริง'),
 'C08':('S03/S05/S08','เลือก ROV แล้วรักษา disconnect topic และ event qualifiers'),
 'C09':('S06/S09/S10','CS2 ห้ามถูกแทนด้วย VALORANT แม้ retrieval สูงกว่า'),
 'C10':('S07/S08/S14','complete offering set ใหญ่กว่า top-K และมี scope receipt'),
 'C11':('S05/S07/S13','multi-platform scope และ dedup ตามเกมหรือ offering ที่ถาม'),
 'C12':('S11/S12/S15','ราคาไม่พร้อมยังตอบ booking independent need'),
 'C13':('S10/S11','งบ derive ไม่ได้หากราคา/สูตรไม่พร้อม'),
 'C14':('S05/S06/S11','PC2h/VR30m/audience ไม่คูณไขว้'),
 'C15':('S05/S08/S11','rental package ไม่ derive จาก hourly'),
 'C16':('S08/S10/S13','วันไทยและ physical opening มี evidence; ตอบสั้นตรง'),
 'C17':('S10/S12','empty bookable ไม่ยืนยัน physical closed'),
 'C18':('S07/S08/S10','free set ตรง15:00/freshness/mapping ไม่ใช่ available_now'),
 'C19':('S08/S12/S15','live unavailable ยังตอบ booking procedure'),
 'C20':('S05/S06/S15','same task สองเกมคงสอง subject-bound needs'),
 'C21':('S07/S08/S10/S14','before/after FirstBlood พร้อม linked exceptions ครบ'),
 'C22':('S05/S06/S10','not PSU staff ไม่เลือก staff rate เพราะ substring'),
 'C23':('S07/S10/S12','FAQ-rate claim mapping/overlapping applicability/authority/conflict'),
 'C24':('S03/S08/S16','published new price revision reread โดยไม่ถาม service ซ้ำ'),
 'C25':('S03/S08/S16','withdrawal ไม่ resurrect history/cache'),
 'C26':('S03/S16','unrelated epoch change ไม่ทิ้ง valid task slots'),
 'C27':('S07/S10','known complete empty inventory จึงตอบไม่มีใน scope นั้น'),
 'C28':('S07/S12','unknown inventory ไม่แปลเป็นไม่มี'),
 'C29':('S07/S10','platform supported ไม่เท่ากับ offering/installed ที่ศูนย์'),
 'C30':('S13/S14','ภาษาอังกฤษคง decision/exception/critical quantities'),
 'C31':('S06/S12/S17','invalid model body แยกจาก source missing'),
 'C32':('S01/S11/S15','queue/model/children ใช้งบเดียว finalizer reserve ไม่ reset'),
 'C33':('S04/S08/S16','เกมชื่อใหม่จาก owner form ตอบ how_to_play ไม่เพิ่ม regex'),
 'C34':('S06/S11/S12','unsupported operator ไม่ให้โมเดล invent formula'),
 'C35':('S07/S10/S12','broken FK/invalid platform ไม่เดาผู้เล่น'),
 'C36':('S03/S05','explicit reset price→booking ไม่ตอบ abandoned task'),
 'C37':('S07/S12/S15','ตอบที่อยู่แล้วถามเฉพาะ material price slot')}
def cell(x):return str(x).replace('|','/').replace('\n',' ')
lines=['# Coverage ก่อนเริ่ม implementation R102','',
 'สถานะทุกแถวคือ **planned — ยังไม่รันใน R102** เอกสารนี้ไม่ได้เปลี่ยน executed flags ของ R97 และไม่ถือผล R101 เดิมเป็น exact acceptance ของ R102','',
 '## 1. R97 exact scenarios ทั้ง 37 ข้อ','',
 '| ID | คำถามต้นฉบับ | Preconditions ที่ runner ต้องสร้าง | Expected invariant | ขั้นที่เกี่ยวข้อง / จุดต้องปิด |','|---|---|---|---|---|']
cases=[]
for c in spec['cases']:
 stages,note=routes[c['id']]
 lines.append('| '+' | '.join(map(cell,[c['id'],c['utterance'],c['fixture_precondition'],c['expected_behavior'],stages+' — '+note]))+' |')
 cases.append({**c,'executed':False,'status':'design_only','stages':stages.split('/'),'implementation_focus_th':note,'fixture_id':None,'runner_case_id':None,'result':None})
lines+=['','## 2. Task graph ทั้ง 32 งาน','',
 'Required alternatives ด้านล่างคัดจาก registry documentation ของ R101 เพื่อเป็นฐาน ไม่ได้ประกาศว่า R102 implementation ผ่านแล้ว ทุก task ต้องมี reader/render/status และอย่างน้อย source-backed positive กับ relevant missing/invalid path ผูก case IDs ก่อน freeze','',
 '| Task | Kinds | Required alternatives ฐาน R101 | R102 acceptance ที่ต้องมี |','|---|---|---|---|---|']
tasks=[]
for s in task_lines:
 cols=[x.strip() for x in s.strip('|').split('|')];task=cols[0].strip('`')
 target='เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่'
 if task in {'price','rental'}:target+='; currentness/unit/audience/operator และ conflict'
 elif task in {'policy','procedure','faq_content','competition_rules'}:target+='; action/actor/conditions/dependent clauses ไม่ตกหล่น'
 elif task=='schedule':target+='; physical-open/bookable/closing/maintenance แยกและ timezone/date scope'
 elif task=='live_status':target+='; target window/provider/mapping/freshness/partial static needs'
 elif task.startswith('game_'):target+='; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed'
 lines.append('| '+' | '.join(cols[:3]+[target])+' |');tasks.append({'task':task,'baseline_kinds':cols[1],'baseline_required':cols[2],'acceptance_th':target,'status':'planned','executed':False})
lines+=['','## 3. Owner kinds ทั้ง 24 หมวด','',
 'ทุกแถวต้องมี create/edit/withdraw ใน isolated fixture, preview/published separation, correct revision receipts และ Thai/English task-specific queries ไม่ใช้ข้อมูลทดลองแทน production','',
 '| Kind / ฟอร์ม | Publish-core fields จาก schema เดิม | References ที่ต้องคง |','|---|---|---|']
kinds=[]
for c in catalog:
 core=[f['key'] for f in c['fields'] if f.get('publish_core')]
 refs=[f"{f['key']}→{f['reference_kind']}" for f in c['fields'] if f.get('reference_kind')]
 lines.append('| '+' | '.join(map(cell,[c['kind']+' / '+c['owner_form'],', '.join(core) or 'ตาม readiness ราย task',', '.join(refs) or 'ไม่มี FK ที่ประกาศใน catalog']))+' |')
 kinds.append({'kind':c['kind'],'publish_core_fields':core,'reference_fields':refs,'lifecycle_required':['create','edit','withdraw'],'status':'planned','executed':False})
lines+=['','## 4. จุดที่ต้องแก้ก่อน integrated batch','',
 '1. ปิด policy/FAQ clause coverage และ source-scoped amounts; ไม่ย้ายค่าจากหัวข้ออื่นเพื่อให้ตรง keyword',
 '2. ปิด structured/prose claim mappings และ authority-conflict safe path โดยไม่เปลี่ยน approved history',
 '3. ปิด targeted gaps/clarification: audience, validity, universal eligibility และ source scope',
 '4. ปิด whole-request semantic orchestration สำหรับ mixed resolved/unresolved needs และ live/unknown target locks',
 '5. ปิด runtime tracing/output contracts และ exact fixtures/runner สำหรับทุกแถว ไม่ใส่ executed=true จากการอ่านเอกสาร',
 '6. แยก owner facts และ real integration blockers ออกจาก implementation status','',
 'ก่อน freeze ให้ใส่ implementation paths และ fixture/case IDs จริงใน machine-readable matrix จากนั้นหนึ่ง orchestrator รันทุก lane โดย source ไม่เปลี่ยน ดู [FULL_FLOW_TH.md](FULL_FLOW_TH.md) สำหรับลำดับทั้งหมด']
(R/'COVERAGE_MATRIX_TH.md').write_text('\n'.join(lines)+'\n','utf8')
manifest={'status':'design_only_not_implemented_or_executed','date':'2026-10-20','timezone':'Asia/Bangkok',
 'baseline':'R101 release_subset09','reference':'R97 Flow V2','runtime_edited':False,'chatbot_tests_run':False,
 'design_counts':{'r97_exact_scenarios':len(cases),'tasks':len(tasks),'owner_kinds':len(kinds),'target_language_wording_variants':37*3*4},
 'execution_counts':{'requests':0,'model_calls':0,'behavioral_assertions':0},
 'batch_policy':{'freeze_after_all_implementation':True,'one_integrated_run_before_analysis':True,'intermediate_chatbot_reruns':False,'rerun_legacy':False},
 'reference_hashes':{str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [spec_path,catalog_path,flow_path]},
 'cases':cases,'tasks':tasks,'owner_kinds':kinds}
(R/'FLOW_COVERAGE_PLAN.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'design_counts':manifest['design_counts'],'execution_counts':manifest['execution_counts']},ensure_ascii=False))
