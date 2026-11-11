"""Summarize saved audit rows, compare identical keys, and assemble Thai report."""
import collections,datetime,hashlib,html,json,re,sqlite3,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;P=R/'.local-private'
load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
summary=load(R/'SUMMARY.json');runs=summary['runs'];rows=[json.loads(x) for x in (P/'QUESTION_AUDIT.jsonl').open(encoding='utf8')]
byrun={name:{x['key']:x for x in rows if x['run']==name} for name in runs}
current=ROOT/'r135_shared_contract_20261111';manifest=load(current/'ROUND02_MANIFEST.json')
focus=[];result_index=[]
for folder,entry in manifest['evidence'].items():
 p=current/folder/'RESULT.json';z=load(p);result_index.append({'folder':folder,'phase':entry['phase'],'result':z,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 if entry['phase']!='final' or not (folder.startswith('robustness_round02_final_') or folder.startswith(('round02_http_','shared_http_','typo_http_'))):continue
 for n,item in enumerate(load(current/folder/'DETAILS.json')):
  response=item.get('response') or {};q=item.get('q') or item.get('question');answer=response.get('answer',item.get('answer',''))
  focus.append({'run':'round02_focused_HTTP' if response else 'round02_focused_source_only','key':folder+':'+str(n),'question':q,'answer':answer,'locale':None,'mode':response.get('mode','focused_source_only'),'seconds':item.get('wall_seconds'),'review_flags':['focused_development_case_not_accuracy'],'public_source_urls':[],'reason_codes':[],'evidence_folder':folder})
(P/'FOCUSED_CASES.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in focus),encoding='utf8')
(R/'FOCUSED_RESULT_INDEX.json').write_text(json.dumps(result_index,ensure_ascii=False,indent=2),encoding='utf8')
viewer=P/'RESULTS_ANALYSIS_VIEW.html';text=viewer.read_text(encoding='utf8');a=text.index('const data=')+len('const data=');b=text.index(';let page=0;',a)
viewer.write_text(text[:a]+json.dumps(rows+focus,ensure_ascii=False).replace('</',r'<\/')+text[b:],encoding='utf8')
def timing(sub):
 ts=[x['seconds'] for x in sub];return {'requests':len(sub),'sum_seconds':sum(ts),'median_seconds':statistics.median(ts),'max_seconds':max(ts),'over60':sum(t>60 for t in ts),'unavailable':sum(x['mode']=='pipeline:common_unavailable' for x in sub),'partial':sum('partial_answer' in x['mode'] for x in sub)}
paired={}
keys=set(byrun['verified_200'])
for name in ['hybrid_10pct','bounded_200','verified_200']:
 common=keys&byrun[name].keys();paired[name]=timing([byrun[name][key] for key in common]);paired[name]['missing_selected200_keys']=len(keys-common)
transitions=collections.Counter();new_unavailable=[];recovered_unavailable=[]
for key in sorted(keys):
 old=byrun['hybrid_10pct'][key];new=byrun['verified_200'][key];transitions[(old['mode'],new['mode'])]+=1
 if old['mode']!='pipeline:common_unavailable' and new['mode']=='pipeline:common_unavailable':new_unavailable.append({'key':key,'question':new['question'],'old_mode':old['mode'],'old_answer':old['answer'],'new_answer':new['answer'],'old_seconds':old['seconds'],'new_seconds':new['seconds'],'new_model_calls':new.get('model_calls',[])})
 if old['mode']=='pipeline:common_unavailable' and new['mode']!='pipeline:common_unavailable':recovered_unavailable.append({'key':key,'question':new['question'],'new_mode':new['mode']})
eventstats={}
for name in ['hybrid_10pct','bounded_200','verified_200']:
 rr=list(byrun[name].values());stats={}
 for subsetname,sub in [('all',rr),('unavailable',[x for x in rr if x['mode']=='pipeline:common_unavailable'])]:
  counts=collections.Counter()
  for x in sub:
   events=x.get('model_calls',[]);audits=x.get('model_audits',[])
   if any(e.get('stage')=='model_admission_denied' for e in events):counts['admission_denied_event_requests']+=1
   if 'explicit_timeout_recorded' in x.get('model_event_flags',[]):counts['explicit_timeout_requests']+=1
   if any(e.get('transport_ok') is True for e in events):counts['gateway_transport_success_requests']+=1
   if any(e.get('transport_ok') is False for e in events):counts['gateway_transport_failure_requests']+=1
   counters=x.get('model_counters',{})
   if counters.get('model_calls_attempted')==0:counts['zero_model_calls_attempted_counter']+=1
   if x.get('claim_packets_count',0)>0:counts['top_level_claim_packets_present']+=1
   if not x['public_source_urls'] and x.get('claim_packets_count',0)>0:counts['no_public_url_but_claim_packets_present']+=1
  stats[subsetname]={'requests':len(sub),**dict(counts)}
 eventstats[name]=stats
deadline={};anomalies=[]
for name,relative in [('hybrid_10pct','r135_hybrid_eval10_20261110/evaluation'),('bounded_200','r135_bounded_eval200_20261111/evaluation'),('verified_200','r135_verified_eval200_20261111/evaluation')]:
 count=0;false_count=0
 for line in (ROOT/relative/'RESULTS.jsonl').open(encoding='utf8'):
  row=json.loads(line);z=row['response'];d=z.get('deadline') or {};limit=d.get('global_timeout_sec');elapsed=d.get('global_elapsed_sec')
  if d.get('global_timeout_enabled') and isinstance(limit,(int,float)) and isinstance(elapsed,(int,float)) and elapsed>limit:
   count+=1;false_count+=z.get('timed_out') is False;anomalies.append({'run':name,'key':row['key'],'question':row['question'],'client_seconds':row['elapsed_seconds'],'response_wall_seconds':z.get('wall_sec'),'deadline':d,'timed_out':z.get('timed_out'),'timing_status':z.get('timing_status')})
 deadline[name]={'recorded_global_elapsed_over_declared_limit':count,'over_limit_but_timed_out_false':false_count}
enrichment={'paired_same200':paired,'model_events_nonexclusive':eventstats,'deadline':deadline,'deadline_anomalies':anomalies,'focused_cases_in_viewer':len(focus),'five_runs_rows':len(rows),'all_viewer_rows':len(rows)+len(focus),'limits':'Same-key historical comparison, not causal or semantic accuracy. Trace coverage 2511 rows, earlier two 5% only response summaries. Events can overlap; no logs or frozen databases were changed.'}
enrichment['same200_mode_transitions_hybrid10_to_verified']=[{'old_mode':a,'new_mode':b,'questions':n} for (a,b),n in transitions.most_common()]
enrichment['became_unavailable']=new_unavailable;enrichment['recovered_from_unavailable']=recovered_unavailable
(R/'DEEP_FINDINGS.json').write_text(json.dumps(enrichment,ensure_ascii=False,indent=2),encoding='utf8')
def table(headers,values):
 return '| '+' | '.join(headers)+' |\n|'+ '|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(str(v).replace('|','/').replace('\n',' ') for v in row)+' |\n' for row in values)+'\n'
names={'r135_5pct':'R135 5% เดิม (7 พ.ย.)','hybrid48_5pct':'Hybrid48 5% (8 พ.ย.)','hybrid_10pct':'Hybrid 10% (10–11 พ.ย.)','bounded_200':'Bounded 200','verified_200':'Verified-source 200'}
parts=['''# รายงานวิเคราะห์ผลลัพธ์และปัญหาจาก log ที่บันทึกไว้ทั้งหมดในขอบเขตรอบนี้

วันที่จัดทำ: 12 พฤศจิกายน 2026 (Asia/Bangkok)

## 1. ข้อสรุปที่หลักฐานรองรับ

ระบบมีทั้งปัญหาที่ตอบไม่ได้จริง ปัญหาการแยกงาน/ตรวจความครบ ปัญหาข้อความกำกวม และข้อจำกัดของข้อมูลต้นทาง ไม่ใช่เพียงไม่มีลิงก์อ้างอิง ส่วนการแก้ล่าสุดพิสูจน์ว่าบางกลุ่มดีขึ้น แต่ยังไม่มีผลชุดใหญ่ของโค้ดล่าสุดที่ใช้รับรองภาพรวม

**ข้อแลกเปลี่ยนที่พบจริงเมื่อจับคู่ 200 คำถามเดียวกัน:** Hybrid10 เดิม unavailable 22/200 → Bounded35/200 → Verified36/200 ขณะที่เวลารวมคำขอลดจาก4,158.454sเป็น370.948s จึงมีทั้งความเร็วที่ดีขึ้นและความพร้อมตอบที่แย่ลงในผลวัดย้อนหลังชุดนี้ ไม่ใช่ดีขึ้นทุกด้าน และยังแยกผลของเวลา/source/backendออกจากตัวFlowทั้งหมดไม่ได้

อ่านผลที่เซฟไว้ 5 รอบ รวม **4,623 แถวคำตอบ** และ matched assistant traces ของรอบ 10% กับ 200 สองรอบรวม **2,511 แถว** แบบ SQLite read-only พร้อมหลักฐาน focused รอบ02 อีก 27 คำถาม source-only และ 21 คำขอ HTTP การนับแถวข้ามรอบมีคำถามซ้ำ จึงห้ามเรียกว่า 4,623 คำถามไม่ซ้ำหรือความแม่นยำของรุ่นล่าสุด

การตรวจทุกแถวเป็นการอ่านและจัดกลุ่มด้วยสคริปต์ ไม่ใช่การรับรองความหมายโดยมนุษย์ทุกแถว ส่วนตัวอย่างที่อ่านเชิงคุณภาพระบุแยกด้านล่าง ไม่มีการเรียกโมเดล รันทดสอบใหม่ ให้คะแนน literal ใหม่ หรือแก้ข้อมูลจริง/ผล frozen

ขอบเขต “ทั้งหมด”: ทั้งหมดของไฟล์ RESULTS.jsonl ทั้งห้ารอบที่ระบุใน INPUT_MANIFEST.json พร้อม trace และ focused evidence ที่ระบุ ไม่รวมทุกแชตส่วนตัว ทุกไฟล์สำรอง ทุกการทดลองในประวัติโครงการ และไม่ได้รับประกันว่าพบ bug ทุกตัว

## 2. ปริมาณงาน สถานะ และเวลาของแต่ละรุ่น
''']
parts.append(table(['รุ่น','แถว / unique keys','HTTP 200','common_unavailable','partial','median / p95 / max (วินาที)','>60s'],[(names[n],f"{s['requests']} / {s['unique_keys']}",s['http_200'],s['modes'].get('pipeline:common_unavailable',0),s['modes'].get('pipeline:common_partial_answer',0),f"{s['timing']['median_seconds']:.3f} / {s['timing']['p95_seconds']:.3f} / {s['timing']['max_seconds']:.3f}",s['timing']['over60']) for n,s in runs.items()]))
parts.append('Hybrid48 5% มี `common_live_unavailable` อีก 1 ข้อ แยกจาก `common_unavailable` 198 ข้อ จึงมี 199 ข้อที่ชื่อ mode มี unavailable รวมกัน ห้ามสลับตัวหารโดยไม่ระบุ\n\nทุกชุดไม่มี key ซ้ำภายในไฟล์ และไม่มี outer `timed_out=true` ตาม response ที่บันทึก แต่ไม่ได้แปลว่าไม่มี timeout ภายในโมเดลหรือไม่เกินงบเวลาที่ตั้งไว้\n\n')
parts.append('### คะแนน literal ที่เซฟไว้ (ไม่คำนวณใหม่)\n\n')
score_rows=[]
for n,s in runs.items():
 saved=s.get('saved_scores_unchanged',{});g=saved.get('grades') or saved.get('literal_grades')
 if not g and n in {'bounded_200','verified_200'}:g=saved.get('bounded200' if n=='bounded_200' else 'verified200',{}).get('literal_grades')
 if g:score_rows.append((names[n],g.get('matched'),g.get('not_matched'),g.get('unsupported_literal',g.get('not_scored_no_supported_literal')),str(s.get('saved_score_file'))))
parts.append(table(['รุ่น','matched','not matched','ไม่มีเกณฑ์ literal รองรับ','ไฟล์คะแนน'],score_rows))
parts.append('สำหรับ 10%: matched 1,946 / 2,487 supported grade identities (78.25% ของเกณฑ์ข้อความที่รองรับ), not matched 541, unsupported 3,097; มี 1,242/2,111 คำถามไม่มีเกณฑ์ literal รองรับเลย เทียบ R134 ที่บันทึกไว้ 2,008/2,487: ผ่านทั้งคู่ 1,882, เฉพาะรุ่นใหม่ 64, เฉพาะเก่า 126, ไม่ผ่านทั้งคู่ 415 ตัวเลขนี้ไม่ใช่ semantic accuracy และ 541 ไม่ใช่จำนวนคำตอบผิดทางความหมาย\n\n')
parts.append('## 3. เปรียบเทียบเฉพาะ 200 keys เดียวกัน\n\n')
parts.append(table(['รุ่น / subset','จำนวน','unavailable','partial','รวมเวลาคำขอ (s)','median / max (s)','>60s'],[(names[n],s['requests'],s['unavailable'],s['partial'],f"{s['sum_seconds']:.3f}",f"{s['median_seconds']:.3f} / {s['max_seconds']:.3f}",s['over60']) for n,s in paired.items()]))
parts.append('ทั้งสามชุดจับคู่ได้ครบ 200 keys เวลารวมข้างบนเป็นผลรวม elapsed ของคำขอ ไม่รวม preflight/ช่วงว่างทั้งหมด รอบ verified เคยรายงานทั้งรอบ 384 วินาที ขณะที่ผลรวมคำขอ 370.948 วินาที จึงไม่ขัดกัน เปรียบเทียบนี้ยังมีความต่างของข้อมูล เวลาและสถานะ backend; ไม่สรุปว่าแพตช์ทำให้เวลาหรือคะแนนเปลี่ยนทั้งหมด\n\nLiteral ที่บันทึกบน 200 ชุดนี้: Hybrid10 subset 203/255 → bounded 202/255 → verified 196/255; R134 197/255 ส่วนต่าง bounded→verified มีเพียง 2 คำถาม: 5 grade identities รอ `3 sessions` แต่เว็บที่ตรวจตอนแก้ระบุ 6 และอีก 1 ของ Shifter ไป unavailable ไม่แก้เกณฑ์หรือบวกคะแนนกลับเอง ส่วน net1 identity ระหว่าง Hybrid10 subset→bounded ยังไม่มี per-criterion paired-difference file ที่อ่านได้ในขอบเขตนี้ จึงไม่อ้างว่าแจกแจง semantic cause ของส่วนต่างทั้งหมดครบแล้ว\n\n')
parts.append(f'เทียบ Hybrid10→Verified: มี {len(new_unavailable)} คำถามที่เดิมไม่ใช่ common_unavailable แล้วกลายเป็น unavailable และ {len(recovered_unavailable)} คำถามที่ฟื้นจาก unavailable เป็นสถานะอื่น ทั้งนี้การฟื้นเป็น partial/unconfirmed ยังไม่ใช่การตอบครบ\n\n'+table(['คำถามที่กลายเป็น unavailable','สถานะเดิม','เวลาเดิม→ใหม่ (s)'],[(x['question'],x['old_mode'],f"{x['old_seconds']:.3f} → {x['new_seconds']:.3f}") for x in new_unavailable]))
parts.append('## 4. “ไม่มีข้อมูลยืนยัน” ต้องแยกเป็นหลายชนิด\n\n'+table(['สถานะ','ความหมายที่ควรใช้','ห้ามสรุป'],[
('unavailable','กระบวนการตีโจทย์/ตรวจหลักฐานยังไม่พร้อมในคำขอนั้น','ต้นทางไม่มีข้อมูล หรือโมเดลล่มทุกครั้ง'),('partial','บางส่วนมีข้อมูล แต่ความครบ/เงื่อนไข/ช่วงมีผลยังไม่ยืนยัน','คำตอบทุกบรรทัดผิด'),('unconfirmed / not_current','ยังยืนยันขอบเขต ปัจจุบัน หรือ live state ไม่ได้','ไม่มี URL อย่างเดียว'),('clarification','ต้องการข้อมูลเพิ่มหรือความหมายกำกวม','ระบบเสียทุกกรณี'),('HTTP 200','ส่ง response กลับได้','เนื้อหาถูกต้อง'),('ไม่มี public URL','sources ที่ส่งออกไม่มี URL สาธารณะ','ไม่มี internal claims/receipts เสมอไป')]))
parts.append('### ข้อมูลอ้างอิงที่ส่งออก\n\n'+table(['รุ่น','ไม่มี public URL ใน response.sources','มี public URL','หมายเหตุ'],[(names[n],s['flags_per_request_nonexclusive'].get('no_public_url_in_sources_not_proof_of_missing_evidence',0),s['requests']-s['flags_per_request_nonexclusive'].get('no_public_url_in_sources_not_proof_of_missing_evidence',0),'ตรวจช่อง sources เท่านั้น; ไม่รวม URL ในคำตอบ/ข้อมูลวันหยุด') for n,s in runs.items()]))
parts.append('หลังแก้เว็บใน 200 เดียวกัน จำนวนไม่มี URL ใน sources ลดจาก 195 เป็น 168 แต่ไม่ได้ทำให้ unavailable หายไป (35→36) จึงมีหลักฐานชัดว่าการเติมลิงก์อย่างเดียวไม่แก้ทุกปัญหา ลิงก์หน้าเว็บ, หลักฐานภายใน, สิทธิ์เผยแพร่, ช่วงมีผล และการรองรับสิ่งที่ถาม เป็นคนละข้อกำหนด\n\n')
parts.append('## 5. สิ่งที่พบจาก model receipts และ flow traces\n\n')
parts.append(table(['รุ่น / ขอบเขต','จำนวน','มี event admission_denied','บันทึก timeout โดยตรง','gateway ส่งสำเร็จอย่างน้อยครั้งหนึ่ง','gateway ล้มอย่างน้อยครั้งหนึ่ง'],[(names[n]+' / '+label,s['requests'],s.get('admission_denied_event_requests',0),s.get('explicit_timeout_requests',0),s.get('gateway_transport_success_requests',0),s.get('gateway_transport_failure_requests',0)) for n,groups in eventstats.items() for label,s in groups.items()]))
parts.append('จำนวนต่อแถวซ้อนกันได้: คำขอเดียวอาจเรียกสำเร็จครั้งหนึ่งแล้วล้มอีกครั้ง หรือถูกปฏิเสธ stage หนึ่งและ timeout อีก stage หนึ่ง Event admission_denied เป็นหลักฐานว่าตัว app ไม่ส่ง stage นั้นต่อ ไม่ใช่หลักฐานว่าถูกระบบอนุมัติของ Codex ปฏิเสธ และยังไม่ระบุว่ามาจาก cooldown/concurrency/health เฉพาะเหตุใดหากไม่มีรายละเอียดเพิ่ม\n\n')
if (R/'ADMISSION_AUDIT.json').exists():
 aa=load(R/'ADMISSION_AUDIT.json');parts.append('### ตรวจ receipt ชั้น admission เพิ่มแล้ว\n\n'+table(['รุ่น','คำขอที่ถูกdenied','health statusจากreceipt','ในunavailable'],[(names[n],v['denied_requests'],v['health_status_per_request_nonexclusive'],v['unavailable_health_status_per_request_nonexclusive']) for n,v in aa['runs'].items()]))
 parts.append('receiptระบุ circuit breaker cooldown active, failure_scope=kind_only, last_error_type=TimeoutError และ http_attempted=false เช่น Monster Hunter Rise ใช้จอยยังไง: evidence_selection ถูกปฏิเสธด้วยcooldownเหลือ86.34วินาทีหลังfailure2ครั้ง **เป็น health gate ของแอป local ไม่ใช่ permission block ของ Codex** ไม่ควรปิดguardทั้งชุดเพื่อให้เรียกได้ ควรตรวจdeadline/cooldown recovery, half-open probesแบบจำกัด และทางตอบข้อมูลที่ทำด้วยโค้ดได้\n\nใน36unavailableของverified200: timeoutอย่างเดียว6, admission-deniedอย่างเดียว22, มีทั้งสองอย่าง8 รวม36 ข้อมูลนี้อธิบายสิ่งที่เกิดในคำขอได้ชัดขึ้น แต่ยังไม่พิสูจน์ว่าโมเดลล่มถาวรหรือทุกข้อจะตอบถูกหากเรียกโมเดลสำเร็จ\n\n')
parts.append('### Reason codes: มีไว้ชี้ทาง ไม่ใช่ข้อสรุปสาเหตุ\n\n')
for name in ['hybrid_10pct','verified_200']:
 s=runs[name];parts.append('**'+names[name]+' — ทุกสถานะคำตอบ**\n\n'+table(['reason ที่บันทึก','จำนวนคำขอที่พบ (ซ้อนกันได้)'],list(s['recorded_reasons_per_request_nonexclusive'].items())[:18]))
parts.append('รายการนับใหม่ด้านบนตรวจทุกสถานะ ไม่ใช่เฉพาะ unavailable และข้าม snapshot/raw source fields เพื่อไม่เอาข้อมูลต้นทางมาปนกับ diagnostics จึงต้องไม่เทียบจำนวนตรง ๆ กับ UNAVAILABLE_TRACE_AUDIT เก่าซึ่งนับเฉพาะ324ข้อ เช่น no_accepted_replacement_task ปรากฏในคำตอบที่อ่านได้ด้วย จึงไม่ใช่ bug ทุกครั้ง\n\n### First-stage labels ใน flow audit\n\n')
parts.append(table(['stage label','Hybrid10 จำนวนคำขอ','Verified200 จำนวนคำขอ'],[(k,runs['hybrid_10pct']['recorded_first_stages_per_request_nonexclusive'].get(k,0),runs['verified_200']['recorded_first_stages_per_request_nonexclusive'].get(k,0)) for k in sorted(set(runs['hybrid_10pct']['recorded_first_stages_per_request_nonexclusive'])|set(runs['verified_200']['recorded_first_stages_per_request_nonexclusive']))]))
parts.append('นี่เป็น attribution ที่ระบบเขียนเอง ไม่ใช่การพิสูจน์ว่า rendering เป็น root cause ตามจำนวนทั้งหมด ต้องอ่านคำถาม/คำตอบและ receipts ประกอบ\n\n')
parts.append('## 6. รายการปัญหาและข้อจำกัดพร้อมแนวทางแก้\n\n')
issues=[
('LOG-01','P1','การรอโมเดลกินเวลาและงบไม่หยุดทุกเส้นทาง','พบจริงในรอบเก่า; hard deadline ยังไม่พิสูจน์','Hybrid10 >60s362ข้อ; มี gateway timeout ตรง ๆ และ outlier2,859.009s','ใช้ monotonic request deadline ร่วม, cap connect/read/queue แต่ละ stage, จบด้วย verified partial, ตรวจ cancellation และ deadline telemetry'),
('LOG-02','P1','model admission ถูกปฏิเสธแต่ข้อความแสดงเป็น transport/model unavailable','เปิด','verified200 พบ model_admission_denied ใน trace; บางข้อไม่มี gateway transport attempt','แยก not_attempted/admission/timeout/protocol/schema ให้ตรง; เก็บ health/cooldown/concurrency cause โดยไม่ retry วน'),
('LOG-03','P1','คำถามชัดแต่ native predicate ไม่ครอบคลุมหรือคำผิดพาไปโมเดล','แก้บางกลุ่มแล้ว; ที่เหลือเปิด','Shifter อยู่ซนไหน, Gaming Keyboard อยู่โซนไกน, บุคคล/เกมหลายคำถามไปfallback','ใช้ source-bound vocabulary + bounded spelling candidates; รักษา raw/name/number/polarity; ambiguity ต้องถาม'),
('LOG-04','P1','แยกงานเกิน/ซ้ำ แล้วแจ้งว่างานเดิมยังไม่ตอบ','แก้ boundary/occurrenceเฉพาะขอบเขต; ต้องตรวจ output ต่อ','PUBG genre ตอบแล้วแต่แจ้งไม่มีแผน; PS5 usage และวันจันทร์มีหัวข้อซ้ำ','ใช้ need IDs/raw spans ร่วม, reconcile completion กับ claims, deduplicateเฉพาะงานเดียวกัน ไม่รวมคนละบริการ'),
('LOG-05','P0','ชื่อเกม/ภาค/แพลตฟอร์มถูกยืมข้ามเป้าหมาย','แก้ numeric family C04/C05 เฉพาะกรณีที่ตรวจ','TEKKEN9→8 ก่อนแก้; compatibilitydescriptionหลุดหลังแก้typedเพียงชั้นเดียว','ตรวจ source relation ที่ selector/receipt/final delivery; ไม่มี fallbackเลี่ยงguard; Roman/DLC/wordsequelsยังต้องตรวจ'),
('LOG-06','P0/P1','คำผิดในกลุ่มผู้ใช้ทำให้แสดงราคาหลายกลุ่ม รวม0บาทที่ไม่ใช่คำตอบเฉพาะผู้ถาม','ต้องยืนยันสถานะปัจจุบัน; พบจริงใน frozen200','นักศึกษาต่งามหาลัยNintendoส่ง6อัตรารวมPSU0บาท แม้ไม่ได้ฟันธงว่าฟรี','แยก audience unresolved จาก audience all; ถามยืนยันว่าเป็นนักศึกษาต่างสถาบันก่อนคำนวณ; ห้ามเลือกPSUจากคำว่านักศึกษาอย่างเดียว'),
('LOG-07','P0/P1','ราคา/จำนวน/ระยะเวลา: คำตอบกับคำชี้แจงไม่สอดคล้อง','บางกลุ่มแก้แล้ว แต่ไม่ครอบคลุมหลายservice','PC30นาทีแสดง0บาทสำหรับ30นาทีแล้วแจ้งไม่ยืนยัน30นาที; PS5ถาม30แต่แสดง60พร้อมcaveat','ให้ proofผูก task/rate/rule/person/service ทุกบรรทัด; แยก rate display กับ payable total; รักษา normal positives'),
('LOG-08','P1','ช่วงจำนวนคน/หน่วยเรียกเก็บยังคลุมเครือ','เปิดตามsourceบางรายการ','Nintendo/VR มีคนเป็นช่วง และ unitบางrateunknown; ยังไม่พิสูจน์การหารคนหรือราคาเหมารวม','รักษาช่วงคน, ถาม allocation, ไม่สร้างราคาต่อคนเอง; owner-confirmed billing unitเป็นข้อมูลที่ต้องเพิ่ม'),
('LOG-09','P1','ตารางเปิดอาคาร/เล่น/จอง/สถานะว่างสดไม่ใช่เรื่องเดียวกัน','เปิดบางoperation; การระงับบางข้อสมเหตุผล','VR equipment ถูกตีเป็นlive availability; Cockpit14–15มีURLแต่mappingไม่ครบ','แยก operation/static inventory vs live occupancy, require date/time/resource IDs, cache statusแยกจากschedule'),
('LOG-10','P1','ข้อมูล policy/personnel ยังไม่มีช่วงมีผลชัด','ข้อมูลยังไม่ครบ ไม่ใช่ไม่มีเว็บอย่างเดียว','หลายpartialแสดงบทบาท/กฎพร้อม validity caveat','เพิ่ม effective interval/approval/source authorityเมื่อเจ้าของยืนยัน; ไม่เดาวัน; จัดcaveatสั้นและตรงขอบเขต'),
('LOG-11','P1','ข้อความต้นทางหลายฉบับซ้ำหรือscopeยังไม่ชัด','เปิด','เครื่องดื่มแสดง2sourceข้อความเหมือนกันพร้อมvariant warning','ผูก revision/scope/authorityก่อนยุบ; เท่ากันทางข้อความไม่พิสูจน์scopeเดียวกัน'),
('LOG-12','P1','กติกาแข่งขันต้องผูก event/edition/clause และความครบ','เปิดบางส่วน','บางข้อส่งกฎงานหนึ่งพร้อมขอให้ยืนยันงาน; บางข้อtimeout evidence_selection','แยกถามตัวงานจากอ่านข้อกฎ, รองรับtargetedclause+dependency, อย่าใช้ชื่อเกมแทนตัวงาน'),
('LOG-13','P2','ข้อความจากข้อมูลต้นทางไม่สะอาด','เปิด','อาหรับปนTEKKEN8และตัวอักษร literal\\n ในCockpitusage','เพิ่มdata-qualityauditแยกจากsemanticguard; แก้ผ่านownerworkflow/สำเนาและเก็บrevision ไม่rewriteเงียบ ๆ'),
('LOG-14','P1/P2','literalเกณฑ์เก่าทำให้คำตอบตามsourceใหม่ดูคะแนนลด','พบจริง; ต้องแยกจากbug','5criteriaคาด3sessionsแต่เว็บที่ตรวจได้6; Shifterอีก1เป็นunavailableจริง','เก็บคะแนนเดิมและsource-alignedreviewคู่กัน; versiongoldsetและtimestamp ไม่เปลี่ยนตัวหารเพื่อทำคะแนน'),
('LOG-15','P1','publiccitation, internalreceipt และsource applicabilityถูกเข้าใจเป็นเรื่องเดียว','เปิดบางเส้นทาง','verified200มีURLเพิ่มแต่unavailableไม่ลด; livebookingมีURLแต่ยืนยันสถานะไม่ได้','แสดงsourceเมื่อexactpinsตรง, แยก noURL/noevidence/notcurrent/targetmismatch; URLไม่ใช่ใบอนุญาตให้claim'),
('LOG-16','P1','การวัดยังไม่ครอบคลุมการใช้งานทั้งหมด','เปิด','27focused/149checks/21HTTPไม่ใช่broadscoreใหม่; C07ใน200มีเพียง1ตัวอย่าง','เก็บheldoutไม่ใช้ฝึก, controlledsparsecategorytestsแยก, owner/editor lifecycleและattachmentsยังต้องผ่านgates'),
('LOG-17','P2','logโตและdiagnosticซ้ำทำให้ตรวจยาก/ใช้พื้นที่มาก','พบจริง','transcriptsรอบ10%ประมาณ4.59GBสำหรับ2111คำขอ; response logประมาณ21.7MB','แยก compactrequestledgerจากartifact blobs/source snapshotsตามhash, retention/rotation, เก็บreceiptpointerครบก่อนลดข้อมูล'),
('LOG-18','P1','ถามนอกขอบเขตอาจเสียเวลาเรียกmodelก่อนบอกขอบเขต','พบในตัวอย่าง; ยังไม่ใช่ทุกoutofscope','will it rain tomorrow15.242sและserver/client13.963sไปunavailable','ใช้boundedoutofscoperouteเมื่อหลักฐานชัด, ไม่เดาคำตอบสภาพอากาศ; ambiguityยังใช้budgetจำกัด')]
parts.append(table(['ID','ระดับ','ปัญหา','สถานะ','หลักฐาน','แนวทาง'],issues))
parts.append('ระดับ P0/P1 เป็นลำดับความสำคัญตามผลกระทบและความเสี่ยง ไม่ใช่คำยืนยันว่าคำตอบทุกข้อในกลุ่มผิด ปัญหาทางไฟล์/โฟลเดอร์ไม่พบหลักฐานว่าเป็นต้นเหตุโดยตรงของกรณีเหล่านี้: logsชี้ไปที่ field/target/relation/reader/budget ต้องไม่จัดโฟลเดอร์ใหม่แทนการแก้ binding\n\n')
parts.append('## 7. กรณีเวลาเกินงบที่ต้องไม่มองข้าม\n\n'+table(['รุ่น','เกิน global limit ที่รายงาน','เกินแต่ timed_out=false'],[(names[n],v['recorded_global_elapsed_over_declared_limit'],v['over_limit_but_timed_out_false']) for n,v in deadline.items()]))
parts.append('กรณีช้าที่สุดใน frozen Hybrid10: `Please check: What do the RoV tournament ruls say about the competition format? please.` client 2,859.009s, response wall 2,858.9373s, configured global limit190s, deadline remaining0 แต่ timing_status=completed และ timed_out=false ตัวเลขทั้งฝั่งclientและserverสอดคล้องกัน จึงไม่ใช่แค่ผลรวมเวลารอบ แต่ยังไม่มีหลักฐานแยกว่าเกิดจาก blockingcall, processpause/เครื่องsleep หรือเส้นทางใด เพราะ request_context ของคำขอนี้ไม่มี gatewayevent การไม่มีeventไม่พิสูจน์ว่าไม่ได้เรียกผ่านทางอื่น\n\nสรุปได้เพียงว่ารอบนั้นยังไม่บังคับเวลาหรือรายงานสถานะเกินงบได้ครบทุกเส้นทาง ส่วน bounded200/verified200เร็วขึ้นจริงตามelapsed แต่ยังเป็นการจำกัดแบบcooperative ไม่ใช่harddeadlineproof\n\n')
parts.append('## 8. ตัวอย่างที่อ่านคำถาม–คำตอบและตรวจความสอดคล้องจริง\n\nการวิเคราะห์ด้านล่างเป็น intent/output review เฉพาะตัวอย่าง ไม่ใช่ source entailment acceptance ทั้งหมด และเป็นผลของรุ่นที่ระบุ ไม่ย้ายข้อผิด frozen ไปกล่าวหาว่ายังเกิดในโค้ดล่าสุดโดยไม่มีผลใหม่\n\n')
reviews=[
('c137296b97e3f28d83912421eda5acce608c6514b8195f85d8e786813498ac50','ผู้ใช้ถามการถ่ายวิดีโอภายในสถานที่','แยกin-gamecaptureจากถ่ายบุคคล/สถานที่ได้ การwithholdpermissionสมเหตุผลจากขอบเขตที่แสดง ไม่ควรเอากฎcaptureไปอนุญาตถ่ายสถานที่','คงscopeguard แต่ตอบข้อจำกัดก่อนและลดข้อความซ้ำ'),
('227ea7ee0beee57012b2bda07a4b24210e9b09a4aa642ccb82be1f85f942a567','ต้องการวิธีใช้อุปกรณ์PS5','มีusageแล้วแต่หัวข้อซ้ำและบอกไม่มีsourceสำหรับdetailอีกครั้ง ทำให้ไม่รู้ว่าตอบส่วนใดแล้ว','reconcile need IDs และบอกเฉพาะขั้นตอนที่sourceยังไม่มี'),
('70580dbafcf62f55cb7c3dd508c72043894bd70ae58807cdbf43df8452656075','ต้องการรายการอุปกรณ์ที่มีในVRZone','ตอบรายการแล้วกลับขอเวลา อาจสับสนstaticinventoryกับliveavailability','ตรวจoperationก่อนบังคับtime slot'),
('07c763b10d8997393a45bcdbaabfe93c079aacbd774f29f96caa3832a4629878','ถามแนวเกมPUBG','ตอบBattleRoyaleแล้วแจ้งส่วนเดิมยังไม่มีแผน เป็นcompletion/output inconsistency','ผูกcoverageกับneedและclaimที่ส่งจริง'),
('7dc588121765be2792f3be6f8db0071b58ebb4009f4c925c6ee284b136b2d36f','ถามราคานักศึกษาPSUเล่นPC30นาที','แสดง0บาทสำหรับ30นาทีแล้วแจ้งยังไม่ยืนยัน30นาที ต้นเหตุที่ควรตรวจคือproofของหลายservice/renderer ไม่ใช่เติมURLอย่างเดียว','ให้rate/durationproofแต่ละserviceตรงกับข้อความและpartialstate'),
('9baf9105a9fb80b9173340cfca87b95d89e0f08f82071915601f60978af935af','พิมพ์ผิดแต่สื่อว่านักศึกษาต่างมหาวิทยาลัยเล่นNintendo30นาที','ส่งราคา6รายการรวมPSU0บาท แม้เป็นalternative ไม่ฟันธงว่าฟรี แต่ไม่ตอบกลุ่มที่ตั้งใจและเสี่ยงสับสน','ถามยืนยันaudienceเมื่อไม่มั่นใจ;อย่ากลายเป็นall audiencesโดยปริยาย'),
('ce48c51aaa345c0c35e3a80dcc74d0579d6b4070a68c404f49c498736d08c35c','ถามPS5นักศึกษาต่างมหาวิทยาลัย30นาที','ส่งอัตรา60นาทีและบอก30ยังยืนยันไม่ได้ แยกได้ว่าไม่ได้ตอบยอด30ครบ;ยังต้องถาม/พิสูจน์roundingrule','บอกก่อนว่านี่เป็นอัตราอ้างอิง60นาทีและยอดที่ถามยังไม่ยืนยัน'),
('99e58322f22105f7f5fc09134ef72b9d2355e0fb44b48cd67822e0b96e03c6f5','ถามCockpitบุคคลทั่วไป30นาที','ตอบ200THB;ตรวจfrozenrateพบ20000minor/60นาทีและsession_ceil จึงไม่สรุปว่า200ผิดจากการหารครึ่ง แต่ข้อความยังไม่อธิบายceilและunitยังunknownในrecord','แสดงกติกาคิดเต็มช่วงตามsourceและตรวจหน่วย/approvalก่อนclaimpayabletotal'),
('36c4c5f316fbaba1a03cb02d0543234b1606c4e8c6b70447ade02748425cd149','ต้องการเครื่องCockpitที่ว่าง14–15','มีลิงก์จองจริงแต่mappingหรือwindowยังไม่ครบ จึงไม่สามารถสรุปfree/occupiedได้','ถามวันที่/จับresourceและwindowให้ครบ ไม่เดาว่างจากschedule'),
('91170922dba40c4c9335d6d2234009d4c587c393e5f863298778b1c1d068ea4d','ถามวิธีจองและวันเปิดสองเรื่อง','ส่ง6ขั้นตอนจอง แต่วันเปิดยังไม่มีข้อมูลยืนยัน;partialถูกสะท้อนแต่ยังไม่ครบเจตนา','ตรวจservicecalendarbindingของsiblingโดยไม่ทิ้งbooking'),
('46182d9ba58edbb20f085b98d0f6b7b82c836832b43f8da8751f5a1f96b338a1','ถามจองได้กี่sessions','ตอบ6 แต่literalเก่ารอ3 จึงเป็นsource/criterionversionconfound5identities ไม่ใช่5semanticbugs','รักษาคะแนนเก่าและแนบsource-alignedcheckที่มีอยู่'),
('41012f5c83e7677c556132b420329ddeeddecb5cc52392d26ffd96482d213616','ถามตำแหน่งShifterด้วยคำพิมพ์ตก','frozenตอบunavailableจริง;มีแพตช์native+fieldและHTTPหลังวัดที่บันทึกแล้ว จัดเป็นhistoricalrepairedwithinbounds','ไม่อ้าง196scoreรวมแพตช์หลังวัด'),
('8b03ee50da5f0a02e4a0cb26fd37ac3f0b226e7634b32075fdf3c0e0400ddbad','ถามวันจันทร์เช้าเปิดหรือปิด','เริ่มบอกไม่พบคำตอบแล้วตอบปิดบำรุงรักษาในหัวข้อเดิมซ้ำ;ยังต้องแยกopeningกับplayservice','นำdirectanswerที่มีscopeก่อนและตัดorphanneednotice'),
('382fe8f396d714c1378b09ed7eb764a5d49e48ddd3189aac8047bae0644a5c38','ถามดื่มเครื่องดื่มได้หรือไม่','สองpolicyให้ใจความเหมือนกันแต่ระบบยังมองvariantsunresolved;ไม่ใช่ข้อขัดแย้งข้อความโดยตรง','ตรวจscope/version/sourceก่อนยุบและอธิบายจุดต่างจริง'),
('e428a2156c0eb3909c3af048050043db617404f7d851aab7eecfcb45307342b5','ถามกติกาTEKKEN8เรื่องsetting','ส่งclauseหลายข้อและชื่องานพร้อมcaveat ยังต้องยืนยันeventและdependencies;มีเนื้อหาไม่เท่ากับครบกฎที่ใช้จริง','ถามตัวงานเมื่อจำเป็น, ไม่ขยายกฎeventหนึ่งไปทุกงาน')]
# Resolve by exact keys; accidental hand transcription differences must not invent examples.
verified=byrun['verified_200'];matched_reviews=[];missing_reviews=[]
for key,intent,assessment,nextstep in reviews:
 x=verified.get(key)
 if not x:missing_reviews.append(key);continue
 matched_reviews.append({'key':key,'run':'verified_200','question':x['question'],'answer':x['answer'],'intent':intent,'assessment':assessment,'next_step':nextstep})
 for_append=f"### ตัวอย่าง {len(matched_reviews)} — {intent}\n\n- รุ่น: verified_200; key `{key}`\n- คำถาม: {x['question']}\n- สถานะ/เวลา: `{x['mode']}` / {x['seconds']:.3f}s\n- คำตอบที่เซฟไว้:\n\n"+'\n'.join('> '+line for line in x['answer'].splitlines())+f'\n\n**วิเคราะห์:** {assessment}\n\n**ควรแก้/รักษา:** {nextstep}\n\n'
 parts.append(for_append)
(R/'QUALITATIVE_REVIEW.json').write_text(json.dumps({'scope':'manual intent/output consistency review of named saved examples; source validation only where expressly stated','reviewed_count':len(matched_reviews),'items':matched_reviews,'unmatched_draft_keys_not_used':missing_reviews},ensure_ascii=False,indent=2),encoding='utf8')
parts.append('## 9. unavailable ทั้ง 36 ข้อใน verified200\n\nนี่คือรายการผลเก่าเพื่อจัดคิว ไม่ใช่ยืนยันว่าทั้ง36ยังล้มในcandidateปัจจุบัน reasonแสดงย่อ;รายละเอียดทั้งหมดดูQUESTION_AUDIT/HTML\n\n')
parts.append(table(['key','คำถาม','วินาที','model event ที่ตรวจพบ','reasonสำคัญ'],[(x['key'],x['question'],f"{x['seconds']:.3f}",', '.join(sorted(set(str(e.get('stage')) for e in x.get('model_calls',[])))),', '.join(c for c in x.get('reason_codes',[]) if c not in {'no_accepted_replacement_task','compatibility_scope_not_migrated'})[:500]) for x in verified.values() if x['mode']=='pipeline:common_unavailable']))
parts.append('## 10. การแก้ล่าสุดทำอะไรได้แล้ว และยังพิสูจน์อะไรไม่ได้\n\n'+table(['กลุ่ม','หลักฐานก่อนแก้','หลักฐานหลังแก้','ขอบเขต'],[
('sharedboundary/context','plannerกับobserverแบ่งไม่ตรง;บางpositiveผ่านด้วยcorrectivetasksอยู่แล้ว','round01 105checks/14HTTP','ไม่อ้างbaselineผิดทุกข้อ'),('repeatedquote','6checksล้ม3','6checksผ่าน','ประโยคเต็มซ้ำ/ taskfamilycountตรง;substringกำกวมยังblock'),('wrongnumericgameedition','matrix26/27;TEKKEN9ตอบ8;แก้typedอย่างเดียวcompatยังหลุด1/18','numeric19checksและHTTPpositives/negativesผ่าน','source-derivednumericfamily C04/C05;ไม่ครอบคลุมRoman/DLCทุกแบบ'),('finalround02','เก็บfailureเดิมครบ','27matrix +149checksอื่น +21HTTP/52assertionsผ่าน','คนละตัวหารและซ้ำพฤติกรรม;ไม่ใช่accuracy'),('sourcequality','อาหรับปนในคำตอบ','ตรวจพบอยู่ในpayloadจริง','ยังไม่แก้ownerrecord;ไม่ใช่หลักฐานว่าโมเดลแต่งคำนี้ขึ้น')]))
parts.append('โค้ดlatest commit99791918 ยังไม่มี full200/2111ใหม่ การใช้คะแนน196/255หรือ1946/2487แทนคะแนนlatestจึงไม่ถูกต้อง และผลscopeguardผ่านไม่พิสูจน์ความถูกต้องทางเกมของข้อความต้นทางทุกบรรทัด\n\n')
parts.append('## 11. แผนแก้จากสาเหตุร่วมและเกณฑ์ตรวจ\n\n'+table(['ลำดับ','งาน','กรณีปกติที่ต้องรักษา','กรณีผิดที่ต้องกัน','เงื่อนไขจบรอบ'],[
('1','need completion / partial output reconciliation','ราคา+จอง+เกมครบ;usage/genreตอบตรง','ตอบแล้วกลับบอกส่วนเดิมไม่มีข้อมูล;หัวข้อซ้ำ','finaltext/needstate/claimsตรงกันและไม่ตัดsibling'),('2','audience+duration+service scope','PSU0;ต่างสถาบันถูกกลุ่ม;หนึ่งและหลายservice','คำผิดทำให้แสดงPSU0แทนต่างมหาลัย;forgedtotal/quantity','positive+ambiguity+wrongtarget+sourceedit/withdrawผ่าน'),('3','deadline+admission diagnostics','native/source-backedตอบได้แม้modelไม่พร้อม','runcallเกินงบ,timeoutfalse,admissionถูกเรียกว่าDBเสีย','จับactualstageและเวลา;จำลองslow/denied/errorโดยไม่หยุดmodel;verifiedpartialยังส่งได้'),('4','source applicability/dataquality','ใช้webpinsเมื่อcontentตรง;ราคาowner0คงเดิม','stale/withdrawn/crossentity,foreigntext/literalescapes','แก้เฉพาะสำเนาพร้อมrevisionและไม่publishเอง'),('5','owner/editor lifecycle+attachments+หมวดเบาบาง','add/edit/withdrawผ่านHTTP/editorและแชต','cacheเก่า/recordถอน/ภาพยังอ่านไม่ได้แต่claimอ่านแล้ว','หลักฐานtransaction/snapshot/receiptsครบและข้อจำกัดชัด'),('6','รอบรวมหลังมีการแก้เชื่อมระบบจริง','ใช้manifestเดิมและworker1','เปลี่ยนข้อสอบ/เอาholdoutฝึก/เรียกscoresemantic','รายงานrequesterrors/literal/source-reviewedsubsetแยกและเปรียบเทียบsamekeys')]))
parts.append('ไม่เริ่มรอบรวมใหม่ในงานวิเคราะห์นี้ และไม่แก้runtimeตามรายการข้างบนโดยเงียบ ๆ งานรอบนี้เป็นรายงานจากlogเท่านั้น\n\n')
parts.append('## 12. ไฟล์ส่งมอบและข้อจำกัดการตรวจ\n\n- `REPORT_TH.md`: รายงานนี้\n- `SUMMARY.json`: machine summary ทั้ง5รอบและคะแนนเดิมที่อ่านมา\n- `DEEP_FINDINGS.json`: same200 comparisons, eventcounts, deadline anomalies\n- `INPUT_MANIFEST.json`: path/SHA256ของRESULTSทั้ง5ไฟล์และSQLiteที่อ่านแบบread-only\n- `FOCUSED_RESULT_INDEX.json`: result summaries รอบ02รวมfailedattempts\n- `QUALITATIVE_REVIEW.json`: ตัวอย่างที่อ่านเชิงคุณภาพและคำวิเคราะห์\n- `.local-private/RESULTS_ANALYSIS_VIEW.html`: เปิดดู/ค้นคำถามคำตอบทั้งหมดและfocusedcasesที่เครื่อง โดยไม่มีAPIภายนอก\n- `.local-private/QUESTION_AUDIT.jsonl`, `.csv`: รายการทุกแถวจาก5รอบ พร้อมreason/flagsที่สกัด\n- `.local-private/FOCUSED_CASES.jsonl`: 48focuseddeliveries แยกจากตัวหารbenchmark\n\nrawanswers/traces/DBอยู่เครื่อง ไม่ใส่Git มีเพียงรายงานสรุป/สคริปต์/manifestตามขอบเขตที่ผู้ใช้อนุญาต\n\nข้อจำกัด: สองรอบ5%อ่านresponseครบแต่ไม่ได้เปิดSQLitetraceทั้งหมดใหม่;3รอบหลังmatchtraceครบ2511คำขอ การนับreasonเป็นสิ่งที่ระบบรายงานและซ้อนกันได้ ไม่ใช่rootcauseproof ส่วนsourcefactตรวจเจาะจงเฉพาะที่ระบุ ไม่ได้เปิดเว็บใหม่ อ่านภาพแนบครบ หรือรับรองsemanticทุก4623แถว ไม่รวมผลfixture/กรณีปลอมเป็นproductionexamples การสร้างสคริปต์ครั้งแรกมีencodingnameผิดก่อนอ่านคะแนน แก้แล้วรันเฉพาะการวิเคราะห์ใหม่ ไม่ใช่Flowfailureและไม่มีการทดสอบโมเดลซ้ำ\n\nเอกสาร100ปัญหา/143auditgaps/76requirementsเดิมอยู่ `../r135_bounded_response_20261111/ALL_KNOWN_ISSUES_TH.md` ใช้ประกอบประวัติ ไม่ลบหรือเปลี่ยนrequirementเป็นcompleteจากรายงานนี้\n')
(R/'REPORT_TH.md').write_text('\n'.join(line.rstrip() for line in ''.join(parts).splitlines())+'\n',encoding='utf8')
print(json.dumps({'report':str(R/'REPORT_TH.md'),'manual_review_cases':len(matched_reviews),'unmatched_draft_keys':missing_reviews,'viewer_rows':len(rows)+len(focus),'same200':paired,'event_counts':eventstats,'deadline_counts':deadline},ensure_ascii=False))
