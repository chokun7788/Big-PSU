import json, os, sys
from pathlib import Path

project = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0, str(project))
os.environ['PSU_BILINGUAL_EN_ENABLED'] = '1'
os.environ['PSU_SEMANTIC_RETRIEVAL'] = '0'
from app.pipeline.engine import answer_question_pipeline_debug

cases = [
 ('th', 'VALORANT technical pause สื่อสารได้ไหม'),
 ('en', 'Can players communicate during a VALORANT technical pause?'),
 ('th', 'ขอตารางบทลงโทษ CS2'),
 ('en', 'Show the CS2 penalty table'),
 ('th', 'Tekken 8 การตั้งค่าเกมเป็นยังไง'),
 ('en', 'What are the Tekken 8 in-game settings?'),
 ('en', 'How many players are in a CS2 team?'),
 ('en', 'Can I use a tablet or iPad in the RoV tournament?'),
 *[(lang, f'กฎ {game} มีอะไรบ้าง' if lang == 'th' else f'What are the {game} tournament rules?') for lang in ('th', 'en') for game in ('CS2', 'RoV', 'Tekken 8', 'VALORANT')],
]
results = []
for locale, question in cases:
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
    record = {'question': question, 'locale': locale, 'mode': result.mode, 'answer': result.answer, 'validation': result.validation.ok, 'hits': [h.get('id') for h in result.hits]}
    results.append(record)
    print(json.dumps(record, ensure_ascii=False), flush=True)
report = Path(Path(__file__).with_name('r25_report_path.txt').read_text(encoding='utf-8').strip())
with (report/(sys.argv[1] if len(sys.argv) > 1 else 'first_probe.json')).open('x', encoding='utf-8') as handle:
    json.dump(results, handle, ensure_ascii=False, indent=2)
