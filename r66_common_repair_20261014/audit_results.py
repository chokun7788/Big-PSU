"""Read-only post-run audit; original grades are never rewritten."""
import sys,json,collections,sqlite3,zlib,hashlib,math
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1];out=B/('AUDIT_'+tag)
if out.exists() and any(out.iterdir()):raise FileExistsError(out)
out.mkdir(exist_ok=True)
def partition(reason):
 s=str(reason)
 if s.startswith(('route:','route expected','outcome expected','intent:','legacy_mode_prefix:','status:','forbidden_category','route_mismatch','outcome_mismatch','wrong_category','wrong_intent','mode_mismatch')):return 'protocol_outcome'
 if 'source' in s or 'document_id' in s or 'chunk' in s or 'evidence' in s or 'rulebook target' in s:return 'source_alignment'
 if 'first_line' in s or 'heading' in s:return 'presentation'
 if 'latency' in s or 'timeout' in s:return 'performance'
 if 'english_thai_prose' in s:return 'locale_marker'
 if 'validation' in s:return 'validation'
 return 'content_contract'
summary={};failures=[]
for flag in ('off','llm'):
 rows=[json.loads(x) for x in (B/('MATRIX_'+tag+'_'+flag+'.jsonl')).read_text(encoding='utf-8').splitlines() if x.strip()]
 counts=collections.Counter();locales=collections.defaultdict(collections.Counter);reasons=collections.Counter();modes=collections.Counter();transport=[];model=collections.Counter()
 for r in rows:
  counts['requests']+=1;counts['exceptions']+=bool(r.get('exception'));result=r.get('result') or {};modes[result.get('mode','exception')]+=1
  counts['validation_rejected_requests']+=result.get('validation',{}).get('ok') is False
  for g in r.get('grades',[]):
   counts['grades']+=1;counts['strict_pass']+=bool(g['passed']);loc=locales[r['effective_locale']];loc['grades']+=1;loc['strict_pass']+=bool(g['passed'])
   ps=collections.defaultdict(list)
   for why in g.get('failures',[]):ps[partition(why)].append(why);reasons[why]+=1
   if not g['passed']:
    counts['failed_grades']+=1
    for p in ps:counts[p+'_failed_grades']+=1
    if set(ps)=={'protocol_outcome'}:counts['protocol_outcome_only_failed_grades']+=1
    failures.append({'arm':flag,'key':r['key'],'question':r['question'],'locale':r['effective_locale'],'file':g.get('file'),'grade':g,'partitions':dict(ps),'answer':result.get('answer'),'mode':result.get('mode'),'plan':(result.get('decision_artifact') or {}).get('query_plan')})
  for t in result.get('trace',[]):
   if any(k in str(t.get('stage','')).lower() for k in ('llm','semantic','entity')):transport.append({'key':r['key'],'question':r['question'],'trace':t})
  observed={}
  def collect(x):
   if isinstance(x,dict):
    if 'attempted' in x and 'transport_ok' in x:observed[json.dumps(x,sort_keys=True,ensure_ascii=False)]=x
    for v in x.values():collect(v)
   elif isinstance(x,list):
    for v in x:collect(v)
  collect(result)
  for x in observed.values():
   model['trace_observations']+=1
   if x.get('attempted'):
    model['attempted']+=1;model['transport_ok']+=x.get('transport_ok') is True;model['transport_not_ok']+=x.get('transport_ok') is not True
    model['schema_accepted']+=x.get('schema_accepted') is True;model['final_field_plan_accepted']+=x.get('final_plan_accepted') is True
    model['semantic_selection_rejected']+=x.get('semantic_selection_accepted') is False
   else:model['not_attempted_gate']+=1
 times=sorted(r.get('elapsed_wall',0) for r in rows)
 timing={'mean_sec':sum(times)/len(times),'p50_sec':times[math.ceil(.5*len(times))-1],'p95_sec':times[math.ceil(.95*len(times))-1],'max_sec':max(times),'scope':'serialized selected questions on this machine; not a concurrency SLA'}
 summary[flag]={'counts':dict(counts),'locales':{k:dict(v) for k,v in locales.items()},'failure_reasons':reasons.most_common(),'modes':dict(modes),'model_trace_observations':dict(model),'model_count_scope':'deduplicated available trace/decision audit objects; not a complete API traffic counter or correctness score','timing':timing,'elapsed_total':sum(r.get('elapsed_wall',0) for r in rows),'sha256':hashlib.sha256((B/('MATRIX_'+tag+'_'+flag+'.jsonl')).read_bytes()).hexdigest()}
 (out/('MODEL_TRACE_'+flag+'.json')).write_text(json.dumps(transport,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'ALL_FAILED_GRADES.json').write_text(json.dumps(failures,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# รายการ grades ที่ไม่ผ่าน — '+tag,'','แยกตัวตรวจ route/outcome, source identity, presentation, content contract; ชื่อ content contract ไม่ใช่คำตัดสินว่าคำตอบผิดเชิงความหมายทุกข้อ ข้อสอบเดิมอาจอ้างราคา/อายุข้อมูลเก่า ต้องอ่านคู่ source และเวลาอ้างอิง','']
for n,r in enumerate(failures,1):
 md+=['## '+str(n)+'. '+r['arm']+' / '+str(r['file']),'','คำถาม: '+r['question'],'','Locale: '+r['locale']+'; mode: '+str(r['mode'])+'; key: `'+r['key']+'`','', '```json',json.dumps(r['partitions'],ensure_ascii=False,indent=2),'```','','คำตอบจริง:','',str(r['answer']),'','แผนอ่านข้อมูล:','','```json',json.dumps(r['plan'],ensure_ascii=False,indent=2),'```','']
(out/'ALL_FAILED_GRADES.md').write_text('\n'.join(md),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
