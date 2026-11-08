from pathlib import Path
R=Path(__file__).resolve().parent
s=(R.parent/'r126_latency_audit_20261023/serve_audit.py').read_text('utf8')
s=s.replace("S=R.parent/'r125_date_context_presentation_20261023/system'","S=Path(os.environ['R127_SYSTEM'])")
start=s.index('from app.knowledge.common.migrated_view')
end=s.index('original_urlopen=')
hooks=s[start:end]
hooks=hooks.replace('from app.web_api import server\n','')
s=s[:start]+"from app.web_api import server\nif os.environ['R127_ARM']=='legacy':server.WEB_ROOT=R\nif os.environ['R127_ARM']=='current':\n"+'\n'.join(' '+line for line in hooks.splitlines())+'\n'+s[end:]
s=s.replace(" store=MigratedView(S/'data/knowledge/common.sqlite');Engine.from_snapshot(store.snapshot(),cache_key=store.path.resolve())"," if os.environ['R127_ARM']=='current':\n  store=MigratedView(S/'data/knowledge/common.sqlite');Engine.from_snapshot(store.snapshot(),cache_key=store.path.resolve())")
(R/'serve.py').write_text(s,'utf8')
