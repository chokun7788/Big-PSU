"""Real HTTP conversation replay: intent, target, sections and new clauses."""
import json, re, sys, time, uuid, urllib.request
from pathlib import Path
from datetime import datetime

W=Path(__file__).parent
if not (W/'r37_report_path.txt').exists():
    R=W/('r37_conversation_tests_'+datetime.now().strftime('%Y%m%d_%H%M%S'))
    R.mkdir()
    (W/'r37_report_path.txt').write_text(str(R),encoding='utf-8')
else:
    R=Path((W/'r37_report_path.txt').read_text(encoding='utf-8').strip())
port=int(sys.argv[1]); run=sys.argv[2]
T=lambda q, kind='overview', game='valorant':dict(q=q,kind=kind,game=game)
sessions=[
 ('original','th',[T('มีเกมอะไรให้แข่งมั่ง','catalog'),T('valorant'),T('ขอกฏหนาอย'),T('ขอกฏของเกมหน่อย'),T('ขอกฏของเกม valo หน่อย'),T('มีกฏอื่นไหม','more')]),
 ('polite','th',[T('ตอนนี้มีเกมไหนให้แข่งบ้างครับ','catalog'),T('เอาวาโล'),T('ขอกฎเกมนี้หน่อยย'),T('แล้วมีกฎอื่นอีกมั้ย','more')]),
 ('typo','th',[T('มีเกมไรให้แข่งมั่ง','catalog'),T('valroant'),T('ขอกฎหน่อยยย'),T('มีข้ออื่นอีกป่าว','more')]),
 ('casual','th',[T('แข่งเกมไหนได้บ้าง','catalog'),T('วาโลครับ'),T('กติกาเกมนี้มีไรมั่ง'),T('แล้วข้ออื่นล่ะ','more')]),
 ('continuation','th',[T('มีเกมอะไรให้แข่งขันบ้าง','catalog'),T('valo'),T('ขอกฏของเกมหน่อย'),T('ต่ออีกหน่อย','more')]),
 ('english','en',[T('Which games can we compete in?','catalog'),T('valo'),T('can i see the rulez for this game pls'),T('any other rulez?','more')]),
 ('explicit','th',[T('ขอกฏของเกม valo หน่อย'),T('มีกฏอื่นไหม','more')]),
 ('switch','th',[T('ขอกฎแข่ง VALORANT'),T('แล้ว cs2','overview','cs2'),T('มีกฎอื่นไหม','more','cs2'),T('กฎศูนย์มีอะไรบ้าง','center')]),
 ('topic_boundary','th',[T('ขอกฎแข่ง VALORANT'),T('เปิดกี่โมง','schedule'),T('มีกฎอื่นไหม','no_inherit')]),
 ('unsupported','th',[T('ขอกฎแข่ง VALORANT'),T('กฎแข่ง Minecraft','unsupported')]),
 ('edition','th',[T('ขอกฎแข่ง VALORANT'),T('ขอกฎแข่ง VALORANT ปี 2024','edition')]),
 ('new_task','th',[T('ขอกฎแข่ง VALORANT'),T('ไม่เอากฎแล้ว VALORANT คืออะไร','games')]),
]
if len(sys.argv)>3:
 sessions=json.loads(Path(sys.argv[3]).read_text(encoding='utf-8'))
def compact(text):return re.sub(r'\s+','',str(text)).casefold()
def bullets(answer):
    return [re.sub(r'^[•*\-]\s*','',line).strip() for line in answer.splitlines() if re.match(r'^\s*[•*\-]\s+',line) and len(line.strip())>18]

records=[]
with (R/(run+'.jsonl')).open('x',encoding='utf-8') as f:
 for sid,locale,turns in sessions:
  history=[]; session='r37-test-'+uuid.uuid4().hex
  for i,case in enumerate(turns):
   q=case['q']; payload=dict(question=q,locale=locale,recent_history=history[-10:],client_session_id=session,debug=True,experimental_rag_fallback=True)
   start=time.perf_counter()
   try:
    req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=60) as response:x=json.load(response)
   except Exception as exc:x={'error':repr(exc)}
   errors=[]; category=x.get('route_category'); answer=x.get('answer',''); mode=x.get('mode',''); sources=x.get('sources',[]); ctx=x.get('context_resolution',{})
   kind=case['kind']; emitted=bullets(answer); novel=[]
   if x.get('error') or not answer:errors.append('request_or_empty_answer')
   if kind=='catalog':
    if x.get('route_intent')!='competition_rulebook_catalog':errors.append('not_competition_catalog')
    for title in ('Counter-Strike 2','RoV','Tekken 8','VALORANT'):
     if title not in answer:errors.append('catalog_missing:'+title)
    if ('ไม่ได้ยืนยัน' if locale=='th' else 'does not confirm') not in answer:errors.append('catalog_missing_registration_boundary')
   if kind in ('overview','more','detail'):
    if category!='competition_rules':errors.append('wrong_domain:'+str(category))
    if kind!='detail' and 'competition_rule_overview_source' not in mode:errors.append('not_source_overview')
    expected='competition_rules_'+case['game']+'_'
    if not sources or not all(expected in str(s.get('url','')) for s in sources):errors.append('wrong_or_missing_rulebook_sources')
    if kind=='overview' and answer.count('**')<6:errors.append('fewer_than_three_sections')
    prior=[compact(item['text']) for item in history if item['role']=='assistant' and item.get('route_category')=='competition_rules']
    novel=[line for line in emitted if not any(compact(line) in a for a in prior)]
    if kind=='more':
     if len(novel)<2:errors.append('fewer_than_two_new_clauses')
     repeated=[line for line in emitted if any(compact(line) in a for a in prior)]
     if repeated:errors.append('repeated_clauses:'+str(len(repeated)))
   if kind=='center':
    if category=='competition_rules' or ctx.get('used_context'):errors.append('competition_leaked_into_center_policy')
   if kind=='detail':
    for word in case.get('must_include',[]):
     if word.casefold() not in answer.casefold():errors.append('requested_detail_missing:'+word)
   if kind in ('schedule','games'):
    if category!=kind:errors.append('new_task_wrong_domain:'+str(category))
    if ctx.get('used_context'):errors.append('old_competition_context_leaked')
   if kind=='no_inherit':
    if ctx.get('context_game') or ctx.get('used_context') or category=='competition_rules':errors.append('context_crossed_topic_boundary')
   if kind in ('unsupported','edition'):
    if sources:errors.append('borrowed_other_game_or_edition_source')
    if kind=='edition' and '2024' not in answer:errors.append('requested_year_missing')
   row=dict(session=sid,turn=i+1,expect=case,payload=payload,result=x,wall_sec=round(time.perf_counter()-start,3),errors=errors,passed=not errors,new_clause_count=len(novel))
   records.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
   print(json.dumps(dict(session=sid,turn=i+1,q=q,mode=mode,errors=errors,new_clause_count=len(novel)),ensure_ascii=False),flush=True)
   history.extend([dict(role='user',text=q),dict(role='assistant',text=answer,route_category=category,route_intent=x.get('route_intent'),resolved_text=ctx.get('resolved_question',''),universal_intent=x.get('universal_intent'))])
summary=dict(requests=len(records),passed=sum(x['passed'] for x in records),failed=[{k:x[k] for k in ('session','turn','expect','errors')} for x in records if not x['passed']],scope='HTTP route + catalogue + same-game sources + overview sections + literal new-clause checks + topic/edition boundaries; not full expert or owner approval')
with (R/(run+'_SUMMARY.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False),flush=True)
