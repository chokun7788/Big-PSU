from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r124_legacy_guided_parity_20261023'
for name in ['foundation','source_guards','live','exact_faq']:
 p=R/f'verify_{name}.py';assert not p.exists()
 text=(P/f'verify_{name}05.py').read_text('utf-8-sig').replace("S=R/'revision05_system'","S=R/'system'")
 text=text.replace("R/'ALL_RETAINED_JOBS.jsonl'","R.parent/'r124_legacy_guided_parity_20261023/ALL_RETAINED_JOBS.jsonl'")
 p.write_text(text,'utf8')
for filename in ['web_chat/index.html','web_chat/app.js']:
 p=R/'system'/filename;p.write_text(p.read_text('utf8').replace('R124','R125'),'utf8')
