"""Exercise the packaged Dashboard HTTP handler and Chatbot adapter with synthetic CSV."""

import json
import os
import sys
import threading
from datetime import datetime
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "outputs" / "owner_review_20260926_p0_final" / "PSU_Esports_Chatbot_Local"
OUTPUT = ROOT / "outputs" / "p0_package_http_fixture_final_20260926.json"
sys.path.insert(0, str(PACKAGE))

from app.booking import live_status
from booking_dashboard import server


appointments = (
    "id,service_id,day,time,duration,status,name\n"
    "1,1,2026-09-29,10:00,60,approved,Synthetic Person\n"
    "2,3,2026-09-29,09:00,30,approved,Synthetic Person\n"
)
services = "id,name,duration\n1,PC #01,60\n2,PC #02,60\n3,VR Station (Morning),30\n"
diag = {"mode": "remote_csv_live", "appointments_meta": {"hash": "synthetic"}, "services_meta": {"hash": "synthetic"}}

with patch.object(server, "fetch_csv_pair", return_value=(appointments, services, diag)), patch.object(
    server, "now_bangkok", return_value=datetime(2026, 9, 29, 8, 0)
):
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
    worker = threading.Thread(target=httpd.serve_forever, daemon=True)
    worker.start()
    try:
        with urlopen(f"http://127.0.0.1:{httpd.server_port}/health", timeout=3) as response:
            health = json.load(response)
        with patch.dict(os.environ, {
            "PSU_LIVE_BOOKING_ENABLED": "1",
            "PSU_LIVE_BOOKING_CACHE_SEC": "0",
            "PSU_LIVE_BOOKING_STATUS_URL": f"http://127.0.0.1:{httpd.server_port}/api/chatbot-status",
        }):
            live_status.reset_live_booking_cache()
            snapshot = live_status.get_live_booking_status("2026-09-29")
    finally:
        httpd.shutdown()
        worker.join(timeout=3)
        httpd.server_close()

public = snapshot.as_public_dict()
payload_text = json.dumps(public, ensure_ascii=False)
by_name = {r.resource_name: r for r in snapshot.resources}
slots = {name: {s.start: s for s in resource.slots} for name, resource in by_name.items()}
checks = {
    "http_dashboard_health": health.get("service") == "psu-booking-dashboard" and health.get("calendar_contract") == "lunch-closed-v1",
    "http_adapter_connected": snapshot.ok and snapshot.source == "remote_csv_live",
    "owner_data_not_exposed": "Synthetic Person" not in payload_text,
    "pc1_10_busy": slots["PC #01"]["10:00"].status == "busy",
    "pc2_10_free": slots["PC #02"]["10:00"].status == "available",
    "lunch_closed": slots["PC #01"]["12:00"].status == "closed",
    "vr_0930_full_hour_block": slots["VR Station (Morning)"]["09:00"].status == "busy" and slots["VR Station (Morning)"]["09:00"].end == "10:00",
}
result = {
    "fixture_type": "packaged_dashboard_real_http_handler_with_synthetic_csv",
    "real_owner_api_connected": False,
    "owner_confirmed_rows": False,
    "checks": checks,
}
with OUTPUT.open("x", encoding="utf-8") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(f"{sum(checks.values())}/{len(checks)} packaged HTTP checks; wrote {OUTPUT}")
assert all(checks.values()), checks
