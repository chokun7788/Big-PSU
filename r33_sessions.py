import sys,os,json
from pathlib import Path
from unittest.mock import patch
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P));os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
from app.pipeline.engine import answer_question_pipeline_debug
from app.session.context_resolver import resolve_question_with_context
from app.booking.live_status import _unavailable
from r33_full_corpus import plain
cases=json.loads((R/'candidate_D_inventory.json').read_text(encoding='utf-8'))['session_cases'];records=[]
with (R/'R33_SESSION_CASES.jsonl').open('x',encoding='utf-8') as f:
 for entry in cases:
  history=[];turns=[]
  for c in entry['case']['turns']:
   context=resolve_question_with_context(c['question'],history)
   with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'known offline session fixture',error_code='fixture_offline')),patch('app.runtime.fast_answer.get_live_booking_status',side_effect=lambda d:_unavailable(d,'known offline session fixture',error_code='fixture_offline')):
    x=answer_question_pipeline_debug(context.resolved_question,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
   errors=['missing:'+t for t in c.get('must_contain',[]) if t.casefold() not in x.answer.casefold()]+['forbidden:'+t for t in c.get('must_not_contain',[]) if t.casefold() in x.answer.casefold()]
   turns.append(dict(expected=c,context=plain(context),result=plain(x),passed=not errors,errors=errors))
   history.extend([dict(role='user',text=c['question']),dict(role='assistant',text=x.answer,resolved_text=context.resolved_question,route_category=x.route.category,route_intent=x.route.intent,universal_intent=plain(x.universal_intent))])
  row=dict(case=entry,turns=turns,passed=all(x['passed'] for x in turns));records.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
with (R/'R33_SESSION_SUMMARY.json').open('x',encoding='utf-8') as f:json.dump(dict(sessions=len(records),passed=sum(x['passed'] for x in records),turns=sum(len(x['turns']) for x in records),turns_passed=sum(t['passed'] for x in records for t in x['turns']),failed_ids=[x['case']['case']['id'] for x in records if not x['passed']],scope='Frozen original session wording/content checks; automatic offline context resolver, no real booking occupancy oracle'),f,ensure_ascii=False,indent=2)
print(json.dumps({'sessions':len(records),'passed':sum(x['passed'] for x in records),'failed_ids':[x['case']['case']['id'] for x in records if not x['passed']]}),flush=True)
