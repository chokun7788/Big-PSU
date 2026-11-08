import hashlib,json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));assert c['url']=='http://127.0.0.1:12422'
def get(path):
 with urllib.request.urlopen(c['url']+path,timeout=4) as f:return json.load(f)
for _ in range(60):
 try:h=get('/health');break
 except OSError:time.sleep(.5)
else:raise RuntimeError('R128 preview did not start')
run=json.loads((R/'FINAL_RUN.json').read_text('utf8'));freeze=json.loads((Path(run['api']['output'])/'FINAL_SOURCE_FREEZE.json').read_text('utf8'))
checks={'runtime_R128':h['runtime']['version']=='R128','build_R128':h['common_loaded_build']['build_id']=='common-r128-complete-common-flow','llm_enabled':h['runtime']['local_llm']['enabled'],'live_wordpress_enabled':h['runtime']['booking']['enabled'] and h['runtime']['booking']['fetch_mode']=='wordpress','draft_preview_explicit':h['runtime']['knowledge_draft_preview'],'same_source_as_tested':all(hashlib.sha256((R/'system'/p).read_bytes()).hexdigest()==sha for p,sha in freeze.items())}
with urllib.request.urlopen(c['url']+'/',timeout=4) as f:html=f.read().decode()
checks['R128_page_served']='Common Flow R128' in html
rows=[]
for q in ['วันที่ 26 ตุลาเปิดไหม','God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง']:
 req=urllib.request.Request(c['url']+'/api/chat',json.dumps({'question':q,'locale':'th','debug':True,'experimental_rag_fallback':True,'client_session_id':'r128-activation-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex},ensure_ascii=False).encode(),{'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=60) as f:response=json.load(f)
 rows.append({'question':q,'response':response})
checks['date_on_activated_service']='26 ตุลาคม' in rows[0]['response']['answer'] and '13:00' in rows[0]['response']['answer']
checks['controls_table_on_activated_service']='| ปุ่ม |' in rows[1]['response']['answer']
checks['private_sources_keep_citation_mapping']=any('[S1' in source['id'] for source in rows[1]['response'].get('sources',[]))
checks['private_sources_do_not_expose_paths']=not any('C:\\' in source['id'] or 'owner-form://' in source['id'] for source in rows[1]['response'].get('sources',[]))
(R/'ACTIVATION_RESPONSES.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
result={'all_passed':all(checks.values()),'checks':checks,'url':c['url'],'pid':c['pid'],'health':h,'candidate_only':True,'production_R78_replaced':False,'output':c['output']}
(R/'ACTIVATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'all_passed':result['all_passed'],'checks':checks,'url':c['url'],'pid':c['pid']},ensure_ascii=False,indent=2));assert result['all_passed']
