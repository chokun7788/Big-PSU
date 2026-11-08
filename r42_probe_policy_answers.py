import sys,os,json,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(ROOT));os.chdir(ROOT)
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0',PSU_CHAT_LOG_DIR=str(OUT/'policy_probe_logs'))
from app.pipeline.engine import answer_question_pipeline_debug
rows=[]
for q,lang in [('How far ahead must I book?','en'),('How many days in advance can I cancel my booking?','en'),('จองได้สูงสุดกี่เครื่อง','th'),('ต้องจองล่วงหน้ากี่วัน','th')]:
    r=answer_question_pipeline_debug(q,locale=lang,experimental_allow_llm=False)
    rows.append(dict(question=q,locale=lang,mode=r.mode,category=r.route.category,intent=r.route.intent,answer=r.answer));print(rows[-1],flush=True)
with (OUT/(sys.argv[1]+'_'+uuid.uuid4().hex[:6]+'.json')).open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
