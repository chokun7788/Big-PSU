import json, sys, os
from pathlib import Path
from unittest.mock import patch
BASE=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=Path((BASE/'r52_current_path.txt').read_text())
sys.path.insert(0,str(ROOT))
from app.pipeline.protected_intents import _is_price_without_service
from app.session.conversation_plan import resolve_request_plan
from app.pipeline.query_signals import looks_like_clear_general_request
from app.pipeline.answer_contracts import _answer_types
from app.pipeline.schemas import PipelineRoute
import app.pipeline.experimental_fallback as f

def checks():
    tests=[]
    def add(name,actual,expected):tests.append(dict(name=name,actual=actual,expected=expected,passed=actual==expected))
    for q in ['Why can high frame rate still feel choppy?', 'Explain the refresh rate of a monitor.', 'Explain sample rates for audio.']:
        add('not_price:'+q,_is_price_without_service(q.lower(),None),False)
    add('real_price_missing_service',_is_price_without_service('what is the hourly rate for using equipment?',None),True)
    for q in ['Compare TCP and UDP, including one advantage and one disadvantage of each.', 'Box A has 3 balls and box B has 5. Move 2 from B to A. How many are in each box? Explain briefly.']:
        add('not_scope:'+q,resolve_request_plan(q,locale='en') is None,True)
    add('all_service_prices',resolve_request_plan('Show all service prices',locale='en')['tasks'][0]['scope']['entity_selection'],'all')
    for q in ['อธิบายว่า ping ในเครือข่ายคืออะไรแบบสั้นๆ', 'แปลประโยค Please check your network connection เป็นภาษาไทย', 'Give three steps for learning touch typing.', 'Write a friendly two-sentence invitation to a group study session.', 'Compare TCP and UDP, including one advantage and one disadvantage of each.']:
        add('general:'+q,looks_like_clear_general_request(q),True)
    for q in ['Explain the booking rules of the PSU studio.', 'Write the service fees of PSU.', 'What is the latest news today?']:
        add('source_required:'+q,looks_like_clear_general_request(q),False)
    route=PipelineRoute('general','general_knowledge_query',.9,'fact','low','fixture')
    add('across_not_control','controls' in _answer_types('Network latency is delay across a network.',route,'pipeline:general_llm_after_rag_miss'),False)
    with patch.object(f,'effective_locale',return_value='en'):
        add('three_steps_profile',f.select_general_generation_profile('Give three steps for learning touch typing.').expected_items,3)
        add('two_sentence_profile',f.select_general_generation_profile('Write a friendly two-sentence invitation to a group study session.').expected_items,2)
        add('long_profile',f.select_general_generation_profile('Explain a computer network in approximately 500 words.').name,'long_explanation')
        p=f.GeneralGenerationProfile('two_sentences',128,'',128,2)
        add('single_sentence_rejected',f._general_output_contract('Join our study group.',p,{'ollama_done_reason':'stop'})[0],False)
        add('two_sentences_allowed',f._general_output_contract('Join our study group. We can learn together.',p,{'ollama_done_reason':'stop'})[0],True)
    return tests

if __name__=='__main__':
    tests=checks(); label=sys.argv[1] if len(sys.argv)>1 else 'checks'
    with (OUT/(label+'.json')).open('x',encoding='utf-8') as stream:json.dump(tests,stream,ensure_ascii=False,indent=2)
    print(label, sum(t['passed'] for t in tests),'/',len(tests))
    for t in tests:
        if not t['passed']:print(json.dumps(t,ensure_ascii=False))
