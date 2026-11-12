# Workspace and preservation rules

- Work explicitly in `D:\CodexProjects\Big-PSU` for this project. Avoid creating new project artifacts on C:.
- Use the existing `origin` for `https://github.com/chokun7788/Big-PSU.git`. Do not push this project to PSU_SAVE or overwrite that repository.
- Preserve original owner data, approvals, frozen code, evaluation manifests, and raw results.
- Do not stop the protected model, use subagents, or rerun/regrade R132.
- Current flow work is `r135_recovery_loop_20261112`; its parent `r135_shared_contract_20261111`, earlier bounded/intent candidates, full R135 and measured evaluations are retained separately. Read `flow.md`, `STATUS.json`, `RESEARCH_AND_LOOP_PLAN_TH.md`, `LOOP01_REPORT_TH.md`, `LOOP01_MANIFEST.json`, and the latest `LOOP02_REPORT_TH.md`/`LOOP02_MANIFEST.json` before changing it. Saved-log analysis is in `r135_log_analysis_20261112/REPORT_TH.md`.
- Finish intent/output repairs and focused checks before a new full sample. The next full trial must be sequential, one question at a time.
- Keep `.local-private`, raw chat history, tokens, model weights, runtime databases/logs, and large raw evidence out of Git.
- Local data migration must be byte-verified before originals are removed. Never follow a junction into an unrelated project during recursive cleanup.
- User requests progress reports every six hours. State actual work, evidence, limits, and next steps without inventing completion percentages.
- The user-approved model-first experiment is `r135_model_first_20261112`; read its `MODEL_FIRST_REPORT_TH.md`, `STATUS.json`, `flow.md` and `IMPLEMENTATION_MANIFEST.json` before continuing. It is an experimental separate candidate, not a replacement for recovery-loop02. Actual base-profile model splits needs but has known intent/context/ambiguity errors. Keep failed evidence; do not treat source replay or mocked controls as model accuracy.
