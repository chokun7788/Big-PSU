"""Download a pinned public HF checkpoint with size/LFS hash verification."""
import concurrent.futures,hashlib,json,os,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;DEST=Path('D:/CodexTraining/psu-r121-20261022/model');DEST.mkdir(parents=True,exist_ok=True)
REPO='typhoon-ai/typhoon2.5-qwen3-4b';REV='ce0a7416fe82d4404b2b4a253ce3ac095ab1252c'
with urllib.request.urlopen('https://huggingface.co/api/models/'+REPO+'/revision/'+REV+'?blobs=true',timeout=30) as h:info=json.load(h)
assert info['sha']==REV
(R/'BASE_MODEL_SOURCE.json').write_text(json.dumps(info,ensure_ascii=False,indent=2),'utf8')
files=[f for f in info['siblings'] if f['rfilename'].endswith(('.json','.safetensors','.txt','.jinja'))]
state={};started=time.monotonic()
def save():
 # Only the main thread writes the shared progress file.
 (R/'DOWNLOAD_STATUS.json').write_text(json.dumps({'repository':REPO,'revision':REV,'directory':str(DEST),'elapsed_sec':round(time.monotonic()-started,2),'files':state},indent=2),'utf8')
def one(f):
 name=f['rfilename'];p=DEST/name;want=f.get('size');expected=(f.get('lfs') or {}).get('sha256')
 def valid():return p.exists() and p.stat().st_size==want and (not expected or hashlib.file_digest(p.open('rb'),'sha256').hexdigest()==expected)
 if valid():return name,{'verified':True,'size':want,'cached':True}
 part=p.with_name(p.name+'.part')
 for attempt in range(3):
  try:
   offset=part.stat().st_size if part.exists() else 0
   url='https://huggingface.co/'+REPO+'/resolve/'+REV+'/'+name+'?download=true&r121='+str(int(time.time()))
   req=urllib.request.Request(url,headers={'Range':'bytes='+str(offset)+'-'} if offset else {})
   with urllib.request.urlopen(req,timeout=120) as h:
    append=offset>0 and h.status==206
    with part.open('ab' if append else 'wb') as out:
     while True:
      b=h.read(4*1024*1024)
      if not b:break
      out.write(b)
   assert part.stat().st_size==want,(name,part.stat().st_size,want)
   if expected:
    with part.open('rb') as h:assert hashlib.file_digest(h,'sha256').hexdigest()==expected
   os.replace(part,p);return name,{'verified':True,'size':want,'sha256':expected}
  except Exception:
   if attempt==2:raise
   time.sleep(2)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 futures=[pool.submit(one,f) for f in files]
 while futures:
  done,pending=concurrent.futures.wait(futures,timeout=2,return_when=concurrent.futures.FIRST_COMPLETED)
  for fut in done:
   name,result=fut.result();state[name]=result
  futures=list(pending)
  for f in files:
   name=f['rfilename'];part=DEST/(name+'.part')
   if part.exists():state[name]={'downloaded_bytes':part.stat().st_size,'total_bytes':f.get('size'),'verified':False}
  save()
assert all(state[f['rfilename']]['verified'] for f in files)
(R/'BASE_MODEL_COMPLETE.json').write_text(json.dumps({'complete':True,'repository':REPO,'revision':REV,'directory':str(DEST),'files':state,'total_bytes':sum(f['size'] for f in files)},indent=2),'utf8')
print('Pinned base model download verified.',flush=True)
