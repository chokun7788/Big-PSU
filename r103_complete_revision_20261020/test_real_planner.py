"""Small real Ollama check on newly authored synthetic content, no GT edits."""
import dataclasses,json,os,sys,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(S))
os.environ.update(PSU_ESPORTS_NOW='2026-10-19T12:00:00+07:00',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_COMMON_PLAN_LLM='1')
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.pipeline.request_deadline import request_deadline
store=CommonStore(T/'SYNTHETIC_ONLY.sqlite');store.initialize(allow_demo=True)
g=template('game');g['record_id']='fixture_real_r101_aurora';g['aliases']={'th':['เส้นทางออโรร่า R101'],'en':['Aurora Paths R101']}
for k,v in {'title':{'th':'เส้นทางออโรร่า R101','en':'Aurora Paths R101'},'summary':{'th':'เกมทดลองสำรวจแผนที่ COMET_FACT','en':'A synthetic map exploration game COMET_FACT'},'how_to_play':{'th':'เดินตามทาง COMET_PLAY','en':'Follow the paths COMET_PLAY'}}.items():g['fields'][k].update(status='known',value=v,evidence_refs=[])
save_owner_record(store,g,0,'isolated-real-model-test');rows=[]
questions=[('en','Could you walk me through the basic idea behind Aurora Paths R101?','COMET_FACT'),
 ('en','What would playing Aurora Paths R101 actually involve?','COMET_PLAY'),
 ('th','ช่วยเล่าแนวคิดคร่าวๆของ เส้นทางออโรร่า R101 ให้ฟังที','COMET_FACT')]
native=urllib.request.urlopen;calls=[]
def observed(req,*a,**kw):
 row={'url':req.full_url,'opened':False};calls.append(row);start=time.perf_counter()
 try:r=native(req,*a,**kw);row['opened']=True;return r
 except Exception as e:row.update(error=type(e).__name__);raise
 finally:row['elapsed']=time.perf_counter()-start
urllib.request.urlopen=observed
for lang,q,marker in questions:
 with request_deadline(25):r=CommonAnswerer(DraftSnapshotView(store)).answer(q,locale=lang,planner=lambda *a:None)
 row={'question':q,'locale':lang,'expected_marker':marker,'passed':r is not None and marker in r.answer,'result':dataclasses.asdict(r) if r else None}
 rows.append(row);(T/'RESULTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(q,row['passed'],r.answer if r else None,flush=True)
summary={'requests':len(rows),'passed':sum(r['passed'] for r in rows),'calls':calls,'real_model':True,'isolated_synthetic_content':True,'full_accuracy_claimed':False}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary)
