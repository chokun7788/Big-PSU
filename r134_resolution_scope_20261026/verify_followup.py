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
for name,q,expected in cases:
 result=e.answer(q,'auto',allow_llm=False,understanding=propose(e.index,q));ids={c['record_id'] for c in result['claims']};checks[name]=(expected<=ids if name=='team_size' else ids==expected) and (result['status']=='missing_source' if name=='offsite' else result['status']=='answer');rows.append({'name':name,'question':q,'result':result,'passed':checks[name]})
 if name=='team_size':checks['team_roster_not_preparation_capacity']='competition_competition_rules_cs2_psu_phuket_2026_section_050' not in ids
checks['heading_alone_still_rejected']=not substantive('2. Game Settings',['2. Game Settings'])
checks['thai_permission_clause_retained']=substantive('อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น')
checks['team_quantity_clause_retained']=substantive('Each team consists of 5 players.')
out=R/('followup_verification_'+str(time.time_ns()));out.mkdir();r={'all_passed':all(checks.values()),'checks':checks,'rows':rows,'inferences':0,'source_changes':0,'semantic_accuracy':None};(out/'RESULT.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),'utf8');(R/'FOLLOWUP_VERIFICATION_LATEST.json').write_text(json.dumps({'output':str(out),'all_passed':r['all_passed'],'checks':len(checks)},indent=2),'utf8');print(json.dumps({'checks':checks,'answers':[{ 'name':x['name'],'answer':x['result']['answer']} for x in rows]},ensure_ascii=False));assert r['all_passed']
