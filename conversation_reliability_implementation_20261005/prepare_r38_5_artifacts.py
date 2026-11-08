from pathlib import Path
import runpy
HERE=Path(__file__).parent.resolve()
s=(HERE/'finalize_r38_4.py').read_text(encoding='utf-8').replace('r38_4','r38_5').replace('r38.4','r38.5')
f=HERE/'finalize_r38_5.py'
with f.open('x',encoding='utf-8') as stream:stream.write(s)
runpy.run_path(str(f),run_name='__main__')
h=(HERE/'extracted_holdout_check_r38_4.py').read_text(encoding='utf-8').replace('r38_4','r38_5').replace('r38.4','r38.5')
h=h.replace("    rows.append(dict(question=q,locale=locale,answer=r['answer'] if r else None,passed=bool(r and r['trace'][0].metadata.get('returned_ids'))))", "    result=answer(q,locale=locale,experimental_allow_llm=False)\n    rows.append(dict(question=q,locale=locale,answer=result.answer,mode=result.mode,passed=bool(r and r['trace'][0].metadata.get('returned_ids') and result.route.category=='competition_rules' and any(t.stage=='competition_full_coverage' for t in result.trace))))")
f=HERE/'extracted_holdout_check_r38_5.py'
with f.open('x',encoding='utf-8') as stream:stream.write(h)
runpy.run_path(str(f),run_name='__main__')
a=(HERE/'final_package_check_r38_4.py').read_text(encoding='utf-8').replace('r38.4','r38.5')
with (HERE/'final_package_check_r38_5.py').open('x',encoding='utf-8') as stream:stream.write(a)
