"""Read-only component diagnosis, not an end-to-end model replay."""
import sys
sys.dont_write_bytecode = True
import json
import hashlib
from dataclasses import asdict
from pathlib import Path
import urllib.request

project = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0, str(project))
from app.session.context_resolver import resolve_question_with_context, latest_context_state
from app.pipeline.preprocess import preprocess_input, extract_entities
from app.pipeline.router import route_intent
from app.pipeline.universal_intent import resolve_universal_intent, refine_route_with_universal_intent
from app.pipeline.question_frame import build_question_frame
from app.pipeline.capability_registry import build_candidate_decisions
from app.pipeline.protected_intents import answer_protected_intent
from app.calculator.service_fee import answer_service_fee, _detect_group, SERVICE_FEES
from app.pipeline.closed_query_improvements import _fee_catalog

out = Path(__file__).resolve().parent
initial = 'ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก'
pre = preprocess_input(initial)
entities = extract_entities(pre)
protected = answer_protected_intent(pre.clean_query, locale='th', service=entities.service, rules=[], price_intent=entities.price_intent)
history = [
    {'role': 'user', 'text': initial},
    {'role': 'assistant', 'text': protected.answer, 'route_category': 'clarification', 'route_intent': 'price_missing_service'},
]
strong_history = [history[0], {**history[1], 'universal_intent': {'domain': 'service_fee', 'operation': 'price_lookup', 'filters': {'user_group': 'external'}}}]
cases = []
for question, hist, locale in [
    ('ทั้งหมด', history, 'th'), ('PC', history, 'th'),
    ('ทั้งหมด', strong_history, 'th'), ('PC', strong_history, 'th'),
    ('ไก่กับไข่อะไรเกิดก่อนกัน', [], 'th'),
    ('all', [{'role':'user','text':'What are the fees for external users?'}, {'role':'assistant','text':'Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?', 'route_category':'clarification','route_intent':'price_missing_service'}], 'en'),
    ('PC', [{'role':'user','text':'What are the fees for external users?'}, {'role':'assistant','text':'Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?', 'route_category':'clarification','route_intent':'price_missing_service'}], 'en'),
]:
    resolved = resolve_question_with_context(question, hist, locale=locale)
    p = preprocess_input(resolved.resolved_question)
    e = extract_entities(p)
    route, _ = route_intent(p, e)
    intent, _ = resolve_universal_intent(p.clean_query, route, allow_llm=False)
    route, _ = refine_route_with_universal_intent(route, intent)
    frame = build_question_frame(p.clean_query, route, intent)
    accepted, rejected, trace = build_candidate_decisions(route, intent, question=p.clean_query)
    cases.append({'question': question, 'locale': locale, 'history_variant': 'strong_price_metadata' if hist is strong_history else 'screenshot_text' if hist is history else 'other', 'history_count':len(hist), 'context_state': latest_context_state(hist), 'resolved':resolved.to_dict(), 'entities':asdict(e), 'route':asdict(route), 'intent':asdict(intent), 'frame':frame.as_dict(), 'candidate_selection':trace.metadata, 'accepted':[c.as_dict() for c in accepted], 'rejected':[c.as_dict() for c in rejected]})
catalogs = []
for q in ['ตารางราคาทั้งหมดของบุคคลภายนอก', 'ตารางราคาทั้งหมดสำหรับบุคคลทั่วไป', 'All service prices for general adults']:
    result = _fee_catalog(q, 'en' if q.startswith('All') else 'th')
    catalogs.append({'question':q, 'matched':result is not None, 'mode':result.mode if result else '', 'answer':result.answer if result else ''})
calculators = [{'question':q, 'group_detection':_detect_group(q), 'calculator':answer_service_fee(q)} for q in ['ราคา PC สำหรับบุคคลภายนอก', 'ราคา PC สำหรับบุคคลทั่วไป', 'ราคา PC สำหรับนักศึกษาต่างสถาบัน']]
packages = {'source':project, '8090':project / 'owner_local_delivery_20261003_competition_conversation_r37_final3/PSU_Esports_Chatbot_Local', 'with_models':Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_20261003\02_With_Models\system\PSU_Esports_Chatbot_Local')}
hashes = {}
for label,root in packages.items():
    hashes[label]={str(rel):hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in ['app/session/context_resolver.py','app/pipeline/capability_registry.py','app/pipeline/protected_intents.py','app/pipeline/closed_query_improvements.py','app/calculator/service_fee.py','web_chat/app.js']}
health=[]
for port in [8090,8091,8092]:
    try:
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=2) as response:
            data=json.load(response)
        health.append({'port':port,'ok':data.get('ok'),'time':data.get('time'),'runtime':data.get('runtime'),'performance_log':data.get('pipeline_workers',{}).get('performance',{}).get('path')})
    except Exception as exc:
        health.append({'port':port,'error':str(exc)})
result={'method':'isolated read-only component calls; no local LLM, semantic route refinement, tool-router or HTTP chat replay; scores are reconstructed, not screenshot trace', 'initial':{'question':initial,'entities':asdict(entities),'protected':asdict(protected)}, 'cases':cases,'catalogs':catalogs,'calculators':calculators,'recorded_rates':SERVICE_FEES,'source_hashes':hashes,'health':health}
(out/'component_findings.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
for c in cases:
    print(json.dumps({'q':c['question'],'locale':c['locale'],'history':c['history_variant'],'resolved':c['resolved'],'route':c['route'],'operation':c['frame']['operation'],'selection':c['candidate_selection']['selection'],'top':[a['capability_id']+':'+str(a['score']) for a in c['accepted'][:3]],'context_state':c['context_state']},ensure_ascii=False))
print(json.dumps({'catalogs':[{k:v for k,v in c.items() if k!='answer'} for c in catalogs], 'group_detection':[{k:v for k,v in c.items() if k!='calculator'} for c in calculators], 'same_files':all(hashes['source']==h for h in hashes.values())},ensure_ascii=False))
