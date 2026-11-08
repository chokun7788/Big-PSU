# Big-PSU — PSU Esports Studio Phuket Chatbot

Canonical local workspace: `D:\CodexProjects\Big-PSU`.

This repository preserves the project's code versions, plans, and summary reports.
It is a development archive, not a claim that every experimental flow is production-ready.

## Current work

- `PSU_Esports_Chat_Current_R134`: previous installed release, retained for comparison.
- `r135_complete_flow_audit_20261026`: full R135 76-requirement / 14-category candidate; unfinished.
- `r135_hybrid48_20261108`: experimental hybrid using R135 contracts and a bounded R134 compatibility reader.
- `r135_hybrid48_intent_round02_20261108`: current isolated intent/output repairs. Focused checks passed; full follow-up evaluation has not started.

The hybrid's completed 1,056-request evaluation matched 988 of 1,255 supported literal criteria.
267 literal criteria did not match, and 1,527 other criteria were outside that scorer.
These are not semantic correctness scores. Saved R134 comparisons have different clock/source/backend conditions.

## Local data retained outside Git

The complete local migration includes models, SQLite databases, runtime logs, raw evaluation evidence,
and historical artifacts. Those remain on D: and are excluded from Git, together with possible credentials,
generated dependencies, large raw files, and compiled binaries.

The private chat archive is `.local-private/chat-history/`. It contains four thread-history segments and
visible user/assistant exports; raw tool traces can contain secrets and must not be published.
Codex's own active conversation storage is managed by the app and is not relocated by editing its database.

Migration receipts, per-file SHA-256 verification, and private exclusion details are stored beside this
workspace in `D:\CodexProjects\_psu_migration_20261108`.

## Runtime

Existing application/test Python: `%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.
Existing model environment: `D:\CodexTraining\psu-r121-20261022\venv\Scripts\python.exe`.
Model weights remain in their existing local location; no weights are downloaded or trained by this migration.
Historical absolute C: paths may need the compatibility links described in the migration report.

Read the current candidate's status, focused evidence, and known limits before running a flow.
Do not restart frozen measurements, rewrite historical results, or treat HTTP success as answer correctness.
