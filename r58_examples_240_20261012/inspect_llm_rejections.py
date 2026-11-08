"""Capture six local-model replies to explain rejected schema plans.
Wrap the transport in this test process only; do not change planner code or facts.
"""
import json,urllib.request
from unittest.mock import patch
import build_and_test as task
from app.knowledge.common.planner import plan_fields
from app.pipeline.llm_health import preflight_ollama
real_open=urllib.request.urlopen
captured=[]
class ObservedResponse:
    def __init__(self,response):self.response=response
    def __enter__(self):self.response.__enter__();return self
    def __exit__(self,*args):return self.response.__exit__(*args)
    def read(self,*args):
        data=self.response.read(*args)
        try:
            body=json.loads(data);captured.append({'raw_response':body.get('response'),'done':body.get('done'),'done_reason':body.get('done_reason')})
        except ValueError:captured.append({'decode_error':True})
        return data
def observed(*args,**kw):return ObservedResponse(real_open(*args,**kw))
def reason(proposal,records,ids):
    if not isinstance(proposal,dict):return 'not_object'
    if set(proposal)!={'requested_fields','all_fields','platform'}:return 'wrong_property_set'
    kinds={records[x]['kind'] for x in ids}
    if 'game' in kinds:kinds.update(('game_service','game_mode','control_set'))
    allowed={f['key'] for k in kinds for f in task.CATALOG[k]['fields']};fs=proposal.get('requested_fields')
    if not isinstance(fs,list) or not 1<=len(fs)<=12:return 'invalid_field_list_length_or_type'
    if any(not isinstance(f,str) or f not in allowed for f in fs):return 'unsupported_field_key: '+repr(fs)
    if len(set(fs))!=len(fs):return 'duplicate_fields'
    if type(proposal['all_fields']) is not bool:return 'wrong_all_fields_type'
    platforms={task.value(r,'platform') for r in records.values() if task.value(r,'platform')}
    if proposal['platform'] is not None and proposal['platform'] not in platforms:return 'unsupported_platform: '+repr(proposal['platform'])
    return 'accepted'
def main():
    records=task.CommonStore(task.DB).snapshot()['release']['records'];rows=[]
    samples=[json.loads(x) for x in (task.BASE/'LLM_SAMPLE_RESULTS.jsonl').read_text(encoding='utf-8').splitlines()]
    samples=[x for x in samples if x['planner_attempts'] and not any(a['checked_plan'] for a in x['planner_attempts'])][:6]
    preflight_ollama(model='scb10x/typhoon2.5-qwen3-4b',kind='demo_rejection_probe',timeout_sec=20,num_predict=1,num_ctx=3072)
    for c in samples:
        captured.clear()
        with patch('app.knowledge.common.planner.urllib.request.urlopen',observed):clean=plan_fields(c['question'],records,[c['rid']])
        try:proposal=json.loads(captured[-1]['raw_response']);reject=reason(proposal,records,[c['rid']])
        except (IndexError,TypeError,ValueError):proposal=None;reject='no_decodable_model_reply'
        rows.append({'question':c['question'],'kind':c['kind'],'lang':c['lang'],'raw':captured.copy(),'proposal':proposal,'checked_plan':clean,'diagnosed_reason':reject})
    task.filejson('LLM_REJECTION_DIAGNOSIS.json',rows)
    print(json.dumps([{'kind':x['kind'],'lang':x['lang'],'reason':x['diagnosed_reason']} for x in rows],ensure_ascii=False))
if __name__=='__main__':main()
