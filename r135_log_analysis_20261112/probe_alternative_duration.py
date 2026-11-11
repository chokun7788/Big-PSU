"""Source-only baseline for an actual contradictory PC duration notice."""
import importlib.util,json,os,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(sys.argv[1]).resolve();sys.path.insert(0,str(R/'system'))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'))
out=R/('alternative_duration_'+str(time.time_ns()));out.mkdir();rows=[];checks={}
for n,q in enumerate(['นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท','PSU Student plays PC for 30 minutes, how much does it cost?','นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง']):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model/HTTP permitted')),patch.dict(os.environ,{'PSU_ANALYSIS_BUDGET_SEC':'0'}):result=reader.answer(q,locale='en' if n==1 else 'th',planner=None)
 answer=result.answer;rows.append({'question':q,'answer':answer,'hits':result.hits,'artifact':result.decision_artifact})
 checks[f'normal_price_{n}']=bool(result.hits) and ('0 บาท' in answer or '0 THB' in answer)
 checks[f'no_false_duration_notice_{n}']=not ('ยังยืนยันการใช้เงื่อนไขต่อไปนี้' in answer or 'Application of these requested constraints remains unverified' in answer)
 if n==2:checks['booking_survives']='สลิป' in answer
report={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'model_calls':0,'scope':'actual source-only natural delivery for same-audience alternative PC services, not semantic accuracy'}
(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));sys.exit(0 if report['all_passed'] else 1)
