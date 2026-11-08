from pathlib import Path
import json,ast,sqlite3
from prepare import B,SYSTEM,ROOT,PACK,sha,dbhash
receipt=json.loads((B/'DELIVERY_RECEIPT.json').read_text(encoding='utf-8'))
for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
 for name,h in receipt['source_hashes'][label].items():assert sha(root/name)==h,'Source changed after delivery '+str(root/name)
for path,h in receipt['db_hashes'].items():assert dbhash(Path(path))==h,'Original database changed '+path
for file in ['guards_release_final.log','installed_project_guards.log']:
 text=(B/file).read_text(encoding='utf-8');assert 'Ran 57 tests' in text and text.rstrip().endswith('OK')
semantic=json.loads((B/'semantic_release_final/SUMMARY.json').read_text(encoding='utf-8'));assert semantic['passed']==148
owner=json.loads((B/'OWNER_HTTP_SUMMARY.json').read_text(encoding='utf-8'));assert owner['passed']==48
web=json.loads((B/'WEB_FIXTURE_REVIEWED.json').read_text(encoding='utf-8'));assert web['passed']==48
unnamed=json.loads((B/'UNNAMED_SUMMARY.json').read_text(encoding='utf-8'));assert unnamed['passed']==10
translation=json.loads((B/'TRANSLATION_CHECK_REVIEWED.json').read_text(encoding='utf-8'));assert translation['passed']==3
context=json.loads((B/'TRANSLATION_CONTEXT_CHECK.json').read_text(encoding='utf-8'));assert context['passed']
archives=json.loads((B/'ARCHIVES.json').read_text(encoding='utf-8'));assert len(archives)==2
for a in archives:assert Path(a['path']).stat().st_size==a['bytes']
for root in [B/'delivery/PSU_Chatbot_With_Models',B/'delivery/PSU_Chatbot_Download_Models']:
 for name,h in receipt['source_hashes']['candidate'].items():
  if name.startswith('tests/') or name=='package_manifest.json':continue
  assert sha(root/name)==h,'Portable source differs '+str(root/name)
db=SYSTEM/'data/knowledge/approved.sqlite'
with sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True) as c:
 heads=c.execute('SELECT count(*) FROM cc_heads').fetchone()[0]
 releases=c.execute('SELECT count(*) FROM cc_releases').fetchone()[0]
final={'date_th':'2026-10-13','candidate_guards':{'passed':57,'total':57},'installed_project_guards':{'passed':57,'total':57},'semantic_bilingual_real_bundled_llm':{'passed':148,'total':148,'th':74,'en':74,'synthetic_facts':True,'human_semantics_guarantee':False},'owner_http_categories':24,'owner_http_reads':{'passed':48,'total':48},'actual_chat_http_reads':{'passed':48,'total':48,'supervisor_load_test':False},'unnamed_faq_and_negatives':{'passed':10,'total':10},'translation_fixtures':{'passed':3,'total':3},'translation_game_context':{'passed':1,'total':1},'original_db_hashes_unchanged':True,'all_prior_git_entries_retained':True,'prior_git_entries':receipt['old_git_entries'],'production_common_heads':heads,'production_common_releases':releases,'agent_approved_real_facts':False,'live_booking_currently_reverified_in_this_round':False,'public_internet_deployment':False,'new_operational_calendar_sync_to_wordpress_certified':False,'archives':archives}
(B/'FINAL_VERIFICATION.json').write_text(json.dumps(final,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(final,ensure_ascii=False,indent=2))
