"""Task-first orchestration over common snapshots and existing typed readers.

Unknown interpretations stay explicit. Compatibility paths are identified in
the trace; neither path can read legacy facts or create business policy.
"""
from dataclasses import dataclass, asdict, replace
import re, time
from .registry import value, CATALOG
from .query_contract import normalize, strip_names, live_request, resolve_fields, unresolved_clauses, resolution_uncertain
from .task_contracts import TASKS, fields_for

@dataclass
class TaskPlan:
    task: str
    record_ids: list
    requested_fields: list
    operation: str
    acceptance_path: str
    bindings: list
    slots: dict
    qualifiers: list
    unresolved_spans: list
    all_fields: bool = False

def _match(pattern,q):return bool(re.search(pattern,q,re.I))

def typed_task(question,ids,records,names):
    """Task language independent of owner record names and factual values."""
    from .task_interpretation import interpret
    kinds={records[k]['kind'] for k in ids};q=normalize(question)
    for group in [ids,[k for k in ids if records[k]['kind']=='game']]:
        profile=interpret(question,group,records,names)
        if profile and profile['task'] in TASKS:return profile['task'],'whole_task_contract'
    if 'game' in kinds:
        if _match(r'ปุ่ม|ควบคุม|กดอะไร|\b(?:controls?|buttons?|bindings|jump|sprint|crouch)\b',q):return 'game_controls','typed_action'
        if _match(r'กี่คน|ผู้เล่น|เล่น.{0,12}ด้วยกัน|\b(?:players?|multiplayer|play together)\b',q):return 'game_players','typed_players'
        if _match(r'เวอร์ชัน|\b(?:installed version|game version)\b',q):return 'game_version','typed_version'
        if _match(r'บัญชี|\b(?:account|login|log in)\b',q):return 'game_account','typed_account'
        if _match(r'โซนไหน|มีให้เล่น|มีเกมนี้|ติดตั้ง|\b(?:where can|which zone|offered|installed|have this game)\b',q):return 'game_at_studio','typed_offering'
        if _match(r'แพลตฟอร์ม|เครื่องไหน|\b(?:platforms?|available on)\b',q):return 'game_platforms','typed_platform'
        if _match(r'วิธีเล่น|เล่นยังไง|เล่นอย่างไร|\b(?:how (?:do|can) (?:i|you) play|how to play|gameplay)\b',q):return 'game_how_to_play','typed_how_to'
        if _match(r'เป็นเกม|คือเกม|แนวเกม|เกี่ยวกับอะไร|\b(?:what (?:kind|type) of game|game about|overview|introduction|genre|what is)\b',q):return 'game_overview','typed_overview'
    if 'equipment_model' in kinds:
        if _match(r'โซนไหน|อยู่ที่ไหน|\b(?:which zone|what zone|where.*located)\b',q):return 'equipment_location','typed_equipment_location'
        if _match(r'คือ(?:อุปกรณ์)?อะไร|อุปกรณ์อะไร|\b(?:what is|what kind|what type|explain|describe)\b',q):return 'equipment_explain','typed_equipment_explain'
        if _match(r'สเปก|รุ่น|\b(?:specs?|specifications?|hardware|model)\b',q):return 'equipment_specs','typed_specs'
    if kinds&{'zone','service','resource'}:
        if _match(r'อุปกรณ์|\b(?:equipment|hardware)\b',q):return 'equipment_list','typed_equipment_list'
        if _match(r'กี่คน|\b(?:capacity|how many (?:people|players))\b',q):return 'resource_capacity','typed_capacity'
        if _match(r'กี่นาที|กี่ชั่วโมง|นานแค่ไหน|\b(?:how long|session duration|reserved duration)\b',q):return 'service_duration','typed_duration'
    if 'center' in kinds:
        if _match(r'ใคร.{0,10}(?:ดูแล|ดำเนิน|เจ้าของ)|ของมหาวิทยาลัย|\b(?:who (?:runs?|operates?|owns?|manages?)|operated by|operator)\b',q):return 'center_operator','typed_operator'
        if _match(r'อยู่(?:ตรง|ที่)?ไหน|ที่อยู่|ตึก|อาคาร|ชั้น|แผนที่|\b(?:where|address|located|location|building|floor|map)\b',q):return 'center_location','typed_location'
        if _match(r'คืออะไร|\b(?:what is|overview|about)\b',q):return 'center_overview','typed_center'
    if 'person' in kinds and _match(r'ใคร|บุคลากร|ทีมงาน|สมาชิก|\b(?:who|staff|members?|team|role)\b',q):return 'people','typed_directory'
    if 'contact' in kinds and _match(r'ติดต่อ|โทร|เพจ|\b(?:contact|phone|email|facebook)\b',q):return 'contact','typed_contact'
    if 'facility' in kinds and _match(r'จอดรถ|ที่พัก|ที่นั่ง|\b(?:parking|rest|seating|facility|facilities)\b',q):return 'facility','typed_facility'
    return None,None

