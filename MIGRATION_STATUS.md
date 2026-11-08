# Migration status — 8 November 2026

Source: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2`

Destination: `D:\CodexProjects\Big-PSU`

## Completed

- Initial copy: approximately 66.36 GiB of project data.
- SHA-256 comparison of 206,824 selected file paths; identified differences were recopied and rechecked.
- Additional work-directory/long-path checks: 319 files.
- Private archive of this conversation: four segments and 3,576 visible user/assistant messages at capture.
- New Git repository initialized with `origin = https://github.com/chokun7788/Big-PSU.git`.
- Git selection follows the user's choice: code versions, plans, and summary reports. Models, databases,
  raw evidence, private chat archives, runtime logs, and generated dependencies stay local on D:.

## Read permissions resolved; eligible-folder cleanup completed

The user explicitly authorized repairing read access below:

`work\r30_test_dependencies`

An elevated, narrowly scoped helper granted Chokhun read access successfully. The subsequent
additional verification covered 541 files with zero blockers. Cleanup rechecked source and
destination bytes per folder before moving the C: original into staging, creating a compatibility
junction to D:, and removed that verified staging copy. **127 folders migrated successfully**;
all 127 compatibility links validated. C: free space after cleanup was approximately **64.5 GiB**.
The D: trial chat health check passed and protected model PID 26336 remained running.
See `ACTIVATION.json` and `MIGRATION_COMPLETION_RECEIPT.json` for actual results.

The protected model still uses `r129_full_plan_completion_20261024` and
`r135_hybrid48_20261108` on C:; retain those folders without stopping the model.
The old `conversation_reliability_implementation_20261005` contains junctions to the separate
Learn-LLM repository and is retained when the reparse-directory safety check fails.
Root-level files and the original `work` folder remain unless separately verified and migrated.

Private audit receipts are in `D:\CodexProjects\_psu_migration_20261108`:
`VERIFICATION.json`, `VERIFIED_FILES.jsonl`, `REPAIRED_FILES.json`, and `FINAL_COPY_CHECK.json`.

## Codex application state

The raw conversation is backed up privately on D:, but Codex still manages its live session storage.
This migration does not edit Codex's internal database or move unrelated chats. The thread's project
working-folder selection still needs to be switched to this D: folder through the app's normal project UI.
Until that selection changes, use the D: workspace explicitly for project work.
