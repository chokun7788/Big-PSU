"""Probe only the aggregate-only local Dashboard endpoint."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen


OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "p0_api_probe_20260926.json"
URL = "http://127.0.0.1:8091/api/chatbot-status?date=2026-09-29"
result = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "endpoint": URL,
    "aggregate_only_endpoint": True,
    "connection_success": False,
    "payload_live_source": False,
    "semantic_oracle_verified": False,
}
try:
    with urlopen(URL, timeout=3) as response:
        payload = json.load(response)
    result.update({
        "connection_success": True,
        "http_ok": bool(payload.get("ok")),
        "payload_live_source": payload.get("source") == "remote_csv_live",
        "returned_date": payload.get("date"),
        "resource_count": len(payload.get("resources") or []),
        "center_source": (payload.get("center") or {}).get("source"),
        "generated_at": payload.get("generated_at"),
        "privacy_marker": payload.get("privacy"),
    })
except Exception as exc:
    result["error"] = f"{type(exc).__name__}: {exc}"
with OUTPUT.open("x", encoding="utf-8") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps(result, ensure_ascii=False))
