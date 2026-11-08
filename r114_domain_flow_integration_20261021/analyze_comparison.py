"""Read saved outputs only. Preserve the original strict judge and every failure."""
import collections,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r113_multi_flow_benchmark_20261021'
NAMES={'C01':'ที่ตั้ง/ติดต่อ','C02':'บุคลากร','C03':'อุปกรณ์','C04':'เกม/รายการเกม','C05':'ปุ่มเกม','C06':'ราคาปกติ','C07':'เหมาจ่าย',
 'C08':'การจอง','C09':'ชำระเงิน','C10':'กฎใช้บริการ','C11':'ปฏิทิน','C12':'สถานะสดจำลอง','C13':'กติกาแข่ง','C14':'ข่าวจำลอง'}
FIELDS=['missing_claims','unrequested_claims','wrong_values','evidence_mismatches']

def content_ok(g):return not any(g[k] for k in FIELDS)
def main():
    run=R/'verification'/sys.argv[1];done=json.loads((run/'TEST_COMPLETE.json').read_text('utf8'));assert done['complete']
    out=run/'analysis';out.mkdir(exist_ok=False)
    jobs={x['id']:x for p in [B/'EFFECTIVE_QUESTIONS_1400.jsonl',R/'RESERVED_QUESTIONS_140.jsonl'] for x in map(json.loads,p.read_text('utf8').splitlines())}
    winners=json.loads((B/'WINNER_CANDIDATE_CONFIG.json').read_text('utf8'))['category_to_flow']
    baseline={x['question_id']:x for x in map(json.loads,(B/'main_natural/RESULTS.jsonl').read_text('utf8').splitlines()) if x['flow_id']==winners[x['category']]}
    groups=collections.defaultdict(collections.Counter);fails=[];model=collections.Counter();seen=set();md=[]
    with (out/'ALL_FAILURES.jsonl').open('x',encoding='utf8') as f:
        for line in (run/'RESULTS.jsonl').open(encoding='utf8'):
            x=json.loads(line);j=jobs[x['question_id']];g=x['grade'];pair=(x['arm'],x['question_id']);assert pair not in seen;seen.add(pair)
            positive=bool(j['expected']['claims'])
            for key in [(x['arm'],x['category'],'all'),(x['arm'],'ALL',x['locale']),(x['arm'],'ALL','all')]:
                c=groups[key];c['n']+=1;c['strict']+=g['passed'];c['content_exact']+=content_ok(g);c['positive_n']+=positive
                c['positive_content_exact']+=positive and content_ok(g);c['state_only_fail']+=not g['passed'] and content_ok(g)
                c['routing_exact']+=all(n['category']==x['category'] for n in x['result']['needs'])
                c['positive_routing_n']+=positive;c['positive_routing_exact']+=positive and all(n['category']==x['category'] for n in x['result']['needs'])
                c['empty_correct_abstention']+=not positive and content_ok(g)
                if x['arm']!='reserved_automatic':
                    bg=baseline[x['question_id']]['grade'];c['baseline_n']+=1;c['baseline_strict']+=bg['passed'];c['baseline_content_exact']+=content_ok(bg)
                    c['improved']+=not bg['passed'] and g['passed'];c['regressed']+=bg['passed'] and not g['passed']
                for k in FIELDS:c[k]+=bool(g[k])
            if not g['passed']:
                row={**x,'expected':j['expected'],'classification':'expected_state_only' if content_ok(g) else 'source_contract_mismatch_requires_review',
                     'actual_semantic_content_failure_confirmed':False}
                f.write(json.dumps(row,ensure_ascii=False)+'\n');fails.append(row)
        for line in (run/'MODEL_EVENTS.jsonl').open(encoding='utf8'):
            e=json.loads(line);model['calls']+=1;model['http_attempted']+=e.get('http_attempted',False);model['transport_ok']+=e['transport_ok'];model['schema_ok']+=e['schema_ok']
            model['valid_items']+=e.get('valid_items',0);model['invalid_items']+=e.get('invalid_items',0)
    assert len(seen)==2940
    summary={'executions':len(seen),'source_and_code_unchanged':done['source_and_code_unchanged'],'model_identity_verified':done['model_identity_verified'],
      'groups':[{'arm':a,'category':c,'locale':l,**dict(v)} for (a,c,l),v in groups.items()],'model':dict(model),
      'failure_rows':len(fails),'semantic_accuracy_established':False,'baseline_rerun':False,'reserved_set_is_now_development_validation':True}
    (out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
    lines=['# ผลเปรียบเทียบ R114 กับ saved R113',
      '',f"รอบ `{run.name}`: ครบ **2,940 executions** = คำถามเดิม 1,400 ข้อ × 2 วิธี routing + คำถามเพิ่มเติม 140 ข้อ; เวลา {done['elapsed_sec']:.1f} วินาที เปิด LLM แบบมีเงื่อนไข ไม่รัน baseline ใหม่",'',
      '**เกณฑ์:** strict ตรวจ source claim identity/value/evidence/ขอบเขตและสถานะตรงทั้งหมด; content exact ใช้ส่วนตรวจเดิมแต่แยกสถานะออก ทั้งสองค่าไม่ใช่ human semantic accuracy และไม่ใช่คะแนน Full Test 20,554 requests',
      '', '## รายหมวด — 100 คำถามเดิมต่อหมวด', '',
      '| หมวด | R113 winner strict | R114 ระบุหมวด | R114 เลือกหมวดเอง | เลือกหมวดเอง content exact |',
      '|---|---:|---:|---:|---:|']
    for c,n in NAMES.items():
        h=groups[('same_source_hinted',c,'all')];a=groups[('automatic_routing',c,'all')]
        lines.append(f"| {c} {n} | {h['baseline_strict']}/{h['n']} | {h['strict']}/{h['n']} | {a['strict']}/{a['n']} | {a['content_exact']}/{a['n']} |")
    lines+=['','## รวมและแยก locale ที่ผู้ใช้ส่งมา','','| วิธี | locale | strict | content exact | positive content exact | ดีขึ้น/ถอยลงจาก R113 |','|---|---|---:|---:|---:|---:|']
    for arm in ['same_source_hinted','automatic_routing','reserved_automatic']:
        for loc in ['all','th','en','auto']:
            c=groups.get((arm,'ALL',loc))
            if not c:continue
            lines.append(f"| {arm} | {loc} | {c['strict']}/{c['n']} ({100*c['strict']/c['n']:.2f}%) | {c['content_exact']}/{c['n']} | {c['positive_content_exact']}/{c['positive_n']} | {c['improved']}/{c['regressed']} |")
    lines+=['','## ต้องอ่านคะแนนอย่างไร','',
      '- R113 baseline ให้หมวดอยู่แล้ว จึงเทียบ hinted เพื่อแยกตัวอ่าน; automatic เป็นการเพิ่มความยากเรื่อง router ไม่ใช่ baseline router เดิม',
      '- ใช้ source read model เดียวกัน ผลไม่รวมประโยชน์จากข้อมูล draft ที่ย้ายเพิ่มใน R114 การทำงานกับ native schema/HTTP ตรวจแยกใน acceptance gates',
      '- ชุดเพิ่มเติมถูกตรึงก่อนรอบแรก แต่หลังตรวจผลแล้วถือเป็น development validation ไม่ใช่ blind holdout หรือชุดผู้ใช้จริง',
      '- C12 เป็น provider fixtures และ C14 เป็น synthetic news; ผลไม่ยืนยันว่าระบบจริงมีเครื่องว่างหรือข่าวนั้นจริง',
      '- กรณี C12 มีทั้งข้อมูลพร้อมกับ stale/unavailable ในคำถามเดียวกัน: การส่ง partial อาจถูกต้องกว่า expected answer ของ oracle เดิม เก็บ strict fail ไว้ ไม่แก้ expected เพื่อยกคะแนน',
      '- กติกาที่ถามทั้งหัวข้อแต่ expected สุ่มไว้เพียงย่อหน้าเดียว อาจมี unrequested_claims จากการคืนหลายย่อหน้าหัวข้อเดียวกัน ต้องดู source และขอบเขตภาษาก่อนสรุปเป็นตอบผิด',
      '- ข้อที่ขาด claim/มี claim เพิ่มยังต้องแยก missing information, selection error, scope error และ oracle granularity ไม่ถือทุก fail เป็นความผิดเนื้อหาที่พิสูจน์แล้ว',
      '- ภาษาอังกฤษบางข้อใช้ข้อความกติกาต้นฉบับภาษาไทยและมี flag translation missing คะแนน source contract ไม่ตรวจความลื่นไหลของคำแปล',
      '', '## Model transport / protocol','',f'```json\n{json.dumps(dict(model),ensure_ascii=False,indent=2)}\n```',
      '', 'transport/schema ผ่านยังไม่ยืนยันว่าเลือก evidence ถูก ข้อผิดพลาดคำตอบดู raw claim และ expected แยกกัน',
      '', '## ข้อที่ไม่ผ่านทุกข้อ','', 'รายละเอียด raw แบบเครื่องอ่านได้อยู่ใน [ALL_FAILURES.jsonl](ALL_FAILURES.jsonl) และ [FAILURES_DETAIL_TH.md](FAILURES_DETAIL_TH.md) เก็บต้นฉบับทุกข้อ รวมทั้งสถานะ mismatch']
    (out/'COMPARISON_REPORT_TH.md').write_text('\n'.join(lines)+'\n','utf8')
    details=['# ข้อที่ไม่ผ่าน strict ทุกข้อ','','การจัดกลุ่มอัตโนมัติด้านล่างยังไม่ใช่การตัดสิน semantic โดยมนุษย์','']
    for x in fails:
        g=x['grade'];details += [f"## {x['arm']} / {x['question_id']} / {x['category']}",'', '**คำถาม:** '+x['question'],'', '**คำตอบ:**','', '```text',x['result']['answer'],'```','',
          '**สถานะ:** '+g['expected_status']+' → '+g['actual_status'], '', '**การเลือก:** '+', '.join(n['reason'] for n in x['result']['needs']),'',
          '```json',json.dumps({k:g[k] for k in FIELDS},ensure_ascii=False,indent=2),'```','',
          '**Expected source refs และ actual claims:**','', '```json',json.dumps({'expected':x['expected']['claims'],'actual':x['result']['claims']},ensure_ascii=False,indent=2),'```','']
    (out/'FAILURES_DETAIL_TH.md').write_text('\n'.join(details)+'\n','utf8')
    print(json.dumps({'groups':summary['groups'][-4:],'model':dict(model),'failure_rows':len(fails)},ensure_ascii=False))

if __name__=='__main__':main()
