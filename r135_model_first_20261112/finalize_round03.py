"""Preserve parent and freeze final trial evidence, not historical scores."""
import ast,hashlib,json,statistics,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((R/'BASELINE_MANIFEST.json').read_text());parent=Path(base['parent'])
assert all(sha(parent/'system'/p)==h for p,h in base['app_sha256'].items()),'Parent app changed'
model=json.load(urllib.request.urlopen('http://127.0.0.1:12921/health',timeout=5));assert model['pid']==json.loads((R/'TRAINED_PLANNER_AUDIT.json').read_text())['serving']['pid']
preview=json.load(urllib.request.urlopen('http://127.0.0.1:8145/health',timeout=5));assert preview['runtime']['version']=='R135-Model-first-trial03'
paths=['trained_planner_controls_1794479103047417600/RESULT.json','compact_review_controls_1794479100840333000/RESULT.json','numeric_scope_1794479030130940900/RESULT.json','context_contract_1794479073274793500/RESULT.json','price_currency_1794479105101341600/RESULT.json','alternative_duration_controls_1794479116585789300/RESULT.json']
evidence=[]
for p in paths:
 r=json.loads((R/p).read_text());assert r['all_passed'],p
 evidence.append({'path':p,'sha256':sha(R/p),'checks':len(r['checks']),'all_passed':True,'scope':'source/mock/replay; not inference accuracy'})
trials=[]
for name in ['retained_real_batch_1794477977572793400','compact_real_batch_1794478522067761000']:
 r=json.loads((R/name/'RESULT.json').read_text());details=json.loads((R/name/'DETAILS.json').read_text(encoding='utf8'))
 trials.append({'path':name+'/RESULT.json','sha256':sha(R/name/'RESULT.json'),'requests':r['requests'],'declared_intent_cases_passed':r['declared_intent_cases_passed'],'median_seconds':statistics.median(x['seconds'] for x in details),'max_seconds':max(x['seconds'] for x in details),'full_answer_accuracy_claimed':False})
http='http_round03_1794479185977374000/RESULT.json';h=json.loads((R/http).read_text());assert h['all_passed']
changed=[str(p.relative_to(R)) for p in (R/'system/app').rglob('*.py') if str(p.relative_to(R/'system')) not in base['app_sha256'] or sha(p)!=base['app_sha256'][str(p.relative_to(R/'system'))]]
for p in changed:ast.parse((R/p).read_text(encoding='utf8'))
manifest={'round':3,'parent_app_files_preserved':len(base['app_sha256']),'protected_model_pid_preserved':model['pid'],'model_weights_retrained_or_reloaded':False,'active_default':'compact+guard-only','runtime_version':preview['runtime']['version'],'retained_and_one_review_promoted':False,'changed_vs_parent':changed,'app_sha256':{str(p.relative_to(R/'system')):sha(p) for p in (R/'system/app').rglob('*.py')},'source_mock_regressions':evidence,'source_mock_check_count':sum(e['checks'] for e in evidence),'actual_model_trials':trials,'final_http':{'path':http,'sha256':sha(R/http),'requests':2,'checks':sum(len(c['checks']) for c in h['cases'])},'deployed':False,'broad_trial_started':False,'semantic_accuracy_claimed':False,'raw_data_private':True,'report_sha256':sha(R/'ROUND03_REPORT_TH.md')}
(R/'ROUND03_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'round03_source_scope_fixed_model_intent_unresolved','parent':'r135_recovery_loop_20261112','deployed':False,'full_eval_running':False,'preview_port':8145,'runtime_version':preview['runtime']['version'],'default_planner':'compact','default_review':'guard-only','report':'ROUND03_REPORT_TH.md','manifest':'ROUND03_MANIFEST.json','retained_trial_intent_cases':'0/6, not accuracy','compact_review_trial_intent_cases':'4/6, not full-answer accuracy','review_promoted':False,'source_mock_checks':manifest['source_mock_check_count'],'final_http_requests':2,'known_gaps':['static services vs controls','typo secondary task omissions','edition/context loss','shared/anaphoric numeric scope','source billing unit semantics/currentness/authority','game control action reader','owner editor/attachments','cooldown/hard deadline'],'next_group':'source-grounded output-operation proposal and game action binding; stop unchanged retained/prompt/review loops'},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'parent_preserved':True,'protected_model_pid':model['pid'],'checks':manifest['source_mock_check_count'],'http_checks':manifest['final_http']['checks'],'changed_app_files':len(changed)}))
