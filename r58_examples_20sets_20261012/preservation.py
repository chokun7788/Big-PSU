"""Read-only production checks. Writes one new receipt beside DEMO data."""
import json,hashlib,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
M=json.loads((B/'MANIFEST.json').read_text(encoding='utf-8'))
P=json.loads((B.parent/'r58_examples_240_20261012/FINAL_PRESERVATION_RECEIPT_V2.json').read_text(encoding='utf-8'))
def digestdb(p):
    c=sqlite3.connect('file:'+p.as_posix()+'?mode=ro',uri=True)
    try:
        h=hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
        counts={t:c.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in ('cc_heads','cc_revisions','cc_releases')}
        return {'logical_sha256':h,'counts':counts}
    finally:c.close()
receipt={'client_date_bangkok':'2026-10-12','scope':'All production access read-only; earlier receipt used for root; package and original demo also compared with baseline captured this experiment.'}
receipt['production']={}
for p,prior in P['production_checks'].items():
    x=digestdb(Path(p));x['matches_prior_receipt']=x['logical_sha256']==prior['logical_sha256']
    if 'ready_package' in p:x['matches_current_turn_baseline']=x['logical_sha256']==M['baseline']['production_package']
    receipt['production'][p]=x
receipt['old_demo']=digestdb(B.parent/'r58_examples_240_20261012/DEMO_ONLY.sqlite')
receipt['old_demo']['unchanged_from_this_turn_baseline']=receipt['old_demo']['logical_sha256']==M['baseline']['old_demo']
receipt['new_demo']=digestdb(B/'DEMO_720_ONLY.sqlite')
receipt['source_files']={}
for rel,item in P['source_files'].items():
    current={root:hashlib.sha256((Path(root)/rel).read_bytes()).hexdigest() for root in item['sha256_by_copy']}
    receipt['source_files'][rel]={'matches_previous_hashes':current==item['sha256_by_copy'],'current_sha256':current}
receipt['pass']=all(x['matches_prior_receipt'] for x in receipt['production'].values()) and receipt['old_demo']['unchanged_from_this_turn_baseline'] and all(x['matches_previous_hashes'] for x in receipt['source_files'].values())
with (B/'PRESERVATION_RECEIPT.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps({'pass':receipt['pass'],'old_demo_unchanged':receipt['old_demo']['unchanged_from_this_turn_baseline'],'new_counts':receipt['new_demo']['counts']},ensure_ascii=False))
