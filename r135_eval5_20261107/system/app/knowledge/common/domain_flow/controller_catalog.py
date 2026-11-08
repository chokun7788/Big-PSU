"""Recorded input-device compatibility is separate from a console catalog.

Names are owner data. No platform-to-controller compatibility is inferred.
Only exact source relations, references and requested scope establish a row.
"""
import json,re
from .projection import value,title
from .scope import norm,contains,validity_allows

FACET='input_device_game'
DEVICE_NOUN=r'จอย|เกมแพด|พวงมาลัย|คีย์บอร์ด|เมาส์|\b(?:VR\s+(?:motion\s+)?controllers?|controllers?|gamepads?|racing wheel|keyboard\s+and\s+(?:mouse|mice)|keyboards?|mouse|mice)\b'
def model_key(text):return norm(str(text))
def platform_key(text):
    label=norm(str(text));key=re.sub(r'[^a-z0-9]','',label)
    aliases={'pc':'pc','ps5':'ps5','playstation5':'ps5','playstationps5':'ps5','nintendoswitch':'switch','switch':'switch','vr':'vr','cockpit':'cockpit'}
    return aliases.get(key,label)

def scoped_offer(index,offer,service,scopes):
    """The user's named service/resource/zone must lie on this offered path."""
    if scopes['service'] and service['record_id'] not in scopes['service']:return None
    refs=[];extra=[]
    if scopes['resource']:
        if not attested(index,offer,'installed_resource_ids') or not scopes['resource']&set(value(offer,'installed_resource_ids') or []):return None
        refs+=offer['fields']['installed_resource_ids']['evidence_refs'];extra+=sorted(scopes['resource']&set(value(offer,'installed_resource_ids') or []))
    if scopes['zone']:
        direct=set(value(service,'studio_zone_ids') or []) if attested(index,service,'studio_zone_ids') else set()
        if scopes['zone']&direct:refs+=service['fields']['studio_zone_ids']['evidence_refs'];extra+=sorted(scopes['zone']&direct)
        else:
            if not attested(index,service,'resource_ids'):return None
            resources=[index.records.get(rid,{}) for rid in value(service,'resource_ids') or []]
            matched=[r for r in resources if r.get('kind')=='resource' and attested(index,r,'zone_id') and value(r,'zone_id') in scopes['zone']]
            if not matched:return None
            refs+=service['fields']['resource_ids']['evidence_refs'];refs.extend(ref for r in matched for ref in r['fields']['zone_id']['evidence_refs']);extra.extend(r['record_id'] for r in matched);extra.extend(value(r,'zone_id') for r in matched)
    for rid in extra:
        r=index.records.get(rid,{})
        if r.get('kind') in {'resource','zone'}:
            if not attested(index,r,'name'):return None
            refs+=r['fields']['name']['evidence_refs']
    return {'refs':refs,'record_ids':sorted(set(extra))}

def grouping(index,service,kind):
    if kind=='platform':
        label=str(value(service,'platform'));return {'labels':{platform_key(label):{'th':label,'en':label}},'refs':service['fields']['platform']['evidence_refs'],'record_ids':[]}
    if kind!='zone':return {'labels':{},'refs':[],'record_ids':[]}
    refs=[];ids=[];resources=[]
    if attested(index,service,'studio_zone_ids') and value(service,'studio_zone_ids'):
        ids=value(service,'studio_zone_ids');refs+=service['fields']['studio_zone_ids']['evidence_refs']
    elif attested(index,service,'resource_ids'):
        for rid in value(service,'resource_ids') or []:
            r=index.records.get(rid,{})
            if r.get('kind')!='resource' or not attested(index,r,'zone_id'):return None
            ids.append(value(r,'zone_id'));resources.append(rid);refs+=r['fields']['zone_id']['evidence_refs']
        refs+=service['fields']['resource_ids']['evidence_refs']
    if not ids:return None
    labels={}
    for rid in ids:
        zone=index.records.get(rid,{})
        if zone.get('kind')!='zone' or not attested(index,zone,'name'):return None
        labels[rid]=title(zone);refs+=zone['fields']['name']['evidence_refs']
    return {'labels':labels,'refs':refs,'record_ids':sorted(set(ids+resources))}

