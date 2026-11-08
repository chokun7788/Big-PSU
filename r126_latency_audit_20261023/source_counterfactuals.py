"""Inspect saved plans and current sources without new inference or data edits."""
import json,os,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R.parent/'r125_date_context_presentation_20261023/system';sys.path.insert(0,str(S));os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import parse
from app.knowledge.common.domain_flow.projection import value,title
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.answer import CommonAnswerer
c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(c['output']);rows=[json.loads(s) for s in (OUT/'HTTP_RESULTS.jsonl').read_text('utf8').splitlines()];by={r['category']:r for r in rows};engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot());at=reference_time('2026-10-23T21:00:00+07:00');audit={}
for key,canonical in [('booking_paraphrase','จองเครื่องทำยังไง'),('policy_paraphrase','ไปนั่งดูเพื่อนเล่นเฉย ๆ ได้ไหม')]:
 if key not in by:continue
 art=by[key]['response'].get('decision_artifact',{});u=art.get('understanding') or {};question=(u.get('event') or {}).get('input_question') or by[key]['question'];tasks=u.get('tasks') or [];cat=tasks[0]['category'] if tasks else 'C10'
 old=engine.plan(cat,question,at);equivalent=engine.plan(cat,canonical,at)
 source_matches=[]
 for rid,r in engine.index.records.items():
  if r['kind']=='faq' and re.search(r'ดูเพื่อน|นั่งดู|watch.*friend',str(value(r,'question') or ''),re.I):source_matches.append({'record_id':rid,'question':value(r,'question'),'answer':value(r,'answer'),'evidence_refs':r['fields']['answer'].get('evidence_refs')})
 audit[key]={'question':question,'model_tasks':tasks,'raw_query_plan':old.__dict__,'canonical_query_control':canonical,'canonical_plan':equivalent.__dict__,'matching_current_sources':source_matches if key=='policy_paraphrase' else [],'control_not_an_implemented_runtime_fix':True}
 if key=='policy_paraphrase' and source_matches:
  source_q=source_matches[0]['question'];source_q=source_q.get('th') or source_q.get('en')
  result=CommonAnswerer(MigratedView(S/'data/knowledge/common.sqlite')).answer(source_q,locale='th',at=at,planner=None)
  audit[key]['literal_source_question_control']={'question':source_q,'answer':result.answer if result else None,'artifact':result.decision_artifact if result else None,'model_allowed':False}
if 'price_multi_audience' in by:
 from app.knowledge.common.domain_flow.financial import rate_pool,audience_mentions,_labels
 from app.knowledge.common.domain_flow.scope import contains,norm
 q=by['price_multi_audience']['response']['decision_artifact']['understanding']['event']['input_question'];rates=[f for f in rate_pool(engine.index,q) if f['facet']=='amount'];positives,_=audience_mentions(engine.index,q);groups=[]
 for gid in positives:
  record=engine.index.records[gid];counts=[]
  for label in _labels(record):
   if not contains(q,label):continue
   suffix=re.search(re.escape(norm(label))+r'\s*(\d+)\s*(?:คน|people|persons?|players?)',norm(q));prefix=re.search(r'(\d+)\s*(?:คน|people|persons?|players?)\s*'+re.escape(norm(label)),norm(q))
   if suffix or prefix:counts.append(int((suffix or prefix)[1]))
  selected=[f for f in rates if value(engine.index.records[f['record_id']],'audience_id')==gid]
  groups.append({'audience_id':gid,'matched_aliases':[label for label in _labels(record) if contains(q,label)],'parsed_person_counts':sorted(set(counts)),'matching_rate_count':len(selected),'rates':[{'id':f['id'],'amount':f.get('numeric'),'service':value(engine.index.records[f['record_id']],'service_id'),'duration_minutes':value(engine.index.records[f['record_id']],'duration_minutes')} for f in selected]})
 audit['price_multi_audience']={'question':q,'groups':groups,'code_condition':'billing rejects each audience when len(selected rate rows) != 1; shares one clarification reason for count and service ambiguity'}
if 'controls_paraphrase' in by:
 row=by['controls_paraphrase'];art=row['response']['decision_artifact'];u=art['understanding'];q=u['event']['input_question'];raw=u['event']['raw_content'];meaning=parse(raw,q).tasks[0];plan=engine.plan('C05',q,at,meaning);candidates=engine.scoped_candidates('C05',q,plan,at)
 target=[f for f in engine.index.bind('C05',q) if re.search(r'หนัก|heavy attack',' '.join(f['value'].values()),re.I)]
 audit['controls_paraphrase']={'question':q,'initial_plan':plan.__dict__,'scoped_top8':[{'id':f['id'],'label':f['label'],'value':f['value']} for f in candidates],'heavy_attack_source_facts':[{'id':f['id'],'label':f['label'],'value':f['value']} for f in target],'answer':row['response']['answer'],'model_events':art.get('domain_flow',{}).get('model_events')}
(R/'SOURCE_COUNTERFACTUALS.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),'utf8')
for key,a in audit.items():print(json.dumps({'case':key,'raw_reason':a.get('raw_query_plan',{}).get('reason'),'canonical_reason':a.get('canonical_plan',{}).get('reason'),'source_matches':len(a.get('matching_current_sources',[])),'candidate_labels':[f['label'] for f in a.get('scoped_top8',[])],'heavy_attack_in_top8':[f['id'] for f in a.get('heavy_attack_source_facts',[]) if f['id'] in {c['id'] for c in a.get('scoped_top8',[])}]},ensure_ascii=False))
