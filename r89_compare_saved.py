"""Same checker/cases on retained legacy ON and R88 common ON answers only."""
import collections,gzip,hashlib,json,sqlite3,sys
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;R=B/'r89_saved_full_comparison_20261018';R.mkdir(exist_ok=False);NEW=B/'r88_full_common_llm_20261017'
sys.path.insert(0,str(NEW));from analyze import literal,rows
config=json.loads((NEW/'CONFIG.json').read_text('utf8'));original=B/'r64_full_comparison_20261013/JOBS.jsonl';assert hashlib.sha256(original.read_bytes()).hexdigest()==config['population_jobs_sha256']
jobs={j['key']:j for j in (json.loads(s) for s in (NEW/'SELECTED_JOBS.jsonl').read_text('utf8').splitlines())}
db=B/'r65_detailed_failure_analysis_20261014/evidence.sqlite';c=sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True)
assert c.execute("SELECT count(*) FROM results WHERE arm='legacy_llm'").fetchone()[0]==20554
old={key:{'answer':a or '', 'exception':e,'effective_locale':locale} for key,a,e,locale in c.execute("SELECT key,answer,exception,locale FROM results WHERE arm='legacy_llm'")}
oldgrades={}
for key,file,row,variant,passed in c.execute("SELECT key,file,rownum,variant,passed FROM grades WHERE arm='legacy_llm'"):
 oldgrades[(key,file,row,variant)]=bool(passed)
c.close();assert len(oldgrades)==55811
totals=collections.Counter();bylocale=collections.defaultdict(collections.Counter);bydomain=collections.defaultdict(collections.Counter);examples=collections.defaultdict(list);sample_domains=collections.defaultdict(set);seen=set()
def bucket(a,b):return 'both_pass' if a and b else 'old_only_pass' if a else 'new_only_pass' if b else 'both_fail'
with gzip.open(R/'PER_REQUEST_COMPARISON.jsonl.gz','xt',encoding='utf8') as out:
 for file,line,row in rows(NEW/'full01'):
  key=row['key'];assert key not in seen;seen.add(key);job=jobs[key];previous=old[key];answer=(row.get('result') or {}).get('answer','');lang=job['locale'];domain=job['r70_stratum']['domain'];stats=[totals,bylocale[lang],bydomain[domain]];old_positive=[];new_positive=[];local=collections.Counter()
  for stat in stats:stat['requests']+=1
  grade_map={(g['file'],g['row'],g['variant']):g for g in row['grades']}
  for entry in job['entries']:
   gid=(entry['file'],entry['row'],entry['variant']);oldraw=oldgrades[(key,*gid)];newraw=grade_map[gid]['passed'];kind=bucket(oldraw,newraw)
   for stat in stats:stat['grades']+=1;stat['old_strict_passed']+=oldraw;stat['new_strict_passed']+=newraw;stat['strict_'+kind]+=1
   oa,oe,op=literal(entry['case'],previous['answer']);na,ne,np=literal(entry['case'],answer);assert op==np and (oa is None)==(na is None)
   if oa is None:continue
   for stat in stats:stat['literal_checked']+=1;stat['old_literal_passed']+=oa;stat['new_literal_passed']+=na
   if not op:continue
   old_positive.append(oa);new_positive.append(na);kind=bucket(oa,na)
   for stat in stats:stat['positive_checked']+=1;stat['old_positive_passed']+=oa;stat['new_positive_passed']+=na;stat['positive_'+kind]+=1
   local[kind]+=1
   if kind in {'old_only_pass','new_only_pass'} and len(examples[kind])<16 and domain not in sample_domains[kind]:
    sample_domains[kind].add(domain);examples[kind].append({'key':key,'question':job['question'],'requested_locale':lang,'domain':domain,'corpus':entry['file'],'row':entry['row'],'variant':entry['variant'],'expected':entry['case'],'old_answer':previous['answer'],'new_answer':answer,'old_literal_failures':oe,'new_literal_failures':ne,'new_decision':(row.get('result') or {}).get('decision_artifact'), 'new_result_file':file,'new_result_line':line,'old_exception':previous['exception']})
  if old_positive:
   for stat in stats:stat['positive_checked_requests']+=1;stat['old_all_positive_passed_requests']+=all(old_positive);stat['new_all_positive_passed_requests']+=all(new_positive)
  out.write(json.dumps({'key':key,'question':job['question'],'locale':lang,'positive_contract_grades':len(old_positive),'old_positive_all_passed':all(old_positive) if old_positive else None,'new_positive_all_passed':all(new_positive) if new_positive else None,'grade_pairs':local},ensure_ascii=False)+'\n')
  if len(seen)%5000==0:print(json.dumps({'compared_saved_requests':len(seen)}),flush=True)
