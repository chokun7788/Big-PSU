"""Task grammar contrasts; source data remains unchanged."""
import json,os,sys
from pathlib import Path
B=Path(__file__).resolve().parent;T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(B/'system/data/knowledge/common.sqlite'),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_BILINGUAL_EN_ENABLED='1')
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.question_profiles import tasks,select
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.profile_confirmation import build,resolve
rs=MigratedView(B/'system/data/knowledge/common.sqlite').snapshot()['release']['records']
rows=[]
for q,expected in [
 ('What is the correct file format for a slip?',False),
 ('Which slip format is correct?',False),
 ('Is this the correct slip?',False),
 ('What is the correct proof of payment format?',False),
 ('How do I correct the slip?',True),
 ('Can I correct my slip?',True),
 ('Please correct my slip.',True),
 ('I need to correct a wrong slip.',True),
 ('The slip was incorrect. What should I do?',True),
 ('Correct my slip.',True),
 ('แนบสลิปผิด ต้องแก้ยังไง',True),
 ('รูปสลิปที่ถูกต้องใช้ไฟล์แบบไหน',False)]:
    selected,audit=select(q,rs);passed=('correction' in tasks(q))==expected and (expected or selected is None)
    rows.append({'question':q,'expected_correction_task':expected,'passed':passed,'tasks':sorted(tasks(q)),'selection':audit})
pending=build('I attached incorrect proof of payment. How do I fix it?',rs)
history=[{'role':'assistant','delivery_status':'server_written','common_read_state':{'schema_version':1,'profile_confirmation':pending}}]
for q in ('No, I mean proof of identity.','ไม่ใช่ครับ หมายถึงบัตรประชาชน','ไม่ใช่หมายถึงอันอื่น','not that, another topic'):
    result=resolve(q,history,rs)
    rows.append({'question':q,'passed':bool(result and result['action']=='cancel'),'scope':'reject pending topic; does not assert an answer for the added detail','result':result})
(T/'RESULTS.json').write_text(json.dumps({'count':len(rows),'passed':sum(r['passed'] for r in rows),'scope':'task classification and literal-profile rejection only, not full answer or model accuracy','cases':rows},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'count':len(rows),'passed':sum(r['passed'] for r in rows)}));raise SystemExit(any(not r['passed'] for r in rows))
