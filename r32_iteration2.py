from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert old in s,rel;p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/pipeline/competition_facet_recovery.py',"    if target.status!='exact' or not looks_like_competition_rule_query(query):return None", "    if target.status!='exact' or not looks_like_competition_rule_query(query):return None\n    if re.search(r'ไม่ใช่(?:กฎ|กฏ|กติกา)|not (?:competition |tournament )?rules',query,re.I):return None")
edit('app/pipeline/competition_facet_recovery.py',"    registry=tuple((name,alias) for name,aliases in FACET_ALIASES for alias in aliases", "    aliases_with_valid_settings=FACET_ALIASES+(('match_settings',('game settings','การตั้งค่าในเกม')), )\n    registry=tuple((name,alias) for name,aliases in aliases_with_valid_settings for alias in aliases")
edit('app/pipeline/competition_facet_recovery.py','    for edit in edits:\n', "    for edit in edits:\n        # March is a valid month/verb, and may signal a timing ambiguity.\n        # Whole-span distance does not authorize replacing a valid word.\n        if re.search(r'\\bmarch\\b',edit.original,re.I):continue\n")
edit('app/pipeline/competition_request_contract.py',r"r'กำหนดส่ง|deadline|substitutes?|สำรอง',query",r"r'กำหนดส่ง|deadline|substitutes?|สำรอง|ปิดรับสมัคร|registration.{0,20}closed|add.{0,25}roster',query")
edit('app/pipeline/competition_detail.py','''            note=("I could not find complete verified source clauses for every requested topic." if locale=='en' else "ยังไม่พบข้อกฎที่ยืนยันได้ครบทุกประเด็นที่ถามครับ")
            return CompetitionDetail(note,(),tuple(c.name for c in concepts),'no_answer',('requested_source_missing:'+concept.name,))''','''            if not requirements:return None
            note=("I could not find complete verified source clauses for every requested topic." if locale=='en' else "ยังไม่พบข้อกฎที่ยืนยันได้ครบทุกประเด็นที่ถามครับ")
            return CompetitionDetail(note,(),tuple(c.name for c in concepts),'no_answer',('requested_source_missing:'+concept.name,))''')
print('fixed real-word preservation and locally scoped roster condition')
