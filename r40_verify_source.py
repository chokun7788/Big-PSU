import os, sys, subprocess, json, time, uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r40_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
env=dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONDONTWRITEBYTECODE='1', PSU_CHAT_LOG_DIR=str(OUT/'unit_logs'))
results=[]
names = sys.argv[1:] or ('test_targeted_dialogue_r40.py','test_conversation_flow_r38.py','test_two_turn_choices_r39.py',
             'test_competition_session_context_r35.py','test_p0_calendar_booking_reconciliation_20260925.py',
             'test_saved_booking_oracle_r32.py','test_booking_on_demand_20261001.py')
for name in names:
    start=time.perf_counter()
    p=subprocess.run([sys.executable,'-B','-m','unittest','discover','-s','tests','-p',name,'-v'],cwd=ROOT,env=env,text=True,encoding='utf-8',capture_output=True,timeout=120)
    file=OUT/(name.replace('.py','')+'_'+uuid.uuid4().hex[:6]+'.txt')
    with file.open('x',encoding='utf-8') as f:f.write(p.stdout+p.stderr)
    results.append(dict(file=name,returncode=p.returncode,elapsed_sec=round(time.perf_counter()-start,3),evidence=file.name))
    print(name,p.returncode,p.stderr[-220:],flush=True)
dest=OUT/('source_regression_'+time.strftime('%Y%m%d_%H%M%S')+'.json')
with dest.open('x',encoding='utf-8') as f:json.dump(results,f,ensure_ascii=False,indent=2)
sys.exit(int(any(r['returncode'] for r in results)))
