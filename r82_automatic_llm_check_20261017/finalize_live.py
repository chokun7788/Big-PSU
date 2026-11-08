"""Record live results and preservation checks without rewriting raw runs."""
import hashlib,json
from pathlib import Path
import auto_test as a
B=Path(__file__).resolve().parent;T=B/'results/20261017T074528Z-4c2b1f'
r=json.loads((T/'RESULTS.json').read_text(encoding='utf8'))
rows=[json.loads(s) for s in (T/'CHAT_TURNS.jsonl').read_text(encoding='utf8').splitlines()]
qa=json.loads((B/'RUNNER_QA_semantic_tracking.json').read_text(encoding='utf8'))
install=json.loads((a.R81/'INSTALLATION.json').read_text(encoding='utf8'))
health=json.loads((T/'02_chat_health_before.json').read_text(encoding='utf8'))
binding_rejections=[{'question':x['question'],'reason':a.binding_rejection(x.get('body'))} for x in rows if a.binding_rejection(x.get('body'))]
checks={'real_chat_http_completed':r['completed'] and r['count']==14,'llm_on_verified':r['llm_enabled_verified'],'real_model_generation_completed':r['real_model_generation_verified'],'live_answer_contracts_14_of_14':r['passed']==r['count']==14,'loaded_source_verified':a.c.verify_health(health['body'],a.c.fingerprint()),'database_unchanged':hashlib.sha256((a.S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()==install['database_sha256'],'r81_product_code_unchanged':all(hashlib.sha256((a.S/name).read_bytes()).hexdigest()==digest for name,digest in install['installed_files'].items()),'updated_runner_controlled_qa_24_of_24':qa['count']==qa['passed']==24}
result={'checks':checks,'evidence_checks_passed':all(checks.values()),'entire_model_selector_passed':False,'selector_attempts':3,'selector_timeouts':2,'selector_binding_rejections':binding_rejections,'full_corpus_tested':False,'run_directory':str(T),'model_failure_analysis':str(T/'MODEL_FAILURE_ANALYSIS_TH.md')}
with (B/'LIVE_DELIVERY_QA.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False));assert all(checks.values())