assert set(jobs)==seen and totals['requests']==20554 and totals['grades']==55811
assert totals['old_strict_passed']==42601 and totals['new_strict_passed']==5033
result={'created_at_utc':datetime.now(timezone.utc).isoformat(),'complete':True,'old_arm':'R64 legacy_llm retained in R65 evidence.sqlite','new_arm':'R88 common ON frozen R87 stage 2','same_corpus_sha256':config['population_jobs_sha256'],'same_literal_checker':'R88 analyze.literal; positive text and complete-clause contracts; no semantic equivalence claim','same_grades':True,'llm_calls_made':0,'chatbot_requests_executed':0,'old_or_new_data_modified':False,'totals':totals,'by_requested_locale':dict(bylocale),'by_domain':dict(bydomain),'caveats':['Archived runs from different dates and application/data revisions, not a controlled schema-only experiment','Exact/literal translation/wording differences and protective expired-data refusals can fail; no human semantic accuracy claim','R64 native content-only definition is different and is not compared numerically with R88 positive literal percentage','R64 HTTP session and R88 engine-session checks use different execution surfaces; not a head-to-head session score'], 'examples':examples}
with (R/'SAME_CHECKER_COMPARISON.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
def pct(n,d):return f'{n:,}/{d:,} ({100*n/d:.2f}%)'
t=totals
lines=['# เปรียบเทียบผลที่บันทึกไว้: Format เดิม R64 กับ Format กลาง R88','',
'ใช้เฉพาะแขน LLM ON ของทั้งสองรอบ อ่านคำตอบเดิมและผลล่าสุดเทียบโจทย์/ตัวตรวจเดียวกัน ไม่รัน pipeline หรือโมเดลใหม่ ไม่แก้ oracle ข้อมูล โค้ด หรือ logs เดิม','',
'## ผลรวมคำถามและเกณฑ์เดียวกัน','', '| ตัวชี้วัด | เดิม R64 / LLM ON | ใหม่ R88 / LLM ON |','|---|---:|---:|',
f"| ผ่านเกณฑ์เดิมทั้งหมด รวม route/mode/status | {pct(t['old_strict_passed'],t['grades'])} | {pct(t['new_strict_passed'],t['grades'])} |",
f"| ผ่านเกณฑ์ข้อความที่ต้องปรากฏ (ตัวตรวจเดียวกัน) | {pct(t['old_positive_passed'],t['positive_checked'])} | {pct(t['new_positive_passed'],t['positive_checked'])} |",
f"| ระดับคำถาม: ผ่านเกณฑ์ข้อความเชิงบวกทุกแถวที่ผูกไว้ | {pct(t['old_all_positive_passed_requests'],t['positive_checked_requests'])} | {pct(t['new_all_positive_passed_requests'],t['positive_checked_requests'])} |",'',
'เกณฑ์ strict ถูกออกแบบตาม flow เดิม จึงไม่ใช่เนื้อหาล้วน ส่วน positive literal ตรวจข้อความ/ข้อกฎตรงตามที่กำหนด ไม่ใช่ความถูกต้องเชิงความหมายทุกประโยค ข้อไม่มีเกณฑ์เชิงบวกไม่ถูกนำไปอ้างว่าตอบครบ','',
'## คู่เกณฑ์ข้อความเดียวกัน','',f"- ทั้งคู่ผ่าน: {t['positive_both_pass']:,}",f"- เดิมผ่าน ใหม่ไม่ผ่าน: {t['positive_old_only_pass']:,}",f"- ใหม่ผ่าน เดิมไม่ผ่าน: {t['positive_new_only_pass']:,}",f"- ทั้งคู่ไม่ผ่าน: {t['positive_both_fail']:,}",'',
'## แยกตามภาษาในคำขอ (cohort คงที่ทั้งสองฝั่ง)','', '| ภาษา requested | Requests | เดิมผ่าน positive literal | ใหม่ผ่าน positive literal |','|---|---:|---:|---:|']
for lang,s in sorted(bylocale.items()):lines.append(f"| {lang} | {s['requests']:,} | {pct(s['old_positive_passed'],s['positive_checked'])} | {pct(s['new_positive_passed'],s['positive_checked'])} |")
lines+=['','auto แยกไว้ ไม่เปลี่ยนกลุ่มตามภาษาที่บอตแต่ละรุ่นตอบกลับ จึงต่างจากตาราง effective locale ในรายงานเก่า','',
'## ข้อสรุปที่หลักฐานรองรับ','',
'Format กลางปัจจุบันยังตามผลเดิมไม่ทันในเกณฑ์ข้อความชุดนี้ ความต่างไม่ใช่เฉพาะชื่อ route เพราะยังมีช่องว่างใน positive literal อย่างไรก็ดี ช่องว่างนี้รวมการแปลคนละถ้อยคำ การตอบ label ต่างระดับ และการไม่ยืนยันราคาที่หมดอายุ จึงไม่ใช่จำนวนข้อผิดสาระจริงทั้งหมด','',
'ยังสรุปไม่ได้ว่า schema กลางทำให้แย่ลงด้วยตัวมันเอง: engine/router/relations/field selection/projection และวันที่/validity เปลี่ยนด้วย ต้องแก้ task coverage และตรวจ source/oracle เป็นรายกลุ่ม ไม่ปิด validity guard หรือเติมนโยบายเพื่อไล่คะแนน','',
'คะแนน R64 content-only 96% ในรายงานเก่าใช้ตัวตรวจคนละนิยามกับ positive literal 72.10% ของ R88 จึงไม่ใช้คู่นั้นเป็นตารางเทียบตรง ตัวเลขในรายงานนี้อ่านคำตอบเก่าผ่าน R88 literal เดียวกันแล้ว','',
'## ตัวอย่างที่ผลต่างกัน','']
for kind,label in [('old_only_pass','เดิมผ่าน / ใหม่ไม่ผ่าน'),('new_only_pass','ใหม่ผ่าน / เดิมไม่ผ่าน')]:
 lines+=['### '+label,'']
 for e in examples[kind][:8]:
  lines+=['#### '+e['question'],'',f"หมวด: {e['domain']}; key: `{e['key']}`",'', '**คำตอบเดิม**','',e['old_answer'],'','**คำตอบใหม่**','',e['new_answer'],'','**เหตุที่ตัวตรวจไม่ผ่าน**','', '```json',json.dumps({'old':e['old_literal_failures'],'new':e['new_literal_failures']},ensure_ascii=False,indent=2),'```','']
lines+=['## หลักฐาน','', '- SAME_CHECKER_COMPARISON.json: counts ทุกกลุ่มและตัวอย่างพร้อม expected/decision','- PER_REQUEST_COMPARISON.jsonl.gz: ผลทุก request key ที่เทียบ','- ต้นทางเดิม: r65_detailed_failure_analysis_20261014/evidence.sqlite (read-only)','- ต้นทางใหม่: r88_full_common_llm_20261017/full01/RESULTS_*.jsonl.gz','- ทั้งสองฝั่ง 20,554 requests / 55,811 grades; ไม่มีผลตกหล่นหรือรัน chatbot ซ้ำ']
with (R/'COMPARISON_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in {'examples','by_domain'}},ensure_ascii=False))
