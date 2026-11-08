from pathlib import Path
root=Path(__file__).parent
f=root/'r30_build_G6_analysis.py'
s=f.read_text(encoding='utf-8')
s=s.replace('Combined G5 complete sweep with G6 affected-competition replay; timestamps/latencies span both runs. LLM/semantic disabled, production input guard, controlled unavailable booking snapshot; no combined answer accuracy across duplicated/historical/weak corpora','All 20327 requests actually reexecuted in G6; verified key/grade/provenance audit saved separately. LLM/semantic disabled; server locale binding, direct pipeline, runtime guard short-circuit tested separately; controlled unavailable booking. No combined answer accuracy across duplicated/historical/weak corpora')
s=s.replace('ข้อผิดเพิ่มเติมที่แก้ G4/G6','ข้อผิดเพิ่มเติมที่แก้ G4/G5/G6')
s=s.replace('G6: restored enumerated roster topic','G5: restored enumerated roster topic')
s=s.replace('หลักฐานก่อน/หลังใน *_source_G6_results.jsonl และ Flow final','หลักฐานก่อน/หลังใน source fixtures และ Flow final; G6 เพิ่ม CS2 duration/venue จาก s08_c01')
s=s.replace('จึงแก้ G6 พร้อม regression tests','จึงแก้ G5 พร้อม regression tests')
s=s.replace('G6 ตรวจ accidental repeat','G5 ตรวจ accidental repeat')
s=s.replace('continued inputs 262 เคส','continued inputs 260 เคส')
f.write_text(s,encoding='utf-8',newline='\n')
f=root/'r30_finish_flow_G6.py';s=f.read_text(encoding='utf-8').replace('+- Strong','- Strong').replace('+- คู่','- คู่')
f.write_text(s,encoding='utf-8',newline='\n')
s=(root/'r30_idle_concurrency.py').read_text(encoding='utf-8').replace('r30-G5','r30-G6')
with (root/'r30_idle_concurrency_G6.py').open('x',encoding='utf-8') as out:out.write(s)
s=(root/'r30_http_G6.py').read_text(encoding='utf-8')
start=s.index('tasks=');end=s.index('counts=',start)
s=s[:start]+"tasks=[('source_G6',json.loads((r/'focused_fixture_G6_source.json').read_text(encoding='utf-8'))['cases']),('mixed_title8',json.loads((r/'mixed_title_fixture_G3.json').read_text(encoding='utf-8'))['cases'])]\n"+s[end:]
s+="\nwith (r/(run+'_summary.json')).open('x',encoding='utf-8') as out:json.dump({'url':base,'total':sum(v['total'] for v in counts.values()),'passed':sum(v['passed'] for v in counts.values()),'by_suite':counts,'scope':'post-release source/regression/guard and locale contracts; no occupancy oracle'},out,ensure_ascii=False,indent=2)\n"
with (root/'r30_post_release_G6.py').open('x',encoding='utf-8') as out:out.write(s)
print('Prepared reporting scope corrections and final verification runners; application source unchanged.')
