import json,os,sys
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project))
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.competition_presentation import pause_rows_for_query,focused_pause_lines
for q in ('VALORANT technical pause ได้กี่นาที','กติกา Tekken 8 minimum age requirement เท่าไร'):
 r=answer_question_pipeline_debug(q,locale='th',experimental_allow_llm=False,experimental_rag_fallback=True)
 print(json.dumps({'q':q,'answer':r.answer,'mode':r.mode,'hits':[(h['id'],h.get('section_title'),h.get('text')) for h in r.hits]},ensure_ascii=False))
 for t in r.trace:
  if t.stage in ('competition_source_grounding','competition_source_contract','evidence_contract','execution','question_frame','early_answer_contract','retrieval','evidence_contract_executor'):print(json.dumps(vars(t),ensure_ascii=False))
 print('pause probe',[(r['id'],focused_pause_lines(q,r['text'])) for r in pause_rows_for_query(q,r.hits)])
