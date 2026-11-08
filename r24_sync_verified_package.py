"""Preserve the candidate snapshot, then update only our r24 delivery package."""
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
REPORT = Path(Path(__file__).with_name('r24_report_path.txt').read_text(encoding='utf-8').strip())
PACKAGE = ROOT / 'owner_local_delivery_20261001_competition_r24_final/PSU_Esports_Chatbot_Local'
BACKUP = REPORT / 'package_final_before_sync'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def sync_file(source, destination):
    if destination.exists() and digest(source) == digest(destination):
        return None
    relative = destination.relative_to(PACKAGE)
    old_digest = digest(destination) if destination.exists() else None
    if destination.exists():
        backup = BACKUP / relative
        backup.parent.mkdir(parents=True, exist_ok=True)
        with backup.open('xb') as handle:
            handle.write(destination.read_bytes())
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    assert digest(source) == digest(destination)
    return {'path': str(relative), 'before_sha256': old_digest, 'after_sha256': digest(destination)}

changes = []
for source in sorted((ROOT / 'app').rglob('*')):
    if not source.is_file() or '__pycache__' in source.parts or source.suffix == '.pyc':
        continue
    change = sync_file(source, PACKAGE / source.relative_to(ROOT))
    if change:
        changes.append(change)

release = (ROOT / 'data/locales/en/CURRENT').read_text(encoding='utf-8').strip()
for source in sorted((ROOT / 'data/locales/en/releases' / release).rglob('*')):
    if source.is_file():
        change = sync_file(source, PACKAGE / source.relative_to(ROOT))
        if change:
            changes.append(change)
change = sync_file(ROOT / 'data/locales/en/CURRENT', PACKAGE / 'data/locales/en/CURRENT')
if change:
    changes.append(change)

manifest_path = PACKAGE / 'package_manifest.json'
manifest_backup = BACKUP / 'package_manifest.json'
with manifest_backup.open('xb') as handle:
    handle.write(manifest_path.read_bytes())
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
manifest['r24_verified_sync_at'] = datetime.now(timezone.utc).isoformat()
manifest['english_release'] = release
manifest['r24_app_sha256'] = {str(path.relative_to(PACKAGE)): digest(path) for path in sorted((PACKAGE / 'app').rglob('*.py')) if '__pycache__' not in path.parts}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
evidence = {'package': str(PACKAGE), 'backup': str(BACKUP), 'changes': changes, 'english_release': release, 'runtime_data_and_existing_logs_untouched': True}
with (REPORT / 'package_final_sync.json').open('x', encoding='utf-8') as handle:
    json.dump(evidence, handle, ensure_ascii=False, indent=2)
print(json.dumps({'package': str(PACKAGE), 'changed_files': len(changes), 'english_release': release}, ensure_ascii=False))
