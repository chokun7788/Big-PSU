"""Example editor, always restricted to DEMO_ONLY.sqlite in this folder."""
import os,sys,json,secrets,socket,webbrowser,argparse
from pathlib import Path
from http.server import ThreadingHTTPServer
BASE=Path(__file__).resolve().parent
SYSTEM=BASE.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
sys.path.insert(0,str(SYSTEM));os.chdir(SYSTEM)
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import make_handler
WARNING='ข้อมูลตัวอย่างแยกเท่านั้น — ไม่ใช่ข้อมูลบริการ ราคา กฎ หรือสถานะจริงของ PSU / DEMO ONLY — NOT PRODUCTION'
def main():
    p=argparse.ArgumentParser();p.add_argument('--no-browser',action='store_true');a=p.parse_args()
    store=CommonStore(BASE/'DEMO_ONLY.sqlite');snapshot=store.snapshot()
    if not snapshot['allow_demo'] or not snapshot['release']:raise SystemExit('Refuse a non-demo or empty database')
    token=secrets.token_urlsafe(32)
    with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
    Original=make_handler(store,token,'DEMO_OPERATOR_NOT_REAL_OWNER',port)
    class DemoHandler(Original):
        def reply(self,code,data,ctype='application/json; charset=utf-8'):
            if ctype.startswith('text/html') and isinstance(data,bytes):
                text=data.decode('utf-8').replace('<body>','<body><header><h1>'+WARNING+'</h1><p>เกมใช้คำอธิบายผู้พัฒนา ส่วนบริการ ราคา กฎ อุปกรณ์ และการติดตั้งเป็นเรื่องสมมุติ ห้ามนำไปยืนยันบริการจริง</p></header>',1)
                text=text.replace('กรอกข้อมูลจริงของศูนย์ ตรวจทาน แล้วเผยแพร่ให้แชทบอทอ่าน','กรอกข้อมูลตัวอย่างในฐาน DEMO นี้เท่านั้น ไม่มีผลกับแชทที่ใช้งานจริง')
                text=text.replace('ข้อมูลที่กรอกเป็นข้อมูลศูนย์ที่ตรวจจากแหล่งจริงแล้ว ช่องไม่ทราบยังคงไม่ทราบ','ข้อมูลที่กรอกเป็นข้อมูลจำลองสำหรับทดสอบเท่านั้น ไม่ได้ยืนยันข้อมูล PSU จริง')
                data=text.encode('utf-8')
            if isinstance(data,dict) and 'answer' in data:data={**data,'answer':WARNING+'\n\n'+data['answer'],'demo_only':True}
            return super().reply(code,data,ctype)
    server=ThreadingHTTPServer(('127.0.0.1',port),DemoHandler);server.daemon_threads=True
    url=f'http://127.0.0.1:{port}/#token={token}'
    (BASE/'demo-owner-session.json').write_text(json.dumps({'pid':os.getpid(),'port':port,'url':url,'db':str(store.path)}),encoding='utf-8')
    print(f'DEMO ONLY editor listening on 127.0.0.1:{port}',flush=True)
    if not a.no_browser:webbrowser.open(url)
    try:server.serve_forever()
    finally:server.server_close()
if __name__=='__main__':main()
