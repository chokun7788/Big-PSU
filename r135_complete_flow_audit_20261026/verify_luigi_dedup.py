"""Source-backed controls for overlapping same-request answer rendering."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record

O=R/('luigi_dedup_regression_'+str(time.time_ns()));O.mkdir()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close()
store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
q="I am planning a visit and would like to know: What kind of game is Luigi's Mansion 3"
def run(question,source=None):
    with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):
        r=CommonAnswerer(source or view).answer(question,locale='en',at='2026-10-16T12:00:00+07:00',planner=None)
    details.append({'question':question,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None})
    return r
r=run(q);checks['summary_and_genre_once']=bool(r and r.answer.count('**genre**:')==1 and '**game overview**:' in r.answer)
checks['both_task_ledgers_preserved']=bool(r and len(r.decision_artifact.get('need_results',[]))>=2)
checks['both_source_claims_preserved']=bool(r and {'summary','genre'} <= {x['facet'] for x in r.decision_artifact.get('domain_flow',{}).get('typed_claims',[])})
r=run("What kind of game is Luigi's Mansion 3 and also what are the opening hours?")
checks['independent_unknown_not_hidden']=bool(r and 'game overview' in r.answer and ('unconfirmed' in r.answer.lower() or 'no confirmed source' in r.answer.lower()))
rid='game_detail_luigis_mansion_3';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['genre']['value']['en']='Controlled revised genre';save_owner_record(store,record,record['revision'],'isolated-source-edit')
r=run(q);checks['actual_source_edit_delivered_once']=bool(r and r.answer.count('Controlled revised genre')==1)
class Forged:
    path=view.path
    def connect(self):return store.connect()
    def snapshot(self):
        s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['genre']['value']['en']='Forged genre';s['epoch']+=10000;return s
    def still_current(self,s):return s==self.snapshot()
r=run(q,Forged());checks['unattested_genre_not_delivered']=r is None or 'Forged genre' not in r.answer
report={'checks':checks,'all_passed':all(checks.values()),'http_or_inference':False,'owner_data_modified':False,'limitations':'Does not establish source authority or semantic coverage for all questions.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
