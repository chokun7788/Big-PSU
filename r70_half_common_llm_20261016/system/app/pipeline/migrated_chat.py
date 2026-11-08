"""New-chat dispatcher: copied common content + live read-only booking adapter.

No legacy FAQ, static fee table, RAG index or model-generated factual fallback
may answer a common-data miss. Publication and approval are never written here.
"""
from __future__ import annotations
import os,time,sqlite3
from dataclasses import replace
from app.knowledge.common.answer import CommonAnswerer,database_path
from app.knowledge.common.migrated_view import MigratedView,PROFILE
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,PipelineTrace,EntityBundle,ValidationResult

def answer(question,*,locale,history=None,allow_llm=True):
 started=time.perf_counter();language=locale.effective
 audits=[]
 def finish(result,kind):
  status={'profile':PROFILE,'database':'common.sqlite','draft_preview_only':True,'production_publication_verified':False,'knowledge_source':kind,'legacy_fallback_used':False}
  hits=[{**h,'title':'ข้อมูลอ้างอิงของชุดย้าย' if language=='th' else 'Migrated source information'} for h in result.hits]
  return replace(result,hits=hits,language=locale,elapsed=time.perf_counter()-started,decision_artifact={**(result.decision_artifact or {}),'migration':status,'planner_audits':audits},trace=[*result.trace,PipelineTrace('migrated_chat','selected',1.0,'isolated copied data; no legacy content fallback',status)])
 def message(text,kind='clarification'):
  return PipelineAnswer(answer=text,hits=[],elapsed=time.perf_counter()-started,mode='pipeline:migrated_'+kind,confidence=0,route=PipelineRoute('knowledge','common_read',0,kind,'medium','migrated common content only'),entities=EntityBundle(),validation=ValidationResult(True))
 from app.pipeline.chatbot_identity import is_chatbot_greeting_query,is_chatbot_identity_query
 if is_chatbot_greeting_query(question) or is_chatbot_identity_query(question):
  text=('สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ' if language=='th' else 'Hello. I am the PSU Esports Studio - Phuket assistant. Ask about games, equipment, prices, booking, service hours, studio rules or competition rules.')
  return finish(message(text,'greeting'),'assistant_interface')
 try:
  view=MigratedView(database_path())
  from app.knowledge.common.planner import plan_fields
  def planner(q,records,ids):return plan_fields(q,records,ids,diagnostic=audits.append)
  # Try common first: its schema can distinguish static inventory from live
  # availability and a wrongly booked machine from an occupancy question.
  result=CommonAnswerer(view).answer(question,locale=language,history=history or [],planner=planner if allow_llm else None)
  if result is not None:
   if not result.validation.ok:
    # Do not present a failed candidate as a confirmed answer. Preserve why
    # it failed for analysis, and ask for the missing situation without
    # applying a broad policy to a more specific unsupported case.
    text=('ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด' if language=='th' else 'I cannot confirm an answer for the full situation you described. Please add details or split the question into separate parts.')
    clarification=message(text)
    clarification=replace(clarification,trace=result.trace,decision_artifact={'rejected_candidate':{'mode':result.mode,'validation_errors':list(result.validation.errors),'query_plan':(result.decision_artifact or {}).get('query_plan')}})
    return finish(clarification,'migrated_common')
   return finish(result,'migrated_common')
  from app.booking.live_status import is_live_booking_question
  if is_live_booking_question(question):
   from app.runtime.fast_answer import answer_live_booking_status
   live=answer_live_booking_status(question,started)
   if live is not None:
    result=PipelineAnswer(answer=live.answer,hits=live.hits,elapsed=live.elapsed,mode='pipeline:'+live.mode,confidence=live.confidence,route=PipelineRoute('reservation','live_booking_status',live.confidence,'fact','medium','live read-only booking transport'),entities=EntityBundle(),validation=ValidationResult(True),trace=[PipelineTrace('live_booking','read_only',live.confidence,'existing status adapter',live.diagnostics or {})],decision_artifact={'live_booking':live.diagnostics or {}})
    return finish(result,'live_booking')
  text=('ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด' if language=='th' else 'I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.')
  return finish(message(text),'migrated_common')
 except (OSError,sqlite3.Error,ValueError,KeyError,TypeError) as exc:
  # Missing/corrupt knowledge never switches back to the old dataset.
  result=message('ฐานข้อมูลชุดใหม่ยังอ่านไม่ได้ กรุณาลองใหม่ / The new knowledge database is unavailable. Please retry.','unavailable')
  result=replace(result,decision_artifact={'store_error_type':type(exc).__name__})
  return finish(result,'unavailable')
