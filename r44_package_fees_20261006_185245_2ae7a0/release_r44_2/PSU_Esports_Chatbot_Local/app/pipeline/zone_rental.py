"""User-supplied zone/organization rental fees, separate from play-session fees."""
from __future__ import annotations
import copy,json,re
from pathlib import Path
from app.core.normalization import normalize_text
from app.core.source_registry import ZONE_RENTAL_FEES_20261006_ID, make_source_hit
from app.pipeline.schemas import EntityBundle,PipelineRoute,PipelineTrace,ValidationResult

DATA_PATH=Path(__file__).resolve().parents[2]/'data/curated/zone_rental_fees_20261006.json'
TARGETS=('all_zones','cockpit','vr','nintendo_switch','ps5','pc')
GROUPS=('external','internal');PERIODS=('half_day','full_day')
RENTAL=re.compile(r'เหมา(?!ะ)|เช่า|\b(?:rent(?:al)?|hire|venue)\b',re.I)
HALF=re.compile(r'ครึ่งวัน|\bhalf[ -]?day\b',re.I)
FULL=re.compile(r'เต็มวัน|ทั้งวัน|เหมาวัน|\b(?:full[ -]?day|whole day|daily|per day)\b',re.I)
PRICE=re.compile(r'ราคา|ค่าบริการ|กี่บาท|เท่าไหร่|เท่าไร|\b(?:price|prices|fees?|rates?|cost|how much)\b',re.I)
HOURLY=re.compile(r'รายชั่วโมง|ต่อชั่วโมง|\bhourly\b|\bper hour\b',re.I)
RETURN=re.compile(r'^(?:กลับ(?:ไป|มา)(?:เรื่อง|ที่)?|(?:go )?back to|return to)',re.I)
ASKS={'rates','capacity','equipment','duration_definition','effective_date','booking','live_availability','overtime','per_unit','eligibility','hourly_rental','multi_day'}

def load_zone_rental_data():
    data=json.loads(DATA_PATH.read_text(encoding='utf-8'))
    if data.get('schema_version')!=1 or data.get('price_scope')!='zone_rental_for_organizations' or data.get('source_id')!=ZONE_RENTAL_FEES_20261006_ID:
        raise ValueError('invalid zone rental source schema')
    rows=data.get('rows',[])
    if [r.get('id') for r in rows]!=list(TARGETS):raise ValueError('rental source target coverage')
    for row in rows:
        for group in GROUPS:
            for period in PERIODS:
                price=row['prices_thb'][group][period]
                if type(price)!=int or price<0:raise ValueError('rental price must be a nonnegative integer')
    return data

def valid_zone_rental_plan(p):
    return (isinstance(p,dict) and p.get('schema_type')=='zone_rental_v1' and p.get('schema_version')==1
        and all(isinstance(p.get(k),list) and len(p[k])<=limit and all(isinstance(v,str) and v in allowed for v in p[k])
            for k,allowed,limit in [('targets',TARGETS,6),('groups',GROUPS,2),('periods',PERIODS,2),('asks',ASKS,12)])
        and bool(p['groups']) and bool(p['periods']) and bool(p['asks'])
        and isinstance(p.get('unresolved_targets'),list) and len(p['unresolved_targets'])<=6
        and all(isinstance(v,str) and 0<len(v)<=100 for v in p['unresolved_targets'])
        and all(len(p[k])==len(set(p[k])) for k in ('targets','groups','periods','asks'))
        and bool(p['targets'] or p['unresolved_targets'])
        and isinstance(p.get('resolved_query'),str) and 0<len(p['resolved_query'])<=2000)

def _targets(q):
    from app.session.conversation_plan import service_mentions, excluded_services
    selected=service_mentions(q,fuzzy=True)
    bundle=bool(re.search(r'ทุกโซน|ทั้งศูนย์|ทั้งห้อง|\ball zones\b|\b(?:entire|whole)\s+(?:studio|venue|room)\b',q,re.I))
    catalog=bool(re.search(r'แต่ละโซน|แยก.{0,8}โซน|ทุกแพ็กเกจ|ราคาทั้งหมด|ทุกแบบ|\b(?:all (?:rental )?(?:prices|rates|packages)|each zone)\b',q,re.I))
    selected=list(TARGETS) if catalog else (['all_zones'] if bundle else [])+selected
    excluded=excluded_services(q)
    return list(dict.fromkeys(t for t in selected if t not in excluded))

