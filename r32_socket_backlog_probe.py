import socket,concurrent.futures,json
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from pathlib import Path
R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip())
class Handler(BaseHTTPRequestHandler):pass
def trial(size):
 cls=type('ProbeServer',(ThreadingHTTPServer,),{'request_queue_size':size})
 server=cls(('127.0.0.1',0),Handler);clients=[]
 def connect(i):
  s=socket.socket();s.settimeout(1)
  try:s.connect(server.server_address);clients.append(s);return dict(id=i,connected=True)
  except OSError as e:s.close();return dict(id=i,connected=False,error=type(e).__name__,errno=e.errno,winerror=getattr(e,'winerror',None),message=str(e))
 try:
  # Delay accepting deliberately: every connection must fit in the TCP backlog.
  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:rows=list(pool.map(connect,range(10)))
  return dict(backlog=size,total=10,connected=sum(x['connected'] for x in rows),rows=rows)
 finally:
  for s in clients:s.close()
  server.server_close()
rows=[trial(ThreadingHTTPServer.request_queue_size),trial(16)]
with (R/'WINDOWS_SOCKET_BACKLOG_PROBE.json').open('x',encoding='utf-8') as f:json.dump(dict(scope='Isolated Windows localhost TCP listeners: ten connections while accept is deliberately delayed; not an actual WordPress or production load SLA',trials=rows),f,ensure_ascii=False,indent=2)
print(json.dumps(rows),flush=True)
