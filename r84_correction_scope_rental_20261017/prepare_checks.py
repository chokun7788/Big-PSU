from pathlib import Path
B=Path(__file__).resolve().parent
p=B/'live_candidate.py';s=p.read_text(encoding='utf8')
start=s.index('CASES=[');end=s.index('\nrows=[]',start)
s=s[:start]+'from contracts import CASES,check\n'+s[end:]
start=s.index("  ids=set(p.get");end=s.index('  model_errors=[]',start)
s=s[:start]+"  errors=check({'decision_artifact':r.decision_artifact,'common_read_state':state,'answer':r.answer,'validation_ok':r.validation.ok},expect)\n"+s[end:]
s=s.replace("B/'candidate/app/knowledge/common'","B/('before' if '--before' in sys.argv else 'candidate')/'app/knowledge/common'")
p.write_text(s,encoding='utf8')
p=B/'web_focused.py';s=p.read_text(encoding='utf8');start=s.index('tree=ast.parse(');end=s.index('\ndef main():',start)
s=s[:start]+'from contracts import CASES,check\n'+s[end:];s=s.replace("sid='r83-'","sid='r84-'");p.write_text(s,encoding='utf8')
print('Prepared focused runners')
