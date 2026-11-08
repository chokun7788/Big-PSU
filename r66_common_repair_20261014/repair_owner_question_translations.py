import sys,json,copy,hashlib,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now,value
from app.knowledge.records import canonical_json
s=CommonStore(B/'common.sqlite');backup=B/'common_before_owner_question_review.sqlite'
assert not backup.exists()
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(backup) as dst:src.backup(dst)
with s.connect() as c:rs=s.heads(c)
fixes={'migrated_owner_claim_contact':"If I cannot find the studio, who can I contact?",'migrated_owner_claim_change_machine':"Can I change a booking made for the wrong machine?"};changes=[]
for rid,en in fixes.items():
 r0=rs[rid];r=copy.deepcopy(r0);before=value(r0,'question');target={**before,'en':en};raw=canonical_json({'mapped_fields':{'question':target},'translation_lineage':[{'original_field_evidence':r0['fields']['question']['evidence_refs'],'th':before['th'],'previous_en':before['en'],'en':en,'reason':'Domain polysemy: ศูนย์ means studio/center, เครื่อง means machine in this booking context'}],'owner_reviewed':False});sid='r66_question_review_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'translation://r66-owner-question-review/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['faq'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None};s.add_source(source,raw,actor='r66-question-review');r['fields']['question'].update(value=target,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/question'}]);r['localization'].update(en_status='agent_translated',source_revision_hash=None);s.save(r,actor='r66-question-review',expected_version=r0['revision'],change_note='Correct generated English question against unchanged Thai and existing studio context');changes.append({'record_id':rid,'old_en':before['en'],'new_en':en})
(B/'OWNER_QUESTION_TRANSLATION_REPAIRS.json').write_text(json.dumps({'changes':changes,'owner_questions_reviewed':19,'published':False,'owner_approved':False},ensure_ascii=False,indent=2),encoding='utf-8');print(len(changes))
