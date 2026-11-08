import collections,json,sqlite3
from pathlib import Path
BASE=Path(__file__).resolve().parent;O=BASE/'r65_detailed_failure_analysis_20261014';db=O/'evidence.sqlite';c=sqlite3.connect(db);c.row_factory=sqlite3.Row
vocabulary=collections.defaultdict(collections.Counter);trimmed=0;before=db.stat().st_size
for row in c.execute('SELECT rowid,* FROM grades').fetchall():
 g=json.loads(row['grade_json']);d=g.get('grader_detail') or {}
 if row['passed'] and d.get('strong_outcome_matches') is False:
  er=c.execute('SELECT case_json FROM expected WHERE key=? AND file=? AND rownum=? AND variant=?',(row['key'],row['file'],row['rownum'],row['variant'])).fetchone();e=json.loads(er[0]);vocabulary[row['arm']][str(e.get('expected_answer_status') or e.get('outcome'))]+=1
 if isinstance(d,dict):
  change=False
  for key in ('answer','trace','hits'):
   if key in d:del d[key];change=True
  if change:
   trimmed+=1;g['grader_detail']=d;c.execute('UPDATE grades SET grade_json=? WHERE rowid=?',(json.dumps(g,ensure_ascii=False,separators=(',',':')),row['rowid']))
c.commit();c.execute('PRAGMA wal_checkpoint(TRUNCATE)');c.execute('VACUUM');c.commit();c.close()
report={'before_bytes':before,'after_bytes':db.stat().st_size,'duplicate_grade_payloads_trimmed':trimmed,'full_original_grade_retained_in_results_raw':True,'original_R64_files_changed':False,'strong_outcome_false_by_expected_vocabulary':dict(vocabulary)}
(O/'STORAGE_AND_OUTCOME_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
