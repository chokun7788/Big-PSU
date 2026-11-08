import json
from pathlib import Path
root=Path(__file__).parent;r=Path((root/'r30_report_path.txt').read_text().strip())
cases=[]
for title in ['The Last of Us Part I / Part II','Horizon Call of the Mountain','The Legend of Zelda: Breath of The Wild','It Takes Two']:
    cases.append({'id':'MIX-TH-'+str(len(cases)),'question':title+' ราคาเท่าไหร่','locale':'auto','group':'ingress_locale','must_contain':[],'must_not_contain':['wrong keyboard','English information:'],'outcome':'','required_source':'','not_category':''})
for q in ['Can I play เกม at the studio?','What are the ปุ่ม in The Last of Us Part II?','Is The Last of Us Part II available?','How much is Horizon Call of the Mountain?']:
    cases.append({'id':'MIX-EN-'+str(len(cases)),'question':q,'locale':'auto','group':'english_mixed_locale','must_contain':[],'must_not_contain':[],'outcome':'','required_source':'','not_category':''})
with (r/'mixed_title_fixture_G3.json').open('x',encoding='utf-8') as f:json.dump({'cases':cases,'scope':'actual input language and protected source names; no full answer oracle for under-specified or live questions'},f,ensure_ascii=False,indent=2)
s=(root/'r30_http_G.py').read_text(encoding='utf-8').replace('2026.10.02-full-improvement-r30-G2','2026.10.02-full-improvement-r30-G3').replace("'runtime':'r30-G2'","'runtime':'r30-G3'")
s=s.replace("('competition_G43',json.loads((r/'focused_fixture_G_new_v2.json').read_text(encoding='utf-8'))['cases'])]","('competition_G43',json.loads((r/'focused_fixture_G_new_v2.json').read_text(encoding='utf-8'))['cases']),('mixed_title8',json.loads((r/'mixed_title_fixture_G3.json').read_text(encoding='utf-8'))['cases'])]")
s=s.replace("('focused79','competition_G43')", "('focused79','competition_G43','mixed_title8')")
s=s.replace("if c['outcome'] and status!=c['outcome']:", "if c['outcome'] and c.get('group')!='true_wrong_layout' and status!=c['outcome']:")
s=s.replace("if c.get('group')=='true_wrong_layout' and 'keyboard_layout_mismatch' not in raw.get('input_quality',{}).get('flags',[]):errors.append('missed_true_layout')", """if c.get('group')=='true_wrong_layout' and (raw.get('mode')!='input_guard_layout_retype' or 'keyboard_layout_mismatch' not in raw.get('input_quality',{}).get('flags',[])):errors.append('missed_true_layout')
                    if c.get('group')=='english_mixed_locale' and raw.get('language',{}).get('effective')!='en':errors.append('incorrect_thai_locale')""")
with (root/'r30_http_G3.py').open('x',encoding='utf-8') as f:f.write(s)
s=(root/'r30_build_final_analysis.py').read_text(encoding='utf-8').replace('FINAL_G2_','FINAL_G3_').replace('final_G2_inventory.json','final_G3_inventory.json').replace('final_G2_all_results.jsonl','final_G3_all_results.jsonl')
with (root/'r30_build_G3_analysis.py').open('x',encoding='utf-8') as f:f.write(s)
print(json.dumps({'new_mixed_cases':len(cases)}))
