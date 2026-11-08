"""Contradictory current prices must not become a confident quote."""
import copy,json,os,sqlite3,sys
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(S))
os.environ.update(PSU_ESPORTS_NOW='2026-10-12T15:00:00+07:00',PSU_LOCAL_LLM_ASSIST_ENABLED='0')
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer,title
from app.knowledge.common.claim_conflicts import detect
from app.knowledge.common.read_graph import fact,evaluate
from app.calendar.service_calendar import now_bangkok
src=R.parent/'r58_examples_240_20261012/DEMO_ONLY.sqlite';db=T/'SYNTHETIC_ONLY.sqlite'
with sqlite3.connect(src.as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as b:a.backup(b)
store=CommonStore(db);rs=store.snapshot()['release']['records'];old=next(r for r in rs.values() if r['kind']=='rate')
r=copy.deepcopy(old);r['record_id']='r101_conflicting_rate';r['revision']=1;r['fields']['amount_minor']['value']=value(old,'amount_minor')+10000
save_owner_record(store,r,0,'isolated-conflict-test');view=DraftSnapshotView(store);snap=view.snapshot();checks=[]
def check(name,ok):checks.append({'case':name,'passed':bool(ok)});print(name,bool(ok),flush=True)
check('same current billing tuple with different values is a conflict',bool(detect([old['record_id']],snap,now_bangkok())))
q=title(rs[value(old,'service_id')],'en')+' price'
with patch('urllib.request.urlopen',side_effect=AssertionError('No model needed for source conflict')):answer=CommonAnswerer(view).answer(q,locale='en')
check('chat exposes conflict instead of choosing amount',answer is not None and answer.decision_artifact['need_results'][0]['status']=='conflict' and not answer.hits)
store.withdraw(r['record_id'],actor='isolated-conflict-test');snap=view.snapshot()
check('withdrawn competing rate no longer conflicts',not detect([old['record_id']],snap,now_bangkok()))
game=next(r for r in snap['release']['records'].values() if r['kind']=='game');field=next(k for k,f in game['fields'].items() if f['status']=='known' and f['evidence_refs'])
broken=copy.deepcopy(snap);sid=game['fields'][field]['evidence_refs'][0]['source_id'];broken['release']['sources'][sid]['authority_for']=['rate']
check('valid-looking pointer cannot bypass source authority',evaluate(fact(game['record_id'],field),broken,now_bangkok())['status']=='broken_relation')
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],'checks':checks,'data':'isolated synthetic only'}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary);sys.exit(bool(summary['failed']))
