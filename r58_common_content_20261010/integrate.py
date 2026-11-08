from pathlib import Path
OUT=Path(__file__).resolve().parent
CAND=OUT/'system/PSU_Esports_Chatbot_Local'
p=CAND/'app/pipeline/engine.py';s=p.read_text(encoding='utf-8')
anchor='            from app.pipeline.request_focus import explicit_request_focus\n'
assert s.count(anchor)==1
s=s.replace(anchor,"            from app.knowledge.common.answer import try_common_answer\n            common = try_common_answer(question, locale=resolved_locale.effective,\n                recent_history=recent_history, allow_llm=bool(experimental_allow_llm))\n            if common is not None:\n                return common\n"+anchor)
p.write_text(s,encoding='utf-8')
print('Candidate engine integrated')
