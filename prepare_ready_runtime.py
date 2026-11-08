"""Copy existing local runtimes and required model blobs into a fresh delivery."""
from pathlib import Path
import hashlib, json, shutil, time

ROOT = Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Chatbot_Ready_20261003')
PY = Path(r'C:\Users\Chokhun\.cache\codex-runtimes\codex-primary-runtime\dependencies\python')
OL = Path(r'C:\Users\Chokhun\AppData\Local\Programs\Ollama')
STORE = Path(r'C:\Users\Chokhun\.ollama\models')
runtime = ROOT / 'runtime'
runtime.mkdir(exist_ok=False)
records = []

def copy(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        raise RuntimeError(f'Refusing overwrite: {dst}')
    shutil.copy2(src, dst)
    records.append({'path': str(dst.relative_to(ROOT)), 'bytes': dst.stat().st_size})

print('Copying Python standard library and timezone data...', flush=True)
for src in PY.iterdir():
    if src.is_file():
        copy(src, runtime / 'python' / src.name)
for part in ['Lib', 'DLLs']:
    for src in (PY / part).rglob('*'):
        if not src.is_file() or '__pycache__' in src.parts or src.suffix == '.pyc':
            continue
        rel = src.relative_to(PY)
        if 'site-packages' in rel.parts and not any(p == 'tzdata' or p.startswith('tzdata-') for p in rel.parts):
            continue
        copy(src, runtime / 'python' / rel)
print('Copying Ollama executable, CPU/GPU libraries and supplied licenses...', flush=True)
copy(OL / 'ollama.exe', runtime / 'ollama' / 'ollama.exe')
for src in (OL / 'lib' / 'ollama').rglob('*'):
    if src.is_file():
        copy(src, runtime / 'ollama' / src.relative_to(OL))
print('Copying only the two required models; checking every blob digest...', flush=True)
model_names = [('scb10x/typhoon2.5-qwen3-4b:latest', 'registry.ollama.ai/scb10x/typhoon2.5-qwen3-4b/latest'),
               ('psu-bge-m3:q8_0', 'registry.ollama.ai/library/psu-bge-m3/q8_0')]
models = []
seen = set()
for name, manifest_path in model_names:
    src = STORE / 'manifests' / manifest_path
    raw = src.read_bytes()
    manifest = json.loads(raw)
    copy(src, runtime / 'models' / 'manifests' / manifest_path)
    models.append({'name': name, 'digest': hashlib.sha256(raw).hexdigest()})
    for layer in [manifest['config'], *manifest['layers']]:
        digest = layer['digest']
        if digest in seen:
            continue
        seen.add(digest)
        blob = STORE / 'blobs' / digest.replace(':', '-')
        dst = runtime / 'models' / 'blobs' / blob.name
        copy(blob, dst)
        sha = hashlib.file_digest(dst.open('rb'), 'sha256').hexdigest()
        if sha != digest.split(':', 1)[1]:
            raise RuntimeError(f'Corrupt copied model: {dst}')
        records[-1]['sha256'] = sha
        print(f'Checked {blob.name}: {dst.stat().st_size:,} bytes', flush=True)
manifest = {'runtime_version': '2026.10.03-ready-folder-r37.2', 'python': '3.12',
            'ollama': '0.34.4', 'models': models, 'files': records,
            'bundled_bytes': sum(x['bytes'] for x in records),
            'excluded': ['old chat logs', 'Ollama user keys', 'unrelated models', 'test datasets', 'Codex runtime site packages except tzdata']}
(ROOT / 'ready_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'files': len(records), 'bytes': manifest['bundled_bytes'], 'complete': True}), flush=True)