def _compatible_remainder(question,ids,records,names,task,basis):
    """Keep meaningful conditions; never waive unknown qualification wholesale."""
    q=strip_names(question,ids,names)
    if _match(r'\b(?:if|unless|except|without|only)\b|ถ้า|ยกเว้น|เฉพาะ|ไม่(?:ใช่|เอา|ต้อง)|ห้าม',q):return False
    if basis=='whole_task_contract':return True
    fields=resolve_fields(q,{records[k]['kind'] for k in ids})[0]
    if fields and not unresolved_clauses(q,{records[k]['kind'] for k in ids}) and not resolution_uncertain(q,{records[k]['kind'] for k in ids}):return True
    # Descriptive tasks use complete reusable sentence grammar, not source IDs.
    q=re.sub(r'^(?:(?:could|can|would) you\s+)?(?:please\s+)?','',q)
    q=re.sub(r'(?:ครับ|ค่ะ|หน่อย|นะครับ|please|[?!.,])+\s*$','',q).strip()
    patterns={
      'center_operator':r'(?:who (?:runs?|operates?|owns?|manages?)(?: the)?(?: studio|center|centre)?|(?:ศูนย์)?เป็นของ(?:ใคร|มหาวิทยาลัย)|ใคร(?:เป็นเจ้าของ|ดูแล|ดำเนินการ)(?:ศูนย์)?)',
      'center_location':r'(?:(?:where (?:is|are)(?: the)?|address|location|building|floor|map)(?: studio|center|centre)?|(?:ศูนย์)?(?:อยู่(?:ตรง|ที่)?ไหน|ที่อยู่|อยู่ตึกอะไร|อยู่ชั้นไหน|แผนที่))',
      'game_players':r'(?:(?:ใช้)?(?:ผู้เล่น)?กี่คน|how many (?:players|people)(?: (?:can|may) play)?|player count)',
      'equipment_explain':r'(?:คือ(?:อุปกรณ์)?อะไร|เป็นอุปกรณ์อะไร|what (?:is|kind of equipment is|type of device is)(?: this)?|(?:explain|describe)(?: this)?(?: equipment|device)?)',
      'equipment_location':r'(?:(?:which|what) zone (?:has|is|contains)(?: this equipment)?|where is(?: located)?|อยู่(?:ที่)?โซนไหน|โซนไหนมี)',
      'game_overview':r'(?:(?:what (?:kind|type) of game is|what is|tell me about|describe|explain)(?: this game)?|(?:คือเกมอะไร|เป็นเกมอะไร|เกมแนวไหน|แนะนำเกม|อธิบายเกม))',
      'game_how_to_play':r'(?:เล่นยังไง|เล่นอย่างไร|วิธีเล่น|how to play|how (?:do|can) (?:i|you) play(?: this game)?)',
      'game_at_studio':r'(?:(?:เล่นได้ที่|อยู่|มีให้เล่นที่)?โซนไหน|มีให้เล่นไหม|มีเกมนี้ไหม|where can (?:i|you) play(?: this game)?|which zone(?: is it in)?|(?:is|do you have)(?: this game)?(?: available)?(?: at the studio)?)',
      'people':r'(?:who (?:are|is)(?: the)?(?: studio)?(?: members|staff|team)|(?:บุคลากร|ทีมงาน|สมาชิก)(?:มีใครบ้าง|คือใคร))',
    }
    return bool(task in patterns and re.fullmatch(patterns[task],q,re.I))

