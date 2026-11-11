"""Mixed-coordinator boundaries, raw spans and non-vacuous source delivery."""
import json,time,types
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow import routing
from app.knowledge.common.domain_flow.request_verifier import clauses

out=R/('shared_contract_'+str(time.time_ns()));out.mkdir();checks={};rows=[]
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');index=Engine.from_snapshot(view.snapshot(),cache_key=view.path.resolve()).index
questions=[
 'มีเกมอะไรบ้าง; PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองยังไง',
 'PC นักศึกษา PSU ราคาเท่าไหร่; จองยังไง แล้วมีเกมอะไรบ้าง',
 'มีเกมอะไรบ้าง and also PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองยังไง',
 'What games are offered; how do I book and what is the PC price for PSU students',
]
for n,q in enumerate(questions):
 checks[f'three_distinct_parts_{n}']=len(routing.split_needs(q,index))==3
 checks[f'observer_agrees_boundaries_{n}']=[p['text'] for p in clauses(q,index)]==routing.split_needs(q,index)
fn=getattr(routing,'need_spans',None)
checks['raw_span_contract_available']=fn is not None
if fn:
 for n,q in enumerate([*questions,'มีเกมอะไรบ้าง; มีเกมอะไรบ้าง','PC price; I am not a PSU student']):
  parts=fn(q,index);checks[f'raw_offsets_exact_{n}']=all(q[p['start']:p['end']]==p['text'] for p in parts)
 dup=fn('มีเกมอะไรบ้าง; มีเกมอะไรบ้าง',index)
 checks['repeated_text_has_distinct_spans']=len(dup)==2 and dup[0]['start']!=dup[1]['start']
 checks['negative_qualifier_not_detached']=len(fn('PC price; I am not a PSU student',index))==1
fake=types.SimpleNamespace(subject_labels={'C03':{'Wheel and also Gear; Pro','Foo and what Bar'}})
checks['source_name_protects_all_delimiters']=routing.split_needs('Wheel and also Gear; Pro ใช้ทำอะไร',fake)==['Wheel and also Gear; Pro ใช้ทำอะไร']
checks['source_name_protects_predicate_words']=routing.split_needs('Foo and what Bar ใช้ทำอะไร',fake)==['Foo and what Bar ใช้ทำอะไร']
checks['object_coordination_not_split']=routing.split_needs('keyboard and mouse อยู่ที่ไหน',index)==['keyboard and mouse อยู่ที่ไหน']
checks['negative_quantity_not_collapsed']='2 ชั่วโมง 2 ชั่วโมง' in routing.split_needs('VR 2 ชั่วโมง 2 ชั่วโมง ราคาเท่าไหร่',index)[0]
checks['unspaced_thai_boundary_not_lost']=len(routing.split_needs('มีเกมอะไรบ้างแล้วจองยังไง',index))==2
checks['observer_existing_use_boundary_retained']=len(clauses('ราคาเท่าไหร่แล้วใช้ยังไง',index))==2
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.context_guard import apply
q=questions[1];u=apply(q,index,propose(index,q));u=apply(q,index,u)
checks['repeat_context_review_retains_recomputed_basis']=any(a.get('action')=='source_related_booking_ellipsis' and a.get('task_quote')=='จองยังไง' for a in u.event.get('context_scope_review',[]))
reader=CommonAnswerer(view)
for n,q in enumerate(questions[:3]):
 with patch('urllib.request.urlopen',side_effect=AssertionError('no model/HTTP')),patch.dict('os.environ',{'PSU_ANALYSIS_BUDGET_SEC':'0'}):r=reader.answer(q,locale='th',planner=None)
 rows.append({'question':q,'answer':r.answer,'artifact':r.decision_artifact,'hits':r.hits})
 checks[f'price_survives_zero_model_budget_{n}']='0 บาท' in r.answer
 checks[f'booking_delivered_{n}']='สลิป' in r.answer
 checks[f'catalog_delivered_{n}']=any(h.get('record_id','').startswith('availability_') for h in r.hits)
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'checks':checks,'scope':'bounded lexical boundary/offset contract plus actual source-only natural delivery with model budget zero; no general intent proof or hard deadline guarantee','model_calls':0,'http_requests':0}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report},ensure_ascii=False),flush=True)
assert report['all_passed']
