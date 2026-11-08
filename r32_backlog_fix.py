from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip());path=P/'app/web_api/server.py'
with (R/'final10_server_before_backlog.py').open('xb') as f:f.write(path.read_bytes())
s=path.read_text(encoding='utf-8');anchor='def main() -> int:\n';assert s.count(anchor)==1
definition='''class ChatHTTPServer(ThreadingHTTPServer):
    # Let a short burst reach the existing admission/worker limits so the
    # client can receive a bounded, retryable 503 instead of a TCP failure.
    # This changes pending connections only, not active requests or workers.
    request_queue_size = 16


'''
s=s.replace(anchor,definition+anchor).replace('server = ThreadingHTTPServer((args.host, args.port), ChatHandler)','server = ChatHTTPServer((args.host, args.port), ChatHandler)');path.write_text(s,encoding='utf-8')
test='''import unittest, socket, concurrent.futures
from app.web_api.server import ChatHTTPServer, ChatHandler

class NativeBurstIntakeTests(unittest.TestCase):
    def test_ten_pending_connections_reach_native_intake(self):
        server=ChatHTTPServer(('127.0.0.1',0),ChatHandler)
        clients=[]
        def connect(_):
            client=socket.socket();client.settimeout(1)
            try:client.connect(server.server_address);return client
            except Exception:client.close();raise
        try:
            # No accept loop yet: all ten must fit while the server is busy.
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
                futures=[pool.submit(connect,i) for i in range(10)]
                for future in futures:
                    try:clients.append(future.result())
                    except OSError as exc:self.fail(str(exc))
            self.assertEqual(len(clients),10)
        finally:
            for client in clients:client.close()
            server.server_close()
'''
with (P/'tests/test_native_burst_intake_r32.py').open('x',encoding='utf-8') as f:f.write(test)
print('Changed native pending-connection backlog to 16; worker/admission limits retained.')
