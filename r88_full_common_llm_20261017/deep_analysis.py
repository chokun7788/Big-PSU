"""Analyze retained answers, plans and sources; never rerun or edit a response."""
import argparse,collections,gzip,json,re,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'));sys.path.insert(0,str(R))
from analyze import rows,bucket,literal
def walk(v):
 if isinstance(v,dict):
  yield v
  for child in v.values():yield from walk(child)
 elif isinstance(v,list):
  for child in v:yield from walk(child)
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--partial',action='store_true');parser.add_argument('--tag',default='FINAL');args=parser.parse_args()
 summary=json.loads((R/('ANALYSIS_'+args.tag+'.json')).read_text('utf8'));assert args.partial or summary['complete']
 jobs={j['key']:j for j in (json.loads(s) for s in (R/'SELECTED_JOBS.jsonl').read_text('utf8').splitlines())}
 suffix='' if not args.partial else '_'+args.tag;db=R/('FAILURE_EVIDENCE'+suffix+'.sqlite');assert not db.exists()
 conn=sqlite3.connect(db);conn.executescript('CREATE TABLE request_failures(key TEXT PRIMARY KEY,locale TEXT,domain TEXT,mode TEXT,diagnostic TEXT,question TEXT,answer TEXT,result_file TEXT,result_line INTEGER,failed_grade_count INTEGER,details_json TEXT); CREATE TABLE grade_failures(key TEXT,file TEXT,row_number INTEGER,variant TEXT,case_id TEXT,partitions_json TEXT,failures_json TEXT,expected_case_json TEXT); CREATE INDEX failed_domain ON request_failures(domain,diagnostic);')
 categories=collections.Counter();parts=collections.Counter();examples=collections.defaultdict(list);by_language=collections.defaultdict(collections.Counter);pipeline_methods=collections.Counter();primary_known=collections.Counter();seen=set();counts=collections.Counter()
 for file,line,row in rows(R/'full01'):
  key=row['key']
  if key in seen:continue
  seen.add(key);job=jobs[key];result=row.get('result') or {};art=result.get('decision_artifact') or {};plan=art.get('query_plan') or {};answer=result.get('answer','');mode=result.get('mode','execution_exception');language=row.get('effective_locale',row['requested_locale']);domain=job['r70_stratum']['domain']
  pipeline_methods[plan.get('method','no_common_method')]+=1
  grades=row.get('grades',[]);failed=[g for g in grades if not g['passed']];expected_map={(e['file'],e['row'],e['variant']):e for e in job['entries']}
  if not failed:continue
  counts['requests_with_any_raw_failure']+=1
  grade_categories={bucket(str(err)) for g in failed for err in g.get('failures',[])};parts.update(grade_categories)
  audits=list(walk(art));model_calls=row.get('observed_model_http_calls',[]);transport_failed=any(not c.get('transport_ok') for c in model_calls)
  gate=any(a.get('reason') in {'model_busy','circuit breaker cooldown active','call budget exhausted'} or a.get('error_stage')=='admission' for a in audits)
  text_issues=[];positive_checked=False
  for entry in job['entries']:
   ok,errs,positive=literal(entry['case'],answer);positive_checked|=positive
   if errs:text_issues.extend(errs)
  if row.get('exception'):diagnostic='execution_or_watchdog'
  elif transport_failed:diagnostic='model_transport_failure'
  elif gate:diagnostic='model_admission_or_budget'
  elif 'live_booking_status_unavailable' in mode or ('unavailable' in mode and any('fixture_offline' in str(a) for a in audits)):diagnostic='controlled_booking_unavailable'
  elif grade_categories=={'protocol'} and not text_issues:diagnostic='protocol_only_no_literal_failure'
  elif 'not_current' in mode or any(a.get('field')=='validity' and a.get('status')=='not_current' for a in audits):diagnostic='source_validity_guard_vs_historical_oracle'
  elif 'studio_scope' in mode or 'migrated_scope' in mode:diagnostic='product_scope_guard_vs_historical_oracle'
  elif plan.get('unconfirmed_topic'):diagnostic='specific_unconfirmed_policy_vs_expected_answer'
  elif plan.get('profile_confirmation') or 'clarification' in mode:diagnostic='clarification_or_topic_confirmation'
  elif 'retry' in mode:diagnostic='retry_or_data_model_guard'
  elif grade_categories <= {'protocol','evidence_identifier','outcome'} and not text_issues:diagnostic='protocol_outcome_or_lineage_needs_review'
  elif text_issues and (plan.get('operation')=='rules' or plan.get('rule_selection')):diagnostic='competition_clause_scope_or_wording'
  elif text_issues and plan.get('operation')=='controls':diagnostic='control_projection_or_wording'
  elif text_issues and plan.get('operation') in {'price','rental'}:diagnostic='price_scope_validity_or_wording'
  elif text_issues:diagnostic='source_selection_field_coverage_or_wording'
  else:diagnostic='native_grader_failure_needs_content_review'
  categories[diagnostic]+=1;by_language[language][diagnostic]+=1
  if positive_checked:counts['failed_requests_with_positive_contract']+=1
  if text_issues:counts['failed_requests_with_literal_mismatch']+=1
  details={'diagnostic_is_hypothesis':diagnostic not in {'execution_or_watchdog','model_transport_failure','controlled_booking_unavailable'},'grading_categories':sorted(grade_categories),'literal_failures':list(dict.fromkeys(text_issues)),'positive_contract_present':positive_checked,'decision_artifact':art,'source_hits':result.get('hits',[]),'model_http_calls':model_calls,'input_quality':row.get('input_quality'),'exception':row.get('exception'),'result_validation':result.get('validation'),'route':result.get('route')}
  conn.execute('INSERT INTO request_failures VALUES(?,?,?,?,?,?,?,?,?,?,?)',(key,language,domain,mode,diagnostic,row['question'],answer,file,line,len(failed),json.dumps(details,ensure_ascii=False)))
  for grade in failed:
   entry=expected_map.get((grade['file'],grade['row'],grade['variant']),{})
   conn.execute('INSERT INTO grade_failures VALUES(?,?,?,?,?,?,?,?)',(key,grade['file'],grade['row'],grade['variant'],str(grade.get('id')),json.dumps(grade.get('partitions',{}),ensure_ascii=False),json.dumps(grade.get('failures',[]),ensure_ascii=False),json.dumps(entry.get('case',{}),ensure_ascii=False)))
  if len(examples[diagnostic])<5:examples[diagnostic].append({'key':key,'question':row['question'],'locale':language,'domain':domain,'mode':mode,'answer':answer,'method':plan.get('method'),'selected_ids':plan.get('record_ids',[]),'requested_fields':plan.get('requested_fields',[]),'failed_grades':[{**g,'expected_contract':expected_map.get((g['file'],g['row'],g['variant']),{}).get('case',{})} for g in failed[:2]],'details':details})
  if counts['requests_with_any_raw_failure']%500==0:conn.commit()
 conn.commit();conn.close()
 explanations={
 'execution_or_watchdog':('P0','พบ exception/watchdog จริง ต้องดู traceback และช่วง deadline ก่อนตีความคำตอบ แก้ตัวรัน/เส้นทางที่ล้ม ไม่แก้ owner facts'),
 'model_transport_failure':('P0','มี HTTP ไปโมเดลแล้วเชื่อมไม่สำเร็จจริง แยก permission/refused/timeout ตาม model_http_calls ไม่อ้างว่า source ไม่ครบเพียงเพราะโมเดลล่ม'),
 'model_admission_or_budget':('P1','พบเหตุ queue/circuit/deadline ของตัวเรียกโมเดล เป็นข้อจำกัด availability/budget ที่สัมพันธ์กับคำตอบ ต้องตรวจทั้ง waiting และ schema/binding ไม่เพิ่ม alias เพื่อกลบ'),
 'controlled_booking_unavailable':('เงื่อนไขทดสอบ','ตัวทดสอบตั้ง Booking เป็น unavailable เพื่อกันสถานะสดเปลี่ยน ไม่ใช่หลักฐานว่า WordPress จริงล่ม และไม่ใช่การยืนยันว่าง/ถูกจอง'),
 'protocol_only_no_literal_failure':('Compatibility','ไม่ผ่านเฉพาะ route/intent/mode เดิม โดยไม่มี literal mismatch ที่พบ ไม่สรุปว่าเนื้อหาถูกครบถ้าไม่มี positive contract'),
 'source_validity_guard_vs_historical_oracle':('ตรวจ oracle/source date','ระบบพบราคา/ข้อมูลไม่อยู่ในช่วงมีผล ต้องเทียบ validity ใน source กับ reference date ของโจทย์ เกณฑ์เก่าที่ต้องการตัวเลขอาจขัดกับการป้องกันข้อมูลหมดอายุ ไม่ต่ออายุหรือเดาราคาศูนย์เอง'),
 'product_scope_guard_vs_historical_oracle':('ขอบเขตผลิตภัณฑ์','คำตอบถูกจำกัดเรื่องร้านเกม/ศูนย์ตามขอบเขตผู้ใช้ บาง oracle เก่าคาดข้อความนอกขอบเขต ต้องตรวจความเหมาะสมของโจทย์ ไม่ขยายบอตให้ตอบทุกเรื่องเพื่อผ่านคะแนน'),
 'specific_unconfirmed_policy_vs_expected_answer':('ต้องตรวจ facts','คำถามเฉพาะมีหัวข้อที่ระบบยังไม่ยืนยัน ข้อมูลวิธีแก้สลิปไม่ใช่หลักฐานวิธีแก้ตัวตนหรือยอดเงิน ไม่ควรเอานโยบายใกล้เคียงมาตอบแทน'),
 'clarification_or_topic_confirmation':('P1','ระบบเลือกขอความชัดเจน/ยืนยันหัวข้อแทนตอบทันที แยกการถามเพิ่มที่จำเป็นออกจาก false clarification โดยดู candidate scope, rejected_candidate, review clauses และ common_read_state'),
 'retry_or_data_model_guard':('P1','คำตอบถูกพักด้วย retry/data/model guard ต้องอ่าน reason ไม่ถือ flag LLM ON ว่า inference สำเร็จทุกข้อ'),
 'protocol_outcome_or_lineage_needs_review':('Compatibility/ต้องตรวจเนื้อหา','route/outcome หรือรหัส evidence เปลี่ยน ต้องตาม source_id/locator/record lineage ก่อนสรุปว่าอ้างผิดเกม การไม่มี literal mismatch ไม่ใช่ความถูกต้องที่มนุษย์รับรอง'),
 'competition_clause_scope_or_wording':('P1','มี literal/source clause ที่คาดแต่ไม่ปรากฏ อาจเป็นการเลือกเล่ม/facet/proposition, ตัดเงื่อนไขไม่ครบ หรือถ้อยคำแปลต่าง ต้องดู selected_ids/requested_fields/obligations และ expected clauses คู่กัน'),
 'control_projection_or_wording':('P1','ตรวจ action→binding/control set ว่าเลือกโหมดและปุ่มครบหรือไม่ แยก mapping ที่หายจากการแปล/รูปแบบถ้อยคำที่ทำให้ literal checker ไม่ตรง'),
 'price_scope_validity_or_wording':('P1','ตรวจ service/resource/zone/audience/period และ source revision อย่าคิดรายชั่วโมงหรือแพ็กเกจเองเพื่อให้ได้ตัวเลขใน oracle'),
 'source_selection_field_coverage_or_wording':('P1','มีเนื้อหาที่ oracle กำหนดแต่ไม่พบ ต้องดูว่าตัวเลือกไปผิด record, เลือก field ไม่ครบ, แผนทิ้ง proposition หรือเป็นคำพ้อง/การแปลที่ checker ไม่รับ ไม่อ้างเป็น root cause ที่ยืนยันแล้วทั้งหมด'),
 'native_grader_failure_needs_content_review':('ต้องทบทวน','native grader ไม่ผ่านแต่ literal เพิ่มเติมไม่มีหลักฐานพอ ต้องอ่าน expected case และ grader_detail ก่อนจัดว่าเป็นความผิดของเนื้อหา')}
 result={'complete':summary['complete'],'requests_seen':len(seen),'failure_request_counts':dict(categories),'grading_partitions_request_counts':dict(parts),'by_language':dict(by_language),'methods':dict(pipeline_methods),'counters':dict(counts),'diagnostics_are_rule_based_hypotheses':True,'not_human_semantic_certification':True,'all_failures_database':str(db),'examples':examples}
 with (R/('DEEP_ANALYSIS'+suffix+'.json')).open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
 title='# วิเคราะห์ข้อผิดพลาด R88 — Format กลาง / LLM ON'+(' (ผลบางส่วน)' if args.partial else '')
 out=[title,'','## การอ่านผล','',f"อ่านผลที่มีแล้ว {len(seen):,} unique requests ไม่รันคำถามซ้ำ ไม่แก้คำตอบหรือ oracle สถานะครบ: {summary['complete']}",'','การจัดกลุ่มนี้เป็นการวินิจฉัยอัตโนมัติจาก trace/plan/expected contract เพื่อจัดคิวตรวจ ไม่ใช่หลักฐานว่ารู้ root cause ทุกข้อหรือรับรองความหมายโดยมนุษย์ Request หนึ่งอาจมีหลายเกณฑ์และหลายปัญหา ตารางกลุ่มหลักเลือกเหตุที่ควรตรวจแรก แต่ฐานหลักฐานเก็บความไม่ผ่านทุกเกณฑ์ไว้ครบ','', '## ลำดับตรวจและสาเหตุที่เป็นไปได้','', '| ระดับ | กลุ่ม | Requests | วิเคราะห์และแนวทาง |','|---|---|---:|---|']
 for category,count in categories.most_common():
  priority,explanation=explanations[category];out.append('| '+priority+' | '+category+' | '+str(count)+' | '+explanation+' |')
 out+=['','## เหตุใดเปิด LLM แล้วยังอาจตอบผิด','', '- ON เปิดความสามารถตาม routing ไม่ได้บังคับทุกคำถามให้ใช้ LLM หรือข้าม evidence/validity checks','- HTTP สำเร็จ หมายถึงขนส่งสำเร็จ; schema ผ่าน หมายถึงรูปแบบแผนผ่าน; binding ผ่าน หมายถึงผูก schema ได้ สิ่งเหล่านี้ไม่ใช่คำรับรองว่าตีความเจตนาหรือเลือก source ถูก','- deterministic bridge ก็มี coverage limit; โมเดลอาจได้รับ candidates ที่ยังไม่ครอบคลุม หรือแผนที่อ่านได้เพียงบาง field จึงยังต้องวัดเนื้อหาที่ตอบจริง','- raw score รวมชื่อ route/รหัสเดิมและเงื่อนไขเก่า จึงรายงาน raw/literal/source/outcome/model transport แยกกัน ไม่ตัดเกณฑ์ทิ้งเพื่อให้คะแนนดี','', '## ตัวอย่างคำถาม คำตอบจริง สิ่งที่คาด และเหตุที่เลือก','']
 for category,samples in examples.items():
  out+=['### '+category,'',explanations[category][1],'']
  for example in samples[:3]:
   out+=['#### '+example['question'],'',f"ภาษา: {example['locale']} / หมวด: {example['domain']} / key: `{example['key']}`",'', '**คำตอบที่ผู้ใช้จะได้**','',example['answer'] or '(ว่าง/exception)','', '**แผนที่เลือกจริง**','', '```json',json.dumps({'mode':example['mode'],'method':example['method'],'selected_ids':example['selected_ids'],'requested_fields':example['requested_fields'],'literal_failures':example['details']['literal_failures']},ensure_ascii=False,indent=2),'```','', '**สิ่งที่โจทย์คาดและข้อที่ไม่ผ่าน**','']
   for grade in example['failed_grades']:
    case=grade['expected_contract'];expected={k:case[k] for k in ['id','question','question_en','expected_category','expected_route_categories','expected_intent','expected_answer_status','expected_game_id','answer_contract','must_contain','must_contain_any','must_not_contain','required_clauses','clauses'] if k in case}
    out+=['```json',json.dumps({'corpus':grade['file'],'failures':grade['failures'],'expected':expected},ensure_ascii=False,indent=2),'```','']
   out+=['คำตอบที่เหมาะสมต้องยืนยันตาม source ปัจจุบันและครอบคลุม proposition ที่ถาม เกณฑ์ที่แสดงคือสิ่งที่ oracle คาด ไม่ใช่นโยบายใหม่ที่อนุมัติให้ศูนย์ ตรวจ facts/วันที่/การแปลก่อนใช้ข้อความคาดเป็นคำตอบจริง','']
 if (R/'SESSION_GUARD_SUMMARY.json').exists():
  sessions=json.loads((R/'SESSION_GUARD_SUMMARY.json').read_text('utf8'));out+=['## การถามต่อและ input guard','',f"Session {sessions['sessions']} ชุด / {sessions['turns']} เทิร์น ผ่าน literal {sessions['literal_turns_passed']} เทิร์น มี trusted common_read_state; ผล engine ไม่ใช่การวัด persistence ผ่าน browser",'',f"Guard diagnostics {sessions['guard_cases']} เคส; layout {sessions['layout_correct']}, repeated detection {sessions['repeat_correct']}, historical block policy {sessions['legacy_block_policy_correct']} — ปัจจุบันใช้ warn_and_continue จึงไม่ถือ expected block แบบเก่าเป็นเกณฑ์คำตอบ",'']
 out+=['## หลักฐานทั้งหมด','', '- REPORT_FINAL_TH.md และ ANALYSIS_FINAL.json: coverage/ภาษา/หมวด/transport แยกกัน','- FAILURE_EVIDENCE'+suffix+'.sqlite: request_failures และ grade_failures ของทุกแถวที่ไม่ผ่าน พร้อมคำตอบ expected case แผน sources และ model diagnostics','- full01/RESULTS_*.jsonl.gz: ผลจริงทั้งข้อผ่านและไม่ผ่าน พร้อม trace และค่าการตรวจ','- DEEP_ANALYSIS'+suffix+'.json: กลุ่มเหตุและตัวอย่าง; diagnostics ยังต้องตรวจ source สำหรับข้อสรุปเชิงความหมาย','- CONFIG.json / RUN_SCOPE_R88_TH.md: ขอบเขตที่ตรึงและ source hashes','','ไม่ได้แก้ production data หรือเพิ่มนโยบายจากการอนุมาน ชุดนี้ไม่ใช่ load benchmark หรือ owner approval']
 report=R/('DEEP_FAILURE_ANALYSIS_TH'+suffix+'.md')
 with report.open('x',encoding='utf8') as f:f.write('\n'.join(out)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in {'examples','methods','by_language'}},ensure_ascii=False))
if __name__=='__main__':main()
