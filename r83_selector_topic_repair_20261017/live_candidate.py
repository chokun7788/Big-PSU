"""Focused real-model conversations using a candidate overlay, not a full test."""
import hashlib,importlib.util,json,os,statistics,sys,time
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0')
sys.path.insert(0,str(S))
import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
import app.pipeline as pipeline_pkg
pipeline_pkg.__path__.insert(0,str(B/'candidate/app/pipeline'))
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.knowledge.common.dialogue import state_from_answer
spec=importlib.util.spec_from_file_location('r79_http',B.parent/'r79_connection_diagnostics_20261017/check_connection.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
sys.path.insert(0,str(B.parent/'r82_automatic_llm_check_20261017'))
from auto_test import Runner
boot=T/'model_readiness';boot.mkdir();boot_runner=Runner(boot)
tags=boot_runner.get('model_list','http://127.0.0.1:11434/api/tags')
warm=boot_runner.ensure_model(tags,'scb10x/typhoon2.5-qwen3-4b')
helper.emit_json(T/'MODEL_PREFLIGHT.json',warm)
if not warm.get('http_ok') or not (warm.get('body') or {}).get('done'):raise SystemExit('Real model generation preflight did not finish')
CASES=[
 ('th-personal','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ใช่ แต่เป็นเมาส์ของผม','personal')]),
 ('en-personal','en',[('Can I bring my own input peripheral?','pending'),('Yes, but it is my own keyboard.','personal')]),
 ('th-personal-phrase','th',[('ที่ศูนย์อนุญาตให้เอาอุปกรณ์อินพุตของผมไปใช้ได้ไหม','pending'),('เมาส์','personal')]),
 ('en-personal-phrase','en',[('Can I use a personal input device at the studio?','pending'),('keyboard','personal')]),
 ('th-proof','th',[('แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง','pending'),('ใช่','slip')]),
 ('en-proof','en',[('I attached incorrect proof of payment. How do I fix it?','pending'),('yes','slip')]),
 ('th-proof-phrase','th',[('ผมอัปโหลดรูปหลักฐานโอนเงินผิด ต้องแก้ยังไง','pending'),('ใช่ครับ','slip')]),
 ('en-proof-phrase','en',[('I uploaded the wrong payment attachment. How can I correct it?','pending'),('yes','slip')]),
 ('th-proof-variant','th',[('ส่งรูปยืนยันชำระเงินผิดรูป ต้องแก้ไขอย่างไร','pending'),('ใช่ครับ','slip')]),
 ('en-proof-typo','en',[('I uploded the wrong payment attachement. How can I correct it?','pending'),('yes','slip')]),
 ('en-identity','en',[('I attached incorrect proof of identity. How do I fix it?','no_slip_facts')]),
 ('en-amount','en',[('The payment amount was incorrect. How do I fix it?','no_slip_facts')]),
 ('en-studio-owned','en',[("Can I use the studio's keyboard?",'no_personal_facts')]),
 ('en-competition','en',[('Can I bring my own keyboard to a tournament?','no_personal_facts')]),
]
rows=[]
for case,lang,turns in CASES:
 history=[]
 for q,expect in turns:
  start=time.perf_counter();r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'explicit_focused_locale'),history=history,allow_llm=True);elapsed=time.perf_counter()-start
  p=(r.decision_artifact or {}).get('query_plan') or {};audit=p.get('entity_selection') or {};state=state_from_answer(r) or {};errors=[]
  ids=set(p.get('record_ids',[]))|{x['record_id'] for x in p.get('response_projection',[]) if x.get('fields') and x.get('record_id')}
  if not r.validation.ok or not r.answer.strip():errors.append('validation_or_empty')
  if expect=='pending' and not state.get('profile_confirmation'):errors.append('missing_topic_confirmation')
  if expect=='personal' and ('migrated_owner_claim_personal_keyboard_mouse' not in ids or not any(s in r.answer for s in ['ไม่อนุญาต','not allowed'])):errors.append('missing_personal_source_rule')
  if expect=='slip' and ('procedure_wrong_slip' not in ids or 'facebook.com/psuesportsphuket' not in r.answer):errors.append('missing_slip_procedure')
  if expect=='no_slip_facts' and ('facebook.com/psuesportsphuket' in r.answer or 'procedure_wrong_slip' in ids):errors.append('wrong_procedure_for_different_document_or_amount')
  if expect=='no_personal_facts' and ('migrated_owner_claim_personal_keyboard_mouse' in ids or any(s in r.answer for s in ['Personal keyboards and mice are not allowed','ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัว'])):errors.append('personal_rule_applied_to_other_scope')
  model_errors=[]
  if audit.get('availability_failure'):model_errors.append(audit['availability_failure'])
  if audit.get('semantic_selection_accepted') is False and audit.get('reason'):model_errors.append(audit['reason'])
  row={'case':case,'locale':lang,'question':q,'expect':expect,'passed':not errors,'errors':errors,'model_errors':model_errors,'seconds':round(elapsed,3),'answer':r.answer,'plan':p,'state':state,'artifact':r.decision_artifact,'hits':r.hits};rows.append(row)
  with (T/'TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
  print(json.dumps({'case':case,'question':q,'passed':not errors,'errors':errors,'model_errors':model_errors,'seconds':row['seconds'],'proposal_only':audit.get('topic_proposal_only'),'model_called':audit.get('attempted')},ensure_ascii=False),flush=True)
  history += [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state,'delivery_status':'server_written'}]
summary={'count':len(rows),'passed':sum(r['passed'] for r in rows),'real_llm_generation_verified':True,'llm_enabled':True,'format':'common','candidate_overlay':True,'actual_web_http_tested':False,'full_corpus':False,'model_call_count':sum((r['plan'].get('entity_selection') or {}).get('attempted') is True for r in rows),'proposal_calls':sum(bool((r['plan'].get('entity_selection') or {}).get('topic_proposal_only')) for r in rows),'model_failures':[{'case':r['case'],'question':r['question'],'failures':r['model_errors']} for r in rows if r['model_errors']],'failed_answers':[{'case':r['case'],'question':r['question'],'errors':r['errors']} for r in rows if not r['passed']],'database_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest()}
helper.emit_json(T/'SUMMARY.json',summary);print(json.dumps(summary,ensure_ascii=False));raise SystemExit(any(not r['passed'] for r in rows) or any(r['model_errors'] for r in rows))
