"""Two fixes after measured 200: native location phrase and source-title display."""
import json,time
from unittest.mock import patch
from verification_support import R
from app.core.locale import LocaleDecision
from app.pipeline.migrated_chat import answer
from app.knowledge.common.migrated_view import MigratedView
from app.web_api.server import _source_list

out=R/('post_eval_delivery_'+str(time.time_ns()));out.mkdir();checks={};rows=[]
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite')
for q,lang in [('Driving Force Shifter อยู่ซนไหน','th'),('Driving Force Shifter อยู่โซนไหน','th'),('Gaming Mouse อยู่ซนไหน','th'),('อุปกรณ์อำพันที่ไม่เคยมี อยู่ซนไหน','th'),('จองได้สูงสุดกี่รอบ','th')]:
 with patch('urllib.request.urlopen',side_effect=AssertionError('network/model forbidden')):
  result=answer(q,locale=LocaleDecision(lang,lang,lang,1,'test'),store=view,allow_llm=False,allow_live=False)
 sources=_source_list(result.hits)
 rows.append({'question':q,'answer':result.answer,'sources':sources,'artifact':result.decision_artifact})
 if q.startswith('Driving'):
  checks['known_shifter_'+str(len(rows))]='Cockpit Zone' in result.answer and bool(result.hits)
  checks['raw_question_retained_'+str(len(rows))]=result.decision_artifact['request_context']['input']['raw_question']==q
 elif q.startswith('Gaming'):
  checks['other_known_device']='PC Zone' in result.answer and bool(result.hits)
 elif q.startswith('อุปกรณ์'):
  checks['unknown_device_no_borrow']=not result.hits
 else:
  checks['verified_website_title_retained']=bool(sources) and all('Booking limits' in s['id'] for s in sources)
  checks['booking_answer_retained']='6 Sessions' in result.answer
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
report={'all_passed':all(checks.values()),'checks':checks,'scope':'post-200 source-only shared chat dispatcher; two repairs not included in measured 196/255; no inferred all-system score'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'output':str(out),**report},ensure_ascii=False));assert report['all_passed']
