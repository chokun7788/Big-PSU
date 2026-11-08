"""Compile the active CommonStore snapshot into typed, source-linked facts.

No answer cache is retained across releases/epochs. Owner edits and withdrawals
therefore change the next request without code edits or a separate index publish.
"""
import json,hashlib

def value(r,k):
    f=r.get('fields',{}).get(k,{})
    return f.get('value') if f.get('status')=='known' else None

def bilingual(v):
    if isinstance(v,dict) and ('th' in v or 'en' in v):return {'th':str(v.get('th') or ''),'en':str(v.get('en') or '')}
    if isinstance(v,list):return {l:'; '.join(bilingual(x)[l] for x in v) for l in ['th','en']}
    if isinstance(v,dict):return {l:'; '.join(k+': '+bilingual(x)[l] for k,x in v.items()) for l in ['th','en']}
    return {'th':str(v),'en':str(v)}

def title(r):
    for k in ['title','name','display_name','event_name','subject','question']:
        if value(r,k) is not None:return bilingual(value(r,k))
    return {'th':r['record_id'],'en':r['record_id']}

def attach_rule_scope(facts,records):
    from .scope import contains,years
    games=[r for r in records.values() if r['kind']=='game'];events=[r for r in records.values() if r['kind']=='competition']
    for f in facts:
        if f['category']!='C13':continue
        body=' '.join(f['subject'].values())
        if f.get('event_id') in records:f['game_id']=value(records[f['event_id']],'game_id')
        if not f.get('game_id'):
            matches=[]
            for game in games:
                labels=[*title(game).values(),*sum(game.get('aliases',{}).values(),[])]
                hits=[len(s) for s in labels if contains(body,s)]
                if hits:matches.append((max(hits),game['record_id']))
            if matches:
                top=max(n for n,_ in matches);ids={rid for n,rid in matches if n==top}
                if len(ids)==1:f['game_id']=next(iter(ids))
        if f.get('game_id') and not f.get('event_id'):
            candidates=[r for r in events if value(r,'game_id')==f['game_id']]
            dated=[r for r in candidates if years(' '.join(title(r).values()))==years(body)]
            if len(dated)==1:candidates=dated
            if len(candidates)==1:f['event_id']=candidates[0]['record_id']

FIELDS={
 'center':('C01',[('address','ที่อยู่','address'),('building','อาคาร','building'),('floor','ชั้น','floor'),('map_url','แผนที่','map link'),('description','ข้อมูลศูนย์','studio overview'),('operator','ผู้ดำเนินการ','operator')]),
 'contact':('C01',[('value','ช่องทางติดต่อ','contact information'),('office_hours','เวลาติดต่อ','contact hours')]),
 'facility':('C01',[('location','ที่ตั้ง','location'),('usage_conditions','วิธีใช้','usage conditions')]),
 'person':('C02',[('display_name','ชื่อ','name'),('role','หน้าที่และตำแหน่ง','role'),('team','ทีม','team'),('affiliation','สังกัด','affiliation'),('period','ช่วงเวลาตามโปรไฟล์','recorded profile period')]),
 'equipment_model':('C03',[('name','ชื่ออุปกรณ์','equipment name'),('device_type','ชนิดอุปกรณ์','device type'),('specifications','สเปก','specifications'),('usage','การใช้งาน','usage')]),
 'resource':('C03',[('capacity_persons','จำนวนคนเล่นพร้อมกัน','simultaneous player capacity')]),
 'zone':('C03',[('room_seats','จำนวนที่นั่งห้อง','room seats')]),
 'game':('C04',[('summary','คำอธิบายเกม','game overview'),('official_description','คำบรรยายฉบับเต็มจากแหล่งข้อมูลที่บันทึกไว้','full recorded source description'),('how_to_play','วิธีเล่น','how to play'),('genre','แนวเกม','genre'),('supported_platforms','แพลตฟอร์มที่เกมรองรับ','supported platforms')]),
 'closure':('C11',[('local_date','วันที่ปิดพิเศษ','exception date'),('reason','เหตุผล','reason')]),
 'news':('C14',[('body','รายละเอียดกิจกรรม','event details'),('event_start','วันที่จัด','event date'),('registration_url','ช่องทางสมัคร','registration link')]),
}

