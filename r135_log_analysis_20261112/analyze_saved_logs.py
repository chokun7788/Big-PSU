"""Read-only analysis of saved trials; never invokes inference or rescoring."""
import collections,csv,datetime,hashlib,html,json,re,sqlite3,statistics,time
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent
PRIVATE=R/'.local-private';PRIVATE.mkdir(exist_ok=True)
RUNS=[('r135_5pct','r135_eval5_20261107',False),('hybrid48_5pct','r135_hybrid48_20261108/evaluation',False),('hybrid_10pct','r135_hybrid_eval10_20261110/evaluation',True),('bounded_200','r135_bounded_eval200_20261111/evaluation',True),('verified_200','r135_verified_eval200_20261111/evaluation',True)]
reason_keys={'reason','reason_codes','fatal','error','failure_type','rejection_reason'}
skip={'snapshot','knowledge_snapshot','record_revisions','records','source_pairs','input','query_debug','release','facts','sources'}
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
def walk(x,key=''):
 out=set()
 if isinstance(x,dict):
  for k,v in x.items():
   if k not in skip:out|=walk(v,k)
 elif isinstance(x,list):
  for v in x:out|=walk(v,key)
 elif isinstance(x,str) and key in reason_keys and re.fullmatch(r'[a-z][a-z0-9_]{4,}',x):out.add(x)
 return out
def urls(x):
 out=set()
 if isinstance(x,dict):
  for k,v in x.items():
   if k in {'url','source_url','href'} and isinstance(v,str) and v.startswith(('https://','http://')):out.add(v)
   elif isinstance(v,(dict,list)):out|=urls(v)
 elif isinstance(x,list):
  for v in x:out|=urls(v)
 return out
def compact_artifact(a):
 ctx=a.get('request_context') or {};events=ctx.get('events') or []
 calls=[]
 for e in events:
  if isinstance(e,dict) and any(term in str(e.get('stage','')).lower() for term in ['gateway','admission']):
   calls.append({k:e[k] for k in ['stage','model_stage','transport_ok','accepted','reason','error','error_type','elapsed_seconds','elapsed_ms'] if k in e})
 audits=[{k:x[k] for k in ['stage','attempted','accepted','reason','error_type','body_received','elapsed_ms'] if k in x} for x in ctx.get('audits',[]) if isinstance(x,dict)]
 flow=a.get('flow_audit') or {};issues=flow.get('issues') or []
 return {'reason_codes':sorted(walk(a)),'flow_issues':issues,'model_calls':calls,'model_audits':audits,'model_counters':{k:ctx.get(k) for k in ['semantic_attempts','model_calls_reserved','model_calls_attempted','model_calls_transport_completed','corrective_reads']},'artifact_response_type':a.get('response_type'),'claim_packets_count':len(a.get('claim_packets') or []),'need_statuses':[{'task':n.get('task'),'status':n.get('status'),'terminal_state':n.get('terminal_state'),'reason_codes':n.get('reason_codes',[])} for n in a.get('need_results',[]) if isinstance(n,dict)]}
