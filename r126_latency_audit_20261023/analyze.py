"""Produce measured latency evidence, preserving the tested runtime unchanged."""
import collections,csv,hashlib,json,math,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;S=R.parent/'r125_date_context_presentation_20261023/system';cfg=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(cfg['output'])
def load(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(s) for s in p.read_text('utf8').splitlines() if s.strip()]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def link(p,label):return '['+label+'](<'+str(Path(p).resolve()).replace('\\','/')+'>)'
assert load(OUT/'COMPLETE.json')['requests']==34
http=rows(OUT/'HTTP_RESULTS.jsonl');timings=rows(OUT/'TIMINGS.jsonl');pools=collections.defaultdict(collections.deque)
for t in timings:pools[t['question']].append(t)
combined=[]
notes={
'date_explicit':('source_supported','วันที่ไทยชัดเจนเข้าresolverโดยตรง; ครั้งแรกมีlocal cold initialization เพิ่ม'),
'date_english':('confirmed_parser_gap','October 26 ยังไม่รองรับในdate resolver; ไปโมเดลแล้วกลับmissing_source ทั้งที่คำถามวันเดียวกันภาษาไทยตอบได้'),
'date_paraphrase':('temporal_scope_gap','ตอบเวลาประจำวันจันทร์ แต่ยังไม่ยึด “จันทร์หน้า” เป็นวันที่จริงสำหรับspecialclosure; ไม่ใช่หลักฐานว่ายืนยันวันนั้นครบ'),
'date_relative':('confirmed_parser_gap','resolverรองรับอีก3วัน แต่คำว่าอีกสามวันยังไม่ถูกแปลงเป็นตัวเลขในเส้นทางวันเวลา'),
'catalog_direct':('source_supported','รายการเกมแยกบริการตามrecorded offering'),
'catalog_paraphrase':('supported_but_slow','คำถามเกมPS5แบบอ้อมเข้าcontext model แม้ท้ายที่สุดอ่านcatalogueปัจจุบันได้'),
'catalog_filter':('operator_or_data_scope_gap','ขอเกมเล่น4คนได้ ต้องมีfilter/operatorและplayersต่อmodeที่ยืนยัน; ปัจจุบันจบunsupported_operation ไม่เหมารวมว่าsourceทุกเกมไม่มี'),
'equipment_direct':('source_supported','คำจำกัดความอุปกรณ์เข้าทางอ่านตรง'),
'equipment_paraphrase':('partial_scope_needs_review','ตีอุปกรณ์ได้หลังโมเดล แต่แสดงsubsetและเตือนความครบ ยังไม่พิสูจน์ว่าเป็นรายการทุกอุปกรณ์'),
'hardware':('source_supported','GPUจากnative specification; sourceข้อมูลปัจจุบัน ไม่ใช้เป็นผลเทียบcausalกับlegacy'),
'price_digits':('source_supported','service/audience/durationชัด ตัวเลขตรง จึงอ่านและคำนวณได้โดยไม่เรียกโมเดล'),
'price_words':('supported_but_slow','ใช้โมเดลสร้างconstraints/แปลงสองชั่วโมงก่อนคำนวณ140บาท; ช้าหลักจากJSON generation'),
'price_compare':('operation_representation_gap','คืนราคาทั้งPCและPS5 แต่โมเดลใช้price_calculateแทนcompare; จำนวนเงินไม่ถือว่าผิดเพียงเพราะรูปแบบoperationต่าง ต้องเพิ่มcomparison obligation'),
'price_multi_audience':('confirmed_wrong_clarification','จำนวนคนสองกลุ่มที่ถามจับได้แล้ว แต่aliasซ้อนเพิ่มกลุ่มนักศึกษาทั่วไปที่ไม่ได้ถาม และPCมีสองกลุ่มบริการ ทำให้billingปฏิเสธ; reasonรวมคน/บริการทำให้ถามซ้ำผิดจุด'),
'booking_direct':('partial_source_variants','อ่านขั้นตอนเร็ว แต่ยังคงหลายsourcevariantsและข้อความซ้ำ ไม่ใช่LLMช้า'),
'booking_paraphrase':('confirmed_source_binding_gap','modelfocus=booking_procedureถูก แต่ส่งต่อเป็นC08/owner_policyกว้าง ตัวอ่านยังอาศัยถ้อยคำ/aliasเดิมจนentity_not_bound; canonicalวิธีจองมีsource'),
'booking_compound':('supported_compound_but_slow','แยกbooking+weeklyได้ แต่ยังใช้context modelหนึ่งครั้งก่อนtyped children; partialเรื่องscopeตารางประจำคงอยู่'),
'cancel':('source_supported','นโยบายยกเลิกเข้ากรอบตรง'),
'policy_direct':('source_supported','นำขวดน้ำเข้า≠ดื่ม; กรอบเดิมอ่านsourceปัจจุบันโดยตรง'),
'policy_paraphrase':('confirmed_source_binding_gap','พาเพื่อนมานั่งดูถามแล้วmissing_source ทั้งที่FAQเจ้าของมีคำตอบดูได้; literal source question controlตอบได้โดยไม่ใช้โมเดล'),
'policy_personal_device':('supported_but_slow','ตอบอนุญาตนำอุปกรณ์ส่วนตัวโดยแจ้งstaffได้ แต่ใช้context modelเพื่อเข้าถึงsource'),
'documents':('selector_only_cost','ไม่เสียcontext modelแล้ว แต่ยังเรียกevidence selectorเลือกเอกสาร/คำตอบหลายฉบับ'),
'controls_direct':('source_supported','รายการbindingsตรงกับเกม/แพลตฟอร์ม พร้อมข้อจำกัดsecondary source'),
'controls_paraphrase':('confirmed_wrong_action_selection','R2/Heavy Attackอยู่ในsource แต่ไม่เข้าscoped top8; selectorได้เพียงcamera/move/map/sprint/lock/pause/block/aim แล้วตอบAim/Move ไม่ตอบตีแรง'),
'compound_controls_price':('legitimate_partial_subset','สองประเด็นถูกแยก; 8ปุ่มยังไม่ระบุsubsetเมื่อsourceมี12entries จึงไม่เรียกpartialนี้ว่าคำตอบผิดทั้งหมด'),
'rules':('content_omission_or_event_scope_gap','ถามโทษอะไรบ้าง แต่ได้เพียงหลักการพิจารณาIntent/Impact ไม่แจกแจงโทษ; genericถ้าทำผิดทำให้ไม่เข้าtopic-familyreader ต้องแยกจากเงื่อนไขความผิดเฉพาะและระบุeventscope'),
'ambiguous':('legitimate_clarification_but_slow','ไม่มีhistoryให้รู้ว่าอันนั้นหมายถึงอะไร ควรถามขอบเขตได้เร็ว แต่ปัจจุบันยังเข้าโมเดล'),
'unknown_game':('legitimate_unconfirmed_but_slow','HadesIIไม่มีsourceยืนยัน ไม่ควรแต่งว่ามี; ปัญหาด้านเวลาคือยังสร้างcontext planก่อนตอบunconfirmed'),
'live_current':('actual_provider_read','เรียกWordPressจริงและclock/freshness; ไม่ควรcacheคำตอบว่างแบบข้ามวัน'),
'live_day':('actual_provider_read','รอบจองวันที่27จากproviderจริง แยกจากตารางบริการประจำ'),
'live_missing_scope':('legitimate_fast_clarification','ทราบวันแต่ไม่ทราบเครื่อง จึงถามเฉพาะเครื่องโดยไม่เข้าโมเดล'),
'repeat_fast':('source_supported','คำถามเดิมในprocessอุ่นเร็ว; indexcacheทำงาน'),
'repeat_slow':('repeated_model_cost','คำถามอังกฤษเหมือนเดิมยังเรียกcontextอีกและยังตอบไม่ได้ แสดงว่าไม่มีinterpretation memoizationในเส้นทางนี้'),
'repeat_compound':('repeated_model_cost','compoundเดิมยังเสียcontextmodelเกือบเท่าเดิม ไม่มีการreuseplanข้ามคำขอในเส้นทางนี้')}
for row in http:
 t=pools[row['question']].popleft();gen=[e for e in t['http'] if e['kind']=='model' and any(p in e['url'] for p in ['/api/chat','/api/generate'])];events=t['events'];art=row['response'].get('decision_artifact',{})
 selected={k:sum(e['duration_sec'] for e in events if e['name']==k) for k in ['source.snapshot','index.from_snapshot','context.interpret','evidence.select','provider.fetch','answer.render_one','answer.finish','request.compile','answer.obligation_check']}
 category,note=notes[row['category']]
 combined.append({**{k:row[k] for k in ['i','category','question','started_at','wall_sec']},'pipeline_sec':t['wall_sec'],'local_cpu_sec':t['local_cpu_sec'],'model_calls':len(gen),'model_http_sec':sum(e.get('total_sec',0) for e in gen),'generated_tokens':sum(e.get('eval_count') or 0 for e in gen),'model_stages':[e.get('stage') for e in gen],'model_transport_ok':all(e.get('transport_ok') for e in gen),'timed_spans':selected,'outcome':art.get('response_type'),'semantic_review_class':category,'review_note':note,'answer':row['response']['answer'],'generation_http':gen,'artifact':art})
