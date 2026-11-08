"""Exercise the adapter over a local synthetic HTTP server, not owner data."""

from __future__ import annotations

import json
import os
import sys
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse


PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "p0_http_fixture_20260926.json"
sys.path.insert(0, str(PROJECT))

from app.booking.live_status import get_live_booking_status, render_live_booking_answer, reset_live_booking_cache  # noqa: E402
from booking_dashboard import server as dashboard  # noqa: E402


target_date = "2026-09-29"
appointments = dashboard.parse_csv(
    "id,service_id,day,time,duration,status\n"
    "1,1,2026-09-29,13:00,60,approved\n"
)
services = dashboard.parse_csv("id,name,duration\n1,PC #01,60\n2,PC #02,60\n")
with patch.object(dashboard, "now_bangkok", return_value=datetime(2026, 9, 25, 8, 0)):
    status = dashboard.build_status(
        appointments, services, target_date,
        {"mode": "remote_csv_live", "appointments_meta": {"hash": "synthetic"}, "services_meta": {"hash": "synthetic"}},
    )
payload = dashboard.chatbot_status_payload(status)
request_dates: list[str] = []


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        request_dates.append(parse_qs(parsed.query).get("date", [""])[0])
        if parsed.path != "/api/chatbot-status":
            self.send_error(404)
            return
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
thread = threading.Thread(target=httpd.serve_forever, daemon=True)
thread.start()
try:
    with patch.dict(os.environ, {
        "PSU_LIVE_BOOKING_ENABLED": "1",
        "PSU_LIVE_BOOKING_CACHE_SEC": "0",
        "PSU_LIVE_BOOKING_STATUS_URL": f"http://127.0.0.1:{httpd.server_port}/api/chatbot-status",
    }):
        reset_live_booking_cache()
        snapshot = get_live_booking_status(target_date)
finally:
    httpd.shutdown()
    thread.join(timeout=3)
    httpd.server_close()

if not snapshot.ok or snapshot.date != target_date or request_dates != [target_date]:
    raise AssertionError((snapshot, request_dates))
answers = {
    "th_booked": render_live_booking_answer("PC #01 ว่างไหม 2026-09-29 13:00", snapshot, "th"),
    "en_booked": render_live_booking_answer("Is PC #01 free on 2026-09-29 at 13:00?", snapshot, "en"),
    "th_free": render_live_booking_answer("PC #02 ว่างไหม 2026-09-29 13:00", snapshot, "th"),
    "en_free": render_live_booking_answer("Is PC #02 free on 2026-09-29 at 13:00?", snapshot, "en"),
}
semantic = {
    "th_booked": "ไม่ว่าง" in answers["th_booked"],
    "en_booked": "not available" in answers["en_booked"],
    "th_free": "ว่าง" in answers["th_free"] and "ไม่ว่าง" not in answers["th_free"],
    "en_free": "is available" in answers["en_free"],
}
if not all(semantic.values()):
    raise AssertionError(answers)
result = {
    "fixture_type": "synthetic_loopback_http",
    "owner_confirmed": False,
    "real_dashboard_connected": False,
    "synthetic_http_connected": True,
    "requested_date": target_date,
    "returned_date": snapshot.date,
    "source_marker": snapshot.source,
    "resource_count": len(snapshot.resources),
    "semantic_expected_checks": semantic,
}
with OUTPUT.open("x", encoding="utf-8") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(f"PASS synthetic HTTP transport and {sum(semantic.values())}/{len(semantic)} semantic checks; wrote {OUTPUT}")
