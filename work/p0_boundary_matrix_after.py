"""Read-only P0 boundary probe with synthetic services and no real booking calls."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from unittest.mock import patch


PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "p0_boundary_matrix_20260926.json"
sys.path.insert(0, str(PROJECT))

from app.booking.live_status import (  # noqa: E402
    _snapshot_from_payload,
    live_booking_calendar_conflict,
    render_live_booking_answer,
)
from app.calendar.service_calendar import current_service_slot  # noqa: E402
from booking_dashboard import server  # noqa: E402


dates = {
    "2026-09-28": {"day": "Monday", "calendar": {"11:59": "maintenance", "12:00": "outside_hours", "12:30": "outside_hours", "13:00": "open", "16:00": "outside_hours"}},
    "2026-09-29": {"day": "Tuesday", "calendar": {"11:59": "open", "12:00": "outside_hours", "12:30": "outside_hours", "13:00": "open", "16:00": "outside_hours"}},
    "2026-10-02": {"day": "Friday", "calendar": {"11:59": "open", "12:00": "outside_hours", "12:30": "outside_hours", "13:00": "maintenance", "16:00": "outside_hours"}},
    "2026-07-28": {"day": "recorded_special_closure", "calendar": {"11:59": "closed", "12:00": "closed", "12:30": "closed", "13:00": "closed", "16:00": "closed"}},
}
rows = []
for day, config in dates.items():
    with patch.object(server, "now_bangkok", return_value=datetime(2026, 7, 1, 8, 0)):
        dashboard_status = server.build_status(
            [],
            [{"id": "1", "name": "PC #01", "duration": "60"}],
            day,
            {"mode": "remote_csv_live", "appointments_meta": {"hash": "synthetic"}, "services_meta": {"hash": "synthetic"}},
        )
    snapshot = _snapshot_from_payload(server.chatbot_status_payload(dashboard_status))
    for at, expected_calendar in config["calendar"].items():
        current = current_service_slot(datetime.fromisoformat(f"{day}T{at}:00+07:00"))
        if current["status"] != expected_calendar:
            raise AssertionError((day, at, expected_calendar, current["status"]))
        matching = next((s for s in dashboard_status["services"][0]["slots"] if s["start"] <= at < s["end"]), None)
        texts = {}
        conflicts = {}
        for locale, question in (
            ("th", f"PC #01 ว่างไหม {day} {at}"),
            ("en", f"Is PC #01 free on {day} at {at}?"),
        ):
            conflicts[locale] = live_booking_calendar_conflict(question, snapshot)
            texts[locale] = render_live_booking_answer(question, snapshot, locale)
        expected_conflict = (
            (day in {"2026-09-28", "2026-09-29", "2026-10-02"} and at in {"12:00", "12:30"})
            or (day == "2026-07-28" and at != "16:00")
        )
        if expected_conflict:
            if not all(conflicts.values()):
                raise AssertionError((day, at, conflicts))
            if "ขัดกับ" not in texts["th"] or "disagree" not in texts["en"]:
                raise AssertionError((day, at, texts))
        rows.append({
            "date": day,
            "day": config["day"],
            "time": at,
            "calendar_status": current["status"],
            "dashboard_center_source": dashboard_status["center"]["source"],
            "dashboard_center_open": dashboard_status["center"]["open"],
            "dashboard_slot_status": matching["status"] if matching else None,
            "dashboard_slot_available_count": matching["available_count"] if matching else None,
            "th_conflict": conflicts["th"],
            "en_conflict": conflicts["en"],
            "th_answer": texts["th"],
            "en_answer": texts["en"],
        })

result = {
    "fixture_type": "synthetic_no_bookings_for_boundary_reconciliation",
    "owner_confirmed": False,
    "api_connected": False,
    "source_config_modified": False,
    "tested_cases": len(rows),
    "both_languages_per_case": True,
    "rows": rows,
}
with OUTPUT.open("x", encoding="utf-8") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(f"PASS {len(rows)} boundary rows in Thai and English; wrote {OUTPUT}")
