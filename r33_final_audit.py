import json,hashlib,urllib.request
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');W=Path(__file__).parent;R=Path((W/'r33_report_path.txt').read_text().strip())
for f in (R/'FINAL_RESULTS_TH.md',):
 s=f.read_text(encoding='utf-8');old='94 เกี่ยวกับการนำอุปกรณ์ส่วนตัวที่ไม่มีนโยบายทั่วไป, 2 unknown English identity, 3 holiday-date/multi-zone price clarifications'
 assert s.count(old)==1
 f.write_text(s.replace(old,'94 เกี่ยวกับการนำอุปกรณ์ส่วนตัวที่ไม่มีนโยบายทั่วไป, 2 RoV catalog absence ที่เกณฑ์เก่ายังคาด answer_available, 3 holiday-date/multi-zone price clarifications'),encoding='utf-8')
g=json.loads((R/'final_G_runtime_freeze.json').read_text());i=json.loads((R/'final_I_runtime_freeze.json').read_text());diff=[k for k,v in i['manifest'].items() if g['manifest'].get(k)!=v]
assert diff==['app/pipeline/closed_query_improvements.py']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert all(sha(P/k)==v for k,v in i['manifest'].items())
health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=10))
assert health['runtime']['version']=='2026.10.02-usable-task-frames-r33' and all(w['alive'] and w['ready'] for w in health['pipeline_workers']['workers'])
audit=dict(runtime_changes_G_to_I=diff,project_runtime_matches_freeze=len(i['manifest']),health=health,public_url='http://127.0.0.1:8090/',source_review_new_failed_grade_counts={'missing_general_peripheral_policy':94,'RoV_absence_old_status':2,'holiday_date_clarification':2,'multi_zone_price_clarification':1},no_fresh_final_I_full_sweep_claim=True)
with (R/'FINAL_RELEASE_AUDIT.json').open('x',encoding='utf-8') as f:json.dump(audit,f,ensure_ascii=False,indent=2)
handoff=f'''# ส่งต่องาน PSU Esports Chatbot r33 finalI

Report: `{R}`
Flow: `{P/'docs/134_usable_task_frames_r33_verified_flow_20261002.md'}`
Package: `{P/'owner_local_delivery_20261002_usable_task_frames_r33_finalI/PSU_Esports_Chatbot_Local'}`
Production: http://127.0.0.1:8090/ launcher PID 40340; record `web_chat_runs/r33_ready_8090_123587b876.json`
Runtime version `2026.10.02-usable-task-frames-r33`

## ตรวจแล้ว

- unit 472/472, usage HTTP 56/56, source 30/30, partial 8/8, edition24/24
- G 937 HTTP complete935/937 (2 old partial status expectations); I differs only closed_query_improvements contact source lookup and tests
- fullD20,327/55,583, replayG7,177; H compound corpus selector0; I verified new contact source mapping with unit and actual HTTP. Composite not fresh finalI full sweep
- typo v2 clean/noisy1760/2000 each; clean-pass/noisy-fail9 vsr32 107. Positive contracts894 only
- source/Gold584hashes unchanged; existingtests145files unchanged; runtime/UI129package hashes match
- release literal9/10 with ราคา vs ค่าบริการ lexical miss; clean control exact/source sidecar reviewed10/10. Never hide original failed literal result
- helper concurrency8090 and8091 10/10 each

## ต่อจากนี้

อ่าน FINAL_RESULTS_TH.md / FLOW_R33_FINAL_TH.md / REMAINING_9_SOURCE_REVIEW.jsonl / ALL_REMAINING_FAILURE_TRIAGE.jsonl ก่อนแก้
4 actionable noise errors: จอสอบถาม preface changes validator equipment frame despite PC+VR price source; จ่ายเงินยังไงตอนของ loses booking cue; คำพูไดม่เหมาะสม corrupts negation; อ้างอิงติกา...จำนวยผู้เล่น loses competition operations
Other5 are valid-word ambiguity/truncated identity; don't force pay/rice/march/embers or guessed identity to match Gold
Owner questions: GENERAL peripheral policy; media; Tekken pause conflict; RoV6.1.5.1 incomplete; edition/entryfee/age/roster; English identity; translation/controller verification
REAL BOOKING OCCUPANCY COLLECTION STILL PAUSED. No booking mutations authorized. Synthetic31/31 doesn't establish real statuses

## 保存 / process / dependencies

Keep all dirty Git/code/owner data/old packages/logs/results; no reset/stash/delete/commit. Before432files in report and manifests; notecode includes changes frompriorchat
Test-only dependencies `work/r33_test_dependencies`; run complete unit runner with require_escalated because files have OWNER RIGHTS ACL. No runtime dependency change
E/G contact caused worker restarts; H HTTP run interrupted/overlapped I traffic, not a clean regression score. All raw retained
Project write grant is turn-scoped; request via system on next turn if needed
Test8091 finalI PID39376 should be stopped only after exact commandline/port ownership checks; production8090 kept for user
'''
with (W/'PSU_ESPORTS_R33_HANDOFF_FINAL_20261002.md').open('x',encoding='utf-8') as f:f.write(handoff)
print(dict(version=health['runtime']['version'],ready=True,changed_G_to_I=diff,handoff=str(W/'PSU_ESPORTS_R33_HANDOFF_FINAL_20261002.md')))
