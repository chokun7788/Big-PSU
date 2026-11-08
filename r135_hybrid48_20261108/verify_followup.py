"""Source assertions for omissions found while R132 was already frozen."""
import json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.rule_semantics import substantive
e=Engine.from_snapshot(snapshot());checks={};rows=[]
cases=[
 ('settings_macro','กติกา CS2 ปรับ Brightness Resolution Crosshair ที่ไหน แล้วใช้สคริปต์หรือมาโครได้ไหม',{'competition_competition_rules_cs2_psu_phuket_2026_section_045','competition_competition_rules_cs2_psu_phuket_2026_section_046'}),
 ('thai_food','กติกา CS2 ในพื้นที่แข่งอนุญาตอาหารเครื่องดื่มอะไรบ้าง',{'competition_competition_rules_cs2_psu_phuket_2026_section_053'}),
 ('prep_food','Under CS2 tournament rules, how many players may prepare and what food or drinks are permitted?',{'competition_competition_rules_cs2_psu_phuket_2026_section_050','competition_competition_rules_cs2_psu_phuket_2026_section_053'}),
 ('team_size','How many players must a Counter-Strike 2 team have?',{'competition_competition_rules_cs2_psu_phuket_2026_section_018'}),
 ('offsite','What is the studio policy for rent laptop home',set()),
]
def known_clause_delivery(result):
 if result['status']=='answer':return True
 if result['status']!='partial' or not result['claims']:return False
 for need in result['needs']:
  proof=need['plan']['metadata'].get('rule_dependency_proof',{});ledger=need.get('execution_contract',{})
  if not proof or proof['errors'] or proof['missing_fact_ids'] or ledger.get('fatal'):return False
  if not proof['limits'] or any(x['reason'] not in {'dependency_set_unconfirmed','clause_completeness_unconfirmed'} for x in proof['limits']):return False
  # The retained owner fields really are unknown. Do not reclassify source
  # uncertainty as a content regression or change owner fields to make a pass.
  for limit in proof['limits']:
   fact=e.index.byid[limit['fact_id']];record=e.index.records[fact['record_id']];key='depends_on_ids' if limit['reason']=='dependency_set_unconfirmed' else 'completeness'
   if record['fields'].get(key,{}).get('status')!='unknown':return False
 return 'ข้อกติกาที่อ้างถึง' in result['answer'] or 'linked rule clauses' in result['answer']
for name,q,expected in cases:
 result=e.answer(q,'auto',allow_llm=False,understanding=propose(e.index,q));ids={c['record_id'] for c in result['claims']};checks[name]=(expected<=ids if name=='team_size' else ids==expected) and (result['status']=='missing_source' if name=='offsite' else known_clause_delivery(result));rows.append({'name':name,'question':q,'result':result,'passed':checks[name]})
 if name=='team_size':checks['team_roster_not_preparation_capacity']='competition_competition_rules_cs2_psu_phuket_2026_section_050' not in ids
checks['heading_alone_still_rejected']=not substantive('2. Game Settings',['2. Game Settings'])
checks['thai_permission_clause_retained']=substantive('อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น')
checks['team_quantity_clause_retained']=substantive('Each team consists of 5 players.')
out=R/('followup_verification_'+str(time.time_ns()));out.mkdir();r={'all_passed':all(checks.values()),'checks':checks,'rows':rows,'inferences':0,'source_changes':0,'semantic_accuracy':None};(out/'RESULT.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),'utf8');(R/'FOLLOWUP_VERIFICATION_LATEST.json').write_text(json.dumps({'output':str(out),'all_passed':r['all_passed'],'checks':len(checks)},indent=2),'utf8');print(json.dumps({'checks':checks,'answers':[{ 'name':x['name'],'answer':x['result']['answer']} for x in rows]},ensure_ascii=False));assert r['all_passed']
