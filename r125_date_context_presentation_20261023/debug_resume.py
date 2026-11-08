import json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1',PSU_LIVE_BOOKING_ENABLED='1',PSU_LIVE_BOOKING_FETCH_MODE='wordpress')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common.flow_context import request_context
c=json.loads((R/'LIVE_API_PROCESS.json').read_text('utf8'));rows=json.loads((Path(c['output'])/'API_RESULTS.json').read_text('utf8'))
prior=next(r['response'] for r in rows if r['question']=='พฤศจิกายน')
h=[{'role':'assistant','text':prior['answer'],'delivery_status':'server_written','common_read_state':prior['common_read_state']}]
with request_context():r=answer(CommonAnswerer(MigratedView(S/'data/knowledge/common.sqlite')),'PC2',locale='th',history=h,planner=object())
print(r.answer if r else 'NONE')
