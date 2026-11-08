import sys,json,copy,re,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now
from app.knowledge.records import canonical_json
from app.knowledge.common.translation import protected
s=CommonStore(B/'common.sqlite')
with s.connect() as c:rs=s.heads(c)
changes=[]
for rid,r0 in rs.items():
 if r0['kind']!='faq':continue
 v=value(r0,'answer')
 if not isinstance(v,dict) or 'กะทู้' not in str(v.get('th')) or 'Kata Noi' not in str(v.get('en')):continue
 r=copy.deepcopy(r0);target=copy.deepcopy(v);target['en']='PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Wichit Songkhram Road, Kathu, Phuket 83120.'
 assert protected(v['th'])==protected(target['en'])
 raw=canonical_json({'mapped_fields':{'answer':target},'translation_lineage':[{'original_field_evidence':r0['fields']['answer']['evidence_refs'],'th':v['th'],'previous_en':v['en'],'en':target['en'],'reason':'Thai source explicitly says Kathu; Kata Noi was a model mistranslation'}],'owner_reviewed':False});sid='r66_location_review_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'translation://r66-location-review/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['faq'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None};s.add_source(source,raw,actor='r66-location-translation-review')
 r['fields']['answer'].update(value=target,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/answer'}]);r['localization'].update(en_status='agent_translated',source_revision_hash=None);s.save(r,actor='r66-location-translation-review',expected_version=r0['revision'],change_note='Correct location English against exact existing Thai source; not a new location')
 changes.append({'record_id':rid,'old_en':v['en'],'new_en':target['en']})
(B/'LOCATION_TRANSLATION_REPAIRS.json').write_text(json.dumps({'changes':changes,'published':False},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'changes':len(changes),'published':False}))
