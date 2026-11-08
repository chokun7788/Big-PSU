"""Review only legacy source-presence failures; never modify Gold/raw outcomes."""
import hashlib, json, re, sys
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(project))
from app.knowledge.localization import approved_localization
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
run=sys.argv[1]
rows=[json.loads(line) for line in (report/(run+'_details.jsonl')).read_text(encoding='utf-8').splitlines() if line.strip()]
source={r['id']:r for r in [json.loads(line) for line in (project/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]}
def norm(text):
    return re.sub(r'\s+',' ',text.casefold()).strip()
reviews=[]
for row in rows:
    if row['passed']:continue
    matches=[]
    if row['failures']==['answer_without_substantive_source_content']:
        for source_id in row['source_ids']:
            origin=source_id.removeprefix('canonical::')
            if origin not in source:continue
            translated=approved_localization(source[origin],'text') or ''
            # Separate complete exported bullets. Exact full-clause inclusion
            # can prove short facts; seven-word windows cannot prove them.
            for clause in re.split(r'\n|\s+\*\s+',translated):
                clause=clause.strip().lstrip('*-•· ').strip()
                substantive=bool(re.search(r'\d|\b(?:must|may|allowed|used|warning|rollback|loss|forfeit)\b',clause,re.I))
                if substantive and len(clause)>=12 and norm(clause) in norm(row['answer']):
                    item={'source_id':origin,'literal_complete_clause':clause,'source_sha256':hashlib.sha256(source[origin]['text'].encode()).hexdigest()}
                    if item not in matches:matches.append(item)
    reason=('short atomic equipment statement hidden inside a flattened source bullet list' if row.get('game')=='tekken8' else 'literal penalty clauses excluded by the legacy modal/numeric word filter') if matches else 'unresolved: requires further semantic review'
    reviews.append({'id':row['id'],'question':row['question'],'original_failures':row['failures'],'source_presence_confirmed':bool(matches),'reason':reason,'matches':matches})
result={'run':run,'total':len(rows),'legacy_passed':sum(row['passed'] for row in rows),'legacy_failed':len(reviews),'source_presence_resolved':sum(row['source_presence_confirmed'] for row in reviews),'unresolved_ids':[row['id'] for row in reviews if not row['source_presence_confirmed']],'source_presence_passed_after_review':sum(row['passed'] for row in rows)+sum(row['source_presence_confirmed'] for row in reviews),'review_scope':'source-presence check only; not all proposition completeness, not owner approval; original Gold and raw results preserved','reviews':reviews}
with (report/(run+'_source_presence_review.json')).open('x',encoding='utf-8') as handle:json.dump(result,handle,ensure_ascii=False,indent=2)
print(json.dumps({key:value for key,value in result.items() if key!='reviews'},ensure_ascii=False),flush=True)
