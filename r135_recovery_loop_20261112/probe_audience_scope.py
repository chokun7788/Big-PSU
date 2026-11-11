"""New audience-ambiguity audit, actual natural source-only requests, no repair."""
import json,os,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.projection import value
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');index=Engine.from_snapshot(view.snapshot(),cache_key=view.path.resolve()).index;reader=CommonAnswerer(view)
cases=[('foreign_clean','นักศึกษาต่างมหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท'),('foreign_typo','ขอสอบถามหน่อยครับ นักศึกษาต่งามหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท'),('psu_positive','นักศึกษา PSU เล่น Nintendo Switch 30 นาที เสียกี่บาท'),('all_audiences_explicit','Nintendo Switch ราคาแต่ละกลุ่มเท่าไหร่'),('student_unspecified','นักศึกษา เล่น Nintendo Switch 30 นาที เสียกี่บาท'),('psu_negated','ไม่ใช่นักศึกษา PSU เล่น Nintendo Switch 30 นาที เสียกี่บาท')]
out=R/('audience_scope_probe_'+str(time.time_ns()));out.mkdir();rows=[];checks={}
for name,q in cases:
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model/HTTP')),patch.dict(os.environ,{'PSU_ANALYSIS_BUDGET_SEC':'0'}):result=reader.answer(q,locale='th',planner=None)
 rate_ids=sorted({h.get('record_id') for h in result.hits if index.records.get(h.get('record_id'),{}).get('kind')=='rate'})
 groups=sorted({value(index.records[rid],'audience_id') for rid in rate_ids})
 rows.append({'id':name,'question':q,'answer':result.answer,'audience_ids':groups,'rate_ids':rate_ids,'artifact':result.decision_artifact})
 if name=='foreign_clean':checks['normal_foreign_student_only']=groups==['audience_psu_alumni_general_student']
 if name=='foreign_typo':checks['typo_not_unrequested_psu_price']='audience_psu_student_staff' not in groups
 if name=='psu_positive':checks['normal_psu_student_retained']=groups==['audience_psu_student_staff']
 if name=='all_audiences_explicit':checks['explicit_all_audiences_retained']=len(groups)==3
 if name=='student_unspecified':checks['unspecified_student_not_silently_priced_as_psu']='audience_psu_student_staff' not in groups
 if name=='psu_negated':checks['negated_psu_never_delivered']='audience_psu_student_staff' not in groups
(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'model_calls':0,'scope':'natural source-only audience relevance/ambiguity controls; alternative prices are not automatically false amounts; no model or semantic accuracy'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}))
