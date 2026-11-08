import collections,json,re,sqlite3,zlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;O=BASE/'r65_detailed_failure_analysis_20261014';B=BASE/'r64_full_comparison_20261013'
c=sqlite3.connect(O/'evidence.sqlite');c.row_factory=sqlite3.Row
def kind(s):
 if 'grader_exception' in s:return 'grader_error'
 if s=='pipeline_exception' or s.startswith('worker_error'):return 'runtime'
 if s=='latency_ceiling' or 'watchdog' in s or 'timeout' in s or s.startswith('latency '):return 'deadline'
 if s.startswith(('route:','route expected','route ','intent:','intent ','legacy_mode_prefix:','forbidden_category')) or s in {'wrong_category','wrong_intent'}:return 'protocol'
 if s.startswith(('status:','status expected','outcome expected','outcome ')) or s=='wrong_outcome':return 'outcome'
 if 'validation' in s:return 'validation'
 if any(w in s for w in ('english_thai','Thai prose','localization')):return 'language'
 if any(w in s for w in ('source','target','evidence')):return 'source_target'
 if any(w in s for w in ('forbidden','off_topic')):return 'forbidden_content'
 if any(w in s for w in ('missing','required','clause','coverage','alternatives')):return 'missing_content'
 return 'other'
stats={};reason_samples={};oracle={};native={}
for arm in ('legacy_offline','common_offline','legacy_llm','common_llm'):
 counts=collections.Counter();reasons=collections.Counter();combos=collections.Counter();per_issue=collections.Counter();exceptions=collections.Counter()
 rows=c.execute('SELECT rowid,* FROM grades WHERE arm=?',(arm,)).fetchall()
 for g in rows:
  rs=json.loads(g['reasons_json']);issues=set(kind(s) for s in rs);counts['grades']+=1;counts['strict_pass']+=g['passed']
  if not rs:counts['no_failure_recorded']+=1
  else:
   counts['failed']+=1;combos[','.join(sorted(issues))]+=1
   if issues<={'protocol'}:counts['protocol_only_failure']+=1
   if issues<={'protocol','outcome'}:counts['protocol_or_outcome_only_failure']+=1
   if issues<={'deadline'}:counts['deadline_only_failure']+=1
   if issues&{'missing_content','source_target','language','forbidden_content','validation','other'}:counts['content_or_gate_failure']+=1
  for k in issues:per_issue[k]+=1
  for s in rs:
   reasons[s]+=1
   if kind(s) not in reason_samples:reason_samples[kind(s)]={'arm':arm,'key':g['key'],'file':g['file'],'row':g['rownum'],'reason':s}
  revised=','.join(sorted(issues))
  if revised!=g['issues']:c.execute('UPDATE grades SET issues=? WHERE rowid=?',(revised,g['rowid']))
 for x in c.execute('SELECT exception,COUNT(*) n FROM results WHERE arm=? AND exception IS NOT NULL GROUP BY exception',(arm,)):exceptions[x['exception']]=x['n']
 stats[arm]={'counts':counts,'failure_combinations':combos,'grades_affected_by_issue':per_issue,'exact_reasons':reasons,'exceptions_by_message':exceptions,'failed_unique_requests':c.execute('SELECT COUNT(DISTINCT key) FROM grades WHERE arm=? AND passed=0',(arm,)).fetchone()[0]}
 c.commit()
for e in c.execute('SELECT * FROM expected'):
 q=json.loads(e['case_json']);contract=q.get('answer_contract') or {k:q[k] for k in ('must_contain','must_contain_any','must_not_contain') if k in q}
 positives=bool(contract.get('must_contain') or contract.get('must_contain_any') or contract.get('must_contain_all_groups') or q.get('required_clauses') or (q.get('clauses') and q.get('sources')) or ('source_keywords' in q and 'min_score' in q))
 k='positive_text_or_clause' if positives else 'evidence_id_only' if 'expected_game_id' in q else 'negative_only' if contract.get('must_not_contain') else 'route_outcome_only'
 oracle[k]=oracle.get(k,0)+1
 if q.get('must_contain_all_groups') and not q.get('answer_contract'):oracle['top_level_all_groups_ignored_by_adapter']=oracle.get('top_level_all_groups_ignored_by_adapter',0)+1
 for field in ('expected_answer','answer_th','answer_en','expected_response','reference_answer'):
  if q.get(field) and not positives:oracle['reference_text_not_asserted:'+field]=oracle.get('reference_text_not_asserted:'+field,0)+1
for mode in ('legacy','common'):
 d=json.loads((B/(mode+'_test_all.py_temp_fixed.json')).read_text(encoding='utf-8'))
 funcs=set();err=collections.Counter()
 for typ in ('failures','errors'):
  for name,trace in d[typ]:
   funcs.add(name.split(')')[0]+')');err[trace.strip().splitlines()[-1][:200]]+=1
 native[mode]={'tests_run':d['tests'],'failure_events':len(d['failures']),'error_events':len(d['errors']),'affected_functions':len(funcs),'unaffected_functions':d['tests']-len(funcs),'assertion_or_error_tail_counts':err}
out={'arms':stats,'oracle_inventory_per_arm':oracle,'native':native,'reason_samples':reason_samples,'coverage':{'results':c.execute('SELECT COUNT(*) FROM results').fetchone()[0],'grades':c.execute('SELECT COUNT(*) FROM grades').fetchone()[0],'expected':c.execute('SELECT COUNT(*) FROM expected').fetchone()[0]},'classification_revision':'handles native route expected/outcome expected/latency strings missed by R64 content partition; original grades untouched'}
(O/'METRICS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'coverage':out['coverage'],'oracle':oracle,'arms':{a:{'counts':v['counts'],'exceptions':v['exceptions_by_message'],'top_reasons':v['exact_reasons'].most_common(9)} for a,v in stats.items()},'native_counts':{a:{k:v for k,v in d.items() if k!='assertion_or_error_tail_counts'} for a,d in native.items()}},ensure_ascii=False,indent=2))
c.close()
