"""Install pinned Ollama blobs, with resumable HTTPS downloads and SHA checks."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, sys, time, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / 'runtime' / 'models'

def sha(path):
    with path.open('rb') as f: return hashlib.file_digest(f, 'sha256').hexdigest()

def fetch(item, destination):
    partial = destination.with_name(destination.name + '.partial')
    if partial.exists() and partial.stat().st_size > item['bytes']:
        partial.rename(partial.with_name(partial.name + '.' + str(time.time_ns()) + '.invalid'))
    for attempt in range(1, 5):
        offset = partial.stat().st_size if partial.exists() else 0
        if offset == item['bytes']: break
        headers = {'User-Agent': 'PSU-Esports-Portable/1.0', 'Accept-Encoding': 'identity'}
        if offset: headers['Range'] = f'bytes={offset}-'
        try:
            request = urllib.request.Request(item['url'], headers=headers)
            with urllib.request.urlopen(request, timeout=45) as response:
                if offset and response.status == 206:
                    if not response.headers.get('Content-Range','').startswith(f'bytes {offset}-'):
                        raise RuntimeError('Download server returned a different resume offset')
                    mode = 'ab'
                elif response.status == 200:
                    offset, mode = 0, 'wb'
                else: raise RuntimeError(f'Unexpected download status {response.status}')
                count, last = offset, 0.0
                with partial.open(mode) as f:
                    while block := response.read(4 * 1024 * 1024):
                        count += len(block)
                        if count > item['bytes']: raise RuntimeError('Downloaded model is larger than the pinned size')
                        f.write(block)
                        now=time.monotonic()
                        if now-last >= 3:
                            print(f"{item['label']}: {count/item['bytes']:.0%} ({count/1e6:.0f}/{item['bytes']/1e6:.0f} MB)",flush=True)
                            last=now
            if count != item['bytes']: raise RuntimeError('Incomplete download; progress is saved for next try')
            break
        except (urllib.error.URLError, TimeoutError, OSError, RuntimeError) as exc:
            if attempt == 4: raise RuntimeError('Model download failed. Check internet/free disk space and open Start-Chatbot.cmd again. Partial downloads were kept.') from exc
            print(f'Download interrupted; retry {attempt}/4 in a moment...',flush=True)
            time.sleep(min(2*attempt, 6))
    if sha(partial) != item['sha256']:
        partial.rename(partial.with_name(partial.name + '.' + str(time.time_ns()) + '.invalid'))
        raise RuntimeError('Downloaded model failed SHA-256 verification; it was not installed. Please retry.')
    os.replace(partial, destination)
    print(f"Verified: {item['label']}",flush=True)

def ensure(check_only=False):
    manifest=json.loads((ROOT/'ready_manifest.json').read_text(encoding='utf-8-sig'))
    seed=ROOT/'runtime'/'model_seed'
    missing=[]
    for item in manifest['model_blobs']:
        file=STORE/'blobs'/('sha256-'+item['sha256'])
        if file.exists():
            if file.stat().st_size != item['bytes'] or sha(file) != item['sha256']:
                raise RuntimeError(f"Model file is damaged: {file.name}. Move it aside and retry; other files were kept.")
        else: missing.append(item)
    if check_only:
        print(json.dumps({'ready':not missing,'missing':[i['label'] for i in missing],'variant':manifest['variant']}),flush=True)
        return 2 if missing else 0
    STORE.joinpath('blobs').mkdir(parents=True, exist_ok=True)
    if missing:
        if manifest['variant'] != 'download_models':
            raise RuntimeError('Bundled models are missing. Extract/copy the complete With_Models folder again.')
        need=sum(i['bytes']-(STORE/'blobs'/('sha256-'+i['sha256']+'.partial')).stat().st_size if (STORE/'blobs'/('sha256-'+i['sha256']+'.partial')).exists() else i['bytes'] for i in missing)
        if shutil.disk_usage(STORE).free < need + 512*1024*1024:
            raise RuntimeError(f'Not enough free disk space. Need about {(need+512*1024*1024)/1e9:.1f} GB more free space.')
        print('First use: downloading the pinned local AI models (about 3.65 GB total).',flush=True)
        for item in missing: fetch(item, STORE/'blobs'/('sha256-'+item['sha256']))
    # Install metadata only after all weights are present and verified.
    for item in manifest['model_seed_files']:
        source=seed/item['path']
        if sha(source) != item['sha256']: raise RuntimeError('Model metadata is damaged; extract this package again.')
        target=STORE/item['path']
        if target.exists():
            if sha(target) != item['sha256']: raise RuntimeError('Installed model metadata differs; files were left intact.')
        else:
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(source,target)
    print('Both local models are ready and match the package.',flush=True)
    return 0

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check-only',action='store_true')
    args=parser.parse_args()
    try: sys.exit(ensure(args.check_only))
    except Exception as exc:
        print(str(exc),file=sys.stderr,flush=True)
        sys.exit(1)
