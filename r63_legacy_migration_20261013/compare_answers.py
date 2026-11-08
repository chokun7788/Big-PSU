"""Compare original owner facts with DRAFT common responses; no publications."""
import json,os,sys,time,dataclasses
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent;SYSTEM=BASE/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local';sys.path.insert(0,str(SYSTEM))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import preview_answer
OUT=Path(sys.argv[1]).resolve();ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
os.environ['PSU_LOCAL_LLM_ASSIST_ENABLED']='0'
store=CommonStore(OUT/'review/approved.sqlite')
raw=json.loads((ROOT/'data/sources/user_service_answers_20261008.json').read_text(encoding='utf-8'))
curated=json.loads((ROOT/'data/curated/user_service_facts_20261008.json').read_text(encoding='utf-8'))
checks=[]
for key,claim in curated['claims'].items():
 if claim.get('status')!='user_confirmed':continue
 item=next(x for x in raw['items'] if x['number'] in claim['source_items']);question=item['question']
 result=preview_answer(store,question,draft=True)
 expected=claim['answers']['th'];actual=result.answer if result else None
 checks.append({'question':question,'source_item':item['number'],'expected_original':item['answer'],'expected_curated':expected,'answer':actual,'passed':bool(actual and expected in actual),'decision':dataclasses.asdict(result.decision_artifact) if result and dataclasses.is_dataclass(result.decision_artifact) else result.decision_artifact if result else None})
extras=[('Gaming PC รุ่น MSI MAG Infinite S3 14th ข้อมูลทั้งหมด','usage','equipment_gaming_pc'),('Animal Crossing วิธีเล่น','how_to_play','game_detail_animal_crossing')]
for question,key,rid in extras:
 result=preview_answer(store,question,draft=True);expect=store.get(rid)['record']['fields'][key]['value']['th'];actual=result.answer if result else None
 checks.append({'question':question,'expected':expect,'answer':actual,'passed':bool(actual and expect in actual)})
report={'passed':sum(x['passed'] for x in checks),'total':len(checks),'llm_enabled':False,'scope':'exact original Thai owner questions + explicit full/details fields, not all paraphrases','cases':checks}
(OUT/'DRAFT_QUESTIONS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
print(json.dumps({'passed':report['passed'],'total':report['total'],'failures':[x['question'] for x in checks if not x['passed']]},ensure_ascii=False))
