import json,sqlite3,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;db=R/'system/data/knowledge/common.sqlite'
c=sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True)
records={rid:json.loads(p) for rid,p in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
sources={sid:{'metadata':json.loads(payload),'snapshot':json.loads(snapshot)} for sid,payload,snapshot in c.execute('SELECT source_id,payload,snapshot FROM cc_sources')}
write=lambda n,v:(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
write('NATIVE_BEFORE.json',{'records':records,'sources':sources,'withdrawn':[x[0] for x in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]})
print('records',len(records),'sources',len(sources))
for rid in ['game_detail_new_super_mario_bros','member_1d884f11f3890dea','availability_nintendo_1_2','migrated_schedule_4']:
 r=records.get(rid);print(rid,json.dumps(r,ensure_ascii=False)[:2200])
print('source samples')
for sid,x in list(sources.items())[:2]:print(sid,x['metadata'],list(x['snapshot']) if isinstance(x['snapshot'],dict) else type(x['snapshot']).__name__)
const=json.loads((R/'CODE_CONSTANTS.json').read_text('utf8'))
for x in const:
 if any(t in ' '.join(x['names']) for t in ['CUSTOMER_GROUP_ALIASES','SERVICE_ALIASES','SERVICE_FEES','WEEKLY','OPENING','HOURS']):print('CONST',x['path'],x['names'],str(x['value'])[:400])
print('code constants paths',sorted(set(x['path'] for x in const)))
