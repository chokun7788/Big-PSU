"""Export 20 readable scenario sets, calculate analysis, retain all raw logs."""
import experiment as t
import json,collections,csv
def read(p):return json.loads((t.B/p).read_text(encoding='utf-8'))
def rows(p):return [json.loads(x) for x in (t.B/p).read_text(encoding='utf-8').splitlines() if x.strip()]
def link(label,p):return f'[{label}]({(t.B/p).as_posix()})'
def save(p,s):
    with (t.B/p).open('x',encoding='utf-8') as f:f.write(s+'\n')
def block(v):return '\n```json\n'+json.dumps(v,ensure_ascii=False,indent=2)+'\n```\n'
def exports():
    rec={p.stem:json.loads(p.read_text(encoding='utf-8')) for p in (t.B/'records').glob('*/*.json')}
    assert len(rec)==480
    for i,s in enumerate(t.SCENARIOS,1):
        text=f'# ชุด {i:02} — {s[0]} / {s[1]}\n\n**{t.WARNING}**\n\nเกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์\n\n'
        text+=f'แพลตฟอร์มตัวอย่าง: {s[6]} • จำนวนผู้เล่น {s[7]}–{s[8]} • เวลาเล่น {s[9]} นาที / กินช่องจอง {s[10]} นาที\n\n'
        text+='## ข้อมูลครบ 24 หมวด\n'
        for k in t.ORDER:
            r=rec[t.rid(k,i)];p=t.PROMPTS[k]
            text+=f'\n### {t.CATALOG[k]["owner_form"]} (`{k}`)\n\nรหัส `{r["record_id"]}`\n\nคำถามตัวอย่าง:\n\n- {r["aliases"]["th"][0]} {p[1]}\n- {r["aliases"]["en"][0]} {p[2]}\n- {r["aliases"]["th"][0]} {p[6]}\n\n'
            for key,f in r['fields'].items():text+=f'**{key} — {f["status"]}**'+block(f['value'])
            text+='\n'+link('JSON record',f'records/{k}/{r["record_id"]}.json')+'\n'
        save(f'SET_{i:02}.md',text)
    diversity={}
    for k in t.ORDER:
        rs=[r for r in rec.values() if r['kind']==k]
        diversity[k]={key:len({t.canonical_json({'status':r['fields'][key]['status'],'value':r['fields'][key]['value']}) for r in rs}) for key in rs[0]['fields']}
    t.filejson('FIELD_DIVERSITY.json',diversity)
    print('Exported 20 scenario guides / 480 records',flush=True)
