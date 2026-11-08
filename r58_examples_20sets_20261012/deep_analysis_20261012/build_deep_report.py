"""Exhaustive forensic report; only writes new analysis artifacts in this folder."""
import sys,json,collections,hashlib,ast,re,csv
from pathlib import Path
OUT=Path(__file__).resolve().parent;DATA=OUT.parent
sys.path.insert(0,str(DATA));import experiment as t
from app.knowledge.common import answer as a
SYS=t.SYSTEM
def read(p):return json.loads((DATA/p).read_text(encoding='utf-8'))
def rows(p):return [json.loads(x) for x in (DATA/p).read_text(encoding='utf-8').splitlines() if x.strip()]
def put(name,v):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8') as f:
        if isinstance(v,str):f.write(v+'\n')
        else:json.dump(v,f,ensure_ascii=False,indent=2)
def link(label,p,line=None):return f'[{label}]({Path(p).as_posix()}{":"+str(line) if line else ""})'
def block(v,kind='json'):return '\n```'+kind+'\n'+(v if isinstance(v,str) else json.dumps(v,ensure_ascii=False,indent=2))+'\n```\n'
def data_link(label,p):return link(label,DATA/p)
def out_link(label,p):return link(label,OUT/p)
ALL=sorted(rows('content_final/ANSWERS_AND_DECISIONS.jsonl'),key=lambda r:r['id'])
SUM=read('content_final/SUMMARY.json');FAIL=[r for r in ALL if not r['passed']]
STORE=t.CommonStore(t.DB);SNAP=STORE.snapshot();REC=SNAP['release']['records'];NAMES=SNAP['release']['names']
NONE={r['id']:r for r in rows('deep_analysis_20261012/NONE_ROUTE_REPLAY_V2.jsonl')}
LLM=rows('LLM_RESULTS.jsonl');CONV=rows('CONVERSATION_RESULTS.jsonl');HTTP=rows('HTTP_ROUND2_RESULTS.jsonl');PIPE=rows('PIPELINE_RESULTS.jsonl')
SOURCES={p:str(hashlib.sha256((SYS/p).read_bytes()).hexdigest()) for p in ['app/knowledge/common/answer.py','app/knowledge/common/planner.py','app/knowledge/common/registry.py','app/knowledge/common/store.py','app/knowledge/common/owner_server.py','app/pipeline/engine.py','app/pipeline/preprocess.py','app/web_api/server.py']}
def location(rel,text):
    for i,line in enumerate((SYS/rel).read_text(encoding='utf-8').splitlines(),1):
        if text in line:return link(rel,SYS/rel,i)
    raise RuntimeError('Missing code anchor '+text)
A='app/knowledge/common/answer.py';P='app/knowledge/common/planner.py';E='app/pipeline/engine.py'
LOC={
 'terms':location(A,'TERMS={'),'normal':location(A,'def normal('),'all':location(A,'def all_query('),'live':location(A,'def live_query('),'names':location(A,'def named('),'threshold':location(A,'if candidates and'),'fields':location(A,'def field_requests('),'history':location(A,'def context_query('),'pending':location(A,'if ids and not requested'),'return_none':location(A,'if not kind:return None'),'redirect':location(A,"if any(records[k]['kind']=='game'"),'gate':location(A,'if planner and not broad'),'clarify':location(A,"if remainder and method not in"),'defaults':location(A,'if not keys and not requested'),'bundles':location(A,"if r['kind']=='policy':keys="),'join':location(A,"if r['kind']=='game':"),'unmatched':location(A,'for key in requested:'),'finish':location(A,'def finish('),'ref':location(A,"elif key.endswith('_id')"),'conf':location(A,'confidence=1.0'),'validator':location(P,'def checked_plan'),'llm_schema':location(P,"schema={'type'"),'llm_prompt':location(P,"payload={'model'"),'llm_health':location(P,"record_llm_success('common_query_plan'"),'common_entry':location(E,'common = try_common_answer('),'preprocess':location(E,'pre = preprocess_input(question)'),'focus':location(E,'focused_question, focus = explicit_request_focus(question)'),'owner_preview':location('app/knowledge/common/owner_server.py',"if path=='/api/preview':"),'web_llm':location('app/web_api/server.py','LOCAL_LLM_ASSIST_ENABLED ='),'preprocess_impl':location('app/pipeline/preprocess.py','def preprocess_input(')}
FRIENDLY={
 'address':'ที่อยู่','building':'อาคาร','floor':'ชั้น','location':'ตำแหน่ง','room_seats':'จำนวนที่นั่งในห้อง','specifications':'สเปก','device_type':'ประเภทอุปกรณ์','capacity_persons':'คนเล่นพร้อมกันของเครื่อง','operational_status':'สถานะพร้อมใช้งานทางกายภาพ','session_minutes':'เวลาเล่นต่อรอบ (นาที)','occupancy_minutes':'เวลาที่กันช่องจอง (นาที)','required_proofs':'หลักฐานที่ต้องแสดง','eligibility':'ผู้ที่ใช้สิทธิ์ได้','value':'ช่องทางติดต่อ','office_hours':'เวลาติดต่อ','steps':'ขั้นตอน','required_documents':'เอกสารที่ต้องใช้','how_to_play':'วิธีเล่น','summary':'เนื้อหาเกม','details':'รายละเอียดข้อกำหนด','decision':'คำตัดสินอนุญาต/ห้าม','exceptions':'ข้อยกเว้น','offered':'มีเกมให้เล่นในบริการนี้หรือไม่','game_version':'รุ่นที่ติดตั้ง','players_min':'จำนวนผู้เล่นขั้นต่ำ','players_max':'จำนวนผู้เล่นสูงสุด','bindings':'ปุ่มควบคุม','platform':'แพลตฟอร์ม','amount_minor':'ราคา','duration_minutes':'ระยะเวลาที่ราคาครอบคลุม (นาที)','equipment_included':'อุปกรณ์ที่รวม','bookable_periods':'ช่วงเวลาที่จองได้','open_periods':'ช่วงเปิด','maintenance_periods':'ช่วงบำรุงรักษา','state':'สถานะวันพิเศษ','reason':'เหตุผล','rulebook_release':'ฉบับกติกา','competition_dates':'วันที่แข่ง','text':'ข้อความข้อกติกาเต็ม','completeness':'สถานะความครบของข้อกติกา','body':'เนื้อหาประกาศ','event_start':'เวลาเริ่มกิจกรรม','event_end':'เวลาจบกิจกรรม','role':'หน้าที่','public_contact_id':'รายการช่องทางติดต่อสาธารณะ','answer':'คำตอบ FAQ','scope_note':'ขอบเขตที่คำตอบใช้ได้','status_mapping':'การจับคู่สถานะ','freshness_policy':'ข้อกำหนดความสดของข้อมูล'}
CAUSES={
 'R01':('สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล','field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้',LOC['fields']),
 'R02':('จำนวนคน/ที่นั่ง/ระยะเวลาไปชน keyword ผิดความหมาย','คำกี่คนถูกจับเป็น players_min ทั่วทุกหมวด; บางคำถามจำนวนใช้เท่าไหร่แล้วไป amount_minor แม้ไม่มีเจตนาถามราคา ต้องแยก capacity/seat/min/max/session/occupancy',LOC['terms']),
 'R03':('ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ','TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope',LOC['fields']),
 'R04':('What is/about/description ถูกตีเป็น summary เกินบริบท','คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง',LOC['terms']),
 'R05':('ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ','list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ',LOC['fields']),
 'R06':('หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state','context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure',LOC['history']),
 'R07':('คำถามต่ออังกฤษไม่ผ่านเงื่อนไขอ่านประวัติ','guard มี แล้ว/it/this/that หรือ field_requests/all_query; And เพียงอย่างเดียวไม่มี จึงไม่ยืม record ก่อนหน้าแล้ว fallback kind หาไม่ได้',LOC['history']),
 'R08':('fuzzy ปฏิเสธชื่อที่ยังคลุมเครือ','SequenceMatcher ต้องได้ >=0.88 และอันดับแรกห่างอันดับสอง >=0.06 นี่เป็น guard เลือกผิดรายการ ไม่ใช่ probability; ดู score จริงใน replay ก่อนตัดสินลด threshold',LOC['threshold']),
 'R09':('พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง','method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน',LOC['clarify']),
 'R10':('คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย','field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม',LOC['fields']),
 'R11':('รูปแบบ JSON โมเดลกว้างกว่าข้อกำหนดรับผล','schema อนุญาต platform string ใดก็ได้ แต่ checked_plan รับเฉพาะ null/แพลตฟอร์มใน records; โมเดลจึงส่ง record ID/unknown/service แล้วทั้ง plan ถูกปฏิเสธ',LOC['llm_schema']),
 'R12':('ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ','planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม',LOC['gate']),
 'R13':('คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด','all_query ตรวจครบแบบ substring และ all\\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง',LOC['all']),
 'R14':('confidence/validation/source trust ถูกปนกับการตอบตรงคำถาม','finish ตั้ง confidence 1.0 และ ValidationResult(True) คงที่ หลังพิมพ์ผลจาก typed fields โดยไม่ได้ทวนทุกส่วนคำถาม; health success ไม่ตรวจ accepted plan',LOC['conf']),
 'R15':('ทางเข้าฐานกลางคืนคำตอบก่อนใช้ preprocess/dialogue ของเส้นทางเดิม','engine เรียก common ก่อน explicit_request_focus/preprocess_input และ returns ทันทีเมื่อ non-None; clarification/unknown จาก common จึงไม่ใช้ตัวแก้ typo/typed plan ที่อยู่ถัดไป',LOC['common_entry']),
 'R16':('ข้อมูลอ้างอิงแสดงเป็นรหัสภายในแทนข้อมูลปลายทางที่ใช้ได้','title เลือก title/name/display_name/... ไม่มี value ของ contact; การ render *_id จึงอาจพิมพ์ demo20_contact_* แทน channel+value และ scorer ก็ยอมรับชื่อ fallback นี้',LOC['ref']),
 'R17':('คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ','score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ',LOC['defaults']),
 'R18':('ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown','ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field',LOC['unmatched']),
 'R19':('การอ่าน label ไทยและการปรับตัวพิมพ์ไม่สมมาตร','q ถูก casefold แต่ meaning_th ไม่ถูก casefold ในการเทียบ fallback; labels ที่มี API/PC/ISO/WordPress/VR เป็นต้นหลุด exact match นี่มีหลักฐานแยกจากชุดก่อน ไม่เหมารวมทุกเคสใหม่',LOC['fields']),
 'R20':('การสลับไปกฎแข่งใช้ details เป็นสัญญาณกว้างเกินไป','เกมที่มี details ถูกเปลี่ยน ids เป็น competition โดยไม่ยืนยัน competition intent หรือคำปฏิเสธ; พบจริงใน age_rating contract ชุดเดิม ไม่มีเหตุให้แก้ข้อมูลเกมเพื่อชดเชย',LOC['redirect']),
 'R21':('live routing และราคาฟรีใช้คำร่วมกัน','live_query ตรวจ free แบบคำเดี่ยว; Is this free to play? จึงชี้ไป live route แม้เป็นราคา 0 ต้องแยก free-of-charge จาก free station; เป็น probe/helper ที่ยืนยันได้ ยังไม่ใช่ count ใน 2403',LOC['live'])}
