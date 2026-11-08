"""Create and verify ZIP64 archives, excluding runtime chat histories/state."""
from pathlib import Path
import hashlib,json,shutil,time,zipfile

OUT=Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_20261003')
records=[]
for folder in ['01_Download_Models','02_With_Models']:
    root=OUT/folder
    archive=OUT/(folder+'.zip')
    if archive.exists():raise RuntimeError('Refusing to overwrite existing archive')
    # Keep 2 GB free even if compression gives no savings.
    total=sum(p.stat().st_size for p in root.rglob('*') if p.is_file())
    if shutil.disk_usage(OUT).free<total+2_000_000_000:
        raise RuntimeError('Insufficient free disk space for safe archive creation; folders are intact.')
    print(f'Creating {archive.name}...',flush=True)
    count=0
    with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
        for path in root.rglob('*'):
            if not path.is_file():continue
            rel=path.relative_to(root)
            if 'state' in rel.parts or ('logs' in rel.parts and path.name!='.gitkeep'):
                raise RuntimeError('Unexpected private runtime state/log in clean release')
            z.write(path,arcname=folder+'/'+rel.as_posix());count+=1
    print(f'Checking archive CRC: {archive.name}...',flush=True)
    with zipfile.ZipFile(archive) as z:
        bad=z.testzip()
        if bad:raise RuntimeError(f'Corrupt ZIP entry: {bad}')
        assert len(z.infolist())==count
        assert folder+'/Start-Chatbot.cmd' in z.namelist()
        weights=[i for i in z.infolist() if '/runtime/models/blobs/' in i.filename and i.file_size>100_000_000]
        assert len(weights)==(2 if folder=='02_With_Models' else 0)
    with archive.open('rb') as f:sha=hashlib.file_digest(f,'sha256').hexdigest()
    row={'archive':archive.name,'bytes':archive.stat().st_size,'entries':count,'crc_passed':True,'model_weight_files':len(weights),'sha256':sha}
    records.append(row);print(json.dumps(row),flush=True)
(OUT/'archive_checks.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
(OUT/'SHA256SUMS.txt').write_text(''.join(r['sha256']+'  '+r['archive']+'\n' for r in records),encoding='utf-8')
print('Both share archives are ready and CRC verified.',flush=True)
