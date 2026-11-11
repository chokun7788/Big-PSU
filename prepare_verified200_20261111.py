"""Freeze substantive source/scope changes for the exact previous 200 jobs."""
import hashlib,json,pathlib,shutil,sqlite3
R=pathlib.Path(__file__).resolve().parent
S=R/'r135_bounded_response_20261111'
D=R/'r135_verified_eval200_20261111'
assert not D.exists(),'Do not overwrite a measured run'
controls={'source_scope_lifecycle':S/'verified_sources_controls_1794393487397226300/RESULT.json',
          'currency_regression':S/'price_currency_1794393513035533100/RESULT.json',
          'bounded_regression':S/'bounded_response_1794393520199470300/RESULT.json'}
assert all(json.loads(p.read_text(encoding='utf-8'))['all_passed'] for p in controls.values())
D.mkdir()
shutil.copytree(S/'system',D/'system',ignore=shutil.ignore_patterns('__pycache__','*.sqlite','*.sqlite-*','owner-session.json'))
a=sqlite3.connect((S/'system/data/knowledge/verified_sources.sqlite').as_uri()+'?mode=ro',uri=True)
b=sqlite3.connect(D/'system/data/knowledge/evaluation_frozen.sqlite');a.backup(b);a.close();b.close()
O=D/'evaluation';O.mkdir()
prior=R/'r135_bounded_eval200_20261111/evaluation'
shutil.copyfile(prior/'SELECTED_JOBS.jsonl',O/'SELECTED_JOBS.jsonl')
launcher=(R/'r135_bounded_eval200_20261111/Start-Evaluation.ps1').read_text(encoding='utf-8-sig').replace('8138','8140').replace('R135-Bounded-eval200','R135-Verified-eval200')
(D/'Start-Evaluation.ps1').write_text(launcher,encoding='utf-8')
runner=(prior/'run_sequential.py').read_text(encoding='utf-8').replace('8138','8140').replace('R135-Bounded-eval200','R135-Verified-eval200')
runner=runner.replace("for p in sorted((R/'system/app').rglob('*')):","for p in sorted([*(R/'system/app').rglob('*'), R/'system/data/knowledge/verified_web_citations.json']):")
marker="code=fingerprint();source=epoch();identity=health['runtime']['installation_id']"
extra="""# Content checks are separate preflight requests, not part of the 200 grades.
for check_question,check_locale,expect in [('จองได้สูงสุดกี่รอบ','th','six'),('How many sessions can I book at Andaman Hotel?','en','foreign'),('PC นักศึกษา PSU ราคาเท่าไหร่','th','zero')]:
 _,_,p=ask(check_question,check_locale)
 with (O/'SOURCE_PREFLIGHT.jsonl').open('a',encoding='utf8') as pf:pf.write(json.dumps({'question':check_question,'response':p},ensure_ascii=False)+'\\n')
 assert p.get('ok')
 if expect=='six':assert '6 Sessions' in p.get('answer','') and any(s.get('url')=='https://esports.computing.psu.ac.th/' for s in p.get('sources',[]))
 if expect=='foreign':assert '6' not in p.get('answer','') and not p.get('sources') and 'place' in p.get('answer','')
 if expect=='zero':assert '0 บาท' in p.get('answer','')
dbhash=hashlib.sha256((R/'system/data/knowledge/evaluation_frozen.sqlite').read_bytes()).hexdigest()
"""
assert marker in runner
runner=runner.replace(marker,extra+marker)
runner=runner.replace("if epoch()!=source or fingerprint()!=code:raise RuntimeError('Final snapshot mismatch')", "if epoch()!=source or fingerprint()!=code or hashlib.sha256((R/'system/data/knowledge/evaluation_frozen.sqlite').read_bytes()).hexdigest()!=dbhash:raise RuntimeError('Final snapshot mismatch')")
(O/'run_sequential.py').write_text(runner,encoding='utf-8')
scorer=(prior/'score_compare.py').read_text(encoding='utf-8').replace("R/'r135_hybrid_eval10_20261110/evaluation/RESULTS.jsonl'","R/'r135_bounded_eval200_20261111/evaluation/RESULTS.jsonl'")
scorer=scorer.replace('bounded200','verified200').replace('previous_hybrid_same200','previous_bounded_same200').replace('ตัวจำกัดเวลา','ข้อมูลเว็บและขอบเขตใหม่').replace('Flow ผสมรอบก่อน','ตัวจำกัดเวลาก่อนแก้ข้อมูล')
(O/'score_compare.py').write_text(scorer,encoding='utf-8')
manifest={'jobs':200,'workers':1,'same_jobs_as':'r135_bounded_eval200_20261111','selection_sha256':hashlib.sha256((O/'SELECTED_JOBS.jsonl').read_bytes()).hexdigest(),
 'frozen_database_sha256':hashlib.sha256((D/'system/data/knowledge/evaluation_frozen.sqlite').read_bytes()).hexdigest(),
 'registry_sha256':hashlib.sha256((D/'system/data/knowledge/verified_web_citations.json').read_bytes()).hexdigest(),
 'focused_gates':{k:str(p.relative_to(R)) for k,p in controls.items()},
 'substantive_changes':['3 booking FAQ drafts 3->6 sessions from current official page','source-bound policy subject verification and wrong-location rejection','direct FAQ answer without awkward source-question heading'],
 'limits':['not a deployment or completed R135','same reviewed 200 regression questions, not an unseen semantic test','literal criteria may encode legacy policy; source correctness assessed separately','4 extra preflight HTTP requests excluded from 200 count','unread images/attachments remain unverified','cooperative time budget, not a hard deadline']}
(O/'PREPARED_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'directory':str(D),'manifest':manifest},ensure_ascii=False))
