"""Preserve run01 and create a runner with robust status writes/cache resume."""
from pathlib import Path
R=Path(__file__).resolve().parent
x=(R/'train_planner.py').read_text('utf8')
x=x.replace("parser.add_argument('--run',default='train01')", "parser.add_argument('--run',default='train02')")
old="tmp=OUT/'progress.new';tmp.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8');os.replace(tmp,OUT/'PROGRESS.json')"
new="""tmp=OUT/('progress_'+str(time.time_ns())+'.json');tmp.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
 # Status telemetry must never abort GPU work because Windows holds a reader.
 for attempt in range(8):
  try:os.replace(tmp,OUT/'PROGRESS.json');break
  except PermissionError:time.sleep(.05*(attempt+1))
 with (OUT/'STATUS_JOURNAL.jsonl').open('a',encoding='utf8') as journal:journal.write(json.dumps(v,ensure_ascii=False)+'\\n')"""
assert old in x;x=x.replace(old,new)
x=x.replace("for i,x in enumerate(xs):\n    before=", """for i,x in enumerate(xs):
    if name=='baseline_test' and x['key'] in CACHED_BASELINE:
     row=CACHED_BASELINE[x['key']];assert row['question']==x['question'] and row['adapter_disabled'] is True
     result.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\\n');f.flush();continue
    before=""")
x=x.replace("'train_planner.py','planner_metrics.py'", "Path(__file__).name,'planner_metrics.py'")
x=x.replace("infer_set(model,tok,test,'baseline_test',True)", """prior=R/'train01';prior_freeze=json.loads((prior/'RUN_FREEZE.json').read_text('utf8'))
 assert all(sha(p)==h for p,h in prior_freeze.items()),'Earlier baseline source/data changed'
 assert not (prior/'OPTIMIZATION_PROOF.json').exists() and not (prior/'TRAINING_LOSS.jsonl').exists(),'Prior run had optimization'
 cached=list(map(json.loads,(prior/'baseline_test.jsonl').open(encoding='utf8')))
 assert len(cached)==len({r['key'] for r in cached}) and [r['key'] for r in cached]==[t['key'] for t in test[:len(cached)]]
 CACHED_BASELINE={r['key']:r for r in cached}
 write('BASELINE_RESUME.json',{'source':str(prior),'cached_rows':len(cached),'source_hashes_verified':True,'raw_results_sha256':sha(prior/'baseline_test.jsonl'),'reason':'run01 Windows status-file replacement error before optimization','training_configuration_changed':False})
 infer_set(model,tok,test,'baseline_test',True)""")
target=R/'train_planner02.py';assert not target.exists();target.write_text(x,'utf8')
print('run02 source created; run01 unchanged')
