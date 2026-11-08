import json,hashlib,urllib.request,collections,re,subprocess
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r32_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
load=lambda n:json.loads((R/n).read_text(encoding='utf-8'));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
scopes=[('candidate6','full initial sweep',20327),('candidate7_replay','all bilingual pairs and competition/named-game contexts',8526),('final10_replay','every source-detail no-answer/rejected no-answer trace; no old corpus query contains a standalone Gregorian year',17),('final12_replay','same 17 source-gap/no-answer queries after age partial fix',17),('final13_replay','every recorded registered-facet recovery overlapping และ/กับ/and; same-facet conjunction-bound rescore',3)]
execution=[]
for tag,scope,n in scopes:
 name=tag+'_all_results.jsonl' if tag=='candidate6' else tag+'_results.jsonl'
 execution.append(dict(run=tag,scope=scope,executions=n,results_file=name,results_sha256=sha(R/name)))
with (R/'FINAL_EXECUTION_SCOPE.json').open('x',encoding='utf-8') as f:json.dump(dict(runtime='2026.10.02-source-content-reliability-r32',final_package='owner_local_delivery_20261002_source_content_reliability_r32_final13/PSU_Esports_Chatbot_Local',scope='Full C6 plus affected replays; not a fresh full final13 run. Query pipeline labels retained from scripts have the actual scopes listed here. HTTP final13 937 requests ran fresh separately.',runs=execution,final_results_sha256=sha(R/'final13_all_results.jsonl'),known_artifact_errors=['Copied early HTTP summary labels r31; actual health and package confirm r32. See API_EXECUTION_PROVENANCE_FINAL13.json.','C12 merge completed full results and summary before failing to exclusively create a changes sidecar whose copied filename already existed. Whole result count/identities were verified by the full comparison.','Some replay provenance text copied the source-abstention wording to the conjunction-only run; use explicit scopes/keys above.']),f,ensure_ascii=False,indent=2)
h=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=10));assert h['runtime']['version']=='2026.10.02-source-content-reliability-r32'
assets=[]
for name in ['index.html','app.js','chat_request.js']:
 raw=urllib.request.urlopen('http://127.0.0.1:8090/'+name,timeout=10).read();assert raw==(P/'web_chat'/name).read_bytes();assets.append(dict(file=name,sha256=hashlib.sha256(raw).hexdigest(),matches_project=True))
unit=load('final13_unit_all.json');assert unit['success'] and unit['tests']==464
positive=load('release8090_final13_positive_http_summary.json');year=load('release8090_final13_edition_http_summary.json');partial=load('release8090_final13_partial_http_summary.json');burst=load('release8090_final13_cold_browser_helper_concurrency.json')
assert (positive['passed'],year['passed'],partial['passed'],burst['passed'])==(30,24,8,10)
protected=load('protected_manifest.json');assert all(sha(P/k)==v for k,v in protected.items())
before=load('before_manifest.json');tests=[k for k in before if k.startswith('tests/')];assert all(sha(P/k)==before[k] for k in tests)
freeze=load('final13_runtime_freeze.json');pack=P/'owner_local_delivery_20261002_source_content_reliability_r32_final13/PSU_Esports_Chatbot_Local'
assert all(sha(P/k)==v and sha(pack/k)==v for k,v in freeze['manifest'].items())
api=load('api8091_final13_http_summary.json');api_total=sum(x['total'] for x in api['by_suite'].values());api_pass=sum(x['passed'] for x in api['by_suite'].values());assert (api_total,api_pass)==(937,935)
record=dict(health=h,web_url='http://127.0.0.1:8090/',launcher_record=str(ROOT/'web_chat_runs/r32_ready_8090_dccd2b12eb.json'),static_assets=assets,unit=dict(total=464,passed=464),postrelease_source=dict(total=30,passed=30),postrelease_editions=dict(total=24,passed=24),postrelease_partial=dict(total=8,passed=8),postrelease_burst=dict(total=10,passed=10,retries=burst['retries'],elapsed_ms=[x['elapsed_ms'] for x in burst['rows']]),http_frozen=dict(total=api_total,passed=api_pass,status_differences=2),protected_hashes_verified=len(protected),preexisting_test_files_unchanged=len(tests),package_runtime_hashes_match=len(freeze['manifest']),real_occupancy_verified=False,owner_policy_confirmed=False)
with (R/'RELEASE_FINAL13_VERIFICATION.json').open('x',encoding='utf-8') as f:json.dump(record,f,ensure_ascii=False,indent=2)
# Correct own new document after checking source text and final outcomes.
docs=[P/'docs/133_all_remaining_r32_verified_flow_20261002.md',R/'FLOW_FINAL.md',R/'FINAL_RESULTS_TH.md']
for path in docs:
 text=path.read_text(encoding='utf-8');text=text.replace('REMAINING_107_ANALYSIS_TH.md','REMAINING_107_FINAL13_ANALYSIS_TH.md').replace('OWNER_QUESTIONS_TH.md','OWNER_QUESTIONS_FINAL_TH.md')
 text=text.replace('C13 รันซ้ำเก็บผลแยก','C13 935/937 (สองข้อคาด no_answer เดิมแต่ตอบ partial ที่มีหลักฐาน)')
 text=text.replace('หลัง deploy รุ่นสุดท้ายตรวจซ้ำและเก็บผลแยก','หลัง deploy final13 ผ่าน 24/24')
 if path.name=='FINAL_RESULTS_TH.md':
  text+='\n## ตรวจหลังเปิดเว็บ final13\n\nพอร์ต 8090: source 30/30, partial 8/8, explicit editions 24/24 และสิบคำถามพร้อมกันผ่าน 10/10 โดยมี retry รวม 8 ครั้ง (1.31–4.83 วินาทีในชุดนี้) ไฟล์หน้าเว็บสามไฟล์ตรง hash ของโครงการ/แพ็กเกจ ไม่ใช่ผลวัดการจอง WordPress จริง\n\nAPI เกณฑ์เดิม 935/937; strong composition/content/new questions 726/728 โดยสอง status differences เป็น eligibility + minimum age ที่อธิบายไว้ ไม่เรียก 728/728 บนรุ่นนี้\n\nExtra corpus C7: diverse 97/184, legacy rules 0/228, challenger v2 194/369, challenger v1 43/80; อีก 120 rows เป็น observations ไม่มี human oracle จึงไม่สรุปว่าตอบถูก 120/120 ดู candidate7_extra_results.jsonl สำหรับคำตอบและเหตุผล grade ทุกข้อ\n'
  assert 'ข้อ RoV 6.1.1 ฉบับเต็ม' not in text
 with (R/('docs_review_before_'+path.name)).open('x',encoding='utf-8') as f:f.write(path.read_text(encoding='utf-8'))
 path.write_text(text,encoding='utf-8')