def percentile(xs,p):return sorted(xs)[max(0,math.ceil(len(xs)*p)-1)]
def stats(xs):return {'n':len(xs),'median_sec':statistics.median(xs),'p95_nearest_rank_sec':percentile(xs,.95),'mean_sec':statistics.mean(xs),'min_sec':min(xs),'max_sec':max(xs)}
groups={str(n):[r for r in combined if r['model_calls']==n] for n in sorted({r['model_calls'] for r in combined})};groupstats={n:stats([r['wall_sec'] for r in rs]) for n,rs in groups.items()}
contexts=[e for r in combined for e in r['generation_http'] if e.get('stage')=='context' and e.get('eval_count')]
xs=[e['eval_count'] for e in contexts];ys=[e['total_sec'] for e in contexts];xm=statistics.mean(xs);ym=statistics.mean(ys);slope=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs);intercept=ym-slope*xm;r2=1-sum((y-(intercept+slope*x))**2 for x,y in zip(xs,ys))/sum((y-ym)**2 for y in ys)
modelrows=[r for r in combined if r['model_calls']];modelshare=sum(r['model_http_sec'] for r in modelrows)/sum(r['pipeline_sec'] for r in modelrows)
gpu=[]
for sample in rows(OUT/'GPU_DURING.jsonl'):
 values=next(csv.reader([sample.get('sample','')]),[])
 if len(values)!=8:continue
 try:gpu.append({'time':sample['time'],'pstate':values[0].strip(),'power_w':float(values[1]),'sm_mhz':float(values[3]),'gpu_pct':float(values[4]),'used_mib':float(values[6]),'free_mib':float(values[7])})
 except ValueError:continue