summaries={};items=[];inputs=[]
for name,relative,traces in RUNS:
 folder=ROOT/relative;p=folder/'RESULTS.jsonl';raw=[json.loads(line) for line in p.open(encoding='utf8') if line.strip()]
 times=[];modes=collections.Counter();reasons=collections.Counter();stages=collections.Counter();errors=collections.Counter();langs=collections.Counter();categories=collections.Counter();availability=collections.Counter();missing=[];trace_found=0
 db=folder/'runtime/logs/transcripts.sqlite';conn=sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True) if traces else None
 for j,row in enumerate(raw):
  response=row.get('response') or {};q=row.get('question','');answer=response.get('answer','');seconds=float(row.get('elapsed_seconds') or 0);times.append(seconds)
  mode=response.get('mode','');modes[mode]+=1;langs[row.get('locale','')]+=1;categories[str(response.get('route_category'))]+=1
  source_urls=sorted(urls(response.get('sources',[])));x={'run':name,'key':row.get('key'),'question':q,'answer':answer,'locale':row.get('locale'),'mode':mode,'seconds':seconds,'transport_ok':row.get('transport_ok'),'http_status':row.get('http_status'),'outer_timed_out':response.get('timed_out'),'route_category':response.get('route_category'),'route_intent':response.get('route_intent'),'public_source_urls':source_urls,'response_sources_count':len(response.get('sources') or []),'trace_analyzed':False}
  if conn:
   found=conn.execute("SELECT metadata_json FROM chat_messages WHERE session_id=? AND role='assistant' ORDER BY id DESC LIMIT 1",(row.get('session_id'),)).fetchone()
   if found:
    a=load_json=json.loads(found[0] or '{}');a=a.get('decision_artifact') or {};x.update(compact_artifact(a));x['trace_analyzed']=True;trace_found+=1
    reasons.update(x['reason_codes']);stages.update({str(z.get('first_stage')) for z in x['flow_issues'] if isinstance(z,dict) and z.get('first_stage')})
    errtags=set()
    for event in x['model_calls']+x['model_audits']:
     err=str(event.get('error') or event.get('error_type') or '')
     if err:
      if 'TimeoutError' in err or 'timed out' in err:errtags.add('explicit_timeout_recorded')
      elif 'admission' in err.lower():errtags.add('explicit_admission_error_recorded')
      else:errtags.add('other_model_error_recorded')
     if event.get('transport_ok') is True:errtags.add('gateway_transport_success_recorded')
     if event.get('transport_ok') is False:errtags.add('gateway_transport_failure_recorded')
    x['model_event_flags']=sorted(errtags);errors.update(errtags)
   else:missing.append(row.get('key'))
  flags=[]
  if 'unavailable' in mode:flags.append('unavailable_status')
  if 'partial_answer' in mode:flags.append('partial_status_not_automatically_wrong')
  if 'clarification' in mode:flags.append('clarification_status')
  if 'unconfirmed' in mode or 'not_current' in mode:flags.append('unconfirmed_or_not_current_status')
  if seconds>60:flags.append('over60s')
  if seconds>120:flags.append('over120s')
  if not source_urls:flags.append('no_public_url_in_sources_not_proof_of_missing_evidence')
  if re.search(r'validity|ช่วง.*มีผล|วันเริ่ม|วันสิ้นสุด|current permission|not.*current',answer,re.I):flags.append('validity_wording_present_review_needed')
  if re.search('[\u0600-\u06ff]',answer):flags.append('arabic_characters_in_answer_review_needed')
  x['review_flags']=flags;items.append(x)
  if (j+1)%250==0:print(json.dumps({'run':name,'rows_analyzed':j+1}),flush=True)
 if conn:conn.close()
 keycounts=collections.Counter(x.get('key') for x in raw)
 summary={'requests':len(raw),'unique_keys':len(keycounts),'duplicate_rows':sum(v-1 for v in keycounts.values()),'transport_ok':sum(x.get('transport_ok') is True for x in raw),'http_200':sum(x.get('http_status')==200 for x in raw),'outer_timed_out':sum((x.get('response') or {}).get('timed_out') is True for x in raw),'modes':dict(modes.most_common()),'locales':dict(langs),'route_categories':dict(categories),'timing':{'sum_seconds':sum(times),'mean_seconds':statistics.mean(times),'median_seconds':statistics.median(times),'p95_seconds':sorted(times)[max(0,int(len(times)*.95)-1)],'max_seconds':max(times),'over20':sum(t>20 for t in times),'over60':sum(t>60 for t in times),'over120':sum(t>120 for t in times)},'trace_analysis_requested':traces,'trace_matches':trace_found,'trace_missing_keys':missing,'recorded_reasons_per_request_nonexclusive':dict(reasons.most_common()),'recorded_first_stages_per_request_nonexclusive':dict(stages.most_common()),'recorded_model_event_flags_nonexclusive':dict(errors.most_common()),'flags_per_request_nonexclusive':dict(collections.Counter(f for x in items if x['run']==name for f in x['review_flags']).most_common())}
 for filename in ['SCORES_LITERAL.json','SCORES_COMPARISON.json']:
  if (folder/filename).exists():summary['saved_score_file']=str((folder/filename).relative_to(ROOT));summary['saved_scores_unchanged']=load(folder/filename)
 # Old 5% keeps scores at the root, new ones in evaluation.
 summaries[name]=summary;inputs.append({'path':str(p.relative_to(ROOT)),'sha256':digest(p),'rows':len(raw),'bytes':p.stat().st_size,'trace_database':str(db.relative_to(ROOT)) if traces else None,'trace_mode':'SQLite read-only, session matched latest assistant' if traces else 'not analyzed; historical response summary only'})
 print(json.dumps({'run':name,'finished':len(raw),'trace_matches':trace_found}),flush=True)
