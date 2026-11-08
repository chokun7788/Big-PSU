from pathlib import Path
import json
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
R=Path(Path(__file__).with_name('r34_report_path.txt').read_text().strip())
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert s.count(old)==1,(rel,s.count(old));p.write_text(s.replace(old,new),encoding='utf-8')
module='''"""Explicit source task signals shared by answers and their validators."""
import re
from app.core.normalization import SERVICE_ALIASES, contains_alias

def fee_comparison_query(query: str) -> bool:
    services = [key for key, aliases in SERVICE_ALIASES.items()
                if contains_alias(query, aliases, fuzzy=False)[0]]
    comparison = re.search(r'แพงกว่า|ถูกกว่า|(?:เทียบ|ต่างกัน).*ราคา|ราคา.*(?:เทียบ|ต่างกัน)|\\b(?:more expensive|cheaper)\\b|\\bcompare\\b.*\\b(?:prices?|fees?)\\b|\\b(?:prices?|fees?)\\b.*\\bcompare\\b', query, re.I)
    return len(services) >= 2 and bool(comparison)
'''
p=P/'app/pipeline/source_task_signals.py';assert not p.exists();p.write_text(module,encoding='utf-8')
edit('app/pipeline/question_frame.py','    # A zone/genre catalogue question asks for multiple games, even when the', '''    from app.pipeline.source_task_signals import fee_comparison_query
    if fee_comparison_query(question):
        return "price_lookup", "service_fee", 0.98
    # A zone/genre catalogue question asks for multiple games, even when the''')
edit('app/pipeline/closed_query_improvements.py',"    if not re.search(r'แพงกว่า|ถูกกว่า|\\b(?:more expensive|cheaper)\\b',query,re.I):return None", "    from app.pipeline.source_task_signals import fee_comparison_query\n    if not fee_comparison_query(query):return None")
edit('app/core/task_frame_recovery.py',"targets.extend(('which','expensive'))", "targets.extend(('which','expensive','cheaper'))")
edit('app/core/task_frame_recovery.py',"('อันไหนแพงกว่า',2)","('อันไหนแพงกว่า',2),('อันไหนถูกกว่า',1)")
# Separate source review: never modify the baseline or an owner/Gold fixture.
fixture=json.loads((R/'R34_FOUR_GROUP_SOURCE_FIXTURE.json').read_text(encoding='utf-8'))
for c in fixture['cases']:
 if c['group']=='price':c['required']=[['375'] if g==['380'] else g for g in c['required']]
 if c['group']=='speech':c['source']+=['Reservation','rule_en_general_studio_rules']
fixture['oracle_review']='VR 60-minute General Student is 375 in SERVICE_FEES and curated_facts_service_fee_2026_aliases, not 380. General Reservation and English studio rules also contain the noise/language prohibition. Content gates remain required; source id alone cannot pass.'
with (R/'R34_SOURCE_REVIEWED_FIXTURE.json').open('x',encoding='utf-8') as f:json.dump(fixture,f,ensure_ascii=False,indent=2)
with (R/'ORACLE_ADJUDICATION_A.md').open('x',encoding='utf-8') as f:f.write('Source review: initial assistant fixture incorrectly assumed VR student 60 minutes = 380. Original source table explicitly says 375. No production price/policy was changed. Initial results retained. Noise/language content also appears in Reservation and rule_en_general_studio_rules; those IDs are accepted only together with required prohibition content. These are assistant source checks, not owner approval.\n')
print('Round A edits and separate source-reviewed oracle saved')
