import json,time,uuid,urllib.request,urllib.error,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(ROOT))
from app.pipeline.competition_targets import resolve_competition_targets
from app.pipeline.conversation_rules import rulebook_manifest
LABEL=sys.argv[1];URL='http://127.0.0.1:8093';rows=[];checks=[]
def req(path,data=None):
    r=urllib.request.Request(URL+path,data=json.dumps(data,ensure_ascii=False).encode() if data is not None else None,headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(r,timeout=35) as f:return json.load(f)
health=req('/health');assert health['runtime']['version'].startswith('2026.10.10-service-r56.')
for g in ('CS2','RoV','Tekken 8','VALORANT'):
    source,release=rulebook_manifest(resolve_competition_targets('rules '+g).targets[0]);expected={r['id'] for r in source}
    for locale in ('th','en'):
        session='r56-full-'+uuid.uuid4().hex;ack='';seen=set();errors=[];pages=0
        for page in range(20):
            q=(f'ขอกฎการแข่งขัน {g} ทั้งหมดทุกข้อ' if locale=='th' else f'Show all recorded competition rules for {g}.') if page==0 else ('ต่อ เอากฎที่เหลือ' if locale=='th' else 'Continue with the remaining rules.')
            start=time.perf_counter();job=req('/api/chat/jobs',dict(question=q,locale=locale,debug=True,experimental_rag_fallback=True,client_session_id=session,client_turn_id=uuid.uuid4().hex,last_seen_response_id=ack))
            limit=time.monotonic()+100
            while job.get('status') in ('queued','running') and time.monotonic()<limit:
                time.sleep(.15);job=req('/api/chat/jobs/'+job['job_id']+'?session_id='+session)
            result=job.get('result') or {};ack=result.get('request_id','');cov=result.get('rule_coverage') or {};returned=set(cov.get('returned_ids',[]));pages+=1
            row=dict(game=g,locale=locale,page=page,question=q,elapsed_sec=time.perf_counter()-start,job=job,runtime=health['runtime']['version']);rows.append(row)
            with (OUT/(LABEL+'_raw.jsonl')).open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
            if job.get('status')!='completed':errors.append('transport')
            if not returned:errors.append('no_sections_returned');break
            if set(cov.get('expected_ids',[]))!=expected:errors.append('source_ids_mismatch')
            if returned&seen:errors.append('repeated_sections')
            if not returned<=expected:errors.append('unknown_section')
            if cov.get('source_release')!=release:errors.append('source_release_mismatch')
            seen |= returned
            print(g,locale,page+1,len(seen),'/',len(expected),errors,flush=True)
            if seen==expected:break
        if seen!=expected:errors.append('incomplete')
        checks.append(dict(game=g,locale=locale,pages=pages,covered=len(seen),expected=len(expected),source_release=release,errors=errors))
with (OUT/(LABEL+'.json')).open('x',encoding='utf-8') as f:json.dump(dict(checks=checks,rows=rows,meaning='readable source section coverage; not approval of event policies or translations'),f,ensure_ascii=False,indent=2)
print('FAIL',sum(bool(c['errors']) for c in checks),flush=True)
