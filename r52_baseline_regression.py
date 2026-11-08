import sys, subprocess, os
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r52_current_path.txt').read_text())
env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONPATH=str(OUT/'before'),PSU_CHAT_LOG_DIR=str(OUT/'baseline_test_logs'))
prefix='tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.'
cases=['test_public_access_questions_use_the_requested_facet','test_specific_policy_facets_beat_generic_public_access','test_unspecified_english_pay_questions_ask_for_service']
p=subprocess.run([sys.executable,'-B','-m','unittest',*[prefix+c for c in cases],'-v'],cwd=OUT/'before',env=env,capture_output=True,text=True,encoding='utf-8')
with (OUT/'baseline_neighbor_failures.txt').open('x',encoding='utf-8') as f:f.write(p.stdout+p.stderr)
print((p.stdout+p.stderr)[-5200:])