def attested(index,record,key):
    from ..registry import pointer,source_errors
    field=record.get('fields',{}).get(key,{})
    if field.get('status')!='known' or not field.get('evidence_refs'):return False
    for ref in field['evidence_refs']:
        pair=index.source_pairs.get(ref.get('source_id'))
        try:
            if not pair or source_errors(*pair,demo=False) or record['kind'] not in pair[0]['authority_for'] or pair[0]['trust'] not in {'owner_confirmed','internal_verified','official'} or pointer(json.loads(pair[1]),ref['locator'])!=field['value']:return False
        except (ValueError,KeyError,TypeError,IndexError):return False
    return True

def request(index,question):
    catalog=r'เกม.{0,100}(?:มีอะไร|อะไรบ้าง|ไหน|ใด)|(?:ขอ|รายชื่อ)\s*เกม|กี่เกม|\b(?:which|what)\s+games?\b|\b(?:list|count|group)\b[^?.;]{0,60}\bgames?\b|\bhow many\s+games?\b|\bcompatible\s+games\b|\bgames\s+(?:list|compatible)\b'
    if not re.search(catalog,question,re.I):return None
    if not re.search(DEVICE_NOUN,question,re.I):return None
    from .named_spans import masked
    text=masked(index,question)
    device=re.search(DEVICE_NOUN,text,re.I)
    if not device:return None
    kind='vr_motion' if re.search(r'VR\s+(?:motion\s+)?controllers?',device[0],re.I) else 'racing_wheel' if re.search(r'racing wheel|พวงมาลัย',device[0],re.I) else 'keyboard_mouse' if re.search(r'keyboard|mouse|mice|คีย์บอร์ด|เมาส์',device[0],re.I) else 'gamepad'
    models=[]
    # Exact model names that the owner added work without another code alias.
    for r in index.records.values():
        model=value(r,'input_device_model') if r['kind']=='control_set' else None
        if model and not re.fullmatch(DEVICE_NOUN,str(model),re.I) and contains(text,str(model)):
            for m in re.finditer(re.escape(str(model)),text,re.I):
                adjacent=m.end()<=device.start() and not text[m.end():device.start()].strip() or m.start()>=device.end() and not text[device.end():m.start()].strip() or m.start()<=device.start() and device.end()<=m.end()
                if adjacent:models.append((m.start(),m.end(),m[0]))
    generic=bool(re.search(r'(?:จอย|เกมแพด|พวงมาลัย|คีย์บอร์ด|เมาส์)\s*(?:มีอะไร|อะไรบ้าง|ได้บ้าง|$)',text,re.I) or re.search(r'(?:with|using|use|supports?)\s+(?:(?:a|an|the)\s*)?$',text[:device.start()],re.I))
    if not models and not generic:
        patterns=[r'(?:with|using|use|supports?)\s+(?:(?:a|an|the)\s+)?(?P<model>[^?.!,;]{1,45}?)\s+(?:'+DEVICE_NOUN+r')',r'(?:จอย|เกมแพด|พวงมาลัย|คีย์บอร์ด|เมาส์)\s*(?P<model>[^?!,;]{1,35}?)(?=\s*(?:มีอะไร|อะไรบ้าง|มีเกม|เล่นเกม|เล่นได้|ใช้กับ|ได้บ้าง|บนเครื่อง|บน\s|ในโซน|$))',r'\b(?P<model>[^\s?!,;]+)\s+(?:'+DEVICE_NOUN+r')']
        for pattern in patterns:
            found=[m for m in re.finditer(pattern,text,re.I) if m['model'].strip().casefold() not in {'a','an','the','any','with','using','use','game','games','list','which','what','compatible','supported','recorded','all'}]
            if found:
                models=[(*m.span('model'),m['model'].strip()) for m in found];break
    models=list(dict.fromkeys(models));unique={model_key(x[2]) for x in models}
    error='multiple_controller_models_require_explicit_relation' if len(unique)>1 else None
    joined_text=re.sub(r'keyboard\s+and\s+(?:mouse|mice)','input_pair',text,flags=re.I)
    joined=re.search(r'(?:with|using|use|supports?|จอย|เกมแพด|พวงมาลัย|คีย์บอร์ด|เมาส์)\s+[^?.!,;]{0,60}(?:\bor\b|\band\b|หรือ|และ)[^?.!,;]{0,35}(?:'+DEVICE_NOUN+r'|มีอะไร|อะไรบ้าง)',joined_text,re.I)
    if joined:error='multiple_controller_models_require_explicit_relation'
    if re.search(r'ไม่ใช่|ไม่เอา|ยกเว้น|\b(?:not|without|except)\b',text,re.I):error='controller_exclusion_scope_not_resolved'
    a=min([device.start(),*[m[0] for m in models]]);b=max([device.end(),*[m[1] for m in models]])
    remaining=(question[:a]+' '*(b-a)+question[b:]).rstrip()
    count=bool(re.search(r'กี่เกม|\b(?:count|how many)\b',text,re.I));grouped=bool(re.search(r'\bgroup(?:ed)?\b.{0,30}\bgames?\b|\bby\s+(?:platform|zone)|แยกตาม|จัดกลุ่ม',text,re.I));by='zone' if re.search(r'\bby\s+zones?\b|ตามโซน',text,re.I) else 'platform' if re.search(r'\bby\s+platforms?\b|ตามแพลตฟอร์ม',text,re.I) else None
    if grouped and by is None:error='controller_grouping_field_missing'
    operation=('group_count' if count else 'group_list') if grouped else 'count' if count else 'list'
    return {'device_kind':kind,'model':next(iter(unique)) if len(unique)==1 else None,'model_quotes':[x[2] for x in models],'source_span':{'start':a,'end':b,'text':question[a:b]},'remaining_question':remaining,'error':error,'operation':operation,'group_by':by}

