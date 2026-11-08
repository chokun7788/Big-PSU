"""Summarize one completed live run without modifying its raw results."""
import hashlib,json,statistics,sys
from pathlib import Path
B=Path(__file__).resolve().parent
T=Path(sys.argv[1]).resolve()
if not T.is_relative_to(B/'results'):raise ValueError('Select a run inside this runner results directory')
result=json.loads((T/'RESULTS.json').read_text(encoding='utf8'))
rows=[json.loads(s) for s in (T/'CHAT_TURNS.jsonl').read_text(encoding='utf8').splitlines()] if (T/'CHAT_TURNS.jsonl').is_file() else []
model_files=list(T.glob('*_real_model_generation.json'))
generation=json.loads(model_files[0].read_text(encoding='utf8')) if model_files else {}
envelope=generation.get('body') or {}
metrics={key+'_ms':round(envelope[key]/1e6,3) for key in ['total_duration','load_duration','prompt_eval_duration','eval_duration'] if isinstance(envelope.get(key),(int,float))}
timings={}
for lang in ('th','en'):
    values=[r['elapsed_seconds'] for r in rows if r['locale']==lang]
    timings[lang]={'count':len(values),'median_seconds':round(statistics.median(values),3) if values else None,'max_seconds':max(values) if values else None,'min_seconds':min(values) if values else None}
details=[]
for r in rows:
    body=r.get('body') if isinstance(r.get('body'),dict) else {};p=(body.get('decision_artifact') or {}).get('query_plan') or {};audit=p.get('entity_selection') or {}
    details.append({'case':r['case'],'question':r['question'],'answer':body.get('answer'),'locale':r['locale'],'seconds':r['elapsed_seconds'],'passed':r['passed'],'content_errors':r['errors'],'method':p.get('method'),'selector_failure':r.get('selector_failure'),'selector_attempted':audit.get('attempted'),'selector_transport_ok':audit.get('transport_ok'),'selector_schema_accepted':audit.get('schema_accepted'),'selector_semantic_accepted':audit.get('semantic_selection_accepted'),'selector_reason':audit.get('reason'),'selector_timing_ms':audit.get('timing_ms'),'model_metrics':audit.get('model_metrics'),'model_call_avoided':audit.get('model_call_avoided')})
source= B.parent/'r78_web_session_check_20261016/system'
installation=json.loads((B.parent/'r81_selector_latency_20261017/INSTALLATION.json').read_text(encoding='utf8'))
code_unchanged=all(hashlib.sha256((source/name).read_bytes()).hexdigest()==digest for name,digest in installation['installed_files'].items())
review={'source_run':str(T),'execution_context':'assistant tools after user enabled full access','raw_result':result,'model_generation_metrics':metrics,'timings_by_language':timings,'details':details,'r81_installed_code_unchanged':code_unchanged,'sample_is_not_full_test':True,'timings_are_after_recorded_model_warmup':True}
with (T/'REVIEW.json').open('x',encoding='utf8') as f:json.dump(review,f,ensure_ascii=False,indent=2)
lines=['# ผลทดสอบจริงอัตโนมัติหลังเปิด Full access','',
       '- ตัวรันเรียกจากเครื่องมือในแชท ไม่ต้องให้ผู้ใช้ส่งคำถามทีละข้อ',
       '- ตรวจว่าเปิด LLM: '+str(result['llm_enabled_verified']),
       '- โมเดลสร้างข้อความจริงสำเร็จ: '+str(result['real_model_generation_verified']),
       '- ข้อความที่ได้ผล: '+str(result['count'])+'/'+str(result['expected_count']),
       '- ผ่านเกณฑ์คำตอบ: '+str(result['passed'])+'/'+str(result['count']),
       '- DB ไม่เปลี่ยน: '+str(result['database_unchanged']),
       '- โค้ด R81 ไม่เปลี่ยนระหว่างรอบ: '+str(code_unchanged),'',
       '## ผลการเรียกโมเดลแยกจากเนื้อหา','',
       '```json',json.dumps(result['chat_selector'],ensure_ascii=False,indent=2),'```','',
       'คำถามบางข้อใช้ข้อมูลตรงหรือถามยืนยัน จึงไม่เรียก LLM ตาม Flow ปกติ การสร้าง READY สำเร็จพิสูจน์ว่าโมเดลสร้างข้อความได้ แต่ไม่พิสูจน์ว่า selector เลือกแหล่งข้อมูลถูก การคืน JSON ถูกเป็นอีกเกณฑ์แยกจากความหมายและคำตอบ','',
       '## เวลา HTTP หลัง warm-up','',
       '| ภาษา | จำนวนข้อความ | มัธยฐาน (วินาที) | ต่ำสุด | สูงสุด |',
       '|---|---:|---:|---:|---:|']
for lang,v in timings.items():lines.append('| '+lang+' | '+str(v['count'])+' | '+str(v['median_seconds'])+' | '+str(v['min_seconds'])+' | '+str(v['max_seconds'])+' |')
lines+=['','เป็นตัวอย่างชุดเล็กหลัง warm-up ไม่ใช่เวลาปกติทุกคำถามหรือ benchmark ความจุระบบ ไม่ได้รัน full corpus','',
        '## ผลรายข้อความ','']
for i,d in enumerate(details,1):
    lines += ['### '+str(i)+'. '+d['question'],'',
        '- ภาษา: '+d['locale']+'; HTTP '+str(d['seconds'])+' วินาที; ผ่าน: '+str(d['passed']),
        '- วิธีตอบ: '+str(d['method'])+'; model_call_avoided='+str(d['model_call_avoided']),
        '- selector: attempted='+str(d['selector_attempted'])+', transport='+str(d['selector_transport_ok'])+', schema='+str(d['selector_schema_accepted'])+', semantic='+str(d['selector_semantic_accepted']),
        '- ข้อผิดพลาด: '+str(d['content_errors'])+'; selector_failure='+str(d['selector_failure'])+'; reason='+str(d['selector_reason']),'',str(d['answer']),'']
if result.get('obstacle'):lines+=['## อุปสรรคที่พบ','',json.dumps(result['obstacle'],ensure_ascii=False,indent=2),'']
lines+=['## หลักฐาน','',
        '- RESULTS.json: ผลรวม ข้อผิดพลาด และ hash ของ DB',
        '- CHAT_TURNS.jsonl: คำถาม คำตอบ และ audit จริงทั้งหมด',
        '- *_real_model_generation.json: response และ timing จาก Ollama',
        '- *_chat_health_*.json และ launcher logs: source fingerprint, LLM ON และการเปิด/ปิด R78',
        '- REVIEW.json: สรุปแบบอ่านด้วยเครื่อง ไม่มีการแก้ log เดิม','']
with (T/'REPORT_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines))
print(json.dumps({'result':result,'timings':timings,'model_metrics':metrics,'report':str(T/'REPORT_TH.md')},ensure_ascii=False))