QUANTITY={'capacity_persons','capacity_max','capacity_min','room_seats','players_min','players_max','session_minutes','occupancy_minutes','duration_minutes'}
def plan(r):return (r.get('decision') or {}).get('query_plan',{})
def lexical(r):
    q=a.normal(r['question']);p=plan(r); spans=[]
    for rid in p.get('record_ids',[]):
        for alias in NAMES.get(rid,[]):
            alias=a.normal(alias)
            if alias:
                for match in re.finditer(re.escape(alias),q):spans.append((match.start(),match.end(),alias))
    tokens=[]
    for key,terms in a.TERMS.items():
        for term in terms:
            for m in re.finditer(re.escape(term),q):tokens.append({'field':key,'term':term,'offset':m.start(),'inside_named_entity':any(s<=m.start() and m.end()<=e for s,e,_ in spans)})
    kinds={REC[x]['kind'] for x in p.get('record_ids',[]) if x in REC}
    if 'game' in kinds:kinds.update(('game_service','game_mode','control_set'))
    direct=[]
    for k in kinds:
        for f in t.CATALOG[k]['fields']:
            keymatch=f['key'].replace('_',' ') in q;labelmatch=f['meaning_th'] in q
            if keymatch or labelmatch:direct.append({'field':f['key'],'kind':k,'match':'canonical key' if keymatch else 'meaning_th literal'})
    return {'term_matches':tokens,'catalog_matches':direct,'normalization':'NFC + casefold + collapse spaces only'}
def tags(r):
    p=plan(r);req=p.get('requested_fields',[]);exp=set(r['expected_fields']);result=[]
    if not r['passed']:
        if not r.get('decision'):result.append('R07' if r['style']=='followup' else 'R08')
        elif not req and not p.get('all_fields'):result.append('R01')
        if exp&QUANTITY and (('players_min' in req and (not 'players_min' in exp or 'players_max' in exp and 'players_max' not in req)) or ('amount_minor' in req and not 'amount_minor' in exp)):result.append('R02')
        kinds={REC[x]['kind'] for x in p.get('record_ids',[]) if x in REC}
        if 'game' in kinds:kinds.update(('game_service','game_mode','control_set'))
        supported={f['key'] for k in kinds for f in t.CATALOG[k]['fields']}
        virtual={'amount_minor'} if kinds&{'service','audience','zone'} else set()
        if req and set(req)-supported-virtual:result.append('R03')
        if 'summary' in req and 'summary' not in exp:result.append('R04')
        if len(exp)>1:result.append('R05')
        if r['style']=='followup' or 'history' in p.get('method',''):result.append('R06')
        if any(x['inside_named_entity'] for x in lexical(r)['term_matches']):result.append('R10')
        overview=bool(re.search(r'รายละเอียด|ข้อมูล|\b(?:details|information|tell me about)\b',r['question'],re.I))
        eligible=not p.get('all_fields') and not overview and (not req or req==['steps'] and not set(req)&supported)
        if req and not eligible and any(x.startswith('missing_field:') for x in r['reasons']):result.append('R12')
        if any(o.get('record_id') is None for o in (r.get('decision') or {}).get('obligations',[])):result.append('R18')
    if r['passed'] and not p.get('all_fields') and not req and r['style'] not in {'all_fields','old_control_all_fields'}:result.extend(('R09','R17'))
    if p.get('all_fields') and r['style'] not in {'all_fields','old_control_all_fields'}:result.extend(('R13','R17'))
    return list(dict.fromkeys(result))
def expected(r):
    target=REC[r['rid']];out=[]
    for key in r['expected_fields']:
        f=target['fields'][key];label=FRIENDLY.get(key,key)
        if f['status']=='unknown':v='ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed'
        elif f['status']=='not_applicable':v='ไม่เกี่ยวข้องกับรายการนี้ / Not applicable'
        elif key=='amount_minor':v=f'{f["value"]//100:,}.{f["value"]%100:02d} '+str(t.prior.value(target,'currency') or 'THB')
        elif key.endswith('_id') or key.endswith('_ids'):
            ids=f['value'] if isinstance(f['value'],list) else [f['value']]
            values=[]
            for rid in ids:
                ref=REC[rid];display=a.title(ref,r['lang'])
                if ref['kind']=='contact':display+=' — '+str(t.prior.value(ref,'channel'))+': '+str(t.prior.value(ref,'value'))
                values.append(display)
            v=', '.join(values) if values else 'ไม่มีรายการอ้างอิง (ยืนยันใน fixture)'
        elif key=='steps':
            pieces=[]
            for step in sorted(f['value'],key=lambda s:s['order']):
                instruction=str(step['order'])+'. '+a.text(step['instruction'],r['lang'])
                contact=REC.get(step.get('contact_id'))
                if contact:instruction+=' — '+str(t.prior.value(contact,'channel'))+': '+str(t.prior.value(contact,'value'))
                pieces.append(instruction)
            v='\n'.join(pieces)
        elif key=='bindings':v='\n'.join(a.text(x['action'],r['lang'])+' → '+', '.join(x['buttons'])+' / '+x['gesture']+' / '+a.text(x['context'],r['lang']) for x in f['value'])
        else:v=a.text(f['value'],r['lang'])
        out.append(label+' ('+key+'): '+v)
    return '\n'.join(out)
def reason_text(r):
    p=plan(r);req=p.get('requested_fields',[]);exp=r['expected_fields'];obs=(r.get('decision') or {}).get('obligations',[])
    miss=[k for k in exp if not any(o.get('record_id')==r['rid'] and o.get('field')==k for o in obs)]
    if not r.get('decision'):
        n=NONE.get(r['id'])
        if n:return 'original CommonAnswerer คืน None ที่บรรทัด '+str(n['observed']['return_line'])+'; '+n['diagnostic']+'; ไม่มี fallback legacy ถูกเรียกใน core test นี้'
        return 'ไม่มีผลจาก CommonAnswerer ใน log นี้ ยังไม่ใช่หลักฐานว่า DB ไม่มีข้อมูล'
    if not req and not p.get('all_fields'):
        return ('หา '+r['rid']+' ถูกแล้ว แต่ requested_fields=[]; '+('bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent' if r['passed'] else 'ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด'))
    if r['passed'] and p.get('all_fields') and r['style'] not in {'all_fields','old_control_all_fields'}:return 'broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent'
    return 'เลือก record '+str(p.get('record_ids'))+' และหัวข้อ '+str(req)+'; field ของ target ที่ยังไม่มี obligation คือ '+str(miss)+'. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด'
def signature(r):
    p=plan(r);states=tuple((k,REC[r['rid']]['fields'][k]['status']) for k in r['expected_fields'])
    return (r['kind'],r['lang'],r['style'],tuple(r['expected_fields']),tuple(p.get('requested_fields',[])),p.get('all_fields'),p.get('method'),(r.get('decision') or {}).get('response_type'),states,tuple(tags(r)))
