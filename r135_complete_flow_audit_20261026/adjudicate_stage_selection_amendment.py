"""Immutable semantic correction after row266 source-purpose re-audit."""
import copy,json
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import CRITERIA,digest,example_sha,file_sha,source_identity
from app.knowledge.common.domain_flow.understanding import parse
W=R/'training_review_workbench_1793037663397671000';S=W/'review_round_013';O=W/'semantic_amendments_round014';O.mkdir(exist_ok=True)
def read(p):return json.loads(p.read_text('utf8'))
examples=[json.loads(t) for t in (S/'EXAMPLES.jsonl').read_text('utf8').splitlines()];line,x=next((n,x) for n,x in enumerate(examples,1) if x['annotation_provenance']['historical_review_ref']['line']==267)
source=read(W/'SOURCE_SNAPSHOT.json');q=x['raw_question'];assert q=='ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 เลือกด่านยังไง'
label={'version':'r129-plan-v2','focus':'unclear','context_quotes':[],'tasks':[{'id':'t1','quote':q,'domain':'general','operation':'unknown','facet':'','target':'Tekken 8','constraints':[{'slot':'requested_scope','quote':'เลือกด่าน','source_record_id':'','scope':'local'}],'ambiguous':True}],'shared_bindings':[]}
assert parse(json.dumps(label,ensure_ascii=False),q).accepted
ids=['competition_competition_rules_tekken8_psu_esports_section_004','controls_ps5_tekken_8']
reasons=[
 'One stage-selection procedure question includes source-verification framing, but no explicit tournament or rulebook noun.',
 'Existing C13/rule_lookup injects a competition context not stated by the user. General/unknown with ambiguity preserves the need until ordinary gameplay versus tournament rule scope is clarified.',
 'Tekken 8 and เลือกด่าน are literal input substrings. No platform, tournament identity, stage name, action binding or source-derived operation is invented.',
 'Allowed dialogue history is empty. A competition source found during review cannot supply a missing user context or turn this corpus row into a continuation of another question.',
 'There is no negation. The missing procedure-versus-rule context is a genuine ambiguity; asking for verified information does not remove it.',
 'Actual TEKKEN section004 revision5 records Random stage as a competition setting. The PS5 controls revision6 lists gameplay bindings without a stage-selection procedure. Neither establishes which question the user intended.',
 'No Random answer, control button, platform default, rule permission or fabricated tournament context enters the corrected label.']
evidence={'kind':'individual_semantic_amendment_not_yet_compiled','original_row':266,'question_key':x['question_key'],'raw_question':q,'prior_label':x['plan_label'],'reviewed_label':label,'decision':'corrected','notes':dict(zip(CRITERIA,reasons)),'source_identity_sha256':digest(source_identity(source)),'source_record_ids':ids,'source_field_evidence':{rid:{'revision':source['release']['records'][rid]['revision'],'record_sha256':digest(source['release']['records'][rid])} for rid in ids},'prior_example_ref':{'path':str((S/'EXAMPLES.jsonl').resolve()),'line':line,'sha256':file_sha(S/'EXAMPLES.jsonl')},'prior_example_sha256':example_sha(x),'reviewer':{'id':'Codex-primary-agent-R135-source-adjudication','kind':'agent'},'unique_original_questions_added':0,'current_v2_v3_cohorts_modified':False,'compile_together_with_other_real_semantic_amendments':True,'optimization_allowed_before_amendments_compiled':False}
p=O/'AMENDMENT_266.json'
if p.exists():assert read(p)==evidence
else:p.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'path':str(p.relative_to(R)),'sha256':file_sha(p),'adjudicated':True,'new_unique_questions':0,'corpus_rebuilt':False}))
