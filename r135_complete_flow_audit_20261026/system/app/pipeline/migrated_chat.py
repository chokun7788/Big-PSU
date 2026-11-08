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

def answer(question,*,locale,history=None,allow_llm=True,store=None,allow_live=True):
 from app.knowledge.common.flow_context import request_context
 from app.booking.live_status import booking_request_snapshots
 with request_context() as context, booking_request_snapshots():
  context.pin_reference_time()
  result=_answer(question,locale=locale,history=history,allow_llm=allow_llm,store=store,allow_live=allow_live)
  if (result.decision_artifact or {}).get('response_type')=='retry' and context.reserve_corrective():
   from app.knowledge.common.snapshot_provider import PinnedSnapshotView
   fresh_store=store.store if isinstance(store,PinnedSnapshotView) else store
   result=_answer(question,locale=locale,history=history,allow_llm=allow_llm,store=fresh_store,allow_live=allow_live)
  return replace(result,decision_artifact={**(result.decision_artifact or {}),'request_context':context.public()})

def _answer(question,*,locale,history=None,allow_llm=True,store=None,allow_live=True):
 from app.knowledge.common.normalized_query import normalize_query
 normalized=normalize_query(question);question=normalized.text
 from app.knowledge.common.flow_context import CURRENT
 flow_context=CURRENT.get()
 if flow_context is not None and not flow_context.input:flow_context.input={'raw_question':normalized.raw,'normalized_question':normalized.text,'span_map':normalized.public(),'requested_locale':locale.requested,'effective_locale':locale.effective}
 from app.knowledge.common.response_locale import requested_output
 target_locale=requested_output(question)
 if target_locale:locale=replace(locale,effective=target_locale,reason='explicit_answer_language')
 if flow_context is not None:flow_context.input['effective_locale']=locale.effective
 started=time.perf_counter();language=locale.effective
 audits=[];reader=None;view=store;focus=None;preview_mode=False
 from app.knowledge.common.migrated_view import PUBLISHED_PROFILE
 published_profile=os.getenv('PSU_COMMON_CHAT_PROFILE')==PUBLISHED_PROFILE
 migrated_mode=(store is None and not published_profile) or isinstance(store,MigratedView) or bool(getattr(store,'migration_preview_only',False))
 from app.pipeline.request_focus import explicit_request_focus
 parent_question=question;question,focus=explicit_request_focus(question)
 if question!=parent_question:
  from app.knowledge.common.domain_flow.request_provenance import derived_input
  derived_input(question,'explicit_request_focus',[],parent_question=parent_question)
 def finish(result,kind):
  from app.knowledge.common.result_contract import finalize
  unmatched=(result.decision_artifact or {}).get('unmatched_target') or {}
  if unmatched.get('mention'):
   from app.knowledge.common.span_binding import bind
   original=bind(normalized.raw,unmatched['mention'])
   if original:
    result=replace(result,answer=result.answer.replace('“'+unmatched['mention']+'”','“'+original['quote']+'”'),decision_artifact={**result.decision_artifact,'unmatched_target':{**unmatched,'mention':original['quote'],'source_span':original}})
  try:current_snapshot=view.snapshot() if view is not None else None
  except (OSError,sqlite3.Error,ValueError,KeyError,TypeError):current_snapshot=None
  if current_snapshot is not None and view is not None:
   snapshot_error=None
   try:fresh=view.still_current(current_snapshot)
   except (OSError,sqlite3.Error,ValueError,KeyError,TypeError) as exc:fresh=False;snapshot_error=type(exc).__name__
   if flow_context is not None:flow_context.event('S16_snapshot_check',still_current=fresh,release_id=current_snapshot.get('active'),epoch=current_snapshot.get('epoch'))
   if not fresh:
    art={**(result.decision_artifact or {}),'response_type':'unavailable' if snapshot_error else 'retry','query_plan':{'record_ids':[],'requested_fields':[],'method':'r102_snapshot_unavailable' if snapshot_error else 'r102_snapshot_changed'},'claim_packets':[],'obligations':[]}
    art['need_results']=[{**r,'status':'temporary_failure','reason_codes':['snapshot_changed_before_delivery'],'receipts':[],'claim_packets':[],
     'coverage':{**r.get('coverage',{}),'receipts':[]},'execution_contract':{}} for r in art.get('need_results',[])]
    if art.get('execution_contract'):
     from app.knowledge.common.domain_flow.native_contract import invalidate
     art['execution_contract']=invalidate(art['execution_contract'])
    result=replace(result,answer='ข้อมูลเปลี่ยนระหว่างตอบ กรุณาลองอีกครั้ง / Data changed while answering. Please retry.',hits=[],mode='pipeline:common_retry',decision_artifact=art)
  result=finalize(result,normalized.raw,current_snapshot,history)
  if current_snapshot is not None and current_snapshot.get('release') and not (result.decision_artifact or {}).get('flow_contract'):
   from app.knowledge.common.complete_flow import certify
   from app.knowledge.common.request_plan import RequestPlan,Need
   from app.knowledge.common.flow_context import request_reference_time as now_bangkok
   raw=(result.decision_artifact or {}).get('request_plan')
   if raw:
    typed=RequestPlan(raw['version'],raw['question'],[Need(**n) for n in raw['needs']],raw['scope'])
    result=certify(result,typed,current_snapshot,now_bangkok())
  art=dict(result.decision_artifact or {})
  draft=art.get('content_view')=='evaluation_draft' or migrated_mode or preview_mode
  published=art.get('content_view')=='published' and not draft
  status={'profile':PROFILE if migrated_mode else 'owner-draft-preview' if draft else 'common-published',
   'database':view.path.name if view is not None else 'common.sqlite','draft_preview_only':draft,
   'production_publication_verified':published,'knowledge_source':kind,'legacy_fallback_used':False}
  hits=[{**h,'title':'ข้อมูลอ้างอิงของชุดย้าย' if language=='th' else 'Migrated source information'} if migrated_mode else h for h in result.hits]
  art['input_normalization']=normalized.public()
  if focus:art['request_focus']=focus
  if reader is not None and reader.declined_profile_ids and kind!='live_booking':
   plan=dict(art.get('query_plan') or {})
   if not plan.get('record_ids') or plan.get('profile_confirmation'):
    plan['declined_profile_ids']=sorted(reader.declined_profile_ids)
    if not plan.get('profile_confirmation'):plan['profile_confirmation_closed']=True
    art['query_plan']=plan
  from app.knowledge.common.flow_audit import finish as finish_audit
  result=replace(result,hits=hits,language=locale,elapsed=time.perf_counter()-started,decision_artifact={**art,'migration':status,'planner_audits':audits if reader is not None else art.get('planner_audits',[]),'query_resolution':reader.diagnostics if reader is not None else art.get('query_resolution',[])},trace=[*result.trace,PipelineTrace('migrated_chat','selected',1.0,'isolated copied data; no legacy content fallback',status)])
  return finish_audit(result)
 def message(text,kind='clarification'):
  return PipelineAnswer(answer=text,hits=[],elapsed=time.perf_counter()-started,mode='pipeline:migrated_'+kind,confidence=0,route=PipelineRoute('knowledge','common_read',0,kind,'medium','migrated common content only'),entities=EntityBundle(),validation=ValidationResult(True))
 from app.pipeline.chatbot_identity import is_chatbot_greeting_query,is_chatbot_identity_query
 if is_chatbot_greeting_query(question) or is_chatbot_identity_query(question):
  text=('สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ' if language=='th' else 'Hello. I am the PSU Esports Studio - Phuket assistant. Ask about games, equipment, prices, booking, service hours, studio rules or competition rules.')
  return finish(message(text,'greeting'),'assistant_interface')
 try:
  from app.knowledge.common.snapshot_provider import PinnedSnapshotView
  if view is None:
   from app.knowledge.common.store import CommonStore
   view=CommonStore(database_path()) if published_profile else MigratedView(database_path())
  if not isinstance(view,PinnedSnapshotView):view=PinnedSnapshotView(view)
  if not view.snapshot().get('release'):
   body='ยังไม่มีชุดข้อมูลที่อนุมัติและเผยแพร่สำหรับแชทนี้ครับ ผู้ดูแลต้องเผยแพร่ข้อมูลจากหน้าจัดการก่อน' if language=='th' else 'No approved knowledge release has been published for this chat. The administrator needs to publish the data in the owner editor first.'
   result=message(body,'unconfirmed')
   result=replace(result,decision_artifact={'response_type':'unconfirmed','content_view':'published','publication_empty':True})
   return finish(result,'common_published_empty')
  preview_mode=bool(view.snapshot().get('evaluation_draft_only'))
  from app.knowledge.common.followup_scope import competition_question,delivered_state
  resume=None
  if (delivered_state(history) or {}).get('pending_competition_scope'):
   from app.knowledge.common.flow_context import request_reference_time as now_bangkok
   snap_for_resume=view.snapshot();rs_for_resume=snap_for_resume['release']['records'];at_for_resume=now_bangkok()
   resume=competition_question(question,history,{k:r for k,r in rs_for_resume.items() if effective(r,at_for_resume,rs_for_resume)},snap_for_resume['release']['names'])
  if resume:
   if resume.get('expired'):
    return finish(message('ข้อมูลหัวข้อเปลี่ยนไป กรุณาระบุเรื่องที่ต้องการอีกครั้งครับ' if language=='th' else 'The topic scope has changed. Please specify your question again.'),'migrated_common')
   result=answer(resume['question'],locale=locale,history=[],allow_llm=allow_llm,store=view,allow_live=allow_live)
   art=dict(result.decision_artifact or {});art['dialogue_repair']={'method':'qualified_competition_game_selection','original_input':question,'active_query':resume['question'],'inherited_scope':resume['inherited_scope'],'candidate_competition_ids':resume['competition_ids'],'previous_answer_facts_used':False}
   return finish(replace(result,decision_artifact=art),'migrated_common')
  from app.knowledge.common.profile_confirmation import latest,resolve as resolve_confirmation
  from app.knowledge.common.reply_repair import rejection,barrier,declined_from_history
  from app.knowledge.common.qualified_reply import qualification
  if latest(history) and (rejection(question) or qualification(question)):
   from app.knowledge.common.flow_context import request_reference_time as now_bangkok
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
     result=answer(active_query,locale=locale,history=barrier(declined),allow_llm=allow_llm,store=view,allow_live=allow_live)
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
  def external_need(q):
   # Reuse the approved live adapter inside multi-need execution. Never read
   # static occupancy as a fallback and never enable live in owner preview.
   if not allow_live:
    r=message('หน้านี้ยังไม่ได้อ่านสถานะจองสดครับ' if language=='th' else 'Live booking is not read in this preview.','live_unavailable')
    return replace(r,decision_artifact={'response_type':'live_unavailable','live_booking':{'attempted':False,'reason':'content_preview_no_live_provider'}})
   from app.runtime.fast_answer import answer_live_booking_status
   live=answer_live_booking_status(q,started)
   if live is None:return None
   return PipelineAnswer(answer=live.answer,hits=live.hits,elapsed=live.elapsed,mode='pipeline:'+live.mode,confidence=live.confidence,route=PipelineRoute('reservation','live_booking_status',live.confidence,'fact','medium','live read-only booking transport'),entities=EntityBundle(),validation=ValidationResult(True),decision_artifact={'live_booking':live.diagnostics or {}})
  reader=CommonAnswerer(view,external_executor=external_need)
  result=reader.answer(question,locale=language,history=history or [],planner=planner if allow_llm else None)
  if result is not None:
   if not result.validation.ok:
    # Do not present a failed candidate as a confirmed answer. Preserve why
    # it failed for analysis, and ask for the missing situation without
    # applying a broad policy to a more specific unsupported case.
    rejected={'mode':result.mode,'validation_errors':list(result.validation.errors),'query_plan':(result.decision_artifact or {}).get('query_plan'),'request_plan':(result.decision_artifact or {}).get('request_plan'),'need_results':(result.decision_artifact or {}).get('need_results')}
    # A short FAQ alias can consume an unrelated task (e.g. a payment-method
    # alias inside a wrong-attachment question). Keep rejecting the factual
    # answer, but preserve a usable confirmation state for a declared topic.
    if 'unresolved_query_clause' in result.validation.errors:
     from app.knowledge.common.flow_context import request_reference_time as now_bangkok
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
  if is_live_booking_question(question) and not allow_live:
   text=('หน้านี้ตรวจเฉพาะข้อมูลที่เลือก ยังไม่ได้อ่านสถานะจองสด กรุณาตรวจสถานะเครื่องในหน้าแชทที่เชื่อมระบบจอง' if language=='th' else 'This preview checks the selected content only. Live booking availability is not read here; check it in the booking-connected chat.')
   result=message(text,'live_unavailable')
   result=replace(result,decision_artifact={'response_type':'live_unavailable','live_booking':{'attempted':False,'reason':'content_preview_no_live_provider'}})
   return finish(result,'live_booking_not_read')
  if is_live_booking_question(question):
   from app.runtime.fast_answer import answer_live_booking_status
   live=answer_live_booking_status(question,started)
   if live is not None:
    result=PipelineAnswer(answer=live.answer,hits=live.hits,elapsed=live.elapsed,mode='pipeline:'+live.mode,confidence=live.confidence,route=PipelineRoute('reservation','live_booking_status',live.confidence,'fact','medium','live read-only booking transport'),entities=EntityBundle(),validation=ValidationResult(True),trace=[PipelineTrace('live_booking','read_only',live.confidence,'existing status adapter',live.diagnostics or {})],decision_artifact={'live_booking':live.diagnostics or {}})
    return finish(result,'live_booking')
  from app.knowledge.common.target_selection import unmatched_mention
  final_snap=view.snapshot();final_records=final_snap['release']['records'];unknown=unmatched_mention(normalized.raw,final_records,final_snap['release']['names'])
  if unknown:
   text=('ยังไม่พบรายการเกมที่ตรงกับ “'+unknown+'” ในข้อมูลชุดนี้ครับ จึงยังยืนยันบริการสำหรับเกมนี้ไม่ได้' if language=='th' else 'No game record matching “'+unknown+'” was found in this data set, so its studio offering is not confirmed.')
   result=message(text,'unconfirmed');result=replace(result,mode='pipeline:common_unknown_target',decision_artifact={'response_type':'unconfirmed','public_response_kind':'no_answer','unmatched_target':{'mention':unknown,'reason':'no_catalog_match','scope':'current_common_release'}})
   return finish(result,'migrated_common')
  text=('ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด' if language=='th' else 'I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.')
  return finish(message(text),'migrated_common')
 except (OSError,sqlite3.Error,ValueError,KeyError,TypeError) as exc:
  # Missing/corrupt knowledge never switches back to the old dataset.
  result=message('ฐานข้อมูลชุดใหม่ยังอ่านไม่ได้ กรุณาลองใหม่' if language=='th' else 'The new knowledge database is unavailable. Please retry.','unavailable')
  result=replace(result,decision_artifact={'store_error_type':type(exc).__name__})
  return finish(result,'unavailable')