(R/'SUMMARY.json').write_text(json.dumps({'created_at_bangkok':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat(),'runs':summaries,'total_saved_response_rows':len(items),'unique_question_keys_across_runs':len({x['key'] for x in items}),'no_new_inference_or_scoring':True,'all_rows_machine_inspected_not_all_human_semantically_accepted':True},ensure_ascii=False,indent=2),encoding='utf8')
(PRIVATE/'QUESTION_AUDIT.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in items),encoding='utf8')
with (PRIVATE/'QUESTION_AUDIT.csv').open('w',encoding='utf-8-sig',newline='') as f:
 writer=csv.writer(f);writer.writerow(['run','key','question','answer','mode','seconds','public_urls','recorded_reasons','review_flags'])
 for x in items:writer.writerow([x['run'],x['key'],x['question'],x['answer'],x['mode'],x['seconds'],' | '.join(x['public_source_urls']),' | '.join(x.get('reason_codes',[])),' | '.join(x['review_flags'])])
# Standalone local viewer; no remote scripts, API calls, or raw metadata exposure.
payload=json.dumps(items,ensure_ascii=False).replace('</',r'<\/')
viewer='''<!doctype html><html lang="th"><meta charset="utf-8"><title>PSU saved-log analysis</title><style>body{font:16px system-ui;margin:24px;background:#f5f7fa;color:#172031}input,select,button{padding:10px;margin:5px}article{background:white;padding:18px;margin:12px 0;border-radius:10px}pre{white-space:pre-wrap;overflow-wrap:anywhere}.bad{color:#ab2525}.meta{font-size:13px;color:#516176}summary{cursor:pointer}#pages{position:sticky;top:0;background:#f5f7fa;padding:6px}</style><h1>รายงานคำถามและคำตอบจาก log ที่เซฟไว้</h1><p>ข้อมูลท้องถิ่น: สถานะ/flags ไม่ใช่ข้อสรุปความถูกต้องทางความหมาย ไม่มีการเรียกโมเดลหรือให้คะแนนใหม่</p><div id="pages"><select id="run"><option value="">ทุกรุ่น</option></select><select id="flag"><option value="">ทุกสถานะ</option></select><input id="search" placeholder="ค้นคำถาม คำตอบ หรือ reason" size="45"><button id="prev">ก่อนหน้า</button><button id="next">ถัดไป</button><span id="count"></span></div><main id="rows"></main><script>const data=PAYLOAD;let page=0;const $=s=>document.getElementById(s);const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));for(const v of [...new Set(data.map(x=>x.run))])$('run').add(new Option(v,v));for(const v of [...new Set(data.flatMap(x=>x.review_flags))].sort())$('flag').add(new Option(v,v));function render(){const q=$('search').value.toLowerCase();const rows=data.filter(x=>(!$('run').value||x.run===$('run').value)&&(!$('flag').value||x.review_flags.includes($('flag').value))&&(!q||JSON.stringify(x).toLowerCase().includes(q)));page=Math.max(0,Math.min(page,Math.ceil(rows.length/30)-1));$('count').textContent=` ${rows.length} รายการ / หน้า ${page+1}`;$('rows').innerHTML=rows.slice(page*30,page*30+30).map(x=>`<article><b>${esc(x.question)}</b><p class="meta">${esc(x.run)} · ${esc(x.mode)} · ${x.seconds}s · key ${esc(x.key)}</p><pre>${esc(x.answer)}</pre><details><summary>flags / เหตุผลที่บันทึก / หลักฐาน</summary><pre>${esc(JSON.stringify({flags:x.review_flags,reasons:x.reason_codes,flow:x.flow_issues,model_calls:x.model_calls,model_audits:x.model_audits,source_urls:x.public_source_urls},null,2))}</pre></details></article>`).join('')};for(const id of ['run','flag','search'])$(id).oninput=()=>{page=0;render()};$('prev').onclick=()=>{page--;render()};$('next').onclick=()=>{page++;render()};render();</script></html>'''.replace('PAYLOAD',payload)
(PRIVATE/'RESULTS_ANALYSIS_VIEW.html').write_text(viewer,encoding='utf8')
(R/'INPUT_MANIFEST.json').write_text(json.dumps({'inputs':inputs,'read_only':True,'raw_metadata_not_copied':True,'inference_calls':0,'rescoring':False,'private_outputs':['.local-private/QUESTION_AUDIT.jsonl','.local-private/QUESTION_AUDIT.csv','.local-private/RESULTS_ANALYSIS_VIEW.html']},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'finished':True,'total_rows':len(items),'runs':list(summaries)}),flush=True)
