import json,sys
from pathlib import Path
W=Path(__file__).parent;R=Path((W/'r35_report_path.txt').read_text().strip());run=sys.argv[1]
rows=[json.loads(line) for line in (R/(run+'_HTTP.jsonl')).read_text(encoding='utf-8').split('\n') if line.strip()]
grades=[]
for row in rows:
 x=row['result'];sid=row['session'];turn=row['turn'];a=x.get('answer','');errors=[]
 if sid=='user_original' and turn==1:
  for t in ('Counter-Strike 2','RoV','Tekken 8','VALORANT','ไม่ได้ยืนยัน'): 
   if t not in a:errors.append('missing:'+t)
 if (sid=='user_original' and turn>1) or ((sid in ('th_pending','en_pending','en_inherit','switch') or sid.startswith('all_games_')) and turn==2):
  if 'competition_rule_overview_source' not in x.get('mode',''):errors.append('overview_not_rendered')
  if a.count('**')<6:errors.append('fewer_than_3_sections')
  if not x.get('sources') or not all('competition_rules' in s.get('url','') for s in x['sources']):errors.append('not_rulebook_sources')
  target=x.get('context_resolution',{}).get('context_game','')
  expected_id={'VALORANT':'valorant','Counter-Strike 2':'cs2','Arena of Valor (RoV)':'rov','Tekken 8':'tekken8'}.get(target)
  if expected_id and not all('competition_rules_'+expected_id+'_' in s.get('url','') for s in x.get('sources',[])):errors.append('wrong_game_rulebook')
 if sid=='facet' and turn==2:
  for t in ('ANCIENT','ANUBIS','DUST 2','INFERNO','MIRAGE','NUKE','TRAIN'):
   if t not in a:errors.append('missing_map:'+t)
 if sid=='year' and turn==2:
  if x.get('sources'):errors.append('borrowed_different_edition')
  if '2024' not in a or 'does not verify' not in a:errors.append('missing_requested_edition_boundary')
 if sid in ('topic_change','no_history') and (sid=='no_history' or turn==2):
  if x.get('context_resolution',{}).get('used_context'):errors.append('old_task_leaked')
  if x.get('route_category')!='games':errors.append('new_detail_task_not_answered')
 grades.append(dict(session=sid,turn=turn,passed=not errors,errors=errors))
summary=dict(requests=len(grades),passed=sum(x['passed'] for x in grades),failed=[x for x in grades if not x['passed']],scope='Source-content checks for catalogue, overview sections, seven CS2 maps, edition boundary and new topic; not owner policy approval')
with (R/(run+'_CONTENT_AUDIT.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False))
