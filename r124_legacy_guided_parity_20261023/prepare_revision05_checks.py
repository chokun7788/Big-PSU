from pathlib import Path
R=Path(__file__).resolve().parent
for name in ['foundation','live','source_guards','exact_faq']:
 p=R/f'verify_{name}05.py'
 assert not p.exists()
 text=(R/f'verify_{name}04.py').read_text('utf-8-sig').replace("revision04_system","revision05_system")
 if name=='source_guards':
  text=text.replace("from app.knowledge.common.domain_flow.precision import center_location", """r=run('0f5e0fd0');checks['inventory_presence_not_collection_listing']=categories(r)==['C03'] and r.decision_artifact['execution_contract']['tasks'][0]['operation']=='detail'
r=run('da13326d');checks['ambiguous_edition_not_whole_catalog']='Overcooked' in r.answer and 'Mario Kart' not in r.answer and not r.decision_artifact['need_results'][0]['claim_packets']
from app.knowledge.common.domain_flow.precision import center_location""")
 p.write_text(text,'utf8')
for name in ['serve_live.py','start_api.py']:
 p=R/name;p.write_text(p.read_text('utf-8-sig').replace('revision04_system','revision05_system').replace('R124-revision04-live','R124-revision05-live'),'utf8')
p=R/'probe_revision05_api.py';assert not p.exists()
text=(R/'probe_latest_api.py').read_text('utf8').replace("'5d18afc2','a603ab1a'","'5d18afc2','a603ab1a','0f5e0fd0','da13326d'").replace('len(rows)==11','len(rows)==13').replace("'retained_static_queries':8","'retained_static_queries':10")
text=text.replace("'map_list_body_present':", "'inventory_detail':by['0f5e0fd0']['pipeline']['decision_artifact']['execution_contract']['tasks'][0]['operation']=='detail',\n 'edition_clarification':'Mario Kart' not in by['da13326d']['response']['answer'] and not by['da13326d']['pipeline']['decision_artifact']['need_results'][0]['claim_packets'],\n 'map_list_body_present':")
p.write_text(text,'utf8')
