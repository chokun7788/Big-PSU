"""One reviewed migration-only read link, with immutable revision fingerprints."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
rows=json.loads((B/'SOURCE_INSPECTION.json').read_text('utf8'))
records={x['id']:x['record'] for x in rows if 'record' in x}
s='migrated_game_god_of_war_ragnar_k';t='game_detail_god_of_war_ragnarok'
def digest(r):return hashlib.sha256(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
link={'source_record_id':s,'target_record_id':t,'source_record_sha256':digest(records[s]),'target_record_sha256':digest(records[t]),'fields':['genre','summary','how_to_play'],'basis':'Same full game title, Latin accent variant only; target summary explicitly names God of War Ragnarök. Source is revision-1 imported title-only placeholder; no owner fact is replaced. Source/target record hashes must both remain unchanged. Does not merge editions, availability, platform, controls or prices.','owner_identity_approval':False,'review_scope':'agent-reviewed migration draft only','evidence':{'source_title':records[s]['fields']['title'],'target_title':records[t]['fields']['title'],'target_summary':records[t]['fields']['summary']}}
(B/'system/app/knowledge/common/identity_links.json').write_text(json.dumps({'version':1,'links':[link]},ensure_ascii=False,indent=2),encoding='utf8')
print('Created 1 hash-guarded, field-scoped link; database unchanged.')
