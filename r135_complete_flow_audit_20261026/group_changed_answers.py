"""Build a lossless review queue from saved R132 answers; never grade them."""
import collections,gzip,hashlib,json,pathlib,re,time
R=pathlib.Path(__file__).resolve().parent;W=R.parent; source=W/'r132_flow_repairs_20261025/sample_analysis/ANSWER_CHANGES_REVIEW_REQUIRED.json'
rows=json.loads(source.read_text(encoding='utf-8'));keys={r['key'] for r in rows};results={};files=[]
for path in sorted((W/'r132_flow_repairs_20261025/sample01').glob('RESULTS*.jsonl.gz')):
 files.append({'path':str(path.relative_to(W)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 with gzip.open(path,'rt',encoding='utf-8') as f:
  for line in f:
   r=json.loads(line);k=r.get('key')
   if k in keys:
    if k in results:raise ValueError('duplicate result key '+k)
    hits=r.get('result',{}).get('hits',[])
    results[k]={'result_file':str(path.relative_to(W)),'elapsed_sec':r.get('elapsed_sec'),'source_refs':sorted({(h.get('record_id',''),h.get('field',''),h.get('source_id',''),h.get('locator','')) for h in hits})}
def group(r):
 old=r.get('old','');new=r.get('new','')
 lines=lambda s:collections.Counter(x.strip() for x in s.splitlines() if x.strip())
 if lines(old)==lines(new):return 'same_nonempty_lines_reordered'
 if re.search(r'cannot be confirmed|unavailable|ตรวจสอบไม่ได้|ไม่สามารถตรวจสอบ',old,re.I):return 'previous_unavailable_or_unconfirmed'
 if re.search(r'applicability|ยังยืนยันไม่ได้ว่าอัตรา|มีผล.*ยืนยัน|effective interval',new,re.I):return 'new_temporal_or_validity_wording'
 return 'other_changed_content'
O=R/('changed_answer_group_queue_'+str(time.time_ns()));O.mkdir();counts=collections.Counter();categories=collections.Counter();missing=[]
with (O/'ITEMS.jsonl').open('w',encoding='utf-8') as f:
 for r in rows:
  k=r['key'];item={**r,'candidate_group':group(r),'original_result':results.get(k),'review_state':'review_required'}
  if k not in results:missing.append(k)
  counts[item['candidate_group']]+=1
  for c in r.get('categories',[]):categories[c]+=1
  f.write(json.dumps(item,ensure_ascii=False)+'\n')
report={'source_path':str(source.relative_to(W)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'result_files':files,'items':len(rows),'unique_keys':len(keys),'matched_original_results':len(results),'missing_original_result_keys':missing,'candidate_group_counts':dict(counts),'category_counts_nonexclusive':dict(categories),'limitations':'Grouping is only a review queue: no semantic review, accuracy grade, root-cause conclusion, model inference, R132 regrade or proof of category completion. Same lines do not prove factual correctness.'}
(O/'REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'path':str(O),'items':len(rows),'matched':len(results),'groups':dict(counts),'missing':len(missing)}));assert len(rows)==len(keys) and not missing
