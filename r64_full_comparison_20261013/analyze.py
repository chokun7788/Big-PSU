import collections,json,gzip,zlib,codecs
from pathlib import Path
B=Path(__file__).resolve().parent
CUTOFFS={}
def read(path):
 limit=CUTOFFS.get(str(path),path.stat().st_size)
 if path.suffix=='.gz':
  decoder=codecs.getincrementaldecoder('utf-8')();decompressor=zlib.decompressobj(31);pending=''
  with path.open('rb') as stream:
   while stream.tell()<limit and (chunk:=stream.read(min(65536,limit-stream.tell()))):
    pending+=decoder.decode(decompressor.decompress(chunk));lines=pending.split('\n');pending=lines.pop()
    for line in lines:
     try:yield json.loads(line)
     except ValueError:pass
 else:
  with path.open('rb') as stream:
   while stream.tell()<limit:
    line=stream.readline(limit-stream.tell())
    if not line.endswith(b'\n'):break
    try:yield json.loads(line)
    except ValueError:pass
def bucket(s):
 if 'ownership_blocked' in s or 'pipeline_exception' in s or 'worker_error' in s:return 'runtime_exception'
 if 'watchdog' in s or 'timeout' in s or s=='latency_ceiling':return 'deadline_or_performance'
 if any(x in s for x in ['english_thai','Thai prose','localization']):return 'language_or_translation'
 if s.startswith(('route:','intent:','legacy_mode_prefix:','status:')) or s in ['wrong_category','wrong_outcome']:return 'route_mode_or_outcome_contract'
 if any(x in s for x in ['source','target','evidence']):return 'target_or_source_grounding'
 if any(x in s for x in ['missing','required','clause','coverage']):return 'missing_requested_content'
 if any(x in s for x in ['forbidden','off_topic']):return 'wrong_or_extra_content'
 if 'validation' in s:return 'internal_validation_rejected'
 return 'other_contract_failure'
def main():
 report={};samples=[]
 for arm,paths in [(m+'_offline',[B/(m+'_offline')/'RESULTS.jsonl',B/(m+'_offline_resumed')/'RESULTS.jsonl',B/(m+'_bounded')/'RESULTS.jsonl']+sorted(B.glob(m+'_bounded_*/RESULTS.jsonl'))) for m in ['legacy','common']]+[(m+'_llm',[B/'model_matrix'/(m+'_RESULTS.jsonl.gz')]+sorted(B.glob('model_matrix_*/'+m+'_RESULTS.jsonl.gz'))) for m in ['legacy','common']]:
  counts=collections.Counter();bylang=collections.defaultdict(collections.Counter);categories=collections.Counter();seen=set();bycorpus=collections.defaultdict(collections.Counter);model_audit=collections.Counter()
  for path in paths:
   if not path.exists():continue
   for r in read(path):
    if r['key'] in seen:continue
    seen.add(r['key']);lang=r.get('effective_locale',r.get('requested_locale','auto'));counts['requests']+=1
    if 'exception' in r:counts['runtime_exceptions']+=1
    for t in r.get('result',{}).get('trace',[]):
     if t.get('stage')=='common_query_planner':
      for a in t.get('metadata',{}).get('attempts',[]):
       model_audit['audit_events']+=1
       for k in ('attempted','transport_ok','schema_accepted','final_plan_accepted'):
        if a.get(k) is True:model_audit[k]+=1
       if a.get('error_type'):model_audit['error:'+a['error_type']]+=1
       if a.get('gate_reason'):model_audit['gate:'+a['gate_reason']]+=1
    for g in r.get('grades',[]):
     counts['grades']+=1;counts['passed']+=g['passed'];bylang[lang]['total']+=1;bylang[lang]['passed']+=g['passed'];bycorpus[g['file']]['total']+=1;bycorpus[g['file']]['passed']+=g['passed'];counts['content_asserted']+=g.get('content_asserted',False);counts['content_passed']+=g.get('content_checks_passed') is True
     detail=g.get('grader_detail') or {};positive=detail.get('positive_content_asserted') is True or g.get('evidence_level') in {'complete_clause_content','complete_clause_composition','competition_legacy_evidence','native_answer_quality'}
     counts['positive_content_asserted']+=positive;counts['positive_content_passed']+=positive and g.get('content_checks_passed') is True
     for reason in g.get('failures',[]):categories[bucket(reason)]+=1
     if not g['passed'] and len([s for s in samples if s['arm']==arm])<30:
      samples.append({'arm':arm,'question':r['question'],'locale':lang,'corpus':g['file'],'row':g['row'],'failures':g['failures'],'answer':r.get('result',{}).get('answer'),'decision':r.get('result',{}).get('decision_artifact'),'exception':r.get('exception')})
  report[arm]={'counts':counts,'by_language':dict(bylang),'failure_buckets':categories,'by_corpus':dict(bycorpus),'common_planner_model_audit':model_audit,'complete':counts['requests']==20554 and counts['grades']==55811}
 (B/'ANALYSIS_LATEST.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');(B/'FAILURE_SAMPLES_LATEST.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({k:{'counts':v['counts'],'complete':v['complete']} for k,v in report.items()},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