def _root_candidates(question,records,names,history):
    from .answer import context_query
    from .identity_links import resolve
    q,ids,method=context_query(question,history,names,records)
    ids,names,audit=resolve(question,ids,records,names)
    return ids,names,method

def _implicit_subject(question,records):
    q=normalize(question);kind=None
    if _match(r'\b(?:who (?:operates|runs|owns|manages)|where is (?:the )?(?:studio|center)|studio address)\b|ศูนย์.{0,10}(?:อยู่(?:ตรง|ที่)?ไหน|ของใคร)|ที่อยู่ศูนย์|อยู่ตึก|อยู่ชั้น',q):kind='center'
    elif _match(r'\b(?:studio members|studio staff|staff members|studio team)\b|บุคลากร|ทีมงาน',q):kind='person'
    elif _match(r'\b(?:contact (?:you|the studio)|phone number|studio email)\b|ติดต่อศูนย์|เบอร์โทร|เพจศูนย์',q):kind='contact'
    if not kind:return []
    ids=[k for k,r in records.items() if r['kind']==kind]
    if kind=='person':ids=[k for k in ids if not _match(r'not public|internal only|private profile|ห้ามเผยแพร่|ภายในเท่านั้น',str(value(records[k],'public_scope') or ''))]
    return ids if len(ids)==1 or kind=='person' else []

def _select_task(question,records,names,ids,allow_llm,diagnostic):
    task,basis=typed_task(question,ids,records,names)
    if task:
        selected=[k for k in ids if records[k]['kind'] in TASKS[task].kinds]
        if selected and _compatible_remainder(question,selected,records,names,task,basis):return task,selected,'deterministic:'+basis
    from .query_scope import operation
    if operation(question) in {'policy','booking','checkin','calendar','rental','price','rules'}:
        diagnostic({'stage':'task_dispatch','path':'compat_typed_qualifiers','reason':'reuse_existing_sensitive_task_parser_without_extra_model_call'})
        return None
    if ids and len({records[k]['kind'] for k in ids})==1:
        kinds={records[k]['kind'] for k in ids};residue=strip_names(question,ids,names)
        fields,_=resolve_fields(residue,kinds)
        if fields and not unresolved_clauses(residue,kinds) and not resolution_uncertain(residue,kinds) and not _match(r'\d|ถ้า|ยกเว้น|ไม่|ห้าม|\b(?:if|unless|except|not|without)\b',residue):
            from .planner import allowed_schema
            _,allowed,_=allowed_schema(ids,records)
            if set(fields)<=allowed:return 'schema_attributes',ids,'deterministic:typed_schema_attributes'
    if not allow_llm:return None
    residue=strip_names(question,ids,names)
    semantic_sensitive=r'\d|\b(?:if|unless|except|only|not|without|before|after|and|or|children|kids|newest|latest|spoilers?|pay|paid|payment|refund|my|own|personal)\b|ถ้า|ยกเว้น|เฉพาะ|ห้าม|ไม่ได้|ไม่เอา|และ|หรือ|เด็ก|ล่าสุด|ชำระ|จ่าย|คืนเงิน|ส่วนตัว|ตัวเอง|ของผม|ของฉัน'
    if _match(semantic_sensitive,residue):
        diagnostic({'stage':'task_acceptance','path':'compatibility','reason':'sensitive_qualifiers_require_typed_domain_contract'})
        return None
    from .entity_search import candidates, topic_alignment
    from .answer import title
    roots=[k for k in ids if records[k]['kind'] in {'game','equipment_model','resource','service','zone','center','contact','facility','person','audience','competition','news','faq','policy','procedure'}]
    rows=[{'record_id':k,'kind':records[k]['kind'],'name':title(records[k],'en'),'text':''} for k in roots[:8]]
    if not rows:
        rows=[r for r in candidates(question,records,names) if topic_alignment(question,records[r['record_id']])[0]][:8]
    if not rows:return None
    from .task_proposer import propose
    p=propose(question,rows,diagnostic=diagnostic)
    if not p:return None
    selected=p['record_id'];task=p['task'];kinds={records[selected]['kind']}
    # Sensitive policy, fee, exception and temporal interpretations retain the
    # existing typed qualifier engines until independently supported.
    if TASKS[task].operation in {'price','policy','booking','calendar','rules','live'}:return None
    if task in {'game_overview','game_how_to_play'} and _match(r'\b(?:name|time|named|price|free|cost)\b|ชื่ออะไร|ราคา|ฟรี',residue):return None
    if roots and selected not in roots:return None
    # The operation can cross schema fields only through the task's declared
    # relationship. It cannot request arbitrary extra fields from the model.
    if not fields_for(task,[selected],records):return None
    if task in {'people','contact','facility','center_operator','center_location','center_overview'} and roots and kinds&{'game','service','resource'}:return None
    diagnostic({'stage':'task_acceptance','path':'semantic','task':task,'record_id':selected,'quotes':{'task':p['task_quote'],'subject':p['subject_quote']},'human_semantics_verified':False})
    return task,[selected],'semantic:bounded_task_contract'

