import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
for name in ('app/pipeline/query_signals.py','app/pipeline/experimental_fallback.py','tests/test_remaining_repairs_r56.py'):
 p=ROOT/name;backup=OUT/'before_loop7'/name;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,backup)
p=ROOT/'app/pipeline/query_signals.py';t=p.read_text(encoding='utf-8');old="r'ราคา|ค่าบริการ|จอง|ว่าง|กฎ|กฏ|กติกา|ศูนย์|มหาวิทยาลัย|";assert old in t;t=t.replace(old,"r'ราคา|ค่าบริการ|จอง|(?<!ระห)ว่าง|กฎ|กฏ|กติกา|ศูนย์|มหาวิทยาลัย|",1);p.write_text(t,encoding='utf-8')
p=ROOT/'app/pipeline/experimental_fallback.py';t=p.read_text(encoding='utf-8')
old='    reference = evidence_prompt(evidence_for(question,profile.name))';new=old+'''\n    creation_constraint = ''
    from app.pipeline.query_signals import looks_like_explicit_creation_request
    if looks_like_explicit_creation_request(question):
        creation_constraint = ('For this writing task, do not invent a specific day, date, time or venue, including today, tomorrow or tonight. '
            'Use an invitation or dialogue about arranging a mutually convenient session without fixing those details. '
            'Return only the requested writing; no explanatory note. Follow the requested length. '
            'งานเขียนนี้ห้ามกำหนดวัน วันที่ เวลา หรือสถานที่เอง รวมถึงวันนี้ พรุ่งนี้ หรือคืนนี้ '
            'ให้พูดถึงการตกลงเวลาที่สะดวกร่วมกันโดยไม่ระบุวันเวลาจริง และไม่เพิ่มหมายเหตุท้ายข้อความ')'''
assert old in t;t=t.replace(old,new,1);t=t.replace('{reference}\n\nQUESTION:', '{reference}\n{creation_constraint}\n\nQUESTION:')
old="            'semantic_numeric_approximation_changed':";assert old in t;t=t.replace(old,"            'creation_unsupported_specifics': 'Remove every invented day, date, time and venue, including today, tomorrow and tonight. Keep the invitation or dialogue and the requested length; use mutually convenient timing without a fixed date.',\n            'requested_length_coverage_missing': 'Expand the requested writing to the requested word count without adding fixed dates, times, venues or claims about studio policies.',\n"+old,1)
old="or str(llm_call.get('llm_output_rejected_reason','')).startswith('semantic_'))";new="""or str(llm_call.get('llm_output_rejected_reason','')).startswith('semantic_')
                     or (llm_call.get('llm_generation_profile') == 'long_explanation'
                         and llm_call.get('llm_output_rejected_reason') in {'creation_unsupported_specifics','requested_length_coverage_missing'}
                         and __import__('app.pipeline.query_signals',fromlist=['looks_like_explicit_creation_request']).looks_like_explicit_creation_request(question)))"""
assert old in t;t=t.replace(old,new,1);t=t.replace('Run the one permitted general-model call and preserve its audit trace.','Run a bounded model attempt and, when budget permits, one validated repair.')
p.write_text(t,encoding='utf-8')
p=ROOT/'tests/test_remaining_repairs_r56.py';t=p.read_text(encoding='utf-8');old="'ช่วยเขียนโพสต์ชวนเพื่อนมาเล่นเกมด้วยกัน สั้นๆ 80 คำ')";new="'ช่วยเขียนโพสต์ชวนเพื่อนมาเล่นเกมด้วยกัน สั้นๆ 80 คำ','ช่วยเขียนบทสนทนาสั้นๆระหว่างเพื่อนสองคนที่นัดมาเล่นเกม ใช้ประมาณ 80 คำ')";assert old in t;t=t.replace(old,new,1);p.write_text(t,encoding='utf-8')
# Update only the newly created r56 distribution folders.
s=(BASE/'r56_packages_update6.py').read_text(encoding='utf-8').replace('r56.6','r56.7').replace('r56.5','r56.6').replace('REVISION6','REVISION7').replace('revision6','revision7');exec(compile(s,'package_update7','exec'))
print('loop7: Thai between false positive, explicit writing prompt, one bounded repair')
