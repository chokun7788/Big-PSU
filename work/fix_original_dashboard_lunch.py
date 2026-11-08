import ast
import hashlib
from pathlib import Path


source = Path(r"D:\Download New\booking_dashboard_v26_slot_balanced_layout\booking_dashboard_v26_slot_balanced_layout\server.py")
backup = Path(__file__).with_name("original_D_dashboard_server_before_lunch_20260926.py")
expected_hash = "462418cf8c76b0223d8e36beec455e11f526fce9adadd347c70718110cd5ecae"
content = source.read_bytes()
actual_hash = hashlib.sha256(content).hexdigest()
if actual_hash != expected_hash:
    raise RuntimeError(f"Original Dashboard changed since review: {actual_hash}")
with backup.open("xb") as handle:
    handle.write(content)

newline = b"\r\n" if b"\r\n" in content else b"\n"


def replace_once(old: str, new: str) -> None:
    global content
    old_bytes = old.encode("ascii").replace(b"\n", newline)
    new_bytes = new.encode("ascii").replace(b"\n", newline)
    if content.count(old_bytes) != 1:
        raise RuntimeError(f"Expected one matching block, got {content.count(old_bytes)}")
    content = content.replace(old_bytes, new_bytes)


replace_once(
    '''def weekday_key_from_date(selected_date: str) -> str:
''',
    '''def exclude_lunch_break(periods: List[List[str]]) -> List[List[str]]:
    """Exclude the confirmed 12:00-13:00 non-bookable break from opening periods."""
    bookable: List[List[str]] = []
    for start, end in periods:
        if start < "12:00":
            morning_end = min(end, "12:00")
            if start < morning_end:
                bookable.append([start, morning_end])
        if end > "13:00":
            afternoon_start = max(start, "13:00")
            if afternoon_start < end:
                bookable.append([afternoon_start, end])
    return bookable


def weekday_key_from_date(selected_date: str) -> str:
''',
)
replace_once(
    '''            periods = normalize_periods([[hours.get("start", "09:00"), hours.get("end", "16:00")]])
        return {
''',
    '''            periods = normalize_periods([[hours.get("start", "09:00"), hours.get("end", "16:00")]])
        periods = exclude_lunch_break(periods)
        return {
''',
)
replace_once(
    '''    periods = normalize_periods(cfg.get("open_periods"))
    return {
''',
    '''    periods = exclude_lunch_break(normalize_periods(cfg.get("open_periods")))
    return {
''',
)
ast.parse(content.decode("utf-8"))
source.write_bytes(content)
print(f"Patched {source}; preserved original copy at {backup}")
