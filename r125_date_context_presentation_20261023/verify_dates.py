"""Current-date and delivered month context regressions; no network/model."""
import copy,json,os,re,sys,time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.dialogue import state_from_answer
from app.knowledge.common.domain_flow.date_context import resolve
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.flow_context import request_context
store=MigratedView(S/'data/knowledge/common.sqlite');checks={};outputs=[];at=reference_time('2026-10-20T12:00:00+07:00')
OUT=R/('date_verification_'+str(time.time_ns()));OUT.mkdir()
def forbidden(*a,**k):raise AssertionError('This request must not use model or network')
def run(q,history=None,clock=at):
 with patch('urllib.request.urlopen',forbidden),request_context():
  result=answer(CommonAnswerer(store),q,locale='th',at=clock,history=history,planner=object())
 assert result is not None
 outputs.append({'question':q,'answer':result.answer,'artifact':result.decision_artifact,'elapsed':result.elapsed})
 return result
for q,date in [('วันที่26ตุลาเปิดไหม','2026-10-26'),('วันที่ 26 ตุลาคม 2569 เปิดไหม','2026-10-26'),('วันที่26 ต.ค. เปิดไหม','2026-10-26'),('วันที่ 26/10/2026 เปิดไหม','2026-10-26'),('วันที่ 26 ตุลา พ.ศ.2569 เปิดไหม','2026-10-26'),('วันที่25เปิดไหม','2026-10-25'),('วันที่20เปิดไหม','2026-10-20'),('PC2 วันที่27 ว่างไหม','2026-10-27')]:
 r=resolve(q,at);checks['date_'+q]=r['target_date']==date
for q in ['วันที่ 26 ตุลาเปิดไหม','วันที่27เปิดไหม','วันที่ 25 เปิดไหม']:
 r=run(q);checks['fast_calendar_'+q]=bool(r.decision_artifact.get('need_results')) and not r.decision_artifact.get('domain_flow',{}).get('model_events')
checks['oct26_is_monday_open_13_16']='วันจันทร์ที่ 26 ตุลาคม 2569' in outputs[0]['answer'] and '13:00–16:00' in outputs[0]['answer'] and 'เปิดให้บริการ' in outputs[0]['answer']
r=run('วันที่15เปิดไหม');state=state_from_answer(r);checks['past_day_asks_month']='เดือนไหน' in r.answer and state['date_pending']['day']==15
history=[{'role':'assistant','text':r.answer,'delivery_status':'server_written','common_read_state':state}]
checks['invalid_month_keeps_pending']=resolve('เดือน13',at,history)['pending']['day']==15
checks['month_reply_buddhist_year']=resolve('พฤศจิกายน พ.ศ.2570',at,history)['target_date']=='2027-11-15'
checks['leading_bare_day_has_current_month']=resolve('27ศูนย์เปิดไหม',at)['target_date']=='2026-10-27'
for month,date in [('ตุลาคม','2026-10-15'),('เดือนหน้า','2026-11-15'),('พฤศจิกายนครับ','2026-11-15'),('เดือน11','2026-11-15')]:
 r=resolve(month,at,history);checks['month_reply_'+month]=r and r.get('target_date')==date
 r=run(month,history);checks['delivered_month_executes_'+month]='ไม่มีข้อมูล' not in r.answer and bool(r.decision_artifact.get('need_results')) and not (state_from_answer(r) or {}).get('date_pending')
r=run('PC2 วันที่15ว่างไหม');s=state_from_answer(r);h=[{'role':'assistant','text':r.answer,'delivery_status':'client_acknowledged','common_read_state':s}]
checks['live_scope_preserved_after_month']=resolve('เดือนหน้า',at,h)['query'].startswith('PC2 วันที่15ว่างไหม')
untrusted=copy.deepcopy(h);untrusted[0]['delivery_status']='uncertain'
checks['untrusted_client_state_not_resumed']=resolve('เดือนหน้า',at,untrusted) is None
checks['topic_change_not_resumed']=resolve('ราคา PC เท่าไร',at,history) is None
checks['invalid_feb_day_clarifies']=resolve('วันที่31กุมภาเปิดไหม',at)['status']=='clarification'
checks['month_end_no_rollover_guess']=resolve('วันที่31เปิดไหม',reference_time('2026-04-20T12:00:00+07:00'))['status']=='clarification'
checks['december_month_reply_rolls_year']=resolve('เดือนหน้า',reference_time('2026-12-20T12:00:00+07:00'),history)['target_date']=='2027-01-15'
r=run('วันที่31เปิดไหม');h=[{'role':'assistant','text':r.answer,'delivery_status':'server_written','common_read_state':state_from_answer(r)}]
# Explicit invalid month/day response uses pending state generated in April.
april=run('วันที่31เปิดไหม',clock=reference_time('2026-04-20T12:00:00+07:00'));ah=[{'role':'assistant','delivery_status':'server_written','common_read_state':state_from_answer(april)}]
checks['february_reply_for_31_clarifies']=resolve('กุมภาพันธ์',at,ah)['status']=='clarification'
engine=Engine.from_snapshot(store.snapshot(),cache_key=store.path.resolve())
for q,cat,facet,op in [('God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง','C05','input_bindings','list'),('Nintendo Switch OLED คืออะไร','C03','usage','detail'),('Counter-Strike 2 map pool ในกติกาคืออะไร','C13','rule_clause','rule_lookup')]:
 u=Understanding([MeaningTask(q,{'C05':'game_controls','C03':'equipment','C13':'competition_rules'}[cat],cat,op,facet)],True,'controlled_presentation_probe',{})
 with patch('urllib.request.urlopen',forbidden):r=engine.answer(q,'th',at=at,allow_llm=False,understanding=u)
 refs=re.findall(r'\[S(\d+)\]',r['answer']);checks['citations_in_range_'+cat]=all(1<=int(n)<=len(r['claims']) for n in refs) and set(map(int,refs))==set(range(1,len(r['claims'])+1))
 checks['group_heading_once_'+cat]='**' in r['answer'] and r['answer'].count('**'+('Nintendo Switch OLED' if cat=='C03' else 'God of War Ragnarök / PlayStation / PS5' if cat=='C05' else 'PSU Phuket CS2 2026 Tournament')+'**')==1
 outputs.append({'question':q,'answer':r['answer'],'claims':r['claims']})
summary={'all_passed':all(checks.values()),'checks':checks,'model_calls':0,'network_calls':0,'controlled_clock':'2026-10-20T12:00+07:00','output':str(OUT)}
(OUT/'RESULTS.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2),'utf8');(OUT/'VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False,indent=2));assert summary['all_passed']