handoff=f'''# R32 completed local development and verified release — 2026-10-02

Project: {P}
Report directory: {R}
Flow: {P/'docs/133_all_remaining_r32_verified_flow_20261002.md'}
Final report: {R/'FINAL_RESULTS_TH.md'}

Actual 8090 launcher PID 21556, exact package final13, record web_chat_runs/r32_ready_8090_dccd2b12eb.json. Runtime version 2026.10.02-source-content-reliability-r32; version alone does not distinguish candidate packages, use package paths and manifest.
Actual test 8091 final13 PID 23968 should be stopped by closeout, inspect owned identity before acting. Do not stop any unrelated process. Logs/packages preserved.

464/464 units; API final13 935/937 with two intentional frozen no_answer-to-source-partial differences, strong 726/728. Independent source/partial 38/38, explicit editions 24/24, postrelease cold retry-helper 10/10 (8 retries). Known booking synthetic31/31; actual occupancy collection paused by user. Twelve sessions24turns all pass. Existing C7 smoke71/85, extra970/981, nativeguard500 exactflags471; no claim of all semantic correctness.

Full corpus20327/55583 is C6 full + C7 replay8526 + C10 source-abstention17 + C12 source-gap17 + C13 conjunction3. Final legacy passed51983,failedunique1898,newfailedgrades2 explained independently. Same-v2 paired2000:clean1772,noisy1676,regression107 (TH54/EN53),positive894. Remaining42positive failures and65no-positive-oracle pairs; full per-case final13 analysis saved. Trace grouping:71task/facet,19person/role,7content,9status/other,1valid-wordambiguity; inferred categories not owner adjudication.

Runtime changed12 files including new competition_facet_recovery, request contracts, source-gap/year/partial guard, answer-type recognition, server retryable503/backlog16, web retry helper. No worker increase. English builder frozen-reference compatibility six metadata rows plus new current reference overlay. Saved booking oracle checker requires snapshot SHA,+07time, confirmer, exact date/resource/slot; pending templateV2 fixes SHA field.

584protected hashes and140preexisting tests unchanged;423before snapshots; no reset/stash/commit. New data/results were exclusive files. No initial all-log hash manifest exists, don't claim cryptographic verification of every historical log. r31 and intermediate packages/logs preserved. Some old runner summary/provenance labels were copied; explicit FINAL_EXECUTION_SCOPE and API_EXECUTION_PROVENANCE_FINAL13 resolve actual scopes. C12 merge sidecar filename collision happened AFTER complete result/summary writing and count validation; preserved, final13 merge clean.

Owner questions: Tekkenpause conflicting source/penalty; RoV6.1.5.1 truncated s08_c01; actual event edition validity; entryfees/minage/registered-roster; photo/video policy; translation policy review. Englishhash103/104 is not human approval. Do not infer missing policy. Actual booking collection remains paused until user resumes.

Next technical order is in final Flow:42positive failures with source/content adjudication; task/person cues with protected identities;65independent contentoracles; native repeat FN27/FP2; sustained load when needed. Do not increase aliases/thresholds just to make frozen tests pass. Review full appendix before new changes.
'''
with (ROOT/'R32_SESSION_HANDOFF_20261002_FINAL13.md').open('x',encoding='utf-8') as f:f.write(handoff)
print(json.dumps({'postrelease_passed':72,'protected':len(protected),'tests_unchanged':len(tests),'runtime_files_verified':len(freeze['manifest']),'http_passed':api_pass,'documents_updated':len(docs)},ensure_ascii=False),flush=True)
