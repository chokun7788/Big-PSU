import json,hashlib,difflib,re,statistics,urllib.request
from pathlib import Path
import r41_probe
BASE=Path(__file__).resolve().parent;OUT=r41_probe.OUT
ROOT=r41_probe.ROOT
def save(name,value):
    with (OUT/name).open('x',encoding='utf-8') as f:
        f.write(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def unique(pattern):
    files=list(OUT.glob(pattern));assert len(files)==1,(pattern,files)
    return files[0]
def load(pattern):
    p=unique(pattern);return p,json.loads(p.read_text(encoding='utf-8'))

groups=[]
for pattern,label in [('final_r41_3_targeted_*summary.json','บทสนทนาหลักใหม่'),('final_r41_3_variations_*summary.json','คำถามเพิ่มเติมและขอบบริบท'),
    ('final_r41_3_regression_targeted_*summary.json','เคส r40 หลัก'),('final_r41_3_regression_transfer_*summary.json','สำนวน r40'),
    ('final_r41_3_regression_boundary_*summary.json','ขอบเขตและข้อจำกัด'),('final_r41_3_regression_mixed_*summary.json','คำถามผสมราคา/ปุ่ม'),
    ('adjacent_http_*summary.json','สองรอบ ราคา/กฎ/หัวข้อ')]:
    p,d=load(pattern);assert d['passed']==d['executed_cases']
    groups.append(dict(label=label,file=p.name,**{k:d[k] for k in ('passed','executed_cases','requests')},results=d['results']))
total=sum(g['executed_cases'] for g in groups);requests=sum(g['requests'] for g in groups)
records=[r for g in groups for c in g['results'] for r in c['records']]
latencies=sorted(r['elapsed_sec'] for r in records)
with urllib.request.urlopen('http://127.0.0.1:8093/health',timeout=6) as r:health=json.load(r)
assert health['runtime']['version']=='2026.10.06-task-memory-r41.3'
assert health['runtime']['local_llm']['enabled'] and health['runtime']['semantic_rag']['enabled'] and health['warmup']['ok']
save('HEALTH_FINAL_R41_3.json',health)

regressions=sorted(OUT.glob('source_regression_*.json'))
units=json.loads(regressions[-1].read_text(encoding='utf-8'));unitcount=0
for u in units:
    assert u['returncode']==0,u
    text=(OUT/u['evidence']).read_text(encoding='utf-8');unitcount+=int(re.search(r'Ran (\d+) tests',text)[1])

before=json.loads((OUT/'before_manifest.json').read_text(encoding='utf-8'))
changed=[];new=[];diff=[]
for rel,oldhash in before.items():
    p=ROOT/rel;assert p.is_file(),rel
    if hashlib.sha256(p.read_bytes()).hexdigest()!=oldhash:
        changed.append(rel);old=OUT/'before'/rel;assert old.is_file(),rel
        diff.extend(difflib.unified_diff(old.read_text(encoding='utf-8').splitlines(True),p.read_text(encoding='utf-8').splitlines(True),fromfile='before/'+rel,tofile='after/'+rel))
for folder in ('app','web_chat','deployment_templates','tests'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.relative_to(ROOT).as_posix() not in before:
            rel=p.relative_to(ROOT).as_posix();new.append(rel)
            diff.extend(difflib.unified_diff([],p.read_text(encoding='utf-8').splitlines(True),fromfile='/dev/null',tofile='after/'+rel))
protected=['booking_dashboard/center_schedule.json','data/curated/service_policy_answers.json','data/competition_rules/competition_rule_chunks.jsonl',
    'data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','app/calculator/service_fee.py']
assert not set(protected)&set(changed)
release=Path((OUT/'release_r41_3_path.txt').read_text(encoding='utf-8'))
parity={}
for folder in ('app','web_chat'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
            rel=p.relative_to(ROOT).as_posix();parity[rel]=(release/rel).is_file() and hashlib.sha256((release/rel).read_bytes()).hexdigest()==hashlib.sha256(p.read_bytes()).hexdigest()
assert all(parity.values())
save('SOURCE_CHANGE_R41.diff',''.join(diff));save('SOURCE_AUDIT_R41.json',dict(changed=changed,new=new,protected_unchanged=protected,source_release_parity=parity,
    before_file_count=sum(p.is_file() for p in (OUT/'before').rglob('*')),before_hash_count=len(before),git_changes_preexisting_preserved=True))

gold={c['id']:c for c in r41_probe.cases()};regrades=[]
for pattern in ('baseline_source_r40_3_*summary.json','baseline_http_r40_3_*summary.json'):
    p,d=load(pattern);rs=[r41_probe.grade(gold[c['id']],c['records']) for c in d['results']]
    metadata_only=sum(not c['passed'] and set(k for k,v in c['checks'].items() if not v)<={'outcome','task_ids_complete','child_statuses'} for c in rs)
    regrades.append(dict(file=p.name,original_saved_passed=d['passed'],strict_passed=sum(c['passed'] for c in rs),executed=len(rs),
        metadata_only_failures=metadata_only,behavior_failures=sum(not c['passed'] for c in rs)-metadata_only,results=rs))
save('REGRADES_R41.json',regrades)
gates=dict(http_conversations=total,http_requests=requests,http_passed=total,unit_methods=unitcount,source_unit_file=regressions[-1].name,
    runtime_version=health['runtime']['version'],runtime_url='http://127.0.0.1:8093/',source_parity_files=len(parity),
    protected_files_unchanged=protected,changed_files=changed,new_files=new,
    latency_sec=dict(p50=statistics.median(latencies),p95=latencies[max(0,int(len(latencies)*.95)-1)],max=max(latencies)),
    limits=['targeted checks only, not full corpus','execution contract is not factual accuracy certification','owner facts and live occupancy not verified','no clean-machine portability proof'])
save('FINAL_AUTOMATED_GATES_R41.json',gates)

flow=(OUT/'FLOW_R41_INITIAL.md').read_text(encoding='utf-8')
flow+='''
## Flow หลังแก้และตรวจทาน

### A. รับคำถามและสถานะ

1. ตรวจ session/turn fingerprint: turn ID เดิมกับคำถามใหม่เป็น conflict; duplicate เดิม replay ไม่เพิ่ม revision
2. Parent store ตรวจ TTL/session/revision และ acknowledgement ของคำตอบก่อนหน้า
3. Explicit return-to-topic → หา requested task ของ operation นั้นที่ server ทำเสร็จและ client แจ้งว่าได้รับแล้ว
4. ถ้าตัวกลับเรื่องมีชื่อเป้าหมายใหม่ ตัวเลข หรือคำปฏิเสธ → ใช้ตัวแก้บริบทปกติ รักษาคำถามใหม่; เงื่อนไขส่วนเกินที่ยังรวมไม่ได้ → ถาม scope
5. Bare all → ตรวจว่ามี operation เดียวหรือหลายเรื่อง; หลายเรื่องถามว่าหมายถึงส่วนใด
6. Controls ของเกมที่เลือก → ตอบปุ่มจากแหล่งเดิมใหม่; unresolved child ยังอยู่ใน scope; ห้ามเหลือแต่ known titles
7. Catalog มีทั้งโซนและเกม → bare all/ordinal ถามแกนที่ต้องการ; all zones ชัดเจนแล้วจึงแสดงทุกโซน
8. Family menu → ใช้ตัว resolver ที่มีอยู่ตรวจว่าคำถามมี family ambiguity จริง แล้วเก็บเฉพาะ candidates ที่แสดงในคำตอบตามลำดับ; generic example list ไม่ใช่ menu
9. ราคาใช้ schema ราคาเดิม รักษา customer_group_ids/packages/duration/exclusions; resume ไม่ใช้ราคาที่เคยตอบเป็นแหล่งใหม่

### B. แผนและการ execute

1. Parent ส่ง context_resolution และ request_plan มีชนิดชัดถึง worker
2. dialogue_state_clarification_v1 → deterministic clarification TH/EN ไม่เรียก intent model
3. dialogue_selection_v1 → execute 1–4 requests ตามลำดับ; เกินขอบเขตถามแบ่งคำขอ ไม่ตัด subset
4. Compound เดียวกันหลาย targets ต้องรวม memory โดยรักษา child queries และ request labels แม้บาง target ไม่มีข้อมูล
5. Deadline ระหว่าง children → เก็บ executed/pending IDs แต่ระบุ unavailable และ output_withheld; ไม่รายงานคำตอบทั้งหมดสำเร็จ
6. Final language/source validator veto → schema_rejected แม้ children เคย execute; ไม่ให้ parent complete ค้างอยู่
7. Memory ไม่เก็บ answer/hits/prices/status availability เพื่อ replay facts; เก็บคำขอเพื่อให้ execute ใหม่เท่านั้น

### C. Contract ที่อ่านได้

| ค่า | ความหมาย | สิ่งที่ไม่ได้พิสูจน์ |
|---|---|---|
| answered | มีคำตอบของ task ที่ผ่าน validator ปัจจุบัน | ไม่ยืนยัน semantic accuracy ทุกข้อหรือนโยบายล่าสุด |
| partial | full-rule coverage ยังมี remaining/missing clauses | ไม่ยืนยันว่าอ่านเอกสารครบ |
| clarification | ต้องเลือกเป้าหมาย/ขอบเขต | ไม่ใช่ข้อมูลในฐานสูญหาย |
| missing | no_answer/unconfirmed/unverified/source gap | ไม่แปลว่า API ล่ม |
| unavailable | เส้นทาง timeout/backend unavailable | ไม่แปลว่าเครื่องถูกจอง |
| rejected | validator ไม่ยอมส่ง draft | ไม่ใช้ validator ok ของข้อความ fallback เป็นหลักฐานว่า draft ถูก |

Compound มี expected_task_ids/executed_task_ids/tasks/answered_task_ids/pending_task_ids/missing_task_ids/outcome. API, log และ decision artifact บันทึก contract เดียวกัน

### D. ทำจริง 4 รอบตรวจและปรับ

1. Baseline แสดงช่องว่าง request memory ข้ามหมวด และ absence ของ coverage metadata; แยก metadata-only failure จากคำตอบผิด
2. เพิ่ม memory + scoped all + per-task contract → source และ HTTP หลัก 25/25
3. Variation 16 เคสพบ family menu ยังไม่ harvest และ Thai unknown target inherit old game; พบ grader catalog ใช้ mode เดียว และเฉลย second option ไม่ตรงลำดับจริง → แก้โค้ดและ oracle แยกกัน
4. Regression พบ guard กว้างไปจน bare unknown selections ไม่เก็บ pending operation → จำกัดเฉพาะ complete controls question; เพิ่ม partial-all เพื่อกัน missing child ถูกตัด; final variants 18/18 พร้อม unit/HTTP เดิม

ไม่ถือจำนวนรอบเป็นหลักฐานความถูกต้อง ผลผ่านต้องมี raw และ oracle ที่ตรวจ operation/content/scope/outcome ตามชนิด task

## หลักการประกอบและข้อจำกัดหลักฐาน

- CheckList: ใช้ minimum functionality/invariance/directional expectation ตรวจ all/resume/new target โดยไม่เหมารวมคะแนนชุดใหญ่: https://aclanthology.org/2020.acl-main.442/
- CheckDST: แยกการรักษา dialogue state จากการตอบภาษาได้: https://aclanthology.org/2022.findings-emnlp.391/
- Schema Guided Dialogue: ใช้ domain/operation/slots แยกชัด: https://arxiv.org/abs/1909.05855
- ใช้แนวคิดประกอบการออกแบบ ไม่อ้างว่า implementation นี้เหมือนระบบใน paper หรือได้คะแนนเดียวกัน ไม่ค้น paper เพิ่มในรอบนี้

## งานที่ยังทำเองต่อได้

1. Generalize clarification/return selectors ไปยังสมาชิก เวลา และ booking พร้อม fixture; รอบนี้ยังไม่ได้เปิด explicit resume ของทุกหมวด
2. วัด retrieval candidate quality + content completeness ต่อ fact/section แยกจาก task execution; semantic accuracy ไม่ได้เกิดจาก contract อย่างเดียว
3. เพิ่ม typo/paraphrase holdout ที่อิสระจากการแก้ครั้งนี้; fresh variants ที่ถูกใช้แก้แล้วถือเป็น regression
4. สร้าง WithModels/DownloadModels ตาม source ใหม่และตรวจบนเครื่องสะอาด; candidate รอบนี้เป็นแพ็กเกจทดลองในเครื่องนี้
5. ตรวจ booking stale/error/count/timezone ด้วย fixture เพิ่ม แล้วค่อย real slot oracle เมื่อมีข้อมูลจริง
6. ตรวจ recovery/latency under concurrency และ source update/translation gap; เก็บ rate/owner policy ไม่แก้โดยเดา

## จุดที่ต้องให้มนุษย์ยืนยัน

- อัตราค่าบริการปัจจุบันหลังตารางเก่าหมดอายุ 31/03/2026
- Tekken pause conditions ที่เอกสารขัดกัน; RoV ข้อที่ต้นฉบับไม่ครบ; competition roster/check-in/VALORANT source gaps
- สถานะจองจริงรายเครื่องและช่วงเวลาเทียบ booking ของเจ้าของ ไม่อนุมานจาก connect API สำเร็จ
- นโยบายถ่ายภาพ/อาหาร/ผู้ใช้ภายนอก และศัพท์ชื่อทางการที่แหล่งยังไม่ยืนยัน

## เกณฑ์ส่งมอบ

Passed targeted automated checks + unchanged protected files + frozen local release/source parity. ไม่เท่ากับ backlog 66 ข้อหมด ไม่รับรองภาษาแปรรูปทุกแบบ ไม่รับรอง current owner facts หรือ fresh-machine installation
'''
save('FLOW_R41_FINAL.md',flow)

rows=['| ชุด | ผ่าน/ทั้งหมด | Requests | หลักฐาน |','|---|---:|---:|---|']
for g in groups:rows.append(f"| {g['label']} | {g['passed']}/{g['executed_cases']} | {g['requests']} | [{g['file']}]({(OUT/g['file']).as_posix()}) |")
report=f'''# รายงาน r41.3 — request memory และคำตอบหลายเรื่อง

## สรุป

แก้ source จริง 4 ไฟล์ เพิ่ม module 2 ไฟล์ และ test 1 ไฟล์ เก็บก่อนแก้/raw/candidate เก่าแยกไว้ ไม่ commit หรือ reset งานเดิม รุ่นเว็บที่ตรวจ: http://127.0.0.1:8093/ — `{health['runtime']['version']}`

## สิ่งที่แก้แล้ว

1. กลับไปเรื่องราคา/ปุ่ม/กฎ/รายชื่อเกม หลังเปลี่ยนหัวข้อ โดยรักษาเกม/โซน/กลุ่มบุคคลภายนอก
2. ทั้งหมด/all of them หลังเลือกเกม แสดง controls ของเกมที่เลือก; หลาย operation ถาม scope
3. อันแรก/อันที่สอง/first/second ใช้ลำดับ family choices ที่แสดงจริง; catalog หลายระดับไม่เดาแกน
4. Minecraft controls ภาษาไทยไม่ถูกเติม VALORANT จากคำถามเก่า และ all รอบถัดไปไม่หวนกลับผิดเกม
5. หลาย targets ไม่จำเหลือเกมสุดท้าย; missing child ไม่ถูกตัดเมื่อ all/resume
6. แยก answered/partial/clarification/missing/unavailable/rejected ใน API/log/decision artifact; timeout เก็บ executed/pending แต่ไม่กล่าวว่า output ครบ

## ผลอัตโนมัติ

{chr(10).join(rows)}

รวม **{total}/{total} conversations**, **{requests} HTTP requests**. Unit ที่เกี่ยวข้อง **{unitcount}/{unitcount} test methods**. ไม่รัน full corpus สองหมื่นกว่าเคส

ผล baseline HTTP ด้วยเกณฑ์เดียวกัน: **{regrades[1]['strict_passed']}/25**; มี failure เพราะคำตอบ/บริบท **{regrades[1]['behavior_failures']}** และเพราะ metadata coverage ใหม่ยังไม่มี **{regrades[1]['metadata_only_failures']}**. จึงไม่เรียกทุก failure ว่าตอบผิด

รอบ variation แรก 11/16 ตามเกณฑ์ที่บันทึกไว้: 2 เคส catalog ตอบสองโซนจริงแต่ grader ไม่รับ multi mode, 2 เคส family ordinal ยังไม่เข้าใจและเฉลยเดิมระบุ second title ผิดลำดับ, 1 เคส Thai unknown target inherit old game. เก็บ raw เดิมและแก้ oracle แยก ไม่แก้คะแนนย้อนหลังในไฟล์เดิม

ตอนขยาย guard พบ regression ของ bare unknown selections จึงจำกัด guard เฉพาะ controls question ที่สมบูรณ์และรัน regression ใหม่ ไม่ยกระดับ guard ให้ครอบทุกคำถามโดยไม่มีหลักฐาน

## ความเร็วและรันไทม์

ชุดนี้ p50 {gates['latency_sec']['p50']:.3f}s / p95 {gates['latency_sec']['p95']:.3f}s / max {gates['latency_sec']['max']:.3f}s. เป็นเวลาที่เครื่องนี้กับคำถามชุดนี้หลัง warmup ไม่ใช่ SLA ทุกคำถาม

Health ยืนยัน local LLM + semantic RAG เปิด และ preflight/warmup ผ่าน ไม่ได้แปลว่าทุกเคสเรียกโมเดลหรือพิสูจน์ทุกคำตอบถูกตามนโยบายจริง

## การรักษาข้อมูล

ตรวจ hash ไฟล์หลัก 5 ไฟล์ไม่เปลี่ยน: calendar เจ้าของ, service policy, competition chunks, review queue, calculator rates. Source app/web ตรง candidate **{len(parity)} ไฟล์**. มี [source diff]({(OUT/'SOURCE_CHANGE_R41.diff').as_posix()}) เทียบ backup รอบนี้ ไม่ใช้ git diff ทั้งหมดแทนงานรอบนี้

รุ่น r40.3/r41.1/r41.2/log เดิมยังอยู่ ปิดเฉพาะ baseline/r41.1 ที่ผมเปิดในรอบนี้เพื่อเปลี่ยนไป candidate ใหม่; รุ่นอื่นที่คุณเปิดไว้ไม่ได้ปิด. พบรุ่นแจกเดิมที่พอร์ต 8092 จึงรุ่นใหม่เลือก 8093

## ข้อจำกัดที่ยังเหลือ

- Memory เก็บ requested tasks ≤8 operations/session, TTL 30 นาทีโดยค่าเริ่มต้น, ไม่อยู่หลัง server restart. ครอบคลุม explicit return grammar ที่ตรวจ; ไม่รับรองทุก paraphrase/ทุกหมวด
- Bare all ของ catalog ยังถามว่าหมายถึงโซนหรือเกมเมื่อไม่ชัด; ถ้าบอก all zones จึงแสดงทุกโซน
- Generic task status เป็น execution coverage; completeness ของเนื้อหาต้องใช้ domain oracle เพิ่ม โดยกฎละเอียดมี clause coverage แยก
- Fixture/mock tests พิสูจน์ state/timeout contract; ยังไม่พิสูจน์ real booking occupancy และ owner policy
- Current prices, pause conflicts, truncated rules และ source gaps ต้องรอหลักฐานมนุษย์ ไม่ใช้คะแนน tests ตัดสิน
- ชุดทดลองใหม่นี้ใช้ Python/Ollama/models ที่มีในเครื่อง ไม่ได้อัปเดตชุดแจก WithModels/DownloadModels และไม่ยืนยันเครื่องสะอาด

## ไฟล์ใช้งาน/ตรวจต่อ

- [Flow ฉบับสมบูรณ์]({(OUT/'FLOW_R41_FINAL.md').as_posix()})
- [หลักฐานผ่านอัตโนมัติ]({(OUT/'FINAL_AUTOMATED_GATES_R41.json').as_posix()})
- [หลักฐานต่อบทสนทนา]({(OUT/'CASE_ANALYSIS_R41_TH.md').as_posix()})
- [ตัวเปิด candidate ที่ตรวจบนเครื่องนี้]({(release/'Open-PSU-Esports-Background.cmd').as_posix()})
'''
save('REPORT_R41_3_TH.md',report)

analysis=['# วิเคราะห์บทสนทนาต่อเคส r41.3','', 'คะแนนผ่านหมายถึงเกณฑ์ task/content/scope ที่กำหนด ไม่รับรอง owner facts ทุกข้อ','']
for g in groups:
    analysis+=['## '+g['label'],'']
    for c in g['results']:
        ident=c.get('id') or c.get('case',{}).get('id')
        analysis+=['### '+ident,'','ผล: ผ่าน' if c['passed'] else 'ผล: ไม่ผ่าน','', 'เกณฑ์: '+json.dumps(c.get('checks',{}),ensure_ascii=False),'']
        for i,r in enumerate(c['records'],1):
            b=r['response'];contract=b.get('task_contract') or {}
            analysis +=[f"#### รอบ {i}: {r['payload']['question']}",'',f"mode: `{b.get('mode')}`; resolved: `{b.get('resolved_question')}`; outcome: `{contract.get('outcome')}`",'',b.get('answer',''),'']
            state=b.get('context_resolution',{})
            analysis +=['เหตุผลการผูกบริบท: '+str(state.get('reason','ไม่มี debug resolution')),'', 'Child statuses: '+json.dumps([(t.get('task_id'),t.get('status'),t.get('category'),t.get('mode')) for t in contract.get('tasks',[])],ensure_ascii=False),'']
save('CASE_ANALYSIS_R41_TH.md','\n'.join(analysis)+'\n')

status=json.loads((BASE/'r40_targeted_flow_20261006_022135_9e5ad7/BACKLOG_EXECUTION_STATUS_FINAL.json').read_text(encoding='utf-8'))
updates={
'B007':'เพิ่ม generic requested-task schema ใน parent; explicit resume price/control/rules/catalog/equipment selector. ไม่ครบทุกหมวด',
'B008':'ตรวจ HTTP 1–4 rounds และ unit archive เกิน 8 turns/TTL/revision. ไม่รับรอง long dialogue ทุกแบบ',
'B010':'all controls, unresolved children, multiple operations และ explicit all zones มี contract; ambiguous catalog axis ถามเฉพาะขอบเขต',
'B011':'explicit return หลังเปลี่ยนเรื่อง TH/EN รักษา targets/customer filters และหลาย child queries; ใช้ acknowledged parent archive ไม่ใช่ cached answer',
'B041':'oracle ตรวจ operation/content/scope และ per-child execution status; แก้ metadata-only/catalog/ordinal gold errors แยก raw. ยังไม่ full semantic oracle',
'B055':'compound execution coverage แยก missing/clarification/unavailable/partial/rejected และ pending IDs; timeout output_withheld ไม่กล่าวว่า complete. ยังไม่ content completeness ทุก fact',
'B062':'task contract อยู่ใน API/log/decision artifact เชื่อม question/child operation/status; ไม่ตรวจ source ranking ทุก stage ในรอบนี้'}
for row in status:
    if row['id'] in updates:
        row['r41_execution_note']=updates[row['id']];row['r41_status']='partially_implemented_and_targeted_verified'
    else:row['r41_status']='not_reassessed_in_this_round'
save('BACKLOG_STATUS_R41.json',status)
print(json.dumps(dict(conversations=total,requests=requests,units=unitcount,changed=changed,new=new,parity=len(parity),baseline_regraded=[(r['strict_passed'],r['metadata_only_failures'],r['behavior_failures']) for r in regrades]),ensure_ascii=False))
