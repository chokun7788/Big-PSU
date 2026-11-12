"""Experimental whole-question model planner, then source-checked readers.

No regex clause splitter runs before this model call. Model plans are proposals,
not source facts. Unavailable/invalid model output never silently becomes a
successful legacy whole-question answer. Free-form answer rewriting is deferred.
"""
import json,os,time,types,re
from dataclasses import replace

def schema():
 return {'type':'array','minItems':1,'maxItems':8,'items':{'type':'array','minItems':3,'maxItems':3,'prefixItems':[{'type':'string','enum':list(CODES)},{'type':'integer','minimum':0},{'type':'integer','minimum':0}]}}

CODES={'Z':('C04','detail','zone','none'),'S':('C04','detail','studio_services','none'),'R':('C12','availability','live_status','ready_support_or_live'),'L':('C12','availability','live_status','none'),'P':('C06','detail','amount','none'),'B':('C08','detail','owner_policy','none'),'G':('C04','list','game_catalog','none'),'C':('C05','control','input_bindings','none'),'E':('C03','detail','location','none'),'D':('C04','detail','summary','none'),'Q':(None,'detail','','unspecified')}

def chunks(question):return [{'start':m.start(),'end':m.end(),'text':m[0]} for m in re.finditer(r'\S+',question)]

def parse(content,question):
 needs=json.loads(content);pieces=chunks(question);seen=set();out=[]
 if not isinstance(needs,list) or not 1<=len(needs)<=8:raise ValueError('invalid_need_count')
 for item in needs:
  if not isinstance(item,list) or len(item)!=3:raise ValueError('invalid_compact_need')
  code,a,b=item
  if code not in CODES or type(a) is not int or type(b) is not int or not 0<=a<=b<len(pieces):raise ValueError('invalid_code_or_raw_chunk_range')
  if (code,a,b) in seen:raise ValueError('duplicate_identical_need')
  seen.add((code,a,b));start=pieces[a]['start'];end=pieces[b]['end'];quote=question[start:end]
  cat,op,facet,ambiguity=CODES[code]
  out.append({'quote':quote,'category':cat,'operation':op,'facet':facet,'target':'','ambiguity':ambiguity,'source_span':{'start':start,'end':end,'text':quote}})
 return out