def _groups(q):
    internal=bool(re.search(r'หน่วยงานภายใน|หน่วยงานในมหาวิทยาลัย|\binternal\b|\bpsu (?:department|unit|organization)\b',q,re.I))
    external=bool(re.search(r'หน่วยงานภายนอก|หน่วยงานนอก|\bexternal\b',q,re.I))
    if re.fullmatch(r'(?:ภายใน|ในมหาวิทยาลัย)[.!?\s]*',q):internal=True
    if re.fullmatch(r'(?:ภายนอก|นอกมหาวิทยาลัย)[.!?\s]*',q):external=True
    return [g for g,found in [('external',external),('internal',internal)] if found]

def _asks(q):
    asks=[]
    if PRICE.search(q):asks.append('rates')
    for key,pattern in [
        ('capacity',r'ที่นั่ง|รองรับ|กี่คน|\b(?:seats|seating|capacity|how many people)\b'),
        ('equipment',r'อุปกรณ์|กี่เครื่อง|รวมอะไร|มีอะไรให้|\b(?:equipment|included devices|how many machines|what is included)\b'),
        ('duration_definition',r'กี่ชั่วโมง|กี่โมง|ช่วงเวลา|นับเวลา|\b(?:how many hours|what hours|what times|how long)\b'),
        ('effective_date',r'เริ่มใช้|มีผล|หมดอายุ|\b(?:validity|effective date|valid from|expiry)\b'),
        ('booking',r'จอง|\b(?:book|booking|reserve|reservation)\b'),
        ('live_availability',r'ว่าง|ถูกจอง|\b(?:available|availability|booked)\b'),
        ('overtime',r'เจ้าหน้าที่|นอกเวลา|\b(?:staff|overtime|extra charge)\b'),
        ('per_unit',r'เครื่องเดียว|ต่อเครื่อง|pc\s*#?\s*\d+(?!\d|\s*(?:วัน|days))|\b(?:one machine|single pc|per machine|per device)\b'),
        ('eligibility',r'นักศึกษา|บุคคลทั่วไป|\b(?:student|individual|private person|general adult)\b'),
        ('multi_day',r'(?:[2-9]|\d{2,})\s*วัน|\b(?:[2-9]|\d{2,})\s*days\b'),
    ]:
        if re.search(pattern,q,re.I):asks.append(key)
    if HOURLY.search(q):asks.append('hourly_rental')
    if 'hourly_rental' in asks or ('overtime' in asks and not re.search(r'ราคา|ค่าบริการ|\brental (?:prices?|fees?|rates?)\b',q,re.I)):
        asks=[a for a in asks if a!='rates']
    if 'effective_date' in asks and not re.search(r'กี่บาท|เท่าไหร่|เท่าไร|\b(?:how much|prices|rates|fees)\b',q,re.I):
        asks=[a for a in asks if a!='rates']
    return list(dict.fromkeys(asks)) or ['rates']

