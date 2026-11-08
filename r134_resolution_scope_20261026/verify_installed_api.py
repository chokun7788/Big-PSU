"""Actual user launcher/runtime acceptance; original questions and source cases."""
import json,time,uuid,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r132_flow_repairs_20261025';D=R.parent/'r131_diagnostic_review_20261025';out=R/('installed_acceptance_'+str(time.time_ns()));out.mkdir();rows=[]
cases=json.loads((D/'CONSOLIDATED_SOURCE_REVIEW.json').read_text('utf8'))['cases'];prefixes=['f6a75fef','934b6162','9749c57f','cc40820b','0c25d981','06563f1a','b9fa6734','7e3ed641','db84ae34','4dc69c73','41bef879','35997d9f','371be50e','bf6817cf','4a52eaf2','864bd598']
expected={
 'f6a75fef':{'equipment_gaming_pc'},'934b6162':{'r114_q037_owner_policy'},'9749c57f':{'migrated_faq_rule_damage_responsibility'},'cc40820b':{'competition_competition_rules_tekken8_psu_esports_section_002'},'0c25d981':{'competition_competition_rules_cs2_psu_phuket_2026_section_037','competition_competition_rules_cs2_psu_phuket_2026_section_038'},'06563f1a':{'competition_competition_rules_cs2_psu_phuket_2026_section_046'},'7e3ed641':{'availability_cockpit_01_02'},'41bef879':{'competition_competition_rules_cs2_psu_phuket_2026_section_045','competition_competition_rules_cs2_psu_phuket_2026_section_046'},'35997d9f':{'competition_competition_rules_cs2_psu_phuket_2026_section_053'},'371be50e':{'competition_competition_rules_cs2_psu_phuket_2026_section_050','competition_competition_rules_cs2_psu_phuket_2026_section_053'},'bf6817cf':{'competition_competition_rules_cs2_psu_phuket_2026_section_018'},'building_floor':{'center_psu_phuket'},'guardian':{'r114_q032_owner_policy'},
}
questions=[(p,next(c['question'] for c in cases if c['key'].startswith(p))) for p in prefixes]+[('building_floor','อยู่ตึกอะไร ชั้นไหน?'),('guardian','เด็กเข้าใช้บริการได้ไหม ต้องมีผู้ปกครองหรือเปล่า?'),('documents','What ID does an external visitor need to use the studio?')]
with (out/'RESULTS.jsonl').open('x',encoding='utf8') as stream:
 for name,q in questions:
  t=time.perf_counter();req=urllib.request.Request('http://127.0.0.1:8115/api/chat',json.dumps({'question':q,'locale':'auto','debug':True,'experimental_rag_fallback':True,'client_session_id':'r133-installed-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex},ensure_ascii=False).encode(),{'Content-Type':'application/json'})
  try:
   with urllib.request.urlopen(req,timeout=195) as f:a=json.load(f)
   art=a.get('decision_artifact') or {};ids=set((art.get('query_plan') or {}).get('record_ids') or []);passed=a.get('validation_ok') is True and not a.get('timed_out') and expected.get(name,set())<=ids
   if name in ['db84ae34','4a52eaf2','864bd598']:passed=passed and not ids
   if name=='b9fa6734':passed=passed and 'controls_ps5_tekken_8' in ids and 'amount' in (art.get('query_plan') or {}).get('requested_fields',[])
   if name=='documents':passed=passed and 'r114_q037_owner_policy' not in ids and any(t.get('canonical_operation')=='policy.checkin_documents' for t in (art.get('understanding') or {}).get('tasks',[]))
   row={'name':name,'question':q,'response':a,'passed':passed,'source_ids':sorted(ids),'elapsed_sec':time.perf_counter()-t}
  except Exception as exc:row={'name':name,'question':q,'passed':False,'error':repr(exc),'elapsed_sec':time.perf_counter()-t}
  rows.append(row);stream.write(json.dumps(row,ensure_ascii=False)+'\n');stream.flush();print(json.dumps({k:row.get(k) for k in ['name','passed','source_ids','error','elapsed_sec']},ensure_ascii=False),flush=True)
summary={'all_passed':all(x['passed'] for x in rows),'cases':len(rows),'failed':[x['name'] for x in rows if not x['passed']],'output':str(out),'semantic_accuracy':None,'known_case_source_expectations_only':True};(out/'COMPLETE.json').write_text(json.dumps(summary,indent=2),'utf8');(R/'INSTALLED_ACCEPTANCE_LATEST.json').write_text(json.dumps(summary,indent=2),'utf8');assert summary['all_passed']
