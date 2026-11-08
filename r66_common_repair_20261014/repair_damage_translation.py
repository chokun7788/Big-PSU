"""Source-bound damage FAQ translation revision. No policy/approval changes."""
import sys,json,copy,hashlib,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now
from app.knowledge.common.translation import validate_translation
from app.knowledge.records import canonical_json
s=CommonStore(B/'common.sqlite');backup=B/'common_before_damage_translation.sqlite'
assert not backup.exists()
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(backup) as dst:src.backup(dst)
with s.connect() as c:rs=s.heads(c)
rid='migrated_faq_rule_damage_responsibility';r0=rs[rid];v=copy.deepcopy(value(r0,'answer'));old=v['en']
parallel=rs['migrated_faq_rule_en_damage_responsibility_natural'];en=value(parallel,'answer')['en']
assert '100–500' in v['th'] and '500–2,000' in v['th'] and 'ราคาจริงหรือ' in v['th']
assert '100-500 THB' in en and 'actual cost or 500-2,000 THB' in en
v['en']=en
# Dash variants are presentation, not a new rate. Validate normalized literals.
validate_translation(v['th'].replace('–','-'),en)
raw=canonical_json({'mapped_fields':{'answer':v},'translation_lineage':[{'th':v['th'],'previous_en':old,'en':en,'original_field_evidence':r0['fields']['answer']['evidence_refs'],'parallel_english_evidence':parallel['fields']['answer']['evidence_refs'],'reason':'Restore omitted fine ranges and actual-cost condition from unchanged Thai; parallel existing English agrees'}],'owner_reviewed':False})
sid='r66_damage_translation_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
src={'source_id':sid,'kind':'derived_curated','path':'translation://r66-damage-fines/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['faq'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
s.add_source(src,raw,actor='r66-damage-translation-review');r=copy.deepcopy(r0);r['fields']['answer'].update(value=v,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/answer'}]);r['localization'].update(en_status='agent_translated',source_revision_hash=None)
s.save(r,actor='r66-damage-translation-review',expected_version=r0['revision'],change_note='Restore omitted damage fine ranges in generated English, verified against original Thai and parallel source')
(B/'DAMAGE_TRANSLATION_REPAIR.json').write_text(json.dumps({'record_id':rid,'old_en':old,'new_en':en,'parallel_record':parallel['record_id'],'published':False,'owner_approved':False},ensure_ascii=False,indent=2),encoding='utf-8')
print('One draft translation revision; original sources retained')
