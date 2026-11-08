"""Legacy rental language/selection behavior; facts exclusively from common.

Uses the old pure grammar helpers. Catalog members, prices, equipment and
source pointers are read from the current snapshot, never legacy JSON files.
"""
import copy,re
from .registry import value
from .query_contract import normalize,matches,live_request
from app.pipeline.zone_rental import _selection,_periods,_asks,RENTAL,HALF,FULL,PRICE,HOURLY,RETURN,NEGATIVE

def catalog(records):
    packages={k:r for k,r in records.items() if r['kind']=='rental_package'}
    zones={z for r in packages.values() for z in (value(r,'zone_ids') or []) if z in records}
    groups={value(r,'audience_id') for r in packages.values() if value(r,'audience_id') in records}
    labels={}
    for zid in zones:
        z=records[zid];name=value(z,'name') or {};words=list(name.values()) if isinstance(name,dict) else [name]
        words+=sum(z.get('aliases',{}).values(),[])
        for sid,s in records.items():
            if s['kind']=='resource' and value(s,'zone_id')==zid:
                for service in records.values():
                    if service['kind']=='service' and sid in (value(service,'resource_ids') or []):words.append(value(service,'platform'))
        labels[zid]=list(dict.fromkeys(normalize(w) for w in words if isinstance(w,str) and w))
        # A noun head from an actual zone label, not a fixed list of devices.
        labels[zid]+= [w[:-5].strip() for w in labels[zid] if w.endswith(' zone')]
        labels[zid]+= [re.sub(r'playstation\s*(\d+)',r'ps\1',w) for w in labels[zid] if re.search(r'playstation\s*\d+',w)]
    return packages,sorted(zones),sorted(groups),labels

def zone_selection(q,zones,labels):
    patterns=[(rid,'|'.join((r'(?<![a-z0-9])' if re.match('[a-z0-9]',s) else '')+re.escape(s)+(r'(?![a-z0-9])' if re.search('[a-z0-9]$',s) else '') for s in sorted(set(labels[rid]),key=len,reverse=True))) for rid in zones]
    bundle=[z for z in zones if any(re.search(r'\ball zones\b|ทุกโซน',s) for s in labels[z])]
    if re.search(r'ทุกโซน|ทั้งศูนย์|ทั้งห้อง|\ball zones\b|\b(?:entire|whole)\s+(?:studio|venue|room)\b',q):return bundle,True
    if re.search(r'ทุกแพ็กเกจ|ทุกแบบ|แต่ละโซน|ราคาทั้งหมด|\ball (?:rental )?(?:packages|prices|rates)\b|\beach zone\b',q):
        negative={rid for rid,pattern in patterns for m in re.finditer(pattern,q,re.I) if NEGATIVE.search(q[:m.start()])}
        return [rid for rid in zones if rid not in negative],False
    return _selection(q,patterns,zones),False

def group_selection(q,groups,records):
    from .audience_scope import resolve,organization_groups
    selected,audit=resolve(q,records)
    selected=[rid for rid in (selected or []) if rid in groups]
    if re.fullmatch(r'(?:ภายใน|ภายนอก|internal|external)[.!?\s]*',q):
        side='internal' if q.strip(' .!?') in {'ภายใน','internal'} else 'external'
        selected=[rid for rid in groups if side in organization_groups(' '.join((value(records[rid],'name') or {}).values()))]
    negative=bool(re.search(r'ไม่เอา|ยกเว้น|\b(?:not|except|excluding)\b',q))
    if negative and not selected:
        excluded,_=resolve(re.sub(r'ไม่เอา|ยกเว้น|ไม่ใช่|\b(?:not|except|excluding)\b',' ',q),records)
        if excluded:selected=[rid for rid in groups if rid not in excluded]
    if re.search(r'ทั้งสองกลุ่ม|ทั้งภายในและภายนอก|\bboth (?:groups|organization types)\b',q):selected=list(groups)
    return selected

