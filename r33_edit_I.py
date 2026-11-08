from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
f=P/'app/pipeline/closed_query_improvements.py';s=f.read_text(encoding='utf-8')
old="    rows={row['id']:row for row in load_curated_rows() if row.get('id')}";assert s.count(old)==1
s=s.replace(old,"    rows={}\n    for row in load_curated_rows():\n        if row.get('id') and row.get('language','th')=='th' and row.get('text'):\n            rows.setdefault(row.get('content_id') or row['id'],row)")
needle="    hits=[hit_from_curated(rows[source]) for source in source_ids]";assert s.count(needle)==1
s=s.replace(needle,"    if any(result['answer'].strip() not in str(rows[source]['text']) for result in results for source in result.get('source_ids',[])):return None\n"+needle)
f.write_text(s,encoding='utf-8')
f=P/'tests/test_usable_task_frames_r33_20261002.py';s=f.read_text(encoding='utf-8')
s=s.replace("{hit['id'] for hit in result.hits}","{source for hit in result.hits for source in hit['metadata']['source_ids']}")
f.write_text(s,encoding='utf-8')
print('I: bind approved rule source IDs to canonical content IDs; retain projected evidence IDs')
