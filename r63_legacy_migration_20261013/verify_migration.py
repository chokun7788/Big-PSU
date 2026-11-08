import json,os,sqlite3,sys,hashlib,collections
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent
SYSTEM=BASE/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local';sys.path.insert(0,str(SYSTEM))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import validate,value,pointer
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.owner_server import preview_answer
OUT=Path(sys.argv[1]).resolve();ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
store=CommonStore(OUT/'review/approved.sqlite');checks=[]
def check(name,passed,detail=None):checks.append({'name':name,'passed':bool(passed),'detail':detail})
with store.connect() as c:heads=store.heads(c);sources=store.sources(c)
for rid,r in heads.items():check('schema+FK+evidence:'+rid,not validate(r,heads,sources),validate(r,heads,sources))
for row in json.loads((OUT/'SOURCE_MANIFEST.json').read_text(encoding='utf-8')):
 p=ROOT/row['path'];q=OUT/'original_files'/row['path'];h=row['sha256']
 check('source preserved:'+row['path'],hashlib.sha256(p.read_bytes()).hexdigest()==h==hashlib.sha256(q.read_bytes()).hexdigest())
for f in json.loads((OUT/'FIELD_LINEAGE.json').read_text(encoding='utf-8')):
 p=OUT/'original_files'/f['source_path'];raw=p.read_text(encoding='utf-8-sig')
 data=[json.loads(x) for x in raw.splitlines() if x.strip()] if p.suffix=='.jsonl' else json.loads(raw) if p.suffix=='.json' else raw
 check('source locator:'+f['record_id']+':'+f['field'],pointer(data,f['locator'])==f['source_value'])
 check('target retained:'+f['record_id']+':'+f['field'],value(heads[f['record_id']],f['field'])==f['mapped_value'])
