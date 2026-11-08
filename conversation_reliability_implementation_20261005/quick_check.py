import sys, os, json, traceback
from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT)); os.chdir(ROOT)
os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
os.environ['PSU_CANONICAL_KNOWLEDGE']='0'
from app.session.conversation_plan import resolve_request_plan
from app.pipeline.engine import answer_question_pipeline_debug

results=[]
for locale,initial,followups in [
 ('th','ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก',['PC','ทั้งหมด','ไม่ใช่นักศึกษานะ','เอาคอมก่อน','ไม่เอา VR','ทุกบริการยกเว้น VR']),
 ('en','Service prices for external users',['PC','all of them','not a student','the PC one','all services except VR']),
 ('th','ราคา PC บุคคลทั่วไป',['แล้ว VR ล่ะ','VR คืออะไร','ไก่กับไข่อะไรเกิดก่อนกัน']),
]:
 p=resolve_request_plan(initial,locale=locale)
 for q in [initial,*followups]:
  try:
   plan=p if q==initial else resolve_request_plan(q,active_task=p['tasks'][0],locale=locale)
   result=answer_question_pipeline_debug(q,request_plan=plan,locale=locale,experimental_rag_fallback=True,experimental_allow_llm=False)
   results.append({'locale':locale,'q':q,'plan':plan,'mode':result.mode,'validation':vars(result.validation),'answer':result.answer})
   print(locale,q,result.mode,result.validation)
  except Exception:
   print(traceback.format_exc());results.append({'q':q,'error':traceback.format_exc()})
Path(__file__).with_name('quick_check_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
