import json,time,os
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
out=R/('partial_siblings_'+str(time.time_ns()));out.mkdir();checks={};rows=[]
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'))
for n,q in enumerate(['PC นักศึกษา PSU ราคาเท่าไหร่; Andaman Hotel อยู่ที่ไหน','PC นักศึกษา PSU ราคาเท่าไหร่; กาแล็กซี่นี้มีชื่ออะไร']):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')),patch.dict(os.environ,{'PSU_ANALYSIS_BUDGET_SEC':'0'}):r=reader.answer(q,locale='th',planner=None)
 a=r.decision_artifact or {};checks[f'price_still_delivered_{n}']='0 บาท' in r.answer and any('rate_' in h.get('record_id','') for h in r.hits)
 checks[f'not_reported_complete_{n}']=a.get('response_type')!='answer'
 checks[f'no_borrowed_center_address_{n}']=not any(h.get('record_id')=='center_psu_phuket' and h.get('field') in {'address','building','floor','map_url'} for h in r.hits)
 rows.append({'q':q,'answer':r.answer,'artifact':a,'hits':r.hits});(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'checks':checks,'scope':'2 source-only natural compound requests at zero optional-model budget; no hard deadline or generic availability proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
