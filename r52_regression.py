import os, sys, subprocess, json
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r52_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
tmp=OUT/'test_tmp';tmp.mkdir(exist_ok=True)
env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONPATH=str(ROOT),PSU_TEST_TMP_DIR=str(tmp),PSU_CHAT_LOG_DIR=str(OUT/'test_logs'),PSU_LLM_PREFLIGHT='0')
label=sys.argv[1]
args=[sys.executable,'-B','-m','unittest','tests.test_research_flow_r52','tests.test_conversation_flow_r38','tests.test_intent_trap_protected_flow','tests.test_competition_claim_contract','tests.test_worker_recycle_r27_20261001','-v']
p=subprocess.run(args,cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8')
with (OUT/(label+'.txt')).open('x',encoding='utf-8') as s:s.write(p.stdout+p.stderr)
print((p.stdout+p.stderr)[-9000:]);print('exit',p.returncode)
