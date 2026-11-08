"""Version the next new owner package after the reviewed English scope fix."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\build_owner_local_package.ps1")
BACKUP = ROOT / "work/build_owner_local_package_before_r3_20260926.ps1"
original = TARGET.read_bytes()
old = b'2026.09.26-owner-review-candidate-r2'
new = b'2026.09.26-owner-review-candidate-r3'
if original.count(old) != 1:
    raise RuntimeError("Expected unique runtime version anchor")
with BACKUP.open("xb") as handle:
    handle.write(original)
TARGET.write_bytes(original.replace(old, new, 1))
print(TARGET)
