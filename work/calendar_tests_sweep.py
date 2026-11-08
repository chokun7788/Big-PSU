"""Read-only schedule comparison against the live source tree.

All synthetic overrides stay in memory. This script creates no project files.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import sys
import time
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


REPO = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(REPO))
from app.calendar import service_calendar as calendar  # noqa: E402
from app.pipeline import bilingual_english as english  # noqa: E402
from app.pipeline.schemas import EntityBundle  # noqa: E402
from app.runtime.fast_answer import answer_schedule  # noqa: E402

spec = importlib.util.spec_from_file_location("psu_booking_dashboard_server", REPO / "booking_dashboard" / "server.py")
assert spec and spec.loader
dashboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dashboard)


def service_slot(day: str, hhmm: str) -> dict:
    instant = datetime.fromisoformat(f"{day}T{hhmm}:00").replace(tzinfo=ZoneInfo("Asia/Bangkok"))
    result = calendar.current_service_slot(instant)
    return {"status": result["status"], "playable": result["playable"], "slot": result["slot"]["time_range"] if result["slot"] else None}


def dashboard_day(day: str) -> dict:
    result = dashboard.build_status([], [{"id": "1", "name": "Fixture PC #01", "duration": "60"}], day, {"mode": "synthetic_fixture"})
    return {"center_open": result["center"]["open"], "center_source": result["center"]["source"], "open_periods": result["center"]["open_periods"], "slots": {slot["start"]: slot["status"] for slot in result["services"][0]["slots"]}}


def main() -> None:
    values = {}
    for day in ["2026-09-28", "2026-09-29", "2026-10-02", "2026-07-28"]:
        values[day] = {
            "chatbot": {time_s: service_slot(day, time_s) for time_s in ["11:59", "12:00", "12:30", "12:59", "13:00", "15:59", "16:00"]},
            "dashboard": dashboard_day(day),
        }
    original_loader = dashboard.load_center_schedule
    config = copy.deepcopy(original_loader())
    config["dates"] = {"2026-09-28": {"open": False, "reason": "TEST CLOSED"}, "2026-10-02": {"open": True, "open_periods": [["10:00", "11:00"]], "reason": "TEST LIMITED"}}
    dashboard.load_center_schedule = lambda: config
    try:
        values["in_memory_date_override"] = {
            "closed_monday": dashboard_day("2026-09-28"),
            "limited_friday": dashboard_day("2026-10-02"),
        }
    finally:
        dashboard.load_center_schedule = original_loader

    os.environ["PSU_ESPORTS_TODAY"] = "2026-07-27"
    values["language_samples"] = {
        "th_tomorrow": answer_schedule("พรุ่งนี้เปิดไหม", time.perf_counter()).answer,
        "en_tomorrow": english._answer_schedule("Is the studio open tomorrow?", EntityBundle()).answer,
        "en_friday": english._answer_schedule("Is the studio open Friday?", EntityBundle()).answer,
        "th_friday": answer_schedule("วันศุกร์เปิดกี่โมง", time.perf_counter()).answer,
    }
    os.environ["PSU_ESPORTS_TODAY"] = "2026-10-12"
    values["public_holiday_without_service_closure"] = {
        "date": "2026-10-13",
        "closure_record": calendar.closure_for(date(2026, 10, 13)) is not None,
        "holiday_records": len(calendar.holidays_for_date(date(2026, 10, 13))),
        "th_tomorrow": answer_schedule("พรุ่งนี้เปิดไหม", time.perf_counter()).answer,
        "en_tomorrow": english._answer_schedule("Is the studio open tomorrow?", EntityBundle()).answer,
    }
    os.environ.pop("PSU_ESPORTS_TODAY", None)
    values["now_language_samples"] = {}
    for instant in ["2026-09-28T12:30:00+07:00", "2026-09-28T13:00:00+07:00", "2026-10-02T12:30:00+07:00", "2026-10-02T13:00:00+07:00", "2026-07-28T13:00:00+07:00"]:
        os.environ["PSU_ESPORTS_NOW"] = instant
        values["now_language_samples"][instant] = {
            "th": answer_schedule("ตอนนี้เล่นได้ไหม", time.perf_counter()).answer.split("\n")[0],
            "en": english._answer_schedule("Is the studio open now?", EntityBundle()).answer.split("\n")[0],
        }
    print(json.dumps(values, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
