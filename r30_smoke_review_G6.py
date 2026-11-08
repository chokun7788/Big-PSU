import json,re
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());runs=json.loads((r/'final_G6_smoke_all.json').read_text(encoding='utf-8'));rows=[]
for x in runs:
    if x['status']=='passed':continue
    log=Path(x['log']).read_text(encoding='utf-8',errors='replace');lines=log.splitlines();errors=[v for v in lines if re.match(r'^(?:AssertionError|\w+(?:\.\w+)*Error|FAILED|FAIL)',v)]
    diagnostic=(errors[-1] if errors else '\n'.join(lines[-8:]))
    if 'PipelineAnswer(' in diagnostic:diagnostic=diagnostic[:300]+' … (full PipelineAnswer/trace retained in log)'
    diagnostic=diagnostic[:1300]
    name=Path(x['file']).name
    known={
      'smoke_test_answer_pipeline.py':'Expecting a historical mode prefix does not establish incorrect CS2 roster content; retain the old grade and compare source/content separately.',
      'smoke_test_availability_policy_regressions.py':'Family-title ambiguity is now clarification instead of guessing a reservation service.',
      'smoke_test_bilingual_web_api.py':'503 under concurrent requests while machine loaded. Idle final check recorded separately; no evidence here identifies WordPress as cause.',
      'smoke_test_boundary_guard.py':'Current freshness_live_source_required behavior differs from assertion. Requires source/freshness policy review, not a declaration that stale live status is valid.',
      'smoke_test_english_draft_preview.py':'Approved source-bound competition overview now returned; historical draft/mode assertion differs. Does not prove every translated clause correct.',
      'smoke_test_game_catalog.py':'Expectation of bounded Local LLM review differs from deterministic catalog processing; examine actual source/answer independently.',
      'smoke_test_genre_alias_formatting.py':'Expected genre/title/bullet content is absent. Could be alias/normalization or presentation mismatch; not confirmed purely formatting.',
      'smoke_test_update.py':'Exact Thai phrase มหาลัยอื่น differs from full group label นักศึกษา-นักเรียนต่างสถาบัน; retained 25-baht PC source and grade. Verify group/amount/source rather than phrase only.'}
    rows.append({**x,'diagnostic_excerpt':diagnostic,'interpretation':known.get(name,'Baseline replay reproduces the failing file; exact content/control assumptions still require item-level source review. Do not label all assertions obsolete.'),'all_answers_correct':False})
with (r/'FINAL_G6_SMOKE_FAILURE_REVIEW.json').open('x',encoding='utf-8') as out:json.dump(rows,out,ensure_ascii=False,indent=2)
doc=['# Smoke ที่ไม่ผ่าน G6 — หลักฐานรายไฟล์','', '71/85 ไฟล์ผ่าน อีก 14 ไฟล์มี log ครบ แต่ไฟล์ที่หยุด assertion แรกไม่ได้แปลว่าคำถามถัดไปในไฟล์ถูกทั้งหมด','']
for x in rows:doc += ['## '+Path(x['file']).name,'','```text',x['diagnostic_excerpt'],'```','',x['interpretation'],'','Full log: '+x['log'],'']
with (r/'FINAL_G6_SMOKE_FAILURE_REVIEW_TH.md').open('x',encoding='utf-8') as out:out.write('\n'.join(doc)+'\n')
print(json.dumps({'failed_files':len(rows),'observations':'all raw grades retained'}))
