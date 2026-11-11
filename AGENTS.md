# Workspace and preservation rules

- Work explicitly in `D:\CodexProjects\Big-PSU` for this project. Avoid creating new project artifacts on C:.
- Use the existing `origin` for `https://github.com/chokun7788/Big-PSU.git`. Do not push this project to PSU_SAVE or overwrite that repository.
- Preserve original owner data, approvals, frozen code, evaluation manifests, and raw results.
- Do not stop the protected model, use subagents, or rerun/regrade R132.
- Current flow work is `r135_shared_contract_20261111`; its parent `r135_bounded_response_20261111`, earlier `r135_hybrid48_intent_round02_20261108`, full R135 and measured evaluations are retained separately. Read the current candidate's `flow.md`, `STATUS.json` and `IMPLEMENTATION_REPORT_TH.md` before changing it.
- Finish intent/output repairs and focused checks before a new full sample. The next full trial must be sequential, one question at a time.
- Keep `.local-private`, raw chat history, tokens, model weights, runtime databases/logs, and large raw evidence out of Git.
- Local data migration must be byte-verified before originals are removed. Never follow a junction into an unrelated project during recursive cleanup.
- User requests progress reports every six hours. State actual work, evidence, limits, and next steps without inventing completion percentages.
