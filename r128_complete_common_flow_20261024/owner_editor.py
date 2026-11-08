"""Owner editor bound to the same copied draft database as R128 chat."""
import getpass,json,os,secrets,sys,webbrowser
from pathlib import Path
from http.server import ThreadingHTTPServer
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));database=S/'data/knowledge/common.sqlite'
os.environ.update(PSU_KNOWLEDGE_DB=str(database),PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_CHATBOT_OLLAMA_MODEL='psu-r121-trained:latest',OLLAMA_URL='http://127.0.0.1:12421',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import make_handler
store=CommonStore(database)
# Database was initialized in the parent package. Startup is read-only;
# only explicit owner form actions may save/review/publish.
with store.connect() as c:c.execute('SELECT value FROM cc_meta WHERE key=?',('epoch',)).fetchone()
port=12823;token=secrets.token_urlsafe(32);url=f'http://127.0.0.1:{port}/#token={token}'
private=R/'owner_private';private.mkdir(exist_ok=True)
(private/'session.json').write_text(json.dumps({'pid':os.getpid(),'port':port,'url':url,'db':str(database)},ensure_ascii=False),'utf8')
server=ThreadingHTTPServer(('127.0.0.1',port),make_handler(store,token,getpass.getuser(),port));server.daemon_threads=True
if '--open' in sys.argv:webbrowser.open(url)
print('R128 owner editor ready on loopback port 12823; capability stored privately',flush=True)
server.serve_forever()
