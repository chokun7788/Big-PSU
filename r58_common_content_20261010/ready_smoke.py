import json,urllib.request,time,uuid,hashlib
from pathlib import Path
OUT=Path(__file__).resolve().parent;PACK=OUT/'ready_package/PSU_Esports_Chatbot_Local';base='http://127.0.0.1:8098';results=[]
def get(url,headers=None):
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers or {}),timeout=3) as r:return json.load(r)
started=time.monotonic();health=None
while time.monotonic()-started<45:
    try:
        health=get(base+'/health')
        if health.get('ok') and health.get('warmup',{}).get('ok') and health.get('runtime',{}).get('version')=='2026.10.10-common-r58.2' and all(w['ready'] and w['alive'] for w in health['pipeline_workers']['workers']):break
    except (OSError,KeyError):pass
    time.sleep(.25)
else:raise SystemExit('Ready package has not passed health gate; inspect ready_start logs.')
(OUT/'ready_health.json').write_text(json.dumps(health,ensure_ascii=False,indent=2),encoding='utf-8')
session=json.loads((PACK/'data/knowledge/owner-session.json').read_text(encoding='utf-8'));token=session['url'].split('#token=')[1]
headers={'Authorization':'Bearer '+token};registry=get('http://127.0.0.1:8097/api/registry',headers);status=get('http://127.0.0.1:8097/api/status',headers)
results.append({'check':'owner_registry','ok':registry['kinds']==24 and sum(len(c['fields']) for c in registry['catalog'])==155})
results.append({'check':'production_unpublished_drafts','ok':not status['demo'] and status['active']=='' and len(status['records'])==41 and not status['published_ids'],'record_count':len(status['records']),'demo':status['demo'],'active':status['active']})
for q,lang,must,mustnot in [('ศูนย์อยู่ที่ไหน','th',['อาคาร','5'],[]),('เอาคีย์บอร์ดของตัวเองมาได้ไหม','th',['ไม่อนุญาต'],[]),('How far ahead must I book?','en',['at least 1 hour'],[]),('Coral Trail เล่นยังไง','th',[],['เก็บปะการัง','Collect pearls','Space'])]:
    body={'question':q,'locale':lang,'client_session_id':str(uuid.uuid4()),'client_turn_id':'smoke-'+uuid.uuid4().hex,'experimental_allow_llm':True,'experimental_rag_fallback':True}
    req=urllib.request.Request(base+'/api/chat',data=json.dumps(body,ensure_ascii=False).encode('utf-8'),headers={'Content-Type':'application/json'})
    start=time.perf_counter()
    try:
        with urllib.request.urlopen(req,timeout=30) as r:x=json.load(r)
        errors=[s for s in must if s not in x.get('answer','')]+['unexpected '+s for s in mustnot if s in x.get('answer','')]
        results.append({'question':q,'ok':not errors and x.get('ok') is True,'errors':errors,'wall_sec':time.perf_counter()-start,'response':x})
    except Exception as e:results.append({'question':q,'ok':False,'error':repr(e)})
(OUT/'ready_smoke_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
hashes={p.relative_to(PACK/'app/knowledge/common').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (PACK/'app/knowledge/common').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
(OUT/'ready_common_file_hashes.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
print(json.dumps({'checks':len(results),'passed':sum(r['ok'] for r in results),'failed':[r for r in results if not r['ok']],'runtime':health['runtime']['version']},ensure_ascii=False))
if any(not r['ok'] for r in results):raise SystemExit(1)
