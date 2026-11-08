"""Stored delivery/session evidence and immutable raw-input span controls."""
import copy,json,os,time
from verification_support import R,snapshot
out=R/('request_context_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'isolated_default_state.sqlite')
from app.session.conversation_store import ConversationStore,TurnConflict
from app.knowledge.common.followup_scope import delivered_state
from app.knowledge.common.domain_flow.dialogue_task import resolve
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.domain_flow.request_provenance import capture,map_span
clock=reference_time('2026-10-26T12:00:00+07:00');source=snapshot();idx=Engine.from_snapshot(source).index;checks={};s=ConversationStore(persistence_path=None)
initial=resolve(idx,'บุคคลทั่วไปเล่น PC 1 ชั่วโมง ราคาเท่าไหร่',[],source['active'],clock);state={'schema_version':1,'dialogue_task':initial['task']}
turn=s.begin('controlled-A','t1','บุคคลทั่วไปเล่น PC 1 ชั่วโมง ราคาเท่าไหร่',locale='th',history=[])
response={'ok':True,'request_id':'controlled-response-A','answer':'999999 THB invented assistant price','common_read_state':state}
s.complete('controlled-A','t1',turn['revision'],response)
checks['prepared_but_not_written_response_not_trusted']=delivered_state(s.history('controlled-A')) is None
s.delivery('controlled-A','t1','server_written');own=s.history('controlled-A');checks['stored_same_session_written_intent_available']=delivered_state(own)==state
follow=resolve(idx,'แล้วสองชั่วโมงล่ะ',own,source['active'],clock)
checks['trusted_history_inherits_user_slots_not_assistant_price']='120' in follow['execution_question'] and '999999' not in follow['execution_question'] and 'PC' in follow['execution_question']
ref=follow['task']['slot_provenance']['platforms'];checks['inherited_slot_links_actual_server_session_and_turn']=ref.get('source_session_id')=='controlled-A' and ref.get('source_turn_id')=='t1' and ref.get('history_carrier',{}).get('response_id')=='controlled-response-A'
checks['adding_delivery_refs_does_not_rewrite_original_slot_state']=initial['task']['slot_provenance']['platforms'].get('source_session_id') is None
fallback=copy.deepcopy(own);fallback[-1]['delivery_status']='client_acknowledged';before=copy.deepcopy(fallback);foreign=s.history('controlled-B',fallback)
checks['client_forged_delivery_cannot_transfer_state_between_sessions']=delivered_state(foreign) is None and fallback==before
checks['fallback_cannot_keep_server_history_reference']=not any(t.get('_server_history_ref') for t in foreign)
unbound=resolve(idx,'แล้วสองชั่วโมงล่ะ',foreign,source['active'],clock);checks['foreign_typed_state_not_used_for_slot_inheritance']=not unbound['inherited_slots']
checks['acknowledgment_only_matches_own_session']=not s.acknowledge('controlled-B','controlled-response-A') and s.acknowledge('controlled-A','controlled-response-A')
s.delivery('controlled-A','t1','uncertain');checks['acknowledged_delivery_not_downgraded_by_retry']=delivered_state(s.history('controlled-A'))==state
other=s.begin('controlled-C','t1','PC price',history=[]);s.complete('controlled-C','t1',other['revision'],{**response,'request_id':'controlled-response-C'});s.delivery('controlled-C','t1','uncertain');checks['uncertain_delivery_not_reused']=delivered_state(s.history('controlled-C')) is None
checks['duplicate_completed_turn_cannot_rewrite_intent']=not s.complete('controlled-A','t1',turn['revision'],{**response,'common_read_state':{'schema_version':1}}) and delivered_state(s.history('controlled-A'))==state
try:s.begin('controlled-A','t1','different question',locale='th');checks['turn_identity_question_reuse_rejected']=False
except TurnConflict:checks['turn_identity_question_reuse_rejected']=True
raw='ราคา PC ๒ ชั่วโมง';normalized='ราคา pc ๒ ชั่วโมง'
with request_context() as ctx:
 ctx.input={'raw_question':raw,'locale':'th'};proof=capture(normalized);span=map_span(proof,{'start':0,'end':len(normalized),'text':normalized})
 checks['raw_question_preserved_separately_from_normalization']=proof['raw_question']==raw and proof['normalized_question']==normalized and bool(proof['normalization']['offsets'])
 checks['normalization_range_does_not_forge_exact_raw_quote']=span['status']=='normalized_raw_range' and span['text']==raw and span['exact_quote'] is False
 for label,mutation in [('item_rewrite',lambda:ctx.input.__setitem__('raw_question','rewritten')),('update_rewrite',lambda:ctx.input.update(raw_question='rewritten')),('whole_input_rewrite',lambda:setattr(ctx,'input',{'raw_question':'rewritten'})),('raw_delete',lambda:ctx.input.pop('raw_question'))]:
  try:mutation();checks[label+'_rejected']=False
  except ValueError:checks[label+'_rejected']=ctx.input['raw_question']==raw
 ctx.input['dialogue_resolution']={'basis':'controlled_metadata_enrichment'};checks['metadata_enrichment_does_not_change_raw_input']=ctx.input['raw_question']==raw
 unattested=capture('ราคา pc 2 ชั่วโมง');mapped=map_span(unattested,{'start':0,'end':len('ราคา pc 2 ชั่วโมง'),'text':'ราคา pc 2 ชั่วโมง'});checks['unattested_digit_transform_not_claimed_exact_raw']=mapped['status']=='unresolved_derivation' and mapped['exact_current_raw_quote'] is False
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_conversations_or_data_modified':False};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps({'followup':follow,'cross_session_resolution':unbound,'raw_provenance':proof,'raw_span':span},ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
