"""Verify frozen source/model/grade imports without running the sample twice."""
from pathlib import Path
import hashlib,json,sys,urllib.request
R=Path(__file__).resolve().parent;S=R/'system';sys.path[:0]=[str(S),str(R)]
from run_common import configure
configure('preflight')
config=json.loads((R/'CONFIG.json').read_text('utf8'))
assert all(hashlib.sha256((S/e['path']).read_bytes()).hexdigest()==e['sha256'] for e in config['source_manifest'])
from app.pipeline.engine import answer_question_pipeline_debug
from app.knowledge.common.build_info import LOADED_BUILD
from app.knowledge.common.migrated_view import MigratedView
snap=MigratedView(S/'data/knowledge/common.sqlite').snapshot()
assert len(snap['release']['records'])==602
import tools.run_master_ground_truth_eval,tools.eval_contract_v2,tools.run_competition_contract_r27
import tools.run_competition_composition_r28,tools.run_competition_rules_rag_ground_truth,tools.run_answer_quality_eval
payload={'model':'scb10x/typhoon2.5-qwen3-4b','stream':False,'think':False,'prompt':'Return exactly READY','options':{'temperature':0,'num_predict':12,'num_ctx':3072}}
with urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'}),timeout=45) as f:model=json.load(f)
result={'passed':bool(model.get('done') and model.get('response','').strip()),'loaded_build':LOADED_BUILD,'frozen_records':602,'model_response':model,'llm_enabled':True,'sample_requests_executed':0,'grader_modules_imported':True}
with (R/'PREFLIGHT_RESULT.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
assert result['passed'] and LOADED_BUILD['build_id']=='common-r92-task-contracts'
print(json.dumps({'passed':True,'sample_requests_executed':0,'model_done':model.get('done'),'build':LOADED_BUILD['build_id']}))
