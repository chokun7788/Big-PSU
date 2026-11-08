import json,sys,os,importlib.util,time
from pathlib import Path
from collections import Counter
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project));report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip());old_report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard,load_runtime_clean_texts
from app.core.normalization import KEYBOARD_EN_TO_THAI,KEYBOARD_THAI_TO_EN
spec=importlib.util.spec_from_file_location('r29_old_detector',report/'before/app/core/keyboard_input_anomaly.py');mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
old=RuntimeInputQualityGuard(mod.KeyboardInputAnomalyDetector().fit(load_runtime_clean_texts()),mode='enforce',repeat_policy='warn_and_continue',profile_version='r28-snapshot')
new=RuntimeInputQualityGuard.from_environment();new.mode='enforce';new.repeat_policy='warn_and_continue'
th=['วันนี้จอง PC ได้ไหม','เล่นเกมอะไรได้บ้าง','เปิดกี่โมง','ต้องเช็กอินไหม','ใช้เครื่องเล่นได้กี่คน','ราคาเท่าไหร่','นำอุปกรณ์มาคืนที่ไหน','ติดต่อเจ้าหน้าที่อย่างไร','ดูตารางจองวันพรุ่งนี้','กติกาการแข่งขันมีอะไรบ้าง','มีเครื่องไหนว่างบ้าง','นักศึกษาจองอย่างไร','คืนเงินได้ไหม','กินอาหารที่ไหนได้บ้าง','ใช้จอยส่วนตัวได้ไหม']
en=['What time does the studio open?','How much does PC cost?','May I book a VR station?','Show the available PC slots.','Can you tell me the rules?','What equipment can I bring?','Are controllers included?','Where is the studio?','How do I check in?','Can I get a refund?','Please list available games.','How many players are allowed?','Where can I return equipment?','What do I need to book?','Which games can I play?']
controls=[]
for locale,questions,mapping in [('th',th,KEYBOARD_THAI_TO_EN),('en',en,KEYBOARD_EN_TO_THAI)]:
    for i,q in enumerate(questions):
        controls.append({'id':f'new-clean-{locale}-{i}','question':q,'expected_blocked':False,'kind':'clean'})
        controls.append({'id':f'new-layout-{locale}-{i}','question':''.join(mapping.get(ch,ch) for ch in q),'original':q,'expected_blocked':True,'kind':'keyboard_projection'})
controls += [{'id':'literal-negation','question':'Do not change PC1, 2026-10-03, 13:00 or 30 minutes. Is it available?','expected_blocked':False,'kind':'protected_literals'}, {'id':'thai-literals','question':'ไม่ใช่ PC1 หมายถึง PC2 วันที่ 2026-10-03 เวลา 13:00','expected_blocked':False,'kind':'protected_literals'}, {'id':'true-mixed-layout','question':'อยากถามว่า g]jo ได้ไหม','expected_blocked':True,'kind':'mixed_layout'}, {'id':'english-context-real-layout','question':'Could you check this using verified information: g]jo','expected_blocked':True,'kind':'mixed_layout'}]
assert controls==json.loads((report/'new_guard_controls_64.json').read_text(encoding='utf-8'))
run=sys.argv[1] if len(sys.argv)>1 else 'candidate_C'
fixed=json.loads((report/'blocked36_fixture.json').read_text(encoding='utf-8'))['cases']
records=[]
for c in fixed+controls:
    start=time.perf_counter();a=old.inspect(c['question']);b=new.inspect(c['question'])
    records.append(dict(c,before=a.to_log_dict(),after=b.to_log_dict(),elapsed_ms=round((time.perf_counter()-start)*1000,3),passed=b.should_short_circuit==c['expected_blocked'],features=b.features.to_dict()))
with (report/(run+'_guard100.json')).open('x',encoding='utf-8') as f:json.dump({'records':records,'total':len(records),'passed':sum(r['passed'] for r in records)},f,ensure_ascii=False,indent=2)
baseline=json.loads((old_report/'guard_prior_audit.json').read_text(encoding='utf-8'))['records'];regression=[]
for r in baseline:
    b=new.inspect(r['question']);regression.append({'id':r['id'],'corpus':r['corpus'],'question':r['question'],'before_blocked':r['after_blocked'],'after_blocked':b.should_short_circuit,'after':b.to_log_dict()})
summary={'controls_total':len(records),'controls_passed':sum(r['passed'] for r in records),'control_failures':[{k:r[k] for k in ('id','question','expected_blocked','after')} for r in records if not r['passed']],'regression_total':len(regression),'before_blocked':sum(r['before_blocked'] for r in regression),'after_blocked':sum(r['after_blocked'] for r in regression),'newly_blocked':sum(not r['before_blocked'] and r['after_blocked'] for r in regression),'no_longer_blocked':sum(r['before_blocked'] and not r['after_blocked'] for r in regression),'new_profile':new.profile_version,'scope':'guard decisions only; ordinary noise vs deliberate layout labels; untuned new controls become development if inspected failures trigger fixes'}
with (report/(run+'_guard_regression4283.json')).open('x',encoding='utf-8') as f:json.dump({'summary':summary,'records':regression},f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False));sys.exit(bool(summary['control_failures'] or summary['newly_blocked']))
