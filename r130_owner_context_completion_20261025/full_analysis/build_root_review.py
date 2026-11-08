"""Read saved artifacts only; never queries the assistant or edits measured inputs."""
import collections, gzip, json, re, sqlite3, statistics
from pathlib import Path

O = Path(__file__).resolve().parent
R = O.parent
def load(p): return json.loads(p.read_text('utf-8-sig'))
def write(n, v): (O/n).write_text(json.dumps(v, ensure_ascii=False, indent=2), 'utf8')
def lines(p):
    with gzip.open(p, 'rt', encoding='utf8') as f:
        for s in f: yield json.loads(s)

groups = load(O/'FAILURE_GROUPS.json')
selected = {x['key'] for xs in groups['examples'].values() for x in xs}
reason_counts = collections.Counter()
failure_signatures = collections.Counter()
failure_rows = 0
for row in lines(O/'ALL_FAILURES.jsonl.gz'):
    failure_rows += 1
    for reason in row['grade']['failures']: reason_counts[reason] += 1
    sig = (row['category'], *row['groups'])
    failure_signatures[sig] += 1
per_counts = collections.Counter()
per_keys = set()
for row in lines(O/'PER_REQUEST_ANALYSIS.jsonl.gz'):
    assert row['key'] not in per_keys
    per_keys.add(row['key'])
    per_counts.update(row['groups'])
targets = {
 'pc10': lambda q: ('#10' in q or 'pc10' in q or 'pc 10' in q) and ('tekken' in q),
 'president': lambda q: q in ['ใครเป็นประธาน','ใครเป็นประธานศูนย์อีสปอร์ต'],
 'booking_cancel': lambda q: 'จองแล้วไม่สามารถยกเลิก' in q,
 'walkin': lambda q: q in ['ต้องจองล่วงหน้าไหม','เดินเข้าไปใช้บริการเลยได้ไหม หรือต้องจอง?'],
 'games_mis_live': lambda q: 'which game is available in the cockpit' in q,
 'building': lambda q: q in ['อยู่ตึกอะไร ชั้นไหน?','อยู่ตึกอะไร ชั้นไหน'],
 'stream_tournament': lambda q: 'บัคแผนที่' in q and 'สตรีม' in q,
 'unconfirmed_mode': lambda q: 'it takes two' in q and ('คน' in q or 'player' in q),
 'cs2settings': lambda q: 'brightness' in q and 'resolution' in q,
 'tekken_format': lambda q: ('tekken' in q) and ('รูปแบบ' in q or 'format' in q),
}
found = collections.Counter(); category = collections.Counter(); states = collections.Counter()
state_reasons = collections.Counter(); live_reason = collections.Counter(); protocols = collections.Counter()
model_events = collections.Counter(); http = collections.Counter(); latency = []
grade_ids = set(); keys = set(); records = []; sample_sig = collections.Counter(); route_only = 0
with gzip.open(O/'REVIEW_SPECIMENS.jsonl.gz','xt',encoding='utf8') as out:
 for p in sorted((R/'full01').glob('RESULTS_*.jsonl.gz')):
  for row in lines(p):
    key = row['key']; assert key not in keys; keys.add(key)
    result = row.get('result') or {}; a = result.get('decision_artifact') or {}
    c = a.get('execution_contract') or {}; tasks = c.get('tasks',[])
    cats = ','.join(a.get('domain_flow',{}).get('categories',[])) or 'unclassified'
    category[cats] += 1
    failed = [g for g in row['grades'] if not g['passed']]
    if failed and all(all(s.startswith(('route:','intent:')) for s in g['failures']) for g in failed): route_only += 1
    for g in row['grades']:
      identity = (key,g['file'],g['row'],g['variant']); assert identity not in grade_ids; grade_ids.add(identity)
    for t in tasks:
      state = t.get('terminal_state'); states[(cats,state)] += 1
      for code in t.get('reason_codes',[]):
        state_reasons[(state,code)] += 1
        if state == 'provider_unavailable': live_reason[code] += 1
    for e in a.get('domain_flow',{}).get('model_events',[]):
      model_events[(e.get('stage'),e.get('reason'),e.get('transport_ok'),e.get('schema_ok'))] += 1
    for e in row.get('observed_model_http_calls',[]): http[str(e.get('transport_ok'))] += 1
    latency.append(row['elapsed_sec'])
    q=row['question'].casefold()
    matched=[]
    for name,predicate in targets.items():
      if predicate(q) and found[name]<3: matched.append(name);found[name]+=1
    sig=(cats,tuple((t.get('terminal_state'),tuple(t.get('reason_codes',[]))) for t in tasks))
    take=key in selected or bool(matched) or sample_sig[sig]<1
    sample_sig[sig]+=1
    if take:
      small={'key':key,'question':row['question'],'requested_locale':row['requested_locale'],'stratum':row.get('stratum'),
       'elapsed_sec':row['elapsed_sec'],'answer':result.get('answer'), 'route':result.get('route'),
       'query_plan':a.get('query_plan'),'understanding':a.get('understanding'),
       'tasks':tasks,'executor_results':c.get('executor_results'),
       'request_plan':{k:v for k,v in (c.get('request_plan') or {}).items() if k not in ['request_context']},
       'need_results':[{k:v for k,v in n.items() if k not in ['execution_contract']} for n in a.get('need_results',[])],
       'hits':result.get('hits'),'domain_flow':a.get('domain_flow'),
       'observed_model_http_calls':row.get('observed_model_http_calls'),
       'grades':row['grades'],'raw_file':p.name,'targeted':matched}
      out.write(json.dumps(small,ensure_ascii=False)+'\n');records.append(small)
