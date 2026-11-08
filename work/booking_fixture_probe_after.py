"""Isolated, synthetic booking oracle probe; never calls the owner API."""

from __future__ import annotations

import json
import os
import sys
import hashlib
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(PROJECT))

from booking_dashboard import server  # noqa: E402
from app.booking import live_status  # noqa: E402


class Response:
    def __init__(self, data: bytes):
        self.data = data

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None

    def read(self, length):
        return self.data[:length]


# These expected outcomes are authored from the CSV rows below, separately
# from the implementation under test. They are not owner-confirmed bookings.
services_csv = "id,name,duration\n1,PC #01,60\n2,PC #02,60\n"
appointments_csv = (
    "id,service_id,day,time,duration,status,name\n"
    "1,1,2026-09-29,13:00,60,approved,Fixture Person A\n"
    "2,1,2026-09-29,14:00,60,cancelled,Fixture Person B\n"
    "3,2,2026-09-29,15:00,60,no-show,Fixture Person C\n"
)
schedule = server.default_center_schedule()
expected = {
    ("PC #01", "13:00"): ("busy", 1, 0, 0),
    ("PC #01", "14:00"): ("available", 0, 0, 1),
    ("PC #02", "13:00"): ("available", 0, 0, 1),
    ("PC #02", "15:00"): ("no_show", 1, 1, 0),
}

with patch.object(server, "load_center_schedule", return_value=schedule), patch.object(
    server, "now_bangkok", return_value=datetime(2026, 9, 28, 8, 0)
):
    status = server.build_status(
        server.parse_csv(appointments_csv),
        server.parse_csv(services_csv),
        "2026-09-29",
        {"mode": "remote_csv_live", "appointments_meta": {"hash": "synthetic"}, "services_meta": {"hash": "synthetic"}},
    )

slot_results = {}
for resource in status["services"]:
    for slot in resource["slots"]:
        key = (resource["name"], slot["start"])
        if key in expected:
            actual = (slot["status"], slot["booked_count"], slot["no_show_count"], slot["available_count"])
            slot_results["/".join(key)] = {"expected": expected[key], "actual": actual, "pass": actual == expected[key]}

payload = server.chatbot_status_payload(status)
serialized = json.dumps(payload, ensure_ascii=False)
privacy_pass = all(s not in serialized for s in ("Fixture Person", "customer", "appointment_id", "current_bookings", "today_bookings"))

os.environ["PSU_LIVE_BOOKING_ENABLED"] = "1"
os.environ["PSU_LIVE_BOOKING_CACHE_SEC"] = "0"
live_status.reset_live_booking_cache()
with patch.object(live_status, "urlopen", return_value=Response(serialized.encode("utf-8"))):
    snapshot = live_status.get_live_booking_status("2026-09-29")

answers = {}
for key, query, locale, expected_text in (
    ("th_booked", "PC #01 ว่างไหม 2026-09-29 13:00", "th", "ไม่ว่างตลอดช่วง 13:00-14:00"),
    ("en_booked", "Is PC #01 free on 2026-09-29 at 13:00?", "en", "not available for the full period 13:00-14:00"),
    ("th_cancelled_free", "PC #01 ว่างไหม 2026-09-29 14:00", "th", "ว่างตลอดช่วง 14:00-15:00"),
    ("en_cancelled_free", "Is PC #01 free on 2026-09-29 at 14:00?", "en", "available for the full period 14:00-15:00"),
    ("th_no_show_hold", "PC #02 ว่างไหม 2026-09-29 15:00", "th", "ไม่ว่างตลอดช่วง 15:00-16:00"),
    ("en_no_show_hold", "Is PC #02 free on 2026-09-29 at 15:00?", "en", "not available for the full period 15:00-16:00"),
):
    answer = live_status.render_live_booking_answer(query, snapshot, locale)
    answers[key] = {"pass": expected_text in answer, "body": answer.splitlines()[1] if len(answer.splitlines()) > 1 else answer}

result = {
    "fixture_type": "synthetic_csv_rows_with_independent_expected_outcomes",
    "project_file_sha256": {
        "dashboard_server": hashlib.sha256((PROJECT / "booking_dashboard" / "server.py").read_bytes()).hexdigest(),
        "chatbot_adapter": hashlib.sha256((PROJECT / "app" / "booking" / "live_status.py").read_bytes()).hexdigest(),
    },
    "owner_confirmed": False,
    "api_connection_tested": False,
    "adapter_accepted_aggregate_payload": snapshot.ok,
    "slot_results": slot_results,
    "answers": answers,
    "aggregate_privacy_pass": privacy_pass,
}

# Separate known-result edge: a 30-minute reservation cannot occupy the next
# half hour merely because the dashboard groups display slots by hour.
with patch.object(server, "load_center_schedule", return_value=schedule), patch.object(
    server, "now_bangkok", return_value=datetime(2026, 9, 28, 8, 0)
):
    short_status = server.build_status(
        server.parse_csv("id,service_id,day,time,duration,status\n9,8,2026-09-29,09:00,30,approved\n"),
        server.parse_csv("id,name,duration\n8,VR Station (Morning),30\n"),
        "2026-09-29",
        {"mode": "remote_csv_live", "appointments_meta": {"hash": "synthetic"}, "services_meta": {"hash": "synthetic"}},
    )
vr = short_status["services"][0]
hour_slot = next(slot for slot in vr["slots"] if slot["start"] == "09:00")
short_snapshot = live_status._snapshot_from_payload(server.chatbot_status_payload(short_status))
short_answer = live_status.render_live_booking_answer(
    "Is VR free on 2026-09-29 from 09:30 to 10:00?", short_snapshot, "en"
)
result["short_booking_gap"] = {
    "fixture_booking": "09:00-09:30",
    "independently_expected_0930_1000": "free_by_booked_interval",
    "dashboard_slot": {k: hour_slot[k] for k in ("start", "end", "status", "booked_count", "available_count")},
    "dashboard_marks_entire_hour_busy": hour_slot["status"] == "busy" and hour_slot["end"] == "10:00",
    "english_answer_body": short_answer.splitlines()[1] if len(short_answer.splitlines()) > 1 else short_answer,
}
with patch.object(server, "load_center_schedule", return_value=schedule), patch.object(
    server, "now_bangkok", return_value=datetime(2026, 9, 28, 8, 0)
):
    empty_status = server.build_status(
        [], [], "2026-09-29", {"mode": "remote_csv_live"}
    )
try:
    live_status._snapshot_from_payload(server.chatbot_status_payload(empty_status))
except ValueError as exc:
    empty_rejection = str(exc)
else:
    empty_rejection = ""
result["empty_remote_data_gap"] = {
    "synthetic_condition": "both HTTP CSV reads succeed but neither yields a service row",
    "dashboard_source": empty_status["source"],
    "adapter_ok": False if empty_rejection else True,
    "rejected_reason": empty_rejection,
    "resource_count": len(empty_status["services"]),
}
Path(__file__).with_name("booking_fixture_results_after_verified.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, ensure_ascii=False, indent=2))
assert len(slot_results) == len(expected)
assert all(x["pass"] for x in slot_results.values())
assert all(x["pass"] for x in answers.values())
assert snapshot.ok and privacy_pass
