"""Analyze saved real HTTP calls, keeping source gaps separate from code errors."""
import collections,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;run=R/'runs'/sys.argv[1]
def read(p):return json.loads(p.read_text('utf8'))
done=read(run/'TEST_COMPLETE.json');assert done['complete'] and done['unique_question_keys']==1400
out=run/'analysis';out.mkdir(exist_ok=False)
jobs={j['id']:j for j in map(json.loads,(R/'EXISTING_QUESTIONS_1400.jsonl').read_text('utf8').splitlines())}
counts=collections.defaultdict(collections.Counter);failures=[];model=collections.Counter();models={};seen=set();technical=collections.Counter()
with (out/'ALL_FAILURES.jsonl').open('x',encoding='utf8') as f:
    for line in (run/'RESULTS.jsonl').open(encoding='utf8'):
        x=json.loads(line);j=jobs[x['question_id']];g=x['grade'];assert x['question']==j['question'] and x['locale']==j['locale'] and x['question_id'] not in seen;seen.add(x['question_id'])
        positive=bool(j['expected']['claims']);fixture=g['fixture_only_goal'];tech=bool(__import__('re').search(r'(?<![a-z0-9])(?:migrated_rate_|rate_recovered_)',j['question']))
        if tech:technical[x['category']]+=1
        for key in [(x['category'],'all'),('ALL','all'),('ALL',x['locale'])]:
            c=counts[key];c['n']+=1;c['strict']+=g['passed'];c['http_ok']+=g['http_ok'];c['validation_ok']+=g['validation_ok'];c['fixture_only_goals']+=fixture
            c['positive']+=positive;c['nonfixture_positive']+=positive and not fixture;c['nonfixture_positive_passed']+=positive and not fixture and g['passed']
            c['nonfixture_positive_complete_claims']+=positive and not fixture and g['matched_claims']==g['expected_claims']
            c['negative']+=not positive;c['negative_safe_abstention']+=not positive and g['safe_abstention'];c['source_matched_claims']+=g['matched_claims'];c['expected_claims']+=g['expected_claims']
            c['extra_claim_questions']+=bool(g['extra']);c['missing_claim_questions']+=bool(g['missing']);c['value_mismatch_questions']+=bool(g['wrong']);c['pointer_mismatch_questions']+=bool(g['evidence_mismatches'] or g['unknown_refs'])
            c[g['classification']]+=1
        if not g['passed']:f.write(json.dumps(x,ensure_ascii=False)+'\n');failures.append(x)
    for line in (run/'MODEL_EVENTS.jsonl').open(encoding='utf8'):
        e=json.loads(line);models[e['id']]=e
for e in models.values():
    model['calls']+=1;model['transport_ok']+=e['transport_ok'];model['schema_ok']+=e['schema_ok'];model['http_attempted']+=e.get('http_attempted',False)
    model['identity_verified']+=e.get('identity_verified',False)
assert len(seen)==1400
summary={'complete':True,'requests':len(seen),'new_questions':0,'groups':[{'category':c,'locale':l,**dict(v)} for (c,l),v in counts.items()],
 'model':dict(model),'technical_id_questions':dict(technical),'source_and_code_unchanged':done['source_code_inputs_unchanged'],'human_semantic_accuracy_claimed':False,
 'nonfixture_positive_denominator':counts[('ALL','all')]['nonfixture_positive'],'fixture_goals_excluded_from_answered_content_rate':True}
