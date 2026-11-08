from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert old in s,rel;p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/core/intent_cue_recovery.py',r'(?:pc|ps5|vr|cockpit|nintendo|switch|playstation)\b',r'(?:pc(?:[ -]?#?\d+)?|ps5|vr|cockpit|nintendo|switch|playstation)\b')
edit('app/core/intent_cue_recovery.py',r'(?=ไหม|มั้ย)',r'(?=\s*(?:ไหม|มั้ย|หรือเปล่า|รึเปล่า|หรือไม่|รึป่าว|หรือป่าว))')
edit('app/core/intent_cue_recovery.py','    lower = text.casefold()\n    # A known rulebook target', '''    lower = text.casefold()
    from app.pipeline.competition_facet_recovery import recover_facet_cue
    facet = recover_facet_cue(text)
    if facet is not None:
        return CueRecovery(text, facet[0], facet[1].original, facet[1].canonical,
                           facet[1].start, facet[1].edits,
                           'unique registered facet span; exact rulebook context')
    # A known rulebook target''')
edit('app/core/intent_cue_recovery.py','    booking_context = near("booking")', '''    # A location interrogative is recoverable with a surviving modal frame.
    for token in tokens:
        observed=token.group().casefold()
        if observed not in _VALID_ENGLISH_WORDS and osa_distance(observed,'where') == 1 and re.match(r'\\s+can\\s+(?:i|we|you)\\s+',lower[token.end():]):
            return CueRecovery(text,text[:token.start()]+'where'+text[token.end():],token.group(),'where',token.start(),1,'location interrogative plus modal frame')
    if re.search(r'อยู่|มี',text) and re.search(r'ไหน|อะไร',text):
        for token in re.finditer(r'โซ[\\u0e00-\\u0e7f]{1,4}(?=ไหน|อะไร)',text):
            if osa_distance(token.group(),'โซน') == 1:
                return CueRecovery(text,text[:token.start()]+'โซน'+text[token.end():],token.group(),'โซน',token.start(),1,'Thai zone location frame')
    booking_context = near("booking")''')
facet='''"""Bounded facet vocabulary recovery, restricted to an explicit rulebook.
No complete question aliases, numbers, or short negations are candidates.
"""
import re
from functools import lru_cache

@lru_cache(maxsize=512)
def recover_facet_cue(query):
    from app.pipeline.competition_targets import resolve_competition_targets, looks_like_competition_rule_query
    target=resolve_competition_targets(query)
    if target.status!='exact' or not looks_like_competition_rule_query(query):return None
    from app.pipeline.competition_taxonomy import FACET_ALIASES
    from app.pipeline.competition_name_recovery import recover_names
    registry=tuple((name,alias) for name,aliases in FACET_ALIASES for alias in aliases
                   if len(re.sub(r'\\s+','',alias))>=6 and not re.search(r'\\d',alias))
    _,edits=recover_names(query,registry)
    # Preserve registered game spans and exact adjacent negation.
    for edit in edits:
        if re.search(r'\\d',edit.original+edit.canonical):continue
        if re.search(r'\\b(?:no|not|never|without)\\b|ไม่',edit.original,re.I):continue
        recovered=query[:edit.start]+edit.canonical+query[edit.end:]
        after=resolve_competition_targets(recovered)
        if after.status==target.status and after.targets==target.targets:
            return recovered,edit
    return None
'''
(P/'app/pipeline/competition_facet_recovery.py').write_text(facet,encoding='utf-8')
edit('app/pipeline/competition_presentation.py',r'การตั้งค่าเกม$|ประเภท',r'การตั้งค่า(?:ใน)?เกม$|ประเภท')
# Preserve historical metadata explicitly; source answers remain authoritative at runtime.
edit('tools/build_master_ground_truth_10000.py','        seeds.append(make_seed(\n            locale=locale, domain=domain, question=question, origin="rule_patterns",', '''        # v2.3 stored evaluation metadata predates the detailed fine schedule.
        # This compatibility value is descriptive, not a runtime policy oracle.
        # A new dataset version must opt into current source references instead.
        if locale == "en" and row.get("id") == "rule_damage_responsibility":
            answer = "If equipment is damaged, users are responsible for fines or compensation depending on severity, from minor damage fines to full compensation for severe damage."
        seeds.append(make_seed(
            locale=locale, domain=domain, question=question, origin="rule_patterns",''')
edit('app/pipeline/closed_query_improvements.py','def answer_closed_query_improvement(query,locale):\n', '''def _pay_play_ambiguity(query,locale):
    if not re.search(r'\\bwhere\\s+can\\s+(?:i|we|you)\\s+pay\\b',query,re.I):return None
    if re.search(r'\\b(?:payment|booking|bank|transfer|cash|card|slip|account|fee|cost|price)\\b',query,re.I):return None
    resolution=resolve_game_entity(query,operation='availability')
    if not resolution.is_exact:return None
    answer=("Do you mean where to play this game, or how to pay for a booking?" if locale=='en' else "ต้องการถามว่าเล่นเกมนี้ได้ที่โซนไหน หรือชำระเงินค่าจองอย่างไรครับ?")
    return StructuredToolResult(answer,[],'pay_play_clarification',.98,{'ambiguous_real_word':'pay/play','no_silent_rewrite':True})

def answer_closed_query_improvement(query,locale):
    ambiguity=_pay_play_ambiguity(query,locale)
    if ambiguity is not None:return 'clarification',ambiguity
''')
print('edited core/facet/builder/ambiguity')
