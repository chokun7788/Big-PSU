import json,urllib.request,time,uuid,sys
from pathlib import Path
OUT=Path(__file__).resolve().parent;BASE='http://127.0.0.1:8098'
run=sys.argv[1] if len(sys.argv)>1 else '1'
gate_started=time.monotonic();last_gate='';gate_ok=False
while time.monotonic()-gate_started<45:
    try:
        with urllib.request.urlopen(BASE+'/health',timeout=2) as res:health=json.load(res)
        workers=health.get('pipeline_workers',{}).get('workers',[])
        if health.get('ok') and health.get('warmup',{}).get('ok') and workers and all(w.get('ready') and w.get('alive') for w in workers):gate_ok=True;break
    except Exception as e:last_gate=repr(e)
    time.sleep(.25)
(OUT/f'web_startup_gate_{run}.json').write_text(json.dumps({'ready':gate_ok,'wait_sec':time.monotonic()-gate_started,'last_error':last_gate},indent=2))
if not gate_ok:raise SystemExit('Fixture not ready; answer tests were not run.')
CASES=[
 ('ดาวทะเลผจญภัยเล่นยังไง','th',['เก็บไข่มุก'],[]),
 ('Starfish Quest how to play','en',['Collect pearls'],[]),
 ('Starfish Quesst controls','en',['Space'],[]),
 ('Starfish Quest PC controls','en',['Space'],[]),
 ('ดาวทะเลผจญภัยเล่นยังไงแล้วปุ่มอะไรบ้าง','th',['เก็บไข่มุก','Space'],[]),
 ('How to play Starfish Quest and what buttons do I press?','en',['Collect pearls','Space'],[]),
 ('Starfish Quest genre','en',['Not yet confirmed'],[]),
 ('Coral Trail เล่นยังไง','th',['เก็บปะการัง'],[]),
 ('Coral Traill เล่นยังไง','th',['เก็บปะการัง'],[]),
 ('Coral Trail how to play','en',['เก็บปะการัง','Thai source'],[]),
 ('Coral Trail ปุ่มอะไรบ้าง','th',['ยังไม่มีข้อมูลยืนยัน'],['Space']),
 ('Starfish Quest ทั้งหมด','th',['Space','เก็บไข่มุก'],[]),
 ('ไก่กับไข่อะไรเกิดก่อนกัน','th',[],['Space','เก็บไข่มุก']),
 ('เย็นนี้กินอะไรดี','th',[],['Space','เก็บไข่มุก']),
 ('PC ราคาเท่าไหร่','th',[],['Collect pearls','Space']),
 ('ศูนย์อยู่ที่ไหน','th',['ยังไม่มีข้อมูลยืนยัน'],['อาคาร','5']), # Published fixture center has unknown address.
 ('เอาคีย์บอร์ดของตัวเองมาได้ไหม','th',['ไม่อนุญาต'],[]),
 ('กฎการแข่งขัน valorant มีอะไรบ้าง','th',[],['Starfish']),
 ('สามารถถามอะไรได้บ้าง','th',[],['Starfish']),
 ('Starfish Quest PS4 controls','en',['No confirmed'],['Space']),
 ('Starfish Quest บังคับตัวละครด้วยอะไร','th',[],['เก็บไข่มุก']),
 ('Starfish Quest ขอรายละเอียด','th',['เก็บไข่มุก'],[]),
]
def ask(q,lang,session,last_seen=''):
    body={'question':q,'locale':lang,'client_session_id':session,'client_turn_id':'turn-'+str(uuid.uuid4()),'last_seen_response_id':last_seen,'experimental_allow_llm':True,'experimental_rag_fallback':True,'request_id':str(uuid.uuid4())}
    req=urllib.request.Request(BASE+'/api/chat',data=json.dumps(body,ensure_ascii=False).encode('utf-8'),headers={'Content-Type':'application/json'})
    start=time.perf_counter()
    with urllib.request.urlopen(req,timeout=65) as res:x=json.load(res)
    return x,time.perf_counter()-start
results=[]
for q,lang,must,mustnot in CASES:
    try:
        x,elapsed=ask(q,lang,str(uuid.uuid4()));a=x.get('answer','');errors=[f'missing {t}' for t in must if t not in a]+[f'unexpected {t}' for t in mustnot if t in a]
        if q.startswith(('ดาวทะเล','Starfish','How to play Starfish','Coral')) and not x.get('mode','').startswith('pipeline:common_'):errors.append('did not use common route')
        r={'question':q,'locale':lang,'elapsed':elapsed,'errors':errors,'response':x};results.append(r);print(q, 'PASS' if not errors else 'FAIL '+str(errors),f'{elapsed:.2f}s',flush=True)
    except Exception as e:results.append({'question':q,'errors':[repr(e)]});print(q,'ERROR',e,flush=True)
session=str(uuid.uuid4());last_seen=''
for q,must in [('ดาวทะเลผจญภัยเล่นยังไง',['เก็บไข่มุก']),('แล้วปุ่มล่ะ',['Space']),('แล้วทั้งหมด',['Space','เก็บไข่มุก'])]:
    try:
        x,elapsed=ask(q,'th',session,last_seen);last_seen=x.get('request_id','');errors=[f'missing {t}' for t in must if t not in x.get('answer','')];results.append({'question':q,'session_flow':'new_game_followup','elapsed':elapsed,'errors':errors,'response':x});print('followup',q,'PASS' if not errors else errors,flush=True)
    except Exception as e:results.append({'question':q,'errors':[repr(e)]})
(OUT/f'web_results_{run}.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print('TOTAL',len(results),'FAILED',sum(bool(r['errors']) for r in results),flush=True)
