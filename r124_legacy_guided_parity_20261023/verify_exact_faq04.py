"""Every eligible stored stable FAQ is reachable without a per-question parser."""
import copy,json,os,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'revision04_system';sys.path.insert(0,str(S))
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.exact_faq import candidates,answer,key
from app.knowledge.common.domain_flow.projection import value,bilingual
from app.knowledge.common.domain_flow.scope import reference_time
store=MigratedView(S/'data/knowledge/common.sqlite');snap=store.snapshot();engine=Engine.from_snapshot(snap);at=reference_time('2026-10-23T17:00:00+07:00')
OUT=R/('exact_faq_verification_'+str(time.time_ns()));OUT.mkdir();rows=[];seen=set();checks={}
def forbidden(*args,**kwargs):raise AssertionError('Exact-source probe cannot call model/provider')
with patch('urllib.request.urlopen',forbidden):
 for r in engine.index.records.values():
  if r['kind']!='faq':continue
  for lang,q in bilingual(value(r,'question')).items():
   if not q or (lang,key(q)) in seen:continue
   seen.add((lang,key(q)));matched=candidates(engine.index,q,at)
   if not matched:continue
   result=answer(CommonAnswerer(store),snap,engine.index,q,at,lang)
   rows.append({'question':q,'locale':lang,'expected_record_ids':[x['record_id'] for x,_ in matched],
    'returned_record_ids':result.decision_artifact['query_plan']['record_ids'],'answer':result.answer,'validation':result.validation.ok,
    'conflict':result.decision_artifact['query_plan'].get('authority_conflict'),'whole_question_identity':True})
checks['eligible_stable_faqs_all_return_current_source']=bool(rows) and all(set(x['expected_record_ids'])==set(x['returned_record_ids']) and x['validation'] for x in rows)
checks['no_keyword_or_partial_question_match']=not candidates(engine.index,rows[0]['question']+'; price PC for two hours',at)
checks['clock_question_keeps_calendar_path']=not candidates(engine.index,'วันนี้เปิดไหม',at)
checks['live_question_keeps_provider_path']=not candidates(engine.index,'PC2 ว่างไหม',at)
# A conflicting duplicate remains a conflict, never an arbitrarily picked reply.
target=next(r for r in engine.index.records.values() if r['record_id']==rows[0]['expected_record_ids'][0]);modified=copy.deepcopy(snap)
duplicate=copy.deepcopy(target);duplicate['record_id']='controlled_conflicting_faq';duplicate['fields']['answer']['value']={'th':'CONTROLLED CONFLICT','en':'CONTROLLED CONFLICT'}
modified['release']['records'][duplicate['record_id']]=duplicate;modified['epoch']+=100000;modified['active']='controlled-faq-conflict'
class MemoryView:
 path=store.path
 def snapshot(self):return modified
 def still_current(self,s):return s is modified
e=Engine.from_snapshot(modified);q=rows[0]['question'];r=answer(CommonAnswerer(MemoryView()),modified,e.index,q,at,rows[0]['locale'])
checks['different_answers_to_same_question_not_silently_merged']=r is not None and r.decision_artifact['execution_contract']['tasks'][0]['terminal_state']=='conflict'
summary={'all_passed':all(checks.values()),'checks':checks,'question_language_pairs':len(rows),'unique_source_questions':len({key(r['question']) for r in rows}),
 'model_calls':0,'provider_calls':0,'controlled_conflict_memory_only':True,'output':str(OUT)}
(OUT/'RESULTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');(OUT/'VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2));assert summary['all_passed']