def answer(reader,question,*,snap,locale,history=None,at=None,allow_llm=True,diagnostic=None):
    """Return an answer only for an accepted task. None means explicit compat."""
    from .answer import effective
    from .authority import scoped_names,classify,field_ownership
    from .query_scope import derived_names
    from app.calendar.service_calendar import now_bangkok
    started=time.perf_counter();at=at or now_bangkok();lang=locale
    diagnostic=diagnostic or reader.diagnostics.append
    records={k:r for k,r in snap['release']['records'].items() if k not in snap['withdrawn']}
    names=derived_names(scoped_names(snap),records)
    # A unique center name before an explicit location suffix remains a name,
    # e.g. an owner-entered "Studio name - campus". Derive it from data.
    heads={}
    for rid,r in records.items():
        if r['kind']!='center':continue
        for alias in names.get(rid,[]):
            head=re.split(r'\s+[-–—]\s+',alias,maxsplit=1)[0].strip()
            if len(head)>=10 and head!=alias:heads.setdefault(head,[]).append(rid)
    for head,owners in heads.items():
        if len(set(owners))==1:
            rid=owners[0];names[rid]=list(dict.fromkeys([*names.get(rid,[]),head]))
    if live_request(question):
        diagnostic({'stage':'task_dispatch','task':'live_status','path':'compat_typed_live_adapter'});return None
    from .open_day import answer as open_day
    result=open_day(reader,snap,started,question,lang,at,records)
    if result is not None:
        result.decision_artifact['task_flow']={'version':'r95','path':'typed_calendar_adapter','task':'schedule'}
        return result
    # Safe domain executors already enforce package/edition/date constraints.
    from .rental_bridge import answer as rental_answer
    result=rental_answer(reader,snap,started,question,lang,records,history,at)
    if result is not None:
        result.decision_artifact['task_flow']={'version':'r95','path':'typed_rental_adapter','task':'rental'}
        return result
    ids,names,method=_root_candidates(question,records,names,history)
    if any(k not in records for k in ids):
        diagnostic({'stage':'task_dispatch','path':'compat_withdrawn_reference','record_ids':ids})
        return None
    implicit=_implicit_subject(question,records)
    if implicit and ids and all(records[k]['kind']=='faq' for k in ids):
        # A generic FAQ alias such as "where" must not hide an explicit
        # center attribute when the published center has its own typed fields.
        task,basis=typed_task(question,implicit,records,names)
        if task in {'center_location','center_operator'} and _compatible_remainder(question,implicit,records,names,task,basis):ids=implicit
    if not ids:ids=_implicit_subject(question,records)
    # Explicitly retain precise confirmation/qualification and pending slot
    # handling in the compatibility contract; do not start a new vague task.
    if history and len(question.strip())<35:
        diagnostic({'stage':'task_dispatch','path':'compat_pending_context'});return None
    # Recognized price and competition paths are accepted as typed domain
    # contracts by the original domain parser, not a model-selected field set.
    if _match(r'ราคา|ค่าบริการ|กี่บาท|\b(?:price|cost|fees?|rates?|budget|how much)\b',question):
        diagnostic({'stage':'task_dispatch','task':'price','path':'compat_typed_price_slots'});return None
    if _match(r'กฎ|กฏ|กติกา|แข่ง|\b(?:competition|tournament|rulebook|rules)\b',question):
        diagnostic({'stage':'task_dispatch','task':'competition_or_policy','path':'compat_typed_rule_qualifiers'});return None
    selected=_select_task(question,records,names,ids,allow_llm,diagnostic)
    if not selected:return None
    task,ids,path=selected
    # Restrict profile and identity records to the requested semantic role.
    if any(k not in records for k in ids):return None
    if task=='game_players':
        modes=[r for r in records.values() if r['kind']=='game_mode' and value(r,'game_id') in ids]
        if not modes:
            from .answer import title
            body=('ยังไม่มีข้อมูลยืนยันจำนวนผู้เล่นหรือโหมดเกมสำหรับ ' if lang=='th' else 'The common data does not confirm player counts or game modes for ')+ ' / '.join(title(records[k],lang) for k in ids)
            return reader.finish(snap,started,body,[],{'record_ids':ids,'requested_fields':[],'operation':'read','method':'r98_game_mode_missing','missing_relation':'game_mode.game_id','source_answer_confirmed':False},[],response='unconfirmed')
    requested=resolve_fields(strip_names(question,ids,names),{records[k]['kind'] for k in ids})[0] if task=='schema_attributes' else fields_for(task,ids,records)
    if not requested:return None
    if task=='game_overview':
        requested=['summary']+(['genre'] if all(value(records[k],'genre') is not None for k in ids) else [])
    if task=='game_players':
        explicit_counts=resolve_fields(strip_names(question,ids,names),{'game_mode'})[0]
        requested=[f for f in ('players_min','players_max') if f in explicit_counts] or ['players_min','players_max']
        if any(value(r,'mode_name') is not None for r in modes):requested.append('mode_name')
    q=strip_names(question,ids,names)
    explicit,_=resolve_fields(q,{records[k]['kind'] for k in ids})
    if task in {'center_location','contact','facility','equipment_specs','service_duration','resource_capacity'}:
        scoped=[f for f in explicit if f in requested]
        if scoped:requested=scoped
    qualifiers=[m.group() for m in re.finditer(r'\d+(?:[:./-]\d+)*|\b(?:not|except|only|unless|before|after)\b|ไม่|ยกเว้น|เฉพาะ|ก่อน|หลัง',question,re.I)]
    plan=TaskPlan(task,ids,requested,TASKS[task].operation,path,[{'source':'normalized_query','quote':question}],{},qualifiers,[])
    read={'record_ids':ids,'scope_ids':ids,'requested_fields':requested,'operation':plan.operation,'all_fields':False,'method':'common_r95_task_plan','platform':None,
        'task_plan':asdict(plan),'unresolved_clauses':[],'read_contract':{'schema_version':'task_needs_v2','needs':[{'id':task,'source_span':question,'required_fields':requested,'dependencies':[]}],'semantic_correctness_verified':False}}
    read['authority']=classify(question,snap,ids)
    if read['authority']['decision']!='common':return None
    read['field_authority']=field_ownership(snap,ids,requested)
    if task=='equipment_list':
        from .equipment_bridge import answer as equipment_answer
        result=equipment_answer(reader,snap,started,question,lang,records,ids,at,task_contract={'task':'equipment_list','whole_task_covered':True})
        if result is not None:
            result.decision_artifact.setdefault('query_plan',{})['task_plan']=asdict(plan)
            result.decision_artifact['task_flow']={'version':'r95','path':path,'task':task};return result
    # Honor explicit platform without inferring it from a game title.
    from .query_scope import same_platform
    platforms={value(r,'platform') for r in records.values() if isinstance(value(r,'platform'),str)}
    for platform in sorted(platforms,key=len,reverse=True):
        if re.search(r'(?<![a-z0-9])'+re.escape(platform.casefold())+r'(?![a-z0-9])',q):read['platform']=platform;break
    result=reader.execute_task(question,snap=snap,at=at,lang=lang,plan=read)
    result.decision_artifact['task_flow']={'version':'r95','path':path,'task':task,'executor':'shared_common_reader'}
    result.decision_artifact['task_need_graph']={'version':1,'needs':[{'id':task,'source_span':question,'required_fields':requested,'dependencies':[],'status':result.decision_artifact.get('response_type')}], 'coverage_basis':'accepted task contract; not inferred solely from selected fields','human_semantic_correctness_verified':False}
    return result
