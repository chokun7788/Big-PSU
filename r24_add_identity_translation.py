from pathlib import Path
import json, sys, hashlib, shutil

ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT))
from app.knowledge.localization import active_registry_path, source_text_sha256
from tools.manage_english_localizations import source_fields, approve_selected_drafts, validate_candidate, publish

report=Path(Path(__file__).with_name('r24_report_path.txt').read_text(encoding='utf-8'))
id='competition_rules_tekken8_psu_esports_s01_c01'
source=source_fields()[(id,'text')]
draft={
 'content_id':id, 'field':'text','locale':'en',
 'text':"Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title).",
 'source_text_sha256':source_text_sha256(source['text']),
 'status':'draft', 'translation_basis':'assistant translation authorized by the user; event title rendering is not an independently published English name',
}
draft_path=report/'tekken_identity_translation_draft.jsonl'
with draft_path.open('x',encoding='utf-8') as handle:handle.write(json.dumps(draft,ensure_ascii=False)+'\n')
candidate=report/'english_candidate_preserving_previous_release.jsonl'
registry=active_registry_path()
shutil.copy2(ROOT/'data/locales/en/CURRENT',report/'english_CURRENT_before.txt')
approve_selected_drafts(draft_path,candidate,selections=[id+':text'],reviewer='assistant_translation_under_explicit_user_authorization; not_owner_human_review',existing_candidate=registry)
rows,errors=validate_candidate(candidate)
assert not errors, errors
before=[json.loads(line) for line in registry.read_text(encoding='utf-8').splitlines() if line.strip()]
after=[json.loads(line) for line in candidate.read_text(encoding='utf-8').splitlines() if line.strip()]
key=lambda row:(row['content_id'],row['field'],row['locale'])
old={key(row):row for row in before};new={key(row):row for row in after}
assert len(after)==len(before)+1
assert all(new[k]==v for k,v in old.items())
release=publish(candidate,mirror_registry=False)
record={'old_registry':str(registry),'new_release':str(release),'before_records':len(before),'after_records':len(after),'old_records_unchanged':True,'original_source_text':source['text'],'new_translation':draft['text'],'source_hash':draft['source_text_sha256'],'review':'assistant translation under prior explicit user authorization; owner has not reviewed it'}
with (report/'identity_translation_publish.json').open('x',encoding='utf-8') as handle:json.dump(record,handle,ensure_ascii=False,indent=2)
print(json.dumps(record,ensure_ascii=False))
