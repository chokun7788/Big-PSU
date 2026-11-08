from pathlib import Path
HERE=Path(__file__).parent
s=(HERE/'final_package_check.py').read_text(encoding='utf-8').replace('PORT = 8096','PORT = 8093')
extra='''
session='release-'+str(uuid.uuid4())
r=ask('Service prices for external users',session,'en')
r=ask("I'd like the cockpit rate instead",session,'en',r.get('request_id',''))
check('rephrased_price_retains_external',set(r.get('coverage',{}).get('returned_ids',[]))=={'cockpit:general_student','cockpit:general_adult'})
session='release-'+str(uuid.uuid4())
r=ask('Please show every section of the CS2 tournament rulebook',session,'en')
check('every_section_full_rules',(r.get('rule_coverage') or {}).get('detail_level')=='full_sections' and bool((r.get('rule_coverage') or {}).get('returned_ids')))
'''
s=s.replace("stamp=time.strftime('%H%M%S')",extra+"\nstamp=time.strftime('%H%M%S')")
s=s.replace("summary=dict(port=PORT", "summary=dict(runtime_version='2026.10.05-conversation-r38.4',port=PORT")
with (HERE/'final_package_check_r38_4.py').open('x',encoding='utf-8') as f:f.write(s)
