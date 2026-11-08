"""Frozen reference contracts, applied only to SAVED output. Never runs chat."""
import collections,dataclasses,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
import reference_grader
from retained_literal import literal,bucket
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,PipelineTrace,EntityBundle,ValidationResult,UniversalIntent
from app.core.locale import LocaleDecision

def construct(cls,data):
 keys={f.name for f in dataclasses.fields(cls)}
 return cls(**{k:v for k,v in data.items() if k in keys})
def as_answer(raw):
 d=dict(raw)
 d['route']=construct(PipelineRoute,d['route']);d['entities']=construct(EntityBundle,d.get('entities') or {})
 d['validation']=construct(ValidationResult,d.get('validation') or {'ok':False})
 d['trace']=[construct(PipelineTrace,x) for x in d.get('trace',[])]
 if d.get('language'):d['language']=construct(LocaleDecision,d['language'])
 if d.get('universal_intent'):d['universal_intent']=construct(UniversalIntent,d['universal_intent'])
 return construct(PipelineAnswer,d)
def from_http(response,capture):
 p=(capture or {}).get('pipeline')
 if p:
  raw=dict(p['result']);kind='observed_actual_pipeline'
  exact=raw.get('answer')==response.get('answer') and raw.get('mode')==response.get('mode')
 else:
  raw={'hits':response.get('sources') or [],'entities':{},'trace':response.get('trace') or [],'confidence':response.get('confidence') or 0,
       'route':{'category':response.get('route_category') or 'transport_error','intent':response.get('route_intent') or '',
       'confidence':response.get('confidence') or 0,'answer_type':'','risk':'','reason':'API short circuit/no captured pipeline'},
       'validation':response.get('validation') or {'ok':response.get('validation_ok') is True}}
  exact=None;kind='api_short_circuit_or_transport_failure'
 raw.update(answer=response.get('answer') or '',mode=response.get('mode') or 'transport_error',elapsed=response.get('latency_sec') or 0,
     decision_artifact=response.get('decision_artifact'),language=response.get('language'),universal_intent=response.get('universal_intent'))
 return raw,kind,exact
def evaluate(job,raw):
 answer=as_answer(raw);grades=[]
 for e in job['entries']:
  try:g=reference_grader.grade(e['case'],answer,Path(e['file']).name)
  except Exception as exc:g={'passed':False,'failures':['grader_exception:'+type(exc).__name__+':'+str(exc)],'evidence_level':'grader_error'}
  ok,errors,positive=literal(e['case'],answer.answer)
  partitions=collections.defaultdict(list)
  for error in g['failures']:partitions[bucket(error)].append(error)
  grades.append({'file':e['file'],'row':e['row'],'variant':e['variant'],'id':e['case'].get('id'),**g,
      'partitions':dict(partitions),'positive_literal':positive,'literal_passed':ok,'literal_errors':errors})
 return grades

def preflight_saved():
 jobs={j['key']:j for j in map(json.loads,(R/'SELECTED_JOBS.jsonl').open(encoding='utf8'))}
 r89=json.loads((R/'SAVED_R89_COHORT.json').read_text('utf8'));mismatch=[];stats=collections.Counter();out=R/'BASELINE_SCORED_V2.jsonl'
 with out.open('x',encoding='utf8') as f:
  for x in map(json.loads,(R/'SAVED_LEGACY_LLM.jsonl').open(encoding='utf8')):
   key=x['key'];j=jobs[key];assert x['question']==j['question']
   raw=x.get('result') or from_http({},None)[0]
   grades=evaluate(j,raw);positive=[g for g in grades if g['positive_literal']]
   old=r89[key];pairs=old.get('grade_pairs',{})
   # R89 retained aggregate is an independent saved check on this definition.
   oldpassed=pairs.get('both_pass',0)+pairs.get('old_only',pairs.get('old_pass_new_fail',0))
   if len(positive)!=old['positive_contract_grades'] or (bool(positive) and all(g['literal_passed'] for g in positive)!=old['old_positive_all_passed']):mismatch.append(key)
   stats['requests']+=1;stats['grades']+=len(grades);stats['positive_grades']+=len(positive);stats['positive_pass']+=sum(g['literal_passed'] for g in positive)
   stats['saved_strict_pass']+=sum(g['passed'] for g in x['grades']);stats['same_checker_strict_pass']+=sum(g['passed'] for g in grades)
   f.write(json.dumps({'key':key,'question':j['question'],'locale':j['locale'],'grades':grades,'saved_original_grades':x['grades'],'result':raw,'exception':x.get('exception')},ensure_ascii=False)+'\n')
 result={'saved_requests_only':True,'chat_requests':0,'model_calls':0,'stats':dict(stats),'r89_literal_definition_mismatch_keys':mismatch}
 (R/'BASELINE_CHECK_V2.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
 assert not mismatch,mismatch[:10]
 print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':
 from unittest.mock import patch
 with patch('urllib.request.urlopen',side_effect=AssertionError('Offline grader must not use network')),patch('socket.create_connection',side_effect=AssertionError('Offline grader must not connect')):
  preflight_saved()
