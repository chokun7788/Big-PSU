import os,sys,subprocess,json,time,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r50_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONDONTWRITEBYTECODE='1',PSU_CHAT_LOG_DIR=str(OUT/'unit_logs'),PSU_TEST_STATE_DIR=str(OUT/'state_fixtures'))
results=[]
names=sys.argv[1:] or ('test_domain_resume_r42.py','test_task_memory_r41.py','test_targeted_dialogue_r40.py','test_conversation_flow_r38.py','test_two_turn_choices_r39.py','test_competition_session_context_r35.py','smoke_test_live_booking_status.py','test_saved_booking_oracle_r32.py')
for name in names:
    start=time.perf_counter()
    p=subprocess.run([sys.executable,'-B','-m','unittest','discover','-s','tests','-p',name,'-v'],cwd=ROOT,env=env,text=True,encoding='utf-8',capture_output=True,timeout=120)
    file=OUT/(name.replace('.py','')+'_'+uuid.uuid4().hex[:6]+'.txt')
    with file.open('x',encoding='utf-8') as f:f.write(p.stdout+p.stderr)
    results.append(dict(file=name,returncode=p.returncode,elapsed_sec=round(time.perf_counter()-start,3),evidence=file.name))
    print(name,p.returncode,p.stderr[-500:],flush=True)
dest=OUT/('source_regression_'+time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]+'.json')
with dest.open('x',encoding='utf-8') as f:json.dump(results,f,ensure_ascii=False,indent=2)
sys.exit(int(any(r['returncode'] for r in results)))




