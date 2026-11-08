"""Launch the isolated R114 preview and owner editor on unused loopback ports."""
import argparse,json,os,socket,subprocess,sys,time,urllib.request,webbrowser
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SYSTEM=ROOT/'system'
DB=SYSTEM/'data/knowledge/common.sqlite'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--no-browser',action='store_true')
    p.add_argument('--check',action='store_true',help='Check paths and ports without starting servers')
    a=p.parse_args()
    if not DB.is_file():raise SystemExit('Candidate database is missing.')
    for port in (8134,8135):
        with socket.socket() as s:
            try:s.bind(('127.0.0.1',port))
            except OSError:raise SystemExit(f'Port {port} is occupied. Inspect the existing process before starting again.')
    if a.check:print('Candidate paths and ports are ready.');return
    run=ROOT/'runtime'/datetime.now().strftime('%Y%m%d_%H%M%S_%f');run.mkdir(parents=True)
    env=os.environ.copy()
    # Relative paths must never select an older checkout or production DB.
    env.update(PYTHONPATH=str(SYSTEM),PSU_KNOWLEDGE_DB=str(DB),
        PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',
        PSU_RUNTIME_PROFILE='r114-candidate-preview',PSU_RUNTIME_VERSION='R114',
        PSU_CHAT_LOG_DIR=str(run/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(run/'logs/transcripts.sqlite'),
        PSU_CONVERSATION_STATE_PATH=str(run/'conversation.sqlite'),
        PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',
        PSU_CHATBOT_OLLAMA_MODEL='scb10x/typhoon2.5-qwen3-4b:latest',
        PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',
        PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='30',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='32')
    env.pop('PSU_ESPORTS_NOW',None)
    children=[]
    try:
        for name,module,args in [('chat','app.web_api.server',['--host','127.0.0.1','--port','8134']),
                                 ('owner','app.knowledge.common.owner_server',['--port','8135','--db',str(DB),'--no-browser'])]:
            with (run/(name+'.log')).open('x',encoding='utf8') as log:
                proc=subprocess.Popen([sys.executable,'-B','-X','utf8','-m',module,*args],cwd=SYSTEM,env=env,
                    stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            children.append({'name':name,'pid':proc.pid,'process':proc})
        deadline=time.monotonic()+55;health=None
        while time.monotonic()<deadline:
            if any(c['process'].poll() is not None for c in children):raise RuntimeError('A candidate server exited. Inspect the new runtime logs.')
            try:
                with urllib.request.urlopen('http://127.0.0.1:8134/health',timeout=1) as h:health=json.load(h)
                session=json.loads((DB.parent/'owner-session.json').read_text('utf8'))
                if session['pid']==children[1]['pid']:break
            except (OSError,ValueError,KeyError):time.sleep(.25)
        else:raise RuntimeError('Candidate startup timed out; inspect the new runtime logs.')
        if health.get('common_loaded_build',{}).get('build_id')!='common-r114-domain-flow':raise RuntimeError('Unexpected loaded build.')
        (run/'SERVERS.json').write_text(json.dumps({'db':str(DB),'candidate_only':True,'chat_url':'http://127.0.0.1:8134/',
            'processes':[{k:v for k,v in c.items() if k!='process'} for c in children]},indent=2),'utf8')
        if not a.no_browser:
            webbrowser.open('http://127.0.0.1:8134/');webbrowser.open(session['url'])
        print('R114 preview: http://127.0.0.1:8134/')
        print('Owner editor: 127.0.0.1:8135 (open from this launcher; private access stays in owner-session.json)')
        print('Runtime logs: '+str(run))
    except BaseException:
        for c in children:
            c['process'].terminate()
        for c in children:
            try:c['process'].wait(timeout=8)
            except subprocess.TimeoutExpired:c['process'].kill()
        raise

if __name__=='__main__':main()