gpu_summary={'samples':len(gpu),'states':dict(collections.Counter(x['pstate'] for x in gpu)),'ranges':{key:{'min':min(x[key] for x in gpu),'median':statistics.median(x[key] for x in gpu),'max':max(x[key] for x in gpu)} for key in ['power_w','sm_mhz','gpu_pct','used_mib','free_mib']},'sampling_interval_sec_approx':2,'not_causal_power_mode_ab_test':True}
freeze=load(R.parent/'r125_date_context_presentation_20261023/FINAL_SOURCE_FREEZE.json');changed=[p for p,h in freeze.items() if not Path(p).exists() or sha(Path(p))!=h];assert not changed
summary={'completed_questions':len(combined),'actual_transport_errors':sum('error' in r for r in http),'latency_overall':stats([r['wall_sec'] for r in combined]),'latency_by_model_calls':groupstats,'model_http_fraction_of_model_request_pipeline_time':modelshare,'model_calls':sum(r['model_calls'] for r in combined),'all_measured_model_transports_successful':all(r['model_transport_ok'] for r in combined),'context_output_length_regression':{'n':len(xs),'slope_sec_per_generated_token':slope,'intercept_sec':intercept,'r_squared':r2,'interpretation':'Observed end-to-end model HTTP time versus output tokens; not isolated decode speed or proof of causality. Includes prefill, possible queue, compute and HTTP.'},'gpu':gpu_summary,'source_files_checked':len(freeze),'protected_source_changes':changed,'runtime_modified':False,'database_modified':False,'fresh_accuracy':None,'full_test':False}
(R/'ANALYSIS.json').write_text(json.dumps({'summary':summary,'cases':combined},ensure_ascii=False,indent=2),'utf8')
env=load(R/'ENVIRONMENT.json');option=load(R/'BACKEND_OPTIONS_PROBE.json');debug=load(R/'DEBUG_PAYLOAD_PROBE.json');cf=load(R/'SOURCE_COUNTERFACTUALS.json');concurrent=load(OUT/'CONCURRENT_FAST.json')
by={r['category']:r for r in combined}
md=['# R126 — ตรวจสาเหตุความช้าและปัญหาคำถามแบบอื่น','', '## ข้อสรุป','',
f"ทดสอบ pipeline R125 จริง {len(combined)} คำถามแบบเปิดLLM ครอบคลุมวันเวลา เกม อุปกรณ์ ราคา การจอง นโยบาย ปุ่ม กติกา คำถามกำกวม และข้อมูลสด รวมถึงถามซ้ำ. เพิ่มการตรวจคำถามเร็วขณะงานโมเดลกำลังรัน, debugpayloadสองคำขอ และข้อกำหนดoutputtokenของbackendหนึ่งคำขอ",'',
f"คำขอที่เรียกโมเดลใช้เวลาใน model HTTP รวม {modelshare*100:.1f}% ของเวลา pipeline ของกลุ่มนั้น ส่วนนี้รวมเวลาอ่านprompt/สร้างJSON/อาจรอคิว/ส่งHTTP ไม่ใช่เวลาqueryฐานข้อมูลหรือจัดformat. Readerและformatterโดยทั่วไปใช้ระดับมิลลิวินาทีหรือต่ำกว่า ส่วนsnapshotประมาณเศษวินาที",'',
'ปัญหาที่แก้R125ทำให้คำถามตรงเร็ว แต่ยังไม่ทำให้ถ้อยคำหลายแบบที่มีเจตนาเดียวกันเข้าเส้นทางเดียวกันได้ทั้งหมด. การเพิ่มทางลัดเฉพาะถ้อยคำทำให้บางข้อเร็วมากและข้อใกล้กันยังช้า/พลาด นี่คือข้อจำกัดที่ยังเหลือจริง','',
'## 1. วิธีทดลองและขอบเขต','',
'- ใช้ R125 code/data เดิม ผ่าน diagnostic API12622 ที่เพิ่มtiming hooksเฉพาะprocess; APIผู้ใช้12422คงเดิม','- ทุกคำถามหลักแยกsessionเพื่อตัดhistoryที่ไม่เกี่ยวข้อง; รันลำดับเดียว ไม่ทำloadtestGPUหลายผู้ใช้','- จับเวลาระดับsource snapshot, cachedindex, context interpreter, evidence selector, provider, compiler, verifier และrenderer','- เก็บactualHTTP modelstage/responseeval_count โดยไม่ใช้sys.setprofileที่เพิ่มoverheadสูง','- ไม่แก้weights/providerfacts/approvals/ข้อมูลหรือlogsเดิม; เก็บผลใหม่ในโฟลเดอร์นี้','- เป็นชุดdiagnosticที่จงใจมีเคสยากและparaphrase ไม่ใช่randomsampleหรือFullTest และไม่ใช้คำนวณaccuracyทั้งระบบ','',
'## 2. ความเร็วตามจำนวนครั้งที่เรียกโมเดล','', '| จำนวน model generation calls ต่อคำถาม | จำนวนคำถาม | Median | P95* | สูงสุด |','|---:|---:|---:|---:|---:|']
for n,s in groupstats.items():md.append(f"| {n} | {s['n']} | {s['median_sec']:.3f}s | {s['p95_nearest_rank_sec']:.3f}s | {s['max_sec']:.3f}s |")
md += ['', '*P95ใช้nearest-rankในชุดขนาดเล็กนี้ ไม่ใช่productionSLA. กลุ่ม0callsรวมคำถามแรกcoldและproviderHTTPจริง จึงไม่ใช่เวลาอ่านฐานล้วน','',
'### ตัวอย่างที่เห็นความต่างชัด','', '| คำถาม/กลุ่ม | เวลา | Model calls | ผล |','|---|---:|---:|---|']
for key in ['date_explicit','repeat_fast','date_english','date_relative','catalog_direct','catalog_paraphrase','price_digits','price_words','price_multi_audience','documents','controls_direct','controls_paraphrase','live_current']:
 r=by[key];md.append(f"| {r['question']} | {r['wall_sec']:.3f}s | {r['model_calls']} | {r['outcome']} |")
