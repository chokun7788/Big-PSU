# PSU Esports Studio Chatbot — P0 update (26 September 2026)

## Confirmed changes

- The user confirmed that **12:00–13:00 is never bookable**. Both the project Dashboard and the original Dashboard at `D:\Download New\booking_dashboard_v26_slot_balanced_layout\booking_dashboard_v26_slot_balanced_layout` now remove that hour from effective weekly and date override opening periods. Neither `center_schedule.json` was edited. The original D: `server.py` was backed up byte for byte in this task's `work/original_D_dashboard_server_before_lunch_20260926.py`; restart an already running original Dashboard to load the change.
- The user confirmed that a **30 minute VR reservation blocks its full hourly slot**. A 09:00–09:30 reservation makes 09:00–10:00 unavailable. The existing Dashboard behaviour was retained and a regression test was added.
- The Chatbot now parses compact Thai time such as `วันนี้ตอน10โมง PC1 ว่างไหม` as 10:00, and reads the `now` timestamp's hour correctly when a question does not specify a time. This prevents the system from checking an unrelated slot.
- When a requested zone has zero available resources, the Thai answer now explicitly says `ไม่ว่าง` and keeps the `0/1` count.
- The new owner review package has `Open-PSU-Esports-Background.cmd`. It starts the package Chatbot in the background, and the existing package launcher starts the package Dashboard at port 8091. Startup logs use unique filenames so older logs are retained. A local Dashboard health check identifies the package calendar contract and prevents silently accepting an older service on port 8091.

## Automated evidence

| Check | Result | What it establishes |
|---|---:|---|
| Focused regression suite | 80/80 | Routes, date/closure handling, compact Thai time, VR hourly block, lunch rules |
| Calendar boundary matrix | 20 cases in Thai and English | 11:59, 12:00, 12:30, 13:00, Maintenance, Friday, special closure, date override cases |
| Synthetic query oracle | 4/4 | PC1 booked at 10:00, PC2 free at 10:00, English PC1, VR 09:30 blocked |
| Packaged Dashboard HTTP with synthetic CSV | 7/7 | Health endpoint, local HTTP transport, aggregate payload, 10:00 and lunch status, VR hour block, omission of customer name |
| New ZIP | 630 entries, integrity valid | Source/package hashes match for key runtime files; no conversation logs in ZIP |
| Background launcher smoke | Passed with a dummy child process | Hidden process started and wrote a fresh startup log; full Ollama/Chatbot boot was not attempted |

Evidence: `p0_unittest_r2_20260926.txt`, `p0_boundary_matrix_lunch_fixed_20260926.json`, `p0_query_fixture_confirmed_final_20260926.json`, `p0_package_http_fixture_final_20260926.json` in this outputs folder.

These fixtures use deliberately synthetic bookings. They establish that the code answers known cases correctly. They **do not establish** that a real WordPress booking row, cancellation, or no-show is interpreted as the owner expects. The packaged HTTP test proves a local API request succeeds with synthetic CSV; it is separate from verifying a real live booking answer. The actual local 8091 service and owner booking CSV were not verified in this run.

## How to try this release

Unzip `owner_review_20260926_p0_final/PSU_Esports_Chatbot_Local.zip` (version `2026.09.26-owner-review-candidate-r2`) into a **new folder** on the owner machine. For the first run, use `Open-PSU-Esports-Chatbot.cmd` so setup errors remain visible. After local models are installed, `Open-PSU-Esports-Background.cmd` can start it without keeping the command window open. Open Chatbot at `http://127.0.0.1:8080/` and its Dashboard at `http://127.0.0.1:8091/`.

The original D: `start-dashboard.bat` also uses port 8080. Close that process before starting the package Chatbot. The original Dashboard and packaged Dashboard currently have identical schedule file hashes, but edits made later in one copy do not synchronize to the other. The new background command is manual; automatic launch at Windows sign-in is not installed. Windows Task Scheduler supports an at-logon trigger if the owner chooses that operating mode: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create>.

## Owner confirmation still needed

1. Which Dashboard directory should be the **single maintained schedule** on the owner machine: the original D: folder or the Dashboard inside the new package? Should approved schedule changes be copied to a new package during updates? Do not automatically overwrite either `center_schedule.json` or existing `data/logs`.
2. Provide at least three real, non-personal oracle rows: date, time, resource name, expected free/busy result from the reservation system, including one approved booking and one cancelled or no-show booking. Then compare the live API response **and** Chatbot answer for those exact rows. No customer name, email, phone, or booking token is needed.
3. If the process should start automatically after Windows sign-in, confirm that requirement and which owner Windows account will run it. The background command is already available without installing an automatic task.

This remains an **owner review candidate**. The package was built in a new directory and did not replace a previous owner package, schedule file, or log.
