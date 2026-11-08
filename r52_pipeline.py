import os,sys,json,time
from pathlib import Path
from unittest.mock import patch
BASE=Path(__file__).resolve().parent; ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=Path((BASE/'r52_current_path.txt').read_text());sys.path.insert(0,str(ROOT))
os.environ.update(PSU_LLM_PREFLIGHT='0',PSU_UNIVERSAL_INTENT_LLM_FIRST='0',PSU_SEMANTIC_ROUTER='0')
from app.pipeline.engine import answer_question_pipeline_debug as answer
import app.pipeline.experimental_fallback as f
CASES=[
('อธิบายว่า ping ในเครือข่ายคืออะไรแบบสั้นๆ','th','ping คือเวลาตอบกลับของเครือข่ายครับ'),
('Explain network latency in one short paragraph.','en','Network latency is the delay across a network.'),
('Compare TCP and UDP, including one advantage and one disadvantage of each.','en','TCP delivers ordered data reliably but has overhead. UDP has less overhead but can lose data.'),
('Why can high frame rate still feel choppy? Explain frame pacing briefly.','en','Uneven frame pacing can make a high frame rate feel choppy.'),
('Give three steps for learning touch typing.','en','1. Use the home row.\n2. Practice without looking.\n3. Practice accuracy before speed.'),
('แปลประโยค Please check your network connection เป็นภาษาไทย','th','กรุณาตรวจสอบการเชื่อมต่อเครือข่ายของคุณ'),
('Translate the Thai sentence กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต into English.','en','Please check your internet connection.'),
('Write a friendly two-sentence invitation to a group study session.','en','Join our group study session. We can learn together.'),
('Box A has 3 balls and box B has 5. Move 2 from B to A. How many are in each box? Explain briefly.','en','Box A has 5 balls. Box B has 3 balls.'),
]
def run(label):
    rows=[]
    for q,locale,gold in CASES:
        with patch.object(f,'_general_llm_answer_with_metadata',return_value=(gold,{'llm_kind':'general_llm','fixture':True})):
            r=answer(q,locale=locale,experimental_allow_llm=True,experimental_rag_fallback=True,global_timeout_sec=8)
        row={'question':q,'locale':locale,'gold':gold,'answer':r.answer,'mode':r.mode,'route':vars(r.route),'validation':vars(r.validation),'trace':[vars(t) for t in r.trace],'passed':gold in r.answer and 'general_llm' in r.mode}
        rows.append(row);print(locale,row['passed'],r.mode,q,flush=True)
    with (OUT/(label+'.json')).open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2,default=str)
    print('passed',sum(r['passed'] for r in rows),'/',len(rows))
if __name__=='__main__':run(sys.argv[1])
