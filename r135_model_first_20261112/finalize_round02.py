"""Pin round02 evidence without mutating historical reports or raw logs."""
import ast,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((R/'BASELINE_MANIFEST.json').read_text());parent=Path(base['parent'])
assert all(sha(parent/'system'/p)==h for p,h in base['app_sha256'].items()),'Parent app changed'
paths=['context_contract_1794473457827914800/RESULT.json','context_contract_1794473564216301400/RESULT.json','protocol_controls_1794473759423686800/RESULT.json','real_model_batch_1794473597119178800/RESULT.json','real_model_batch_1794473704350231300/RESULT.json','http_context_1794473888357142400/RESULT.json','http_context_1794473888357142400/PERSISTED_CHECKS.json']
evidence=[]
for p in paths:
 result=json.loads((R/p).read_text());evidence.append({'path':p,'sha256':sha(R/p),'all_passed':result.get('all_passed'),'passed_cases':result.get('checks_passed_cases'),'actual_model_calls':result.get('actual_model_calls'),'scope':result.get('scope')})
for p in ['system/app/knowledge/common/model_first.py','test_context_contract.py','test_http_context.py']:
 ast.parse((R/p).read_text(encoding='utf8'))
manifest={'round':2,'parent_app_files_preserved':len(base['app_sha256']),'parent':str(parent),'app_sha256':{str(p.relative_to(R/'system')):sha(p) for p in (R/'system/app').rglob('*.py')},'runtime_version':'R135-Model-first-trial02','preview_port':8145,'active_generation_protocol':'compact three-field context range','withdrawn_generation_protocol':'five-field predicate/context range','generation_accuracy_verified':False,'evidence':evidence,'report_sha256':sha(R/'ROUND02_REPORT_TH.md'),'raw_logs_private':True,'deployed':False,'broad_trial_started':False}
(R/'ROUND02_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'round02_contract_fix_verified_model_semantics_still_experimental','parent':'r135_recovery_loop_20261112','deployed':False,'full_eval_running':False,'preview_port':8145,'runtime_version':'R135-Model-first-trial02','report':'ROUND02_REPORT_TH.md','manifest':'ROUND02_MANIFEST.json','mocked_source_contract_checks':21,'mocked_protocol_checks':12,'latest_actual_development_cases_passed':2,'latest_actual_development_case_count':4,'http_context_requests':1,'http_persisted_checks':9,'next_group':'audit existing trained planner schema; static offering vs controls and omitted compound needs; stop repeated prompt-format tuning','known_gaps':['model intent errors','model omitted needs','context and audience ambiguity','generic booking not verified as free-price workflow','owner editor lifecycle and source authority','cooldown/deadline']},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'parent_preserved':True,'parent_app_files':len(base['app_sha256']),'syntax_passed':True,'evidence_files':len(paths)}))
