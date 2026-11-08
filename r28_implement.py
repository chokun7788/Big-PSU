import ast
from pathlib import Path
PROJECT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
path=PROJECT/'app/pipeline/competition_detail.py'
text=path.read_text(encoding='utf-8')
addition=r'''
    DetailConcept('elimination_format', ('cs2',), r'คัดออก|รูปแบบทัวร์นาเมนต์|elimination format', r'Single Elimination'),
    DetailConcept('competitive_mode', ('cs2',), r'โหมดการแข่งขัน|competitive mode', r'โหมด Competitive|Competitive mode'),
    DetailConcept('bracket_lateness', ('cs2',), r'สาย(?:การแข่งขัน)?(?:ประกาศ|ล่วงหน้า)|ประกาศสาย|มาสาย|bracket|lateness|team is late', r'สายการแข่งขันจะประกาศ|bracket.*announc'),
    DetailConcept('bug_exploitation', ('cs2','tekken8'), r'\bbugs?\b|\bglitch(?:es)?\b|บัค|บั๊ก', r'ห้ามใช้บัค|ห้ามใช้ Bug|Exploiting.*bugs|Bug or Glitch|bugs or glitches'),
    DetailConcept('watch_streams', ('cs2',), r'ดูสตรีม|watch(?:ing)? live streams?', r'ห้ามผู้เล่นดูสตรีม|Watching streams:'),
    DetailConcept('equipment_quality', ('cs2',), r'รับผิดชอบ.*(?:คุณภาพ|ความพร้อม)|(?:quality|readiness).*equipment|responsible.*equipment|responsible.*quality', r'รับผิดชอบต่อคุณภาพ|responsible for the quality'),
    DetailConcept('custom_display', ('cs2',), r'Brightness|Resolution|Crosshair|ความสว่าง|เป้าเล็ง', r'Brightness.*Resolution.*Crosshair'),
    DetailConcept('macros_scripts', ('cs2','valorant'), r'มาโคร|สคริปต์|\bmacros?\b|\bscripts?\b', r'ห้ามใช้สคริปต์|ห้ามใช้มาโคร|No scripts or macros|use of macros.*prohibited'),
    DetailConcept('software_install', ('cs2','valorant'), r'ติดตั้งโปรแกรม|ลงโปรแกรม|install(?:ing)? (?:software|programs?)', r'ห้ามติดตั้งโปรแกรม|(?:not|prohibited).*install|install.*prohibited'),
    DetailConcept('prep_personnel', ('cs2','valorant'), r'(?:เตรียมตัว|Match Prep|match preparation).*(?:กี่คน|players)|(?:how many players|players).*(?:prepare|match prep|match preparation)', r'จำนวนบุคลากร.*6|No more than 6 players|preparation.*6'),
    DetailConcept('competition_food', ('cs2','valorant'), r'กินดื่ม|อาหาร|เครื่องดื่ม|food|drinks?|beverages?', r'น้ำดื่ม.*ภาชนะ.*หมากฝรั่ง|drinking water.*sealed.*chewing gum'),
    DetailConcept('final_authority', ('cs2',), r'คำตัดสิน.*(?:ที่สุด|สุดท้าย)|ผู้จัดเปลี่ยนกฎ|decisions? (?:are |is )?final|organizers?.*amend', r'อำนาจตัดสิน.*ที่สิ้นสุด|decisions.*final'),
    DetailConcept('regulation_timeout', ('valorant',), r'(?:Tactical Timeouts?|เวลานอกทางยุทธวิธี).*(?:รอบปกติ|กี่ครั้ง|regulation|how many)|(?:regulation|how many).*(?:Tactical Timeouts?|เวลานอก)', r'ขอได้ 2 ครั้งต่อแผนที่|2 requests per map|Each team may request up to 2 timeouts'),
    DetailConcept('technical_reasons', ('valorant',), r'(?:Technical Pause|หยุดเกมทางเทคนิค).*(?:ปัญหา|เหตุ|qualify|reasons?)|(?:problems|reasons).*(?:Technical Pause|หยุดเกมทางเทคนิค)', r'ใช้เมื่อมีปัญหา|Used when there are.*(?:malfunctions|disconnections|software)'),
    DetailConcept('ability_boundaries', ('valorant',), r'สกิลนอกขอบ|สกิล.*นอก.*แผนที่|abilities.*outside.*(?:map|boundar)', r'ห้ามใช้สกิล.*นอก|Abilities.*not.*outside|ข้อยกเว้นพิเศษ.*KAY/O|Special exception:.*KAY/O'),
    DetailConcept('cypher_camera', ('valorant',), r'กล้อง Cypher|Cypher cameras?', r'ห้ามวางกล้อง Cypher|Cypher cameras.*must not'),
    DetailConcept('player_boosting', ('valorant',), r'ต่อตัว|กระโดด.*(?:เพื่อน|สูง)|teammates.*boost|boost.*(?:normal|jump)', r'การกระโดดต่อตัว|Using teammates to.*(?:jump|boost)'),
    DetailConcept('character_customization', ('tekken8',), r'ปรับ.*(?:ชุด|ทรงผม|ตัวละคร)|แต่งตัวละคร|customiz|outfits?|hairstyles?', r'ห้าม ปรับแต่งตัวละคร|customization.*prohibited|customization.*not allowed'),
    DetailConcept('tekken_disputes', ('tekken8',), r'ข้อพิพาท|แจ้งใคร|ตัดสิน.*ที่สุด|(?:who|whom).*(?:notified|problems)|dispute decision.*final', r'แจ้งผู้จัดการแข่งขันทันที|ข้อโต้แย้ง.*ที่สิ้นสุด|notify.*organizer|disputes.*final|objections.*final'),
    DetailConcept('rov_sides', ('rov',), r'ใคร.*(?:สีฟ้า|เลือกฝั่ง)|(?:which team|who).*(?:blue|chooses.*side)', r'เกมแรก ทีม|In the first match'),
    DetailConcept('rov_lateness', ('rov',), r'เริ่ม.*ช้า|starts?.*late|start.*minutes late', r'ช้าเกินกว่า.*15 นาที|starts.*15 minutes'),
    DetailConcept('runes', ('rov',), r'รูน|\brunes\b|enhancement systems', r'ใส่รูน|Runes and enhancement'),
    DetailConcept('global_ban_pick', ('rov',), r'แบนและเลือกฮีโร่|แบนเลือกฮีโร่|hero ban.*pick|Global Ban/Pick', r'Global Ban/Pick'),
    DetailConcept('force_majeure', ('rov',), r'เน็ตล่มทั้ง|เซิร์ฟเวอร์ล่ม|เหตุสุดวิสัย|area.wide ISP|game server failure', r'เหตุสุดวิสัย|force majeure'),
'''
needle='\n)\n\n@dataclass(frozen=True)\nclass CompetitionDetail:'
assert needle in text
text=text.replace(needle,addition+needle,1)
text=text.replace('    concepts: tuple[str, ...]\n','    concepts: tuple[str, ...]\n    outcome: str = "answer"\n    reasons: tuple[str, ...] = ()\n',1)
start=text.index('def requested_detail_concepts(');end=text.index('\ndef lookup_competition_detail',start)
replacement=r'''def requested_detail_concepts(query: str, game_id: str) -> tuple[DetailConcept, ...]:
    result = []
    for concept in CONCEPTS:
        if game_id not in concept.games or not re.search(concept.question, query, re.I):
            continue
        excluded = bool(concept.exclude and re.search(concept.exclude, query, re.I))
        # These qualifiers belong to their proposition. An unrelated requested
        # proposition elsewhere must not suppress a known source clause.
        if concept.name == 'money_bomb' and re.search(r'รอบปกติ|regulation|normal rounds?',query,re.I):
            excluded = False
        if concept.name == 'protest' and re.search(r'ยื่น|ใคร|ภายใน|กี่นาที|file|submit|who|minutes|deadline',query,re.I):
            excluded = False
        if concept.name == 'map_pool' and re.search(r'เว็บอะไร|which website|which tool',query,re.I):
            excluded = False
        if concept.name == 'own_equipment' and re.search(r'รับผิดชอบ|คุณภาพ|ความพร้อม|quality|readiness|responsible',query,re.I):
            if not re.search(r'นำ.*มา.*ได้|มาได้|\bbring\b',query,re.I):
                excluded = True
        if concept.name == 'rematch' and re.search(r'เน็ตล่มทั้ง|เซิร์ฟเวอร์|เหตุสุดวิสัย|ISP|server failure',query,re.I):
            if not re.search(r'First Blood|2 (?:นาที|minutes)',query,re.I):
                excluded = True
        if not excluded:
            result.append(concept)
    return tuple(result)
'''
text=text[:start]+replacement+text[end:]
ast.parse(text);path.write_text(text,encoding='utf-8')

