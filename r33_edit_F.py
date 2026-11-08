from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
f=P/'app/pipeline/closed_query_improvements.py';s=f.read_text(encoding='utf-8')
old="    hits=make_source_hits(source_ids)\n    answer='\\n'.join(result['answer'] for result in results)"
assert s.count(old)==1
s=s.replace(old,"    from app.pipeline.retrieval import load_curated_rows,hit_from_curated\n    rows={row['id']:row for row in load_curated_rows()}\n    if not source_ids or any(source not in rows for source in source_ids):return None\n    hits=[hit_from_curated(rows[source]) for source in source_ids]\n    answer='\\n'.join(result['answer'] for result in results)")
needle='def answer_closed_query_improvement(query,locale):';assert s.count(needle)==1
extra='''def _recorded_catalog_gap(query,locale):
    # Only a literal title and an explicit studio availability request. General
    # game descriptions, prices, controls and competition questions stay separate.
    if not re.search(r'ศูนย์|สตูดิโอ|\\b(?:studio|centre|center)\\b',query,re.I):return None
    if re.search(r'ราคา|ค่าบริการ|เท่าไหร่|แนว|กฎ|กติกา|แข่งขัน|\\b(?:price|cost|fee|genre|rules?|tournament|controls?|how)\\b',query,re.I):return None
    availability=bool(re.search(r'มี.+(?:ไหม|มั้ย|หรือเปล่า)|เล่นได้(?:ไหม|มั้ย)|\\b(?:available|offer|have)\\b',query,re.I))
    if not availability:return None
    from app.runtime.fast_answer import _match_known_unsupported_game,_verified_game_catalog,HITS,OUR_GAMES_URL
    title=_match_known_unsupported_game(query.casefold())
    if not title:return None
    # The historical name list is only a recognition aid. Absence must be
    # checked against the current verified catalog on every new process.
    candidates={part.strip().casefold() for part in title.split('/')}
    catalog=_verified_game_catalog()
    if not catalog or any(str(row.get('name','')).casefold() in candidates for row in catalog):return None
    answer=(f'I could not find {title} in the studio\\'s verified game catalog. Please ask staff before booking to play this game. This does not confirm that the studio cannot offer it.\\nSource: {OUR_GAMES_URL}' if locale=='en' else
            f'ยังไม่พบ {title} ในรายการเกมของศูนย์ที่ยืนยันได้ครับ กรุณาสอบถามเจ้าหน้าที่ก่อนจองเพื่อเล่นเกมนี้ ข้อมูลนี้ยังไม่ใช่การยืนยันว่าศูนย์ไม่มีเกมดังกล่าว\\nแหล่งข้อมูล: {OUR_GAMES_URL}')
    return StructuredToolResult(answer,HITS['our_games'],'recorded_game_catalog_no_answer',.97,{'game':title,'catalog_titles_checked':len(catalog),'absence_only':True,'not_live_occupancy':True})

'''
s=s.replace(needle,extra+needle).replace("[('contact',_contact_fields)","[('no_answer',_recorded_catalog_gap),('contact',_contact_fields)")
f.write_text(s,encoding='utf-8')
print('F applied: curated contact source references; bounded catalog absence lookup')