def platform_question(index,question):
    asked=request(index,question)
    return asked['remaining_question'] if asked else question

def selection(index,question,at):
    asked=request(index,question)
    if not asked:return None
    from .scope import reference_time
    at=reference_time(at)
    from .named_spans import masked
    from .temporal import parse as parse_date
    from .scope import requested_years
    from app.calendar.service_calendar import resolve_date_from_text
    date_text=masked(index,asked['remaining_question']);iso_dates=set(re.findall(r'(?<!\d)\d{4}-\d{1,2}-\d{1,2}(?!\d)',date_text));day=None
    if len(iso_dates)>1:asked['error']='multiple_controller_dates_require_separate_roles'
    elif iso_dates:
        from datetime import date
        try:
            y,m,d=map(int,next(iter(iso_dates)).split('-'));day=date(y-543 if y>=2400 else y,m,d)
        except ValueError:asked['error']='invalid_controller_reference_date'
    else:
        day,basis=parse_date(date_text,at.date())
        if basis=='invalid':asked['error']='invalid_controller_reference_date'
        if day is None:
            resolved=resolve_date_from_text(date_text,today=at.date())
            if resolved:day=resolved.target_date
        if day is None and requested_years(date_text):asked['error']='controller_year_requires_specific_date'
    if day:at=at.replace(year=day.year,month=day.month,day=day.day)
    from .dialogue_task import platforms,mentions
    from .game_scope import offerings
    explicit=set(platforms(index,asked['remaining_question']));games=set(mentions(index,question,{'game'}));scopes={kind:set(mentions(index,asked['remaining_question'],{kind})) for kind in ['service','resource','zone']};facts=[];proofs={};unknown=[];limits=[];groups={};labels={}
    if asked['error']:return {'request':asked,'facts':facts,'proofs':proofs,'unknown_control_ids':unknown,'limits':[asked['error']],'groups':groups,'group_labels':labels}
    for rid,r in index.records.items():
        if r['kind']!='control_set':continue
        game=index.records.get(value(r,'game_id'),{})
        if game.get('kind')!='game' or games and game['record_id'] not in games:continue
        if validity_allows({'validity':r.get('validity')},at) is False:continue
        control_platform=platform_key(value(r,'platform')) if value(r,'platform') else None
        if explicit and control_platform and control_platform not in {platform_key(p) for p in explicit}:continue
        offers=[(offer,service) for offer,service in offerings(index,game['record_id']) if not control_platform or control_platform==platform_key(value(service,'platform'))]
        offers=[(o,s) for o,s in offers if all(validity_allows({'validity':x.get('validity')},at) is not False for x in [o,s,game])]
        if not offers:continue
        actual_kind=value(r,'input_device');actual_model=value(r,'input_device_model')
        if actual_kind is not None and actual_kind!=asked['device_kind']:continue
        required=[(r,'game_id'),(r,'input_device'),(r,'platform'),(game,'title')]
        if asked['model']:required.append((r,'input_device_model'))
        if actual_kind is None or not control_platform or asked['model'] and actual_model is None or any(not attested(index,x,k) for x,k in required):unknown.append(rid);continue
        if actual_kind!=asked['device_kind'] or asked['model'] and model_key(actual_model)!=asked['model']:continue
        f=next((f for f in index.byrecord[rid] if f['category']=='C04' and f['facet']==FACET),None)
        if not f:unknown.append(rid);continue
        refs=[ref for x,k in required for ref in x['fields'][k]['evidence_refs']];paths=[];scope_records=[];member_groups={}
        for offer,service in offers:
            fields=[(offer,'game_id'),(offer,'service_id'),(offer,'offered'),(service,'platform')]
            if any(not attested(index,x,k) for x,k in fields):continue
            scope=scoped_offer(index,offer,service,scopes)
            if scope is None:continue
            refs+=scope['refs'];scope_records+=scope['record_ids']
            group=grouping(index,service,asked['group_by'])
            if group is None:unknown.append(rid);limits.append('controller_group_relation_unconfirmed');continue
            refs+=group['refs'];scope_records+=group['record_ids'];member_groups.update(group['labels'])
            refs.extend(ref for x,k in fields for ref in x['fields'][k]['evidence_refs']);paths.append([rid,game['record_id'],offer['record_id'],service['record_id']])
        if not paths:continue
        rows=[index.records[i] for path in paths for i in path]+[index.records[i] for i in scope_records]
        if any(validity_allows({'validity':x.get('validity')},at) is False for x in rows):continue
        uncertain=any(validity_allows({'validity':x.get('validity')},at) is not True for x in rows)
        if uncertain:limits.append('controller_relation_validity_unconfirmed')
        facts.append(f);proofs[f['id']]={'control_record_id':rid,'game_id':game['record_id'],'device_kind':actual_kind,'device_model':actual_model,'control_platform':value(r,'platform'),'requested_device_kind':asked['device_kind'],'requested_model':asked['model'],'requested_platforms':sorted(explicit),'requested_reference_time':at.isoformat(),'requested_source_scopes':{kind:sorted(ids) for kind,ids in scopes.items()},'source_paths':paths,'source_revisions':{x['record_id']:x['revision'] for x in rows},'recorded_validity':{x['record_id']:x.get('validity') for x in rows},'evidence_refs':list({(ref['source_id'],ref['locator']):ref for ref in refs}.values()),'validity_unconfirmed':uncertain,'console_platform_not_controller_proof':True}
        proofs[f['id']]['groups']=sorted(member_groups)
        for key,label in member_groups.items():groups.setdefault(key,set()).add(game['record_id']);labels[key]=label
    return {'request':asked,'facts':sorted(facts,key=lambda f:f['id']),'proofs':proofs,'unknown_control_ids':sorted(set(unknown)),'limits':sorted(set(limits+(['some_controller_compatibility_unknown'] if unknown else []))),'groups':{k:sorted(v) for k,v in groups.items()},'group_labels':labels}

