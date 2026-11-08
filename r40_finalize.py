import json, hashlib, re, difflib, os, statistics, urllib.request
from pathlib import Path
from datetime import datetime
from r40_targeted_probe import OUT, BASE, cases, grade
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name, content):
    with (OUT/name).open('x',encoding='utf-8') as f:f.write(content)
def dump(name,value):save(name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def link(p,label=None):return f'[{label or p.name}]({p.as_posix()})'
def latest(pattern):return max(OUT.glob(pattern),key=lambda p:p.stat().st_mtime)
def traces(b):
    t=b.get('trace') or []
    return t.get('stages',[]) if isinstance(t,dict) else t

os.environ.pop('R40_CASE_FILE',None)
baseline_file=latest('baseline_r39_3_*summary.json'); baseline=read(baseline_file)
case_map={c['id']:c for c in cases()}
baseline_results=[grade(case_map[r['id']],r['records']) for r in baseline['results']]
dump('BASELINE_R39_3_REGRADING_FINAL_ORACLE.json',dict(original_file=baseline_file.name,original_passed=baseline['passed'],
    regraded_passed=sum(r['passed'] for r in baseline_results),cases=len(baseline_results),results=baseline_results))
final_files=[latest(f'final_r40_3_{s}_*summary.json') for s in ('targeted','transfer','boundary','mixed')]
adjacent=latest('adjacent_http_*summary.json'); final_files.append(adjacent)
finals=[read(p) for p in final_files]
assert all(x['passed']==x['executed_cases'] for x in finals), 'Final HTTP gate failed.'
with urllib.request.urlopen('http://127.0.0.1:8097/health',timeout=5) as r:health=json.load(r)
assert health['runtime']['version']=='2026.10.06-targeted-flow-r40.3'
assert health['runtime']['local_llm']['enabled'] and health['runtime']['semantic_rag']['enabled']
dump('HEALTH_R40_3_FINAL.json',health)
total_cases=sum(x['executed_cases'] for x in finals); total_requests=sum(x['requests'] for x in finals)
final_cases={r['id']:r for r in finals[0]['results']}

before=read(OUT/'before_manifest.json'); changes=[]; protected=[]
protected_paths=['booking_dashboard/center_schedule.json','data/curated/service_policy_answers.json',
 'data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','app/calculator/service_fee.py']
for rel,oldhash in before.items():
    p=ROOT/rel; newhash=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
    if rel in protected_paths:protected.append(dict(path=rel,before_sha256=oldhash,after_sha256=newhash,unchanged=oldhash==newhash))
    if newhash!=oldhash:
        assert p.exists(), 'An original file was removed: '+rel
        changes.append(dict(path=rel,kind='modified',before_sha256=oldhash,after_sha256=newhash))
        original=OUT/'before'/rel
        if original.exists():
            patch=''.join(difflib.unified_diff(original.read_text(encoding='utf-8-sig').splitlines(True),
                    p.read_text(encoding='utf-8-sig').splitlines(True),fromfile='before/'+rel,tofile='after/'+rel))
            dest=OUT/'changes_this_turn'/Path(rel+'.patch');dest.parent.mkdir(parents=True,exist_ok=True)
            with dest.open('x',encoding='utf-8') as f:f.write(patch)
for rel in ('app/pipeline/control_request.py','tests/test_targeted_dialogue_r40.py'):
    if rel not in before:changes.append(dict(path=rel,kind='added',after_sha256=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()))
assert all(r['unchanged'] for r in protected)
dump('SOURCE_CHANGES_THIS_TURN.json',changes);dump('PROTECTED_FACT_HASH_CHECK.json',protected)
package=Path((OUT/'release_r40_3_path.txt').read_text(encoding='utf-8'))
hashes=read(OUT/'release_r40_3_hashes.json')
package_drift=[rel for rel,h in hashes.items() if not (package/rel).exists() or hashlib.sha256((package/rel).read_bytes()).hexdigest()!=h]
assert not package_drift
code_drift=[]
for folder in ('app','web_chat'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
            rel=p.relative_to(ROOT); target=package/rel
            if not target.exists() or target.read_bytes()!=p.read_bytes():code_drift.append(rel.as_posix())
assert not code_drift
dump('RELEASE_INTEGRITY_FINAL.json',dict(version=health['runtime']['version'],installation_id=health['runtime']['installation_id'],
    package_files=len(hashes),package_drift=package_drift,source_code_drift=code_drift,logs_excluded_from_release_hash=True))

unit_rows={}
for p in sorted(OUT.glob('source_regression_*.json')):
    for row in read(p):unit_rows[row['file']]=row
assert len(unit_rows)==7 and all(r['returncode']==0 for r in unit_rows.values())
unit_count=0
for row in unit_rows.values():
    text=(OUT/row['evidence']).read_text(encoding='utf-8')
    row['test_methods']=int(re.search(r'Ran (\d+) tests?',text)[1]);unit_count+=row['test_methods']
dump('FINAL_AUTOMATED_GATES.json',dict(http_cases=total_cases,http_requests=total_requests,unit_test_methods=unit_count,
    unit_rows=list(unit_rows.values()),http_reports=[p.name for p in final_files],
    baseline_original_passed=baseline['passed'],baseline_strict_passed=sum(r['passed'] for r in baseline_results),baseline_cases=31,
    release_version=health['runtime']['version'],owner_approval=False,live_booking_truth_verified=False,full_corpus_rerun=False))

statuses=read(OUT/'BACKLOG_EXECUTION_STATUS_INITIAL.json')
scope={
 1:'รุ่น/URL แสดงบนเว็บและ health ของ r40.3 ตรงกัน; เว็บเดิมและชุดแจกเดิมยังมีอยู่',
 2:'สร้าง release r40.3 แยกใหม่สำหรับเครื่องนี้; ยังไม่รวมชุด WithModels/DownloadModels ใหม่',
 4:'แก้ README เรื่อง URL/pอร์ตและแหล่ง booking; ตรวจแม่แบบ cache ตาม health 0 วินาที',
 6:'เส้นทาง missing game controls 13 สำนวน TH/EN ไม่มี intent model stage; ไม่ได้วัด SLA ทุกหมวด',
 7:'เพิ่ม dialogue_selection_v1 สำหรับหลายเกม/โซน; active task ที่เก็บใน parent ยังเน้นราคา',
 8:'ตรวจ 2–3 turn ที่เลือกหัวข้อและแก้ selection; ไม่รับรองบทสนทนายาวทุกแบบ',
 9:'เลือก 2–4 รายการ คงลำดับและตัดซ้ำ; เกิน 4 ถามแบ่งรายการ ไม่ตัดทิ้งเงียบ ๆ',
 10:'ตรวจขอบเขตโซนที่เลือก; all หลายมิติยังต้องวาง contract ต่อ',
 11:'คำถามใหม่ชนะ pending control; ตรวจปฏิเสธปุ่มแล้วถามราคา PC',
 12:'regression revision/idempotency/TTL เดิมผ่าน; ไม่เพิ่ม persist หลัง restart',
 14:'ตรวจ Valoant/cockpik และ mixed language ที่สัมพันธ์กับรายการ; ไม่สร้าง corpus typo ใหม่ขนาดใหญ่',
 17:'กันเลขโรมัน/อารบิก ชื่อภาคผิด และตรวจ guard ในแต่ละ child',
 18:'ใช้ control detector/edition guard ร่วมกันและเพิ่ม parent compound guard; ยังไม่รวม resolver ทั้งระบบ',
 19:'targeted TH/EN ผ่าน; human/official-name review ยังรอ',
 35:'read-only/freshness/date/empty data fixtures เดิมผ่าน; ไม่ยืนยัน snapshot จริง',
 37:'fault/date fixtures ผ่านในขอบเขตเดิม; ไม่ใช่ network outage/load soak ใหม่',
 39:'regrade baseline 31 เคสด้วย oracle เดียวกัน แยกผลเดิม 20/31 จากผลเข้ม 18/31',
 41:'เพิ่ม child operation/unknown scope/price target assertions; ไม่ปรับ grader ทั้ง corpus',
 42:'เพิ่ม 12+8+4 เคสใหม่ระหว่างรอบ แยก first pass จาก regression หลังนำมาแก้',
 46:'สำรอง 306 ไฟล์ก่อนแก้ สร้าง raw/release/log ใหม่; รักษา owner hashes 5 จุด',
 47:'background launcher เปิดจริงและใช้โมเดลที่มีอยู่ในเครื่อง; ไม่ตั้ง always-on/auto-start ถาวร',
 50:'candidate r40.3 ผ่าน targeted gates; ยังไม่ประกาศ production',
 52:'ตรวจ source app/web ตรง package และ static package hashes หลังรัน; ยังไม่ rebuild canonical/index ใหม่',
 54:'36 บทสนทนาตรวจ full rule sections ตาม coverage เดิม; ไม่ทำ viewer/source-update migration',
 55:'known+unknown control ตอบส่วนที่มีพร้อมระบุส่วนไม่ยืนยัน; parent outcome ยังไม่เป็นมาตรฐานทุกหมวด',
 59:'health ของ r40.3 cache 0 วินาที; คู่มือแยก default 10/clamp 0–30 แล้ว',
 62:'เพิ่ม selection provenance/errors/limit และแก้ log context ไม่ตี dialogue selection เป็นราคา; trace schema ยังหลายชนิด',
 63:'แก้ parent ที่ย่อคำถามผสม เหตุการณ์ navigation+price และ controls+price ทั้งสองลำดับ TH/EN; ยังไม่รับรองทุก combination',
 64:'เปรียบเทียบ baseline model-on กับ targeted fast paths; ไม่ใช่ ablation หลาย architecture ใหม่',
 66:'launcher/manifest/JS syntax ผ่าน เปิด candidate จริง; ไม่ใช่ fresh-machine/offline installation proof'
}
for row in statuses:
    number=int(row['id'][1:])
    if 20<=number<=32:state='waiting_for_owner_or_human';note='คำถามและหลักฐานเฉพาะข้ออยู่ใน F-'+row['id']+'; ไม่แก้ fact/approval โดยเดา'
    elif number==33:state='deferred_by_user';note='เก็บ booking truth จริงตามที่ผู้ใช้พักไว้'
    elif number==38:state='full_corpus_not_run_by_user_request';note='รอบนี้ใช้ targeted เท่านั้น'
    elif number==45:state='completed_for_this_turn';note='Git before/after จาก workdir ตรง exit 0; diff ของรอบนี้เทียบ backup แยกจากก่อนหน้า'
    elif number in scope:state='partially_implemented_or_verified_scope';note=scope[number]
    else:state='remaining_not_executed';note='มี Flow เฉพาะข้อ แต่ยังไม่มีหลักฐานใหม่ว่าทำครบในรอบนี้'
    row.update(execution_status=state,execution_note=note)
dump('BACKLOG_EXECUTION_STATUS_FINAL.json',statuses)

rounds=[]
for p in sorted(OUT.glob('*summary.json'),key=lambda p:p.stat().st_mtime):
    x=read(p)
    if 'results' in x:
        count=x.get('executed_cases',x.get('conversations',len(x['results'])))
        rounds.append((p,x.get('label',p.stem),x['passed'],count,'HTTP/model on' if 'port' in x else 'source/model off'))
lat_old=[r['latency'][0] for r in baseline_results if r['kind']=='missing_controls']
lat_new=[r['latency'][0] for r in finals[0]['results'] if r['kind']=='missing_controls']
fast_stages=[]
for r in finals[0]['results']:
    if r['kind']=='missing_controls':
        ts=traces(r['records'][-1]['response'])
        fast_stages.append(dict(id=r['id'],missing_slot_trace=any(t.get('stage')=='closed_control_request' for t in ts),
                               universal_intent_stage=any(t.get('stage')=='universal_intent' for t in ts)))
assert all(x['missing_slot_trace'] and not x['universal_intent_stage'] for x in fast_stages)
dump('MISSING_CONTROLS_LATENCY_AND_STAGES.json',dict(baseline_seconds=lat_old,final_seconds=lat_new,
    baseline_median=statistics.median(lat_old),final_median=statistics.median(lat_new),final_min=min(lat_new),final_max=max(lat_new),
    stages=fast_stages,scope='sequential local-machine warm run; not SLA or load benchmark'))

case_doc='# วิเคราะห์ก่อน/หลังรายเคส r40.3\n\nเปรียบเทียบ 31 เคสเดิมด้วย oracle ชุดสุดท้ายเดียวกัน; raw เดิมไม่ถูกแก้ไข\n\n'
for old in baseline_results:
    new=final_cases[old['id']]; c=case_map[old['id']]
    case_doc+=f"## {old['id']} — {c['kind']}\n\n- คำถาม: "+' → '.join('`'+q+'`' for q in c['turns'])+'\n'
    case_doc+=f"- ก่อน: {'ผ่าน' if old['passed'] else 'ผิด contract'} / `{old['mode']}`\n- หลัง: {'ผ่าน' if new['passed'] else 'ผิด contract'} / `{new['mode']}`\n"
    case_doc+='- เงื่อนไขตรวจหลัง: '+', '.join(f'{k}={v}' for k,v in new['checks'].items())+'\n'
    selected=[t for t in traces(old['records'][-1]['response']) if t.get('stage') in {'universal_intent','conversation_request','active_query_selection','route','entity_resolution','input_recovery','game_entity_resolution','candidate_margin'}]
    case_doc+='- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):\n\n```json\n'+json.dumps(selected,ensure_ascii=False,indent=2)+'\n```\n\n'
    case_doc+='**คำตอบก่อน**\n\n'+old['answer'][:1200]+('\n\n[ตัดข้อความในเอกสารนี้; ฉบับเต็มอยู่ raw]' if len(old['answer'])>1200 else '')+'\n\n'
    case_doc+='**คำตอบหลัง**\n\n'+new['answer'][:1600]+('\n\n[ตัดข้อความในเอกสารนี้; ฉบับเต็มอยู่ raw]' if len(new['answer'])>1600 else '')+'\n\n'
save('CASE_ANALYSIS_R40_3_TH.md',case_doc)

report=f'''# รายงาน Flow → แก้ → ทดสอบ → วิเคราะห์ r40.3

วันที่ {datetime.now().isoformat(timespec='seconds')} / เครื่องเจ้าของ / เริ่มจาก r39.3

## 1. ผลและขอบเขตที่ยืนยันได้

- เว็บจริง `{health['runtime']['version']}` / installation `{health['runtime']['installation_id']}` ที่ [เปิด Chatbot](http://127.0.0.1:8097/)
- เปิด Local LLM และ semantic RAG จริงตาม health; candidate ใช้ WordPress read-only/cache 0 วินาที
- รอบสุดท้าย **{total_cases}/{total_cases} บทสนทนา**, **{total_requests} HTTP requests**; {unit_count}/{unit_count} test methods ของชุดที่เกี่ยวข้อง ผ่านตามหลักฐานรายไฟล์
- baseline 31 เคสเดิม: เกณฑ์แรก 20/31; เมื่อเพิ่มเงื่อนไขว่าปุ่มจองต้องเป็นการจองและราคา PC ต้องเลือก PC จริง ได้ **18/31**; r40.3 ได้ **31/31 ด้วย oracle เดียวกัน** เก็บ regrade เป็นไฟล์ใหม่
- ไม่รัน full corpus สองหมื่นกว่าข้อ ไม่เก็บ live booking truth ที่พักไว้ และไม่ใช้ผล fixture แทนสถานะจริง
- มี Flow ครบ B001–B066 แต่ผลชุดนี้ไม่พิสูจน์ว่าปิดทั้ง 66 รายการ; สถานะรายข้อแยก owner/deferred/partial/remaining
- สำรอง app/web/templates/tests ก่อนแก้ 306 ไฟล์และตรวจ hash ข้อมูลต้องรักษา 5 จุด; แก้ {len(changes)} ไฟล์เฉพาะรอบนี้ตามรายการ diff ไม่รวมเครดิตงานที่ Git ยังไม่บันทึกก่อนหน้า

## 2. ทำไมคำตอบยังผิดทั้งที่มีข้อมูล

มีหลายชั้นที่ทำงานต่อกัน การมี source ถูกต้องแก้ไม่ได้ถ้า operation/target/scope ถูกเปลี่ยนก่อน lookup คะแนน route สูงก็ไม่รับรองว่าตอบคำขอครบ

| กลุ่มสาเหตุ | พฤติกรรมก่อน | จุดที่เสีย | ควรตอบ/การแก้ที่ลงมือ |
|---|---|---|---|
| Missing slot กับ domain confusion | `Tell me the keyboard controls please` กลายเป็นรายการอุปกรณ์; `List all game buttons` บอกไม่ยืนยันเกม | keyword keyboard/buttons ชนะ operation และเรียก model ก่อนรู้ว่าขาดชื่อเกม | ถามชื่อเกมอย่างเดียว; detector ยอมรับเฉพาะ generic words และกันชื่อจริง/เลข/negation/hardware |
| Pending selection หาย | ขอปุ่มแล้วตอบ `VALORANT กับ Mario Kart 8 Deluxe` → no_answer/availability หรือเกมเดียว | การต่อข้อความกับ semicolon ไม่เท่ากับส่งรายการงาน; heuristic splitter ทำหล่น | สร้าง `dialogue_selection_v1` จากการเลือกจริง คง operation แล้ว execute ทุก child |
| Scope หลายโซนหาย | `PC and PS5` ถูกอ่านเป็นอุปกรณ์หรือแสดงแค่โซนเดียว | resolver รับเป้าหมายเดียว/ใช้ assistant catalog เป็นบริบทไม่พอ | ทำ requests ต่อโซน ตรวจ selected headers และ forbidden unselected zones |
| Edition normalization ไม่ครบ | `TEKKEN IX` ตอบ TEKKEN 8 | guard กัน Arabic แต่ Roman ไม่ผ่าน; fuzzy alias ทำชื่อใกล้สุดแทนภาค | ตรวจ Roman ที่ถูกไวยากรณ์เทียบ recorded editions, กันทั้ง single และ child; VIII รับเป็น 8; IX ไม่แทนเป็น 8 |
| Unknown Thai title หลุด operation | `มายคราฟต์` หลังถามชื่อเกม กลับถามหมวดเกม/ราคา/จอง | unknown bare Thai ไม่มี entity ที่ยืนยันจึงไม่ถูก merge เป็น game slot | เก็บชื่อที่ผู้ใช้ส่งและ control operation แต่ไม่ยืนยัน title ว่ามี source |
| Unknown ใน scope หลายรายการถูกทิ้ง | `PC and washing machine` ตอบ PC อย่างเดียว | service scan หา PC ได้แล้วใช้ผลบางส่วน | เก็บ selection_errors และขอระบุโซนทั้งหมดใหม่ |
| Negation กินคำขอใหม่ | `ไม่เอาปุ่ม ขอราคาของ PC` ตอบว่าไม่มี service | ตัวอ่านไม่เอาอ่านเลยถึง PC จึง exclude PC ด้วย | หยุด span ตรง `ขอ/ต้องการ/show/want…`; มีคู่ negative ที่ต้องตัด PC จริง |
| Guard เฉพาะ parent | VALORANT + Minecraft/TEKKEN IX เสี่ยง child ไป lookup เกมอื่น | compound เรียก `_answer_single` ตรงโดยข้าม guard ของ entry | guard ชื่อและภาคใน child ด้วย ตอบ known + explicit unconfirmed แยกส่วน |
| Fast answer กลืนอีก task | ปุ่มจองพร้อมราคา ตอบแค่ลิงก์ | booking navigation shortcut ตรวจทั้งประโยคแล้ว return ก่อน split | จำกัด shortcut ให้ navigation เดียวและใช้ใน child ของคำถามผสม |
| Parent adapter ทิ้ง task ก่อน worker | source test ถูก แต่ HTTP r40.2 ยังตอบราคาล้วน | STORE/resolve_request_plan ย่อ original เป็น `Service prices PC` ก่อนเข้า engine | parent ไม่ canonicalize คำถามผสมเป็น fee task เดียว; source harness ต้องจำลองการ rewrite เหมือนเว็บ |
| ภาษาอังกฤษ singular/plural | price ผ่าน แต่ prices ไม่แยก compound | `_english_compound_intent` รู้จัก price/fee/cost แบบ singular | รองรับ plural ใน operation signal เดิมและทดสอบทั้งภาษา |
| Shared tail ตีประโยคเต็มเป็นชื่อ | `PC ราคาเท่าไหร่ และ VALORANT มีปุ่มอะไรบ้าง` → `PC ราคาเท่าไหร่ มีปุ่มอะไรบ้าง` | parser กระจาย tail ปุ่มให้ operand ที่เป็น price question อยู่แล้ว | ถ้า operand มี operation ครบ ห้ามแชร์ tail; ให้ generic split รักษาสอง operation |
| เกิน batch limit หลุดเส้นทาง | เลือก 5 รายการ → availability/detail ผิดหมวด | parser reject >4 แล้ว fallback ไป general path | explicit clarification ครั้งละไม่เกิน 4 รายการ ไม่ execute subset; เป็น technical bound ไม่ใช่ policy ศูนย์ |
| Trace domain ผิด | selection plan ถูก log เป็น service_fee/price_lookup | response finalizer ใช้ price schema กับ plan ใหม่ | รักษา context ของ dialogue_selection_v1 เดิม |

## 3. ทำไมคะแนนสูงยังเลือกคำตอบผิด

ตัวอย่าง HTTP r40.2 ของคำถามปุ่มจองพร้อมราคา: `conversation_request` แสดง confidence 1.0 และ `universal_intent` 0.98 (`method=conversation_plan`) แต่ input ที่ worker ได้เหลือ `Service prices PC` แล้ว คะแนนนี้ยืนยันการจัดประเภทของข้อความที่ถูกย่อ ไม่ตรวจว่าคำขอปุ่มจองเดิมยังอยู่ จึงเกิด outcome `answered_complete` กับคำตอบที่ครบเพียงงานราคา

เกณฑ์ใหม่ตรวจ original requests → child domains → content → scope ไม่ใช้ confidence เป็นเฉลย สำหรับ multi-controls ต้องมีทุก title/operation และ unknown/edition ต้องไม่ถูกแทนเกมอื่น สำหรับ catalog ต้องมีโซนที่เลือกและไม่มีโซนที่ไม่ได้เลือก

พบ false positive ของ grader ด้วย: เคสไทยราคา+ปุ่มมีคำ PC อยู่ในหัวคำถาม แต่ไม่มีคำตอบราคา ค่า string-presence ผ่านได้ จึงเพิ่ม child operation assertions และ unit test ที่ตรวจทั้ง games กับ service_fee เก็บผลเกณฑ์อ่อนและผลเข้มแยกไว้ ไม่ย้อนแก้ raw

## 4. ผลสุดท้ายแยกชุด

| ชุด | ผ่าน/ทั้งหมด | HTTP requests | หลักฐาน |
|---|---:|---:|---|
'''
for title,p,x in zip(('ปัญหาเดิม TH/EN','สำนวนใหม่/unknown/3 turn','boundary/limit/family/partial','controls+price สองลำดับ TH/EN','regression สอง turn ราคา/กฎ/หัวข้อ'),final_files,finals):
    report+=f"| {title} | {x['passed']}/{x['executed_cases']} | {x['requests']} | {link(p)} |\n"
report+='\n### Unit / fixture gates\n\n| ไฟล์ชุดทดสอบ | methods | exit | ผลดิบ |\n|---|---:|---:|---|\n'
for row in unit_rows.values():report+=f"| {row['file']} | {row['test_methods']} | {row['returncode']} | {link(OUT/row['evidence'])} |\n"
report+=f'''
fixture ตรวจ lunch/maintenance/closed/VR-hour-blocking/read-only/ผิดวัน/ข้อมูลว่าง/transport-success-but-wrong-count ไม่ใช่การเทียบ WordPress กับรายการจองจริง

### เวลาเส้นทางถามชื่อเกม

13 สำนวนในรอบเรียงลำดับบนเครื่องนี้: median ก่อน {statistics.median(lat_old):.4f}s, หลัง {statistics.median(lat_new):.4f}s; ช่วงหลัง {min(lat_new):.4f}–{max(lat_new):.4f}s; trace มี `closed_control_request` และไม่มี `universal_intent` ใน 13 เคสนี้ ไม่ได้สรุป latency ทุกหมวดหรือวัด concurrency SLA

## 5. รอบวิเคราะห์และแก้ — เก็บทั้งผลที่ผิดและที่ผ่าน

| รอบ/ผลที่เก็บ | ประเภท | ผ่าน | เอกสารผล |
|---|---|---:|---|
'''
for p,label,passed,count,kind in rounds:report+=f'| {label} | {kind} | {passed}/{count} | {link(p)} |\n'
report+='''
12 transfer cases พบใหม่ครั้งแรกหลังแก้ชุดแรก: 11/12; หลังนำ failure มาแก้ไม่ถือเป็น independent holdout อีก ส่วน boundary พบ 4/8 ใน first pass, แก้ผ่าน source แต่ HTTP r40.2 ยังเหลือ 6/8 จึงกลับไปแก้ parent adapter ไม่จบที่ source pass ส่วน controls+price first pass 0/4 และ unit พบ weak oracle จึงปรับ parser/เกณฑ์จนผ่านเว็บจริง ชุดเหล่านี้เป็น regression หลังใช้พัฒนาแล้ว คะแนน 91/91 ไม่ใช่ accuracy โลกจริง

## 6. ตรวจทาน Flow หลังทำจริง

1. เพิ่ม state schema selection, selection_errors, target limit และ parent preservation ก่อน worker; ตรวจ original-vs-resolved ในทุกชั้น
2. เพิ่ม per-child edition/unknown/navigation guard; fast path ต้องไม่ข้ามคำขออื่น
3. เพิ่ม operation assertions ไม่ใช้เฉพาะชื่อในคำตอบ; แยก unit/source/HTTP/owner truth
4. ขอบเขตที่ไม่มี source ต้อง missing/conflict/unavailable ไม่แต่ง fact หรือบังคับ approximate entity
5. จำกัด parser selection 2–4 รายการ, fast mixed navigation 2–3 clauses; ใส่ข้อจำกัดจริงในแผนแทนวาดว่าทุกชนิดใช้ state เดียวแล้ว
6. แยก old/new release พร้อม hash; manifest เป็นที่มาของ version และ UI แสดง URL จริง
7. Stop เมื่อ targeted failures ที่ยืนยันได้หมดและ regressions ผ่าน; งาน owner/live/production/holdout ที่ยังขาดหลักฐานไม่ถูกปิดโดยคะแนนรวม

## 7. ยังเหลืออะไร และควรทำลำดับใด

### P0 ข้อมูลที่ต้องตัดสินใจ/ยืนยัน

- ราคาใน source พ้นช่วงประกาศแล้ว: ขอฉบับอัตราที่ใช้จริง ณ ปัจจุบัน วันที่เริ่ม/สิ้นสุด กลุ่มผู้ใช้และแพ็กเกจ; รอบนี้ทดสอบกับ recorded rates ไม่ยืนยันราคาใช้จริงวันนี้
- Tekken pause: ขอ clause ฉบับรับรองว่าข้อจำกัด pause ใช้ Round/Game/Match และให้เลือกข้อความ authoritative ที่ขัดกัน
- RoV ข้อ 6.1.5/6.1.5.1: ขอส่วนต่อจากข้อความที่ถูกตัดและฉบับเต็ม
- ข้อมูล roster/check-in, VALORANT 6 source gaps, อายุ/ค่าสมัคร, คนนอก/อาหาร/ถ่ายภาพ: คำถามและ source IDs แยกใน F-B024–F-B029
- รายการอุปกรณ์จริง ปุ่มที่ปรับบนเครื่องจริง และชื่ออังกฤษทางการ: ใช้รายการ review ให้เจ้าของยืนยัน ไม่เปลี่ยนให้ดู complete โดยแต่ง
- V2 canonical queue 104 pending และ active claim IDs ว่าง: ไม่ใช่แปลว่า legacy/English runtime ไม่มีคำตอบ; activation ต้องผ่าน source/human workflow

### P1 ทำเองต่อได้

1. ขยาย typed task state ให้ครอบคลุมหมวดอื่นและการกลับไปงานเก่า/partial outcome ทุก child; ตอนนี้ parent active task ยังเป็นราคา และ selection plan ใหม่ไม่ใช่ persistent multidomain state
2. เสริม task coverage contract ทุก compound combination และ all หลายมิติ; 91 เคสนี้รองรับเฉพาะแบบที่ตรวจ ห้ามอนุมาน universal robustness
3. ทำ independent holdout ที่ไม่เคยใช้แก้ และ adjudicate historical corpus ด้วย content/target/scope oracle ก่อนรันใหญ่ตามคำสั่งใหม่
4. จัดชุดแจก WithModels/DownloadModels จาก source เดียวกับ r40.3 พร้อม checksum/launcher; fresh Windows/ไทยใน path/offline-first installation ยังไม่ตรวจ
5. รวม trace schema, source hash/English invalidation, local-source viewer และขั้น refresh canonical/index ตาม Flow

### P2 งานเมื่อเลือกใช้งานจริง

- Live per-slot truth ยังพักตามผู้ใช้; load/worker-crash/network-soak/retention/public deployment ต้องเก็บหลักฐานตาม Flow ก่อนรับรอง
- พบเครื่องมืออ่านไฟล์ของ PowerShell ล้มเหลวหนึ่งครั้งพร้อม OutOfMemory ระหว่างมีเว็บหลายรุ่นเปิดอยู่; HTTP รอบนั้นยังผ่าน ไม่สรุปว่าเป็น chatbot answer error
- ปิดเฉพาะ process tree r40.1/r40.2 ที่เปิดรอบนี้หลังตรวจ command line แล้ว เก็บ r40.3 และเว็บเดิมของผู้ใช้; หลักฐาน cleanup แยก เก็บ log ทั้งหมดไม่ลบ
- เครื่อง local ต้องเปิดอยู่ขณะตอบสด; background launcher ไม่ทำให้เครื่องที่ปิดอยู่ตอบได้ และไม่ตั้ง auto-start/public server โดยเดา

## 8. ไฟล์ส่งมอบ/การเปิดใช้

'''
report+=f'- {link(OUT/"FLOW_R40_FINAL.md", "Flow ฉบับตรวจทานครบ 66 รายการ")}\n- {link(OUT/"BACKLOG_EXECUTION_STATUS_FINAL.json", "สถานะลงมือรายข้อ 66 รายการ")}\n- {link(OUT/"CASE_ANALYSIS_R40_3_TH.md", "คำตอบก่อน/หลังและคะแนน trace รายเคส")}\n- {link(OUT/"FINAL_AUTOMATED_GATES.json", "ผล gates พร้อมการแยก owner truth")}\n- {link(OUT/"PROTECTED_FACT_HASH_CHECK.json", "hash ข้อมูลที่รักษาไว้")}\n- {link(OUT/"SOURCE_CHANGES_THIS_TURN.json", "ไฟล์ที่แก้เฉพาะรอบนี้")}\n- {link(package/"Open-PSU-Esports-Background.cmd", "เปิดชุด r40.3 เบื้องหลัง")} หรือ [เว็บที่เปิดอยู่](http://127.0.0.1:8097/)\n\nชุดใหม่เป็น candidate สำหรับเครื่องนี้ ใช้โมเดลที่ติดตั้งอยู่แล้ว ไม่ใช่ชุด WithModels ใหม่ที่รับรองการแจกไปเครื่องอื่นได้ทันที\n'
save('REPORT_R40_3_TH.md',report)

flow=(OUT/'FLOW_R40_REVIEWED.md').read_text(encoding='utf-8')
flow+='''
## 9. Revision หลังลงมือจริง — r40.3 (ใช้ส่วนนี้เมื่อรายการในแผนเดิมยังไม่ระบุ implementation)

### 9.1 ลำดับที่ใช้จริงและข้อแตกต่างจากภาพ Flow

1. UI ส่ง original question + locale + session/turn ID + ack; parent STORE ตรวจ duplicate/revision ก่อนวางงาน
2. price planner ตรวจ compound operations ก่อน canonicalize; ถ้ามีราคาและอีก operation ให้ปล่อย original เข้าตัวแยกงาน ไม่เปลี่ยนเป็น fee-only query
3. หากไม่มี price plan ใช้ latest eligible context สำหรับ pending selection; explicit new question ไม่ถูกนำไปเติม slot เก่า
4. เลือกหลายเกม/โซน → schema `dialogue_selection_v1` จากตัวเลือกผู้ใช้ ไม่ใช้รายการที่ assistant เสนอเป็น selected; 2–4 items → dedupe + requests ตามลำดับ
5. Unknown zone → selection_errors → ถามโซนทั้งหมดใหม่; ไม่ execute PC แล้วทิ้ง unknown. มากกว่า 4 → explicit batch clarification ไม่ fallback ไป intent ทั่วไป ขอบเขตนี้เป็นข้อจำกัดทางเทคนิค
6. Generic control question ที่ไม่ระบุชื่อ → shared detector → ask game ก่อน intent model; detector กัน explicit name/ตัวเลข/negation/hardware และไม่ใช่ universal Thai spell-correction
7. Navigation-only → booking URL แบบไม่แต่งตำแหน่งปุ่ม. Navigation+operation อื่น → แยก child; shortcut ไม่ return คำตอบทั้งประโยค
8. Child execution ต้องผ่าน edition/unknown/navigation guard เช่นเดียวกับ single request; partial known+unknown มีคำตอบส่วนที่รู้และแจ้งไม่ยืนยันส่วนที่เหลือ
9. Shared-tail parser กระจาย operation เฉพาะ operands ที่เป็นชื่อ ถ้า operand มี operation ครบแล้วห้ามเขียน tail ใหม่ทับความหมาย
10. ตรวจ child domain/intent, expected target IDs/headers, forbidden other scopes, required actual facts; ชื่อที่อยู่ในหัวคำถามไม่ใช่ proof ว่ามีคำตอบส่วนนั้น
11. Commit response/revision ตาม STORE; parent outcome ของ generic multi-domain ยัง delegated_existing_pipeline ไม่อ้างว่ามี complete/partial schema ร่วมทุกงาน
12. Log selection context ต้องคง domain/operation ของ selection ไม่ใช้ price finalizer กับทุก schema

### 9.2 สัญญาข้อมูล selection ที่เพิ่มจริง

```json
{
  "schema_type": "dialogue_selection_v1",
  "schema_version": 1,
  "act": "select_multiple_targets",
  "context_used": true,
  "domain": "game_controls",
  "operation": "control_lookup",
  "targets": ["VALORANT", "Beat Saber"],
  "requests": ["What are the controls for VALORANT?", "What are the controls for Beat Saber?"],
  "selection_errors": [],
  "selection_limit": null,
  "provenance": "explicit_user_selection_of_pending_task"
}
```

Plan สร้างภายใน parent จาก session ที่ใช้ได้ ไม่ถือ payload ที่ client ส่งเองเป็น fact. targets/requests ต้องมีจำนวนตรงกัน ≤4 และแต่ละ request ≤240 อักขระ; unknown zone/overflow เป็น clarification ก่อน execution. ยังไม่มี state persistence หลัง server restart และไม่ขยาย active price task เป็น generic state ทุกหมวดในรอบนี้

### 9.3 เมทริกซ์ acceptance ของปัญหาที่แก้

| ความสามารถ | ต้องถูก | Negative/directional ที่ต้องเปลี่ยนผล | เกณฑ์ตรวจ |
|---|---|---|---|
| Missing control target | TH/EN/mixed asks game only | hardware model, damage, explicit Minecraft, number, booking button | missing_slot stage/no intent-model stage + operation |
| Pending multi-target | เลือก 2/3/4 เกม/โซน คง operation | unknown zone; 5 targets; ineligible history | every child target/domain + explicit clarification overflow |
| Edition | VIII→recorded 8, XVI/III ที่บันทึกไว้ | IX/9 ไม่ตอบ 8; number of people ไม่เป็น edition; pronoun I ไม่เป็นภาค | original number/title preserved + per-child guard |
| Partial controls | VALORANT+unknown retains known controls | unknown/absent edition ไม่ถูกแทนเกมที่มี source | known factual controls + explicit missing child |
| Negation | ไม่เอาปุ่ม ขอราคา PC = price PC | ไม่เอา PC ขอ VR = exclude PC | negated span boundary + selected target |
| New task | What is VALORANT? หลัง controls = details | bare VALORANT หลัง controls = controls | context eligible + explicit operation overrides |
| Compound preservation | navigation+price/controls+price TH/EN สองลำดับ | price comparisons/service names with and ยังเป็น operands ของ operation เดียว | parent original intact + child domains + real price/control content |
| Delivery | 2–3 turns + ack/full rule sections | new anonymous page/TTL/replay/revision constraints | fixture/store oracles + HTTP identity |

### 9.4 การแก้ grader และความน่าเชื่อถือของผล

- บันทึก original baseline 20/31 และ final-oracle baseline 18/31 แยกไฟล์ ไม่แก้ raw เดิม
- เพิ่ม assertions: booking navigation ไม่เป็น game controls; price PC ต้องเลือก PC; partial unknown ไม่ถูกตอบเกมอื่น; unknown zone ต้อง clarification
- String contains เป็นเพียงส่วนหนึ่ง: ต้องตรวจ child operation และห้าม missing_game_context ใน known-target child. การมี PC อยู่ในหัวคำถามไม่ใช่คำตอบราคา
- Source harness เดิมยังไม่จำลอง parent canonical rewrite; หลังเว็บ r40.2 พบผิด ได้ปรับ harness ให้ตาม adapter จริงแล้ว. ผล HTTP เป็น gate ของชุดเปิดใช้
- เคสใหม่ที่นำผลไปแก้แล้วเป็น regression; ไม่เรียก independent holdout และไม่อนุมาน accuracy ของ corpus/ผู้ใช้จริง

### 9.5 ตรวจทาน Flow หลัง loop

| Review | สิ่งที่พบจากหลักฐาน | การแก้ Flow |
|---|---|---|
| R4 | multi semicolon ผ่าน resolver แต่ executor ทิ้ง target | ส่ง typed request list และตรวจทุก child |
| R5 | negation span ตัด PC ของงานใหม่ | ระบุ boundary ของ speech act และ directional negative tests |
| R6 | unknown zone ถูกทิ้ง/unknown child ข้าม guard | เพิ่ม selection_errors/per-child guard |
| R7 | >4 selections fallback ผิดและ shortcut กลืน task | explicit bound และ guard เป็นราย child |
| R8 | prices ไม่ถูกอ่านเป็น price compound | เพิ่ม morphology test และสองลำดับ TH/EN |
| R9 | source ผ่านแต่ parentเว็บย่อ original ก่อนเข้า worker | parent preservation + harness parity + HTTP gate |
| R10 | Thai shared tail เปลี่ยน operation และ oracle weak | operands must be names + child-domain/content assertions |
| R11 | context finalizer ใช้ price schema กับ selection | schema-specific trace handling |
| R12 | หลาย runtime มีเหตุ OOM ของเครื่องมือ | เก็บ performance limitation/ปิดเฉพาะ runtime ทดสอบที่สร้างเอง/ไม่หยุดเว็บเดิม |

## 10. สถานะรายข้อหลังทำจริง

ตารางนี้ supersede สถานะ “planned” ตอนต้นของแต่ละ F-Bxxx; รายละเอียดวิธีแก้/เกณฑ์เฉพาะข้อยังอยู่ในข้อ 6 ไม่ปิด 66 รายการจากคะแนนรวม

| ID | สถานะปัจจุบัน | ทำจริง/ยังขาด |
|---|---|---|
'''
for row in statuses:flow+=f"| {row['id']} | {row['execution_status']} | {row['execution_note']} |\n"
flow+=f'\n## 11. หลักฐานและผล gate\n\nรอบสุดท้าย {total_cases}/{total_cases} conversations / {total_requests} HTTP requests และ {unit_count}/{unit_count} related test methods ตามหลักฐานรายไฟล์. ไม่รัน full corpus ไม่ยืนยัน owner fact/live truth.\n\n- '+link(OUT/'REPORT_R40_3_TH.md','รายงานสาเหตุ ผลก่อน/หลัง ข้อที่เหลือ')+'\n- '+link(OUT/'CASE_ANALYSIS_R40_3_TH.md','trace/คำตอบรายเคส')+'\n- '+link(OUT/'FINAL_AUTOMATED_GATES.json','automated gates')+'\n- '+link(OUT/'BACKLOG_EXECUTION_STATUS_FINAL.json','machine-readable status 66 ข้อ')+'\n'
save('FLOW_R40_FINAL.md',flow)
review={'flow_ids':re.findall(r'^### F-(B\d{3}) —',flow,re.M),'status_ids':[r['id'] for r in statuses],
        'duplicate_flow_ids':False,'protected_facts_unchanged':True,'source_code_matches_release':True,'release_static_drift':False,
        'http_cases':total_cases,'http_requests':total_requests,'unit_methods':unit_count,'human_or_owner_approval_inferred':False,
        'utf8_replacement_character':any('\ufffd' in text for text in (flow,report,case_doc))}
assert len(review['flow_ids'])==66 and len(set(review['flow_ids']))==66 and not review['utf8_replacement_character']
local_links=[]
for text in (flow,report,case_doc):
    for raw in re.findall(r'\]\((C:[^\n)]+)\)',text):
        path=Path(raw.split(':',1)[0]+':'+raw.split(':',1)[1])
        if not path.exists():local_links.append(raw)
review['missing_local_links']=local_links
assert not local_links, local_links
dump('DOCUMENT_REVIEW_FINAL.json',review)
print(json.dumps(dict(output=str(OUT),http_cases=total_cases,http_requests=total_requests,unit_methods=unit_count,
                     strict_baseline=sum(r['passed'] for r in baseline_results),source_changes=[r['path'] for r in changes],
                     protected_unchanged=True,review_passed=True),ensure_ascii=False,indent=2))