def _unknown_targets(q):
    # Read the requested noun phrase; a supplied unknown noun cannot mean all zones.
    from app.core.normalization import SERVICE_ALIASES
    from app.session.conversation_plan import service_mentions
    found=[]
    spans=[m[1] for m in re.finditer(r'(?:เหมา(?!ะ)|เช่า|\b(?:rent|hire)\b)\s*(.*?)(?=ครึ่งวัน|เต็มวัน|ทั้งวัน|รายชั่วโมง|รองรับ|กี่คน|มีอุปกรณ์|มีค่า|เจ้าหน้าที่|นอกเวลา|ว่าง|กี่ชั่วโมง|เริ่มใช้|มีผล|หมดอายุ|ยังไง|อย่างไร|\b(?:half[ -]?day|full[ -]?day|whole day)\b|$)',q,re.I)]
    if q.isascii():
        spans.extend(m[1] for m in re.finditer(r'([^?;\n]*?)\brental\b',q,re.I))
    for span in spans:
        span=re.sub(r'\d+\s*(?:วัน|days|ชั่วโมง|hours)\b',' ',span,flags=re.I)
        span=re.sub(r'\bpc\s*#?\s*\d+\b','pc',span,flags=re.I)
        for alias in sorted({a for aa in SERVICE_ALIASES.values() for a in aa},key=len,reverse=True):
            normalized=normalize_text(alias)
            pattern=r'(?<![a-z0-9])'+re.escape(normalized)+r'(?![a-z])' if normalized.isascii() else re.escape(normalized)
            span=re.sub(pattern,' ',span,flags=re.I)
        span=re.sub(r'ทุกแพ็กเกจ|ทั้งศูนย์|ทั้งห้อง|ทุกแบบ|แต่ละโซน|ยกเว้น|ไม่เอา|อุปกรณ์|ห้อง|โซน|เครื่อง|ทั้งหมด|ทุกโซน|หน่วยงานภายใน|หน่วยงานภายนอก|ราคา|กี่บาท|เท่าไหร่|เท่าไร|\b(?:what|is|are|how|much|show|when|do|i|book|hourly|full|half|whole|day|entire|seating|capacity|included|for|a|an|the|zone|studio|all|zones|and|of|equipment|prices?|rates?|fees?|external|internal|organizations?|please|except)\b|และ|กับ|ครับ|ค่ะ|หน่อย|[^\w\u0e00-\u0e7f]+',' ',span,flags=re.I).strip()
        span=' '.join(token for token in span.split() if not service_mentions(token,fuzzy=True))
        if span and len(span)<=100:found.append(span)
    return list(dict.fromkeys(found))[:6]

def resolve_zone_rental_plan(question,history=None,*,locale='th'):
    q=normalize_text(question).strip();previous=None
    explicit=bool(RENTAL.search(q) or ((HALF.search(q) or FULL.search(q)) and PRICE.search(q)))
    if HOURLY.search(q) and not RENTAL.search(q):return None
    if isinstance(history,list):
        candidates=history if RETURN.search(q) and RENTAL.search(q) else history[-1:]
        for row in reversed(candidates):
            if row.get('role')=='assistant' and row.get('delivery_status')=='client_acknowledged' and valid_zone_rental_plan(row.get('request_plan')):
                previous=copy.deepcopy(row['request_plan']);break
    targets=_targets(q);groups=_groups(q);periods=[p for p,found in [('half_day',HALF.search(q)),('full_day',FULL.search(q))] if found]
    bare=re.fullmatch(r'(?:ทั้งหมด(?:เลย)?|ทุกแบบ|all(?: of them)?|both|both periods|ภายใน|ภายนอก|internal|external)[.!?\s]*',q,re.I)
    short_selection=bool(targets or groups or periods or re.search(r'ทั้งสองกลุ่ม|\bboth groups\b',q,re.I)) and len(q)<=90 and not re.search(r'เกม|ปุ่ม|ว่าง|กฎ|แข่งขัน|\b(?:games?|controls?|rules?|availability|available)\b',q,re.I)
    information_followup=bool(previous and re.search(r'กี่ชั่วโมง|กี่โมง|ที่นั่ง|อุปกรณ์|รวมอะไร|มีอะไรให้|เจ้าหน้าที่|นอกเวลา|เริ่มใช้|\b(?:how many hours|seats|equipment|what is included|overtime|effective date)\b',q,re.I))
    if not explicit and not (previous and (bare or short_selection or information_followup)):return None
    # A complete unrelated question containing a service name is a topic shift.
    if not explicit and previous and PRICE.search(q) and not groups and not periods:return None
    inherited=bool(previous and (not explicit or RETURN.search(q)))
    p=copy.deepcopy(previous) if inherited else dict(schema_type='zone_rental_v1',schema_version=1,targets=list(TARGETS),groups=list(GROUPS),periods=list(PERIODS),asks=['rates'],unresolved_targets=[])
    if targets:p['targets']=targets
    elif bare and re.search(r'ทั้งหมด|ทุกแบบ|\ball\b',q,re.I):p['targets']=list(TARGETS)
    if groups:p['groups']=groups
    if re.search(r'ทั้งสองกลุ่ม|ทั้งภายในและภายนอก|\bboth (?:groups|organization types)\b',q,re.I):p['groups']=list(GROUPS)
    if periods:p['periods']=periods
    if bare and re.search(r'\bboth(?: periods)?\b',q,re.I):p['periods']=list(PERIODS)
    if explicit or information_followup:p['asks']=_asks(q)
    unknown=_unknown_targets(q) if explicit else []
    # A fuzzy matched known service should not become a leftover unknown noun.
    if unknown and not targets:p['targets']=[]
    p['unresolved_targets']=unknown
    p.update(original_query=question,context_used=inherited,act='fill_rental_scope' if inherited else 'new_rental_request')
    p['resolved_query']='Zone rental request: '+', '.join(p['targets'])+'; organizations '+', '.join(p['groups'])+'; periods '+', '.join(p['periods'])+'; facts '+', '.join(p['asks'])
    return p