def case_doc(r):
    codes=tags(r);lex=lexical(r);gold={k:REC[r['rid']]['fields'][k] for k in r['expected_fields']}
    s=f'\n## Case {r["id"]}\n\n**หมวด:** {r["kind"]} • **ภาษา:** {r["lang"]} • **รูปแบบ:** {r["style"]} • **record ที่ควรตอบ:** `{r["rid"]}`\n\n'
    s+='### ผู้ใช้ถามอะไร\n'+block(r['question'],'text')
    if r['history']:s+='\nประวัติที่ส่งจริง:'+block(r['history'])
    s+='\nสิ่งที่ผู้ใช้ควรได้รับตาม fixture: '+', '.join(FRIENDLY.get(k,k)+' (`'+k+'`)' for k in r['expected_fields'])+'\n'
    s+='\n### คำตอบที่ระบบส่งจริง\n'+block(r.get('answer') or '[CommonAnswerer returned None]','text')
    s+='\n### คำตอบที่ควรได้จากชุดตัวอย่าง\n\nคำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:\n'+block(expected(r),'text')
    s+='\n### ทำไมได้คำตอบแบบนี้\n\n'+reason_text(r)+'\n\n'
    for code in codes:
        label,desc,loc=CAUSES[code];s+='- **'+code+' — '+label+'**: '+desc+' • '+loc+'\n'
    s+='\nแผนและ obligations ที่อยู่ใน log:'+block(r.get('decision'))
    s+='\nคำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):'+block(lex)
    if r['id'] in NONE:s+='\nการตรวจ return branch/คะแนน fuzzy ด้วยตัวเดิม:'+block(NONE[r['id']])
    s+='\n### ทำไมคะแนนจึงตก/ผ่าน\n\n'+('ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ' if r['passed'] else ', '.join(r['reasons']))+'\n\n'
    s+='สถานะและค่าที่เป็น ground truth พร้อม evidence refs:'+block(gold)
    s+='\n'+data_link('record JSON เดิม','records/'+r['kind']+'/'+r['rid']+'.json')+'\n' if r['rid'].startswith('demo20_') else '\n'+link('record JSON เดิม',t.OLD/'records'/r['kind']/(r['rid']+'.json'))+'\n'
    s+='\nการแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน\n'
    return s
