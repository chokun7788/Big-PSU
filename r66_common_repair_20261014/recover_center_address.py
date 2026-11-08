import sys,json,copy,hashlib,re
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now
from app.knowledge.common.provenance import owner_basis
from app.knowledge.records import canonical_json
from app.knowledge.common.translation import protected
s=CommonStore(B/'common.sqlite')
with s.connect() as c:rs=s.heads(c);sources={sid:p[0] for sid,p in s.sources(c).items()};active=dict(c.execute('SELECT * FROM cc_meta'))['active']
centers=[r for r in rs.values() if r['kind']=='center'];assert len(centers)==1
candidates=[]
for r in rs.values():
 if r['kind']!='faq':continue
 a=value(r,'answer') or {};th=a.get('th','')
 if '83120' in th and re.search(r'อาคาร\s*5',th) and owner_basis(r,s,{'sources':sources}):candidates.append(r)
assert candidates,'No exact owner-confirmed full address source; do not guess'
assert len({value(r,'answer')['th'] for r in candidates})==1,'Conflicting owner addresses'
source_record=candidates[0];address=copy.deepcopy(value(source_record,'answer'));original_en=address.get('en')
address['en']='Building 5, 1st floor, Prince of Songkla University, Phuket Campus, 80 Moo 1 Wichit Songkhram Road, Kathu, Phuket 83120.'
assert protected(address['th'])==protected(address['en']),(address,protected(address['th']),protected(address['en']))
r0=centers[0];assert value(r0,'address') is None
r=copy.deepcopy(r0);raw=canonical_json({'mapped_fields':{'address':address},'source_record_id':source_record['record_id'],'original_field_evidence':source_record['fields']['answer']['evidence_refs'],'original_en_proposal':original_en,'basis':'Exact previously owner-confirmed address copied into missing typed center.address; English translated against Thai; no new location or policy','owner_english_reviewed':False});sid='r66_address_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
src={'source_id':sid,'kind':'derived_curated','path':'migration://r66/existing-owner-address','sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['center'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None};s.add_source(src,raw,actor='r66-address-source-recovery')
r['fields']['address'].update(status='known',value=address,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/address'}],note='Exact original owner-confirmed address; English agent reviewed, not owner reviewed');r['localization'].update(en_status='agent_translated',source_revision_hash=None)
saved=s.save(r,actor='r66-address-source-recovery',expected_version=r0['revision'],change_note='Recover existing owner address into omitted typed field; no invented address')
with s.connect() as c:assert dict(c.execute('SELECT * FROM cc_meta'))['active']==active
(B/'CENTER_ADDRESS_RECOVERY.json').write_text(json.dumps({'record_id':r['record_id'],'source_record_id':source_record['record_id'],'address':address,'version':saved['version'],'published':False},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'source_record_id':source_record['record_id'],'published':False}))
