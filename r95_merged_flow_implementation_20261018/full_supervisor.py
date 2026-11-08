"""Run the approved new-common/LLM-ON full suite once, then analyze outputs.

Uses frozen app/data hashes, exclusive new logs, and explicit completion
markers. A completed run can contain failed answers; coverage is not accuracy.
"""
import datetime,hashlib,json,os,subprocess,sys,time,traceback
from pathlib import Path
R=Path(__file__).resolve().parent

def now():return datetime.datetime.now().astimezone().isoformat()
def hashes():
    return {p.relative_to(R/'system').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith(('.pyc','-wal','-shm'))}

def main():
    event_path=R/'SUPERVISOR_EVENTS.jsonl'
    if event_path.exists() or (R/'full01').exists():raise RuntimeError('Existing full run preserved; do not start a duplicate')
    events=event_path.open('x',encoding='utf-8');state={'started_at':now(),'pid':os.getpid(),'scope':'new_common_r95_llm_on_only','status':'preparing'}
    def update(**fields):
        state.update(fields,updated_at=now());events.write(json.dumps(state,ensure_ascii=False)+'\n');events.flush()
        tmp=R/'SUPERVISOR_STATUS.new.json';tmp.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8');os.replace(tmp,R/'SUPERVISOR_STATUS.json')
        print(json.dumps(state,ensure_ascii=False),flush=True)
    try:
        gate=json.loads((R/'release_gate/RESULT.json').read_text(encoding='utf-8'))
        assert gate['checks']==20 and gate['passed']==20 and gate['llm_enabled']
        jobs=[json.loads(x) for x in (R/'FULL_JOBS.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
        keys=[j['key'] for j in jobs];grades=sum(len(j['entries']) for j in jobs)
        assert len(keys)==len(set(keys))==20554 and grades==55811
        frozen=hashes();(R/'FULL_SOURCE_MANIFEST.json').write_text(json.dumps(frozen,ensure_ascii=False,indent=2),encoding='utf-8')
        config={'created_at':now(),'requests':20554,'grades':55811,'format':'common_r95','llm_enabled':True,'workers':4,'shared_model_slots':1,
            'reference_clock':'2026-10-16T12:00:00+07:00; per-job date overrides','booking':'controlled unavailable; not live occupancy validation',
            'history_population':sum(bool(j.get('history')) for j in jobs),'frozen_files':len(frozen),'jobs_sha256':hashlib.sha256((R/'FULL_JOBS.jsonl').read_bytes()).hexdigest(),
            'database_sha256':frozen['data/knowledge/common.sqlite'],'existing_results_not_rerun':True,'production_installation_changed':False}
        (R/'FULL_CONFIG.json').write_text(json.dumps(config,ensure_ascii=False,indent=2),encoding='utf-8')
        del jobs,keys
        env={**os.environ,'PYTHONUTF8':'1','PYTHONDONTWRITEBYTECODE':'1'}
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0)
        with (R/'FULL_RUN_STDOUT.log').open('x',encoding='utf-8') as log,(R/'FULL_RUN_STDERR.log').open('x',encoding='utf-8') as err:
            child=subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'run_common.py'),'--jobs',str(R/'FULL_JOBS.jsonl'),'--workers','4','--tag','full01'],cwd=R,env=env,stdout=log,stderr=err,creationflags=creationflags)
            update(status='running',runner_pid=child.pid,expected_requests=20554,expected_grades=55811)
            while child.poll() is None:
                time.sleep(20)
                progress=R/'full01/PROGRESS.json'
                if progress.exists():
                    try:p=json.loads(progress.read_text(encoding='utf-8'))
                    except (OSError,ValueError):continue
                    update(progress=p)
            code=child.returncode
        done=json.loads((R/'full01/RUN_FINISHED.json').read_text(encoding='utf-8'))
        if code or not done.get('coverage_complete') or done['completed']!=20554 or done['grades']!=55811:
            raise RuntimeError('Full coverage incomplete; preserved all first-run logs; no automatic answer retries')
        unchanged=hashes()==frozen
        if not unchanged:raise RuntimeError('Frozen app/data changed during full test; results require investigation')
        update(status='analyzing',progress=done,source_unchanged=True)
        with (R/'FULL_ANALYSIS_STDOUT.log').open('x',encoding='utf-8') as log,(R/'FULL_ANALYSIS_STDERR.log').open('x',encoding='utf-8') as err:
            code=subprocess.call([sys.executable,'-B','-X','utf8',str(R/'analyze_run.py'),'--run','full01','--jobs','FULL_JOBS.jsonl','--out','full_analysis'],cwd=R,env=env,stdout=log,stderr=err,creationflags=creationflags)
        if code:raise RuntimeError('Full execution finished but analysis failed; see retained analysis stderr')
        analysis=json.loads((R/'full_analysis/ANALYSIS_FINAL.json').read_text(encoding='utf-8'))
        assert analysis['coverage_complete'] and analysis['requests']==20554 and analysis['grades']==55811
        complete={'completed_at':now(),'coverage_complete':True,'requests':20554,'grades':55811,'format':'common_r95','llm_enabled':True,
            'source_unchanged':True,'all_answers_correct':False,'accuracy_requires_reading_metrics_and_failure_analysis':True,
            'report':str(R/'full_analysis/FINAL_REPORT_TH.md'),'analysis':str(R/'full_analysis/ANALYSIS_FINAL.json'),'totals':analysis['totals'],
            'by_requested_locale':analysis['by_requested_locale'],'same_r93_sample':analysis['same_r93_sample']}
        (R/'FULL_TEST_COMPLETE.json').write_text(json.dumps(complete,ensure_ascii=False,indent=2),encoding='utf-8')
        update(status='completed',completion=complete)
        return 0
    except BaseException as e:
        with (R/'SUPERVISOR_FAILURE.log').open('x',encoding='utf-8') as f:f.write(traceback.format_exc())
        update(status='failed',error_type=type(e).__name__,error=str(e));return 1
    finally:events.close()

if __name__=='__main__':raise SystemExit(main())