gap_code=r'''"""Source gaps and conflicting clauses for one explicitly named rulebook.

This reads source text, never confirms policy or supplies missing values.
"""
from __future__ import annotations
import re
from app.knowledge.localization import approved_localization
from app.pipeline.competition_detail import CompetitionDetail, lookup_competition_detail
from app.pipeline.competition_targets import looks_like_competition_rule_query,resolve_competition_targets
from app.pipeline.competition_presentation import render_rule_reply,source_clause_lines,is_rule_clause

def _rows(rulebook_id):
    from app.pipeline.retrieval import load_curated_rows
    return sorted((r for r in load_curated_rows() if not r.get('_canonical_projection') and str(r.get('id','')).startswith(rulebook_id+'_s')),key=lambda r:(int(r.get('section_index') or 0),int(r.get('chunk_index') or 0)))

def _text(row,locale):
    return (approved_localization(row,'text') or '') if locale=='en' else str(row.get('text') or '')

def _source_gap(query,locale,rows):
    numbered=re.search(r'(?:ข้อ|\bclause|\brule|\bsection)\s*(\d+(?:\.\d+){1,5})(?![\d.])',query,re.I)
    if numbered:
        number=numbered.group(1)
        source_matches=[(row,line) for row in rows for line in source_clause_lines(str(row.get('text') or '')) if re.match(r'^'+re.escape(number)+r'(?:\.|\s)',line)]
        # A final dangling preposition cannot substantiate a complete rule.
        if source_matches and any(re.search(r'ดังกล่าวออกจาก\s*$',line) for _,line in source_matches):
            note=(f'I could not find a complete verified text for clause {number}: the recorded source ends mid-sentence. The organizer must provide the complete source.' if locale=='en' else f'ยังไม่พบข้อความฉบับเต็มที่ยืนยันได้สำหรับข้อ {number} เพราะต้นฉบับจบไม่ครบ ต้องขอเอกสารฉบับเต็มจากผู้จัดครับ')
            return CompetitionDetail(note,(),(), 'no_answer',('source_clause_incomplete',))
        if source_matches:
            translated=[(row,line) for row,_ in source_matches for line in source_clause_lines(_text(row,locale)) if re.match(r'^'+re.escape(number)+r'(?:\.|\s)',line) and is_rule_clause(line)]
            if translated:
                selected=list(dict.fromkeys(line for _,line in translated));used=tuple({row['id']:row for row,_ in translated}.values())
                return CompetitionDetail(render_rule_reply(selected[0],selected[1:],used[0],locale),used,('explicit_clause',))
        note=(f'I could not find a complete verified clause {number} in this rulebook.' if locale=='en' else f'ยังไม่พบข้อความข้อ {number} ฉบับเต็มที่ยืนยันได้ในเอกสารของเกมนี้ครับ')
        return CompetitionDetail(note,(),(), 'no_answer',('explicit_clause_not_covered',))
    missing=[]
    if re.search(r'ค่าสมัคร|ค่าลงทะเบียน|(?:registration|entry|participation) fee',query,re.I):
        money=[(r,line) for r in rows for line in source_clause_lines(_text(r,locale)) if re.search(r'ค่าสมัคร|ค่าลงทะเบียน|(?:registration|entry|participation) fee',line,re.I) and re.search(r'\d',line)]
        if money:
            selected=list(dict.fromkeys(line for _,line in money));used=tuple({r['id']:r for r,_ in money}.values())
            return CompetitionDetail(render_rule_reply(selected[0],selected[1:],used[0],locale),used,('registration_fee',))
        missing.append(('registration_fee_not_in_source','I could not find a registration fee in this game\'s recorded rulebook.' if locale=='en' else 'ยังไม่พบข้อมูลค่าสมัครการแข่งขันในเอกสารของเกมนี้ครับ'))
    if re.search(r'minimum age|age requirement|อายุขั้นต่ำ|อายุอย่างน้อย',query,re.I):
        missing.append(('minimum_age_not_in_source','I could not find a minimum age requirement in this game\'s recorded rulebook.' if locale=='en' else 'ยังไม่พบข้อมูลอายุขั้นต่ำในเอกสารของเกมนี้ครับ'))
    if not missing:
        return None
    detail=lookup_competition_detail(query,locale)
    notes=' '.join(note for _,note in missing);reasons=tuple(reason for reason,_ in missing)
    if detail is None:
        return CompetitionDetail(notes,(),(), 'no_answer',reasons)
    # Keep every supported proposition and make the unresolved one visible.
    marker='\nRulebook:' if locale=='en' else '\nอ้างอิงจากกติกา:'
    label='Additional requested information: ' if locale=='en' else 'ประเด็นที่ยังไม่พบข้อมูล: '
    answer=detail.answer.replace(marker,'\n'+label+notes+marker,1)
    return CompetitionDetail(answer,detail.rows,detail.concepts,'partial',reasons)

def _pause_conflict(query,locale,rows,game_id):
    if game_id!='tekken8' or not re.search(r'หยุดเกม|\bpaus(?:e|ing)',query,re.I):
        return None
    prohibitions=[];permissions=[];penalties=[]
    for row in rows:
        for line in source_clause_lines(_text(row,locale)):
            if re.search(r'เริ่มเกม.*ห้ามหยุดเกม.*เหตุผล|(?:Once|After).*game.*(?:no.*pausing|paus.*(?:prohibited|not permitted))',line,re.I):prohibitions.append((row,line))
            if re.search(r'การกดหยุดเกม.*ผู้เล่นทุกคนยินยอม|game may be paused.*all players agree',line,re.I):permissions.append((row,line))
            if re.search(r'กดหยุดเกม.*(?:ปรับแพ้|โทษ)|(?:intentional.*pause|Pausing the game without).*penalty',line,re.I):penalties.append((row,line))
    if not prohibitions or not permissions:
        return None
    first=('The recorded pause clauses conflict. The organizer must confirm the exception conditions and penalty level before a definite ruling can be given.' if locale=='en' else 'ข้อกฎเรื่องการหยุดเกมในเอกสารขัดกัน ต้องให้ผู้จัดยืนยันเงื่อนไขข้อยกเว้นและระดับโทษก่อนจึงจะสรุปได้ครับ')
    pairs=prohibitions+permissions+penalties;used=tuple({row['id']:row for row,_ in pairs}.values())
    answer=render_rule_reply(first,list(dict.fromkeys(line for _,line in pairs)),used[0],locale)
    return CompetitionDetail(answer,used,('pause_conflict',),'conflict',('source_clauses_conflict',))

def lookup_competition_reply(query,locale):
    target=resolve_competition_targets(query)
    if target.status!='exact' or not looks_like_competition_rule_query(query):return None
    rows=_rows(target.targets[0].rulebook_id)
    gap=_source_gap(query,locale,rows)
    if gap is not None:return gap
    conflict=_pause_conflict(query,locale,rows,target.targets[0].game_id)
    if conflict is not None:return conflict
    return lookup_competition_detail(query,locale)
'''
ast.parse(gap_code)
with (PROJECT/'app/pipeline/competition_source_gaps.py').open('x',encoding='utf-8') as f:f.write(gap_code)

