"""Focused new-flow checks, isolated owner data and read-only installed facts."""
import dataclasses,json,os,sys,copy
from pathlib import Path
from unittest.mock import patch
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
os.environ.update(PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'))
sys.path.insert(0,str(S));import app.knowledge.common as pkg;pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
import app.pipeline as pipe;pipe.__path__.insert(0,str(B/'candidate/app/pipeline'))
from app.knowledge.common.registry import template,value,CATALOG
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.task_interpretation import interpret
from app.knowledge.common.task_registry import readiness,TASKS
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record,preview_answer
from app.knowledge.common.snapshot_provider import DraftSnapshotView,PinnedSnapshotView
from app.knowledge.common.dialogue import state_from_answer
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(name,bool(ok),flush=True)
def ask(q,lang='en',store=None,history=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No network in deterministic flow checks')):
  return answer(q,locale=LocaleDecision(lang,lang,lang,1,'flow_fixture'),history=history or [],allow_llm=False,store=store,allow_live=False)
def hist(q,r):return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
records=MigratedView(S/'data/knowledge/common.sqlite').snapshot()['release']['records']
for gid in ['game_detail_beat_saber','game_detail_zelda_breath_of_the_wild']:
 g=records[gid]
 patterns=[('en','Could you please give me a beginner-friendly introduction to {}?'),('en','Give me a simple overview of {}'),('en','Tell me about {}'),('en','Describe {}'),('en','What kind of game is {}?'),('en','Please explain how to play {}'),('th','ช่วยแนะนำ {} หน่อย'),('th','ขออธิบาย {} แบบเข้าใจง่าย'),('th','เล่าเกม {} ให้ฟัง')]
 for i,(lang,pattern) in enumerate(patterns):
  q=pattern.format(value(g,'title')[lang]);r=ask(q,lang);field='how_to_play' if i==5 else 'summary'
  check('new-wording-'+gid+'-'+str(i),r.validation.ok and any(h.get('record_id')==gid and h.get('field')==field for h in r.hits),dataclasses.asdict(r))
for q in ['give me an introduction to this game for children','give me a summary and price','introduction without spoilers','describe the newest version in 2027','how to pay','not a game overview','อธิบายเกมที่เหมาะกับเด็ก','แนะนำเกมที่ไม่ต้องจอง','tell me about my own hardware','what is this name','what is this time']:
 check('preserve-qualifier-'+q,interpret(q,['game_detail_beat_saber'],records) is None)
check('task-data-readiness-covers-all-24-kinds',set(TASKS)==set(CATALOG))
mixed=ask('Beat Saber game overview and price')
mixed_art=mixed.decision_artifact;first=(mixed_art.get('query_plan',{}).get('clauses') or [{}])[0]
check('compound-mixed-game-service-control-aliases-keep-game-subject','rhythm' in mixed.answer.lower() and first.get('query_plan',{}).get('record_ids')==['game_detail_beat_saber'] and mixed_art.get('need_ledger',{}).get('total_needs')==2,dataclasses.asdict(mixed))
for kind in CATALOG:
 r=template(kind);r['record_id']='fixture_'+kind
 report=readiness(r,{})
 check('empty-readiness-'+kind,bool(report['tasks']) and all(x['status']=='needs_data' for x in report['tasks']),report)
store=CommonStore(T/'ISOLATED_NOT_PRODUCTION.sqlite');store.initialize()
def save(r,values,version):
 r=copy.deepcopy(r)
 for k,v in values.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':'SYNTHETIC ONLY; NOT PRODUCTION'}
 return save_owner_record(store,r,version,'isolated_flow_test',source_title='Synthetic owner input')['record']
def publish(r,key):
 current=store.get(r['record_id']);store.approve(r['record_id'],r['revision'],current['hash'],actor='isolated_flow_test')
 store.publish([r['record_id']],actor='isolated_flow_test',expected_active=store.snapshot()['active'],request_key=key)
game=template('game');game['record_id']='fixture_lumen_circuit';game['localization']['en_status']='agent_translated'
game=save(game,{'title':{'th':'ลูเมนเซอร์กิต ข้อมูลทดลอง','en':'Lumen Circuit Fixture'},'summary':{'th':'ภาพรวมทดลอง LUMEN_V1','en':'Synthetic overview LUMEN_V1'},'genre':{'th':'ผจญภัยทดลอง','en':'Synthetic adventure'},'how_to_play':{'th':'วิธีทดลอง LUMEN_PLAY','en':'Synthetic instructions LUMEN_PLAY'}},0)
report=readiness(game,{game['record_id']:game});by={x['task']:x for x in report['tasks']}
check('readiness-is-task-specific',by['game_overview']['status']=='data_ready' and by['game_controls']['status']=='needs_data',report)
publish(game,'lumen-v1')
for lang,q in [('en','Give me a simple introduction to Lumen Circuit Fixture'),('th','ช่วยแนะนำ ลูเมนเซอร์กิต ข้อมูลทดลอง หน่อย'),('en','Lumen Circuit Fixture how do you play?')]:
 chat=ask(q,lang,store=store);preview=preview_answer(store,q,locale=lang)
 check('owner-preview-and-chat-'+lang+'-'+q,chat.answer==preview.answer and [h['field'] for h in chat.hits]==[h['field'] for h in preview.hits] and preview.validation.ok,{'chat':dataclasses.asdict(chat),'preview':dataclasses.asdict(preview)})
q='Lumen Circuit Fixture game overview';old=ask(q,store=store);prior=hist(q,old)
game=save(game,{'summary':{'th':'ภาพรวมฉบับใหม่ LUMEN_V2','en':'Revised overview LUMEN_V2'}},game['revision'])
draft=preview_answer(store,q,locale='en',draft=True)
published=preview_answer(store,q,locale='en')
check('draft-only-values-are-not-published','LUMEN_V2' in draft.answer and 'LUMEN_V1' in published.answer and not draft.decision_artifact['migration']['production_publication_verified'])
pin=PinnedSnapshotView(DraftSnapshotView(store));pinned_revision=pin.snapshot()['release']['records'][game['record_id']]['revision']
game=save(game,{'summary':{'th':'ข้อมูลเปลี่ยนระหว่างตอบ LUMEN_V3','en':'Concurrent edit LUMEN_V3'}},game['revision'])
check('snapshot-pinned-and-concurrent-edit-detected',pin.snapshot()['release']['records'][game['record_id']]['revision']==pinned_revision and not pin.still_current(pin.snapshot()))
publish(game,'lumen-v3')
follow=preview_answer(store,'summary',locale='en',history=prior)
check('shared-preview-followup-rereads-published-revision','LUMEN_V3' in follow.answer and 'LUMEN_V1' not in follow.answer,dataclasses.asdict(follow))
compound=ask('Lumen Circuit Fixture game overview and price',store=store)
ledger=compound.decision_artifact.get('need_ledger',{})
check('compound-keeps-known-overview-with-unconfirmed-price','LUMEN_V3' in compound.answer and ledger.get('total_needs')==2 and ledger.get('answered_needs')==1 and compound.decision_artifact.get('response_type')=='partial_answer',dataclasses.asdict(compound))
live=preview_answer(store,'Is PC1 free now?',locale='en',draft=True)
check('preview-does-not-claim-live-status',not live.hits and live.decision_artifact.get('response_type')=='live_unavailable',dataclasses.asdict(live))
rate=template('rate');rate['record_id']='fixture_rate'
for f in CATALOG['rate']['fields']:
 if f['publish_core']:rate['fields'][f['key']]={'status':'known','value':{'service_id':'s','audience_id':'a','amount_minor':10000,'currency':'THB','unit':'per_session','duration_minutes':60,'calculation_rule':'fixed'}.get(f['key']),'evidence_refs':[],'note':''}
refs={'s':{'kind':'service'},'a':{'kind':'audience'}};rp=readiness(rate,refs)
check('price-readiness-does-not-approve-unknown-effective-dates',rp['tasks'][0]['status']=='needs_effective_dates',rp)
summary={'count':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x['case'] for x in checks if not x['passed']],'model_calls':0,'full_test':False,'simulated_owner_approvals_only':True}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False));sys.exit(bool(summary['failed']))
