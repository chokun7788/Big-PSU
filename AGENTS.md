# Workspace and preservation rules

- Work explicitly in `D:\CodexProjects\Big-PSU` for this project. Avoid creating new project artifacts on C:.
- Use the existing `origin` for `https://github.com/chokun7788/Big-PSU.git`. Do not push this project to PSU_SAVE or overwrite that repository.
- Preserve original owner data, approvals, frozen code, evaluation manifests, and raw results.
- Do not stop the protected model, use subagents, or rerun/regrade R132.
- Current flow work is `r135_recovery_loop_20261112`; its parent `r135_shared_contract_20261111`, earlier bounded/intent candidates, full R135 and measured evaluations are retained separately. Read `flow.md`, `STATUS.json`, `RESEARCH_AND_LOOP_PLAN_TH.md`, `LOOP01_REPORT_TH.md` and `LOOP01_MANIFEST.json` before changing it. Saved-log analysis is in `r135_log_analysis_20261112/REPORT_TH.md`.
- Finish intent/output repairs and focused checks before a new full sample. The next full trial must be sequential, one question at a time.
- Keep `.local-private`, raw chat history, tokens, model weights, runtime databases/logs, and large raw evidence out of Git.
- Local data migration must be byte-verified before originals are removed. Never follow a junction into an unrelated project during recursive cleanup.
- User requests progress reports every six hours. State actual work, evidence, limits, and next steps without inventing completion percentages.
