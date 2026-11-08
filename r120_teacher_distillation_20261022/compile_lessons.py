"""Transfer teacher task behavior only; omit teacher business answer values."""
import collections,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parent
load=lambda n:json.loads((R/n).read_text('utf8'))
assert load('teacher01/COMPLETE.json')['complete']
rows=list(map(json.loads,(R/'teacher01/RESULTS.jsonl').open(encoding='utf8')));examples=[];decisions=[];techniques=collections.Counter()
domains={'service_fee':('service_fee','C06','price_calculate','amount'),'reservation':('reservation','C08','detail','owner_policy'),'rules':('rules','C10','detail','owner_policy'),'penalty':('rules','C10','detail','owner_policy'),'competition_rules':('competition_rules','C13','rule_lookup','rule_clause'),'equipment':('equipment','C03','detail','name'),'schedule':('schedule','C11','detail','open_periods'),'overview':('contact','C01','detail','operator'),'contact':('contact','C01','detail','value'),'games':('games','C04','detail','summary'),'game_controls':('game_controls','C05','control','input_bindings')}
def slots(q):
 patterns={'duration':r'(?<!\w)(?:(?:one and a half|half an?|one|two|three|four|five|six|a|an|\d+(?:\.\d+)?)\s*(?:hours?|hrs?|minutes?))\b|(?:\d+(?:\.\d+)?|หนึ่ง|สอง|สาม|ครึ่ง)\s*(?:ชั่วโมง|นาที)',
  'persons':r'\b\d+\s*(?:people|persons?|players?)\b|\d+\s*คน','sessions':r'\b\d+\s*sessions?\b|\d+\s*รอบ',
  'date':r'20\d\d[-/]\d\d[-/]\d\d','negation':r'\bnot\b|\bwithout\b|ไม่ใช่|ยกเว้น'}
 return [{'slot':k,'quote':m[0],'source_record_id':''} for k,p in patterns.items() for m in re.finditer(p,q,re.I)]
for row in rows:
 a=row.get('result') or {};route=(a.get('route') or {}).get('category');mode=a.get('mode','');q=row['question'];d=domains.get(route)
 decision={'key':row['key'],'teacher_route':route,'teacher_mode':mode,'accepted':False}
 if row.get('error') or not d or not (a.get('validation') or {}).get('ok') or a.get('confidence',0)<.85 or 'no_answer' in mode or 'unavailable' in mode:
  decision['reason']='teacher_not_confident_source_task';decisions.append(decision);continue
 domain,cat,op,facet=d;ql=q.casefold()
 if 'control' in mode:domain,cat,op,facet='game_controls','C05',('list' if re.search(r'ทั้งหมด|\ball\b|\bbuttons\b',q,re.I) else 'control'),'input_bindings'
 if 'live_booking' in mode:domain,cat,op,facet='live','C12','availability','live_status'
 if cat=='C03':
  if re.search(r'โซนไหน|where|which zone',ql):facet='location'
  elif re.search(r'กี่|how many|quantity',ql):facet='quantity'
  elif re.search(r'gpu|cpu|ram|สเปก|spec',ql):facet='specifications'
  else:facet='usage' if re.search(r'ใช้ทำ|how|used for',ql) else 'name'
 if cat=='C04':
  if re.search(r'โซนไหน|which zone|which studio zone',ql):facet='zone'
  elif re.search(r'วิธีเล่น|เล่นยังไง|how.*play',ql):facet='how_to_play'
  elif re.search(r'แนว|genre|kind of game',ql):facet='genre'
  elif re.search(r'รายชื่อ|มีเกมอะไร|เกมไหนบ้าง|what games|list.*games',ql):op,facet='list','game_catalog'
  elif 'availability' in mode:facet='studio_services'
 if cat=='C11' and re.search(r'maintenance|บำรุง',ql):facet='maintenance_periods'
 if cat=='C01':
  if re.search(r'ที่ไหน|อยู่ที่|where|address|location',ql):facet='address'
  elif re.search(r'แผนที่|map',ql):facet='map_url'
  elif re.search(r'ชั้น|floor',ql):facet='floor'
  elif re.search(r'อาคาร|ตึก|building',ql):facet='building'
  elif re.search(r'ติดต่อ|contact|phone|facebook|เพจ|เบอร์',ql):facet='value'
 plan={'tasks':[{'quote':q,'domain':domain,'operation':op,'facet':facet,'target':'','constraints':slots(q),'ambiguous':False}]}
 stages=[{'stage':t.get('stage'),'decision':t.get('decision')} for t in a.get('trace',[]) if isinstance(t,dict)]
 technique='typed_financial_slots' if cat=='C06' else 'event_scoped_clauses' if cat=='C13' else 'exact_control_binding' if cat=='C05' else 'recorded_calendar' if cat=='C11' else 'source_policy_or_record_lookup'
 techniques[technique]+=1
 examples.append({'id':row['key'],'question':q,'plan':plan,'teacher_route':route,'teacher_mode':mode,'technique':technique,'observable_stages':stages,'business_answer_included':False})
 decision.update(accepted=True,reason='task_behavior_only_business_answer_excluded',domain=domain);decisions.append(decision)
result={'version':1,'method':'retrieved demonstrations and observable behavior transfer; no parameter training','weights_changed':False,'business_answers_included':False,'examples':examples,'response_policy':['lead with the requested fact or missing slot','retain source conditions and stated duration/audience','do not answer a price question with a game catalogue','preserve game/event context from the whole request','for broad rule topics cover the related source sections or mark partial','always read current native facts; never reuse old numeric answers']}
(R/'TEACHER_LESSONS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
(R/'TEACHER_REVIEW.json').write_text(json.dumps({'teacher_requests':len(rows),'accepted_task_examples':len(examples),'quarantined':len(rows)-len(examples),'decisions':decisions,'observable_techniques':dict(techniques),'manual_semantic_approval_claimed':False},ensure_ascii=False,indent=2),'utf8')
assert len(examples)>=32
print(json.dumps({'examples':len(examples),'quarantined':len(rows)-len(examples),'techniques':dict(techniques)}))