def report():
    m=read('MANIFEST.json');summary=read('content_final/SUMMARY.json');allrows=rows('content_final/ANSWERS_AND_DECISIONS.jsonl');fails=read('content_final/FAILURES.json')
    http=read('HTTP_ROUND2_SUMMARY.json');pipe=read('PIPELINE_SUMMARY.json');conv=read('CONVERSATION_SUMMARY.json');llm=read('LLM_SUMMARY.json');llmrows=rows('LLM_RESULTS.jsonl')
    new=[r for r in allrows if r['rid'].startswith('demo20_')];controls=[r for r in allrows if not r['rid'].startswith('demo20_')]
    oldrows=rows('../r58_examples_240_20261012/content_final/ANSWERS_AND_DECISIONS.jsonl');baseline={(r['rid'],r['lang'],r['style']):r for r in oldrows}
    changes=[]
    for r in controls:
        old=baseline[(r['rid'],r['lang'],r['style'].replace('old_control_',''))]
        if old['passed']!=r['passed'] or old.get('decision',{}).get('query_plan')!=r.get('decision',{}).get('query_plan'):changes.append({'current_id':r['id'],'old_id':old['id'],'old_pass':old['passed'],'new_pass':r['passed'],'question':r['question'],'old_plan':old.get('decision',{}).get('query_plan'),'new_plan':r.get('decision',{}).get('query_plan')})
    t.filejson('OLD_CONTROL_CHANGES.json',changes)
    diagnostics=collections.Counter()
    for r in fails:
        plan=(r.get('decision') or {}).get('query_plan',{})
        if not r.get('decision'):diagnostics['no_common_answer_or_exception']+=1
        elif r['rid'] not in plan.get('record_ids',[]):diagnostics['target_record_not_selected']+=1
        elif not plan.get('requested_fields') and not plan.get('all_fields'):diagnostics['record_found_but_no_fields']+=1
        elif any('missing_field:' in x for x in r['reasons']):diagnostics['record_found_but_requested_fields_incomplete_or_wrong']+=1
        else:diagnostics['content_evidence_or_other']+=1
    newrecords={p.stem:json.loads(p.read_text(encoding='utf-8')) for p in (t.B/'records').glob('*/*.json')}
    pairs=[]
    for r in allrows:
        if r['style']=='name_repeat':
            clean=next(x for x in allrows if x['rid']==r['rid'] and x['lang']==r['lang'] and x['style']=='natural')
            pairs.append({'rid':r['rid'],'lang':r['lang'],'clean_pass':clean['passed'],'repeat_pass':r['passed'],'clean_plan':(clean.get('decision') or {}).get('query_plan'),'repeat_plan':(r.get('decision') or {}).get('query_plan')})
    pairs_summary=collections.Counter(('clean_pass' if r['clean_pass'] else 'clean_fail')+'/'+('repeat_pass' if r['repeat_pass'] else 'repeat_fail') for r in pairs)
    t.filejson('TYPO_CLEAN_PAIRS.json',{'summary':dict(pairs_summary),'pairs':pairs})
    llm_causes=collections.Counter();raw_count=0
    records=t.CommonStore(t.DB).snapshot()['release']['records']
    for r in llmrows:
        for a in r['planner_attempts']:
            for raw in a['raw_responses']:
                raw_count+=1
                try:
                    p=json.loads(raw)
                    kinds={records[x]['kind'] for x in a['record_ids']}
                    if 'game' in kinds:kinds.update(('game_service','game_mode','control_set'))
                    keys={f['key'] for k in kinds for f in t.CATALOG[k]['fields']}
                    plats={t.prior.value(x,'platform') for x in records.values() if t.prior.value(x,'platform')}
                    if not isinstance(p,dict) or set(p)!={'requested_fields','all_fields','platform'}:reason='wrong_object_shape'
                    elif not isinstance(p['requested_fields'],list) or not 1<=len(p['requested_fields'])<=12:reason='invalid_field_count'
                    elif any(f not in keys for f in p['requested_fields']):reason='unsupported_field'
                    elif len(set(p['requested_fields']))!=len(p['requested_fields']):reason='duplicate_fields'
                    elif type(p['all_fields']) is not bool:reason='all_fields_not_boolean'
                    elif p['platform'] is not None and p['platform'] not in plats:reason='unsupported_platform'
                    else:reason='valid_shape_and_scope'
                    llm_causes[reason]+=1
                except (ValueError,TypeError,KeyError):llm_causes['decode_or_type_error']+=1
    lookup={(r['rid'],r['lang'],r['style']):r for r in allrows}
    llm_before=sum(lookup[(r['rid'],r['lang'],r['style'])]['passed'] for r in llmrows)
    analysis={'queries':len(allrows),'new_queries':len(new),'new_pass':sum(r['passed'] for r in new),'new_fail':sum(not r['passed'] for r in new),'old_controls':len(controls),'old_control_changes':changes,'exclusive_failure_diagnostics':dict(diagnostics),'typo_clean_pairs':dict(pairs_summary),'raw_llm_outputs':raw_count,'raw_llm_diagnosis':dict(llm_causes),'llm_same_cases_baseline_pass':llm_before,'llm_current_pass':llm['pass']}
    t.filejson('ANALYSIS.json',analysis)
    report=f'''# ผลทดสอบเพิ่ม 20 ชุดหลากหลาย ก่อนแก้ระบบ

**{t.WARNING}**

วันที่อ้างอิง 2026-10-12 เวลาไทย รอบนี้เพิ่มข้อมูลและทดสอบก่อนแก้ตามคำขอ ไม่เปลี่ยนโค้ด production

## 1. ข้อมูลที่เพิ่ม

20 สถานการณ์ × 24 หมวด = 480 รายการใหม่ สำเนาฐานเดิม 240 รายการมาเก็บในฐาน DEMO ใหม่ รวม active 720 รายการ ฐานเดิมและ log เดิมยังอยู่

ชุดใหม่เป็นเกมและสถานที่สมมุติทั้งหมด เพื่อกำหนด Ground Truth ได้แน่นอน ไม่เพิ่มข้อเท็จจริงจากเกมหรือศูนย์จริงโดยไม่มีหลักฐาน คำแปลเป็น agent_translated

ความต่างที่ตั้งใจทดสอบ: 5 แพลตฟอร์ม, จำนวนขั้นต่ำ/สูงสุด, เล่น 20–240 นาที, เวลาเล่นกับ occupancy ต่างกัน, ราคา 0 และราคาปกติ, 4 หน่วยคิดราคา, 4 คำตัดสินกฎ, ขั้นตอน 2/3 ขั้น, วัน closed/modified_hours/open_override, มี/ไม่มีช่วง maintenance, game offered true/false, เครื่อง in_service/out_of_service/retired, known-empty/known-zero/known-false/unknown/not_applicable

ช่องใหม่ 3,100 ช่อง: known {m['new_field_statuses']['known']}, unknown {m['new_field_statuses']['unknown']}, not_applicable {m['new_field_statuses']['not_applicable']} กรอกผ่าน schema/source/reference/save/approve/publish จริงใน DEMO ไม่ใช้เจ้าของจริงอนุมัติ

## 2. ผลรวม แยกการเก็บข้อมูลจากการตอบ

| ชั้นที่ทดสอบ | ผ่าน | ผิด | ขอบเขต |
|---|---:|---:|---|
| นำเข้ารายการใหม่ | 480 | 0 | ตรวจชนิดข้อมูล source และ reference |
| คำถามหลักทั้งหมด | {summary['overall/all'].get('pass',0)} | {summary['overall/all'].get('fail',0)} | {len(allrows)} เคส รวม control เดิม 96 |
| เฉพาะคำถามข้อมูลใหม่ | {analysis['new_pass']} | {analysis['new_fail']} | {len(new)} เคส |
| HTTP API | {http['pass']} | {http['fail']} | {http['queries']} เคส; HTTP 200 {http['http_200']} ไม่ใช่จำนวนตอบถูก |
| ทางเข้าของ AnswerQualityPipeline | {pipe['pass']} | {pipe['fail']} | {pipe['queries']} เคส; skipped legacy {pipe['legacy_skipped']} |
| บทสนทนา 3 รอบ | {conv['pass']} | {conv['fail']} | 160 บทสนทนา / 480 turns ใช้คำตอบก่อนหน้าจริง |
| โมเดลช่วยเลือกหัวข้อ | {llm['pass']} | {llm['fail']} | 48 เคสที่เน้นหมวดมีปัญหา ใช้ Ollama จริง |

ตารางมีการทวนคำถามบางส่วนซ้ำกัน ห้ามบวกรวมเป็นจำนวนเคสไม่ซ้ำ หรือใช้อัตรานี้แทนความแม่นยำของลูกค้าจริง ชุดก่อนมีคำถามตามชื่อช่องจำนวนมาก ส่วนชุดนี้เน้นสำนวนและหลายหัวข้อ จึงไม่ใช่คะแนนก่อน/หลังแก้ที่เทียบกันตรง ๆ

## 3. ผลตามรูปแบบคำถาม

| รูปแบบ | ผ่าน | ผิด | รวม |
|---|---:|---:|---:|
'''
    for style in ['all_fields','natural','paraphrase','followup','multi_field','name_repeat','old_control_all_fields','old_control_natural']:
        x=summary['style/'+style];p=x.get('pass',0);f=x.get('fail',0);report+=f'| {style} | {p} | {f} | {p+f} |\n'
    report+='\n## 4. ทุกหมวด\n\nผลด้านล่างรวม control เดิมในหมวดละ 4 เคส\n\n| หมวด | ใหม่ | ผ่าน | ผิด |\n|---|---:|---:|---:|\n'
    for k in t.ORDER:
        x=summary['kind/'+k];report+=f'| {t.CATALOG[k]["owner_form"]} (`{k}`) | 20 | {x.get("pass",0)} | {x.get("fail",0)} |\n'
    report+='\n## 5. พลาดตรงขั้นตอนไหน\n\nจัดเป็นกลุ่มไม่ซ้ำตาม plan ก่อน แล้วค่อยอ่าน reasons ที่หนึ่งเคสมีได้หลายป้าย\n'+block(dict(diagnostics))
    report+='''
สาเหตุที่ตรวจได้จากโค้ดเดิม:

1. field_requests ใช้ keyword กลาง: กี่คน→players_min โดยไม่ remap ตาม kind ทำให้ resource/service/zone หรือคำถาม max เลือกผิด
2. สำนวนใหม่หลายแบบไม่ได้เชื่อมกับชื่อช่อง เช่นหลักฐาน ที่นั่ง เวลาเล่น จึงเลือก record ได้แต่ requested_fields ว่าง
3. คำในชื่อหมวด/รายการเข้าไปรบกวน intent เช่นปุ่ม กฎ ราคา มีผลแม้ผู้ใช้ถามอีกหัวข้อ
4. multi-field เลือกบางหัวข้อได้แต่ไม่ครอบคลุมทุกสิ่งที่ถาม; ต่อให้คำตอบมี source ก็ยังขาดหัวข้อที่ขอ
5. ประวัติช่วยเลือก record ได้ แต่ไม่ได้รับประกันว่ารู้ field ของคำถามต่อ; บทสนทนาจริงที่เก็บ assistant history แยกตรวจไว้
6. fuzzy มีข้อจำกัด แต่ต้องเทียบ clean/typo เป็นคู่ ไม่ถือว่าทุกเคส typo ที่ตกเกิดจากสะกดผิด
7. planner เรียกเมื่อไม่มีหัวข้อหรือบางเงื่อนไข steps เท่านั้น จึงไม่ช่วยกรณี keyword เลือก field ผิดที่มีอยู่แล้ว
8. confidence/validation ใน CommonAnswerer.finish ปัจจุบันกำหนดค่า 1.0/True คงที่ จึงไม่ใช่โอกาสที่คำตอบถูกตามคำถาม สามารถเลือกหัวข้อผิดแล้วมีค่าพวกนี้ได้

## 6. พิมพ์ซ้ำกับคำปกติ เปรียบเทียบเป็นคู่
'''+block(dict(pairs_summary))
    report+='\n`clean_fail/repeat_fail` ยังไม่พิสูจน์ว่าการพิมพ์ผิดเป็นต้นเหตุ ต้องอ่านสอง plan; `clean_pass/repeat_fail` จึงเป็นการเสื่อมหลังพิมพ์ซ้ำที่ชัดกว่า\n'
    report+='\n## 7. บทสนทนา 3 รอบ\n\n160 บทสนทนา: ขอทั้งหมด → ถามสั้นโดยไม่บอกชื่อ → เปลี่ยนชื่อรายการและขอทั้งหมด ใส่ข้อความคำตอบของ assistant จริงลง history ทุกครั้ง ตรวจว่า record เดิมไม่รั่วเข้าสู่ turn เปลี่ยนรายการ\n'+block(conv['styles'])
    report+='\n## 8. LLM: แยกเรียกได้ / plan ผ่าน / ตอบผ่าน\n\n'
    report+=f'48 คำถามเดียวกันปิด LLM ผ่าน {llm_before}/48 เปิด LLM ผ่าน {llm["pass"]}/48; planner attempts {llm["planner_attempts"]}, accepted plans {llm["accepted_plans"]}. เป็น CommonAnswerer+planner จริง ไม่ได้เปิด legacy/RAG มาสร้างคำตอบให้เรื่องสมมุติ\n\n'
    report+='ตรวจ raw จากการเรียกครั้งเดียวกันนี้ ไม่ใช้การเรียกใหม่มาอ้างแทนผลเก่า:\n'+block(dict(llm_causes))
    report+='\naccepted plan ไม่เท่ากับตอบถูกเสมอ; accepted count กับ pass count แยกอยู่ใน LLM_SUMMARY โดยเคสที่ keyword ตอบอยู่แล้วอาจไม่เรียก LLM\n'
    report+='\n## 9. ผลเดิมหลังเพิ่มข้อมูล\n\nControl 96 เคส: 24 หมวด × 2 ภาษา × (all-fields/natural) ของรายการเดิม 01 เทียบสถานะผ่านและ query_plan กับ log ชุดเดิม ผลเปลี่ยน '+str(len(changes))+' เคส รายละเอียดใน OLD_CONTROL_CHANGES.json\n'
    report+='\n## 10. ตัวอย่างที่ยังผิดและควรตอบอะไร\n\nเป็นค่าของ fixture เท่านั้น ทุกตัวอย่างเลือกจาก log ที่รันจริง ไม่แต่งคำตอบของระบบเพิ่ม\n'
    for k in t.ORDER:
        rs=[r for r in fails if r['kind']==k and r['rid'].startswith('demo20_')]
        r=next((x for x in rs if x['style'] in {'natural','paraphrase','multi_field'}),rs[0] if rs else None)
        if not r:continue
        report+=f'\n### {k} / เคส {r["id"]}\n\nถาม: {r["question"]}\n\nตอบจริง: {r["answer"]}\n\nเหตุที่ตก: {", ".join(r["reasons"])}\n\nPlan:'+block((r.get('decision') or {}).get('query_plan'))+'\nสิ่งที่ควรนำมาตอบ:'+block({key:newrecords[r['rid']]['fields'][key] for key in r['expected_fields']})
    report+='''
## 11. ข้อจำกัดและผลรอบที่เก็บแยก

- รูปแบบราคา/จำนวนคน/กฎนี้เป็น synthetic ไม่ใช่นโยบายจริง และไม่ใช่การตรวจสถานะ WordPress
- scoring ตรวจ obligation/status/เนื้อหาที่ต้องมี/evidence ไม่ได้ให้มนุษย์ตัดสินความลื่นไหล ความยาว และการแปลทุกคำ
- HTTP ไม่เปิดเผย hits จึงตรวจ obligation/content/unknown wording; pipeline และ CommonAnswerer ตรวจ evidence เพิ่ม
- HTTP รอบแรกตั้ง handler ให้ตรวจ Host ด้วยพอร์ต 0 ขณะที่ server ได้พอร์ตสุ่ม จึงได้ 403 ทั้ง 224 เป็นบั๊กตัวรันทดสอบ แก้เฉพาะ harness แล้วเก็บรอบ 2 ใหม่ ไม่ใช้รอบแรกเป็นข้อสรุปว่า chatbot เชื่อมต่อไม่ได้
- รันหลักรอบแรกเก็บบางเคสแล้วหยุดเฉพาะ parent/worker ของตัวทดสอบ รันต่อจาก log เดิมใน content_final เก็บทั้งสองรอบ
- snapshot reuse และ cache การค้นชื่อใช้เฉพาะ test process กับคำถามเดิม/ชื่อใน release เดิม ผลยังมาจาก named() จริง ตรวจ epoch ทุกคำตอบ ไม่ใช่ cache คำตอบที่รู้จาก oracle และไม่ใช่ benchmark latency ของเว็บ
- ไม่รัน full GT 20,000 เคส ไม่แก้ routing/threshold/alias/นโยบายจริงในรอบนี้

## 12. ลำดับแก้หลังตรวจเพิ่ม

1. เลือก semantic field ตาม kind และความหมาย min/max/seat/session/occupancy/proof ให้ตรง
2. แยกชื่อรายการออกจากคำถามก่อนจับหัวข้อ และรักษาทุกหัวข้อเมื่อถามหลายเรื่อง
3. ใช้ประวัติที่ระบุ record ชัดแล้วช่วยเลือก field; ถ้าไม่แน่ใจถามเฉพาะหัวข้อที่ยังขาด
4. LLM schema ต้องจำกัด enum ของ field/platform; เปิดทางช่วยเมื่อ field ที่จับได้ไม่มีใน kind พร้อม log เหตุผล rejection
5. ตรวจ typo ด้วย clean/typo pairs และการเปลี่ยนเรื่อง ห้ามลด threshold จนเลือกอีกเครื่อง/อีกชุด
6. แยก store validity/source confidence ออกจากความถูกต้องของ intent/answer; ไม่ใช้ static 1.0 เป็นคำรับรองตอบตรง

## 13. หลักฐาน

'''
    for p in ['MANIFEST.json','SCENARIOS.json','FIELD_DIVERSITY.json','QUESTIONS_EXPECTED.json','content_final/SUMMARY.json','content_final/ANSWERS_AND_DECISIONS.jsonl','content_final/FAILURES.json','content_final/EVALUATION_SCOPE.json','ANALYSIS.json','OLD_CONTROL_CHANGES.json','TYPO_CLEAN_PAIRS.json','HTTP_ROUND2_SUMMARY.json','HTTP_ROUND2_RESULTS.jsonl','PIPELINE_SUMMARY.json','PIPELINE_RESULTS.jsonl','CONVERSATION_SUMMARY.json','CONVERSATION_RESULTS.jsonl','LLM_SUMMARY.json','LLM_RESULTS.jsonl','PRESERVATION_RECEIPT.json']:report+='- '+link(p,p)+'\n'
    if (t.B/'SCORING_REVIEW.json').exists():
        audit=read('SCORING_REVIEW.json')
        report+='\n## ตรวจคะแนนผ่านเพิ่มเติม\n\n'+str(audit['content_pass_without_resolved_fields'])+' เคสผ่านเนื้อหาที่ต้องมี แต่ requested_fields ว่างและไม่ได้ขอทั้งหมด เป็นเคสพิมพ์ซ้ำที่ตอบหลายช่องตามค่าเริ่มต้น จึงยังไม่ถือว่าเข้าใจหัวข้อครบ ดู '+link('SCORING_REVIEW.json','SCORING_REVIEW.json')+'\n'
    save('REPORT_TH.md',report)
    intro=f'''# 20 ชุดข้อมูลหลากหลาย — DEMO แยก

**{t.WARNING}**

เพิ่ม 20 ชุดสถานการณ์ที่ต่างกัน ชุดละ 24 หมวด รวม 480 รายการใหม่ รักษาฐานเดิม 240 รายการในโฟลเดอร์เดิม ชุดใหม่นี้ใช้สำเนาฐาน DEMO ที่รวม 720 รายการ ไม่เกี่ยวกับ Product จริง

เกมใหม่ทั้ง 20 เกมเป็นเกมแต่งขึ้นเพื่อกำหนดผลที่ควรตอบได้แน่นอน ราคา นโยบาย สถานที่ บุคคล ตาราง และการจับคู่ API สมมุติทั้งหมด คำแปลยังไม่ผ่านมนุษย์

## ผลล่าสุด

ทดสอบคำถามหลัก {len(allrows)} เคส ผ่าน {summary['overall/all'].get('pass',0)} ผิด {summary['overall/all'].get('fail',0)} รวม control เดิม 96 เคส; ผลละเอียดแยกรูปแบบและสาเหตุอยู่ในรายงาน

HTTP 200 {http['http_200']}/{http['queries']} แต่ตอบผ่าน {http['pass']}/{http['queries']}; บทสนทนา 160 ชุด/480 turns ผ่าน {conv['pass']}; LLM ตัวอย่าง 48 เคสผ่าน {llm['pass']}

{link('รายงานผลและสาเหตุอย่างละเอียด','REPORT_TH.md')}

## เปิดข้อมูลแต่ละชุด

ทุกไฟล์มีทั้ง 24 หมวด พร้อมค่าที่กรอก สถานะ known/unknown/not_applicable, ตัวอย่างคำถามไทย–อังกฤษ และ JSON อ้างอิง

| ชุด | ชื่อ | แพลตฟอร์ม | คน | เล่น / ใช้ช่องจอง | ดูข้อมูล |
|---|---|---|---|---|---|
'''
    for i,s in enumerate(t.SCENARIOS,1):intro+=f'| {i:02} | {s[0]} / {s[1]} | {s[6]} | {s[7]}–{s[8]} | {s[9]} / {s[10]} นาที | {link("เปิดชุด",f"SET_{i:02}.md")} |\n'
    intro+='\n## โครงสร้างไฟล์\n\n- `records/`: JSON ใหม่ 480 รายการ\n- `DEMO_720_ONLY.sqlite`: สำเนา DEMO รวมเก่า+ใหม่\n- `content_final/`: ผลหลักครบ ไม่ใช้ log รอบที่ยังรันไม่ครบเป็นผลสรุป\n- `experiment.py`: สร้างและรันทดสอบครั้งแรก\n- `resume_content.py`: รันต่อจาก log ที่เก็บไว้\n- `integration.py`: HTTP handler จริงและทางเข้า pipeline\n- `extra_checks.py`: LLM จริงและบทสนทนา 3 รอบ\n\nสคริปต์ปฏิเสธการเขียนทับผลเดิม ถ้าจะรันใหม่ให้สร้างโฟลเดอร์ผลใหม่ก่อน; ใช้ Python ที่มีใน r58 เดิม ไม่มีการติดตั้งเพิ่ม ผลทดสอบนี้ยังไม่ยืนยันว่าคำถามทุกสำนวนตอบได้ และไม่ได้เปิดข้อมูลตัวอย่างบนเว็บ Product จริง\n'
    if (t.B/'SCORING_REVIEW.json').exists():intro+='\nคะแนนผ่านหมายถึงเนื้อหาที่ต้องมี/status/evidence; audit พบเคสพิมพ์ซ้ำที่ยังไม่เลือกหัวข้อ แต่คำตอบตามค่าเริ่มต้นมีค่าที่ขออยู่ด้วย ดู SCORING_REVIEW.json ไม่ใช้คะแนนผ่านเป็นการรับรองความเข้าใจทุกเคส\n'
    save('README_TH.md',intro)
    print(json.dumps({'report_chars':len(report),'main_queries':len(allrows),'diagnostics':dict(diagnostics),'old_control_changes':len(changes)},ensure_ascii=False),flush=True)
if __name__=='__main__':
    if t.sys.argv[1]=='export':exports()
    elif t.sys.argv[1]=='report':report()
