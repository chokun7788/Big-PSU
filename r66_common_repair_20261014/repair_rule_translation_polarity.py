import sys,json,copy,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now
from app.knowledge.records import canonical_json
from app.knowledge.common.translation import protected
s=CommonStore(B/'common.sqlite')
with s.connect() as c:rs=s.heads(c)
rid='competition_competition_rules_valorant_psu_phuket_2026_section_009';parallel=rs['competition_competition_rules_valorant_psu_phuket_2026_section_024'];r0=rs[rid];v=copy.deepcopy(value(r0,'text'))
assert 'จุดที่ทำลายไม่ได้' in v['th'] and 'indestructible' in value(parallel,'text')['th']
old=v['en'];v['en']=old.replace('invisible or impassable locations','invisible or indestructible locations').replace('on destructible locations','in indestructible locations')
assert v['en']!=old and protected(v['th'])==protected(v['en'])
raw=canonical_json({'mapped_fields':{'text':v},'translation_lineage':[{'th':v['th'],'previous_en':old,'en':v['en'],'original_field_evidence':r0['fields']['text']['evidence_refs'],'parallel_original_english_evidence':parallel['fields']['text']['evidence_refs'],'reason':'Thai ทำลายไม่ได้ and the original bilingual English both say indestructible; repair generated translation, do not change rules'}],'owner_reviewed':False});sid='r66_rule_polarity_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
src={'source_id':sid,'kind':'derived_curated','path':'translation://r66-rule-polarity/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['competition_rule'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None};s.add_source(src,raw,actor='r66-rule-translation-review')
r=copy.deepcopy(r0);r['fields']['text'].update(value=v,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/text'}]);r['localization'].update(en_status='agent_translated',source_revision_hash=None);s.save(r,actor='r66-rule-translation-review',expected_version=r0['revision'],change_note='Correct generated destructible/impassable words against Thai and original bilingual English source; no business policy change')
(B/'RULE_TRANSLATION_POLARITY_REPAIR.json').write_text(json.dumps({'record_id':rid,'old_en':old,'new_en':v['en'],'parallel_source_record':parallel['record_id'],'published':False},ensure_ascii=False,indent=2),encoding='utf-8')
