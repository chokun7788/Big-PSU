from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
def replace(old,new):
 global t
 assert t.count(old)==1,(t.count(old),old[:80]);t=t.replace(old,new)
replace("        if method=='common_procedure_topic':requested=['answer'];broad=False", "        if query_operation=='game_overview' or (any(records[rid]['kind']=='game' for rid in ids) and re.fullmatch(r'(?:เกม|game)\\s*[?!.,]*',q)):\n            requested=[key for key in ('summary','genre','how_to_play') if any(value(records[rid],key) is not None for rid in ids)] or ['title'];broad=False\n        if method=='common_procedure_topic':requested=['answer'];broad=False")
replace("        procedure_ids=operation_faqs(procedure_query,records,query_operation)","""        if query_operation in {'booking','price'} and prior_context and not any(records[rid]['kind']=='game' for rid in ids):
            prior_games=[rid for rid in prior_context['record_ids'] if records[rid]['kind']=='game']
            linked={value(r,'game_id') for r in records.values() if r['kind']=='game_service' and value(r,'service_id') in ids and value(r,'offered') is True}
            scope_ids=list(dict.fromkeys(scope_ids+[rid for rid in prior_games if rid in linked]))
        procedure_ids=operation_faqs(procedure_query,records,query_operation)""")
replace("        if method=='common_procedure_topic' and scope_ids:", "        if query_operation in {'price','booking'} and scope_ids and any(records[rid]['kind']=='game' for rid in scope_ids) and not any(records[rid]['kind']=='game' for rid in selected):\n            blocks.append(('เกมที่เกี่ยวข้อง: ' if lang=='th' else 'Related game: ')+ ' / '.join(title(records[rid],lang) for rid in scope_ids if records[rid]['kind']=='game'))\n        if method=='common_procedure_topic' and scope_ids:")
p.write_text(t,encoding='utf-8');print('named-game identity vs catalog and FK-backed access context')
