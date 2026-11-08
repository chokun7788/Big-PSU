"""Focused release checks, preserving every request and response."""
import json, time, uuid, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
PORT = 8093
records, checks = [], []
def ask(q, session, locale, ack=''):
    payload = dict(question=q, client_session_id=session, client_turn_id=str(uuid.uuid4()), last_seen_response_id=ack, locale=locale, debug=True)
    started = time.perf_counter()
    request = urllib.request.Request(f'http://127.0.0.1:{PORT}/api/chat', data=json.dumps(payload, ensure_ascii=False).encode(), headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(request, timeout=40) as response:
        body = json.load(response)
    records.append(dict(payload=payload, response=body, elapsed_sec=round(time.perf_counter()-started, 4)))
    return body
def check(name, ok):
    checks.append(dict(name=name, passed=bool(ok)))

for locale, q, allq, rulesq, more in [
    ('th','ราคาการใช้บริการบุคคลภายนอก','ทั้งหมด','กติกาการแข่งขันทั้งหมด CS2','ต่อ'),
    ('en','Service prices for external users','all services','All detailed CS2 competition rules','continue')]:
    session = 'release-'+str(uuid.uuid4())
    pending = ask(q,session,locale)
    r = ask('PC',session,locale,pending.get('request_id',''))
    check(locale+'_pc',set(r.get('coverage',{}).get('returned_ids',[])) == {'pc:general_student','pc:general_adult'})
    session = 'release-'+str(uuid.uuid4())
    pending = ask(q,session,locale)
    r = ask(allq,session,locale,pending.get('request_id',''))
    check(locale+'_all',len(r.get('coverage',{}).get('returned_ids',[]))==14)
    session = 'release-'+str(uuid.uuid4())
    r = ask(rulesq,session,locale)
    first = set((r.get('rule_coverage') or {}).get('returned_ids',[]))
    r = ask(more,session,locale,r.get('request_id',''))
    second = set((r.get('rule_coverage') or {}).get('returned_ids',[]))
    check(locale+'_continue',bool(first) and bool(second) and not first.intersection(second))
    check(locale+'_ack', 'client_acknowledged' in (r.get('conversation_state') or {}).get('delivery',{}).values())

session='release-'+str(uuid.uuid4())
r=ask('Service prices for external users',session,'en')
r=ask("I'd like the cockpit rate instead",session,'en',r.get('request_id',''))
check('rephrased_price_retains_external',set(r.get('coverage',{}).get('returned_ids',[]))=={'cockpit:general_student','cockpit:general_adult'})
session='release-'+str(uuid.uuid4())
r=ask('Please show every section of the CS2 tournament rulebook',session,'en')
check('every_section_full_rules',(r.get('rule_coverage') or {}).get('detail_level')=='full_sections' and bool((r.get('rule_coverage') or {}).get('returned_ids')))

stamp=time.strftime('%H%M%S')
raw=HERE/f'final_package_requests_{stamp}.json'
raw.write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
summary=dict(runtime_version='2026.10.05-conversation-r38.4',port=PORT, requests=len(records), passed=sum(c['passed'] for c in checks),checks=checks,raw_file=raw.name)
(HERE/f'final_package_summary_{stamp}.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
if not all(c['passed'] for c in checks): raise SystemExit(1)