def main():
    assert len(ALL)==5056 and len(FAIL)==2403 and len(NONE)==131
    assert all(r['replayed_none'] for r in NONE.values())
    groups=collections.defaultdict(list);bycause=collections.defaultdict(list);annotations=[]
    for r in ALL:
        codes=tags(r)
        annotations.append({'case_id':r['id'],'passed_required_content':r['passed'],'rid':r['rid'],'kind':r['kind'],'lang':r['lang'],'style':r['style'],'cause_tags':codes,'explanation':reason_text(r) if not r['passed'] or codes else 'ผ่าน required content; ไม่มี issue ที่ detector ชุดนี้ยืนยันเพิ่ม ไม่ใช่ human quality approval','missing_fields':[x.split(':',1)[1] for x in r['reasons'] if x.startswith('missing_field:')]})
        if not r['passed']:groups[signature(r)].append(r)
        for code in codes:bycause[code].append(r)
    put('CASE_ANNOTATIONS_5056.json',annotations)
    weak=[r for r in ALL if r['passed'] and tags(r)]
    for k in t.ORDER:
        rs=[r for r in FAIL if r['kind']==k]
        text=f'# ภาคผนวกเคสไม่ผ่าน — {k} / {len(rs)} เคส\n\n**{t.WARNING}**\n\nอ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง\n'
        text+='\nรายการเคส: '+', '.join('[Case '+r['id']+'](#case-'+r['id']+')' for r in rs)+'\n'
        for r in rs:text+=case_doc(r)
        put('FAILURES_BY_CATEGORY/'+k+'.md',text)
    weakdoc=f'# เคสผ่านเนื้อหาแต่มีประเด็นเพิ่มเติม — {len(weak)} เคส\n\nไม่ใช่การย้ายทุกเคสเหล่านี้ไปเป็นผิดโดยอัตโนมัติ: domain bundles บางแบบจำเป็นต่อราคา/กฎ แต่การเลือกหัวข้อยังต้องแยกจากการพิมพ์ค่าไว้ครบ\n'
    for r in weak:weakdoc+=case_doc(r)
    put('PASSES_NEED_REVIEW.md',weakdoc)
    groupdoc='# กลุ่มรูปแบบผิดที่ซ้ำกัน\n\nจับกลุ่มตาม kind/language/style/expected fields/requested fields/method/response type/status ของ gold/cause tags ตัวอย่าง 20 ชุดที่ลักษณะเดียวกันจึงเห็นทั้ง pattern และ case IDs ไม่ถือว่า 2,403 คือ 2,403 บั๊กคนละตัว\n'
    groupmeta=[]
    for i,(sig,rs) in enumerate(sorted(groups.items(),key=lambda x:(-len(x[1]),str(x[0]))),1):
        r=rs[0];meta={'group_id':f'G{i:03}','count':len(rs),'kind':r['kind'],'lang':r['lang'],'style':r['style'],'expected_fields':r['expected_fields'],'requested_fields':plan(r).get('requested_fields'),'method':plan(r).get('method'),'cause_tags':tags(r),'case_ids':[x['id'] for x in rs]};groupmeta.append(meta)
        groupdoc+=f'\n## G{i:03} — {len(rs)} เคส / {r["kind"]} / {r["lang"]} / {r["style"]}\n\n'+reason_text(r)+'\n\nตัวอย่างถาม: '+r['question']+'\n\n'+block(meta)
        groupdoc+='\n[ดูตัวอย่างรายเคส]('+(OUT/('FAILURES_BY_CATEGORY/'+r['kind']+'.md')).as_posix()+'#case-'+r['id']+')\n'
    put('FAILURE_PATTERN_GROUPS.md',groupdoc);put('FAILURE_PATTERN_GROUPS.json',groupmeta)
    # Audit passes with accidental/unrequested unknowns, broad trigger, default bundles and raw references.
    pass_unknown=[];bundle=[];internal=[]
    for r in ALL:
        if not r['passed']:continue
        p=plan(r);obs=(r.get('decision') or {}).get('obligations',[])
        extras=[o for o in obs if o.get('record_id') is None and o.get('field') not in r['expected_fields']]
        if extras:pass_unknown.append({'id':r['id'],'question':r['question'],'style':r['style'],'kind':r['kind'],'extra_unknown':extras,'plan':p,'answer':r['answer']})
        if r['style'] not in {'all_fields','old_control_all_fields'} and not p.get('all_fields'):
            unmapped=set(r['expected_fields'])-set(p.get('requested_fields',[]))
            if unmapped:bundle.append({'id':r['id'],'kind':r['kind'],'style':r['style'],'unmapped_expected_fields':sorted(unmapped),'plan':p})
        for o in obs:
            rr=REC.get(o.get('record_id'));field=o.get('field')
            if rr and field in rr['fields'] and field.endswith(('_id','_ids')):
                val=t.prior.value(rr,field);vs=val if isinstance(val,list) else [val]
                for value in vs:
                    if value in REC and a.title(REC[value],r['lang'])==value and value in r['answer']:internal.append({'id':r['id'],'kind':r['kind'],'field':field,'reference_id':value,'target_kind':REC[value]['kind']})
    metrics={'main_queries':len(ALL),'failed_required_content':len(FAIL),'passed_required_content':len(ALL)-len(FAIL),'distinct_failure_patterns':len(groups),'cause_counts_nonexclusive':{k:{'all':len(v),'failed':sum(not r['passed'] for r in v),'passed_flagged':sum(r['passed'] for r in v)} for k,v in bycause.items()},'passed_extra_unknown_messages':len(pass_unknown),'passed_unmapped_gold_from_defaults_or_bundles':len(bundle),'passed_internal_reference_case_count':len({x['id'] for x in internal}),'passed_internal_reference_occurrences':len(internal),'none_route_summary':json.loads((OUT/'NONE_ROUTE_SUMMARY_V2.json').read_text(encoding='utf-8')),'source_sha256':SOURCES,'human_review':False}
    put('AUDIT_METRICS.json',metrics);put('PASSED_EXTRA_UNKNOWN_MESSAGES.json',pass_unknown);put('PASSED_DEFAULT_BUNDLE_COVERAGE.json',bundle);put('PASSED_INTERNAL_REFERENCE_RENDERING.json',internal)
    put('HELPER_PROBES.json',{'scope':'Pure helper calls only; not requests measured in original 5056 or full live web answers','all_query':{q:a.all_query(q) for q in ['ข้อมูลครบไหม','ไม่ต้องตอบทั้งหมด','football','small','install']},'live_query':{q:a.live_query(q) for q in ['Is this free to play?','Do I need to pay?','มีเกมนี้ให้เล่นไหม']}})
    oldfail=json.loads((t.OLD/'content_final/FAILURES.json').read_text(encoding='utf-8'))
    supplemental=[r for r in oldfail if r['style']=='field_contract']
    olddoc='# ภาคเสริม: contract failures ชุดเดิม 130 เคส\n\n**แยกจาก 2403 failures ของชุดใหม่ ห้ามรวมยอด** ใช้ยืนยัน casefold/label contamination/game-to-competition redirect ที่ code ยังมีอยู่ ไม่ได้บอกว่าทั้ง130เกิดจากสาเหตุเดียว\n'
    for r in supplemental:
        olddoc+=f'\n## Old Case {r["id"]} — {r["kind"]} / {r["lang"]}\n\nถาม: {r["question"]}\n\nควรอ่าน fields: {r["expected_fields"]}\n\nตอบเดิม:'+block(r['answer'] or '[None]','text')+'\nPlan:'+block(r.get('decision'))+'\n'+link('record เดิม',t.OLD/'records'/r['kind']/(r['rid']+'.json'))+'\n'
    put('OLDER_CONTRACT_130_CASES.md',olddoc)
    # Per-kind field coverage: detect exact top missed fields, not only pass %.
    coverage=[]
    for k in t.ORDER:
        rs=[r for r in ALL if r['kind']==k]
        for key in {f for r in rs for f in r['expected_fields']}:
            demand=[r for r in rs if key in r['expected_fields']];met=[r for r in demand if any(o.get('record_id')==r['rid'] and o.get('field')==key for o in (r.get('decision') or {}).get('obligations',[]))]
            coverage.append({'kind':k,'field':key,'expected_queries':len(demand),'field_obligation_found':len(met),'missing':len(demand)-len(met)})
    put('FIELD_OBLIGATION_COVERAGE.json',coverage)
    with (OUT/'CASE_INDEX.csv').open('x',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f);writer.writerow(['case_id','kind','lang','style','content_pass','cause_tags','question'])
        for r in ALL:writer.writerow([r['id'],r['kind'],r['lang'],r['style'],r['passed'],';'.join(tags(r)),r['question']])
    llmdoc='# ผล LLM ทั้ง 48 เคส พร้อมผลดิบและข้อจำกัดที่ปฏิเสธ\n\n27 planner attempts / raw outputs; ไม่มีการเรียกโมเดลซ้ำเพื่อมาแทนผลเดิม\n'
    baseline={(r['rid'],r['lang'],r['style']):r for r in ALL}
    llmcounts=collections.Counter()
    for i,r in enumerate(LLM,1):
        llmdoc+=f'\n## LLM Case {i:02} — main case {r["id"]}\n\nถาม: {r["question"]}\n\nปิด LLM: '+str(baseline[(r['rid'],r['lang'],r['style'])]['passed'])+' • เปิด LLM: '+str(r['passed'])+'\n\nคำตอบที่ได้:'+block(r.get('answer') or '[None]','text')+'\nควรตอบ:'+block(expected(r),'text')
        if not r['planner_attempts']:llmdoc+='\nไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด\n'
        for attempt in r['planner_attempts']:
            llmdoc+='\nPlanner attempt:'+block(attempt)
            for raw in attempt['raw_responses']:
                p=json.loads(raw);platform=p.get('platform');allowed={t.prior.value(rec,'platform') for rec in REC.values() if t.prior.value(rec,'platform')}
                rejected=platform is not None and platform not in allowed;llmcounts['invalid_platform' if rejected else 'accepted_shape']+=1
                llmdoc+='\n'+('ปฏิเสธเพราะ platform='+repr(platform)+' ไม่อยู่ใน '+repr(sorted(allowed))+' และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว' if rejected else 'platform ผ่านข้อกำหนด; ดู accepted checked_plan และผล scorer แยกกัน')+'\n'
        llmdoc+='\nPlan สุดท้าย:'+block(r.get('decision'))
    put('LLM_ALL_48_CASES.md',llmdoc)
    convdoc='# วิเคราะห์บทสนทนา 3 รอบที่พลาด ทั้ง 120 turns\n\nประวัติมีข้อความ assistant จริง ไม่มีเหตุให้สรุปว่าประวัติหายทุกเคส ต้องอ่าน record_ids/method กับ requested_fields แยกกัน\n'
    for r in CONV:
        if not r['passed']:
            convdoc+=f'\n## {r["id"]}\n\nถาม: {r["question"]}\n\nประวัติ:'+block(r['history'])+'\nตอบ:'+block(r.get('answer') or '[None]','text')+'\nควรตอบ:'+block(expected(r),'text')+'\nPlan/obligations:'+block(r.get('decision'))+'\n'+reason_text(r)+'\n'
    put('CONVERSATION_FAILURES_120.md',convdoc)
    # HTTP / actual pipeline correspondence, without pretending skipped fallbacks were run.
    hmap={r['id']:r for r in HTTP};pmap={r['id']:r for r in PIPE};pairs=[]
    for key in hmap:
        h=hmap[key];p=pmap[key];pairs.append({'case_id':key,'question':h['question'],'http_200':h.get('http_status')==200,'http_pass':h['passed'],'pipeline_pass':p['passed'],'same_pass':h['passed']==p['passed'],'legacy_skipped':p.get('legacy_skipped',False)})
    put('HTTP_PIPELINE_PAIRS_224.json',pairs)
    # Main readable synthesis, with representative examples and source links.
    md=f'''# วิเคราะห์สาเหตุการตอบผิดอย่างละเอียด — PSU Esports Chatbot / format กลาง

**{t.WARNING}**

วันที่อ้างอิง 2026-10-12 เวลาไทย รายงานนี้วิเคราะห์ข้อมูลเดิมที่รันเสร็จแล้วครบ 5,056 เคส รวม 2403 เคสที่ไม่ผ่าน และประเด็นในเคสที่ผ่าน เพิ่มเฉพาะ diagnostic replay ของ 131 เคสที่ CommonAnswerer คืน None ไม่รัน full GT ไม่แก้โค้ดหรือข้อมูลจริง

## วิธีอ่านรายงาน

- เริ่มจากข้อ 1–4 เพื่อเห็นภาพและความหมายของคะแนน
- ข้อ 5–15 อธิบายว่าทำไมข้อมูลมีแต่เลือกตอบผิด พร้อมตัวอย่างจริงและโค้ด
- ข้อ 16–22 ตรวจ LLM, confidence, ภาษา, การแสดงผล, การทดสอบ และข้อจำกัด
- ภาคผนวกแยกครบทุกเคสที่ตกตาม 24 หมวด ดูคำถาม คำตอบจริง ค่าที่ควรตอบ history, plan, obligations, keyword ที่จับ และ source refs
- `CASE_ANNOTATIONS_5056.json` มีรายการทุกเคสทั้งผ่าน/ไม่ผ่าน; `FAILURE_PATTERN_GROUPS.md` รวม pattern ซ้ำ {len(groups)} กลุ่ม เพื่อไม่เข้าใจว่า 2403 คือบั๊กคนละตัวทั้งหมด

## 1. ข้อสรุปที่หลักฐานรองรับ

ระบบเก็บและอ่านข้อมูล typed fields ได้ แต่การแปลงคำถามเป็น **record ที่ต้องใช้ + fields ที่ต้องตอบ + ความสัมพันธ์ + จำนวนหัวข้อ + ขอบเขต** ยังไม่ครบ เมื่อขอทุกข้อมูลจึงได้ครบ แต่คำถามเจาะจงถูก matcher เลือก field ผิดหรือเลือกไม่ได้

จากเคสไม่ผ่าน 2403: **1509** หา record ถูกแต่ field ว่าง; **763** หา record ถูกแต่เลือก field ไม่ครบ/ผิด; **131** CommonAnswerer คืน None. รวม 2272/2403 = 94.55% ที่ตกมีหลักฐานว่า target record ถูกแล้ว ปัญหาอยู่ขั้น field/intent มากกว่าการขาด record ในชุดนี้

คำว่า “ตอบผิด” รวมการถามกลับทั้งที่ข้อมูลพร้อม, บอกยังไม่มีข้อมูลทั้งที่ field ที่ถูกมีค่า, ตอบผิดมิติ เช่นขั้นต่ำแทนสูงสุด, และตอบขาดบางหัวข้อ ไม่ได้หมายความว่าทั้ง 2403 เคสแต่งข้อเท็จจริง

## 2. ข้อมูลและขอบเขตที่วิเคราะห์

20 ชุด × 24 หมวด = 480 records ใหม่ กับ 240 เดิม รวม 720 records ใน DEMO. 155 field slots ใน catalog / 122 ชื่อ field ไม่ซ้ำ. TERMS มีเพียง 13 กลุ่ม intent แบบ keyword; catalog ทำให้ field ใหม่ถูกอ่านและแสดงได้ แต่ไม่ได้สร้าง semantic interpretation ทุกสำนวนให้อัตโนมัติ

คำถามหลัก 5056 = ใหม่ 4960 + control เดิม 96. ภาษาไทย 2528, อังกฤษ 2528. ตัวอย่างข้อมูลสมมุติ ราคาศูนย์บาท/known-empty/known-false/unknown/min–max/time ต่างกันถูกเก็บไว้เพื่อดู guard. ไม่มีหลักฐานจากชุดนี้เรื่องความถูกต้องของสถานะ WordPress จริงหรือ translation ที่เจ้าของรับรอง

| ส่วน | ผ่านเกณฑ์เนื้อหา | ไม่ผ่าน | ความหมาย |
|---|---:|---:|---|
| ทั้งหมด | 2653 | 2403 | 52.47% ตาม scoring นี้ ไม่ใช่ human accuracy |
| เฉพาะใหม่ | 2584 | 2376 | 4960 เคส |
| ขอทั้งหมดใหม่ | 960 | 0 | ไม่ต้องเลือกหัวข้อย่อยจากคำถาม |
| สำนวนทั่วไป | 420 | 540 | 960 เคส |
| เปลี่ยนสำนวน | 380 | 580 | 960 เคส |
| ถามต่อ | 440 | 520 | 960 เคส |
| หลายหัวข้อ | 320 | 640 | 960 เคส |
| พิมพ์ซ้ำ | 64 | 96 | 160 เคส; 26 ที่ผ่านยังไม่ resolve field |
| control เดิม | 69 | 27 | เทียบเดิมแล้วไม่เปลี่ยน pass หรือ query_plan เลย 96 เคส |
| HTTP | 116 | 108 | HTTP 200 ครบ 224; ขนส่งสำเร็จไม่เท่ากับตอบถูก |
| pipeline จริง | 116 | 108 | 224 เคส, skipped legacy 8 เมื่อ common miss |
| บทสนทนา 3 รอบ | 360 | 120 | 160 first + 40 followup + 160 switch ผ่าน |
| LLM เฉพาะปัญหา | 5 | 43 | baseline เดียวกัน 3/48; attempts 27, accepted 2 |

หลายแถวใช้คำถามซ้ำกัน ห้ามรวมยอดเป็น unique requests คะแนนชุดเก่า 84.66% เทียบ 52.47% ชุดใหม่ตรง ๆ ไม่ได้ เพราะชุดเก่ามี contract-key/label queries 3100 แต่ชุดใหม่เน้น natural/multi-field ไม่มีการเปลี่ยนโค้ดก่อน/หลังในรอบนี้

## 3. หลักฐานแต่ละระดับและสิ่งที่ยังไม่รู้

| ระดับ | สิ่งที่มี | สิ่งที่สรุปได้ |
|---|---|---|
| log ต้นฉบับ | question, history, answer, decision, obligations, evidence, reasons | ระบบส่งข้อความไหนและเลือก field/record อะไร |
| code ที่ใช้รัน | hash ของ source และ code links ระบุบรรทัด | เงื่อนไขนั้นเกิดได้อย่างไรและอยู่ส่วนไหน |
| replay เฉพาะ None | 131 เคสคืน None เหมือนเดิม, return line, ratio ของ matcher เดิม | ระบุจุดออกและ threshold/margin ของ typo 11 เคส |
| วิเคราะห์ keyword | TERMS/catalog เดิมเทียบ q เดิม, annotate entity spans | คำไหนเข้า matcher; เป็นการคำนวณเพิ่ม ไม่ใช่แสร้งว่า log เดิมเคยบันทึกไว้ |
| LLM raw เดิม | 27 JSON responses ครั้งเดียวกับ 48 tests | emitted platform ผิดจริง 25 ครั้ง; ไม่มีเหตุ timeout/network ใน health ชุดนี้ |
| ข้อสันนิษฐาน | prompt ไม่อธิบาย platform/ไม่ enum | เป็นปัจจัยที่ทำให้โมเดลเลือก string ผิดได้ แต่ไม่เห็นกระบวนการคิดภายในโมเดล |
| ยังไม่ได้ยืนยัน | UX, อังกฤษทุกคำ, ผู้ใช้จริงทุกสำนวน, runtime fallback ของทุก None | ห้ามอ้างว่าอัตโนมัติยืนยันครบแล้ว |

## 4. Flow ที่ทำงานจริงและตำแหน่งที่พลาด

```mermaid
flowchart TD
    Q[รับคำถามและ recent_history] --> C[Common content ก่อน preprocess เดิม]
    C --> N[เลือก record ด้วย exact / fuzzy / history]
    N --> F[เลือก fields ด้วย TERMS + key / label]
    F --> B{{ขอทั้งหมดหรือไม่}}
    B -->|ใช่| ALL[อ่านทุก field และ child records]
    B -->|ไม่ใช่| G{{LLM gate ผ่านหรือไม่}}
    G -->|ผ่าน| L[LLM เลือก fields และ platform]
    L --> V{{checked_plan รับหรือปฏิเสธ}}
    V -->|ปฏิเสธ| OLD[ใช้ requested เดิมหรือ clarification]
    G -->|ไม่ผ่าน| OLD
    V -->|รับ| R[อ่าน requested fields / joins]
    OLD --> R
    ALL --> OUT[render + evidence + static confidence]
    R --> OUT
    OUT --> RETURN[คืนทันที ถ้า common non-None]
    N -->|ยังไม่มี target และ infer kind ไม่ได้| NONE[คืน None ให้เส้นทางถัดไป]
```

ต้องแยก entity resolution, field resolution, join resolution, answer coverage และ rendering. ทั้งห้าส่วนไม่เท่ากัน การหา record ถูกและมี citation ยังตอบผิดส่วนได้

## 5. R01 — ทำไมสำนวนเปลี่ยนแล้วเลือกหัวข้อไม่ได้

field_requests ใช้ `any(term in q)` และ full literal catalog labels. เช่น “อยู่ไหน” ไม่ตรง “อยู่ตรงไหน”; “เล่นยังไง” ไม่ตรง “ต้องทำอะไรเพื่อเล่นให้สำเร็จ”; “required proofs” ไม่ตรง “Which documents do I need to show?”. NFC/casefold ช่วยตัวอักษร/ตัวพิมพ์ ไม่ได้เข้าใจคำพ้องหรือความหมายประโยค

เหตุให้ข้อความถามกลับไม่ช่วย: clarification ถูก hardcode ว่า วิธีเล่น/ปุ่ม/อุปกรณ์/ราคา สำหรับทุกหมวด เช่นถามหลักฐานของ audience ยังได้รับตัวเลือกเกม/ราคา. ข้อมูลมี known required_proofs อยู่แล้ว จึงควรตอบหรือถามเจาะจงหัวข้อที่จำเป็น ไม่ถามซ้ำกว้าง ๆ

## 6. R02/R03 — ทำไมกี่คนได้ players_min และทำไมบอกไม่มีข้อมูล

คำจำนวนคนต้องแยกอย่างน้อย resource.capacity_persons, zone.room_seats, service.capacity_min/capacity_max, game_mode.players_min/players_max และ rental.room_seats. Matcher กลางใช้ players_min เพียงตัวเดียว; ใน resource ไม่มี key นี้ จึง add ไม่ทำงาน แล้วท้าย answer สร้าง unknown record_id=None.

ดังนั้นข้อความ “ยังไม่มีข้อมูล” ในเคสนี้หมายถึง field ที่ matcher เลือกไม่ถูกตอบ ไม่ใช่ว่า capacity_persons ไม่ทราบ. ส่วน game_mode มี players_min จริง จึงอาจตอบขั้นต่ำ 1 ทั้งที่ผู้ถามอยากรู้สูงสุด 4/8/12. ความผิดแบบหลังอันตรายกว่าการถามกลับ เพราะตัวเลขมาจาก source จริงแต่คนละความหมาย

## 7. R04 — ทำไม What is... ไป summary แล้วตอบผิดหมวด

summary มีคำ `what is`, `about`, `description` ใช้ทุก kind. What is their role? / What is the maximum player count? / What is the answer? จึงอาจไป field summary ซึ่งไม่มีใน person/game_mode/faq. ตัวแปร field_kinds จำกัดเฉพาะการวน catalog แต่ไม่ได้กรอง TERMS กลาง เป็นความผิดของขอบเขต matcher ไม่ใช่ข้อพิสูจน์ว่าอังกฤษแปลผิด

## 8. R05 — ทำไมตอบหลายเรื่องไม่ครบ

คำถามหนึ่งประโยคอาจขอราคา+นาที, อาคาร+ชั้น, มีเกมไหม+version, เริ่ม+จบ, กฎ+completeness. ปัจจุบันไม่มีตัวแยก question slots และไม่มี postcondition ทุกส่วนต้องมี answer/status. หากหาเจอ floor แต่ไม่เจอ building, หรือ event_start แต่ไม่เจอ event_end ก็พิมพ์ส่วนที่มีแล้วจบ

ส่วนราคา/แพ็กเกจพิมพ์ทุก fields โดย design และ policy แนบ decision/conditions/exceptions/details/consequence เสมอ จึงสามารถผ่านหลายหัวข้อแม้ plan ไม่ได้เลือกทุก key. การแนบเงื่อนไขราคา/กฎเป็นสิ่งที่ควรรักษา แต่ไม่ควรใช้การแนบเผื่อแทนการพิสูจน์ว่าเข้าใจทุกเรื่อง

## 9. R06/R07 — ประวัติหายหรือ field ไม่ได้ถูกเข้าใจ

ต้องอ่าน method/record_ids/requested_fields. บางเคส method=history_exact และ record ถูก แต่ requested=[] หรือ players_min ผิด. ถ้าแก้ส่ง history เพิ่มเฉย ๆ จะไม่แก้ field mapping. ในบทสนทนา 3 รอบที่ใช้คำตอบ assistant จริง: first 160/160 และ switch 160/160 ผ่าน แต่ followup 40/160 เท่านั้น

None 120 เคสจาก followup ทั้งหมดเป็นอังกฤษ: guard ประวัติไม่รับ And เพียงอย่างเดียว เมื่อไม่มี field keyword หรือ it/this/that แล้วไม่ได้เลือก prior record. question สั้น+มี history อย่างเดียวไม่พอ จึงไป infer kind แล้วกลับ None. นี่เป็นสองปัญหาต่อกัน: field mapping ไม่รู้สำนวน → history guard ไม่ให้ยืม record → common route ไม่ตอบ

context_query สแกน user turns ล่าสุด 6 messages ไม่อ่าน assistant choices เป็น typed pending state. assistant history ที่เพิ่มช่วยให้เห็นบริบท แต่ไม่ได้แปลว่าจะถูกใช้ resolver. การถามกว้าง→แสดงตัวเลือก→เลือกด้วยชื่ออย่างเดียวต้องมี pending intent/selection axis ที่ชัด ไม่ควรยืมคำแบบไม่รู้ชนิดรายการ

## 10. R08 — คะแนน fuzzy จริงเป็นอะไร

Exact ไม่ได้ใช้โมเดลคะแนนความหมาย. ถ้า exact ไม่พบจึงเปรียบเทียบ alias กับช่วงข้อความยาว alias−1/alias/alias+1, ต้องมีชุดตัวเลขเท่ากัน แล้ว SequenceMatcher.ratio >=0.88. เลือกได้เมื่ออันดับแรกทิ้งอันดับสอง >=0.06; ถ้า margin ไม่พอคืนไม่มีชื่อแทนเลือกสุ่ม

คะแนนคือความคล้ายตัวอักษรของ span ไม่ใช่ความมั่นใจตอบถูกหรือความเข้าใจเจตนา. การทำคะแนนชื่อดีขึ้นไม่แก้ required_proofs/session_minutes/players_max หาก field matcher ยังไม่รู้. Replay 11 typo misses ใช้ matcher/ratio ตัวเดิมและเก็บ top 5, alias/span, intended-record score, threshold และ margin ในภาคผนวก

## 11. R09/R17 — ทำไมพิมพ์ผิดกลับผ่าน แต่พิมพ์ถูกไม่ผ่าน

26 คู่ clean_fail/repeat_pass ไม่ใช่หลักฐานว่า typo ช่วยความเข้าใจ. Exact+field ว่างเข้า clarification; bounded_fuzzy+field ว่างถูกยกเว้น clarification แล้วตอบ publish_core/default fields. ตัวอย่าง sessionn ได้ name/resource/platform/session/occupancy จึงมี 60 นาทีอยู่ด้วย. Content scorer ผ่าน แต่ requested=[] และ all_fields=false ยืนยันว่า intent ยังไม่ถูกเลือก

อีก 94 คู่ clean_fail/repeat_fail ยังแยกสาเหตุ typo ไม่ได้ เพราะคำปกติก็ผิด. 38 คู่ผ่านทั้งสอง. 2 คู่ clean_pass/repeat_fail เป็นการตกหลังพิมพ์ซ้ำที่ชัดเจนในเกณฑ์นี้. อย่าใช้ 96 typo failures ทั้งหมดเป็นจำนวนบั๊กสะกด

## 12. R10 — ชื่อรายการทำให้จับหัวข้อผิดได้อย่างไร

q ทั้งประโยคเข้า matcher. ชื่อที่มี policy/procedure/controls หรือข้อกำหนด/ขั้นตอน/ปุ่มจึงเข้า field mapping ก่อนเข้าใจคำถามจริง. Alias ถูกตัดออกตอน remainder guard หลังเลือก fields แล้ว จึงตัดช้าไป. Detector แยก term matches ที่อยู่ใน span ชื่อ เพื่อบอกว่าคำนี้มาจาก title หรือส่วนคำถาม

คำในชื่ออาจทำให้ผ่านโดยบังเอิญด้วย เช่นชื่อ policy ทำให้ได้ details แล้ว policy bundle ตอบ gold ที่ขอครบ. ไม่ใช่ทุก match ใน entity เป็นบั๊ก ต้องดูว่ามันตรงเจตนาผู้ถามหรือทำให้เกิด field เกิน/ขาด

## 13. R13 — คำว่า “ครบไหม” ทำให้ตอบทั้งหมด

all_query ใช้ “ครบ” แบบ substring ไม่มีการแยกถาม completeness จากขอทั้งรายการ. คำอ่านกติกาให้ครบอาจควรขอ text เต็ม แต่ไม่จำเป็นต้องทุก field; “ข้อมูลครบไหม” ควรตอบ completeness. ใน dataset มี passed non-all cases ที่ broad=True ด้วยเหตุนี้ เก็บแยกใน PASSES_NEED_REVIEW.md

helper probe ยังยืนยัน all_query('football'/'small'/'install')=True เพราะ `all\\b` ไม่กันขอบต้น และ all_query('ไม่ต้องตอบทั้งหมด')=True เพราะไม่อ่าน negation. เป็นข้อจำกัดจริงของ helper แต่ไม่เอาเคส probe เหล่านี้ไปเพิ่มยอด 2403 เดิม และไม่อ้างว่า live เว็บส่งคำตอบไหนจาก probe นี้โดยไม่ได้วัด

## 14. R18 — source unknown กับ unsupported field ต้องต่างกัน

unknown ที่อยู่ใน record พร้อม note หมายถึงเจ้าของ/fixture ยังไม่ยืนยันข้อมูลจริง; known-empty/0/false ก็เป็นข้อมูลที่ยืนยันแล้ว ห้ามตีเป็น unknown. แต่ obligation record_id=None จาก requested ที่ตอบไม่ได้เป็นผล resolver ไม่ใช่ field factual unknown. การแสดงเหมือนกันทำให้ผู้ใช้คิดว่าข้อมูลไม่มีและย้อนแก้ DB ผิดจุด

ข้อเสนอเชิงวิเคราะห์: แยก unavailable_fact, unsupported_request_field, unresolved_intent, missing_relation, needs_clarification และ current-time validity. อย่าเพิ่มค่า guessed 0/false หรือบอกเจ้าของกรอกใหม่เพียงเพราะ matcher เลือก key ผิด

## 15. R15 — ทำไมตัวแก้ภาษาเดิมไม่ช่วยทุกคำถามจาก format ใหม่

engine เรียก common และ return non-None ก่อน explicit_request_focus และ preprocess_input เดิม ซึ่งมี keyboard-neighbour, transposition, multi-error phrase, intent recovery, normalize เเ→แ และ competition name recovery. Owner preview เรียก CommonAnswerer โดยตรง ไม่มี planner/preprocess จาก route เดิมเลย

คำตอบ common แบบ clarification/unknown ถือเป็น non-None จึงหยุดก่อนใช้เส้นทางเดิม. การเพิ่มความสามารถ typo/intent ที่ legacy route จึงไม่อัตโนมัติขยายมาถึง common. request_plan ที่ engine รับถูกใช้ส่วนถัดไป แต่ common ใช้เพียง raw question/recent_history. ข้อสรุปนี้ยืนยันด้วยลำดับโค้ด; ยังไม่ถือว่าทุก miss ในชุดนี้เกิดจาก preprocess bypass เพราะไม่ได้เปรียบเทียบเปิด preprocess ทุกเคส

## 16. R11/R12 — ทำไมมี LLM แต่ยังไม่ตอบถูก

48 tests เป็น CommonAnswerer + bounded schema planner, ไม่ใช่ให้ LLM แต่ง fact จากความจำ. 21 เคสไม่มี planner attempt เพราะ gate ไม่เข้า, 27 เรียกได้, 2 plans accepted, 25 rejected platform. การมี requested field ผิดอยู่แล้วทำให้ไม่เรียก LLM มาซ่อม เช่น resource กี่คน→players_min.

JSON schema ให้ requested_fields เป็น string ใดก็ได้และ platform เป็น string/null แต่ validator ตรวจ allowed keys/platforms ทีหลัง. Input prompt มี record_ids แต่ไม่ได้ส่ง allowed platform values/อธิบาย null แบบชัดเจน. Raw แสดง platform เป็น record ID/unknown/service; การปฏิเสธถูกตามข้อกำหนดปัจจุบัน การปล่อยผ่าน string ผิดเพื่อเพิ่มคะแนนจะทำให้ scope ผิด

สาเหตุของ emitted value ที่ยืนยันได้คือผลลัพธ์ผิดข้อกำหนด; การเชื่อมโยงว่า prompt/schema ไม่ constrain เพียงพอเป็น inference รองรับจากโค้ด ไม่ควรฟันธงว่าโมเดลเล็กหรือ translation เป็นตัวการหลักจาก 48 sample. ไม่มี health timeout/failure ใน 27 requests นี้

## 17. R14 — success, confidence และ validation หมายถึงอะไรจริง

HTTP 200=server ส่งผลได้; LLM health success=เรียก/decode ได้; checked_plan non-None=proposal อยู่ใน schema scope; obligation coverage=มีทุกหัวข้อที่คาด; answer correct=ต้องตรงคำถามและ fact. ทั้งห้าไม่ใช่ตัวเดียวกัน

planner เรียก record_llm_success หลัง checked_plan แม้ clean=None, จึง health 27 success แต่ accepted 2. finish ตั้ง trace confidence/route confidence/result confidence=1.0 และ ValidationResult(True) คงที่ หลังพิมพ์ typed source. ตัวเลข 1.0 ไม่ใช่การคำนวณคะแนน semantic ของคำถาม ไม่มี scoring rank ระหว่าง candidate answers ในขั้นนี้

## 18. ภาษาไทยและอังกฤษ — อะไรที่หลักฐานบอกจริง

ไทยผ่าน 1141/2528 (45.13%) อังกฤษ 1512/2528 (59.81%). ข้อมูลภาษาอังกฤษถูกแปลโดย agent แล้ว renderer เลือก en field; pass ตรวจว่าค่าที่คาดอยู่ในคำตอบ ไม่ใช่ตรวจการแปลเทียบต้นฉบับเชิงภาษาศาสตร์

สำนวนอังกฤษบางแบบบังเอิญตรง canonical keys เช่น specifications/rulebook release และบางแบบโดน What is→summary. ไทย “อยู่ตรงไหน” ไม่ตรง literal “อยู่ไหน”, หลักฐาน/เอกสารไม่ได้อยู่ TERMS ฯลฯ. ทั้งหมดเป็นผลกติกาปัจจุบันร่วมกับรูปแบบชุดทดสอบ ไม่ได้พิสูจน์ว่าภาษาไทยโดยธรรมชาติยากกว่าเสมอ. อังกฤษมี history-gate miss 120 ที่ไทย prefix แล้ว ผ่านได้ จึงมี bug เฉพาะอังกฤษด้วย

casefold ของ meaning_th ยังไม่สมมาตรกับ q: labels API/PC/ISO/VR/WordPress ซึ่งมีคำอังกฤษใน label ไทยหลุด. มีตัวอย่าง contract errors ชุดเก่าพร้อม source linkในส่วนเสริม ไม่ใช้ยอดเก่ารวมกับชุดใหม่

## 19. Renderer และข้อมูลที่มี citation แต่ยังไม่เหมาะกับผู้ใช้

title() ไม่อ่าน value ของ contact ทำให้ public_contact_id/contact_id บาง field แสดงรหัสภายใน. Enum เช่น modified_hours/in_service/conditional และเวลา/หน่วยบางค่าแสดงแบบเทคนิค. หลาย citations บอกว่า fact มาจาก approved synthetic source ไม่ใช่ยืนยันว่าจะตอบตรงคำถามหรือเป็นบริการ PSU จริง

kind rate/rental/policy bundle แนบเงื่อนไขเพื่อไม่ตัดบริบทเป็นข้อดี แต่คำตอบอาจยาวหรือรวมข้อมูลที่ผู้ใช้ไม่ได้ถาม. competition ทุกคำถามแนบ child rules ทั้งหมด ส่วน join game_mode ถูก trigger โดย players_min ไม่ใช่ทุก slot players_max ที่อาจถูกเลือกด้วย planner. ข้อจำกัด join ที่ยังไม่ถูกกระตุ้นใน dataset ให้ระบุเป็น code risk ไม่แปลงเป็น count ของเคสผิดโดยเดา

## 20. Scoring ทำอะไร และทำอะไรไม่ได้

ตรวจ record-field obligation, status, expected leaf content, evidence source/locator สำหรับ field known, unknown/not_applicable wording. ไม่ตรวจ style, translation ทุกคำ, implication/negation, extra unrelated assertions ทุกตัว, semantic plan ครอบคลุม gold ทุกช่อง, public-contact dereference ที่ผู้ใช้ใช้งานได้

expected_fields/question ถูกเขียนก่อนรันโดยไม่ส่ง oracle ให้ระบบ แต่ expected formatting ของ reference ใช้ title() จาก implementation เดียวกับ renderer จึงมีโอกาสยอมรับ fallback internal ID ทั้งสองฝั่ง เป็นส่วนที่ test ยังไม่อิสระพอและควรแยก specification ของ public reference display ออกก่อนรับรอง UX. การมี ground truth field ไม่ได้ทำให้ทุกมิติของ scorer เป็น independent human ground truth

26 passes ที่ unresolved intent แสดงช่องโหว่ของการมีข้อความถูกเพียงอย่างเดียว. อีกกลุ่มผ่านจาก domain bundles ไม่ควรเรียกว่า fail ทันที แต่ควรแยก metric intentional slot resolution กับ required content. Passed extra unknown messages ต้องตรวจว่าทำให้ผู้ใช้เข้าใจผิดหรือไม่ แม้ gold อยู่ในคำตอบครบ

## 21. ประสิทธิภาพและสิ่งที่ยังไม่วัด

named() ทำ fuzzy scan ก่อนลอง history แม้คำถามสั้นไม่มีชื่อ; ทุก alias ใช้ sliding spans 3 ขนาดและ SequenceMatcher พร้อมตัวเลข guard. ชื่อมากขึ้นทำให้ต้นทุนเพิ่มเป็นหลายส่วนร่วมกัน การขอ history ก่อน fuzzy เฉพาะเมื่อ followup ชัดเจนเป็นแนวทางที่ต้องรักษา entity-switch guard ไม่ใช่ข้าม lookup ทุกครั้ง

content test ใช้ immutable snapshot และ test-only pure name cache เพื่อทำงานครบ ไม่ใช่ระบบ production cache. elapsed ใน log รวมแย่ง CPU ของ workers และบาง cache hit จึงไม่ใช้ประมาณเวลาเว็บ/จำนวนผู้ใช้. API/pipeline ที่อ่าน DB จริงช่วยยืนยันผลส่วนที่ทวน แต่ไม่เป็น load benchmark รอบนี้

### 21.1 จุดที่ format กลางเป็น data-driven แล้ว และจุดที่ยังไม่ใช่

registry/templates/schema/forms/validation/default rendering รับ fields จาก catalog ได้จริง. แต่ field intent ยังใช้ TERMS 13 กลุ่ม, generic kind inference ยังใช้ KIND_TERMS ที่ไม่ครบทุก24kind, joins ยังเขียน if/else เช่นราคาเดินจาก service/audience/zone และ game_mode joinเริ่มจาก players_min. text_index ที่เก็บใน release ไม่ได้กลายเป็น semantic search อัตโนมัติใน CommonAnswerer นี้

จึงเพิ่มข้อมูลใหม่ที่ schema ยอมรับได้แล้ว ไม่ได้หมายความว่าจะมีวิธีแปลงคำถามใหม่ทุกสำนวนเป็นคำสั่งอ่าน field/relation ทันที. คำถามชื่อเกม+ราคาอาจต้องเดิน game→game_service→service→rate ซึ่งยังไม่ใช่ generic graph query. ความเสี่ยง relationนี้อ่านได้จาก code แต่ไม่เพิ่มจำนวนเคสผิด เพราะชุดgameถามวิธีเล่น/summary ไม่ได้ถามราคาเกมทุกเคส

อีกด้าน policy.conditions_all/schedule/closure ถูกแสดงเป็นข้อมูล แต่ไม่ใช่ execution engine ของเงื่อนไขผู้ใช้/ปฏิทินหรือสถานะสดทุกแบบ. การขอรายละเอียดกฎกับการถามว่าตนเองเข้าเงื่อนไขหรือไม่เป็นคนละงาน อย่าใช้ field rendering ไปยืนยันสิทธิ์หรือสถานะสดโดยยังไม่ได้ resolve context

Owner preview ไม่มี planner; เว็บแชท server ใช้ LOCAL_LLM_ASSIST_ENABLED ซึ่ง code default=True และส่ง flagไป pipeline แต่ยังต้องผ่าน common planner gate. main5056/API/pipeline224 tests ปิด LLMตามscope ส่วน 48 sampleเปิดจริง. ไม่ควรกล่าวว่าทุก requestบนเว็บ production ปิด LLMเพียงเพราะ testsชุดหลักปิด และรอบนี้ไม่ได้อ่านค่า envของprocessเว็บจริง

Closure fixtures อยู่เดือนธันวาคม แต่ query ATเดือนตุลาคม; คำถามระบุ notice recordเพื่อถามข้อมูลในประกาศ ไม่ใช่ทดสอบว่าวันนี้ตามปฏิทินจริงปิดไหม. Some natural wordingอาจมีได้หลายinterpretations; goldเป็นเจตนาที่ผู้สร้างfixtureกำหนดไว้ ไม่ใช่ human-user intentที่ยืนยันทุกประโยค. จึงแยก manual reviewของความกำกวมจากบั๊กที่ recordถูก+fieldไม่มี/ผิดอย่างชัดเจน

## 22. สิ่งที่ไม่ควรสรุปจากการทดสอบ

- ข้อมูลทั้งหมดผิด/ต้องให้เจ้าของกรอกใหม่: ไม่รองรับ เพราะ all_fields 960 ผ่านและ 2272 failures เลือก record ถูก
- เพิ่ม alias หรือ keywordทุกประโยคแล้วจะจบ: ไม่รองรับ เพราะหลายมิติเหมือนกันต้องแยก kind/min/max และ field completeness
- ลด fuzzy threshold อย่างเดียว: ไม่แก้ field mapping และเสี่ยงเลือก wrong item
- เปิด LLM ทุกครั้งจะจบ: มี invalid platform และ gate/schema/slot issues ที่ต้องแก้ร่วมกัน
- อังกฤษผ่านแล้วจึงไม่มีปัญหา: ไม่รองรับ ทั้ง summary keyword และ And history misses พบจริง
- confidence=1 จึงตอบถูก: เป็นค่าคงที่ ไม่ได้ calibrate semantic quality
- 2403 เป็น hallucinations หรือ 2403 root causes: ไม่ใช่ ทั้ง clarification/incomplete/missing path และ pattern ซ้ำรวมอยู่

## 23. สารบัญสาเหตุและจำนวนเคสที่ detector ยืนยัน

รหัสสาเหตุเป็นหลายป้ายต่อเคส ต้องอ่าน primary chain ห้ามบวก counts เป็น unique failures. บางรหัสเป็น code risks/หลักฐานชุดก่อน ไม่ถูกใส่ tag ให้เคสใหม่โดยไม่มี evidence.

| รหัส | ประเด็น | เคสไม่ผ่านที่มี tag | เคสผ่านที่ต้องดูเพิ่ม | จุดโค้ด |
|---|---|---:|---:|---|
'''
    for code,(label,desc,loc) in CAUSES.items():
        count=metrics['cause_counts_nonexclusive'].get(code,{'failed':0,'passed_flagged':0})
        md+=f'| {code} | {label} | {count["failed"]} | {count["passed_flagged"]} | {loc} |\n'
    md+='\n## 24. ตัวอย่างสาเหตุทุกหมวดที่มีเคสไม่ผ่าน\n\nแต่ละตัวอย่างเป็นข้อมูล DEMO ใช้ค่าจาก record ใน release เดียวกับ test ข้อความควรตอบเรียบเรียงเพื่อให้เห็นสิ่งที่ขาด ไม่ถือว่า owner confirmed\n'
    for k in t.ORDER:
        rs=[r for r in FAIL if r['kind']==k];r=next((x for x in rs if x['style'] in {'multi_field','natural','paraphrase'}),rs[0] if rs else None)
        if not r:
            md+=f'\n### {k}\n\nชุดนี้ไม่มี required-content failures ในหมวดนี้ แต่ domain bundles/extra text/translation ยังเป็นอีกมิติ ไม่รับรองทุกคำถามใหม่\n';continue
        md+=f'\n### {k} / Case {r["id"]}\n\nถาม: {r["question"]}\n\nตอบจริง:'+block(r['answer'] or '[None]','text')+'\nควรตอบ:'+block(expected(r),'text')+'\nเหตุ:'+reason_text(r)+'\n\n'+out_link('ดูคำถาม/history/plan/evidence และการจับคำครบทุกเคส','FAILURES_BY_CATEGORY/'+k+'.md')+'\n'
    md+='\n## 25. เคสที่ได้ None: return line และคะแนนชื่อจริง\n\n'
    ns=metrics['none_route_summary'];md+=block(ns)
    for r in NONE.values():
        if 'fuzzy' in r:
            md+=f'\n### Case {r["id"]}: {r["question"]}\n\n'+block(r['fuzzy'])+'\nReturn at line '+str(r['observed']['return_line'])+' ด้วย ids='+str(r['observed']['locals']['ids'])+' และ kind='+str(r['observed']['locals']['kind'])+'\n'
    md+='\n## 26. ประเด็นในคะแนนผ่าน — นับแยกอย่างตรงไปตรงมา\n\n'
    md+=f'- เคสผ่านแต่มี extra unknown ของ field ที่ gold ไม่ได้ขอ: **{len(pass_unknown)}**\n- เคสผ่านที่ gold บาง field ไม่อยู่ใน requested แต่ถูกพิมพ์จาก defaults/bundles: **{len(bundle)}** (อาจเป็นการแนบบริบทที่เหมาะสม ไม่เหมารวมเป็นผิด)\n- เคสผ่านที่มี technical reference ID แสดงแทนชื่อปลายทาง: **{len({x["id"] for x in internal})}** (occurrences {len(internal)})\n- passed non-all ที่ broad=True หรือ fields ว่าง รวมที่ detector flag: **{len(weak)}**\n\n'
    if pass_unknown:
        r=pass_unknown[0];md+='ตัวอย่างผ่านแต่มีข้อความไม่ทราบเกินมา: '+r['question']+'\n'+block(r['answer'],'text')+block(r['extra_unknown'])
    md+='\n## 27. ลำดับแก้จาก evidence และเกณฑ์พิสูจน์ว่าแก้จริง\n\n| ลำดับ | เป้าหมาย | หลักการแก้ | เกณฑ์ทวน |\n|---|---|---|---|\n'
    md+='''| P0 | typed field intent | kind-aware semantic mapping, min/max/seat/proof/session/occupancy, กรอง global keywordที่ใช้ไม่ได้ | gold obligation ครบโดยไม่สร้าง unsupported unknown |
| P0 | multi-intent | แยก slots ทุกส่วน แล้ว validate coverage ก่อน finish | ทุก required field มี known/unknown/clarify ที่อธิบายได้; ไม่ตัด start/end หรือ building/floor |
| P0 | consistent fuzzy/clean | field resolution ใช้กฎเดียวกันหลัง entity exact/fuzzy; ไม่ตอบ defaultเพื่อกลบ field ว่าง | 26 clean-fail/typo-pass ต้องเลือก field ชัดหรือถามเจาะจง; ไม่ให้ accuracyเพิ่มจากตอบเผื่อ |
| P0 | English followup | typed pending state และ followup guard ที่รองรับภาษาจริง พร้อม entity switch precedence | 120 None followups และ 160 dialog followups; switchเดิม160ต้องยังถูก |
| P0 | planner contract | enum fields/platforms/null และ reasonของ reject; gate รองรับผิดkind/ขาดslot | 25 raw invalid platform ถูกป้องกัน; valid planต้องตอบครบ ไม่ bypassvalidator |
| P1 | pipeline integration | normalize/focus/common/typed dialogue ทำงานบนรูปคำถามร่วมกัน โดยรักษา rawและตัวเลข | typo, negation, scope/current record, legacyและcommonไม่ตอบคนละทิศ |
| P1 | broad/live predicates | แยก completeness/all/negation และ free-of-charge/free-slot | ครบไหมไม่ขยายทุกเรื่อง, football/smallไม่ broad, free priceไม่ live miss |
| P1 | quality & metrics | แยก source validity, entity score, accepted plan, slot coverage, content quality | ห้ามstatic1.0ถูกใช้เป็นคำรับรอง; healthsuccess/accepted/correctแยก |
| P2 | display/translation | human-readable enums/units/reference dereference และ language parity | ช่องทางติดต่อใช้ได้จริง, ไม่เผย technicalIDsแทนข้อมูล, อังกฤษreviewแยกจากcopy-value |

ไม่ควรแก้ค่าเจ้าของ/ราคา/เวลา/กฎจริงเพื่อทำให้ test ผ่าน. บั๊ก logic ข้างต้นใช้ fixture และหลักฐาน code แก้เองได้; ความหมายราคานโยบายที่ไม่มีหลักฐานจริงและความเหมาะสมคำแปลยังต้องมีผู้รับผิดชอบรับรองก่อน production

## 28. Coverage ของการวิเคราะห์และความปลอดภัยของหลักฐาน

รายงาน main นี้ + ภาคผนวกทุก failed case + weak-pass cases + LLM48 + conversation120 + annotationทุก5056 ครอบคลุมผลที่มี ไม่ได้ทิ้งเคสที่แก้ยาก. กรณี detector ยังไม่มีหลักฐาน root deeper จะระบุ observation/inference ไม่ใส่สาเหตุโมเดล/ข้อมูลขาดโดยเดา

ไฟล์ code hashes ใน AUDIT_METRICS ใช้ตรวจว่าอ่าน revisionใด. สร้างเฉพาะ deep_analysis_20261012; ไม่เขียนทับรายงาน/SQLite/log เดิม. Probe/replayเป็นการวินิจฉัย ไม่ใช่แก้พฤติกรรม production. Trace รอบแรกติดตามฟังก์ชันกว้างเกินไปจึงหยุดเฉพาะ processนั้น เก็บ partial trace/log และรัน V2ที่ติดตาม returnของCommonAnswerer.answer เท่านั้น; V2เป็นหลักฐาน131ที่ครบ

## 29. ไฟล์สำหรับตรวจทุกเคส

'''
    for p in ['CASE_ANNOTATIONS_5056.json','CASE_INDEX.csv','FAILURE_PATTERN_GROUPS.md','FAILURE_PATTERN_GROUPS.json','PASSES_NEED_REVIEW.md','PASSED_EXTRA_UNKNOWN_MESSAGES.json','PASSED_DEFAULT_BUNDLE_COVERAGE.json','PASSED_INTERNAL_REFERENCE_RENDERING.json','FIELD_OBLIGATION_COVERAGE.json','LLM_ALL_48_CASES.md','CONVERSATION_FAILURES_120.md','HTTP_PIPELINE_PAIRS_224.json','NONE_ROUTE_REPLAY_V2.jsonl','NONE_ROUTE_SUMMARY_V2.json','HELPER_PROBES.json','OLDER_CONTRACT_130_CASES.md','AUDIT_METRICS.json']:md+='- '+out_link(p,p)+'\n'
    md+='\n### ภาคผนวก 24 หมวด\n\n'
    for k in t.ORDER:md+='- '+out_link(t.CATALOG[k]['owner_form']+' — '+str(sum(r['kind']==k for r in FAIL))+' เคส','FAILURES_BY_CATEGORY/'+k+'.md')+'\n'
    md+='\n### ผลต้นฉบับและข้อมูล\n\n'
    for p in ['content_final/ANSWERS_AND_DECISIONS.jsonl','content_final/SUMMARY.json','QUESTIONS_EXPECTED.json','SCORING_REVIEW.json','MANIFEST.json','PRESERVATION_RECEIPT.json','LLM_SUMMARY.json','HTTP_ROUND2_SUMMARY.json','PIPELINE_SUMMARY.json','CONVERSATION_SUMMARY.json']:md+='- '+data_link(p,p)+'\n'
    put('DEEP_ROOT_CAUSE_ANALYSIS_TH.md',md)
    assert STORE.still_current(SNAP)
    print(json.dumps({'main_chars':len(md),'failed_cases_documented':len(FAIL),'annotations':len(annotations),'pattern_groups':len(groups),'weak_pass_cases':len(weak),'pass_extra_unknown':len(pass_unknown),'default_or_bundle':len(bundle),'internal_ref_cases':len({x['id'] for x in internal}),'llm_cases':len(LLM),'conversation_failed_turns':sum(not r['passed'] for r in CONV)},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
