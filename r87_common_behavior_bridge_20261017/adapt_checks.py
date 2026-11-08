from pathlib import Path
B=Path(__file__).resolve().parent
for name in ['live_candidate.py','web_focused.py']:
 p=B/name;s=p.read_text(encoding='utf8').replace("sid='r84-'","sid='r87-'")
 p.write_text(s,encoding='utf8')
print('Prepared targeted common/LLM ON runners')
