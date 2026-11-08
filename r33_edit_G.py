from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
f=P/'app/pipeline/bilingual_english.py';s=f.read_text(encoding='utf-8')
old='        if token in tokens or token + "s" in tokens:';assert s.count(old)==1
s=s.replace(old,'        if token in tokens or (token in _WEEKDAY_NAMES_EN and token + "s" in tokens):')
# _WEEKDAY_NAMES_EN is a tuple of display names: use casefold for comparison.
s=s.replace('token in _WEEKDAY_NAMES_EN and token + "s" in tokens','token in {name.casefold() for name in _WEEKDAY_NAMES_EN} and token + "s" in tokens')
needle='    payment_method_signal = (';assert s.count(needle)==1
s=s.replace(needle,'''    if booking_signal and re.search(r"\\btransfer(?:ring)?\\s+(?:(?:my|the|a)\\s+)?(?:booking|reservation)\\b", query, re.I) and not (tokens & {"bank", "money", "payment", "slip"}):
        return _rule_answer("transfer booking", matcher)
'''+needle)
f.write_text(s,encoding='utf-8')
f=P/'app/core/task_frame_recovery.py';s=f.read_text(encoding='utf-8')
old="    if any(c[:2]==best[:2] and (c[2],c[4])!=(best[2],best[4]) for c in candidates[1:]):return None";assert s.count(old)==1
s=s.replace(old,"    if any(c[:2]==best[:2] and (c[2],c[4])!=(best[2],best[4]) and c[2]<best[2]+len(best[3]) and best[2]<c[2]+len(c[3]) for c in candidates[1:]):return None")
f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/closed_query_improvements.py';s=f.read_text(encoding='utf-8')
s=s.replace("[('no_answer',_recorded_catalog_gap)","[('games',_recorded_catalog_gap)")
f.write_text(s,encoding='utf-8')
print('G applied: full weekday plural boundaries, booking transfer semantics, disjoint correction spans, catalog domain retained')
