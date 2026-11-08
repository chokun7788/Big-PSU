import sys,json,time,uuid,re,urllib.request,urllib.error
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r57_current_path.txt').read_text());OLD=BASE/'r54_shop_cases_20261009_235038';ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
LABEL=sys.argv[1];URL='http://127.0.0.1:8093'
facts=json.loads((ROOT/'data/curated/user_service_facts_20261008.json').read_text(encoding='utf-8'))
oldrows=json.loads((OLD/'responses.json').read_text(encoding='utf-8'))+json.loads((OLD/'extra_responses.json').read_text(encoding='utf-8'))
cases=[r['case'] for r in oldrows]
if len(sys.argv)>2:
    selected=set(sys.argv[2].split(','));scenarios={c.get('scenario') for c in cases if c['id'] in selected and c.get('scenario')}
    cases=[c for c in cases if c['id'] in selected or c.get('scenario') in scenarios]
extra_checks={
 'c018':['Nintendo Switch'],'c045':['Nintendo Switch'],'c046':['Nintendo Switch'],
 'c047':['รายชื่อ'],'c061':['140','120'], 'c062':['1 แพ็กเกจ','เหลือ 30'], 'c063':['PC','30 THB'],
 'c075':['Nintendo Switch Zone','17'], 'c078':['Gran Turismo 7'],'c080':['42'],
 'c097':['ยังไม่ได้ยืนยัน','Steam'],'c126':['PC #02','10:00'],
 'c128':['Monday','13:00'], 'c129':['Maintenance','13:00-16:00'], 'c131':['เสาร์','อาทิตย์'],
 'c132':['Building','09:00'], 'c133':['เลือก','ยืนยัน'], 'c135':['ธนาคาร','เงินสด','ยัง'],
 'c137':['1 แพ็กเกจ','เหลือ 30'], 'c138':['1 whole package','30 THB'], 'c140':['Left Mouse Button','R: Reload'],
 'c144':['i5-14400','32GB','5060'], 'c145':['สมาชิก','จอดรถ','บัตร'], 'c146':['membership','parking','ID'],
 'c151':['PC #01','PC #02','10:00','11:00'], 'c152':['VALORANT','140'], 'c153':['VALORANT','140'],
 'c155':['ดู','ยังไม่ได้ระบุ'],
}
def request(path,payload=None):
    req=urllib.request.Request(URL+path,data=json.dumps(payload,ensure_ascii=False).encode() if payload is not None else None,headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=35) as s:return s.status,json.load(s)
    except urllib.error.HTTPError as s:return s.code,json.load(s)
from r56_contracts import evaluate
contracts={c['id']:c for c in json.loads((OUT/'answer_contracts_v2.json').read_text(encoding='utf-8'))}
sessions={};ack={};rows=[]
health=request('/health')[1];assert health['runtime']['version'].startswith('2026.10.10-service-r57.');(OUT/(LABEL+'_health.json')).write_text(json.dumps(health,indent=2),encoding='utf-8')
def run(c):
    key=c.get('scenario') or c['id'];session=sessions.setdefault(key,'r55-'+uuid.uuid4().hex);start=time.perf_counter()
    status,job=request('/api/chat/jobs',dict(question=c['question'],locale=c['locale'],debug=True,experimental_rag_fallback=True,client_session_id=session,client_turn_id='r55-'+uuid.uuid4().hex,last_seen_response_id=ack.get(key,'')))
    if status==202:
        deadline=time.monotonic()+60
        while job['status'] in ('running','queued') and time.monotonic()<deadline:
            time.sleep(.15);_,job=request('/api/chat/jobs/'+job['job_id']+'?session_id='+session)
    result=job.get('result') or {};ack[key]=result.get('request_id','');answer=result.get('answer','');errors=[];checked=[]
    def require(ok,label):
        checked.append(label)
        if not ok:errors.append(label)
    require(job.get('status')=='completed','transport_complete')
    if c['id']=='c124':require(result.get('mode')=='pipeline:competition_rule_overview_source','broad_rules_need_overview')
    if c.get('claim'):
        canonical=facts['claims'][c['claim']]['answers'][c['locale']]
        require(re.sub(r'\s+','',canonical).casefold() in re.sub(r'\s+','',answer).casefold(),'owner_answer')
    e=c.get('expect') or {}
    for word in list(dict.fromkeys(e.get('contains',[])+extra_checks.get(c['id'],[]))):require(word.casefold() in answer.casefold(),'contains:'+word)
    for word in e.get('forbid',[]):require(word.casefold() not in answer.casefold(),'forbids:'+word)
    if e.get('not_general_model'):require('general_llm_direct' not in result.get('mode',''),'no_general_model')
    audit=evaluate(result,contracts[c['id']]);errors.extend(audit['errors'])
    row=dict(content_audit=audit,case=c,http_status=status,elapsed_sec=time.perf_counter()-start,job=job,checks=checked,errors=errors,verdict='FAIL' if errors else 'CHECKED' if len(checked)>1 else 'REVIEW',runtime=health['runtime']['version'])
    rows.append(row)
    with (OUT/(LABEL+'_raw.jsonl')).open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(c['id'],round(row['elapsed_sec'],2),result.get('mode'),row['verdict'],errors,flush=True)
    return row
for c in cases:run(c)
with (OUT/(LABEL+'.json')).open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print('CASES',len(rows),'FAIL',sum(bool(r['errors']) for r in rows),flush=True)
