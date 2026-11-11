"""Offline report from completed immutable results; no inference or regrading R132."""
import html,json,pathlib,re
R=pathlib.Path(__file__).resolve().parent
O=R/'r135_verified_eval200_20261111/evaluation'
data={
 'แก้ข้อมูลและขอบเขตใหม่':O/'RESULTS.jsonl',
 'ก่อนแก้ข้อมูล (bounded200)':R/'r135_bounded_eval200_20261111/evaluation/RESULTS.jsonl',
 'R134 ที่บันทึกไว้':R/'r134_live_sample_20261031/RESULTS.jsonl'}
jobs=list(map(json.loads,(O/'SELECTED_JOBS.jsonl').open(encoding='utf-8')));keys={x['key'] for x in jobs}
sets={name:{r['key']:r for r in map(json.loads,path.open(encoding='utf-8')) if r['key'] in keys} for name,path in data.items()}
assert all(set(d)==keys and len(d)==200 for d in sets.values())
esc=lambda s:html.escape(str(s))
scores=json.loads((O/'SCORES_COMPARISON.json').read_text(encoding='utf-8'))
parts=['<!doctype html><meta charset="utf-8"><title>ผลแก้ข้อมูลเว็บ 200 ข้อ</title><style>body{font:16px sans-serif;margin:24px}table{width:100%;border-collapse:collapse}td,th{border:1px solid #ccc;padding:12px;vertical-align:top}pre{white-space:pre-wrap;overflow-wrap:anywhere}a{display:block}</style>',
 '<h1>200 คำถามเดิม — ข้อมูลเว็บและขอบเขตเป้าหมาย</h1><p>คะแนนตรวจข้อความเท่านั้น ไม่ใช่ semantic accuracy หรือการตรวจรับทั้งระบบ ใช้ผลย้อนหลังของรุ่นก่อนโดยไม่เรียกโมเดลเก่าซ้ำ เวลา ข้อมูล และ backendต่างกัน ชุดนี้เคยเปิดดูแล้ว ไม่ใช่ unseen test</p>',
 '<p>คำถามเรื่องจำนวนsessionsมีเกณฑ์เดิม5grade identitiesที่คาด3sessions แต่เว็บปัจจุบันระบุ6 จึงรายงานผล literal ตามเกณฑ์เดิมและรายงาน source check แยก ไม่แก้ตัวหารให้คะแนนดูสูงขึ้น</p>',
 '<pre>'+esc(json.dumps(scores,ensure_ascii=False,indent=2))+'</pre>',
 '<table><tr><th>คำถาม</th>'+''.join('<th>'+esc(name)+'</th>' for name in sets)+'</tr>']
for n,job in enumerate(jobs,1):
 parts.append('<tr><td>'+str(n)+'. '+esc(job['question'])+'</td>')
 for name,d in sets.items():
  row=d[job['key']];response=row.get('response',{});sources=response.get('sources',[])
  links=''.join('<a href="'+esc(s['url'])+'">'+esc(s.get('id') or s['url'])+'</a>' for s in sources if re.match(r'^https?://',s.get('url','')))
  parts.append('<td><b>'+esc(row.get('elapsed_seconds','?'))+' วินาที</b><br>'+esc(response.get('mode',''))+'<pre>'+esc(response.get('answer',''))+'</pre>'+links+'</td>')
 parts.append('</tr>')
parts.append('</table>')
(O/'RESULTS_VIEW.html').write_text(''.join(parts),encoding='utf-8')
key='46182d9ba58edbb20f085b98d0f6b7b82c836832b43f8da8751f5a1f96b338a1'
new=next(iter(sets.values()))[key]['response']
source_check={'key':key,'question':next(j['question'] for j in jobs if j['key']==key),
 'current_page_url':'https://esports.computing.psu.ac.th/','expected_current_page_sessions':6,
 'source_aligned_output_observed':bool(re.search(r'\b6\s+sessions',new.get('answer',''),re.I)) and not bool(re.search(r'\b3\s+sessions',new.get('answer',''),re.I)),
 'verified_page_link_returned':any(s.get('url')=='https://esports.computing.psu.ac.th/' for s in new.get('sources',[])),
 'legacy_literal_grade_identities_expecting_3':5,'not_an_all_question_semantic_score':True}
(O/'SOURCE_ALIGNED_CHECK.json').write_text(json.dumps(source_check,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(source_check,ensure_ascii=False))
