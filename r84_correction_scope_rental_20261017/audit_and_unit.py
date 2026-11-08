import copy,hashlib,json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
sys.path.insert(0,str(S));import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.correction_scope import compatible,subject_types
from app.knowledge.common.profile_confirmation import eligible
from app.knowledge.common.question_profiles import select
from app.knowledge.common.unconfirmed_request import topic
from app.knowledge.common.query_scope import operation,rental_ids
from app.knowledge.common.audience_scope import resolve
records=MigratedView(S/'data/knowledge/common.sqlite').snapshot()['release']['records']
slip='procedure_wrong_slip';checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
from contracts import CASES
for name,lang,turns in CASES:
 for q,expect in turns:
  if expect in {'wrong_amount','identity_correction'}:
   check(name+' classified',topic(q)==expect,topic(q))
   check(name+' excludes fallback menu',slip not in eligible(q,records))
   check(name+' excludes literal match',select(q,records)[0]!=slip)
for q in ['แนบสลิปผิดรูป','I uploaded the wrong payment image','แนบหลักฐานโอนเงินผิด']:
 check('Valid proof remains eligible '+q,slip in eligible(q,records))
for q in ['Wrong payment amount and I overpaid','ยอดเงินผิดผมจ่ายเกิน']:
 check('Overpayment retains priority '+q,topic(q)=='overpayment')
# A future owner profile with the right declared subject is not blocked.
profile={'task':'correction','subjects':[{'en':'proof of identity','th':'หลักฐานยืนยันตัวตน'}]}
check('New identity subject remains selectable',compatible('wrong proof of identity',profile))
check('Image is not an amount',not compatible('The payment amount was incorrect',{'task':'correction','subjects':[{'en':'payment-slip image'}]}))
check('Unknown word is not rejected as proven conflict',compatible('I attached the wrong blorple',{'task':'correction','subjects':[{'en':'payment-slip image'}]}))
check('Multiple distinct subjects cannot use one procedure',not compatible('Wrong proof of identity and wrong payment image',{'task':'correction','subjects':[{'en':'payment-slip image'}]}))
for text,expected in [('How much is half-day PS5 rental?','rental'),('How much is PC?','price'),('How much is the fine in competition rules?','rules')]:check('Operation '+text,operation(text)==expected)
for text,expected in [('external organization',['audience_external_org']),('external organisations',['audience_external_org']),('internal organization',['audience_internal_org']),('internal units',['audience_internal_org']),('not external organization, internal unit',['audience_internal_org'])]:check('Organization actor '+text,resolve(text,records)[0]==expected,resolve(text,records))
check('Visitors do not become organizations',resolve('visitor',records)[0] is None)
check('Public audience not treated as external organization',resolve('general public',records)[0]==['audience_general_adult'])
check('All zones is one package scope',set(rental_ids('เหมาทุกโซนเต็มวันหน่วยงานภายนอก',['audience_external_org'],records))=={'rental_all_zones_external_full_day'})
source=json.loads((B/'WORKBOOK_SOURCE.json').read_text(encoding='utf8'));cells=source['cells'];prices=[]
for row,zone in [(3,'all_zones'),(4,'cockpit'),(5,'vr'),(6,'nintendo_switch'),(7,'ps5'),(8,'pc')]:
 for col,audience,period in [('B','external','full_day'),('C','external','half_day'),('D','internal','full_day'),('E','internal','half_day')]:
  rid=f'rental_{zone}_{audience}_{period}';r=records.get(rid);cell=f'{col}{row}';v=cells[cell]
  passed=bool(r and r['fields']['amount_minor']['value']==v*100 and r['fields']['audience_id']['value']=='audience_'+audience+'_org' and r['fields']['period_label']['value']==period)
  prices.append({'record_id':rid,'cell':cell,'source_baht':v,'matches':passed,'validity':r['validity'] if r else None})
  check('Workbook source price '+rid,passed)
check('Exactly 24 active package records',len([r for r in records.values() if r['kind']=='rental_package'])==24)
check('Archived workbook is byte-identical',source['source_sha256']==source['archived_sha256'])
out=B/'verification'/(sys.argv[1] if len(sys.argv)>1 else 'unit_2');out.mkdir(parents=True,exist_ok=False)
(out/'RENTAL_AUDIT.json').write_text(json.dumps({'source_path':source['source_path'],'sheet':source['sheet_names'][0],'source_range':'B3:E8','rows':prices,'matched':sum(x['matches'] for x in prices),'count':len(prices),'source_sha256':source['source_sha256'],'archived_sha256':source['archived_sha256']},ensure_ascii=False,indent=2),encoding='utf8')
(out/'UNIT_RESULTS.json').write_text(json.dumps({'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks,'real_model_verified':False},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'count':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x for x in checks if not x['passed']]},ensure_ascii=False))
raise SystemExit(any(not x['passed'] for x in checks))
