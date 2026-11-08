"""Reviewed local proposals -> new unpublished source-bound revisions only."""
import sys,json,copy,hashlib,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,validate,now
from app.knowledge.common.translation import validate_translation
from app.knowledge.records import canonical_json
proposals=B/'CONTROL_NOTE_REVIEWED';complete=json.loads((B/'CONTROL_NOTE_PROPOSALS'/'COMPLETE.json').read_text(encoding='utf-8'));assert complete['notes']==390 and complete['records']==36
review=json.loads((B/'CONTROL_NOTE_AGENT_REVIEW.json').read_text(encoding='utf-8'));assert review['all_proposals_read'] and not review['unresolved_errors']
assert not (B/'CONTROL_NOTE_TRANSLATION_REPAIRS.json').exists()
s=CommonStore(B/'common.sqlite')
with s.connect() as c:records=s.heads(c);sources=s.sources(c);meta=dict(c.execute('SELECT key,value FROM cc_meta'));assert not meta['active']
prepared=[]
for path in sorted(proposals.glob('controls_*.json')):
 d=json.loads(path.read_text(encoding='utf-8'));rid=d['record_id'];r0=records[rid];v=value(r0,'limitations');assert r0['revision']==d['revision'] and v['en']==d['old_en'] and hashlib.sha256(v['th'].encode()).hexdigest()==d['th_sha256']
 assert review['proposal_hashes'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest()
 old=v['en'].splitlines();new=d['new_en'].splitlines();th=v['th'].splitlines();assert len(old)==len(new)==len(th)
 byline={x['line']:x for x in d['notes']}
 for i,(o,n,t) in enumerate(zip(old,new,th)):
  a=[x.strip() for x in o.split('|')];z=[x.strip() for x in n.split('|')];src=[x.strip() for x in t.split('|')]
  assert len(a)==len(z) and a[:2]==z[:2] and a[3:]==z[3:]
  if i in byline:
   note=byline[i];assert not a[2] and z[2]==note['en'] and src[2]==note['th'];validate_translation(note['th'],note['en'])
  else:assert a==z
 target={**v,'en':d['new_en']};raw=canonical_json({'mapped_fields':{'limitations':target},'translation_lineage':[{'original_field_evidence':r0['fields']['limitations']['evidence_refs'],'original_en':v['en'],'notes':d['notes'],'reason':'Translate previously empty English note columns only; preserve original button/action columns and Thai source'}],'owner_reviewed':False});sid='r66_control_notes_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'translation://r66-control-notes/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['control_set'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
 r=copy.deepcopy(r0);r['fields']['limitations'].update(value=target,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/limitations'}]);r['localization'].update(en_status='agent_translated',source_revision_hash=None);sources[sid]=(source,raw);records[rid]=r;prepared.append((r0,r,source,raw,d,path))
assert len(prepared)==36
for r0,r,source,raw,d,path in prepared:
 errors=validate(r,records,sources,publish=False);assert not errors,(r['record_id'],errors)
backup=B/'common_before_control_notes.sqlite';assert not backup.exists()
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(backup) as dst:src.backup(dst)
changes=[]
for r0,r,source,raw,d,path in prepared:
 s.add_source(source,raw,actor='r66-control-note-translation');saved=s.save(r,actor='r66-control-note-translation',expected_version=r0['revision'],change_note='Fill missing English control notes from unchanged Thai, keeping original columns, source and revisions; agent reviewed, not owner approved')
 item={'record_id':r['record_id'],'field':'limitations','old_en':d['old_en'],'new_en':d['new_en'],'source_id':source['source_id'],'source_path':source['path'],'source_sha256':source['sha256'],'notes':len(d['notes']),'proposal_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'new_version':saved['version']};changes.append(item)
 with (B/'CONTROL_NOTE_APPLY_LOG.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(item,ensure_ascii=False)+'\n')
out={'records':len(changes),'notes':sum(x['notes'] for x in changes),'changes':changes,'published':False,'owner_approved':False,'agent_semantic_review':True}
(B/'CONTROL_NOTE_TRANSLATION_REPAIRS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='changes'}))