assert keys==per_keys
master=[json.loads(s) for s in (R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl').read_text('utf8').splitlines()]
expected_keys={x['key'] for x in master}
expected_grades={(x['key'],e['file'],e['row'],e['variant']) for x in master for e in x['entries']}
assert expected_keys==keys and expected_grades==grade_ids
latency.sort()
def pairs(c): return [{'signature':k,'count':v} for k,v in c.most_common()]
write('ROOT_REVIEW_STREAM_AUDIT.json',{'raw_requests_read':len(keys),'grades_read':len(grade_ids),'failed_grade_rows_read':failure_rows,
 'per_request_rows_read':len(per_keys),'groups_read':dict(per_counts),'categories':dict(category),
 'state_reasons':pairs(state_reasons),'provider_unavailable_reason_codes':dict(live_reason),
 'model_events':pairs(model_events),'http_calls':dict(http),'failure_reasons':pairs(reason_counts),
 'failure_signatures':pairs(failure_signatures),'category_terminal_states':pairs(states),
 'all_failed_grades_route_intent_only_requests':route_only,'specimens_saved':len(records),'targeted':dict(found),
 'latency':{'median':statistics.median(latency),'p95':latency[int(len(latency)*.95)],'p99':latency[int(len(latency)*.99)],'max':max(latency),'above_10s':sum(v>10 for v in latency),'above_20s':sum(v>20 for v in latency)},
 'exact_key_and_grade_identity_sets_verified':True,'semantic_accuracy':None,'classification_not_semantic_adjudication':True})

con=sqlite3.connect('file:'+str((R/'system/data/knowledge/common.sqlite').resolve()).replace('\\','/')+'?mode=ro',uri=True)
sources={k:json.loads(v) for k,v in con.execute('select source_id,payload from cc_sources')}
heads={k:json.loads(v) for k,v in con.execute('select h.record_id,r.payload from cc_heads h join cc_revisions r on r.record_id=h.record_id and r.version=h.head where h.withdrawn=0')}
write('REVIEW_SOURCE_INDEX.json',{'records':heads,'sources':sources,'read_only_sqlite':True})
print(json.dumps({'keys':len(keys),'grades':len(grade_ids),'failed_grades':failure_rows,'specimens':len(records),'categories':dict(category),'reason_top':reason_counts.most_common(35),'provider_reasons':dict(live_reason),'state_reasons_top':state_reasons.most_common(25),'latency':load(O/'ROOT_REVIEW_STREAM_AUDIT.json')['latency']},ensure_ascii=False))
