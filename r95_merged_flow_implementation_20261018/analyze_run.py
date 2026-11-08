"""Grade retained outputs only. Original results/oracles are never rewritten."""
import argparse,collections,gzip,json,statistics,hashlib
from pathlib import Path
from analyze import literal,bucket
R=Path(__file__).resolve().parent;B=R.parent

def rows(folder):
    for p in sorted(folder.glob('RESULTS_*.jsonl.gz')):
        with gzip.open(p,'rt',encoding='utf-8') as f:
            for line in f:
                if line.strip():yield json.loads(line)

def ratio(p,n):return f'{p:,}/{n:,} ({100*p/n:.2f}%)' if n else 'n/a'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--run',required=True);ap.add_argument('--jobs',required=True);ap.add_argument('--out',required=True);args=ap.parse_args()
    run=R/args.run;out=R/args.out;out.mkdir(exist_ok=False)
    jobs={j['key']:j for j in map(json.loads,(R/args.jobs).read_text(encoding='utf-8').splitlines())}
    done=json.loads((run/'RUN_FINISHED.json').read_text(encoding='utf-8'))
    assert done['coverage_complete'] and done['completed']==len(jobs)
    old={row['key']:row for row in rows(B/'r88_full_common_llm_20261017/full01') if row['key'] in jobs}
    sample={r['key']:r for r in map(json.loads,(B/'r93_random_1000_common_on_20261018/PER_REQUEST_ANALYSIS.jsonl').read_text(encoding='utf-8').splitlines())}
    assert len(old)==len(jobs)
    totals=collections.Counter();langs=collections.defaultdict(collections.Counter);domains=collections.defaultdict(collections.Counter)
    reasons=collections.Counter();paths=collections.Counter();signals=collections.Counter();times=[];seen=set();regressions=[];improvements=[];examples=[];sample_totals=collections.Counter()
    with (out/'PER_REQUEST_ANALYSIS.jsonl').open('x',encoding='utf-8') as f:
        for row in rows(run):
            key=row['key'];assert key in jobs and key not in seen;seen.add(key);job=jobs[key]
            result=row.get('result',{});art=result.get('decision_artifact') or {};plan=art.get('query_plan') or {};answer=result.get('answer','');before=old[key].get('result',{}).get('answer','')
            lang=job['locale'];domain=job['r70_stratum']['domain'];counts=[totals,langs[lang],domains[domain]];times.append(row.get('elapsed_sec',0))
            for c in counts:c['requests']+=1;c['exceptions']+=bool(row.get('exception'));c['empty_answers']+=not bool(answer)
            paths[(art.get('task_flow') or {}).get('path','guard_or_dispatcher')]+=1
            if 'not_current' in result.get('mode',''):signals['not_current_requests']+=1
            if art.get('rejected_candidate'):signals['candidate_rejected_requests']+=1
            if result.get('validation',{}).get('ok') is False:signals['invalid_final_requests']+=1
            for call in row.get('observed_model_http_calls',[]):
                totals['model_http_attempts']+=1;totals['model_response_opened']+=bool(call.get('transport_ok'));totals['model_open_failure']+=not bool(call.get('transport_ok'))
            bygrade={(g['file'],g['row'],g['variant']):g for g in row.get('grades',[])}
            oldgrades={(g['file'],g['row'],g['variant']):g for g in old[key].get('grades',[])}
            failures=[];pos=[];oldpos=[];paired=[]
            for e in job['entries']:
                identity=(e['file'],e['row'],e['variant']);g=bygrade[identity];og=oldgrades[identity]
                errs=g.get('failures',[]);groups={bucket(str(e)) for e in errs};reasons.update(errs)
                for c in counts:
                    c['grades']+=1;c['strict_passed']+=bool(g['passed']);c['old_strict_passed']+=bool(og['passed']);c['protocol_only_grades']+=groups=={'protocol'}
                    for group in groups:c['failure_'+group]+=1
                ok,text_errors,positive=literal(e['case'],answer);oldok,_,_=literal(e['case'],before)
                if positive:
                    pos.append(bool(ok));oldpos.append(bool(oldok))
                    for c in counts:
                        c['positive_checked']+=1;c['positive_passed']+=bool(ok);c['old_positive_passed']+=bool(oldok)
                        c['positive_improved_grades']+=bool(ok and not oldok);c['positive_regressed_grades']+=bool(oldok and not ok)
                    if key in sample:
                        previous,_,_=literal(e['case'],sample[key]['answer'])
                        sample_totals['positive_checked']+=1;sample_totals['current_passed']+=bool(ok);sample_totals['r93_passed']+=bool(previous)
                        sample_totals['improved']+=bool(ok and not previous);sample_totals['regressed']+=bool(previous and not ok)
                if errs or text_errors:failures.append({'file':e['file'],'row':e['row'],'id':e['case'].get('id'),'strict_failures':errs,'text_failures':text_errors,'positive':positive,'passed':ok,'old_passed':oldok})
            for c in counts:
                if pos:c['positive_requests']+=1;c['all_positive_pass_requests']+=all(pos);c['old_all_positive_pass_requests']+=all(oldpos)
            summary={'key':key,'question':job['question'],'locale':lang,'domain':domain,'answer':answer,'old_answer':before,'mode':result.get('mode'),
                'path':art.get('task_flow'),'task_plan':plan.get('task_plan'),'query_plan':plan,'need_ledger':art.get('need_ledger'),
                'exception':row.get('exception'),'rejected_candidate':art.get('rejected_candidate'),'failures':failures,
                'positive_contracts':len(pos),'all_positive_pass':all(pos) if pos else None,'old_all_positive_pass':all(oldpos) if oldpos else None}
            f.write(json.dumps(summary,ensure_ascii=False)+'\n')
            if pos and all(oldpos) and not all(pos):regressions.append(summary)
            if pos and all(pos) and not all(oldpos):improvements.append(summary)
    assert seen==set(jobs) and totals['grades']==sum(len(j['entries']) for j in jobs.values())
    times.sort();pct=lambda x:times[int((len(times)-1)*x)]
    report={'coverage_complete':True,'requests':len(seen),'grades':totals['grades'],'llm_enabled':True,'format':'new_common_r95','totals':dict(totals),
        'by_requested_locale':{k:dict(v) for k,v in langs.items()},'by_domain':{k:dict(v) for k,v in domains.items()},'paths':dict(paths),'signals':dict(signals),
        'same_r93_sample':dict(sample_totals),'regressed_requests_vs_r88':len(regressions),'improved_requests_vs_r88':len(improvements),
        'timing':{'wall_sec':done['elapsed_sec'],'p50_sec':pct(.5),'p95_sec':pct(.95),'p99_sec':pct(.99),'max_sec':max(times)},
        'limitations':['Positive literal/clause checks do not establish full semantic accuracy.','Raw strict contracts include legacy protocol identifiers.','Controlled booking unavailable: no real occupancy oracle.','Reference clock 2026-10-16 with per-job overrides, not current live truth.','Full corpus contains single-turn requests; multi-turn fixtures reported separately.','Model response opened does not establish body/semantic success.']}
    for name,data in [('ANALYSIS_FINAL.json',report),('REGRESSIONS_VS_R88.json',regressions),('IMPROVEMENTS_VS_R88.json',improvements),('FAILURE_COUNTS.json',reasons.most_common())]:
        (out/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    t=totals
    lines=['# ผลทดสอบ Flow ใหม่ R95 / Common + LLM ON','',f'รันครบ {len(seen):,} request keys / {t["grades"]:,} grades ไม่รัน legacy หรือ common เก่าซ้ำ ใช้ผล R88 ที่เก็บไว้เปรียบเทียบ','',
        '## คะแนนและขอบเขต','',
        '- Positive text/clause contracts: **'+ratio(t['positive_passed'],t['positive_checked'])+'**; retained R88: '+ratio(t['old_positive_passed'],t['positive_checked']),
        '- Strict: '+ratio(t['strict_passed'],t['grades'])+'; protocol-only failures '+str(t['protocol_only_grades'])+' grades ไม่ใช่ semantic accuracy',
        f'- Execution exceptions {t["exceptions"]}; empty answers {t["empty_answers"]}; improved grades {t["positive_improved_grades"]}; regressed grades {t["positive_regressed_grades"]}',
        '- Requests ผ่านทุก positive contract ที่มี: '+ratio(t['all_positive_pass_requests'],t['positive_requests']),
        f'- Local-model HTTP attempts {t["model_http_attempts"]}, response opened {t["model_response_opened"]}, open failures {t["model_open_failure"]}; ไม่ใช้ transport เป็นความถูกต้องเนื้อหา','',
        '## แยกภาษา','', '| Locale | Requests | R95 positive | Retained R88 positive |','|---|---:|---:|---:|']
    for l,c in sorted(langs.items()):lines.append(f'| {l} | {c["requests"]} | {ratio(c["positive_passed"],c["positive_checked"])} | {ratio(c["old_positive_passed"],c["positive_checked"])} |')
    lines+=['','## เทียบกับ R93 บนคำถามเดียวกัน','',json.dumps(dict(sample_totals),ensure_ascii=False,indent=2),'','ตัวเลข cohort นี้แยกจาก full corpus ไม่เทียบคะแนน sample กับ full ตรง ๆ','',
        '## หมวดที่ยังไม่ผ่าน positive contracts','', '| Domain label | Requests | R95 | R88 |','|---|---:|---:|---:|']
    for d,c in sorted(domains.items(),key=lambda x:-(x[1]['positive_checked']-x[1]['positive_passed'])):
        if c['positive_checked']:lines.append(f'| {d.replace("|","/")} | {c["requests"]} | {ratio(c["positive_passed"],c["positive_checked"])} | {ratio(c["old_positive_passed"],c["positive_checked"])} |')
    lines+=['','## เส้นทางที่ใช้งานจริง','',json.dumps(dict(paths),ensure_ascii=False,indent=2),'','compatibility_common_domain หมายถึงยังใช้ parser เฉพาะหมวดของ common ผ่าน executor ร่วม ไม่อ้างว่าทุกหมวดถูกแทนด้วย semantic TaskPlan แล้ว','',
        '## ข้อจำกัด','',*[f'- {x}' for x in report['limitations']],'','รายละเอียดทุกคำถามอยู่ PER_REQUEST_ANALYSIS.jsonl พร้อม query plan, rejected candidate และผลตรวจดิบ การจัด semantic root causes ต้องอ่านสาระ/ต้นฉบับเพิ่ม ไม่เรียกทุก literal failure ว่าคำตอบผิดข้อเท็จจริง']
    (out/'FINAL_REPORT_TH.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'out':str(out),'requests':len(seen),'positive':ratio(t['positive_passed'],t['positive_checked']),'exceptions':t['exceptions'],'regressions':len(regressions),'timing':report['timing']},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
