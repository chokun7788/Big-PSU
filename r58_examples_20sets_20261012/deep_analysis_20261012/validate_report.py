"""Verify exhaustive case coverage, links and read-only production preservation."""
import json,re,hashlib,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;DATA=B.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def digestdb(p):
    c=sqlite3.connect('file:'+p.as_posix()+'?mode=ro',uri=True)
    try:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
    finally:c.close()
rows=[json.loads(x) for x in (DATA/'content_final/ANSWERS_AND_DECISIONS.jsonl').read_text(encoding='utf-8').splitlines()]
failed={r['id'] for r in rows if not r['passed']}
docs=list((B/'FAILURES_BY_CATEGORY').glob('*.md'));seen=[]
for p in docs:seen+=re.findall(r'^## Case (\d+)$',p.read_text(encoding='utf-8'),re.M)
assert len(docs)==24 and len(seen)==len(set(seen))==2403 and set(seen)==failed
ann=read(B/'CASE_ANNOTATIONS_5056_V2.json')
assert len(ann)==len({r['case_id'] for r in ann})==5056
assert {r['case_id'] for r in ann}=={r['id'] for r in rows}
groups=read(B/'FAILURE_PATTERN_GROUPS.json');group_ids=[rid for g in groups for rid in g['case_ids']]
assert len(group_ids)==len(set(group_ids))==2403 and set(group_ids)==failed
passids=re.findall(r'^## Case (\d+)$',(B/'PASSED_QUALITY_AUDITS_ALL.md').read_text(encoding='utf-8'),re.M)
assert len(passids)==len(set(passids))==814 and all(next(r for r in rows if r['id']==rid)['passed'] for rid in passids)
missing=[];invalid_lines=[];links=0
for p in B.rglob('*.md'):
    for target in re.findall(r'\]\((C:/[^)]+)\)',p.read_text(encoding='utf-8')):
        links+=1;path=target.split('#',1)[0];line=None
        m=re.search(r':(\d+)$',path)
        if m:line=int(m.group(1));path=path[:m.start()]
        dest=Path(path)
        if not dest.exists():missing.append({'document':str(p),'target':target})
        elif line and not 1<=line<=len(dest.read_text(encoding='utf-8').splitlines()):invalid_lines.append(target)
assert not missing and not invalid_lines
source=read(B/'AUDIT_METRICS.json')['source_sha256'];system=DATA.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
source_unchanged={k:hashlib.sha256((system/k).read_bytes()).hexdigest()==v for k,v in source.items()}
assert all(source_unchanged.values())
prior=read(DATA/'PRESERVATION_RECEIPT.json');production={p:digestdb(Path(p))==x['logical_sha256'] for p,x in prior['production'].items()}
old_demo=digestdb(DATA.parent/'r58_examples_240_20261012/DEMO_ONLY.sqlite')==prior['old_demo']['logical_sha256']
new_demo=digestdb(DATA/'DEMO_720_ONLY.sqlite')==prior['new_demo']['logical_sha256']
assert all(production.values()) and old_demo and new_demo
receipt={'main_failed_cases_documented':2403,'category_markdown_files':24,'annotations_all_cases':5056,'failure_pattern_groups':len(groups),'passed_quality_review_cases':len(passids),'main_report_characters':len((B/'DEEP_ROOT_CAUSE_ANALYSIS_TH.md').read_text(encoding='utf-8')),'links_checked':links,'missing_links':missing,'invalid_source_lines':invalid_lines,'source_files_unchanged':source_unchanged,'production_unchanged_vs_prior_receipt':production,'old_demo_unchanged':old_demo,'new_demo_unchanged':new_demo,'scope':'read-only checks; no code/data fixes; all analysis written in this new folder'}
with (B/'DEEP_REPORT_VALIDATION.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps(receipt,ensure_ascii=False),flush=True)
