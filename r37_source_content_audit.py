"""Audit answer clauses against unchanged source/localization text, offline."""
import json,re,sys
from pathlib import Path
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def compact(text):return re.sub(r'[\s*•]','',str(text)).casefold()
thai={};english={}
for file in (P/'data/curated').glob('*.jsonl'):
 for line in file.read_text(encoding='utf-8-sig').splitlines():
  try:row=json.loads(line)
  except json.JSONDecodeError:continue
  if row.get('category')=='competition_rules':thai.setdefault(row.get('id'),[]).append(str(row.get('text') or ''))
release=(P/'data/locales/en/CURRENT').read_text(encoding='utf-8-sig').strip()
for file in (P/'data/locales/en/releases'/release).glob('*.jsonl'):
 for line in file.read_text(encoding='utf-8-sig').splitlines():
  try:row=json.loads(line)
  except json.JSONDecodeError:continue
  if row.get('field')=='text':english.setdefault(row.get('content_id'),[]).append(str(row.get('text') or ''))
grades=[]
for run in sys.argv[1:]:
 for line in (R/(run+'.jsonl')).read_text(encoding='utf-8').splitlines():
  row=json.loads(line);x=row['result'];a=x.get('answer','');errors=[];clauses=[]
  overview=next((t for t in x.get('trace',[]) if t.get('stage')=='competition_overview'),None)
  if not overview or not overview.get('metadata',{}).get('section_ids'):continue
  ids=overview['metadata']['section_ids'];corpus=english if row['payload']['locale']=='en' else thai
  texts=[compact(t) for ident in ids for t in corpus.get(ident,[])]
  for line in a.splitlines():
   if not re.match(r'^\s*•\s+',line):continue
   clause=re.sub(r'^\s*•\s+','',line);clauses.append(clause)
   if row['payload']['locale']=='th' and not re.search(r'[\u0e00-\u0e7f]',clause):errors.append('parallel_english_clause_in_thai_summary:'+clause)
   if not any(compact(clause) in t for t in texts):errors.append('clause_not_literal_in_selected_source:'+clause)
   if re.fullmatch(r'(?:PSU|BLUEKET).*(?:Tournament|Division)',clause,re.I):errors.append('event_title_presented_as_rule')
  block=re.search(r'\*\*[^\n]*Player Emergency Pause[^\n]*\*\*(.*?)(?=\n\*\*|\Z)',a,re.S)
  if block and re.search(r'Play Through Bug|Major Bug|Game Breaking Bug',block.group(1)):errors.append('bug_rules_labeled_as_emergency_pause')
  if len(clauses)<2:errors.append('fewer_than_two_actual_clauses')
  grades.append({'run':run,'session':row['session'],'turn':row['turn'],'clauses':len(clauses),'passed':not errors,'errors':errors})
summary={'answers_audited':len(grades),'clauses_audited':sum(x['clauses'] for x in grades),'passed':sum(x['passed'] for x in grades),'failed':[x for x in grades if not x['passed']], 'scope':'Literal coverage in selected source rows and existing English text, event-title exclusion, emergency-pause label; not complete semantic expert approval'}
out=R/('SOURCE_CONTENT_'+sys.argv[1]+'.json')
with out.open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False))