def execute_typed(reader,engine,quote,meaning,snap,started,at,lang):
 """Read the proposed operation without a second native intent planner.

 Source readers, arithmetic, scope receipts and obligations stay in force.
 No corrective task may silently replace a wrong model category with another.
 """
 from .domain_flow.plan_contract import compile_request
 from .domain_flow.capabilities import dispatch
 from .domain_flow.obligation_verifier import assess,withhold_delivery
 from .domain_flow.readers import blocked
 from .domain_flow.result_contract import package as executor_package
 from .domain_flow.integration import package
 from .domain_flow.terminal_states import PUBLIC
 from .domain_flow.understanding import Understanding
 from .flow_context import request_reference_time
 ref=request_reference_time(at);identity={'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),'reference_time':ref.isoformat()}
 proposed=Understanding([meaning],True,'model_first_typed_operation',{'model_called':True})
 compiled=compile_request(quote,proposed,engine.index,identity);task=compiled.tasks[0]
 plan=blocked(task.category,'invalid_compiled_scope','missing_input') if task.errors else dispatch(engine,task,meaning,quote,ref)
 if plan.ambiguous:plan=blocked(task.category,'model_first_source_selection_unresolved','missing_source')
 plan=engine.finish_plan(task.category,quote,plan,ref)
 child=engine._render_one(task.category,quote,lang,plan,ref);child.update(question=quote,execution_query=quote)
 ledger=assess(engine.index,task,child,identity,quote)
 if ledger['fatal']:
  child=engine._render_one(task.category,quote,lang,blocked(task.category,'source_receipt_verification_failed'),ref);child.update(question=quote,execution_query=quote)
  ledger=withhold_delivery(ledger,'source_receipt_verification_failed','invalid_plan')
 elif any(o.get('kind')=='requested_operation' and o.get('fulfilled') is not True for o in ledger.get('obligations',[])):
  child=engine._render_one(task.category,quote,lang,blocked(task.category,'requested_operation_not_satisfied'),ref);child.update(question=quote,execution_query=quote)
  ledger=withhold_delivery(ledger,'requested_operation_not_satisfied','missing_source')
 child['execution_contract']=ledger;child['executor_result']=executor_package(task,ledger,child,identity)
 state=ledger['terminal_state'];status={'supported':'answer','partial':'partial','missing_input':'missing_input','not_current':'not_current','model_unavailable':'unavailable'}.get(state,'missing_source')
 result={'answer':child['answer'],'status':status,'terminal_state':state,'claims':child.get('claims',[]),'needs':[child],'model_events':[],'understanding':proposed.as_dict(),'fixture':False,'english_translation_missing':False,'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),'execution_contract':{'version':'model_first_source_executor_v1','request_plan':compiled.as_dict(),'tasks':[ledger],'executor_results':[child['executor_result']],'whole_question_semantics_verified':False}}
 return package(reader,snap,started,quote,result)

def answer(reader,question,locale,history,at,snapshot):
 from .flow_context import CURRENT
 from .domain_flow.engine import Engine,language
 from .domain_flow.model_gateway import call
 from .domain_flow.understanding import DOMAINS,FACETS,MeaningTask,Understanding
 from .domain_flow.contracts import RequestBudget
 from .domain_flow.integration import answer as domain_answer,TASKS
 from .domain_flow.request_provenance import derived_input
 from .domain_flow.source_decisions import guard_result
 from .request_plan import Need,RequestPlan,VERSION,aggregate
 started=time.perf_counter();ctx=CURRENT.get();raw=ctx.input.get('raw_question',question) if ctx else question
 snap=snapshot if snapshot is not None else reader.store.snapshot();lang=language(raw,locale)
 if not snap.get('release'):return reader.finish(snap,started,'ยังไม่มี snapshot สำหรับทดลองครับ',[],{'method':'model_first_no_snapshot'},[],response='unavailable')
 if ctx:ctx.bind_snapshot(snap)
 engine=Engine.from_snapshot(snap,cache_key=reader.store.path.resolve())
 instructions=('ตีโจทย์ทุกคำถามย่อยในข้อความเต็ม ห้ามตอบข้อเท็จจริง ส่งเฉพาะ JSON array แต่ละงานคือ [รหัส,indexเริ่ม,indexจบ] โดยindexอ้างอิงชิ้นข้อความที่ให้ (รวมปลายทั้งคู่). ชิ้นข้อความแบ่งเพียงช่องว่าง ไม่ใช่การแบ่งเจตนา คุณเป็นผู้ตัดสินจำนวนงานเอง หนึ่งช่วงมีหลายงานได้. รหัส Z=ถามที่ตั้งหรือโซนเท่านั้น,S=เครื่องหรือบริการที่รองรับเกมแบบข้อมูลคงที่,R=พร้อมเล่นยังไม่ชัดว่ารองรับหรือว่างสด,L=ว่าง/ถูกจอง ณ วันเวลาที่ถาม,P=ราคา/ค่าใช้จ่าย/เสียกี่บาท,B=วิธีจอง,G=รายชื่อเกม,C=ปุ่มควบคุมเกม,E=ตำแหน่งอุปกรณ์,D=ข้อมูลเกม,Q=ไม่ชัดหรือนอกขอบเขต. ราคาแม้มีชื่อโซนก็ต้องPไม่ใช่Z. คำถามว่างตอนนี้ต้องLไม่ใช่S. คำว่าพร้อมโดยไม่ระบุว่ารองรับหรือว่างให้R. ถามสองเรื่องต้องสองงาน. ตัวอย่าง 0=VR,1=ราคาเท่าไหร่,2=แล้วจองยังไง ตอบ [["P",0,1],["B",2,2]]. ตัวอย่าง 0=PS5,1=ว่างพรุ่งนี้ไหม ตอบ [["L",0,1]]. JSONเท่านั้น ไม่อธิบาย.')
 model=os.getenv('PSU_CHATBOT_OLLAMA_MODEL','psu-r129:latest');client=types.SimpleNamespace(model=model,timeout=35,http_attempted=False,admission={})
 payload={'model':model,'stage':'model_first_plan','messages':[{'role':'system','content':instructions},{'role':'user','content':json.dumps({'raw_question':raw,'chunks':{str(n):p['text'] for n,p in enumerate(chunks(raw))}},ensure_ascii=False)}],'format':schema(),'stream':False,'think':False,'keep_alive':'30m','options':{'temperature':0,'seed':135,'num_ctx':8192,'num_predict':160}}
 audit={'version':1,'planner':'actual_local_model_whole_question','model':model,'raw_question':raw,'legacy_splitter_used_before_model':False,'rendering':'existing_verified_source_blocks','free_form_model_rendering_enabled':False}
 try:
  response=call(client,payload);audit['raw_model_content']=response.get('message',{}).get('content','');audit['returned_provenance']=response.get('provenance',{});audit['transport_completed']=True;audit['http_attempted']=client.http_attempted
  needs=parse(audit['raw_model_content'],raw);audit['validated_needs']=needs
 except (OSError,ValueError,TypeError,KeyError) as exc:
  audit.update(failure_type=type(exc).__name__,failure=str(exc),http_attempted=client.http_attempted)
  body='โมเดลตีโจทย์ไม่พร้อมหรือส่งแผนที่ตรวจไม่ผ่านในรอบนี้ จึงยังไม่ตอบแทนด้วยเส้นทางกฎเดิมครับ' if lang=='th' else 'The model planner was unavailable or returned an invalid plan; this trial did not silently substitute a legacy answer.'
  result=reader.finish(snap,started,body,[],{'method':'model_first_planner_failure'},[],response='unavailable')
  return replace(result,decision_artifact={**result.decision_artifact,'model_first':audit})
 outputs=[];public_needs=[]
 for n,item in enumerate(needs,1):
  quote=item['quote'];nid='model_n'+str(n);cat=item['category'];public_needs.append(Need(nid,TASKS.get(cat,'unresolved'),quote,quote,[],[],predicate=item['facet']))
  derived_input(quote,'compiled_parent_task',[{'source_span':item['source_span']}],index=engine.index,parent_question=raw)
  if cat is None or item['ambiguity']!='none':
   body=('คำว่า “พร้อมให้เล่น” หมายถึงเครื่องที่รองรับเกม หรือเครื่องที่ว่างในวันและเวลาใดครับ?' if lang=='th' else 'Does ready to play mean machines supporting the game, or machines free at a particular date and time?') if item['ambiguity']=='ready_support_or_live' else ('กรุณาระบุรายละเอียดส่วนนี้เพิ่มเติมครับ: ' if lang=='th' else 'Please clarify this part: ')+quote
   result=reader.finish(snap,started,body,[],{'method':'model_first_need_clarification','missing_slots':['requested_scope']},[],response='clarification')
   result=replace(result,decision_artifact={**result.decision_artifact,'need_results':[{'need_id':nid,'task':TASKS.get(cat,'unresolved'),'source_span':quote,'status':'needs_user_slot','reason_codes':['model_proposed_scope_ambiguity'],'claim_packets':[],'receipts':[]}]})
  else:
   domain=next(k for k,v in DOMAINS.items() if v[0]==cat)
   meaning=MeaningTask(quote,domain,cat,item['operation'],item['facet'],item['target'] if item['target'] in quote else '')
   proposed=Understanding([meaning],True,'model_first_validated_literal_plan',{'method':'model_first_plan','model_called':True,'whole_question_semantics_verified':False})
   result=domain_answer(reader,quote,locale=lang,history=None,at=at,planner=None,_composing=True,_snapshot=snap,_budget=RequestBudget(max_model_calls=0),_understanding=proposed) if cat=='C12' else execute_typed(reader,engine,quote,meaning,snap,started,at,lang)
   if result is None:result=reader.finish(snap,started,'ยังไม่มีตัวอ่านข้อมูลที่รองรับส่วนนี้ครับ' if lang=='th' else 'No verified reader is available for this need.',[],{'method':'model_first_reader_missing'},[],response='unconfirmed')
   result=guard_result(reader,result,snap,engine.index,quote,at,lang)
   if item['facet']=='studio_services' and result.hits:
    note='รายการนี้ยืนยันเพียงบริการที่มีเกม ไม่ใช่สถานะว่าเครื่องว่างตอนนี้ครับ' if lang=='th' else 'These are recorded services offering the game, not a confirmation that their machines are free now.'
    result=replace(result,answer=result.answer+'\n'+note)
  outputs.append(result)
 plan=RequestPlan(VERSION,raw,public_needs,{'source':'model_first_proposal_then_pinned_source_readers','model_plan_not_semantic_proof':True})
 result=aggregate(reader,snap,started,plan,outputs,lang)
 partial=any((r.decision_artifact or {}).get('response_type')!='answer' for r in outputs)
 if partial:
  art={**result.decision_artifact,'response_type':'partial_answer'}
  art['need_results']=[{**row,'status':'partial_supported'} if (r.decision_artifact or {}).get('response_type')!='answer' and row.get('status') in {'supported','scope_unverified'} else row for row,r in zip(art.get('need_results',[]),outputs)]
  result=replace(result,mode='pipeline:common_partial_answer',route=replace(result.route,answer_type='partial_answer'),decision_artifact=art)
 audit['reader_outcomes']=[{'need_id':n.id,'mode':r.mode,'response_type':(r.decision_artifact or {}).get('response_type'),'source_hits':len(r.hits)} for n,r in zip(public_needs,outputs)]
 return replace(result,decision_artifact={**result.decision_artifact,'model_first':audit})
