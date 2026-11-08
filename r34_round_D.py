from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=P/'app/core/intent_cue_recovery.py';s=p.read_text(encoding='utf-8')
old='    if resolve_competition_targets(text).status in {\'exact\', \'multiple\'}:\n        # The registered target anchors a long task word'
new='''    if resolve_competition_targets(text).status == 'exact' and 'อ้างอิง' in text and not re.search(r'ไม่ใช่(?:กฎ|กฏ|กติกา)|not (?:competition |tournament )?rules', text, re.I):
        # A reference verb and exact registered target survive independently.
        # Bootstrap the rule cue before the separate facet pass on the next step.
        recovery = _thai_span(text, 'กติกา', '', 1, start_after='อ้างอิง')
        if recovery is not None:
            return recovery
    if resolve_competition_targets(text).status in {'exact', 'multiple'}:
        # The registered target anchors a long task word'''
assert s.count(old)==1;p.write_text(s.replace(old,new),encoding='utf-8')
print('Round D exact-target/reference anchored rule-cue bootstrap saved')
