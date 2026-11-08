from pathlib import Path
BASE=Path(__file__).resolve().parent
t=(BASE/'r55_web_tests.py').read_text(encoding='utf-8').replace("BASE/'r55_current_path.txt'","BASE/'r56_current_path.txt'").replace("startswith('2026.10.10-service-r55.')","startswith('2026.10.10-service-r56.')")
t=t.replace('sessions={};ack={};rows=[]',"from r56_contracts import evaluate\ncontracts={c['id']:c for c in json.loads((OUT/'answer_contracts_v2.json').read_text(encoding='utf-8'))}\nsessions={};ack={};rows=[]")
t=t.replace("row=dict(case=c,http_status=status", "audit=evaluate(result,contracts[c['id']]);errors.extend(audit['errors'])\n    row=dict(content_audit=audit,case=c,http_status=status")
(BASE/'r56_web_all.py').write_text(t,encoding='utf-8')
print('r56_web_all.py created; old runner preserved')
