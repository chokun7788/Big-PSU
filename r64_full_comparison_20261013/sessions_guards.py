import collections,dataclasses,json,sys,time
from pathlib import Path
import harness
B=Path(__file__).resolve().parent
def main():
 mode=sys.argv[1];harness.init(mode,False)
 from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
 guard=RuntimeInputQualityGuard.from_environment();rows=[]
 for c in json.loads((B/'GUARDS.json').read_text(encoding='utf-8')):
  expected=c['case'];d=guard.inspect(expected['observed_input'])
  rows.append({'id':expected['id'],'input':expected['observed_input'],'expected':expected,'actual':d.to_public_dict(),'layout_match':('keyboard_layout_mismatch' in d.flags)==expected['should_detect_keyboard_layout'],'repeat_match':('repeated_character_typo' in d.flags)==expected['should_detect_repeated_character'],'legacy_block_policy_match':d.should_short_circuit==expected['should_block_answer']})
 (B/(mode+'_GUARD_RESULTS.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
 sessions=[]
 for entry in json.loads((B/'SESSIONS.json').read_text(encoding='utf-8')):
  history=[];turns=[];case=entry['case']
  for idx,turn in enumerate(case.get('turns',[])):
   question=turn.get('question') or turn.get('query');job={'question':question,'locale':turn.get('locale',case.get('locale','auto')),'reference_date':''}
   try:
    r,quality,locale,elapsed=harness.run(job,history)
    from app.session.context_resolver import resolve_question_with_context
    # Session history carries complete previous user and assistant messages.
    # This backend path does not emulate every server-side persistent task state.
    errors=[];answer=r.answer
    from tools.eval_contract_v2 import contract_matches
    _,errors=contract_matches(answer,turn.get('answer_contract') or turn)
    turns.append({'turn':idx,'question':question,'locale':locale.effective,'answer':answer,'mode':r.mode,'decision':r.decision_artifact,'passed':not errors,'failures':errors,'seconds':elapsed})
    history.extend([{'role':'user','content':question,'text':question},{'role':'assistant','content':answer,'text':answer,'decision_artifact':r.decision_artifact}])
   except Exception as e:turns.append({'turn':idx,'question':question,'passed':False,'error':repr(e)})
  sessions.append({**{k:v for k,v in entry.items() if k!='case'},'id':case.get('id'),'turns':turns})
 (B/(mode+'_SESSION_RESULTS.json')).write_text(json.dumps(sessions,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
 summary={'guard_cases':len(rows),'layout_correct':sum(x['layout_match'] for x in rows),'repeat_correct':sum(x['repeat_match'] for x in rows),'legacy_block_policy_correct':sum(x['legacy_block_policy_match'] for x in rows),'repeat_policy':'warn_and_continue matches current launcher, differs from historical guard prototype','sessions':len(sessions),'turns':sum(len(x['turns']) for x in sessions),'turns_passed':sum(t['passed'] for x in sessions for t in x['turns']),'session_scope':'backend history; actual HTTP persistence assessed separately'}
 (B/(mode+'_GUARD_SESSION_SUMMARY.json')).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