(out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
lines=['# ผลตรวจผ่านแชทจริง — '+run.name,'',
 'ใช้คำถามเดิมครบ 1,400 ข้อ ข้อความ/locale ตรงกับ manifest ทุกข้อ ไม่ส่ง category hint ไม่เพิ่มคำถาม เปิด LLM และยิงจริงผ่าน /api/chat บน candidate DB ข้อมูลที่ย้ายมาแล้ว',
 '', '## เกณฑ์และข้อจำกัด','',
 '- Strict = concept identity/value/status ตรงกับ expected ที่จับคู่ native ก่อนดูคำตอบ พร้อมการตรวจ source refs ที่ snapshot มีจริง ใช้ projection ร่วมเพื่อจัด identity จึงไม่ใช่ independent human semantic accuracy',
 '- Expected เดิมไม่ถูกแก้ ส่วนราคา 24 fields มี presentation ต่างกันแต่ค่าเงิน/หลักฐานยังตรวจแยก การหาหลักฐานผ่านไม่ยืนยันว่ากฎธุรกิจต้นทางถูกต้องครบ',
 '- 160 ข้อ positive ที่ใช้ fake live/news เดิมไม่มี source เหล่านั้นใน native DB รอบนี้ ไม่ใส่ fake data เข้าไปและไม่เอาการตอบ unavailable มาบวกเป็น answered accuracy',
 f"- {sum(technical.values())} คำถามราคาเดิมใช้ internal record IDs เป็นข้อจำกัด corpus ต้องแยกจากภาษาใช้งานทั่วไป แต่ยังเก็บและยิงทุกข้อเหมือนเดิม",
 '- ค่าต่อไปนี้ต่างจาก 99.14% รอบ shared-engine เดิม เพราะใช้ native DB/API และการอ้างอิง source จริง การเทียบข้ามรอบต้องอ่านข้อจำกัดเหล่านี้',
 '', '## รายหมวด','', '| หมวด | Strict ทั้ง 100 ข้อ | Positive ที่มี source จริงผ่าน | Unknown ตอบอย่างปลอดภัย | Fixture goals |','|---|---:|---:|---:|---:|']
for c in sorted(k for k,l in counts if k!='ALL' and l=='all'):
    v=counts[(c,'all')];lines.append(f"| {c} | {v['strict']}/{v['n']} | {v['nonfixture_positive_passed']}/{v['nonfixture_positive']} | {v['negative_safe_abstention']}/{v['negative']} | {v['fixture_only_goals']} |")
v=counts[('ALL','all')]
lines+=['','## รวม','',f"- HTTP ตอบกลับ {v['http_ok']}/{v['n']}; delivery validation ผ่าน {v['validation_ok']}/{v['n']}",
 f"- Strict รวม {v['strict']}/{v['n']} (รวมข้อ source ไม่ตรงกับ fixture เดิมไว้ใน denominator เพื่อไม่ซ่อน coverage)",
 f"- Positive ที่มี source จริง: strict {v['nonfixture_positive_passed']}/{v['nonfixture_positive']}; source claims ครบ {v['nonfixture_positive_complete_claims']}/{v['nonfixture_positive']}",
 f"- Negative safe abstention {v['negative_safe_abstention']}/{v['negative']} (แยกจากการตอบคำถามได้)",
 f"- Median latency {done['latency_median_sec']:.3f}s; P95 {done['latency_p95_sec']:.3f}s; elapsed {done['elapsed_sec']:.1f}s",'',
 '## Model transport/protocol','', '```json',json.dumps(dict(model),ensure_ascii=False,indent=2),'```','',
 'HTTP transport, model transport, schema และความถูกต้องคำตอบเป็นคนละเกณฑ์ ไม่เอาโมเดลตอบกลับสำเร็จมาแทนการตอบถูก','',
 '## กลุ่มที่ไม่ผ่าน','', '```json',json.dumps({k:v for k,v in counts[('ALL','all')].items() if k in {'required_claims_missing','additional_or_wrong_scope_claims','expected_state_mismatch','value_or_presentation_mismatch','calendar_source_scope_or_applicability_gap','fixture_not_in_native_source','http_or_response_failure','delivery_validation_failure','source_pointer_mismatch'}},ensure_ascii=False,indent=2),'```','',
 'รายละเอียดทุกข้ออยู่ใน ALL_FAILURES.jsonl และ FAILURES_DETAIL_TH.md ต้องตรวจ actual body คู่กับ artifact เพื่อแยกผิดเนื้อหา/ขอบเขตออกจากรูปแบบและ source gap','']
(out/'REPORT_TH.md').write_text('\n'.join(lines),'utf8')
details=['# ข้อไม่ผ่าน strict ทุกข้อ','','ผลอัตโนมัติยังไม่ใช่ semantic adjudication','']
for x in failures:
    details += [f"## {x['question_id']} — {x['grade']['classification']}",'',x['question'],'','```text',x['response'].get('answer',''), '```','','```json',json.dumps(x['grade'],ensure_ascii=False,indent=2),'```','']
(out/'FAILURES_DETAIL_TH.md').write_text('\n'.join(details),'utf8')
print(json.dumps({'summary':dict(counts[('ALL','all')]),'model':dict(model)},ensure_ascii=False))