def previous(history):
    from .followup_scope import delivered_state
    state=delivered_state(history) or {};p=state.get('request_contract')
    if not isinstance(p,dict) or p.get('version')!=1 or p.get('domain')!='rental':return None
    requests=p.get('requests');asks=p.get('asks')
    if not isinstance(requests,list) or not 1<=len(requests)<=6 or not isinstance(asks,list) or any(a not in {'rates','capacity','equipment','duration_definition','effective_date','booking','overtime','per_unit','eligibility','hourly_rental','multi_day','custom_package','scope_clarification'} for a in asks):return None
    for row in requests:
        if not isinstance(row,dict) or set(row)!={'zones','audiences','periods'}:return None
        if any(not isinstance(row[k],list) or not row[k] or len(row[k])>100 or any(not isinstance(v,str) for v in row[k]) for k in row):return None
        if any(p not in {'half_day','full_day'} for p in row['periods']):return None
    return copy.deepcopy(p)

def parse(question,history,records):
    q=normalize(question);packages,zones,groups,labels=catalog(records)
    if not packages:return None
    prior=previous(history)
    explicit=bool(RENTAL.search(q) or ((HALF.search(q) or FULL.search(q)) and PRICE.search(q)))
    if live_request(q):return None
    from app.session.conversation_plan import OTHER_TASK,SCHEDULE_TASK,CANCEL
    if CANCEL.search(q) and prior and not explicit:return {'action':'cancel'}
    if not explicit and (OTHER_TASK.search(q) or SCHEDULE_TASK.search(q)):return None
    selected,bundle=zone_selection(q,zones,labels);audiences=group_selection(q,groups,records);periods=_periods(q)
    asks=_asks(q,default_rates=False)
    bare=bool(re.fullmatch(r'ทั้งหมด(?:เลย)?|ทุกแบบ|all(?: of them)?|both(?: periods)?|ภายใน|ภายนอก|internal|external',q.strip(' .!?')))
    information=bool(set(asks)&{'capacity','equipment','duration_definition','effective_date','booking','overtime'})
    if prior and not explicit and not selected and re.fullmatch(r'(?:xbox\w*|ps\s*\d+)',q):return {'action':'unknown_target','unresolved':[question]}
    if not explicit and not (prior and (selected or audiences or periods or bare or information or PRICE.search(q))):return None
    if prior and any(z not in zones or a not in groups for r in prior['requests'] for z in r['zones'] for a in r['audiences']):return {'action':'expired'}
    # Unknown numbered devices cannot silently select all recorded packages.
    numbered=re.findall(r'\b(?:ps\s*\d+|playstation\s*\d+|xbox\w*)\b',q)
    if explicit and not selected and numbered:return {'action':'unknown_target','unresolved':numbered}
    if explicit and bundle and re.search(r'ยกเว้น|ไม่เอา|\b(?:except|excluding|without)\b',q):return {'action':'custom_package'}
    if explicit and re.search(r'\d+\s*(?:ชั่วโมง|hours?|hrs?)',q) and not HALF.search(q) and not FULL.search(q):return {'action':'custom_package'}
    inherited=bool(prior and not explicit) or bool(prior and explicit and re.search(r'^(?:แล้ว|และ|what about|and|return to|back to)',q))
    base=copy.deepcopy(prior['requests']) if inherited else [{'zones':zones,'audiences':groups,'periods':['half_day','full_day']}]
    if inherited and len(base)>1 and selected:
        if not set(selected)<=set(z for row in base for z in row['zones']):return {'action':'scope_clarification'}
        base=[{**row,'zones':[z for z in row['zones'] if z in selected]} for row in base if set(row['zones'])&set(selected)]
    if bare and re.search(r'ทั้งหมด|ทุกแบบ|\ball\b',q):selected=list(zones)
    if bare and re.search(r'\bboth(?: periods)?\b',q):periods=['half_day','full_day']
    for row in base:
        if selected:row['zones']=selected
        if audiences:row['audiences']=audiences
        if periods:row['periods']=periods
    # Preserve target/group/period tuples, using the legacy per-clause rule.
    pieces=re.split(r'\s*(?:และ|;|\band\b|\bversus\b|\bvs\.?\b)\s*',q,flags=re.I)
    scoped=[]
    for piece in pieces:
        child_z,_=zone_selection(piece,zones,labels)
        if child_z:scoped.append({'zones':child_z,'audiences':group_selection(piece,groups,records) or audiences or base[0]['audiences'],'periods':_periods(piece) or periods or base[0]['periods']})
    if len(scoped)>1:base=scoped
    if len(base)>6:return {'action':'scope_clarification'}
    # Explicit personal eligibility never becomes an organizational audience.
    if 'eligibility' in asks:return {'action':'eligibility'}
    return {'version':1,'domain':'rental','requests':base,'asks':asks or (prior['asks'] if inherited else ['rates']),
            'context_used':inherited,'original_query':question,'action':'read'}

