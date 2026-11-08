import sys,json,os
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p));r=Path(Path('r30_report_path.txt').read_text().strip())
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
from app.pipeline.engine import answer_question_pipeline_debug
from r30_full_corpus import plain
cases=[('PC 1 or 2 or 3 hours cost?','en'),('PC 1 หรือ 2 หรือ 3 ชั่วโมงกี่บาท','th'),('ผมไม่ใช่นักศึกษา มอ PC 1 หรือ 2 ชั่วโมงกี่บาท','th'),('I am not a PSU student, PC for 1 or 2 hours cost?','en'),('ค่าเล่นแต่ละเครื่องมีอะไรบ้าง','th'),('อุปกรณ์แต่ละโซนราคาเท่าไหร่','th'),('How much does each service cost?','en'),('What do I need to book to play Hogwarts?','en'),('ปุ่ม Q9 ใน Gran Turismo 7 ใช้ทำอะไร','th'),('What does the Z9 button do in Gran Turismo 7?','en'),('What do I need to book to play Roblox?','en')]
with (r/'additional_boundary_probes.jsonl').open('x',encoding='utf-8') as f:
    for q,l in cases:
        result=answer_question_pipeline_debug(q,locale=l,experimental_allow_llm=False,experimental_rag_fallback=True)
        f.write(json.dumps({'q':q,'locale':l,'result':plain(result)},ensure_ascii=False)+'\n')
        print(json.dumps({'q':q,'mode':result.mode,'answer':result.answer[:1100]},ensure_ascii=False),flush=True)
