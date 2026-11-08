"""Audit saved results and explain failures without issuing new questions."""
import collections,hashlib,json
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent;RUN=R/'main_natural'
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
rows=[json.loads(x) for x in (RUN/'RESULTS.jsonl').read_text('utf8').splitlines()]
jobs=[json.loads(x) for x in (R/'EFFECTIVE_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()];byjob={j['id']:j for j in jobs}
facts={f['id']:f for f in read(R/'COMMON_READ_MODEL.json')['facts']}
configs=read(R/'SELECTED_42.json');ranks=read(R/'RANKING_BY_CATEGORY.json');scores=read(R/'SCORES_42.json')
events=[json.loads(x) for x in (RUN/'MODEL_EVENTS.jsonl').read_text('utf8').splitlines()]
bye={(e['id'],q):e for e in events for q in e['question_ids']}
assert len(bye)==sum(e['question_count'] for e in events)
event_ids=collections.Counter(e['id'] for e in events);collisions={k:v for k,v in event_ids.items() if v>1}
freeze=read(RUN/'RUN_FREEZE.json');add=read(R/'EXCLUSION_ADDENDUM.json');manifest=read(R/'DATA_MANIFEST.json')
assert all(sha(R/p)==h for p,h in freeze['files'].items())
assert sha(Path(manifest['source_database']))==manifest['sha256']
assert sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl')==add['effective_workload_sha256']
expected={(c['id'],j['id']) for c in configs for j in jobs if c['category']==j['category']}
actual={(x['flow_id'],x['question_id']) for x in rows}
assert len(rows)==4200 and len(actual)==4200 and actual==expected
assert all(x['question']==byjob[x['question_id']]['question'] for x in rows)
assert not any('หน่วยโทษ' in x['question'] for x in rows)
assert all((e['flow_id'],q) in actual for e in events for q in e['question_ids'])
def failure_type(x):
 g=x['grade']
 if g['passed']:return 'passed'
 if x['model_event_id'] and not bye[(x['model_event_id'],x['question_id'])]['schema_ok']:
  return 'model_protocol' if bye[(x['model_event_id'],x['question_id'])]['transport_ok'] else 'model_transport'
 if not any(g[k] for k in ['missing_claims','unrequested_claims','wrong_values','evidence_mismatches']):return 'answer_state_only'
 if g['wrong_values']:return 'value_mismatch'
 if g['evidence_mismatches']:return 'evidence_mismatch'
 if g['missing_claims'] and g['unrequested_claims']:return 'missing_and_other_claims'
 if g['missing_claims']:return 'missing_required_claims'
 if g['unrequested_claims']:return 'other_or_extra_claims'
 return 'review_required'
primary=collections.Counter(failure_type(x) for x in rows)
audit={'verified_at':datetime.now().astimezone().isoformat(),'designs':len(read(R/'DESIGNS_140.json')),'implemented_configurations':len(configs),'categories':14,'effective_questions':len(jobs),'unique_flow_question_pairs':len(actual),'executions':len(rows),'per_flow':dict(collections.Counter(x['flow_id'] for x in rows)),'frozen_original_files_unchanged':True,'source_database_unchanged':True,'effective_workload_matches_addendum':True,'excluded_topic_main_executions':0,'model_identity_verified_before_after':read(RUN/'TEST_COMPLETE.json')['model_identity_verified'],'model_events':len(events),'model_event_id_unique':not bool(collisions),'model_event_id_collisions':collisions,'model_event_and_question_composite_unique':True,'model_event_question_results_all_present':True,'classification_exclusive':dict(primary),'model_transport_failures':sum(not e['transport_ok'] for e in events),'model_protocol_failed_batches':sum(e['transport_ok'] and not e['schema_ok'] for e in events),'model_protocol_failed_questions':sum(e['question_count'] for e in events if e['transport_ok'] and not e['schema_ok']),'c06_internal_id_questions':sum('migrated_' in j['question'] for j in jobs if j['category']=='C06'),'source_and_results_hashes':{'source':manifest['sha256'],'read_model':sha(R/'COMMON_READ_MODEL.json'),'effective_jobs':sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl'),'results':sha(RUN/'RESULTS.jsonl'),'model_events':sha(RUN/'MODEL_EVENTS.jsonl')},'production_installed':False,'semantic_accuracy_independently_verified':False}
write(R/'AUDIT_FINAL.json',audit)
profiles={
'C01':('คำถามข้อมูลศูนย์ใช้คำว่าเรื่อง/รายละเอียดแทน label ใน projection ทำให้ typed ไม่ bind facet; lexical บางข้อเลือกที่อยู่แทนคำถามอื่น','location/contact intent → center/facility identity → direct field; semantic ช่วยเลือก field เมื่อจำเป็น → ตรวจว่าไม่มี contact/time ปน','เพิ่ม aliases ของ overview/operator/contact ตาม field และแยกคำถามศูนย์ออกจากกิจกรรม ไม่ให้คำว่า Phuket เลือกทุก record'),
'C02':('source มีตำแหน่งแล้ว แต่สำนวน “ใครดูแลงานอะไร” ไม่ตรง role aliases; hybrid เสียคะแนน schema เพิ่มจาก typed ที่อ่านตรงได้','public entity resolver → name/team/role → public-field allowlist → typed read → semantic เฉพาะชื่อ/หน้าที่ไม่ลงตัว','เพิ่ม role paraphrases ที่เป็น data/config; ห้าม fallback ไปเบอร์ส่วนตัวเมื่อไม่มี field และไม่ส่ง typed success ให้ LLM ซ้ำ'),
'C03':('entity ถูกแต่บางคำตอบรวมชนิดอุปกรณ์ที่ไม่ได้ขอ หรือเลือกข้อมูล quantity/location แทน spec; ตัวเลขหน่วยอาจถูกแต่ field ผิด','device/resource/zone resolution → requested predicate+unit → relation lookup → aggregate เฉพาะหน่วยที่ถาม → claim scope check','แยกจำนวนเครื่อง จำนวนผู้เล่น และที่นั่ง; semantic เลือก requested facet เพียงที่จำเป็น และ renderer ซ่อน None/internal keys'),
'C04':('คำอธิบายเกม แนวเกม วิธีเล่น และ offering ถูกใช้แทนกัน; top1 ทำให้หลาย needs ตกหล่น','game/service resolution → catalog/overview/how-to/platform intent → offering enumeration หรือ detail field → completeness check','catalog ต้อง enumerate source set; overview ไม่ตอบแค่ genre และ supported platforms ไม่เท่ากับเกมที่ติดตั้งศูนย์'),
'C05':('typed ได้ 100/100 ในชุดนี้; hybrid ส่ง unknown binding ไปโมเดลแล้วทั้ง 20 ข้อได้รับ schema failure จึงลดเหลือ80','game+platform+preset → normalized action/context → exact binding → confirmed unknown/clarification → deterministic renderer','เก็บ typed เป็นเส้นหลัก; ถ้า action ไม่มี source ให้ยืนยันว่าไม่มีข้อมูล ไม่ส่งโมเดลเดา; ยังต้องตรวจคนละ preset/ภาคก่อนรับรองใช้งานจริง'),
'C06':('การเลือกตัวเลขจาก record ใกล้เคียงทำให้ตอบราคาเฉพาะบริการแทนคำถามหน่วยคิดเงิน; regex ปีไม่รองรับช่องว่างและบาง subject เป็น internal ID','service+audience+date+persons+sessions → validity → rate/unit lookup → deterministic arithmetic → units/rounding check','ตรวจปีแบบ date slot ก่อน retrieval; หากไม่มีราคาอนาคตห้ามยืมปัจจุบัน; แยก policy ต่อคนจากจำนวนเงิน และแทน internal IDs ด้วย display names'),
'C07':('terms ที่ไม่มีข้อมูล เช่น ค่าปรับเกินเวลา ถูกตอบด้วย duration เพราะชื่อแพ็กเกจตรงแต่ facet ไม่ตรง; typed ไม่เข้าใจสำนวนแพ็กเกจพอ','zone+audience+half/full day → package tuple → duration/equipment/price/terms → known/unknown per field','แยกราคา ระยะเวลา มัดจำ overtime และอุปกรณ์; ครึ่งวัน3ชั่วโมง/เต็มวัน7ชั่วโมงตาม owner overlay ไม่ใช้ค่า duration ตอบจำนวนเงิน'),
'C08':('typed7/100 เพราะ subject นโยบายชื่อ “extend session” ไม่อยู่ในคำถามธรรมชาติ; hybrid หลาย need ตอบไม่ครบ','action classifier → booking/payment/attendance condition slots → decision table → required procedure clauses → per-need checklist','compile นโยบายเป็น action/conditions โดยคง source; เปลี่ยนชื่อ/วัน/เครื่องแยก branches และตรวจ clause ครบทั้งสอง need'),
'C09':('typed8/100 จากการ bind subject ไม่ได้; hybrid บางคำถามโอนขาดดึงกฎโอนเกินมาด้วยแม้ source ทั้งสองถูก','payment scenario → payer/amount_delta/slip/document/payment state → exact policy → required evidence/contact → no transaction execution','สร้าง delta>0/delta<0 branches และ document type แยกกัน; ถามหลักฐานเฉพาะที่กฎต้องใช้ ไม่รวมทุกเรื่องที่มีคำว่าโอน'),
'C10':('lexical94/100 สูงสุดในชุดนี้ แต่ยังตอบไม่ได้บาง policy ที่มี source; typed0/100 ไม่ใช่ไม่มีข้อมูล เป็น subject/facet contract ไม่รับสำนวนสถานการณ์','action+actor+condition → permission enum → exception/remedy → scoped answer + source','ต้อง implement condition decision table จริงแทนเรียก flat matcher ว่า graph; unknown อายุ/ค่าปรับต้องไม่ขยายข้ออนุญาตทั่วไป'),
'C11':('source วันและช่วงเวลามี แต่สำนวนเวลา 16–18 ไม่ bind owner policy และ typed แยกช่วงจอง/maintenance ไม่ครอบคลุมภาษาคน','reference date+Asia/Bangkok → dated closure/owner override → weekday schedule → open/bookable/maintenance interval → short date/status','ใช้ interval resolver จริงและแยกช่วงเปิดกับช่วงจอง; หากถามเปิดวันนี้ให้ตอบวันที่+สถานะที่ยืนยันได้ ไม่แสดง metadata ทั้งก้อน'),
'C12':('lexicalได้94/100จาก fixtures แต่มีกรณีเครื่อง PhantomStation77 กลับตอบ PlayStation5ว่าว่าง; typed0/100 เพราะไม่ bind live_status จากสำนวน','exact resource+time binding → read-only provider → freshness/status → requested slot answer → no fallback to a different resource','resource/time mismatch ต้องหยุดก่อน retrieval; provider unavailable/stale ตอบยืนยันไม่ได้ ห้ามใช้ lexical winner โดยไม่มี guard นี้'),
'C13':('hybrid90/100 แต่ยังเอาแผนที่รายการเดิมไปตอบ CS2 ปี2028ที่ไม่มี source; typed80/100 เก็บ unknown ได้ครบแต่รายละเอียดบางข้อพลาด','event+year+game → exact section/dependency clauses → semantic selector within event → full condition/penalty validation','year/event guard ต้องมาก่อน semantic; สร้าง dependency graph ที่จำเป็นและรักษาข้อยกเว้น; เคารพหัวข้อที่เจ้าของงดทดสอบ'),
'C14':('typed0/100 แม้มีfixture เพราะคำถาม closed/open ใช้ facet “status” ไม่ตรง aliases; hybridยังเสียschemaและไม่พบ field','date+event identity → applicability/status → announcement fields+registration link → source timestamp → no-source answer','เพิ่ม status paraphrases และ temporal filter; ต้องมีข้อมูลข่าวจริงที่เจ้าของยืนยันก่อนใช้ให้บริการ ไม่ยก synthetic events เป็นข่าวจริง'),
}
labels={'model_protocol':'โมเดลส่งแผนไม่ครบ/ไม่ผ่าน schema','model_transport':'การติดต่อโมเดล','answer_state_only':'ต่างเฉพาะ answer-state protocol','value_mismatch':'ค่าไม่ตรง oracle','evidence_mismatch':'ที่มาไม่ตรง oracle','missing_and_other_claims':'ขาด claim ที่ขอและมี claim อื่น','missing_required_claims':'ขาด claim ที่ขอ','other_or_extra_claims':'มี claim อื่น/เกินขอบเขต'}
lines=['# R113 — วิเคราะห์ผลและ Flow ที่ควรประกอบจากหลักฐาน','',
'วิเคราะห์จากไฟล์ผลที่รันเสร็จแล้วเท่านั้น ไม่มีการส่งคำถามทดสอบเพิ่ม เอกสารนี้เป็นผลตรวจและแผนพัฒนาต่อจาก prototype ไม่ได้ติดตั้งทับ R78','',
'## 1. ผลตรวจความครบ','',
f"ครบ {len(rows):,} executions / 42 configurations / 14 หมวด / 100 ข้อร่วมกันต่อ Flow ไม่มีคู่ Flow–คำถามขาดหรือซ้ำ และ original frozen files/source database hashes ตรงเดิม ตรวจได้ใน AUDIT_FINAL.json",'',
'## 2. แยกสิ่งที่ผิดก่อนนับเป็นความถูกต้องของคำตอบ','',
'คะแนน strict ผ่านเมื่อ claim IDs/ค่า/ที่มา/ขอบเขต/answer state ตรงครบ เป็น source-contract accuracy ของชุดพัฒนา ไม่ใช่คะแนน semantic accuracy จากมนุษย์ ข้อที่มี claim อื่นไม่ได้ผิดความหมายทุกข้อ เช่น เพิ่มชนิดอุปกรณ์ขณะถามสเปกอาจให้ข้อมูลถูกแต่เกินขอบเขต ในทางกลับกันเลือกเครื่องคนละตัวหรือกฎคนละปีเป็นความผิดขอบเขตที่ยืนยันได้','',
'| กลุ่มหลักที่ไม่ซ้ำกัน | จำนวนผล | วิธีอ่าน |','|---|---:|---|']
for k,v in primary.items():
 if k!='passed':lines.append(f"| {labels.get(k,k)} | {v} | {'ตรวจพบจาก raw model event' if k.startswith('model_') else 'เปรียบเทียบ contract; รายละเอียด semantic ยังต้อง review ตาม source'} |")
lines += ['',f"ผ่าน strict {primary['passed']:,}/{len(rows):,} จากทุกตัวทดลองรวมกัน ค่านี้รวมทั้งแนวทางที่ดีและไม่ดี ไม่ใช่คะแนนของระบบที่ประกอบผู้ชนะแล้ว",'',
f"โมเดลมีบันทึก HTTP {len(events)} ครั้ง สำเร็จด้าน transport {sum(e['transport_ok'] for e in events)} ครั้ง; มี {audit['model_protocol_failed_batches']} batches / {audit['model_protocol_failed_questions']} คำถามที่แผนไม่ครบจน parser ปฏิเสธชุด ผลเหล่านี้เป็น schema/planning failures ไม่ใช่ข้อยืนยันว่า source ไม่มีหรือโมเดลติดต่อไม่ได้",'',
'ข้อผิด answer_state_only ต้องแยกจากคำตอบผิดเนื้อหา: เมื่อ oracle คาด missing_source แต่ตัวอ่านคืน missing_input พร้อมข้อความว่ายังไม่มีข้อมูล ระบบไม่ได้สร้างข้อเท็จจริงผิด เพียงตอบ protocol คนละ state ส่วน expected=answer แต่คืน missing_input และไม่มี claim เป็นการตอบไม่ได้ทั้งที่ oracle มี source','',
'การรันต่อใช้ batch label บางชื่อซ้ำใน C10 แต่ question IDs ของแต่ละ event ไม่ซ้ำ การโยง trace จึงใช้คู่ (model_event_id, question_id) แทน event_id เดี่ยว ตรวจครบทั้ง 903 model-attempted question results ใน AUDIT_FINAL.json โดยไม่เปลี่ยน event logs เดิม ข้อบกพร่องนี้เป็นเรื่องตัวระบุ trace ของ recovery control และไม่ทำให้คู่ Flow–คำถามรันซ้ำ','',
'## 3. โครง Flow ที่เสนอให้ประกอบต่อ','',
'```mermaid','flowchart TD','  Q[คำถามและบริบท] --> N[แยก needs และวันเวลา]','  N --> D[เลือกหมวดของแต่ละ need]','  D --> G[ตรวจ entity / year / resource / scope]','  G --> R[ตัวอ่านเฉพาะหมวด]','  R --> K{ผูกข้อมูลตรงได้หรือไม่}','  K -->|ได้| T[อ่าน typed facts หรือชุดข้อมูลครบ]','  K -->|ตีความไม่ลงตัว| M[โมเดลเลือกหลักฐานภายใน scope]','  K -->|ไม่มีข้อมูลยืนยัน| U[ตอบ unknown ที่ตรงส่วน]','  M --> V[ตรวจ schema ต่อ item และขอบเขต]','  T --> C[ตรวจครบทุก need / หน่วย / เงื่อนไข]','  V --> C','  U --> C','  C --> A[ตอบสั้นตรงคำถามพร้อมที่มา]','```','',
'ความสามารถ router/graph/decision table/การใช้ provider จริงในแผนนี้ยังไม่ได้รับการพิสูจน์จาก benchmark ตัวอ่านแยกหมวดรอบนี้','']
details=[]
for rank in ranks:
 cid=rank['category'];cause,flow,fix=profiles[cid];group=[x for x in rows if x['category']==cid];winner=rank['recommended_flow']
 lines += [f"## {cid} {rank['name']}",'',f"**ผลสามแบบ:** "+'; '.join(f"{k} = {v}/100" for k,v in rank['all_scores'].items()),f'**คะแนนสูงสุดในชุดนี้:** {winner} — ยังไม่ใช่การรับรองพร้อมใช้จริง','',f'**สาเหตุจากผลและ code path:** {cause}','',f'**Flow ที่ควรพัฒนาต่อ:** {flow}','',f'**จุดเสริมที่จำเป็น:** {fix}','']
 # At least one concrete source-linked example for each family, when it failed.
 for family in ['lexical','typed','hybrid']:
  bad=[x for x in group if x['family']==family and not x['grade']['passed']]
  if not bad:continue
  x=next((x for x in bad if failure_type(x) not in ['model_protocol','model_transport','answer_state_only']),bad[0]);j=byjob[x['question_id']]
  lines += [f"### ตัวอย่าง {x['flow_id']} / {x['question_id']}",'',f"คำถาม: {x['question']}",'','คำตอบจริง:','', '> '+x['result']['answer'].replace('\n','\n> '),'',f"กลุ่ม: {labels.get(failure_type(x),failure_type(x))}; expected state={j['expected']['status']}, actual state={x['result']['status']}",'','สิ่งที่ oracle กำหนดจาก source:','']
  if not j['expected']['claims']:lines.append('- ไม่มี source ยืนยันรายละเอียดที่ถามใน snapshot นี้ ไม่ควรยืมข้อมูล subject/ปี/field อื่นมาตอบ')
  for c in j['expected']['claims']:
   f=facts[c['fact_id']];lines += [f"- `{c['fact_id']}`: {c['value']}",f"  - Evidence: `{json.dumps(c['evidence_refs'],ensure_ascii=False)}`"]
  lines+=['']
  details.append({'flow_id':x['flow_id'],'question_id':x['question_id'],'classification':failure_type(x),'expected':j['expected'],'actual':x['result']})
lines += ['## 4. ลำดับแก้ที่ได้จากผลจริง','',
'1. **P0 — ป้องกันตอบผิด entity/วัน/ปี:** C06 ราคาอนาคต, C12 เครื่องที่ไม่มีจริง, C13 กติกาคนละปี ต้อง guard ก่อนค้นและก่อนโมเดล แม้ตัวค้นได้คะแนนรวมสูงก็ไม่ผ่านเงื่อนไขนี้',
'2. **P0 — แก้ model protocol:** ใช้ JSON schema กำหนดจำนวน plans และ indices ไม่ซ้ำ; รับแผนที่ตรวจผ่านเป็นราย item และเก็บข้อที่ขาดเป็น unavailable ไม่ทิ้งแผนถูกทั้ง batch; แยก protocol failure ออกจาก missing_source',
'3. **P1 — เปลี่ยน policy reader:** C08/C09/C10 ต้อง action/condition decision table ที่อ่าน owner facts ได้ ไม่บังคับให้ลูกค้าพูดชื่อ subject ภายใน',
'4. **P1 — เพิ่ม completeness checks:** หลาย needs ต้องมี checklist, game catalog ต้องครบ offering set, กติกาต้อง clauses/dependencies ครบ; ลด extra facets และ renderer ที่แสดง internal IDs',
'5. **P1 — เพิ่ม data lifecycle:** owner เพิ่มข้อมูลใน schema พร้อม aliases/validity/relations → compile index/typed projection อัตโนมัติ → withdraw/update มีผลในตัวอ่าน โดยยังรักษา source evidence; รอบนี้ยังไม่พิสูจน์ data-only additions ของระบบแชทจริง',
'6. **P2 — ปรับการวัดให้แทนผู้ใช้จริง:** 100 ข้อต่อหมวดนี้เป็น development paraphrases; เพิ่ม human/independent semantic review, unknown ภาษาอังกฤษ, router ข้ามหมวด, ข่าวจริงและ provider contracts ก่อนเปรียบคะแนน Legacy อย่างเป็นธรรม','',
'## 5. ขอบเขตข้อสรุป','',
'Hybrid สูงสุด 8 หมวด / typed 2 / lexical 4 ในชุดพัฒนานี้ เป็นหลักฐานว่าควรเลือกตัวอ่านตามชนิดงาน แต่ lexical ที่ชนะ C12 ยังตอบเครื่องผิด จึงห้ามใช้ winner score เป็นเหตุให้ข้าม entity guard หรือปล่อยขึ้นระบบจริง ทั้ง42ตัวเป็น adapters ของ3families และยังไม่ใช่การพัฒนา production-complete ตามชื่อ graph/solver ทั้งหมด','',
'ค่าที่เป็นเจ้าของตอบ/compiled source ไม่ใช่ผลตรวจเชิงเทคนิคทุกข้อ เช่นนโยบายไม่เก็บ login เป็นคำยืนยันเจ้าของ ไม่ใช่ privacy audit เครื่องจริง; จำนวนคำถามและคะแนนไม่พิสูจน์ว่า data migration ทั้ง schema ครบแล้ว','',
'ไฟล์ประกอบ: 01_DESIGNS_AND_SELECTION_TH.md, 01B_ALL_FLOW_STEPS_AND_IMPLEMENTATION_SCOPE_TH.md, 02_BENCHMARK_REPORT_TH.md, AUDIT_FINAL.json, FAILURE_EXAMPLES_WITH_EXPECTED.json และ main_natural/RESULTS.jsonl','']
(R/'03_ROOT_CAUSE_AND_NEXT_FLOW_TH.md').write_text('\n'.join(lines),'utf8')
write(R/'FAILURE_EXAMPLES_WITH_EXPECTED.json',details)
print(json.dumps({'coverage_verified':True,'classification':dict(primary),'model':{'http':len(events),'protocol_batches':audit['model_protocol_failed_batches']},'internal_id_questions':audit['c06_internal_id_questions']},ensure_ascii=False))
