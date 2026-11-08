"""End-to-end read-only booking latency probe using the packaged runtime."""

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "outputs/owner_review_20260926_english_reference_r3/PSU_Esports_Chatbot_Local"
OUTPUT = ROOT / "outputs/booking_latency_on_this_machine_20260926.json"
RUN = ROOT / "work" / ("booking_latency_probe_" + datetime.now().strftime("%Y%m%d_%H%M%S_%f"))
RUN.mkdir(parents=True, exist_ok=False)
PYTHON = sys.executable
DASHBOARD_PORT = 8095
CHATBOT_PORT = 8096
DATE = "2026-09-28"
QUESTION = "28 กันยายน 2026 เวลา 10:00 PC1 ว่างไหม"


def request_json(url: str, *, body: dict | None = None, timeout: float = 20) -> tuple[dict, float]:
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    headers = {"Accept": "application/json"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method="POST" if body is not None else "GET")
    start = time.perf_counter()
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload, round((time.perf_counter() - start) * 1000, 1)


def ready(url: str, *, service: str, process: subprocess.Popen, seconds: float = 45) -> dict:
    until = time.monotonic() + seconds
    while time.monotonic() < until:
        if process.poll() is not None:
            raise RuntimeError(f"{service} exited during startup with code {process.returncode}")
        try:
            payload, _ = request_json(url, timeout=1)
            if payload.get("service") == service:
                return payload
        except (OSError, ValueError, urllib.error.URLError):
            pass
        time.sleep(0.25)
    raise TimeoutError(f"{service} did not become ready")


def start(command: list[str], *, cwd: Path, env: dict, name: str) -> tuple[subprocess.Popen, list]:
    out = (RUN / f"{name}.out.log").open("x", encoding="utf-8")
    err = (RUN / f"{name}.err.log").open("x", encoding="utf-8")
    flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    proc = subprocess.Popen(command, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                            stdout=out, stderr=err, creationflags=flags)
    return proc, [out, err]


def stop(process: subprocess.Popen) -> None:
    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)


env = os.environ.copy()
env["PYTHONDONTWRITEBYTECODE"] = "1"
env["PSU_LIVE_BOOKING_ENABLED"] = "1"
env["PSU_LIVE_BOOKING_STATUS_URL"] = f"http://127.0.0.1:{DASHBOARD_PORT}/api/chatbot-status"
env["PSU_LIVE_BOOKING_TIMEOUT_SEC"] = "5"
env["PSU_LIVE_BOOKING_CACHE_SEC"] = "10"
env["PSU_PIPELINE_WORKER_SUPERVISOR"] = "0"
env["PSU_PIPELINE_WARMUP"] = "0"
env["PSU_LLM_PREFLIGHT"] = "0"
env["PSU_CHAT_LOG_DIR"] = str(RUN / "chat_logs")
env["PSU_CHAT_LOG_SQLITE_PATH"] = str(RUN / "chat_logs" / "chat_history.sqlite3")
dashboard = chatbot = None
handles = []
result = {
    "machine_test": True,
    "tested_at_local": datetime.now().astimezone().isoformat(),
    "package_version": "2026.09.26-owner-review-candidate-r3",
    "question": QUESTION,
    "date": DATE,
    "temporary_ports": {"dashboard": DASHBOARD_PORT, "chatbot": CHATBOT_PORT},
    "test_configuration": {
        "booking_cache_seconds": 10,
        "dashboard_timeout_seconds": 5,
        "startup_warmup": False,
        "llm_preflight": False,
        "worker_supervisor": False,
        "reason": "isolated temporary servers; live booking route itself is unchanged",
    },
    "results": [],
    "contains_customer_data": False,
}
try:
    dashboard, open_handles = start([PYTHON, "server.py", "--no-browser", "--port", str(DASHBOARD_PORT)],
                                     cwd=PACKAGE / "booking_dashboard", env=env, name="dashboard")
    handles.extend(open_handles)
    health = ready(f"http://127.0.0.1:{DASHBOARD_PORT}/health", service="psu-booking-dashboard", process=dashboard)
    print("Dashboard ready", flush=True)
    result["dashboard_calendar_contract"] = health.get("calendar_contract")

    status, elapsed = request_json(f"http://127.0.0.1:{DASHBOARD_PORT}/api/chatbot-status?date={DATE}")
    result["dashboard_direct"] = {
        "elapsed_ms": elapsed,
        "ok": status.get("ok"),
        "source": status.get("source"),
        "resources_count": len(status.get("resources") or []),
        "privacy": status.get("privacy"),
    }
    print(f"Dashboard direct: {elapsed} ms, source={status.get('source')}", flush=True)

    chatbot, open_handles = start([PYTHON, "-m", "app.web_api.server", "--host", "127.0.0.1", "--port", str(CHATBOT_PORT)],
                                   cwd=PACKAGE, env=env, name="chatbot")
    handles.extend(open_handles)
    ready(f"http://127.0.0.1:{CHATBOT_PORT}/health", service="psu-esports-chat-web", process=chatbot, seconds=90)
    print("Chatbot ready", flush=True)

    url = f"http://127.0.0.1:{CHATBOT_PORT}/api/chat"
    for label in ("fresh_after_start", "repeat_within_cache", "fresh_after_cache_expired"):
        if label == "fresh_after_cache_expired":
            print("Waiting 11 seconds for the booking cache to expire", flush=True)
            time.sleep(11)
        payload, elapsed = request_json(url, body={
            "question": QUESTION,
            "client_session_id": "latency-probe-" + label,
            "recent_history": [],
            "locale": "th",
            "debug": False,
            "experimental_rag_fallback": False,
            "experimental_allow_llm": False,
        }, timeout=25)
        row = {
            "label": label,
            "client_elapsed_ms": elapsed,
            "server_wall_ms": round(float(payload.get("wall_sec") or 0) * 1000, 1),
            "pipeline_elapsed_ms": round(float(payload.get("latency_sec") or 0) * 1000, 1),
            "ok": payload.get("ok"),
            "mode": payload.get("mode"),
            "route_intent": payload.get("route_intent"),
            "answer": payload.get("answer"),
        }
        result["results"].append(row)
        print(f"{label}: {elapsed} ms, mode={row['mode']}", flush=True)
finally:
    if chatbot is not None:
        stop(chatbot)
    if dashboard is not None:
        stop(dashboard)
    for handle in handles:
        handle.close()
    print("Temporary services stopped", flush=True)

with OUTPUT.open("x", encoding="utf-8") as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(OUTPUT)
