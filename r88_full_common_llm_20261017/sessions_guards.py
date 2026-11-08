"""Common/ON session coverage with trusted ID state; guard diagnostics separate."""
import json,multiprocessing as mp,os,sys,time
from pathlib import Path
from types import SimpleNamespace
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R));import run_common as runner
def main():
 os.environ['PSU_R88_RUN_TAG']='sessions';runner.configure('parent')
 from app.pipeline.model_admission import ModelAdmissionBroker
 from app.knowledge.common.dialogue import state_from_answer
 from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
 from tools.eval_contract_v2 import contract_matches
 ctx=mp.get_context('spawn');broker=ModelAdmissionBroker(ctx,limit=1);broker.start();channel=None;conn=None;p=None;sessions=[]
 def stop():
  nonlocal p,conn,channel
  if p is None:return
  if p.is_alive():
   try:conn.send(None)
   except (OSError,EOFError):pass
   p.join(2)
  if p.is_alive():p.terminate();p.join(3)
  conn.close();broker.revoke(channel[2]);p=None
 def start():
  nonlocal p,conn,channel
  channel=broker.register();conn,other=ctx.Pipe();p=ctx.Process(target=runner.child,args=(other,'sessions',channel));p.start();other.close()
  assert conn.poll(90) and conn.recv()['event']=='ready','Session worker not ready'
 try:
  start()
  for entry in json.loads((R/'CORPUS_SESSIONS.json').read_text('utf8')):
   history=[];turns=[];case=entry['case']
   for idx,turn in enumerate(case.get('turns',[])):
    q=turn.get('question') or turn.get('query');locale=turn.get('locale',case.get('locale','auto'))
    job={'key':str(case.get('id'))+':'+str(idx),'question':q,'locale':locale,'reference_date':'','history':history,'entries':[{'file':entry['file'],'row':entry['row'],'variant':'session-'+str(idx),'case':{**turn,'question':q,'locale':locale}}],'r70_stratum':{'domain':'multi_turn','corpus':entry['file'],'locale':locale,'style':'session'}}
    try:
     conn.send(job)
     if not conn.poll(28):raise TimeoutError('Session turn watchdog; no answer was delivered')
     row=conn.recv()['row']
    except Exception as e:
     row={'key':job['key'],'question':q,'requested_locale':locale,'exception':repr(e),'result':{},'grades':[]};stop();start()
    result=row.get('result',{});answer=result.get('answer','');contract=turn.get('answer_contract') or turn;_,errs=contract_matches(answer,contract)
    if row.get('exception'):errs.append('pipeline_exception')
    state=state_from_answer(SimpleNamespace(decision_artifact=result.get('decision_artifact') or {})) or {}
    delivered={'role':'assistant','content':answer,'text':answer,'decision_artifact':result.get('decision_artifact'),'common_read_state':state,'delivery_status':'server_written'}
    history.append({'role':'user','content':q,'text':q})
    if not row.get('exception'):history.append(delivered)
    row.update(turn=idx,literal_passed=not errs,literal_failures=errs,positive_text_contract=any(contract.get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')),delivered_common_state=state);turns.append(row)
    with (R/'SESSION_TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'session_id':case.get('id'),**row},ensure_ascii=False)+'\n')
   sessions.append({'id':case.get('id'),'file':entry['file'],'turns':len(turns),'passed':sum(t['literal_passed'] for t in turns),'positive_text_checked':sum(t['positive_text_contract'] for t in turns),'execution_failures':sum(bool(t.get('exception')) for t in turns)})
 finally:
  stop();broker.stop()
 guard=RuntimeInputQualityGuard.from_environment();guards=[]
 for entry in json.loads((R/'CORPUS_GUARDS.json').read_text('utf8')):
  expected=entry['case'];d=guard.inspect(expected['observed_input'])
  row={'id':expected['id'],'input':expected['observed_input'],'expected':expected,'actual':d.to_public_dict(),'layout_match':('keyboard_layout_mismatch' in d.flags)==expected['should_detect_keyboard_layout'],'repeat_match':('repeated_character_typo' in d.flags)==expected['should_detect_repeated_character'],'legacy_block_policy_match':d.should_short_circuit==expected['should_block_answer']};guards.append(row)
 with (R/'GUARD_RESULTS.json').open('x',encoding='utf8') as f:json.dump(guards,f,ensure_ascii=False,indent=2)
 summary={'sessions':len(sessions),'turns':sum(x['turns'] for x in sessions),'literal_turns_passed':sum(x['passed'] for x in sessions),'positive_text_checked_turns':sum(x['positive_text_checked'] for x in sessions),'execution_failures':sum(x['execution_failures'] for x in sessions),'guard_cases':len(guards),'layout_correct':sum(x['layout_match'] for x in guards),'repeat_correct':sum(x['repeat_match'] for x in guards),'legacy_block_policy_correct':sum(x['legacy_block_policy_match'] for x in guards),'format':'common','llm_enabled':True,'history':'server-written common_read_state IDs, never frozen facts','scope':'engine session continuity; not HTTP persistence/load certification','guard_policy':'warn_and_continue; historical block expectations are diagnostics, not answer correctness','cases':sessions}
 with (R/'SESSION_GUARD_SUMMARY.json').open('x',encoding='utf8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
 print(json.dumps(summary,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
