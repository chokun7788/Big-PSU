"""Compare only saved same-key output; never contacts chat or a model."""
import collections,json,sys,statistics
from pathlib import Path
R=Path(__file__).resolve().parent
run=Path(sys.argv[1]) if len(sys.argv)>1 else R/'full01'
out=run/'analysis';out.mkdir(exist_ok=False)
done=json.loads((run/'TEST_COMPLETE.json').read_text('utf8'))
assert done['complete'] and done['source_code_inputs_unchanged'] and done['model_identity_verified']
old={x['key']:x for x in map(json.loads,(R/'SAVED_R115_RESULTS.jsonl').open(encoding='utf8'))}
jobs={j['key']:j for j in map(json.loads,(R/'SELECTED_JOBS.jsonl').open(encoding='utf8'))}
rows=list(map(json.loads,(run/'RESULTS.jsonl').open(encoding='utf8')))
assert len(rows)==len({r['key'] for r in rows})==48 and {r['key'] for r in rows}==set(jobs)
counts=collections.Counter();reasons=collections.Counter();domain=collections.defaultdict(collections.Counter);gains=[];losses=[];review=[];latencies=[]
for r in rows:
    b=old[r['key']];assert r['question']==b['question'] and len(r['grades'])==len(b['grades'])==len(jobs[r['key']]['entries'])
    positive_old=[];positive_new=[]
    for g,og in zip(r['grades'],b['grades']):
        assert all(g[k]==og[k] for k in ['file','row','variant','positive_literal'])
        counts['grades']+=1;counts['old_strict']+=og['passed'];counts['new_strict']+=g['passed']
        if g['positive_literal']:
            for c in [counts,domain[r['domain']]]:
                c['positive_grades']+=1;c['old_positive']+=og['literal_passed'];c['new_positive']+=g['literal_passed']
            positive_old.append(og['literal_passed']);positive_new.append(g['literal_passed'])
    a=r['response'].get('decision_artifact') or {};u=a.get('understanding') or {}
    reasons[u.get('reason') or 'no_retained_understanding_artifact']+=1
    counts['requests']+=1;counts['http_ok']+=r['http_status']==200;counts['api_timed_out']+=bool(r['response'].get('timed_out'))
    counts['positive_requests']+=bool(positive_new);counts['old_positive_all']+=bool(positive_old) and all(positive_old);counts['new_positive_all']+=bool(positive_new) and all(positive_new)
    if positive_old and all(positive_old) and not all(positive_new):losses.append(r['key'])
    if positive_new and all(positive_new) and not all(positive_old):gains.append(r['key'])
    latencies.append(r['elapsed_sec'])
    review.append({'key':r['key'],'question':r['question'],'domain':r['domain'],'locale':r['requested_locale'],
      'old_answer':b['response'].get('answer'),'new_answer':r['response'].get('answer'),'understanding':u,
      'new_need_results':a.get('need_results',[]),'old_positive':positive_old,'new_positive':positive_new,
      'grades':r['grades'],'elapsed_sec':r['elapsed_sec']})
transport=collections.Counter()
for e in map(json.loads,(run/'MODEL_TRANSPORT.jsonl').open(encoding='utf8')):
    transport['attempts']+=1;transport['success']+=e['transport_ok'];transport['failures']+=not e['transport_ok']
summary={'complete':True,'development_regression_not_holdout':True,'new_questions':0,'candidate_only':True,
    'counts':dict(counts),'interpretation_reasons':dict(reasons),'by_domain':{k:dict(v) for k,v in domain.items()},
    'model_transport':dict(transport),'positive_request_gains':gains,'positive_request_regressions':losses,
    'latency':{'median_sec':statistics.median(latencies),'p95_sec':sorted(latencies)[int(len(latencies)*.95)]},
    'semantic_accuracy_claimed':False,'sources_and_originals_unchanged':done['original_sources_and_results_unchanged']}
(out/'COMPARISON.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
(out/'PER_REQUEST_REVIEW.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in review),'utf8')
def ratio(n,d):return f'{n}/{d} ({100*n/d:.2f}%)' if d else 'N/A'
doc=['# R117 — ผลตรวจความเข้าใจและการนำแผนไปใช้','','ชุดพัฒนา 48 keys เดิมจาก Full ไม่ใช่ Full ใหม่และไม่ใช่ชุดสุ่มเพื่อประมาณความถูกต้องทั้งระบบ เลือก 40 ข้อแบบ seeded จาก 10 หมวดหลักและ 8 known failures ไม่มีคำถามใหม่ ไม่มี baseline rerun','',
     '| เกณฑ์ | Saved R115 | R117 |','|---|---:|---:|',
     f"| Positive literal/clause | {ratio(counts['old_positive'],counts['positive_grades'])} | {ratio(counts['new_positive'],counts['positive_grades'])} |",
     f"| Requests ผ่าน positive ทุกแถว | {ratio(counts['old_positive_all'],counts['positive_requests'])} | {ratio(counts['new_positive_all'],counts['positive_requests'])} |",
     f"| Strict compatibility | {ratio(counts['old_strict'],counts['grades'])} | {ratio(counts['new_strict'],counts['grades'])} |",'',
     'Literal ไม่เท่ากับ semantic accuracy; strict ยังมี contract ชื่อ route/mode เก่ารวมอยู่ด้วย การได้แผน JSON ผ่านไม่รับรองว่าตีความถูก จึงเก็บคำถาม คำตอบ แผนและ need_results ทุกข้อ','',
     '## การวิเคราะห์ถึงขั้นใหม่','', '```json',json.dumps(dict(reasons),ensure_ascii=False,indent=2),'```','',
     'no_retained_understanding_artifact หมายถึงผลสุดท้ายไม่มี artifact ชั้นนี้ อาจเป็นเส้นทางก่อนเข้า interpreter หรือ fallback ที่ไม่ได้ส่ง artifact ต่อ จึงใช้จำนวนนี้สรุปว่าไม่ได้เรียก interpreter ไม่ได้ ตรรกะ fallback และ source guard เดิมยังอยู่','',
     '## หมวดที่มี positive contracts','', '| หมวด | Positive grades | R115 | R117 |','|---|---:|---:|---:|']
for d,c in domain.items():doc.append(f"| {d} | {c['positive_grades']} | {ratio(c['old_positive'],c['positive_grades'])} | {ratio(c['new_positive'],c['positive_grades'])} |")
doc+=['','## Integrity และโมเดล','', '```json',json.dumps({'chat_http_ok':counts['http_ok'],'chat_timed_out':counts['api_timed_out'],'model_transport':dict(transport),'latency':summary['latency'],'originals_unchanged':done['original_sources_and_results_unchanged']},ensure_ascii=False,indent=2),'```','',
      'เปิด LLM ให้ Flow เลือกอ่านข้อมูลเอง รุ่น/digest ตรวจต้นและท้าย; transport กับ JSON/schema และ semantic correctness เป็นคนละเกณฑ์ ไม่ใช้ HTTP200 เป็นคะแนนคำตอบ','',
      '## หลักฐานรายข้อ','', '[ทุกคำขอและแผนก่อนเลือกหมวด](PER_REQUEST_REVIEW.jsonl)','']
for v in review:
    doc += [f"### {v['key']}",'',v['question'],'','**R115**','','```text',v['old_answer'] or '', '```','','**R117**','','```text',v['new_answer'] or '', '```','','**แผนความหมาย**','','```json',json.dumps(v['understanding'],ensure_ascii=False,indent=2),'```','']
(out/'REPORT_TH.md').write_text('\n'.join(doc),'utf8')
print(json.dumps(summary,ensure_ascii=False))
