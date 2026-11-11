import json,time,types
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.game_edition_scope import request,allows
from app.knowledge.common.domain_flow.control_scope import candidates
from app.knowledge.common.domain_flow.receipt_scope import check
v=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');s=v.snapshot();i=Engine.from_snapshot(s,cache_key=v.path.resolve()).index
base=candidates(i,'TEKKEN 8 ปุ่มอะไร');assert base
gid=base[0]['game_id'];checks={};out=R/('numeric_edition_'+str(time.time_ns()));out.mkdir();rows=[]
checks['normal_edition_kept']=allows(i,'TEKKEN 8 ปุ่มอะไร',gid) and bool(candidates(i,'TEKKEN 8 ปุ่มอะไร'))
checks['unknown_edition_not_nearest']=not allows(i,'TEKKEN 9 ปุ่มอะไร',gid) and not candidates(i,'TEKKEN 9 ปุ่มอะไร')
checks['compact_unknown_edition_rejected']=not allows(i,'tekken9 controls',gid)
checks['thai_unknown_edition_rejected']=not allows(i,'เทคเคน 9 ปุ่มอะไร',gid)
checks['headcount_not_game_edition']=allows(i,'TEKKEN 2 คน ปุ่มอะไร',gid)
checks['duration_not_game_edition']=allows(i,'TEKKEN 2 ชั่วโมง ปุ่มอะไร',gid)
checks['generic_source_alias_retained']=allows(i,'TEKKEN ปุ่มอะไร',gid)
checks['known_edition_then_headcount_retained']=allows(i,'TEKKEN 8 สำหรับ 2 คน ปุ่มอะไร',gid)
task=types.SimpleNamespace(category='C05',target_span=None,operation='list',facet='input_bindings')
proof=check(i,task,base[0],'TEKKEN 9 ปุ่มอะไร')
checks['direct_forced_wrong_edition_receipt_rejected']='source_receipt_game_numeric_edition_mismatch' in proof['errors']
reader=CommonAnswerer(v)
for n,q in enumerate(['TEKKEN 8 ปุ่มอะไร','TEKKEN 9 ปุ่มอะไร','tekken9 controls','เทคเคน 9 ปุ่มอะไร']):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP/model')):r=reader.answer(q,locale='th',planner=None)
 rows.append({'q':q,'answer':r.answer,'hits':r.hits,'artifact':r.decision_artifact})
 checks['natural_'+str(n)]=bool(r.hits) if n==0 else not r.hits
for n,q in enumerate(['TEKKEN 8 มีให้เล่นไหม','TEKKEN 9 มีให้เล่นไหม','TEKKEN 8 คือเกมอะไร','TEKKEN 9 คือเกมอะไร']):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP/model')):r=reader.answer(q,locale='th',planner=None)
 rows.append({'q':q,'answer':r.answer,'hits':r.hits,'artifact':r.decision_artifact})
 checks['natural_game_detail_'+str(n)]=bool(r.hits) if n%2==0 else not r.hits
known=i.bind('C04','TEKKEN 8 คือเกมอะไร');assert known
task4=types.SimpleNamespace(category='C04',target_span=None,operation='detail',facet='description')
checks['direct_forced_description_receipt_rejected']='source_receipt_game_numeric_edition_mismatch' in check(i,task4,known[0],'TEKKEN 9 คือเกมอะไร')['errors']
from app.knowledge.common.domain_flow.source_decisions import guard_result
with patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP/model')):good=reader.answer('TEKKEN 8 คือเกมอะไร',locale='th',planner=None)
forced=guard_result(reader,good,s,i,'TEKKEN 9 คือเกมอะไร',None,'th')
checks['forced_compatibility_answer_cannot_bypass_guard']=bool(good.hits) and not forced.hits and 'TEKKEN 8' not in forced.answer
report={'all_passed':all(checks.values()),'checks':checks,'scope':'bounded explicit numeric source-label game family on controls and game detail/availability, including direct forged receipts; not all game editions, Roman numerals or semantic proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
