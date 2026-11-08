"""Reconstruct planner input from pinned native session artifacts, without HTTP.

Artifact identity and deterministic derivation are verified. This does not
certify the semantic correctness or authenticity of a human-exported artifact.
Other transformation stages stay unsupported until independently implemented.
"""
import copy,hashlib,json
from datetime import datetime
from pathlib import Path

VERSION='r135-native-dialogue-training-input-v1'
def _digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')).hexdigest()
def implementation_sha():
    here=Path(__file__).resolve();root=here.parents[3]
    paths=[here,here.with_name('dialogue_task.py'),here.with_name('controller_catalog.py'),here.with_name('input_derivation.py'),here.with_name('request_provenance.py'),here.parent.parent/'followup_scope.py',root/'session/history_boundary.py']
    return _digest({str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
IMPLEMENTATION_SHA256=implementation_sha()

def reconstruct(raw,request_id,session_id,reference_time,snapshot,record):
    from app.session.history_boundary import history_from_record
    from ..flow_context import Context,CURRENT
    from .engine import Engine
    from .dialogue_task import resolve
    from .input_derivation import register,check
    if not isinstance(raw,str) or not raw or not isinstance(request_id,str) or not request_id or not isinstance(session_id,str) or not session_id:raise ValueError('runtime_input_identity_required')
    at=datetime.fromisoformat(reference_time)
    if at.tzinfo is None or at.utcoffset() is None:raise ValueError('runtime_input_explicit_clock_required')
    if not isinstance(record,dict) or not isinstance(record.get('history'),list) or not isinstance(record.get('turns'),dict):raise ValueError('native_session_record_required')
    # Cross-check retained carriers with actual saved response/turn fields, rather
    # than accepting a client-provided common_read_state or delivery boolean.
    responses={t['response'].get('request_id'):(tid,t) for tid,t in record['turns'].items() if isinstance(t,dict) and isinstance(t.get('response'),dict)}
    if len(responses)!=sum(isinstance(t,dict) and isinstance(t.get('response'),dict) for t in record['turns'].values()):raise ValueError('duplicate_session_response_identity')
    history=history_from_record(record,session_id)
    if not history:raise ValueError('owned_session_history_required')
    for turn in history:
        if turn.get('role')=='user':
            saved=record['turns'].get(turn.get('turn_id'))
            if turn.get('session_id')!=session_id or not saved or turn.get('text')!=saved.get('question'):raise ValueError('saved_user_history_identity_mismatch')
        elif turn.get('role')=='assistant' and turn.get('request_id') in responses:
            _,saved=responses[turn['request_id']];response=saved['response']
            if response.get('ok') is not True or turn.get('common_read_state')!=response.get('common_read_state') or turn.get('text')!=response.get('answer',''):raise ValueError('saved_response_history_mismatch')
    ctx=Context(request_id=request_id);ctx.input={'raw_question':raw};ctx.pin_reference_time(at);ctx.bind_snapshot(snapshot);token=CURRENT.set(ctx)
    try:
        engine=Engine.from_snapshot(snapshot);resolution=resolve(engine.index,raw,history,snapshot['active'],at);ctx.input['dialogue_resolution']=resolution;question=resolution['execution_question']
        if question!=raw:
            proof=register(question,'r128_delivered_task_resolution',[{'origin':'current_user','text':raw},{'origin':'delivered_intent_slots','text':question}],index=engine.index,history=history,facts_inherited=False,inherited_slots=resolution['inherited_slots'])
            if not proof.get('verified'):raise ValueError('native_input_derivation_rejected')
        if not check(question)['verified']:raise ValueError('native_input_not_verified')
        return {'version':VERSION,'request_id':request_id,'session_id':session_id,'raw_question':raw,'execution_question':question,'resolution':copy.deepcopy(resolution),'history_sha256':_digest(history),'snapshot':copy.deepcopy(ctx.snapshot),'input_derivation_validation':check(question),'implementation_sha256':IMPLEMENTATION_SHA256,'semantic_correctness_claimed':False}
    finally:CURRENT.reset(token)

def planner_question(example,origin,artifacts,source_ref):
    allowed=example.get('allowed_context')
    if allowed==[]:return example.get('raw_question')
    if not isinstance(allowed,list) or len(allowed)!=1 or not isinstance(allowed[0],dict) or set(allowed[0])!={'kind','runtime_input_ref'} or allowed[0]['kind']!=VERSION:raise ValueError('context_training_requires_attested_runtime_input_not_silent_flattening')
    ref=allowed[0]['runtime_input_ref']
    if origin.get('runtime_input_ref')!=ref:raise ValueError('history_not_bound_to_saved_origin')
    saved=artifacts.read(ref)
    if set(saved)!={'version','question_key','raw_question','request_id','session_id','reference_time','source_ref','session_record_ref','reconstruction','planner_messages'} or saved.get('version')!=VERSION or saved.get('question_key')!=example.get('question_key') or saved.get('raw_question')!=example.get('raw_question'):raise ValueError('saved_runtime_input_identity_mismatch')
    if artifacts.source_digest(saved['source_ref'])!=artifacts.source_digest(source_ref):raise ValueError('history_source_version_requires_readjudication')
    snapshot=artifacts.read(source_ref);record=artifacts.read(saved['session_record_ref'])
    actual=reconstruct(saved['raw_question'],saved['request_id'],saved['session_id'],saved['reference_time'],snapshot,record)
    if actual!=saved['reconstruction']:raise ValueError('saved_runtime_input_derivation_changed')
    from .graph_protocol import messages
    if saved['planner_messages']!=messages(actual['execution_question']):raise ValueError('saved_runtime_planner_messages_mismatch')
    return actual['execution_question']