def plan(index,category,question,at):
    if category!='C04':return None
    selected=selection(index,question,at)
    if selected is None:return None
    from .readers import confirmed,blocked
    if selected['request']['error']:result=blocked(category,selected['request']['error'],'missing_source' if selected['request']['error']=='controller_exclusion_scope_not_resolved' else 'missing_input')
    elif not selected['facts']:result=blocked(category,'controller_compatibility_not_recorded')
    else:result=confirmed(category,selected['facts'],'recorded_controller_game_offering_relation',operator=selected['request']['operation'],complete_set=not selected['unknown_control_ids'],catalog_member_ids=sorted({f['game_id'] for f in selected['facts']}))
    result.metadata['controller_catalog_scope']={k:v for k,v in selected.items() if k!='facts'};result.locked=True
    if selected['request']['group_by']:
        result.metadata.update(catalog_group_members=selected['groups'],catalog_group_counts={k:len(v) for k,v in selected['groups'].items()})
    if result.ids and selected['limits']:result.status='partial'
    return result

def scope_identity(scope):
    """Compare source semantics after a compiler-validated input derivation.

    Raw spans and masked question text describe the particular input location;
    the compiler/input-derivation receipts check their origin separately. They
    cannot be equal when a validated shared prefix moves into a child query.
    All selectors, join paths, source revisions, locators and limits still match.
    """
    if not isinstance(scope,dict):return None
    request=scope.get('request',{})
    return {**{k:v for k,v in scope.items() if k not in {'facts','request'}},
            'request':{k:v for k,v in request.items() if k not in {'source_span','remaining_question','model_quotes'}}}

