"""Actual retained bilingual sources, isolated SQLite backup, no HTTP/model."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.flow_context import CURRENT
O=R/('auto_locale_boundaries_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated.sqlite');source=(R/'system/data/knowledge/common.sqlite').resolve();a=sqlite3.connect(source.as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();view=DraftSnapshotView(CommonStore(O/'source.sqlite'));snapshot=view.snapshot();records=snapshot['release']['records'];faq=records['migrated_faq_rule_schedule_afternoon_time'];game=records['game_detail_it_takes_two'];checks={};details=[];calls=[];old=CommonAnswerer._answer_with_context
def traced(self,q,**kw):calls.append({'locale_received_by_all_readers':kw['locale'],'request_input':copy.deepcopy(CURRENT.get().input)});return old(self,q,**kw)
def run(q,requested,name,expected,lang,rid):
 start=len(calls)
 with patch('urllib.request.urlopen',side_effect=AssertionError('actual HTTP forbidden')),patch.object(CommonAnswerer,'_answer_with_context',traced):r=CommonAnswerer(view).answer(q,locale=requested,at='2026-10-27T10:00:00+07:00',planner=None)
 seen=calls[start];checks[name+'_resolved_before_helper_dispatch']=seen['locale_received_by_all_readers']==lang
 checks[name+'_original_requested_locale_preserved']=seen['request_input']['requested_locale']==requested and seen['request_input']['locale']==requested and seen['request_input']['effective_locale']==lang
 checks[name+'_actual_source_language_text_delivered']=expected in r.answer
 ids=set()
 def walk(v):
  if isinstance(v,dict):
   if isinstance(v.get('record_id'),str):ids.add(v['record_id'])
   ids.update(x for x in v.get('record_ids',[]) if isinstance(x,str))
   for z in v.values():walk(z)
  elif isinstance(v,list):
   for z in v:walk(z)
 walk(r.decision_artifact);checks[name+'_same_actual_source_record_bound']=rid in ids
 details.append({'case':name,'question':q,'requested_locale':requested,'effective_locale':lang,'expected_source_record':rid,'answer':r.answer,'reader_boundary':seen,'artifact':r.decision_artifact});return r
q='Please tell me: What time is the afternoon session'
for requested,lang,name in [('auto','en','named_period_auto_english'),('en','en','named_period_explicit_english'),('th','th','named_period_explicit_thai_override')]:
 expected='Friday — afternoon: 13:00–16:00 (maintenance)' if lang=='en' else 'ศุกร์ — รอบบ่าย: 13:00–16:00 (บำรุงรักษา)'
 run(q,requested,name,expected,lang,'migrated_schedule_4')
for question,requested,lang,name in [('What genre is It Takes Two?','auto','en','typed_auto_english'),('It Takes Two เป็นเกมแนวไหน','auto','th','typed_mixed_auto_thai'),('What genre is It Takes Two?','th','th','typed_explicit_thai_override'),('It Takes Two เป็นเกมแนวไหน','en','en','typed_explicit_english_override')]:run(question,requested,name,game['fields']['genre']['value'][lang],lang,game['record_id'])
checks['source_snapshot_unchanged']=snapshot==view.snapshot();report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'owner_data_modified':False,'source_control_scope':'Retained actual source language values and identity; not all bilingual/translation correctness or benchmark acceptance','missing_or_conflicted_translation_coverage':'review_required'};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
