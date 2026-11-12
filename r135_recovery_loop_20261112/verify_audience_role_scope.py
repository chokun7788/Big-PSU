"""Reader/verifier/compatibility controls for bounded audience ambiguity."""
import copy,json,os,time,types
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.audience_role_scope import request
from app.knowledge.common.domain_flow.receipt_scope import check
from app.knowledge.common.domain_flow.source_decisions import guard_result
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');snap=view.snapshot();index=Engine.from_snapshot(snap,cache_key=view.path.resolve()).index;reader=CommonAnswerer(view)
checks={};rows=[]
clean='นักศึกษาต่างมหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท';typo='นักศึกษาต่งามหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท'
fact=next(f for f in index.bycat['C06'] if f.get('record_id')=='migrated_rate_nintendo_switch_60_1_2_psu_student_staff' and f.get('facet')=='amount')
task=types.SimpleNamespace(category='C06',operation='detail',facet='amount',target_span=None)
for label,q in [('typo',typo),('unspecified','นักศึกษา เล่น Nintendo Switch 30 นาที เสียกี่บาท'),('negated','ไม่ใช่นักศึกษา PSU เล่น Nintendo Switch 30 นาที เสียกี่บาท'),('english','student plays Nintendo Switch for 30 minutes how much')]:
 checks[label+'_unresolved']=request(index,q)['unresolved']
 checks[label+'_forced_receipt_rejected']='source_receipt_audience_role_unresolved' in check(index,task,fact,q)['errors']
checks['normal_foreign_not_blocked']=not request(index,clean)['unresolved']
checks['normal_psu_not_blocked']=not request(index,'นักศึกษา PSU เล่น Nintendo Switch 30 นาที เสียกี่บาท')['unresolved']
checks['normal_adult_not_blocked']=not request(index,'บุคคลทั่วไป เล่น Nintendo Switch 30 นาที ราคาเท่าไหร่')['unresolved']
checks['all_groups_not_blocked']=not request(index,'นักศึกษาอยากดูราคา Nintendo Switch ทุกกลุ่ม')['unresolved']
checks['negated_all_not_bypass']=request(index,'นักศึกษา Nintendo Switch ราคาเท่าไหร่ ไม่เอาราคาทุกกลุ่ม')['unresolved']
checks['non_price_not_blocked']=not request(index,'นักศึกษา Nintendo Switch มีเกมอะไรบ้าง')['unresolved']
checks['unknown_service_not_asserted']=not request(index,'นักศึกษา Unknown Quasar Service ราคาเท่าไหร่')['unresolved']
changed=copy.deepcopy(index)
rid='availability_nintendo_1_2';record=changed.records[rid];record['fields']['name']['value']={'th':'Student Lounge Nintendo','en':'Student Lounge Nintendo'}
checks['source_service_name_not_personal_role']=not request(changed,'Student Lounge Nintendo ราคาเท่าไหร่')['unresolved']
def ask(q):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model/HTTP')),patch.dict(os.environ,{'PSU_ANALYSIS_BUDGET_SEC':'0'}):return reader.answer(q,locale='th',planner=None)
good=ask(clean);forced=guard_result(reader,good,snap,index,typo,None,'th')
checks['forced_compatibility_price_withheld']=bool(good.hits) and not forced.hits and 'ยืนยันกลุ่มผู้ใช้' in forced.answer
forced_compound=guard_result(reader,good,snap,index,typo+' แล้วจองยังไง',None,'th')
checks['forced_flat_compound_price_withheld']=bool(good.hits) and not forced_compound.hits and 'ยืนยันกลุ่มผู้ใช้' in forced_compound.answer
for label,q in [('compound',typo+' แล้วจองยังไง'),('negated','ไม่ใช่นักศึกษา PSU เล่น Nintendo Switch 30 นาที เสียกี่บาท')]:
 result=ask(q);rows.append({'question':q,'answer':result.answer,'hits':result.hits,'artifact':result.decision_artifact})
 ratehits=[h for h in result.hits if index.records.get(h.get('record_id'),{}).get('kind')=='rate']
 checks[label+'_no_guessed_rate']=not ratehits
 if label=='compound':checks['compound_booking_survives']='สลิป' in result.answer and 'ยืนยันกลุ่มผู้ใช้' in result.answer
out=R/('audience_role_controls_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'scope':'bounded lexical role ambiguity; source-only natural + forced receipts/compatibility; name mutation is a parser control, not owner-edit proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
