import collections,json,re,sqlite3,zlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;O=BASE/'r65_detailed_failure_analysis_20261014';c=sqlite3.connect(O/'evidence.sqlite');c.row_factory=sqlite3.Row
samples=[];used=set()
topics={
'competition':r'กฎ|กติกา|แข่งขัน|แข่ง|rules|tournament|competition',
'price':r'ราคา|บาท|price|cost|fee|rate|THB',
'rental':r'ราคาเหมา|เหมา(?:อุปกรณ์|ทั้ง|เครื่อง|โซน|วัน|ครึ่ง|เต็ม)|ครึ่งวัน|เต็มวัน|\b(?:rental|rent|half.day|full.day)\b',
'budget':r'งบ(?:ประมาณ|[0-9\s]|เท่า|เงิน)|มีเงิน|\b(?:budget|afford|money)\b',
'controls':r'ปุ่ม|ควบคุม|controls|button|bindings|กด',
'games':r'เกมอะไร|เกมไหน|what games|which games|how many games',
'schedule':r'เปิด|ปิด|Maintenance|opening|closing|closed|schedule|hours',
'live':r'ว่าง|ถูกจอง|vacant|available|booked|free',
'owner_policy':r'สมาชิก|บัตร|จอดรถ|ยกเลิก|walk.in|passport|keyboard|mouse|membership|receipt|slip',
'multiclause':r'แล้ว|และ|\band\b|also|compare|เทียบ|แตกต่าง',
'typo':r'สวั|cockpik|afteronon|swich|nintendoo|กฏ',
'outside':r'chicken|egg|ไก่|ไข่|อาหาร|dinner|capital|weather'
}
rows=list(c.execute("SELECT DISTINCT r.* FROM results r JOIN grades g USING(arm,key) WHERE g.passed=0 ORDER BY r.key"))
for topic,pattern in topics.items():
 for arm in ('common_llm','common_offline','legacy_llm','legacy_offline'):
  selected=0
  for r in rows:
   if r['arm']!=arm or r['exception'] or not re.search(pattern,r['question'],re.I):continue
   if (arm,r['key']) in used:continue
   g=list(c.execute('SELECT * FROM grades WHERE arm=? AND key=? AND passed=0',(arm,r['key'])))
   if not any(any(x in gg['issues'] for x in ('missing_content','source_target','forbidden_content','validation','language','other')) for gg in g):continue
   raw=json.loads(zlib.decompress(r['raw']));answer=r['answer'] or ''
   examples=[{'file':gg['file'],'row':gg['rownum'],'variant':gg['variant'],'failures':json.loads(gg['reasons_json']),'expected':json.loads(c.execute('SELECT case_json FROM expected WHERE key=? AND file=? AND rownum=? AND variant=?',(r['key'],gg['file'],gg['rownum'],gg['variant'])).fetchone()[0])} for gg in g[:2]]
   plan=raw.get('result',{}).get('decision_artifact') or {};trace=raw.get('result',{}).get('trace') or []
   samples.append({'topic':topic,'arm':arm,'key':r['key'],'question':r['question'],'mode':r['mode'],'confidence':r['confidence'],'answer':answer,'grades':examples,'artifact':plan,'trace':trace,'source':r['source_file'],'line':r['source_line']})
   used.add((arm,r['key']));selected+=1
   if selected>=2:break
# Add concrete protocol-only and exception cases to prevent cherry-picking.
for arm in ('legacy_offline','common_offline','common_llm'):
 for issue in ('protocol','runtime'):
  r=c.execute('SELECT r.* FROM results r JOIN grades g USING(arm,key) WHERE r.arm=? AND g.issues=? LIMIT 1',(arm,issue)).fetchone()
  if r and (arm,r['key']) not in used:
   raw=json.loads(zlib.decompress(r['raw']));samples.append({'topic':issue,'arm':arm,'key':r['key'],'question':r['question'],'mode':r['mode'],'confidence':r['confidence'],'answer':r['answer'],'exception':r['exception'],'artifact':raw.get('result',{}).get('decision_artifact'),'trace':raw.get('result',{}).get('trace',[]),'source':r['source_file'],'line':r['source_line']})
(O/'REVIEW_SAMPLES.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps([{'topic':s['topic'],'arm':s['arm'],'key':s['key'][:10],'q':s['question'],'mode':s['mode'],'answer':(s.get('answer') or '')[:330],'failure':(s.get('grades') or [{}])[0].get('failures'),'plan':{k:(s.get('artifact') or {}).get('query_plan',{}).get(k) for k in ('record_ids','requested_fields','method','unresolved_clauses')}} for s in samples],ensure_ascii=False,indent=2))
print('Samples:',len(samples))
