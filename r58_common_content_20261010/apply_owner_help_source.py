from pathlib import Path
import json,hashlib,shutil,sqlite3
OUT=Path(__file__).resolve().parent
p=json.loads((OUT/'owner_help_latest.json').read_text(encoding='utf-8'));RUN=Path(p['run']);stage=Path(p['stage'])
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
for name in ('index.html','owner.js','owner.css'):
    dest=ROOT/'app/knowledge/common/ui'/name
    if hashlib.sha256(dest.read_bytes()).hexdigest()!=p['before'][str(dest)]['sha256']:raise SystemExit('Source changed after backup: '+str(dest))
doc=ROOT/'docs/common_content_r58/OWNER_EASY_GUIDE_TH.md'
if doc.exists():raise SystemExit('Existing guide must not be overwritten: '+str(doc))
for name in ('index.html','owner.js','owner.css'):shutil.copy2(stage/name,ROOT/'app/knowledge/common/ui'/name)
shutil.copy2(RUN/'OWNER_EASY_GUIDE_TH.md',doc)
receipt={'changed':['app/knowledge/common/ui/'+n for n in ('index.html','owner.js','owner.css')],'added':['docs/common_content_r58/OWNER_EASY_GUIDE_TH.md'],'database_writes':False,'hashes':{n:hashlib.sha256((ROOT/'app/knowledge/common/ui'/n).read_bytes()).hexdigest() for n in ('index.html','owner.js','owner.css')}}
(RUN/'source_apply_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
