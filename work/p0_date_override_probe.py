"""In-memory owner Dashboard closure probe; never edits center_schedule.json."""

from __future__ import annotations

import copy
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from unittest.mock import patch


PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "p0_date_override_20260926.json"
sys.path.insert(0, str(PROJECT))

from app.booking.live_status import _snapshot_from_payload, render_live_booking_answer  # noqa: E402
from app.pipeline.bilingual_english import _answer_schedule  # noqa: E402
from app.pipeline.schemas import EntityBundle  # noqa: E402
from app.runtime.fast_answer import answer_schedule  # noqa: E402
from booking_dashboard import server  # noqa: E402


target = "2026-09-29"
schedule = copy.deepcopy(server.load_center_schedule())
schedule["dates"][target] = {"open": False, "open_periods": [], "reason": "Fixture event closure"}
with patch.object(server, "load_center_schedule", return_value=schedule), patch.object(
    server, "now_bangkok", return_value=datetime(2026, 9, 25, 8, 0)
):
    status = server.build_status(
        [], [{"id": "1", "name": "PC #01", "duration": "60"}], target,
        {"mode": "remote_csv_live", "appointments_meta": {"hash": "synthetic"}, "services_meta": {"hash": "synthetic"}},
    )
snapshot = _snapshot_from_payload(server.chatbot_status_payload(status))
th_live = render_live_booking_answer(f"PC #01 ว่างไหม {target} 13:00", snapshot, "th")
en_live = render_live_booking_answer(f"Is PC #01 free on {target} at 13:00?", snapshot, "en")
th_static = answer_schedule(f"{target} เปิดไหม", time.perf_counter())
en_static = _answer_schedule(f"Is the studio open on {target}?", EntityBundle())
if th_static is None or en_static is None:
    raise AssertionError("calendar handler did not answer the explicit date")
if status["center"]["source"] != "date_override" or status["center"]["open"]:
    raise AssertionError("Dashboard date override did not close the center")
if "ยังจองไม่ได้" not in th_live or "not bookable" not in en_live:
    raise AssertionError("live booking answer did not respect Dashboard closure")
if "เปิดให้เล่น" not in th_static.answer or "open for play" not in en_static.answer:
    raise AssertionError("expected static calendar discrepancy was not observed")
result = {
    "fixture_type": "in_memory_dashboard_date_override",
    "owner_confirmed": False,
    "owner_file_modified": False,
    "api_connected": False,
    "date": target,
    "dashboard_center_source": status["center"]["source"],
    "dashboard_center_open": status["center"]["open"],
    "dashboard_slot_13_status": next(slot["status"] for slot in status["services"][0]["slots"] if slot["start"] == "13:00"),
    "thai_live_answer": th_live,
    "english_live_answer": en_live,
    "thai_static_answer_first_line": th_static.answer.splitlines()[0],
    "english_static_answer_first_line": en_static.answer.splitlines()[0],
    "unresolved_owner_decision": "Which special-date source controls the static calendar and booking dashboard?",
}
with OUTPUT.open("x", encoding="utf-8") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(f"PASS date override contrast; wrote {OUTPUT}")
