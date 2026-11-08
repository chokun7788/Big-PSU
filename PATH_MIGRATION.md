# Current project paths

Canonical workspace: `D:\CodexProjects\Big-PSU`.

- `Open-Hybrid-Trial.cmd`: existing R135-Hybrid48 trial chat on port 8125.
- `Open-Hybrid-Data-Editor.cmd`: its D: database editor on port 8126.
- Intent repair work remains in `r135_hybrid48_intent_round02_20261108`; these launchers do not deploy that unfinished candidate.
- The trial's launch scripts derive code, database, state, and log paths from their location on D:.
- Three compatibility PowerShell launchers in the retained C: trial folder forward to their D: counterparts. Their originals are privately backed up in the migration audit folder.
- The candidate's notebook generator finds the copied `system` folder from the notebook working directory. Its deployment sync tool requires an explicit destination instead of writing into Learn-LLM by default.
- Windows fonts and the bundled Python runtime still reside on C: and retain their valid paths. Model weights use the existing D: training location.
- Historical reports, manifests, frozen evaluations, and old versions retain their recorded paths.
- The already-running protected model retains its original C: command line and receipt path until its normal future restart. Starting the model from the D: launcher next time selects the D: project paths; no running model was stopped for this migration.
- Existing `Open-Current-Chat.cmd` / `Open-Current-Data-Editor.cmd` still select R134 as before. Use the explicitly named Hybrid launchers for the hybrid trial.
