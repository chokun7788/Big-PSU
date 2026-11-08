"""Independent saved-output and frozen-file checks; no test execution."""
import collections,gzip,hashlib,json,time
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent
def load(p):return json.loads(p.read_text('utf-8-sig'))
freeze=load(R/'EXECUTION_FREEZE_R130.json');changed=[]
for name,expected in freeze.items():
 p=Path(name)
 if not p.exists():changed.append({'path':name,'missing':True});continue
 with p.open('rb') as f:actual=hashlib.file_digest(f,'sha256').hexdigest()
 if actual!=expected:changed.append({'path':name,'expected':expected,'actual':actual})
before=load(R/'MODEL_IDENTITY_BEFORE.json');after=load(R/'MODEL_IDENTITY_AFTER.json')
counts=collections.Counter();errors=[];live=collections.Counter();admission=collections.Counter();calls=collections.Counter()
for p in sorted((R/'full01').glob('RESULTS_*.jsonl.gz')):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for line in f:
   row=json.loads(line);a=(row.get('result') or {}).get('decision_artifact') or {};context=a.get('request_context') or {}
   for event in context.get('events',[]):
    if event.get('stage')!='R129_model_gateway':continue
    counts['gateway_events']+=1
    if not event.get('transport_ok'):continue
    counts['gateway_successes']+=1;p=event.get('returned_provenance') or {}
    stage=event.get('model_stage');profile='retained' if stage=='context_understanding' else 'base'
    checks={'profile':p.get('effective_profile')==profile,'adapter':p.get('adapter_sha256')==after['profiles'][profile],
     'profile_digest':p.get('profile_digest')==after['profile_digests'][profile],
     'base':p.get('base_revision')==after['base_revision'],'precision':p.get('quantization')==after['quantization'],
     'messages':p.get('effective_messages_sha256')==event.get('wire_messages_sha256'),
     'schema':p.get('effective_schema_sha256')==event.get('schema_sha256'),
     'stage':p.get('stage')==stage,'model':event.get('model')==after['model']}
    counts['verified_'+profile]+=int(all(checks.values()))
    if not all(checks.values()):errors.append({'key':row['key'],'checks':checks})
   artlive=a.get('live_booking')
   if artlive:
    live['requests_with_live_booking_artifact']+=1
    live[str(artlive.get('status'))]+=1
   for t in (a.get('execution_contract') or {}).get('tasks',[]):
    if t.get('terminal_state')=='provider_unavailable':
     reasons=t.get('reason_codes') or []
     live['provider_unavailable_tasks']+=1
     live['model_coded_tasks' if reasons else 'without_reason_code_tasks']+=1
   for e in (a.get('domain_flow') or {}).get('model_events',[]):
    if e.get('error'):admission[str(e['error'])]+=1
   for c in row.get('observed_model_http_calls',[]):
    calls['actual_http_attempts']+=1;calls['actual_http_successes']+=int(c['transport_ok'])
    if not c['transport_ok']:calls['error:'+str(c.get('error_type'))]+=1
report={'checked_at_unix':time.time(),'frozen_files_checked':len(freeze),'changed_or_missing_files':changed,
 'model_before_after_identity_equal':before==after,'profile_and_adapter_identity_equal':before['profiles']==after['profiles'] and before['profile_digests']==after['profile_digests'],
 'logical_source_before_after_equal':load(R/'SOURCE_SNAPSHOT_BEFORE.json')==load(R/'SOURCE_SNAPSHOT_AFTER.json'),
 'actual_successful_gateway_provenance':dict(counts),'provenance_errors':errors,'live_and_model_unavailability_split':dict(live),
 'actual_http':dict(calls),'model_event_errors':dict(admission),'no_assistant_queries_executed':True}
assert not changed and not errors and report['profile_and_adapter_identity_equal'] and report['logical_source_before_after_equal']
(O/'INDEPENDENT_COMPLETION_VERIFICATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(report,ensure_ascii=False))
