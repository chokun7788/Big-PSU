from pathlib import Path
source=Path('r31_http_B.py').read_text(encoding='utf-8').replace('import sys,os,json,','import re,sys,os,json,',1)
start=source.index('counts=')
source=source[:start]+"tasks=[(suite,[c for c in cases if suite in ('compound18','r31_source') or re.search(r'cs2|counter|เคาน|pause|timeout|หยุด|เวลานอก',c['question'],re.I)]) for suite,cases in tasks]\ntasks=[(suite,cases) for suite,cases in tasks if cases]\n"+source[start:]
with Path('r31_http_C.py').open('x',encoding='utf-8') as out:out.write(source)
