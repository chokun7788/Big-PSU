"""Capture the swallowed exception; read candidate DB, no model or HTTP."""
import json,os,sys,time,traceback
from unittest.mock import patch
from verification_support import R
from app.core.locale import LocaleDecision
from app.pipeline.migrated_chat import answer
from app.pipeline import migrated_chat
from app.knowledge.common.migrated_view import MigratedView

out=R/('store_exception_diagnosis_'+str(time.time_ns()));out.mkdir()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite')
events=[];rows=[]
original=migrated_chat.PipelineAnswer
def capture(*args,**kwargs):
 exc=sys.exception()
 if kwargs.get('mode')=='pipeline:migrated_unavailable' and exc is not None:
  events.append({'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exception(exc)})
 return original(*args,**kwargs)
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite')
for q,lang in [('will it rain tomorrow ?','en'),('มี Minecraft ให้เล่นไหม','th'),('Whoo is the secretary','en')]:
 events=[]
 with patch('urllib.request.urlopen',side_effect=AssertionError('network forbidden')),patch.object(migrated_chat,'PipelineAnswer',capture):
  result=answer(q,locale=LocaleDecision(lang,lang,lang,1,'diagnostic'),store=view,allow_llm=False,allow_live=False)
 rows.append({'question':q,'mode':result.mode,'answer':result.answer,'exceptions':events,'artifact':result.decision_artifact})
 print(json.dumps({'question':q,'mode':result.mode,'exceptions':events},ensure_ascii=False),flush=True)
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('OUTPUT',out)
