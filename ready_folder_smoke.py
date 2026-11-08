from pathlib import Path
import json, time, urllib.request, uuid, sys

out = Path(__file__).parent / ('ready_folder_checks_' + time.strftime('%Y%m%d_%H%M%S'))
out.mkdir()
port = int(sys.argv[1])
def get(path):
    with urllib.request.urlopen(f'http://127.0.0.1:{port}{path}', timeout=10) as response:
        return json.load(response)
h = get('/health')
(out / 'health.json').write_text(json.dumps(h, ensure_ascii=False, indent=2), encoding='utf-8')
assert h['runtime']['version'] == '2026.10.03-ready-folder-r37.2'
assert h['warmup']['ok'] and h['llm_preflight']['ok']
assert all(w['ready'] and w['alive'] for w in h['pipeline_workers']['workers'])
rows = []
sessions = [('th', [('มีเกมอะไรให้แข่งมั่ง', 'catalog', ''), ('valorant', 'rules', 'valorant'), ('ขอกฏหนาอย', 'rules', 'valorant'), ('มีกฏอื่นไหม', 'rules', 'valorant')]),
            ('en', [('Which games have competition rules?', 'catalog', ''), ('VALORANT', 'rules', 'valorant'), ('Can I see the rules?', 'rules', 'valorant'), ('Any other rules?', 'rules', 'valorant')]),
            ('th', [('กฏตอนเเข่ง cs2 มีอะไรมั่ง', 'rules', 'cs2')])]
with (out / 'answers.jsonl').open('x', encoding='utf-8') as f:
    for locale, cases in sessions:
        history = []
        sid = 'ready-check-' + uuid.uuid4().hex
        for q, kind, game in cases:
            payload = dict(question=q, locale=locale, client_session_id=sid, recent_history=history[-10:], debug=True, experimental_rag_fallback=True)
            start = time.perf_counter()
            request = urllib.request.Request(f'http://127.0.0.1:{port}/api/chat', data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(request, timeout=35) as response:
                x = json.load(response)
            errors = []
            if not x.get('answer') or x.get('timed_out'): errors.append('empty_or_timeout')
            if kind == 'catalog' and x.get('route_intent') != 'competition_rulebook_catalog': errors.append('wrong_catalog_route')
            if kind == 'rules':
                if x.get('route_category') != 'competition_rules': errors.append('wrong_rules_category')
                if not x.get('sources') or not all('competition_rules_' + game + '_' in str(s.get('url','')) for s in x['sources']): errors.append('wrong_rulebook_source')
            row = dict(question=q, locale=locale, elapsed_sec=round(time.perf_counter()-start,3), result=x, errors=errors, passed=not errors)
            rows.append(row); f.write(json.dumps(row,ensure_ascii=False)+'\n'); f.flush()
            print(json.dumps({'q':q,'pass':not errors,'seconds':row['elapsed_sec'],'mode':x.get('mode'),'errors':errors},ensure_ascii=False),flush=True)
            history.extend([dict(role='user',text=q),dict(role='assistant',text=x['answer'],route_category=x.get('route_category'),route_intent=x.get('route_intent'),sources=x.get('sources',[]))])
summary = dict(total=len(rows),passed=sum(r['passed'] for r in rows),all_pass=all(r['passed'] for r in rows),results=str(out))
(out / 'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary),flush=True)
if not summary['all_pass']: raise SystemExit(1)