with sqlite3.connect((OUT/'before.sqlite').as_uri()+'?mode=ro',uri=True) as before,store.connect() as after:
 before.row_factory=sqlite3.Row
 tables=[x[0] for x in before.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
 for table in tables:
  rows=before.execute('SELECT * FROM "'+table+'"').fetchall()
  afterrows=after.execute('SELECT * FROM "'+table+'"').fetchall()
  # Preserve every historical row, except intentionally updated draft heads/epoch.
  if table=='cc_heads':
   nowrows={x['record_id']:x for x in afterrows};ok=all(x['record_id'] in nowrows and nowrows[x['record_id']]['head']>=x['head'] and nowrows[x['record_id']]['withdrawn']==x['withdrawn'] for x in rows)
  elif table=='cc_meta':
   a=dict((x['key'],x['value']) for x in afterrows);ok=all(x['key']=='epoch' or a.get(x['key'])==x['value'] for x in rows)
  else:ok=set(tuple(x) for x in rows)<=set(tuple(x) for x in afterrows)
  check('original history:'+table,ok)
  if table in {'cc_approvals','cc_releases'}:check('no automatic '+table,len(rows)==len(afterrows))
 with sqlite3.connect((ROOT/'data/knowledge/approved.sqlite').as_uri()+'?mode=ro',uri=True) as prod:
  check('original production logical DB unchanged',list(before.iterdump())==list(prod.iterdump()))

# Independent semantic controls; expected money values from the supplied table.
amounts={'playstation_5_60_1_2':[0,50,150],'nintendo_switch_60_1_2':[0,50,140],'nintendo_switch_60_3_4':[0,100,280],'cockpit_60_1_1':[0,65,200],'vr_30_1_5':[0,190,525],'vr_60_1_5':[0,375,1050]}
groups=['psu_student_staff','psu_alumni_general_student','general_adult']
for scope,values in amounts.items():
 for grp,amount in zip(groups,values):
  r=heads['migrated_rate_'+scope+'_'+grp];check('independent rate:'+scope+':'+grp,value(r,'amount_minor')==amount*100 and r['validity']['effective_until']=='2026-04-01T00:00:00+07:00')

inventory=json.loads((BASE/'r63_legacy_migration_20261013/SOURCE_INVENTORY.json').read_text(encoding='utf-8'))
def rid(s):return __import__('re').sub('[^a-z0-9_:-]','_',s.lower())
for row in inventory:
 source=json.loads((ROOT/row['path']).read_text(encoding='utf-8'))
 if row['kind']=='competition_document':
  for occurrence,sec in enumerate(source['locales']['th']['fields']['sections']):
   target=heads[rid(row['id'])+'_section_'+str(occurrence+1).zfill(3)]
   check('complete competition section:'+target['record_id'],value(target,'text')['th']==sec['text'] and value(target,'heading')['th']==sec['section_title'])
 if row['kind']=='control_map':
  r=heads[rid(row['id'])];text=value(r,'limitations')['th'];controls=source['locales']['th']['fields']['controls']
  check('controls no fabricated gesture:'+row['id'],value(r,'bindings') is None and all(all(not control.get(k) or control[k] in text for k in ['button','action_th','description_th','section']) for control in controls))
 if row['kind']=='service_availability':
  service=heads[row['id']];links=[r for r in heads.values() if r['kind']=='game_service' and value(r,'service_id')==row['id']]
  titles={value(heads[value(r,'game_id')],'title')['th'] for r in links}
  normalize=lambda text:__import__('re').sub(r'[^\w]','',__import__('unicodedata').normalize('NFKC',text).casefold())
  check('exact offered game scope:'+row['id'],set(map(normalize,source['facts']['games']))==set(map(normalize,titles)) and len(links)==len(source['facts']['games']),{'source':source['facts']['games'],'target':sorted(titles),'normalization':'NFKC, case and punctuation only; editions/numbers retained'})
check('PC 01 Tekken included', 'game_detail_tekken_8' in {value(r,'game_id') for r in heads.values() if r['kind']=='game_service' and value(r,'service_id')=='availability_pc_01_02'})
check('PC 03 Tekken NOT inferred', 'game_detail_tekken_8' not in {value(r,'game_id') for r in heads.values() if r['kind']=='game_service' and value(r,'service_id')=='availability_pc_03_10'})

# Production read cannot use unapproved migration; draft preview explicitly opt-in.
queries=['Animal Crossing เล่นยังไง','ราคาเหมาครึ่งวัน PC หน่วยงานภายนอก','กฎแข่งขัน Tekken 8','ต้องเป็นสมาชิกไหม','How do I play Animal Crossing?','PC 1 ว่างไหม']
for q in queries:check('unpublished migration isolated:'+q,CommonAnswerer(store).answer(q,locale='en' if q.startswith('How') else 'th') is None)
os.environ['PSU_LOCAL_LLM_ASSIST_ENABLED']='0'
previewcases=[('Animal Crossing วิธีเล่น','game_detail_animal_crossing','how_to_play'),('Gaming PC รุ่น MSI MAG Infinite S3 14th รายละเอียด','equipment_gaming_pc','usage'),('นายธนชาติ เอ่งฉ้วน รายละเอียด','member_0629f0033d3d9b24','role'),('คนเล่นต้องเป็นคนที่จองหรือมีรายชื่ออยู่ในรายการจอง','migrated_owner_claim_player_identity','answer')]
preview=[]
for q,record,key in previewcases:
 try:
  result=preview_answer(store,q,draft=True);expected=value(heads[record],key);text=expected.get('th') if isinstance(expected,dict) else str(expected)
  passed=result is not None and text in result.answer
  preview.append({'question':q,'expected_record':record,'expected_field':key,'expected_text':text,'answer':result.answer if result else None,'route':str(result.route) if result and hasattr(result,'route') else None,'passed':passed})
 except Exception as e:preview.append({'question':q,'passed':False,'error':str(e)})
report={'passed':sum(x['passed'] for x in checks),'total':len(checks),'failures':[x for x in checks if not x['passed']],'checks':checks,'draft_preview':preview,'draft_preview_llm':False,'does_not_certify_all_future_questions':True}
(OUT/'VERIFICATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in {'checks','draft_preview'}},ensure_ascii=False))
print('PREVIEW',json.dumps(preview,ensure_ascii=False))
if report['failures']:raise SystemExit(1)
