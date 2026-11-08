import hashlib,json
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');ID='competition_rules_rov_blueket_2025_men_s08_c01'
assert not (OUT/'EDIT4_DONE').exists()
source=next(json.loads(t) for t in (ROOT/'data/curated/curated_competition_rules.jsonl').read_text(encoding='utf-8').splitlines() if json.loads(t).get('id')==ID)
sha=hashlib.sha256(source['text'].encode()).hexdigest()
translation='''6. Offences and penalties — translation of the readable source fragment; incomplete source
6.1. Competitors must not commit any of the following acts.
6.1.1. Using impolite speech or gestures, or making disparaging remarks about others, is prohibited.
6.1.1.1. Penalty: immediate forfeiture of the game in which the offence is found.
6.1.2. Submitting false or distorted competition results is prohibited.
6.1.2.1. Penalty: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from the competition.
6.1.3. Teams must not allow anyone who is absent from their registered team roster to compete. If a competitor does not match the registration, record photographic evidence and stop the match immediately. If the game has already been played to completion, both teams are deemed to have consented to the match; staff will not accept objections.
6.1.3.1. Penalty: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from the competition.
6.1.4. Competitors must not allow another person to play in their place during competition.
6.1.4.1. Penalty: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from the competition.
6.1.5. The readable text prohibits competitors from consuming, trading, or carrying out activities involving drugs, cigarettes, weapons, and other legally prohibited items. The source wording at the end of this clause is unclear.
6.1.5.1. Readable penalty fragment: immediate forfeiture of the game in which the offence is found and immediate disqualification of the offending team from … [the source stops here; the missing ending and application of this clause require organizer confirmation].'''
module='''"""Source-hash-bound rendering of an incomplete rulebook fragment.

Agent translation is labelled as such; this does not publish an approved
localization, complete the policy, or modify the owner's source documents.
"""
import hashlib
ID = %r
SOURCE_SHA256 = %r
ENGLISH_FRAGMENT = %r

def is_recorded_fragment(row):
    return row.get('id') == ID and hashlib.sha256(str(row.get('text','')).encode()).hexdigest() == SOURCE_SHA256

def fragment_translation(row):
    return ENGLISH_FRAGMENT if is_recorded_fragment(row) else None
'''%(ID,sha,translation)
p=ROOT/'app/pipeline/rulebook_source_fragments.py';assert not p.exists();p.write_text(module,encoding='utf-8')
p=ROOT/'app/pipeline/conversation_rules.py';t=p.read_text(encoding='utf-8')
t=t.replace('from app.knowledge.localization import approved_localization','from app.knowledge.localization import approved_localization\nfrom app.pipeline.rulebook_source_fragments import fragment_translation, is_recorded_fragment',1)
t=t.replace("approved_localization(r,'text')) for r in meaningful]", "approved_localization(r,'text') or fragment_translation(r)) for r in meaningful]",1)
t=t.replace("approved_localization(row,'text') or (original if", "approved_localization(row,'text') or fragment_translation(row) or (original if",1)
t=t.replace('    if rows:\n        lines.append(','''    source_gap_ids = [r['id'] for r in rows if is_recorded_fragment(r)]
    if source_gap_ids:
        lines.append('The recorded RoV source is incomplete at clauses 6.1.5 / 6.1.5.1. The fragment translation is prepared by the agent, not organizer approval; no missing penalty ending is inferred.' if english else 'ต้นฉบับ RoV ข้อ 6.1.5 / 6.1.5.1 มีข้อความกำกวมและถูกตัดท้าย ยังต้องให้ผู้จัดยืนยันข้อความและบทลงโทษส่วนที่ขาดครับ')
    if rows:
        lines.append(''',1)
t=t.replace("'answered_partial' if remaining or locale_missing else", "'answered_partial' if remaining or locale_missing or source_gap_ids else",1)
t=t.replace("'source_changed':changed,", "'source_gap_ids':source_gap_ids, 'source_policy_complete':not bool(source_gap_ids), 'fragment_translation_basis':'agent_translation_readable_incomplete_source' if source_gap_ids and english else None,\n                'source_changed':changed,",1)
t=t.replace("warnings=('english_localization_incomplete',) if locale_missing else ()", "warnings=tuple((['english_localization_incomplete'] if locale_missing else [])+(['rulebook_source_incomplete'] if source_gap_ids else []))",1)
p.write_text(t,encoding='utf-8')
(OUT/'ROV_FRAGMENT_TRANSLATION_REVIEW.json').write_text(json.dumps(dict(source_id=ID,source_sha256=sha,source_text=source['text'],translation=translation,status='agent_translation_readable_fragment_not_organizer_approval',constraints=['forfeit game versus disqualify team retained','registered roster condition retained','finished-match consent exception retained','incomplete final penalty not completed','ambiguous 6.1.5 end disclosed','hash mismatch disables fallback']),ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'EDIT4_DONE').write_text('labelled RoV source fragment translation; original source/localization approvals intact',encoding='utf-8');print('RoV readable fragment translated; missing policy explicitly retained')
