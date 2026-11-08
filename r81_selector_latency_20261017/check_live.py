"""User-launched small HTTP validation. Loopback only; no configuration changes."""
import hashlib,importlib.util,json,os,time,uuid
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
spec=importlib.util.spec_from_file_location('r79_diagnostic',B.parent/'r79_connection_diagnostics_20261017/check_connection.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
http_json=helper.http_json

def fingerprint():
    files=[];digest=hashlib.sha256()
    for folder in ('app','web_chat'):
        files.extend(p for p in (S/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix in {'.py','.json','.js','.html','.css'})
    files.extend(S.glob('*.ps1'))
    for p in sorted(files):digest.update(p.relative_to(S).as_posix().encode());digest.update(p.read_bytes())
    return digest.hexdigest()

def verify_health(body,expected):
    if not isinstance(body,dict):return False
    runtime=body.get('runtime',{})
    identity=hashlib.sha256(os.path.normcase(os.path.realpath(S)).encode()).hexdigest()[:16]
    # Actual health exposes the loaded fingerprint in the top-level build.
    loaded=body.get('common_loaded_build',{}).get('loaded_source_sha256')
    return bool(runtime.get('installation_id')==identity and runtime.get('knowledge_profile')=='r69-migration-preview'
        and runtime.get('local_llm',{}).get('enabled') is True and loaded==expected)

CASES=[
 ('en-personal','en',[("Can I bring my own input peripheral?",'pending_fast'),('Yes, but it is my own keyboard.','personal'),('And my mouse?','personal')]),
 ('th-personal','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ใช่ แต่เป็นเมาส์ของผม','personal'),('คีย์บอร์ดด้วยได้ไหม','personal')]),
 ('en-correction','en',[('I attached incorrect proof of payment. How do I fix it?','pending'),('yes','slip')]),
 ('th-reject','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ไม่ใช่ครับ หมายถึงหลังจองต้องจ่ายภายในกี่นาที','deadline')]),
 ('en-extra','en',[("Can I bring my own input peripheral?",'pending_fast'),('Yes, but it is my wireless keyboard.','unconfirmed')]),
 ('th-open','th',[('วันนี้เปิดไหม','open_day')]),
 ('en-open','en',[('Is the studio open today?','open_day')]),
]

def grade(body,expect):
    if not isinstance(body,dict):return ['missing_json_response']
    p=(body.get('decision_artifact') or {}).get('query_plan') or {};a=body.get('answer','');errors=[]
    if body.get('validation_ok') is not True:errors.append('validation_not_ok')
    if not a.strip():errors.append('empty_answer')
    rid='migrated_owner_claim_personal_keyboard_mouse'
    ids=set(p.get('record_ids',[]))|{x['record_id'] for x in p.get('response_projection',[]) if x.get('fields') and x.get('record_id')}
    if expect in {'pending','pending_fast'}:
        if not (body.get('common_read_state') or {}).get('profile_confirmation'):errors.append('missing_topic_confirmation')
        audit=p.get('entity_selection') or {}
        # Only an all-profile candidate set qualifies for the narrow shortcut.
        # Mixed candidate sets retain inference; report it rather than grade
        # correct fallback clarification as an incorrect source answer.
        if audit.get('model_call_avoided') and audit.get('attempted') is not False:errors.append('inconsistent_selector_audit')
        if expect=='pending_fast' and (audit.get('model_call_avoided') is not True or audit.get('attempted') is not False):errors.append('eligible_confirmation_still_waited_for_model')
    if expect=='personal' and (rid not in ids or not any(s in a for s in ['ไม่อนุญาต','not allowed'])):errors.append('missing_source_personal_rule')
    if expect=='unconfirmed' and rid in ids:errors.append('uncovered_condition_answered_as_personal_rule')
    if expect=='slip' and ('procedure_wrong_slip' not in ids or 'facebook.com/psuesportsphuket' not in a):errors.append('missing_slip_procedure')
    if expect=='deadline' and ('10' not in a or '795-276244-1' in a):errors.append('wrong_payment_deadline_projection')
    if expect=='open_day' and (p.get('day_status') not in {'open','closed','unconfirmed'} or len(a)>160 or '\n' in a):errors.append('wrong_compact_opening_status')
    return errors

def main():
    out=B/'user_results'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]);out.mkdir(parents=True,exist_ok=False)
    rows=[];db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
    install=json.loads((B/'INSTALLATION.json').read_text(encoding='utf8'))
    installed=all(hashlib.sha256((S/name).read_bytes()).hexdigest()==digest for name,digest in install['installed_files'].items())
    expected=fingerprint();health=http_json('http://127.0.0.1:8115/health')
    helper.emit_json(out/'HEALTH.json',health)
    verified=installed and health['http_ok'] and verify_health(health.get('body'),expected)
    if verified:
        for case,lang,turns in CASES:
            sid='r81-'+uuid.uuid4().hex
            for q,expect in turns:
                response=http_json('http://127.0.0.1:8115/api/chat',payload={'question':q,'locale':lang,'client_session_id':sid,'client_turn_id':uuid.uuid4().hex,'debug':True},timeout=30)
                errors=grade(response.get('body'),expect) if response['http_ok'] else ['http_unavailable']
                row={'case':case,'locale':lang,'question':q,'expect':expect,'passed':not errors,'errors':errors,**response};rows.append(row)
                with (out/'TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
                print(json.dumps({'case':case,'passed':not errors,'seconds':response['elapsed_seconds']},ensure_ascii=False),flush=True)
                if not response['http_ok']:break
    else:print('Current R81 code / LLM ON could not be verified. Restart R78, then run this check again.',flush=True)
    counts={lang:{'count':sum(r['locale']==lang for r in rows),'passed':sum(r['locale']==lang and r['passed'] for r in rows)} for lang in ('th','en')}
    selector_failures=[]
    for row in rows:
        audit=((row.get('body') or {}).get('decision_artifact') or {}).get('query_plan',{}).get('entity_selection') or {}
        if audit.get('availability_failure'):selector_failures.append({'case':row['case'],'question':row['question'],'failure':audit['availability_failure'],'timing_ms':audit.get('timing_ms')})
    result={'loaded_r81_verified':bool(verified),'expected_loaded_source_sha256':expected,'count':len(rows),'passed':sum(r['passed'] for r in rows),'by_language':counts,'selector_failures_separate_from_answer_contracts':selector_failures,'database_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest(),'live_http_verified':bool(rows) and all(r['http_ok'] for r in rows),'general_model_accuracy_verified':False,'direct_model_generation_tested':False,'note':'Confirmation shortcuts should avoid model inference; these HTTP timings are not direct model generation timings.'}
    helper.emit_json(out/'RESULTS.json',result)
    (out/'SUMMARY.md').write_text('# R81 targeted live HTTP check\n\n```json\n'+json.dumps(result,ensure_ascii=False,indent=2)+'\n```\n\nFull questions, answers and selector audits: TURNS.jsonl. No full test was run.\n',encoding='utf8')
    print('Results saved: '+str(out),flush=True)
if __name__=='__main__':main()