def build_zone_rental_answer(plan,locale='th'):
    if not valid_zone_rental_plan(plan):return None
    data=load_zone_rental_data();en=locale=='en';rows=[r for r in data['rows'] if r['id'] in plan['targets']]
    lines=['Zone rental fees for organizations' if en else 'ราคาเช่าเหมาโซนสำหรับหน่วยงาน'];returned=[];missing=[]
    prices='rates' in plan['asks'];groups={'external':'External organizations' if en else 'หน่วยงานภายนอก','internal':'Internal organizations' if en else 'หน่วยงานภายใน'}
    periods={'half_day':'half day' if en else 'ครึ่งวัน','full_day':'full day' if en else 'เต็มวัน'}
    if prices or {'capacity','equipment'} & set(plan['asks']):
        for row in rows:
            lines+=['',f"**{row['label']}**"]
            if prices:
                for group in plan['groups']:
                    parts=[]
                    for period in plan['periods']:
                        value=row['prices_thb'][group][period];parts.append(f"{periods[period]} {value:,} {'THB' if en else 'บาท'}")
                        returned.append(dict(id=f"{row['id']}:{group}:{period}",value=value,cell=row['source_cells'][f'{group}_{period}']))
                    lines.append(f"• {groups[group]}: "+' / '.join(parts))
            lines.append(f"• {'Seating capacity' if en else 'รองรับ'}: {row['seats']} {'seats' if en else 'ที่นั่ง'}; {'equipment' if en else 'อุปกรณ์'}: {row['equipment_en' if en else 'equipment_th']}")
    messages={
      'duration_definition':('The workbook does not define the number of hours or clock windows for half-day/full-day rental. Please confirm the rental hours with the studio.','ไฟล์ไม่ได้ระบุว่าครึ่งวัน/เต็มวันนับกี่ชั่วโมงหรือเริ่ม–สิ้นสุดกี่โมง ต้องยืนยันช่วงเวลาเช่าเหมาจากศูนย์ครับ'),
      'effective_date':('The workbook does not state an effective or expiry date for these rental rates.','ไฟล์ไม่ได้ระบุวันเริ่มใช้หรือวันสิ้นสุดของอัตราเช่าเหมานี้ครับ'),
      'booking':('The workbook lists rental fees but does not specify the rental booking procedure. Please confirm it with the studio.','ไฟล์ระบุราคาเช่าเหมา แต่ไม่ได้ระบุขั้นตอนหรือช่องทางจองเหมา ต้องสอบถามศูนย์เพื่อยืนยันครับ'),
      'live_availability':('These rental rates do not establish whether the zone is currently available for private rental.','ราคาในไฟล์ยังใช้ยืนยันไม่ได้ว่าโซนว่างสำหรับการเช่าเหมาในวันเวลาที่ถามครับ'),
      'overtime':('The note in the All Zones row says staff overtime compensation is reimbursed under university regulations. It does not state the amount, who pays, or whether it is included in rent.','หมายเหตุในแถว All Zones ระบุว่าค่าตอบแทนเจ้าหน้าที่ทำงานนอกเวลาเบิกตามระเบียบมหาวิทยาลัย แต่ไม่ได้ระบุจำนวนเงิน ผู้จ่าย หรือว่ารวมในค่าเช่าแล้วหรือไม่ครับ'),
      'per_unit':('These are zone rental rates with the listed equipment. The workbook does not provide a rental price per individual machine.','อัตรานี้เป็นราคาเช่าเหมาโซนพร้อมอุปกรณ์ที่ระบุ ไฟล์ไม่ได้ให้ราคาเหมาต่อเครื่อง จึงหารหรือใช้แทนราคาต่อเครื่องไม่ได้ครับ'),
      'eligibility':('Rates are grouped by internal/external organizations. The workbook does not assign an individual or student to either organization rate.','ตารางนี้แบ่งราคาตามหน่วยงานภายใน/ภายนอก ไม่ได้ระบุสิทธิ์ราคาของบุคคลหรือนักศึกษา จึงยังจัดเข้ากลุ่มหน่วยงานให้เองไม่ได้ครับ'),
      'hourly_rental':('This workbook provides half-day/full-day zone rental fees, not an hourly zone rental rate.','ไฟล์นี้ให้ราคาเหมาโซนแบบครึ่งวัน/เต็มวัน ไม่ได้ให้ราคาเหมาโซนรายชั่วโมงครับ'),
      'multi_day':('The workbook lists a full-day rate but does not specify a multi-day package or discount.','ไฟล์ให้อัตราต่อวัน แต่ไม่ได้ระบุแพ็กเกจเหมาหลายวันหรือส่วนลดครับ'),
    }
    for ask in plan['asks']:
        if ask in messages:lines+=['',messages[ask][0 if en else 1]];missing.append(ask)
    if plan['unresolved_targets']:
        lines+=['',('No rental rate is recorded for these requested targets: ' if en else 'ยังไม่มีราคาเช่าเหมาในไฟล์สำหรับรายการที่ระบุ: ')+', '.join(plan['unresolved_targets'])];missing.append('unresolved_targets')
    if prices:
        lines+=['',('Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.' if en else 'อัตรานี้เป็นราคาเช่าเหมาโซนของหน่วยงาน ไม่ใช่ราคาต่อผู้เล่น/เครื่อง ไฟล์ไม่ได้ระบุจำนวนชั่วโมงของช่วงเช่าหรือวันที่มีผลของอัตรา')]
    if any(r['id']=='all_zones' for r in rows) and prices:
        lines.append(data['source_notes'][0]['text_en' if en else 'text_th'])
    lines+=['',('Source: user-provided half/full-day rental workbook' if en else 'แหล่งข้อมูล: ไฟล์ค่าบริการครึ่งวันและเต็มวันที่ผู้ใช้ส่งให้'),data['source_url']]
    known=bool(returned or ({'capacity','equipment'} & set(plan['asks']) and rows) or ('overtime' in plan['asks']))
    status='partial' if known and missing else 'missing' if missing else 'answered'
    outcome='answered_partial' if status=='partial' else 'no_answer' if status=='missing' else 'answered_complete'
    meta=dict(request_plan=plan,returned_rates=returned,missing_fields=missing,source_sha256=data['source_sha256'],source_sheet=data['source_sheet'],price_scope=data['price_scope'],effective_from=data['effective_from'],period_hours=data['period_hours'],outcome=outcome)
    route=PipelineRoute('service_fee','zone_rental_fee',.99,'fact','low','user-provided workbook zone/organization tariffs')
    contract=dict(schema_version=1,kind='single',status=status,outcome=outcome,category='service_fee',intent='zone_rental_fee',source_count=1,coverage_meaning='source_fields_not_live_booking_or_owner_missing_policy')
    return dict(answer='\n'.join(lines),hits=[make_source_hit(ZONE_RENTAL_FEES_20261006_ID)],route=route,entities=EntityBundle(),validation=ValidationResult(True,(),tuple(missing)),
        mode='pipeline:zone_rental_fee',trace=[PipelineTrace('zone_rental_contract',outcome,.99,'cell-bound source facts; no hourly/session conversion',meta),PipelineTrace('task_answer_contract',outcome,1.0,'requested known/missing source fields',contract)],metadata=meta)