path=PROJECT/'app/pipeline/engine.py';text=path.read_text(encoding='utf-8')
text=text.replace('from app.pipeline.competition_detail import lookup_competition_detail','from app.pipeline.competition_source_gaps import lookup_competition_reply',1)
text=text.replace('detail = lookup_competition_detail(pre.clean_query,','detail = lookup_competition_reply(pre.clean_query,',1)
needle='                detail_route = PipelineRoute("competition_rules",'
assert needle in text
text=text.replace(needle,'                detail_mode = {"no_answer":"pipeline:competition_rule_detail_no_answer", "partial":"pipeline:competition_rule_detail_partial_source", "conflict":"pipeline:competition_rule_source_conflict"}.get(detail.outcome,"pipeline:competition_rule_detail_source")\n'+needle,1)
text=text.replace('hits=detail_hits, mode="pipeline:competition_rule_detail_source")','hits=detail_hits, mode=detail_mode)',1)
text=text.replace('"validation_errors":list(detail_validation.errors)}','"validation_errors":list(detail_validation.errors),"outcome":detail.outcome,"reasons":list(detail.reasons)}',1)
text=text.replace('"all requested detail concepts have source clauses", {"concepts":list(detail.concepts),"source_ids":[row[\'id\'] for row in detail.rows]}','"supported clauses retained; source gaps/conflicts explicitly reported", {"concepts":list(detail.concepts),"source_ids":[row[\'id\'] for row in detail.rows],"outcome":detail.outcome,"reasons":list(detail.reasons)}',1)
text=text.replace('self._build_result(detail.answer, detail_hits, started, "pipeline:competition_rule_detail_source",','self._build_result(detail.answer, detail_hits, started, detail_mode,',1)
ast.parse(text);path.write_text(text,encoding='utf-8')
print('Updated concept selection and source gap/conflict replies; source and policies untouched')
