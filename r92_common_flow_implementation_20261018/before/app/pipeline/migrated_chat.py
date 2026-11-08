"""New-chat dispatcher: copied common content + live read-only booking adapter.

No legacy FAQ, static fee table, RAG index or model-generated factual fallback
may answer a common-data miss. Publication and approval are never written here.
"""
from __future__ import annotations
import os,time,sqlite3
from dataclasses import replace
from app.knowledge.common.answer import CommonAnswerer,database_path,effective
from app.knowledge.common.migrated_view import MigratedView,PROFILE
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,PipelineTrace,EntityBundle,ValidationResult

def answer(question,*,locale,history=None,allow_llm=True):
 started=time.perf_counter();language=locale.effective
 audits=[];reader=None
 def finish(result,kind):
  status={'profile':PROFILE,'database':'common.sqlite','draft_preview_only':True,'production_publication_verified':False,'knowledge_source':kind,'legacy_fallback_used':False}
  hits=[{**h,'title':'ข้อมูลอ้างอิงของชุดย้าย' if language=='th' else 'Migrated source information'} for h in result.hits]
  art=dict(result.decision_artifact or {})
  if reader is not None and reader.declined_profile_ids and kind!='live_booking':
   plan=dict(art.get('query_plan') or {})
   if not plan.get('record_ids') or plan.get('profile_confirmation'):
    plan['declined_profile_ids']=sorted(reader.declined_profile_ids)
    if not plan.get('profile_confirmation'):plan['profile_confirmation_closed']=True
    art['query_plan']=plan
  return replace(result,hits=hits,language=locale,elapsed=time.perf_counter()-started,decision_artifact={**art,'migration':status,'planner_audits':audits if reader is not None else art.get('planner_audits',[]),'query_resolution':reader.diagnostics if reader is not None else art.get('query_resolution',[])},trace=[*result.trace,PipelineTrace('migrated_chat','selected',1.0,'isolated copied data; no legacy content fallback',status)])
 def message(text,kind='clarification'):
  return PipelineAnswer(answer=text,hits=[],elapsed=time.perf_counter()-started,mode='pipeline:migrated_'+kind,confidence=0,route=PipelineRoute('knowledge','common_read',0,kind,'medium','migrated common content only'),entities=EntityBundle(),validation=ValidationResult(True))
 from app.pipeline.chatbot_identity import is_chatbot_greeting_query,is_chatbot_identity_query
 if is_chatbot_greeting_query(question) or is_chatbot_identity_query(question):
  text=('สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ' if language=='th' else 'Hello. I am the PSU Esports Studio - Phuket assistant. Ask about games, equipment, prices, booking, service hours, studio rules or competition rules.')
  return finish(message(text,'greeting'),'assistant_interface')
 try:
  view=MigratedView(database_path())
  from app.knowledge.common.followup_scope import competition_question,delivered_state
  resume=None
  if (delivered_state(history) or {}).get('pending_competition_scope'):
   from app.calendar.service_calendar import now_bangkok
   snap_for_resume=view.snapshot();rs_for_resume=snap_for_resume['release']['records'];at_for_resume=now_bangkok()
   resume=competition_question(question,history,{k:r for k,r in rs_for_resume.items() if effective(r,at_for_resume,rs_for_resume)},snap_for_resume['release']['names'])
  if resume:
   if resume.get('expired'):
    return finish(message('ข้อมูลหัวข้อเปลี่ยนไป กรุณาระบุเรื่องที่ต้องการอีกครั้งครับ' if language=='th' else 'The topic scope has changed. Please specify your question again.'),'migrated_common')
   result=answer(resume['question'],locale=locale,history=[],allow_llm=allow_llm)
   art=dict(result.decision_artifact or {});art['dialogue_repair']={'method':'qualified_competition_game_selection','original_input':question,'active_query':resume['question'],'inherited_scope':resume['inherited_scope'],'candidate_competition_ids':resume['competition_ids'],'previous_answer_facts_used':False}
   return finish(replace(result,decision_artifact=art),'migrated_common')
  from app.knowledge.common.profile_confirmation import latest,resolve as resolve_confirmation
  from app.knowledge.common.reply_repair import rejection,barrier,declined_from_history
  from app.knowledge.common.qualified_reply import qualification
  if latest(history) and (rejection(question) or qualification(question)):
   from app.calendar.service_calendar import now_bangkok
   snap=view.snapshot();rs=snap['release']['records'];at=now_bangkok()
   repair=resolve_confirmation(question,history,{rid:r for rid,r in rs.items() if effective(r,at,rs)})
   if repair and repair['action'] in {'rephrase','qualified_request'}:
    active_query=repair['replacement'];declined=declined_from_history(history)|set(repair['declined_profile_ids'])
    # Re-enter the dispatcher so booking/live adapters, greeting and normal
    # source validation see the replacement, not the rejected old question.
    # Reapply product scope because the outer input began with "no".
    from app.pipeline.studio_scope import is_explicit_unrelated_task
    from app.pipeline.query_signals import looks_like_explicit_creation_request
    from app.pipeline.semantic_quality import translation_request
    translation=translation_request(active_query)
    if is_explicit_unrelated_task(active_query) or looks_like_explicit_creation_request(active_query) or (translation and translation['source']):
     body=('ผมช่วยตอบข้อมูลของ PSU Esports Studio - Phuket เช่น เกม อุปกรณ์ ราคา การจอง เวลาให้บริการ และกฎของศูนย์ครับ' if language=='th' else 'I answer questions about PSU Esports Studio - Phuket: games, equipment, prices, booking, service hours and studio rules.')
     result=message(body,'scope')
    else:
     result=answer(active_query,locale=locale,history=barrier(declined),allow_llm=allow_llm)
    art=dict(result.decision_artifact or {});plan=dict(art.get('query_plan') or {})
    unresolved=not plan.get('record_ids') or bool(plan.get('profile_confirmation'))
    plan['declined_profile_ids']=sorted(declined) if unresolved else []
    if unresolved and not plan.get('profile_confirmation'):plan['profile_confirmation_closed']=True
    art['query_plan']=plan
    art['dialogue_repair']={'method':'qualified_reply_new_request' if repair['action']=='qualified_request' else 'rejected_topic_with_replacement','original_input':question,'active_query':active_query,
        'rejected_profile_ids':sorted(declined),'previous_answer_facts_used':False,'old_context_inherited':False}
    result=replace(result,decision_artifact=art,trace=[*result.trace,PipelineTrace('dialogue_repair','replacement_query',1.0,'explicit user replacement after topic rejection',art['dialogue_repair'])])
    return finish(result,art.get('migration',{}).get('knowledge_source','migrated_common'))
  from app.knowledge.common.planner import plan_fields
  def planner(q,records,ids):return plan_fields(q,records,ids,diagnostic=audits.append)
  # Try common first: its schema can distinguish static inventory from live
  # availability and a wrongly booked machine from an occupancy question.
  reader=CommonAnswerer(view)
  result=reader.answer(question,locale=language,history=history or [],planner=planner if allow_llm else None)
  if result is not None:
   if not result.validation.ok:
    # Do not present a failed candidate as a confirmed answer. Preserve why
    # it failed for analysis, and ask for the missing situation without
    # applying a broad policy to a more specific unsupported case.
    rejected={'mode':result.mode,'validation_errors':list(result.validation.errors),'query_plan':(result.decision_artifact or {}).get('query_plan')}
    # A short FAQ alias can consume an unrelated task (e.g. a payment-method
    # alias inside a wrong-attachment question). Keep rejecting the factual
    # answer, but preserve a usable confirmation state for a declared topic.
    if 'unresolved_query_clause' in result.validation.errors:
     from app.calendar.service_calendar import now_bangkok
     fresh=view.snapshot();rs=fresh['release']['records'];current_at=now_bangkok()
     current={rid:r for rid,r in rs.items() if effective(r,current_at,rs)}
     audit={'attempted':False,'reason':'named_source_failed_request_coverage','intent_verified':False,
         'rejected_scope_ids':(rejected['query_plan'] or {}).get('record_ids',[]),'failed_validation':rejected['validation_errors']}
     confirmation=reader.confirm_profile(fresh,started,question,language,current,audit)
     if confirmation is not None:
      art={**(confirmation.decision_artifact or {}),'rejected_candidate':rejected}
      return finish(replace(confirmation,decision_artifact=art),'migrated_common')
    text=('ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด' if language=='th' else 'I cannot confirm an answer for the full situation you described. Please add details or split the question into separate parts.')
    clarification=message(text)
    clarification=replace(clarification,trace=result.trace,decision_artifact={'rejected_candidate':rejected})
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
  result=message('ฐานข้อมูลชุดใหม่ยังอ่านไม่ได้ กรุณาลองใหม่' if language=='th' else 'The new knowledge database is unavailable. Please retry.','unavailable')
  result=replace(result,decision_artifact={'store_error_type':type(exc).__name__})
  return finish(result,'unavailable')