md += ['', '## 3. สาเหตุที่ตรวจยืนยันจากผลและโค้ด','',
'### 3.1 การเข้าเส้นทางเร็วยังขึ้นกับรูปคำและaliasมาก','',
f"`มีเกมอะไรมั่ง` {by['catalog_direct']['wall_sec']:.3f}s เทียบกับ `ที่ศูนย์มีอะไรให้เลือกเล่นบนเครื่องเพลย์ห้าบ้างครับ` {by['catalog_paraphrase']['wall_sec']:.3f}s. ท้ายที่สุดทั้งคู่มีsourcecatalogueให้อ่าน แต่คำถามหลังเสียcontextmodelก่อน. Thai explicit dateเร็ว แต่October26/อีกสามวันยังไม่เข้าresolverแล้วจบunconfirmed",'',
'ต้องขยายตัวresolveวันที่/จำนวนและnormalizealiasอย่างเป็นระบบ พร้อมวัดcoverageของparaphraseตามเจตนา ไม่ใช่เก็บเฉพาะข้อที่เคยแก้ให้ผ่าน','',
'### 3.2 โมเดลต้องเขียนJSONยาวและซ้ำ แม้คำตอบลูกค้าจะสั้น','',
f"ตัวอย่างราคาคำอ่านสองชั่วโมงใช้ {by['price_words']['generated_tokens']} outputtokens และ modelHTTP {by['price_words']['model_http_sec']:.3f}s. คำถามหลายกลุ่มใช้ {by['price_multi_audience']['generated_tokens']} outputtokens และ modelHTTP {by['price_multi_audience']['model_http_sec']:.3f}s ก่อนจะถามกลับ. JSONมีfocus/context_quotes/task.quote/constraints.quote/source_record_idว่างซ้ำหลายแห่ง",'',
f"ใน context calls {len(contexts)} ครั้ง ความสัมพันธ์เชิงเส้นระหว่างmodelHTTPtimeกับoutputtokensมีR²={r2:.4f}, slope≈{slope:.3f}sต่อtokenในชุดนี้. เป็นความสัมพันธ์ที่สังเกต ไม่ใช่decodebenchmarkบริสุทธิ์ เพราะยังไม่ได้แยกprefill/firsttoken/GPUqueue",'',
'ควรให้โมเดลคืนintentcode/slotที่จำเป็นและspan offsetsอย่างกระชับ แล้วให้compilerเติมโครงสร้างเอง. การเปลี่ยนwireต้องจัดadapter/evaluationให้สอดคล้อง ไม่ตัดnum_predictจนJSONขาดหรือจำนวนคนหาย','',
'### 3.3 บางคำถามเรียกสองรอบตามลำดับ','',
f"คำถามตีแรงใช้context {by['controls_paraphrase']['timed_spans']['context.interpret']:.3f}s แล้วevidence selector {by['controls_paraphrase']['timed_spans']['evidence.select']:.3f}s รวมทั้งคำขอ {by['controls_paraphrase']['wall_sec']:.3f}s. คำถามเอกสารตัดcontextออกได้แล้ว แต่ยังเสียselectorประมาณ{by['documents']['timed_spans']['evidence.select']:.3f}s",'',
'ควรอ่านtyped facts/relationsที่พิสูจน์ได้ก่อน ใช้selectorเมื่อมีsemantic choiceจริง และลดการเลือกข้อความทั่วไปที่มีcanonical owner policyระบุอยู่แล้ว. ไม่ควรบังคับLLMทุกข้อเพียงเพราะเปิดLLM','',
'### 3.4 โมเดลตีหมวดถูก แต่ตัวอ่านยังทำkeyword bindingซ้ำและเสียfocus','',
'คำถาม `ถ้าจะเข้าไปเล่นต้องเริ่มตรงไหนก่อนครับ` โมเดลคืนfocus=booking_procedureและC08ถูก แต่runtimeเก็บfocusไว้ในeventเป็นหลัก แล้วreaderรับC08/owner_policyกว้างพร้อมข้อความเดิม จึงentity_not_bound. คำถามcanonicalวิธีจองอ่านsourceได้. เช่นเดียวกับพาเพื่อนมานั่งดู: sourceเจ้าของมีคำตอบแต่paraphraseค้นไม่ถึง','',
'ต้องส่งsemantic predicateที่เฉพาะงานไปถึงreader เช่นbooking.steps/access.spectator แทนเพียงcategory+facetกว้าง แล้วใช้sourceprofileที่ผูกpredicateนั้น. อย่าให้ตัวอ่านต้องเดาเจตนาใหม่จากคำเดิมหลังจ่ายค่าcontextmodelแล้ว','',
'### 3.5 ตัดcandidateก่อนมีความเข้าใจactionเพียงพอ','',
'เคสGodofWarตีแรง: R2/HeavyAttackมีในฐาน แต่scoped_candidatesเลือกtop8เป็นCamera, Move, Map, Sprint, Lock-On, Pause, Block, Aim ไม่มีHeavyAttack. โมเดลเลือกจากตัวเลือกที่ถูกตัดผิด จึงตอบactionอื่น. ข้อความมีsourceจริงไม่ได้พิสูจน์ว่าตรงโจทย์ และคำเตือนpartialไม่ทำให้คำตอบคนละactionถูกต้อง','',
'ต้องวัดcandidate recallก่อนselector ให้semantic action/aliasesผูกกับcurrentbindingในเกม/แพลตฟอร์มที่ถูกต้อง และตรวจrequested action→delivered action. การเพิ่มข้อมูลR2อีกชุดหรือส่งtopKเท่าเดิมไม่แก้สาเหตุนี้','',
'### 3.6 จำนวนคนไม่ได้หาย แต่กฎเลือกservice variantแคบเกินและถามกลับผิดจุด','',
'เคสนักศึกษาPSU1คน+บุคคลทั่วไป2คนเล่นPC2ชั่วโมง: auditพบparsed counts1และ2ถูก แต่มีสองปัญหาร่วมกัน: (1) audience aliasซ้อนทำให้เพิ่มกลุ่มนักศึกษาทั่วไป/ศิษย์เก่าที่ลูกค้าไม่ได้ถาม เพราะกรองlongestmatchเฉพาะภายในrecord ไม่เทียบข้ามaudience (2) PCแบ่ง01–02กับ03–10 ทำให้rateต่อaudienceมี2แถว แต่billingกำหนดlen(selected)==1. ทั้งสองจบด้วยper_audience_counts_or_service_requiredแล้วถามจำนวนคนซ้ำ','',
'ต้องแก้audience matchingที่ซ้อนกันโดยรักษากลุ่มเฉพาะที่ลูกค้าพูดจริง แล้วแยกmissing_personsออกจากservice_variant_ambiguity. เมื่อrate/หน่วย/ช่วงเวลา/audience/กฎคำนวณและeffective scopeเท่ากันจริง ให้ถือเป็นราคาalternativeที่เทียบเท่าและไม่บวกซ้ำ; ถ้าไม่เท่ากันถามเฉพาะvariantที่จำเป็น','',
'### 3.7 ข้อกำหนดtokenที่clientตั้งไว้ไม่ถูกbackendใช้จริง','',
f"ทดสอบส่งnum_predict=1 แต่ได้{option['response']['eval_count']} outputtokens ใช้{option['wall_sec']:.3f}s. โค้ดserve_modelกำหนดmax_new_tokens=850สำหรับcontextและ640สำหรับที่เหลือโดยตรง จึงไม่อ่านnum_predictจากrequest. เปลี่ยนconfigที่clientอย่างเดียวไม่ทำให้จำนวนtokenลดลง",'',
'Backendยังใช้schemaเป็นคำสั่งในprompt ไม่ได้บังคับconstrained decodingจริง. Contextpathเปลี่ยนmessagesเป็นR121 trainingpromptและไม่ใช้format schemaจากcallerในการgenerate. สิ่งนี้เป็นข้อจำกัดprotocol/transport implementation; ในชุดนี้ HTTPสำเร็จไม่ได้พิสูจน์semantics','',
'### 3.8 สภาพเครื่องขณะทดสอบเป็นSilentและGPUทำงานที่clockต่ำ','',
f"Windowsactive scheme=`Silent`; เสียบไฟอยู่. เก็บGPUระหว่างรัน{len(gpu)}ตัวอย่าง: states={gpu_summary['states']}; SM clock{gpu_summary['ranges']['sm_mhz']['min']:.0f}–{gpu_summary['ranges']['sm_mhz']['max']:.0f}MHz, median{gpu_summary['ranges']['sm_mhz']['median']:.0f}MHz; กำลังไฟ{gpu_summary['ranges']['power_w']['min']:.1f}–{gpu_summary['ranges']['power_w']['max']:.1f}W. นี่เป็นสภาพที่วัดได้ ไม่ได้พิสูจน์ว่าเปลี่ยนโหมดจะเร็วขึ้นกี่เท่า",'',
'ต้องA/Bคำถามเดียวกันหลังเปลี่ยนโหมดโดยควบคุมbackend/model/source/temperatureและwarmupจึงระบุผลได้. ยังไม่มีหลักฐานให้สรุปว่าRAM/VRAMไม่พอหรือCPUoffloadเป็นสาเหตุ: โค้ดวางโมเดลบนGPUทั้งหมด และตัวอย่างที่วัดยังมีVRAMเหลือ ไม่มีOOMในชุดนี้','',
'### 3.9 คำถามซ้ำยังจ่ายcontextmodelใหม่','',
f"Englishdateเดิมรอบแรก{by['date_english']['wall_sec']:.3f}s ถามซ้ำ{by['repeat_slow']['wall_sec']:.3f}s. Compoundเดิม{by['booking_compound']['wall_sec']:.3f}s ถามซ้ำ{by['repeat_compound']['wall_sec']:.3f}s. Indexcacheทำงานแต่ไม่มีinterpretationmemoizationที่ทำให้สองเส้นทางนี้ข้ามโมเดล",'',
'หากเพิ่มcacheควรcacheแผนตีความที่ตรวจแล้วและkeyด้วยmodel/wire version/normalized question/locale/resolved date/history scope/sourceepochตามความเกี่ยวข้อง แล้วอ่านfactsใหม่ทุกครั้ง โดยเฉพาะliveไม่cacheคำตอบว่างเป็นข้อเท็จจริงถาวร','',
'### 3.10 แยกต้นทุนฐานข้อมูล/ข้อมูลสด/formatออกจากโมเดล','',
f"ในตัวอย่างdirect GPU query snapshotใช้{by['hardware']['timed_spans']['source.snapshot']:.3f}s, renderer{by['hardware']['timed_spans']['answer.render_one']:.6f}s. LivePC2 provider span{by['live_current']['timed_spans']['provider.fetch']:.3f}s. จึงเป็นคนละปัญหากับ20–74sของmodelpath",'',
f"debugfalse response{debug['rows'][0]['response_bytes']:,}bytes/{debug['rows'][0]['wall_sec']:.3f}s เทียบdebugtrue{debug['rows'][1]['response_bytes']:,}bytes/{debug['rows'][1]['wall_sec']:.3f}s. ลดdebugpayloadมีประโยชน์ต่อขนาดข้อมูล แต่การทดลองนี้ไม่สนับสนุนว่ามันทำให้ช้า20s; ไม่ใช่browserpaintbenchmark",'',
f"ขณะมีคำถามmodelกำลังรัน ถามวันที่แบบdeterministicเพิ่มยังตอบได้{concurrent['wall_sec']:.3f}s. จึงไม่ใช่ว่าทุกเส้นทางของAPIถูกล็อกจนรอโมเดลทั้งหมด",'',
'## 4. ความเสี่ยงจากโค้ดที่ยังไม่ถือว่าพิสูจน์ว่าเกิดในชุดนี้','',
'- GPUmodelserverมีglobal lockหนึ่งตัว; หลายคำขอที่ต้องgenerateจะต้องรอกัน การทดสอบ34ข้อเป็นsequential จึงยังไม่ใช่loadtestพิสูจน์queue time','- Contexttimeout90s/selector60s แต่modelservergenerateไม่เชื่อมกับclientdisconnect; หากclientหมดเวลา งานฝั่งGPUอาจยังทำจนจบแล้วค้างคิวคำขอถัดไป ในชุดนี้ไม่มีtimeoutให้ยืนยันเหตุการณ์นี้','- stream=Falseและserverสร้างresultหลังgenerateจบ; UIรอfinalJSON. Streamingอาจช่วยเวลาที่รู้สึกว่ารอในบางงาน แต่ไม่แก้semanticplan/เวลารวมและไม่ควรส่งsourceanswerก่อนตรวจ','- ยังไม่ได้วัดprefill/firsttoken/decodeแยกกัน และยังไม่ได้เปลี่ยนpower modeหรือbackendทำcausalA/B','',
'## 5. สิ่งที่ควรแก้ตามลำดับ','',
'1. **สัญญาระหว่างmodel→reader:** เก็บintent/action/date/group bindingsไปถึงexecutorจริง หยุดตีด้วยkeywordซ้ำหลังโมเดลรู้เรื่องแล้ว','2. **Completenessของการค้นและเลือก:** แก้candidate recallของcontrols, genericconditionalของpenaltyfamily และcapabilityfilter4playersพร้อมsourceขอบเขตที่ยืนยัน','3. **Structured date/quantity/service normalization:** รองรับEnglishmonths/คำอ่านตัวเลข/nextweekday, แยกaudience countsกับservice variantsและถามเฉพาะสิ่งที่ขาด','4. **ลดgenerationโดยคงความเข้าใจ:** compactintent+slots/spanwire, native readersก่อนselector, cachedvalidated interpretationsที่ไม่cachefactsสด','5. **Backendที่เคารพcontract:** ใช้num_predict/formatจริง มีboundedqueueและcancellation; วัดtransport/protocol/semanticแยก','6. **วัดpower/runtime A/B:** Silentเทียบโหมดทำงานด้วยชุดเดิม ตรวจclock/power/tokens/time ไม่คาดเดาว่าเปลี่ยนแล้วหายทั้งหมด','7. **Gateก่อนใช้จริง:** paraphrase pairs, action recallก่อนtopK, groupquantity/service equivalence, latencyp50/p95ตามจำนวนcalls และsourceedit/withdrawal/livefreshness','',
'สิ่งที่ไม่ควรสรุปจากผลนี้: เติมข้อมูลทั้งหมดอีกครั้งแล้วจะหาย, เปลี่ยนformatแล้วโมเดลจะเร็ว, ลดmax_tokensที่clientอย่างเดียวจะได้ผล, หรือเปลี่ยนGPU/powerแล้วreaderbindingจะถูกเอง','',
'## 6. ผลรายข้อครบ34คำถาม','', '| # | กลุ่ม | เวลา | Model calls / tokens | สถานะ | วิเคราะห์ |','|---:|---|---:|---:|---|---|']
for r in combined:md.append(f"| {r['i']} | {r['category']} | {r['wall_sec']:.3f}s | {r['model_calls']} / {r['generated_tokens']} | {r['outcome']} | {r['review_note']} |")
md += ['', 'สถานะsupported/partial/missing_sourceเป็นสถานะruntime ไม่ใช่semanticgold. ในรายงานนี้แยกวันที่parserไม่ครอบคลุม/แหล่งข้อมูลมีแต่bindingไม่ถึง/เลือกactionผิด/clarificationผิดจุด ออกจากunknownsourceที่ตอบไม่ยืนยันได้อย่างเหมาะสม','',
'## 7. หลักฐาน','',link(R/'ANALYSIS.json','ผลรวมและคำตอบจริงทุกข้อ')+' · '+link(OUT/'TIMINGS.jsonl','spansและHTTP timings')+' · '+link(OUT/'HTTP_RESULTS.jsonl','HTTP responsesจริง'),'',link(R/'SOURCE_COUNTERFACTUALS.json','หลักฐานsource/candidate/rate variants')+' · '+link(R/'ENVIRONMENT.json','powerและGPUที่อ่านจริง')+' · '+link(OUT/'GPU_DURING.jsonl','GPUระหว่างรัน'),'',link(R/'BACKEND_OPTIONS_PROBE.json','num_predict contract probe')+' · '+link(R/'DEBUG_PAYLOAD_PROBE.json','debugpayload probe')+' · '+link(OUT/'CONCURRENT_FAST.json','คำถามเร็วขณะมีงานโมเดล'),'',
f"ตรวจhash code/data R125 {len(freeze)} ไฟล์หลังทดลอง: changed=0. APIผู้ใช้ยังเป็นR125เดิม และไม่มีการฝึกweights/แก้ข้อมูล/approval/ตั้งค่าpowerในรอบวิเคราะห์นี้",'',
'## 8. คำตอบรายข้อเพื่อทบทวน','']
for r in combined:
 md += [f"### {r['i']}. {r['question']}",'',f"{r['wall_sec']:.3f}s · generation={r['model_calls']} · {r['semantic_review_class']}",'',r['review_note'],'','```text',r['answer'],'```','']
(R/'REPORT_TH.md').write_text('\n'.join(md),'utf8')
(R/'STATUS.json').write_text(json.dumps({'status':'analysis_complete','questions':34,'runtime_changed':False,'source_changes':0,'report':str(R/'REPORT_TH.md'),'summary':summary},ensure_ascii=False,indent=2),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
