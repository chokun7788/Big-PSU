import sys, json, urllib.request, time, uuid
from pathlib import Path
W=Path(__file__).parent;R=Path((W/'r35_report_path.txt').read_text().strip())
port=int(sys.argv[1]);run=sys.argv[2];assist=len(sys.argv)>3 and sys.argv[3]=='assist'
sessions=[
 ('user_original','auto',['มีรายการแข่งอะไรบ้าง','valorant','ขอกฏการแข่ง','valorant'],['competition_rules']*4),
 ('th_pending','th',['ขอกฎการแข่งขัน','cs2'],['competition_rules']*2),
 ('en_pending','en',["What are the tournament rules?",'RoV'],['competition_rules']*2),
 ('en_inherit','en',['What is VALORANT?','Can I see the tournament rules?'],['games','competition_rules']),
 ('topic_change','th',['ขอกฎการแข่งขัน','VALORANT คือเกมอะไร'],['competition_rules','games']),
 ('no_history','en',['VALORANT'],['games']),
 ('facet','th',['แข่งต้องใช้แผนที่อะไร','cs2'],['competition_rules']*2),
 ('year','en',['Show the tournament rules for 2024','VALORANT'],['competition_rules']*2),
 ('switch','th',['ขอกติกาการแข่ง VALORANT','แล้ว RoV'],['competition_rules']*2),
]
if run.startswith('final'):
 for lang in ('th','en'):
  for title in ('Counter-Strike 2','RoV','Tekken 8','VALORANT'):
   sessions.append(('all_games_'+lang+'_'+title,lang,['ขอกฎการแข่งขัน' if lang=='th' else 'What are the tournament rules?',title],['competition_rules']*2))
records=[]
with (R/(run+'_HTTP.jsonl')).open('x',encoding='utf-8') as f:
 for sid,locale,questions,categories in sessions:
  history=[];session='r35-'+uuid.uuid4().hex
  for i,(q,cat) in enumerate(zip(questions,categories)):
   payload=dict(question=q,locale=locale,recent_history=history,client_session_id=session,debug=True,experimental_allow_llm=assist,experimental_rag_fallback=assist)
   req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
   start=time.perf_counter()
   with urllib.request.urlopen(req,timeout=60) as response:x=json.load(response)
   errors=[]
   if x.get('route_category')!=cat:errors.append('category:'+str(x.get('route_category'))+' expected:'+cat)
   if i and cat=='competition_rules' and not x.get('context_resolution',{}).get('used_context'):errors.append('context_unused')
   if i and cat=='competition_rules' and x.get('sources') and not all('competition' in str(s).lower() for s in x['sources']):errors.append('source_not_rulebook')
   row=dict(session=sid,turn=i+1,payload=payload,result=x,wall_sec=time.perf_counter()-start,errors=errors,passed=not errors)
   records.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
   history.extend([dict(role='user',text=q),dict(role='assistant',text=x.get('answer',''),route_category=x.get('route_category'),route_intent=x.get('route_intent'),resolved_text=x.get('context_resolution',{}).get('resolved_question',''),universal_intent=x.get('universal_intent'))])
summary=dict(requests=len(records),passed=sum(x['passed'] for x in records),failed=[dict(session=x['session'],turn=x['turn'],errors=x['errors'],context=x['result'].get('context_resolution')) for x in records if not x['passed']],assist=assist)
with (R/(run+'_HTTP_SUMMARY.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False))
