# r21 Dashboard network recovery — 2026-10-01 (Asia/Bangkok)

## User-visible failure

Question from retained chat log: `ตนนี้ pc ว่างให้เล่นไหม`.
At 14:30:46 the chatbot returned `pipeline:live_booking_status_unavailable`.
Both local health endpoints were HTTP 200. The aggregate endpoint was also HTTP 200, but reported `source=sample_fallback`; it was not live booking evidence.

## Confirmed cause

A direct fetch using the same bundled Python and dashboard `read_url` failed for both WordPress CSV URLs with `URLError` / `WinError 10013` (socket access permissions).
After granting network permissions, both fetches succeeded (HTTP 200, text/csv). The existing Dashboard process still returned sample_fallback, showing that permissions granted to new commands did not change the already-running restricted process.
Verified old Dashboard identity: PID 13632, parent 38708, bundled Python running `server.py --no-browser --port 8091`. Parent command was this r21 package launcher at port 8090.
The first Stop-Process attempt failed without stopping the process. Rechecked identity and health; then stopped only that verified process and started Dashboard again with approved external network access (new PID 4708).
The chatbot and worker were not restarted. No runtime source, owner schedule, policy, or fixture was edited. Existing logs were kept; new recovery logs and test evidence have distinct filenames.

## Verified after recovery

- 14:36:24: aggregate endpoint `ok=true`, correct date 2026-10-01, `source=remote_csv_live`, 18 resources, `privacy=aggregate_only`.
- Exact Thai user question: `pipeline:live_booking_status_fast_path`, HTTP elapsed 1.260 sec, pipeline latency 1.1212 sec.
- English `Is PC available now?`: same live route, HTTP elapsed 0.289 sec, pipeline latency 0.2429 sec; reused the snapshot freshly fetched by the Thai request (10-sec cache).
- Snapshot at 14:36:50 reported PC 2/10 available: #05 and #09; other PC resources booked. These are time-specific WordPress-derived results, not a guarantee of current state after that time.
- This confirms successful source connection and emitted aggregate answers. Owner-side independent booking oracle verification remains deferred; it is not replaced by HTTP 200 or validation_ok.

## Evidence

- Original exchange retained in package `data/logs/web_chat_2026-10-01.jsonl`.
- `dashboard_recovery_api_3f5bdc46c1714fb7aa77bf1b827d15ad.json` — full synthetic TH/EN HTTP responses.
- `dashboard_network_recovery_25691001_143600_700_500dfcac.out.log` / `.err.log` — new server output. The 2569 prefix follows Windows Thai calendar filename formatting; incident date is Gregorian 2026-10-01.

## Remaining diagnostic wording gap

`app/booking/live_status.py` currently uses one generic Dashboard unavailable answer for multiple failures. In this incident the Dashboard process was reachable while its upstream live CSV retrieval was blocked. A future error-message improvement should distinguish process unavailable, upstream data unavailable/non-live, timeout, and invalid payload, without presenting sample/stale data as live. No such source patch was needed to recover this incident.
