"""Create and check design artifacts only. Never imports chatbot or calls models."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent

STAGES = [
    ('S00','receive'),('S01','pin_context'),('S02','scope_and_normalize'),
    ('S03','state_and_task_hypotheses'),('S04','candidate_discovery'),('S05','plan_proposal'),
    ('S06','validate_plan'),('S07','compile_read_graph'),('S08','read_sources'),
    ('S09','bounded_corrective_read'),('S10','evaluate_evidence'),('S11','execute_dependencies'),
    ('S12','resolve_unanswered_needs'),('S13','render'),('S14','verify_claims'),
    ('S15','safe_deterministic_output'),('S16','deliver_and_commit_state'),('S17','terminal'),
]
EDGES = [
    ('S00','S01','received'),('S01','S02','coherent_context'),('S02','S03','in_scope'),
    ('S02','S12','out_of_scope_or_uncertain_input'),('S03','S04','hypotheses_available'),
    ('S04','S05','candidate_descriptors_or_explicit_empty_scope'),('S05','S06','proposal_or_typed_plan'),
    ('S06','S07','accepted_plan_or_supported_independent_needs'),('S06','S12','invalid_ambiguous_or_budget_unavailable'),
    ('S07','S08','valid_read_graph'),('S07','S12','unsupported_or_broken_read_graph'),
    ('S08','S09','unread_declared_path_and_budget_remaining'),('S08','S10','no_corrective_pass_needed'),
    ('S09','S10','one_additional_read_completed_or_failed'),('S10','S11','need_results_available'),
    ('S11','S12','calculated_or_dependency_blocked'),('S12','S13','all_needs_have_explicit_result'),
    ('S13','S14','localized_output'),('S14','S16','claims_verified'),
    ('S14','S15','output_not_safe_to_assert'),('S15','S16','supported_independent_claims_or_explicit_temporary_failure'),
    ('S16','S17','delivery_status_recorded_state_commit_only_if_contract_allows'),
]
INVARIANTS = {
    'I01':'Every user need has an explicit terminal result; fields do not define the need set',
    'I02':'No supported derived claim has an unmet hard dependency',
    'I03':'Claims use authorized common facts or approved live observations, not legacy factual fallback',
    'I04':'Material qualifiers and explicit targets retain their meaning and binding',
    'I05':'Unknown is not false, closed, zero, free or allowed without evidence',
    'I06':'Complete lists require exhaustive scope receipts and stable pagination scope',
    'I07':'Ranking and model confidence do not override authority, applicability or validity',
    'I08':'Critical numbers, units, negation and exceptions survive normalization and localization',
    'I09':'State preserves intent references; facts are read again against current coherent snapshot',
    'I10':'Live mapping, freshness and observed_at are explicit; static data cannot replace live truth',
    'I11':'All branches share one deadline and attempt ledger',
    'I12':'Kind/task readiness is distinct from verified NLU and answer correctness',
}
FAMILIES = {
    'public_information':['center','contact','facility','person'],
    'inventory':['zone','equipment_model','resource','service','game_service'],
    'gameplay':['game','game_mode','control_set'],
    'fees':['audience','rate','rental_package'],
    'calendar':['schedule','closure'],
    'policy_and_procedure':['policy','procedure','faq'],
    'competition':['competition','competition_rule'],
    'news':['news'],'live':['live_binding'],
}
CASES = [
    ('C01','all_scope','ขอราคาบุคคลภายนอกทั้งหมด','Published offered-service scope and rates have explicit evidence','price table uses service set and preserves audience',['I01','I06','I07']),
    ('C02','follow_up','PC','Pending price/service slot and previously stated audience exist','fills service slot; preserves price intent and audience',['I04','I09']),
    ('C03','follow_up','ทั้งหมด','Pending task has a delivered candidate scope','selects full declared scope without inventing a new task',['I06','I09']),
    ('C04','paraphrase','Please tell me: Can I get a refund','Source policy matches the action and actor','wrapper does not cause blanket rejection of supported policy',['I01','I04']),
    ('C05','temporal','ตอนเย็นเปิดถึงกี่โมง','Schedule has explicit day-specific closing periods','uses temporal meaning; shows day differences or asks only material day slot',['I01','I04']),
    ('C06','relation','VALORANT ใช้ผู้เล่นกี่คน','Linked game_mode has count facts','reads mode relation; does not require unrelated optional fields',['I01','I03']),
    ('C07','ambiguity','ROV ถ้าเกมหลุดทำยังไง','General-play and competition contexts give materially different actions; no prior context','asks which context, not a generic topic menu',['I01','I04']),
    ('C08','competition','ROV','Pending competition disconnect topic exists','inherits rule topic and resolves the selected game',['I04','I09']),
    ('C09','target_lock','กฎ CS2','CS2 requested; only VALORANT rule is in first candidates','does not answer another game; tries declared CS2 scope or reports exact gap',['I03','I04']),
    ('C10','all_scope','ขอเกมทั้งหมด','Declared complete offering set is larger than retrieval top K','enumerates full offering set or labels pagination',['I06']),
    ('C11','all_scope','มีเกมใน PS5 กับ Switch อะไรบ้าง','Same game is offered in both scopes','deduplicates or groups by requested offering scope explicitly',['I04','I06']),
    ('C12','partial','ราคาและวิธีจอง PC','Current rate unavailable; booking procedure supported','does not calculate price; answers independent booking need',['I01','I02','I07']),
    ('C13','dependency','มี 100 บาทเล่นได้นานแค่ไหน','No current eligible rate or billing rule','no derived play time from missing or expired rate',['I02','I05','I07']),
    ('C14','tuple_binding','PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก','Eligible rate facts exist for requested tuples','does not create unintended audience/service/duration cross product',['I04','I08']),
    ('C15','rental','เหมาเต็มวันราคาเท่าไร','Published rental package exists; no hourly-to-day conversion policy','reads package; does not infer rental price by multiplying hourly rate',['I03','I07','I08']),
    ('C16','calendar','วันนี้เปิดไหม','Opening predicate is explicitly confirmed for request local date','date plus confirmed opening status in concise answer',['I04','I08']),
    ('C17','calendar','วันนี้เปิดไหม','Only empty bookable periods are known; physical opening unknown','does not infer physical closure from empty booking slots',['I05','I07']),
    ('C18','live','ตอนบ่ายสามมีเครื่องไหนว่างบ้าง','Fresh read-only provider observation with known mapping exists','lists verified free resources within requested scope',['I06','I10']),
    ('C19','live','PC ว่างไหมแล้วจองยังไง','Live provider unavailable; static booking procedure supported','reports live limitation and answers independent procedure',['I01','I02','I10']),
    ('C20','same_task_multi_subject','เกม A กับเกม B คือเกมอะไร','Both games have source-backed summaries','two subject-bound overview needs even though operation is the same',['I01','I04']),
    ('C21','rules','ก่อนกับหลัง First Blood ต่างกันยังไง','Relevant rule clauses with different conditions and dependencies exist','preserves both conditions and required exceptions',['I01','I04','I08']),
    ('C22','negation','ไม่ใช่บุคลากร PSU ใช้ราคาไหน','Audience information and eligibility rules exist','negation is preserved; does not pick PSU staff rate by substring',['I04','I08']),
    ('C23','authority','ราคานี้ใช่ไหม','FAQ and structured rate disagree without resolved claim authority','reports or resolves conflict only with applicable source-backed policy',['I03','I07']),
    ('C24','lifecycle','ราคา PC','Same service selected previously; rate has new published revision','re-reads amount from new release without asking service again',['I03','I09']),
    ('C25','lifecycle','ราคา PC','Selected service or rate was withdrawn after previous answer','does not resurrect value from history, alias or cache',['I03','I09']),
    ('C26','lifecycle','PC','Unrelated contact record changed epoch; service task unchanged','revalidates dependencies and preserves valid task slots',['I09']),
    ('C27','known_empty','มีอุปกรณ์ไหม','Explicit complete inventory is empty','may assert empty within that exact scope',['I05','I06']),
    ('C28','unknown','มีอุปกรณ์ไหม','Inventory completeness and members unknown','does not assert that no equipment exists',['I05']),
    ('C29','relation','เกม A เล่นที่ไหน','Game supported_platforms exists but studio offering relation does not','does not equate supported platform with installed studio offering',['I03','I05']),
    ('C30','localization','Explain the booking exception in English','Source permission and exception are supported; translation mode permitted','critical decision, amounts and exception remain unchanged',['I04','I08']),
    ('C31','failure','ขอข้อมูลกติกา','Model returns body that is not valid plan JSON','temporary/plan failure is not reported as absence of source facts',['I01','I11']),
    ('C32','failure','ขอราคาและกติกา','Shared budget exhausted while waiting for model','no recursive budget reset; finalizer reserve preserved',['I01','I11']),
    ('C33','lifecycle','เกมใหม่เล่นยังไง','New game uses supported kind with valid how_to_play source','data-only addition works without new name-specific regex',['I03','I12']),
    ('C34','capability','ขอสูตรโปรโมชั่นแบบใหม่','New record describes an unsupported billing operator','does not execute a model-invented business formula',['I03','I12']),
    ('C35','broken_relation','เกม A เล่นได้กี่คน','game_mode references a missing game or invalid platform','reports broken relation rather than guessing count',['I03','I05']),
    ('C36','scope_reset','ไม่ใช่ ขอวิธีจอง','Pending service-price clarification exists','replaces task explicitly instead of answering abandoned price intent',['I04','I09']),
    ('C37','partial_ambiguity','ศูนย์อยู่ที่ไหน แล้วราคาเท่าไร','Address supported; price has a material unresolved service/audience scope','reads and answers address while asking only necessary price slot',['I01','I02','I04']),
]

def main():
    spec = {
        'status':'design_only_not_implemented','version':'r97-flow-v2','timezone':'Asia/Bangkok',
        'stages':[{'id':sid,'name':name} for sid,name in STAGES],
        'edges':[{'from':a,'to':b,'condition':c} for a,b,c in EDGES],
        'terminal_stages':['S17'],'invariants':INVARIANTS,'kind_families':FAMILIES,
        'budgets':{'semantic_model_attempts_proposed':1,'additional_corrective_read_passes_proposed':1,'shared_request_deadline':True,'values_verified_in_runtime':False},
        'cases':[{'id':cid,'group':group,'utterance':q,'fixture_precondition':pre,'expected_behavior':expected,'required_invariants':inv,'executed':False} for cid,group,q,pre,expected,inv in CASES],
    }
    (OUT/'FLOW_SPEC.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
    sources = list((ROOT/'r96_paper_informed_flow_20261019').glob('*.md'))
    sources += [ROOT/'r96_paper_informed_flow_20261019'/n for n in ['SAVED_EVIDENCE_ANALYSIS.json','READ_ONLY_SOURCE_MANIFEST.json','LITERATURE_AND_SEARCH_LOG.json']]
    current = ROOT/'r95_merged_flow_implementation_20261018/system'
    sources += [current/n for n in ['app/knowledge/common/task_flow.py','app/knowledge/common/task_contracts.py','app/knowledge/common/task_proposer.py','app/knowledge/common/answer.py','app/knowledge/common/composition.py','app/knowledge/common/need_ledger.py','app/knowledge/common/registry.py','app/knowledge/common/provenance.py','app/knowledge/common/authority.py','app/knowledge/common/snapshot_provider.py','app/knowledge/common/followup_scope.py','app/pipeline/migrated_chat.py','app/pipeline/request_deadline.py','app/knowledge/common/catalog.json']]
    manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    manifest_path=OUT/'READ_ONLY_SOURCE_MANIFEST.json'
    if manifest_path.exists():
        old=json.loads(manifest_path.read_text(encoding='utf-8'))
        if old!=manifest:raise ValueError('Retained inputs changed; do not overwrite preservation evidence')
    else:manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    nodes={x['id'] for x in spec['stages']};adj={n:[] for n in nodes};problems=[]
    for edge in spec['edges']:
        if edge['from'] not in nodes or edge['to'] not in nodes:problems.append('unknown stage')
        else:adj[edge['from']].append(edge['to'])
    def descendants(n,stack=()):
        if n in stack:raise ValueError('Unexpected cycle; bounded passes must be explicit stage transitions')
        result={n}
        for target in adj[n]:result|=descendants(target,stack+(n,))
        return result
    unreachable=nodes-descendants('S00')
    dead=[n for n in nodes if not descendants(n)&set(spec['terminal_stages'])]
    catalog=json.loads((current/'app/knowledge/common/catalog.json').read_text(encoding='utf-8'))
    kinds={r['kind'] for r in catalog};mapped={k for v in FAMILIES.values() for k in v}
    case_ids=[r['id'] for r in spec['cases']]
    bad_refs=[(r['id'],i) for r in spec['cases'] for i in r['required_invariants'] if i not in INVARIANTS]
    local_links=[];fences=[];docs={}
    for p in OUT.glob('*.md'):
        text=p.read_text(encoding='utf-8');docs[p.name]={'lines':len(text.splitlines()),'characters':len(text)}
        if sum(line.startswith('```') for line in text.splitlines())%2:fences.append(p.name)
        for target in re.findall(r'\]\(([^)]+)\)',text):
            planned_qa=(p.parent/target).resolve()==(OUT/'DOCUMENT_QA.json').resolve()
            if '://' not in target and not (p.parent/target).exists() and not planned_qa:local_links.append([p.name,target])
    checks={'unknown_edges':problems,'unreachable_stages':sorted(unreachable),'stages_without_terminal_path':dead,'missing_catalog_kinds':sorted(kinds-mapped),'unknown_catalog_kinds':sorted(mapped-kinds),'invalid_invariant_references':bad_refs,'duplicate_case_ids':len(case_ids)!=len(set(case_ids)),'missing_local_links':local_links,'unbalanced_fences':fences}
    qa={'status':'PASS' if not any(checks.values()) else 'FAIL','scope':'document/design-spec consistency only; not chatbot behavior tests','checks':checks,'stages':len(nodes),'catalog_kinds':len(kinds),'review_scenarios':len(case_ids),'input_hashes':len(manifest),'documents':docs,'chatbot_tests_run':0,'runtime_modified':False}
    (OUT/'DOCUMENT_QA.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(qa,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
