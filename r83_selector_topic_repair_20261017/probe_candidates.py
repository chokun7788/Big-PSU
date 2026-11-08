import json,os,sys
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_CHAT_LOG_DIR=str(B/'probe_logs'),PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0')
sys.path.insert(0,str(S))
import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
from app.knowledge.common import entity_search as e
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.semantic_profile import profile
from app.knowledge.common.profile_confirmation import eligible
release=MigratedView(S/'data/knowledge/common.sqlite').snapshot()['release'];records=release['records'];names=release['names']
QUESTIONS=[
 'ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','Can I bring my own input peripheral?',
 'I attached incorrect proof of payment. How do I fix it?','แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง',
 'Can I use a personal input device at the studio?',
 'ที่ศูนย์อนุญาตให้เอาอุปกรณ์อินพุตของผมไปใช้ได้ไหม',
 'I uploaded the wrong payment attachment. How can I correct it?',
 'The payment picture I submitted is incorrect. What should I do?',
 'ผมอัปโหลดรูปหลักฐานโอนเงินผิด ต้องแก้ยังไง',
 'ส่งรูปยืนยันชำระเงินผิดรูป ต้องแก้ไขอย่างไร',
 'I attached incorrect proof of identity. How do I fix it?',
 'ผมโอนเงินผิดจำนวน ต้องแก้ยังไง',
 "Can I use the studio's keyboard?",'Can I bring my own keyboard to a tournament?',
 'I want to bring my own laptop. Is that allowed?',
]
out=[]
for q in QUESTIONS:
 rows=e.candidates(q,records,names);compatible=eligible(q,records);kept=[];dropped=[]
 for row in rows:
  rid=row['record_id'];ok,terms=e.topic_alignment(q,records[rid]);item={'id':rid,'score':row['score'],'profile':bool(profile(records[rid])),'topic_terms':terms}
  (kept if ok or item['profile'] else dropped).append(item)
 entry={'question':q,'before':len(rows),'after':len(kept),'kept':kept,'dropped':dropped,'compatible':compatible};out.append(entry)
 print(json.dumps(entry,ensure_ascii=False),flush=True)
with (B/'CANDIDATE_AUDIT.json').open('x',encoding='utf8') as f:json.dump(out,f,ensure_ascii=False,indent=2)