def compile_snapshot(snapshot):
    release=snapshot.get('release') or {};withdrawn=set(snapshot.get('withdrawn',[]))
    records={k:r for k,r in release.get('records',{}).items() if k not in withdrawn};facts=[];seen=set();deferred=[];affirmations=[]
    def add(cat,r,facet,label,v,refs,subject=None,**extra):
        fid=f"{cat}:{r['record_id']}:{facet}"
        if fid in seen or v is None or not refs:return
        v=bilingual(v);missing=not v['en']
        if not v['en']:v['en']=v['th']
        if not v['th']:v['th']=v['en']
        if not any(v.values()):return
        sub=subject or title(r);seen.add(fid)
        facts.append({'id':fid,'category':cat,'record_id':r['record_id'],'facet':facet,'subject':sub,
          'label':dict(zip(['th','en'],label)),'value':v,'evidence_refs':refs,'fixture':snapshot.get('allow_demo',False),
          'aliases':sum(r.get('aliases',{}).values(),[]),'entity_aliases':sum(r.get('aliases',{}).values(),[]),
          'validity':r.get('validity'),'english_translation_missing':missing,'source_record_kind':r['kind'],**extra})
    def field(cat,r,k,label,**extra):
        f=r['fields'].get(k,{})
        if f.get('status')=='known':add(cat,r,k,label,f.get('value'),f.get('evidence_refs',[]),**extra)
    for r in records.values():
        kind=r['kind']
        if kind in FIELDS:
            cat,fields=FIELDS[kind]
            for k,th,en in fields:field(cat,r,k,(th,en))
        if kind=='game':
            for f in facts:
                if f['record_id']==r['record_id'] and f['facet']=='official_description':
                    f['description_scope_note']=bilingual(value(r,'description_scope_note') or '')
                    f['description_captured_at']=value(r,'description_captured_at')
                    for k in ['description_scope_note','description_captured_at']:f['evidence_refs']+=r['fields'].get(k,{}).get('evidence_refs',[])
        if kind=='equipment_model':
            for x in value(r,'specifications') or []:
                if isinstance(x,dict) and x.get('key') in {'zone','quantity'}:
                    k='location' if x['key']=='zone' else 'quantity'
                    add('C03',r,k,('ที่ตั้ง','location') if k=='location' else ('จำนวนเครื่อง','quantity'),x['value'],r['fields']['specifications']['evidence_refs'])
        if kind=='resource' and value(r,'zone_id') in records:
            add('C03',r,'location',('ที่ตั้ง','location'),title(records[value(r,'zone_id')]),r['fields']['zone_id']['evidence_refs'])
        if kind=='service' and value(r,'capacity_min') is not None and value(r,'capacity_max') is not None:
            lo,hi=value(r,'capacity_min'),value(r,'capacity_max')
            refs=r['fields']['capacity_min']['evidence_refs']+r['fields']['capacity_max']['evidence_refs']
            add('C03',r,'service_capacity',('ช่วงจำนวนผู้ใช้ตามรายการบริการ','participant range stated for the service'),
                {'th':f'{lo}–{hi} คนตามรายการบริการ ไม่ใช่การยืนยันจำนวนที่เล่นพร้อมกัน',
                 'en':f'{lo}–{hi} participants under the service listing; simultaneous play capacity is not established by this range'},
                refs,capacity_min=lo,capacity_max=hi,capacity_semantics='listed_service_participant_range_not_simultaneous_capacity')
        if kind=='control_set':
            game=records.get(value(r,'game_id'));sub=title(game) if game else title(r);platform=value(r,'platform') or ''
            sub={l:s+' / '+platform for l,s in sub.items()}
            for i,b in enumerate(value(r,'bindings') or []):
                action=bilingual(b.get('action') or '');buttons=bilingual(b.get('button_label') or b.get('buttons') or '')
                notes=bilingual(b.get('notes') or '')
                output={l:buttons[l]+(' — '+notes[l] if notes[l] not in {'','None'} else '') for l in ['th','en']}
                add('C05',r,'binding_'+str(i),(action['th'],action['en']),output,r['fields']['bindings']['evidence_refs'],subject=sub,platform=platform,button_label=buttons)
        if kind=='game_mode' and value(r,'game_id') in records:
            game=records[value(r,'game_id')]
            for k,th,en in [('players_min','จำนวนผู้เล่นขั้นต่ำ','minimum players'),('players_max','จำนวนผู้เล่นสูงสุด','maximum players')]:
                v=value(r,k)
                if v is not None:add('C04',r,k,(th,en),v,r['fields'][k]['evidence_refs'],subject=title(game),numeric=v,game_id=game['record_id'],platform=value(r,'platform'),mode_name=value(r,'mode_name'))
        if kind=='rate':
            service=records.get(value(r,'service_id'));group=records.get(value(r,'audience_id'));minor=value(r,'amount_minor')
            if service and group and minor is not None:
                sub={l:title(service)[l]+' / '+title(group)[l] for l in ['th','en']};amount=minor/100
                unit=value(r,'unit');per_person=unit=='per_person';per_group=unit=='per_group'
                suffix=('ต่อคนตามช่วงที่ระบุ','per person for the stated period') if per_person else ('ต่อกลุ่มตามช่วงที่ระบุ','per group for the stated period') if per_group else ('ตามหน่วยและช่วงที่ระบุ','for the stated billing unit and period')
                refs=list(r['fields']['amount_minor']['evidence_refs'])
                for k in ['service_id','audience_id','duration_minutes','unit']:
                    refs+=r['fields'].get(k,{}).get('evidence_refs',[])
                add('C06',r,'amount',('ค่าบริการตามหน่วยที่ระบุ','price for the stated unit'),{'th':f'{amount:g} บาท{suffix[0]}','en':f'{amount:g} THB {suffix[1]}'},refs,
                  subject=sub,numeric=amount,service_id=service['record_id'],audience_id=group['record_id'],billing_unit=unit,calculation_rule=value(r,'calculation_rule'),
                  persons_min=value(r,'persons_min'),persons_max=value(r,'persons_max'))
                # Use the service display name instead of leaking rate IDs.
                field('C06',r,'duration_minutes',('นาทีต่อรอบ','minutes per session'),subject=sub)
        if kind=='schedule':
            day=value(r,'weekday')
            if day is None:continue
            days={'th':['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์'],'en':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']}
            for k,th,en in [('open_periods','เวลาเปิด','opening hours'),('bookable_periods','ช่วงจองเล่น','bookable periods'),('maintenance_periods','ช่วงบำรุงรักษา','maintenance periods')]:
                v=value(r,k)
                if v is not None:add('C11',r,k,(th,en),'; '.join(x['start']+'–'+x['end'] for x in v) or 'ไม่มี / None',r['fields'][k]['evidence_refs'],subject={l:days[l][day] for l in days},weekday=day)
            slots=value(r,'service_slots')
            if slots is not None:
                labels={'open':('เปิดให้เล่น','open for play'),'maintenance':('บำรุงรักษา','maintenance'),'closed':('ปิดบริการเล่น','closed for play')}
                shown={l:'; '.join(s['start']+'–'+s['end']+' '+labels.get(s['state'],(s['state'],s['state']))[l=='en'] for s in slots) or ('ปิดบริการเล่นตามตารางประจำ' if l=='th' else 'Closed for play under the regular timetable') for l in ['th','en']}
                add('C11',r,'service_periods',('ตารางให้บริการเล่น','regular play-service timetable'),shown,r['fields']['service_slots']['evidence_refs'],subject={l:days[l][day] for l in days},weekday=day,service_slots=slots,service_closed=value(r,'service_closed'))
        if kind=='rental_package':
            for k,th,en in [('amount_minor','ราคาแพ็กเกจ','package price'),('duration_minutes','ระยะเวลาเป็นนาที','duration in minutes'),('equipment_included','อุปกรณ์ที่รวม','included equipment'),('room_seats','ที่นั่งห้อง','room seats'),('terms','เงื่อนไขแพ็กเกจ','package terms')]:
                v=value(r,k)
                if v is None:continue
                facet='amount_thb' if k=='amount_minor' else k;num=v/100 if k=='amount_minor' else v if isinstance(v,(int,float)) else None
                out={'th':f'{num:g} บาทต่อแพ็กเกจ','en':f'{num:g} THB per package'} if k=='amount_minor' else v
                add('C07',r,facet,(th,en),out,r['fields'][k]['evidence_refs'],numeric=num)
        if kind=='competition_rule':
            event=records.get(value(r,'competition_id'))
            if event and value(r,'text') is not None:
                label=bilingual(value(r,'heading') or value(r,'facet') or 'กติกา')
                add('C13',r,'rule_clause',(label['th'],label['en']),value(r,'text'),r['fields']['text']['evidence_refs'],subject=title(event),depends_on_ids=value(r,'depends_on_ids') or [],event_id=event['record_id'],section_number=value(r,'section_number'))
        if kind=='policy' and value(r,'decision') is not None:
            decision=value(r,'decision');conditions=value(r,'conditions_all');exceptions=value(r,'exceptions')
            complete=conditions is not None and r['fields'].get('exceptions',{}).get('status') in {'known','not_applicable'}
            captions={'allowed':('อนุญาต','Allowed'),'prohibited':('ไม่อนุญาต','Prohibited'),'required':('จำเป็นต้องทำ','Required'),'conditional':('มีเงื่อนไข','Conditional')}
            content={l:captions.get(decision,(decision,decision))[l=='en'] for l in ['th','en']};refs=list(r['fields']['decision']['evidence_refs'])
            for k in ['conditions_all','exceptions','details','consequence']:
                v=value(r,k)
                if v is None:continue
                label={'conditions_all':('เงื่อนไข','Conditions'),'exceptions':('ข้อยกเว้น','Exceptions'),'details':('รายละเอียด','Details'),'consequence':('ผลที่ตามมา','Consequence')}[k]
                if k=='conditions_all':
                    shown={l:'; '.join(str(x['field'])+' '+str(x['operator'])+' '+str(x['value']) for x in v) or ('ไม่มีเงื่อนไขเพิ่มเติม' if l=='th' else 'No additional conditions') for l in ['th','en']}
                else:shown=bilingual(v)
                for l in content:content[l]+='; '+label[l=='en']+': '+shown[l]
                refs+=r['fields'][k]['evidence_refs']
            add('C10',r,'owner_policy',('ข้อกำหนดและเงื่อนไข','policy and conditions'),content,refs,policy_complete=complete,
              declared_predicates=[str(c.get('field','')) for c in conditions or []],policy_intent=str(value(r,'topic') or ''))
        if kind=='procedure' and value(r,'steps') is not None:
            content={l:'; '.join(str(s['order'])+'. '+bilingual(s['instruction'])[l] for s in sorted(value(r,'steps'),key=lambda x:x['order'])) for l in ['th','en']}
            refs=list(r['fields']['steps']['evidence_refs'])
            for k in ['preconditions','required_documents','deadline_minutes','outcome']:
                v=value(r,k)
                if v is not None:
                    shown=bilingual(v)
                    for l in content:content[l]+='; '+k+': '+shown[l]
                    refs+=r['fields'][k]['evidence_refs']
            add('C08',r,'owner_policy',('ขั้นตอนปฏิบัติ','procedure steps'),content,refs,procedure_complete=True,policy_intent=str(value(r,'topic') or ''))
        if kind=='faq':
            meta=value(r,'scope_note') or {}
            if isinstance(meta,dict) and ('th' in meta or 'en' in meta):meta=meta.get('en') or meta.get('th') or '{}'
            meta=meta if isinstance(meta,dict) else None
            if meta is None:
                raw=value(r,'scope_note') or '{}'
                if isinstance(raw,dict):raw=raw.get('en') or raw.get('th') or '{}'
                try:meta=json.loads(raw)
                except (ValueError,TypeError):meta={}
            descriptor=meta.get('r114_fact') if isinstance(meta,dict) else None
            if isinstance(meta,dict) and meta.get('r114_confirmation'):
                affirmations.append((r,meta['r114_confirmation']));continue
            if descriptor:
                cat=descriptor['category'];facet=descriptor['facet'];a=value(r,'answer')
                extra={k:v for k,v in descriptor.items() if k not in {'category','facet','subject','label'}}
                if 'numeric' in extra:
                    import re
                    m=re.search(r'-?\d+(?:\.\d+)?',bilingual(a)['th']);extra['numeric']=float(m[0]) if m else None
                add(cat,r,facet,tuple(descriptor['label'][l] for l in ['th','en']),a,r['fields']['answer']['evidence_refs'],subject=descriptor['subject'],**extra)
            elif value(r,'answer') is not None:
                # Newly added FAQs can be routed by topic/profile or retrieved
                # within a supplied domain, without per-record code changes.
                intent=str(value(r,'intent_key') or '')
                topics={'booking':'C08','payment':'C09','policy':'C10','calendar':'C11','game':'C04','equipment':'C03','center':'C01','news':'C14','rental':'C07','price':'C06','people':'C02','controls':'C05','competition':'C13'}
                cat=next((c for t,c in topics.items() if intent.startswith(t)),None)
                if cat:add(cat,r,'owner_policy',('คำตอบที่ยืนยัน','confirmed answer'),value(r,'answer'),r['fields']['answer']['evidence_refs'],faq_question=value(r,'question'),policy_intent=intent)
                else:deferred.append(r)
    # A catalog is the complete offered relation set, not retrieval top-K.
    for s in [r for r in records.values() if r['kind']=='service']:
        offers=[r for r in records.values() if r['kind']=='game_service' and value(r,'service_id')==s['record_id'] and value(r,'offered') is True and value(r,'game_id') in records]
        if offers:
            output={l:'; '.join(dict.fromkeys(title(records[value(r,'game_id')])[l] for r in offers)) for l in ['th','en']}
            refs=[x for r in offers for x in r['fields']['game_id']['evidence_refs']]
            add('C04',s,'game_catalog',('รายชื่อเกมทั้งหมด','all offered games'),output,refs,complete_set=True,
                member_ids=sorted({value(r,'game_id') for r in offers}),membership_scope='recorded_offered_relations')
    for game in [r for r in records.values() if r['kind']=='game']:
        offers=[r for r in records.values() if r['kind']=='game_service' and value(r,'game_id')==game['record_id'] and value(r,'offered') is True and value(r,'service_id') in records]
        if offers:add('C04',game,'studio_services',('บริการที่มีเกมนี้','studio services offering this game'),{l:'; '.join(dict.fromkeys(title(records[value(r,'service_id')])[l] for r in offers)) for l in ['th','en']},[x for r in offers for x in r['fields']['offered']['evidence_refs']])
        zone_ids=list(value(game,'studio_zone_ids') or []);refs=list(game['fields'].get('studio_zone_ids',{}).get('evidence_refs',[]));paths=[]
        explicit_venue=value(game,'venue_zone_ids') or []
        if explicit_venue:
            zone_ids+=explicit_venue;refs+=game['fields']['venue_zone_ids']['evidence_refs']
        for zid in zone_ids:
            refs+=records[zid]['fields']['name']['evidence_refs'];paths.append([game['record_id'],zid])
        for offer in offers:
            service=records[value(offer,'service_id')]
            direct=value(service,'studio_zone_ids') or []
            if direct:
                zone_ids+=direct
                for r,k in [(offer,'game_id'),(offer,'service_id'),(offer,'offered'),(service,'studio_zone_ids')]:refs+=r['fields'][k]['evidence_refs']
                for zid in direct:refs+=records[zid]['fields']['name']['evidence_refs'];paths.append([game['record_id'],offer['record_id'],service['record_id'],zid])
            for resource_id in value(service,'resource_ids') or []:
                resource=records.get(resource_id,{})
                zone_id=value(resource,'zone_id');zone=records.get(zone_id,{})
                if zone.get('kind')!='zone':continue
                chain=[(offer,'game_id'),(offer,'service_id'),(offer,'offered'),(service,'resource_ids'),(resource,'zone_id')]
                if not all(r.get('fields',{}).get(k,{}).get('evidence_refs') for r,k in chain):continue
                zone_ids.append(zone_id);refs.extend(p for r,k in chain for p in r['fields'][k]['evidence_refs'])
                paths.append([game['record_id'],offer['record_id'],service['record_id'],resource_id,zone_id])
        if zone_ids:
            unique=sorted(set(zone_ids))
            add('C04',game,'zone',('โซนที่ยืนยันว่ามีเกมนี้','confirmed studio zones offering this game'),
                {l:'; '.join(title(records[z])[l] for z in unique) for l in ['th','en']},
                list({json.dumps(p,sort_keys=True):p for p in refs}.values()),zone_ids=unique,relation_paths=paths,complete_set=False)
    if deferred:
        from .index import FactIndex
        from .routing import route
        index=FactIndex({'records':records,'facts':facts})
        for r in deferred:
            q=' '.join(bilingual(value(r,'question')).values());cat=route(index,q)
            if cat:add(cat,r,'owner_policy',('คำตอบที่ยืนยัน','confirmed answer'),value(r,'answer'),r['fields']['answer']['evidence_refs'],faq_question=value(r,'question'),policy_intent=str(value(r,'intent_key') or ''))
    for record,confirmation in affirmations:
        fields=confirmation.get('fields_for_hash',[])
        for f in facts:
            rid=f['record_id'];r=records.get(rid)
            if not r or rid not in confirmation.get('record_value_hashes',{}):continue
            raw=json.dumps({k:value(r,k) for k in fields},ensure_ascii=False,sort_keys=True,separators=(',',':'))
            if hashlib.sha256(raw.encode()).hexdigest()!=confirmation['record_value_hashes'][rid]:continue
            f['confirmation_ref']=record['record_id'];f['confirmation_as_of']=confirmation['as_of']
            f['confirmation_evidence_refs']=record['fields']['answer']['evidence_refs']+record['fields']['scope_note']['evidence_refs']
            if confirmation.get('per_person_scope'):
                f['confirmed_per_person']=True
                if f['category']=='C06' and f['facet']=='amount':
                    duration=value(r,'duration_minutes');period=(str(duration)+' นาที') if duration is not None else 'ระยะเวลาที่ระบุ'
                    f['label']={'th':'ค่าบริการต่อคนตามระยะเวลาของอัตรา','en':'per-person price for the rate duration'}
                    f['value']={'th':f"{f['numeric']:g} บาทต่อคน สำหรับ {period}",'en':f"{f['numeric']:g} THB per person for "+(str(duration)+' minutes' if duration is not None else 'the stated period')}
    for f in facts:
        search=value(records[f['record_id']],'legacy_search')
        if search:f['legacy_search']=search
    return {'records':records,'facts':facts,'release_id':snapshot.get('active'),'epoch':snapshot.get('epoch')}