def claim_errors(index,question,claims,at,declared=None,exact=True):
    selected=selection(index,question,at)
    if selected is None:return []
    expected={f['id']:f for f in selected['facts']};errors=[]
    if declared is not None and scope_identity(declared)!=scope_identity(selected):errors.append('controller_scope_receipt_changed')
    ids={c.get('fact_id') for c in claims}
    if ids-set(expected) or exact and ids!=set(expected):errors.append('controller_game_source_set_mismatch')
    for c in claims:
        f=expected.get(c.get('fact_id'));proof=selected['proofs'].get(c.get('fact_id'))
        if not f or not proof or c.get('facet')!=FACET or c.get('record_id')!=f['record_id'] or c.get('value') not in title(index.records[proof['game_id']]).values() or any(ref not in c.get('evidence_refs',[]) for ref in proof['evidence_refs']):errors.append('controller_game_relation_or_locator_unproven')
    return sorted(set(errors))

def delivery_errors(index,question,claims,at,needs=()):
    """Recompute each raw controller clause without another task's qualifiers."""
    from .request_verifier import clauses
    parts=clauses(question,index);owners=[p for p in parts if request(index,p['text'])]
    if not owners:return []
    controller_claims=[c for c in claims if c.get('facet')==FACET]
    supported=set();errors=[]
    for owner in owners:
        selected=selection(index,owner['text'],at)
        expected={f['id'] for f in selected['facts']}
        local=[c for c in controller_claims if c.get('fact_id') in expected]
        errors+=claim_errors(index,owner['text'],local,at,exact=False)
        supported.update(c.get('fact_id') for c in local)
        # Compatibility/FAQ claims need their own task's raw clause too. An
        # ordinary catalog cannot stand in for the input-device relation.
        local_needs=[n for n in needs if n.get('source_span') and n['source_span'] in owner['text']]
        for need in local_needs:
            if any(c.get('facet')!=FACET for c in need.get('claim_packets',[])):errors.append('controller_clause_has_non_controller_claims')
    if any(c.get('fact_id') not in supported for c in controller_claims):errors.append('controller_claim_has_no_matching_raw_clause')
    for claim in claims:
        if claim.get('facet')==FACET:continue
        # Legacy projected categories are not a semantic scope certificate:
        # the retained console FAQ is in fact projected as C03/owner_policy.
        unrelated=any(need.get('source_span') and need['source_span'] in part['text'] and not request(index,part['text']) and claim in need.get('claim_packets',[]) for need in needs for part in parts)
        if not unrelated:errors.append('console_catalog_does_not_prove_controller_clause')
    if not needs:
        # Legacy readers have no per-task packets. Recheck the complete claim
        # set when the whole input is one controller clause, including a FAQ.
        if len(parts)==1:errors+=claim_errors(index,question,claims,at,exact=False)
        elif any(index.byid.get(c.get('fact_id'),{}).get('category')=='C04' and c.get('facet')!=FACET for c in claims):errors.append('unscoped_controller_compatibility_claim')
    return sorted(set(errors))

def notice(lang):return 'ยังไม่มีข้อมูลยืนยันว่าเกมใดรองรับอุปกรณ์ควบคุมรุ่นที่ถาม รายชื่อเกมบนเครื่องอย่างเดียวใช้ยืนยันรุ่นจอยไม่ได้ครับ' if lang=='th' else 'The recorded sources do not confirm games for the requested controller. A console game list alone does not establish controller compatibility.'
