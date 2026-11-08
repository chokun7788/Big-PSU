import ast,collections,json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
for p in (S/'app').rglob('*.py'):ast.parse(p.read_text('utf-8-sig'),filename=str(p))
os.environ.update(PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.projection import value
snap=MigratedView(S/'data/knowledge/common.sqlite').snapshot();e=Engine.from_snapshot(snap,cache_key=S)
out={'syntax_checked':True,'kinds':dict(collections.Counter(r['kind'] for r in e.index.records.values())),'categories':{k:len(v) for k,v in e.index.bycat.items()},'audiences':[r for r in e.index.records.values() if r['kind']=='audience'],'rates':[f for f in e.index.bycat['C06'] if f['facet']=='amount'][:6]}
(R/'SCHEMA_AUDIT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8');print(json.dumps({k:v for k,v in out.items() if k not in {'rates','audiences'}},ensure_ascii=False))
for r in out['audiences']:print(r['record_id'],{k:value(r,k) for k in r['fields']})
