"""Exercise resumable download and corrupt-file handling with a known local oracle."""
import hashlib, importlib.util, json, tempfile, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

W=Path(__file__).parent
spec=importlib.util.spec_from_file_location('ensure_download',W/'share_ensure_models.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
module.time.sleep=lambda _seconds: None
data=b'known model fixture\0'*8192
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def do_GET(self):
        offset=int(self.headers.get('Range','bytes=0-').split('=')[1].split('-')[0])
        content=data if self.path!='/corrupt' else b'x'*len(data)
        self.send_response(206 if offset else 200)
        if offset:self.send_header('Content-Range',f'bytes {offset}-{len(content)-1}/{len(content)}')
        self.send_header('Content-Length',str(len(content)-offset));self.end_headers()
        self.wfile.write(content[offset:])
server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
cases=[]
try:
    with tempfile.TemporaryDirectory(prefix='psu_share_oracle_') as directory:
        root=Path(directory)
        item={'label':'fixture','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'url':f'http://127.0.0.1:{server.server_port}/good'}
        path=root/'resumed'; path.with_suffix('.partial').write_bytes(data[:123])
        module.fetch(item,path); assert path.read_bytes()==data;cases.append('resume_known_bytes')
        path=root/'oversized';path.with_suffix('.partial').write_bytes(data+b'oversize')
        module.fetch(item,path);assert path.read_bytes()==data;assert list(root.glob('oversized.partial.*.invalid'));cases.append('oversized_partial_preserved')
        path=root/'corrupt';bad={**item,'url':f'http://127.0.0.1:{server.server_port}/corrupt'}
        try:module.fetch(bad,path)
        except RuntimeError as exc:assert 'SHA-256' in str(exc)
        else:raise AssertionError('Corrupt fixture was accepted')
        assert not path.exists() and list(root.glob('corrupt.partial.*.invalid'));cases.append('corrupt_download_not_installed')
finally: server.shutdown();server.server_close()
out=W/'share_download_oracle_results.json'
with out.open('x',encoding='utf-8') as f:json.dump({'cases':cases,'passed':len(cases),'oracle':'known literal fixture bytes, local HTTP server'},f,indent=2)
print(json.dumps({'passed':len(cases),'cases':cases}),flush=True)
