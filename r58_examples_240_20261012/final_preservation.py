"""Read production stores only; save a new receipt in this demo folder."""
import json, sqlite3, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent
prior=json.loads((BASE.parent/'r58_common_content_20261010/owner_edit_20261011_014153/FINAL_OWNER_EDIT_RECEIPT.json').read_text(encoding='utf-8'))
manifest=json.loads((BASE/'MANIFEST.json').read_text(encoding='utf-8'))
receipt={'client_date_bangkok':'2026-10-12','production_checks':{},'source_files':{},'scope':'Production read-only. Root hash compared with prior owner-edit receipt, package also compared with baseline captured this turn.'}
for db,expected in prior['production_database_after'].items():
    c=sqlite3.connect('file:'+Path(db).as_posix()+'?mode=ro',uri=True)
    digest=hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
    counts={table:c.execute('SELECT COUNT(*) FROM '+table).fetchone()[0] for table in ('records','releases','cc_heads','cc_revisions','cc_releases')}
    c.close()
    receipt['production_checks'][db]={'logical_sha256':digest,'matches_prior_receipt':digest==expected,'counts':counts}
    if 'ready_package' in db: receipt['production_checks'][db]['matches_this_turn_baseline']=digest==manifest['production_package_logical_hash']
roots=[Path(next(iter(prior['production_database_after']))).parents[2],BASE.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local',BASE.parent/'r58_common_content_20261010/ready_package/PSU_Esports_Chatbot_Local']
for rel in prior['source_files_applied']:
    hashes={str(root):hashlib.sha256((root/rel).read_bytes()).hexdigest() for root in roots}
    receipt['source_files'][rel]={'sha256_by_copy':hashes,'all_three_copies_match':len(set(hashes.values()))==1}
demo=sqlite3.connect('file:'+(BASE/'DEMO_ONLY.sqlite').as_posix()+'?mode=ro',uri=True)
receipt['original_demo_counts']={t:demo.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in ('records','releases','cc_heads','cc_revisions','cc_releases')};demo.close()
receipt['all_checks_pass']=all(x['matches_prior_receipt'] for x in receipt['production_checks'].values()) and all(x['all_three_copies_match'] for x in receipt['source_files'].values())
receipt['supersedes_receipt']='FINAL_PRESERVATION_RECEIPT.json: initial count summary only queried legacy tables; this receipt also counts cc_* common format tables. Logical hashes were correct in both.'
with (BASE/'FINAL_PRESERVATION_RECEIPT_V2.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps(receipt,ensure_ascii=False,indent=2))