def answer(reader,snap,started,question,lang,records,history,at):
    contract=parse(question,history,records)
    if contract is None:return None
    from .answer import title,text,effective
    messages={
      'cancel':('ยกเลิกหัวข้อราคาเหมาแล้วครับ ต้องการถามเรื่องใดต่อได้เลย','Rental pricing context cleared. You can ask a new question.'),
      'expired':('รายการในขอบเขตเดิมถูกเปลี่ยนหรือถอน กรุณาระบุโซนและกลุ่มผู้ใช้ใหม่ครับ','The previous scope was changed or withdrawn. Please specify the zone and audience again.'),
      'unknown_target':('ยังไม่พบโซนที่ตรงกับอุปกรณ์ที่ระบุ กรุณาระบุโซนจากรายการของศูนย์ครับ','The requested device does not match a recorded rental zone. Please specify a studio zone.'),
      'custom_package':('ข้อมูลราคาที่มีเป็นแพ็กเกจตามโซน ยังยืนยันราคาของชุดที่ปรับรายการเองไม่ได้ครับ','The recorded prices are zone packages. A modified bundle price is not confirmed.'),
      'eligibility':('ราคาเหมาที่บันทึกแยกสำหรับหน่วยงานภายในและภายนอก ยังยืนยันสิทธิ์ใช้ราคาเหมาในนามบุคคลไม่ได้ครับ','Recorded rental prices distinguish internal and external organizations. Eligibility for an individual is not confirmed.'),
      'scope_clarification':('กรุณาแบ่งเงื่อนไขการเหมาเป็นคำถามที่สั้นลงครับ','Please split the rental conditions into shorter questions.')}
    if contract['action']!='read':
        plan={'record_ids':[],'requested_fields':[],'method':'common_legacy_rental_bridge','operation':'rental','bridge_status':contract['action'],'profile_confirmation_closed':True}
        return reader.finish(snap,started,messages[contract['action']][lang=='en'],[],plan,[],response='clarification')
    packages={rid:r for rid,r in records.items() if r['kind']=='rental_package'}
    ids=[rid for rid,r in packages.items() if any(set(value(r,'zone_ids') or [])&set(row['zones']) and value(r,'audience_id') in row['audiences'] and value(r,'period_label') in row['periods'] for row in contract['requests'])]
    asks=set(contract['asks']);hits=[];obs=[];blocks=[];projection=[];unknown=[];not_current=[]
    fields=[]
    for ask,keys in [('rates',['amount_minor','currency','audience_id','period_label']),('capacity',['room_seats']),('equipment',['equipment_included']),('duration_definition',['duration_minutes']),('overtime',['terms'])]:
        if ask in asks:fields+=keys
    unconfirmed={'booking':('ขั้นตอนจองแบบเหมา','the rental booking procedure'),'hourly_rental':('ราคาเหมารายชั่วโมง','an hourly rental rate'),'per_unit':('ราคาเหมารายเครื่อง','a per-device rental rate'),'multi_day':('การคำนวณราคาเหมาหลายวัน','multi-day rental pricing')}
    if asks&{'per_unit','multi_day','hourly_rental'}:fields=[f for f in fields if f not in {'amount_minor','currency'}]
    def read(r,key):
        f=r['fields'].get(key,{'status':'unknown','value':None,'evidence_refs':[]});rid=r['record_id']
        obs.append({'record_id':rid,'field':key,'status':f['status'],'evidence_refs':f.get('evidence_refs',[])})
        if f['status']!='known':return None
        refs=[]
        for ref in f['evidence_refs']:
            source=snap['release']['sources'][ref['source_id']];label='S'+str(len(hits)+1);refs.append('['+label+']')
            hits.append({'id':rid+':'+key+':'+label,'record_id':rid,'field':key,'title':title(r,lang),'text':text(f['value'],lang),'source_id':ref['source_id'],'snapshot_sha256':source['sha256'],'locator':ref['locator'],'source_url':source.get('public_url') or '', 'citation_label':label})
        return f['value'],' '.join(refs)
    labels={'room_seats':('จำนวนที่นั่งในห้อง','Room seating capacity'),'equipment_included':('อุปกรณ์ที่รวม','Included equipment'),'duration_minutes':('ระยะเวลาเป็นนาที','Duration in minutes'),'terms':('หมายเหตุและเงื่อนไขที่บันทึก','Recorded notes and conditions')}
    for rid in ids:
        r=packages[rid]
        if not effective(r,at,records):not_current.append(rid);continue
        heading=title(r,lang);lines=['**'+heading+'**'];done=[]
        for key in fields:
            v=read(r,key);done.append(key)
            if v is None:
                unknown.append({'record_id':rid,'field':key})
                if key in labels:lines.append(labels[key][lang=='en']+(': ยังไม่มีข้อมูลยืนยัน' if lang=='th' else ': not confirmed'))
                continue
            data,refs=v
            if key=='amount_minor':lines.append(('ราคาแพ็กเกจ: ' if lang=='th' else 'Package price: ')+f'{data/100:,.2f}'+' '+str(value(r,'currency') or '')+' '+refs)
            elif key in labels:lines.append(labels[key][lang=='en']+': '+text(data,lang)+' '+refs)
        if 'effective_date' in asks:
            validity=r['validity']
            if validity['state']=='known':lines.append(('วันมีผล: ' if lang=='th' else 'Validity: ')+str(validity.get('effective_from'))+' / '+str(validity.get('effective_until')))
            else:lines.append('ยังไม่มีวันมีผลของราคาเหมาที่ยืนยันได้' if lang=='th' else 'The effective dates of this rental price are not confirmed.')
        if len(lines)>1:blocks.append('\n'.join(lines))
        projection.append({'record_id':rid,'fields':{key:'explicit' if key not in {'currency','audience_id','period_label'} else 'necessary_context' for key in done}})
    for ask,(th,en) in unconfirmed.items():
        if ask in asks:blocks.append('ยังไม่มีข้อมูลยืนยัน'+th+' กรุณาติดต่อศูนย์เพื่อยืนยันครับ' if lang=='th' else 'The available information does not confirm '+en+'. Please contact the studio.')
    if not_current:blocks.append('บางรายการหมดอายุหรือข้อมูลที่อ้างอิงใช้ยืนยันปัจจุบันไม่ได้ จึงไม่แสดงเป็นราคาปัจจุบัน' if lang=='th' else 'Some packages or their referenced records are not current, so their prices are not asserted as current.')
    if not ids:blocks.append('ไม่พบแพ็กเกจที่ตรงเงื่อนไขในข้อมูลกลางครับ' if lang=='th' else 'No common-data package matches these conditions.')
    if not blocks:blocks.append('ยังไม่มีข้อมูลยืนยันตามรายละเอียดที่ถามครับ' if lang=='th' else 'The requested details are not confirmed in the available information.')
    if 'capacity' in asks:blocks.append('จำนวนนี้คือที่นั่งในห้อง ไม่ใช่จำนวนคนเล่นพร้อมกันที่ยืนยันแล้ว' if lang=='th' else 'This is room seating capacity, not a confirmed simultaneous player count.')
    if asks&{'rates','effective_date'}:
        for rid in ids:
            if packages[rid]['validity']['state']=='unknown':
                unknown.append({'record_id':rid,'field':'validity'})
                obs.append({'record_id':rid,'field':'validity','status':'unknown','evidence_refs':[],'reason':'source_has_no_confirmed_effective_date'})
        if 'rates' in asks and any(x['field']=='validity' for x in unknown):blocks.append('ข้อมูลต้นฉบับยังไม่ระบุวันมีผลของราคาเหมา กรุณายืนยันกับศูนย์ก่อนใช้บริการ' if lang=='th' else 'The source does not specify effective dates for these rental prices. Confirm with the studio before using the service.')
    plan={'record_ids':ids,'requested_fields':list(dict.fromkeys(fields)),'operation':'rental','method':'common_legacy_rental_bridge','request_contract':contract,'response_projection':projection,'unknown_fields':unknown,'not_current_ids':not_current,'legacy_fact_fallback_used':False,'source_answer_confirmed':not unknown and not not_current and not bool(asks&set(unconfirmed))}
    return reader.finish(snap,started,'\n\n'.join(blocks),hits,plan,obs,response='partial_answer' if unknown or not_current or asks&set(unconfirmed) else 'answer')
