"""Synthetic oracle for direct station questions and confirmed hourly VR blocking."""

import json
import sys
from datetime import date, datetime
from pathlib import Path
from unittest.mock import patch


PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "p0_query_fixture_confirmed_final_20260926.json"
sys.path.insert(0, str(PROJECT))

from app.booking import live_status
from app.runtime.fast_answer import answer_live_booking_status
from booking_dashboard import server


services = server.parse_csv(
    "id,name,duration\n1,PC #01,60\n2,PC #02,60\n3,VR Station (Morning),30\n"
)
appointments = server.parse_csv(
    "id,service_id,day,time,duration,status\n"
    "1,1,2026-09-29,10:00,60,approved\n"
    "2,3,2026-09-29,09:00,30,approved\n"
)
with patch.object(server, "load_center_schedule", return_value=server.default_center_schedule()), patch.object(
    server, "now_bangkok", return_value=datetime(2026, 9, 29, 8, 0)
):
    status = server.build_status(
        appointments, services, "2026-09-29",
        {"mode": "remote_csv_live", "appointments_meta": {"hash": "synthetic"}, "services_meta": {"hash": "synthetic"}},
    )

snapshot = live_status._snapshot_from_payload(server.chatbot_status_payload(status))
resource_slots = {
    resource.resource_name: {slot.start: {"status": slot.status, "available_count": slot.available_count}
                             for slot in resource.slots}
    for resource in snapshot.resources
}
with patch.object(live_status, "today_bangkok", return_value=date(2026, 9, 29)), patch(
    "app.runtime.fast_answer.get_live_booking_status", return_value=snapshot
):
    th_busy = answer_live_booking_status("วันนี้ตอน10โมง PC1 ว่างไหม", 0.0)
    th_free = answer_live_booking_status("วันนี้ตอน10โมง PC2 ว่างไหม", 0.0)
    th_vr = answer_live_booking_status("วันนี้ตอน9โมงครึ่ง VR ว่างไหม", 0.0)

assert th_busy is not None and th_free is not None and th_vr is not None
en_busy = live_status.render_live_booking_answer("Is PC1 free today at 10am?", snapshot, "en")
en_vr = live_status.render_live_booking_answer("Is VR free today from 09:30 to 10:00?", snapshot, "en")
expected = {
    "pc1_10_busy": resource_slots["PC #01"]["10:00"]["status"] == "busy" and "PC #01 ไม่ว่างตลอดช่วง 10:00-11:00" in th_busy.answer,
    "pc2_10_free": resource_slots["PC #02"]["10:00"]["status"] == "available" and "PC #02 ว่างตลอดช่วง 10:00-11:00" in th_free.answer,
    "pc1_10_en_busy": "PC #01 is not available for the full period 10:00-11:00" in en_busy,
    "vr_0930_blocked_full_hour": resource_slots["VR Station (Morning)"]["09:00"]["status"] == "busy" and "ไม่ว่างตลอดช่วง 09:00-10:00" in th_vr.answer and "0/1" in th_vr.answer and "0/1" in en_vr,
}
result = {
    "fixture_type": "synthetic_csv_known_result",
    "owner_confirmed": False,
    "real_api_connected": False,
    "vr_policy_confirmed_by_user": "09:00-09:30 blocks 09:00-10:00",
    "expected_checks": expected,
    "answers": {
        "thai_pc1_10": th_busy.answer,
        "thai_pc2_10": th_free.answer,
        "english_pc1_10": en_busy,
        "thai_vr_0930": th_vr.answer,
        "english_vr_0930": en_vr,
    },
}
OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{sum(expected.values())}/{len(expected)} semantic checks; wrote {OUTPUT}")
assert all(expected.values()), expected
