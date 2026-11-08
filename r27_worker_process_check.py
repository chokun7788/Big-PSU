import json, os, sys, time
from pathlib import Path

project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(project))
os.environ.update(PSU_PIPELINE_WORKER_RECYCLE_REQUESTS='3',PSU_PIPELINE_WORKER_WARMUP_EMBEDDING='0',PSU_PIPELINE_WORKER_WARMUP_LLM='0',PSU_SEMANTIC_RETRIEVAL='0',PSU_BILINGUAL_EN_ENABLED='1')
from app.web_api.pipeline_supervisor import PipelineWorkerSupervisor

def wait_ready(supervisor):
    for _ in range(120):
        health=supervisor.health()
        if health['workers'][0]['ready'] and health['workers'][0]['alive']:return health
        time.sleep(.1)
    raise AssertionError('worker did not become ready')

def main():
    report=Path(Path(__file__).with_name('r27_report_path.txt').read_text(encoding='utf-8').strip())
    supervisor=PipelineWorkerSupervisor(workers=1);records=[]
    try:
        supervisor.start();initial=wait_ready(supervisor)
        for index in range(24):
            call=supervisor.answer('กติกา CS2 ทีมหนึ่งมีผู้เล่นกี่คน',timeout_sec=5,experimental_allow_llm=False,experimental_rag_fallback=True,request_id='recycle-check-'+str(index),locale='th')
            record={'index':index,'status':call.status,'elapsed':call.elapsed_sec,'health':supervisor.health()};records.append(record)
            assert call.status=='ok',record
            time.sleep(.2)
        after=supervisor.health()
        assert after['workers'][0]['pid']!=initial['workers'][0]['pid'],'planned recycle did not happen'
        # Crash only the child created by this isolated test.
        active=supervisor._slots[0]
        active.process.terminate();active.process.join(timeout=1)
        crash=supervisor.answer('สมาชิกทีมมีใครบ้าง',timeout_sec=5,experimental_allow_llm=False,experimental_rag_fallback=False,request_id='crash-check')
        assert crash.status=='restarting',crash
        crash_replacement=wait_ready(supervisor)
        recovered=supervisor.answer('สมาชิกทีมมีใครบ้าง',timeout_sec=5,experimental_allow_llm=False,experimental_rag_fallback=False,request_id='crash-recovery')
        assert recovered.status=='ok',recovered
        result={'passed':True,'initial':initial,'requests':records,'after_recycle':after,'crash_status':crash.status,'crash_diagnostics':crash.diagnostics,'after_crash':crash_replacement,'recovery_status':recovered.status}
    finally:supervisor.shutdown()
    events=[json.loads(line) for line in Path(result['after_recycle']['performance']['path']).read_text(encoding='utf-8').splitlines()]
    result['recycle_events']=[e for e in events if e.get('event')=='worker_recycle']
    assert any(e['status']=='promoted' for e in result['recycle_events'])
    with (report/'verified_real_worker_process_check.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps({'passed':True,'requests':len(records),'recycle_promotions':sum(e['status']=='promoted' for e in result['recycle_events']),'crash_recovery':True}))
if __name__=='__main__':main()
