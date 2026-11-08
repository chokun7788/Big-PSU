"""Executable R97 preconditions/oracles. Definitions only, no top-level tests."""
import copy,dataclasses,json,time,contextlib
from unittest.mock import patch
from scenario_support import bi,AT

QUESTIONS={
 'C01':('ขอราคาบุคคลภายนอกทั้งหมด','All prices for external visitors'),
 'C02':('PC','PC'),'C03':('ทั้งหมด','all'),
 'C04':('ขอถามหน่อย ขอคืนเงินได้ไหม','Please tell me: Can I get a refund?'),
 'C05':('วันอังคารตอนเย็นเปิดถึงกี่โมง','What time does the studio close on Tuesday?'),
 'C06':('VALORANT ใช้ผู้เล่นกี่คน','How many players does VALORANT use?'),
 'C07':('ROV ถ้าเกมหลุดทำยังไง','ROV what should I do if I disconnect?'),
 'C08':('ROV','ROV'),'C09':('กฎ CS2','CS2 competition rules'),
 'C10':('ขอเกมทั้งหมด','List all games'),
 'C11':('มีเกมใน PS5 กับ Switch อะไรบ้าง','What games are offered on PS5 and Switch?'),
 'C12':('ราคาและวิธีจอง PC สำหรับบุคคลภายนอก','PC price for external visitors and how do I book PC?'),
 'C13':('มี 100 บาท เล่น PC ได้นานแค่ไหน สำหรับบุคคลภายนอก','With a 100 THB budget, how long can external visitors play PC?'),
 'C14':('PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก','PC price for 2 hours and VR price for 30 minutes for external visitors'),
 'C15':('เหมา PC เต็มวันสำหรับบุคคลภายนอกราคาเท่าไร','PC full-day rental price for external visitors'),
 'C16':('วันนี้เปิดไหม','Are you open today?'),'C17':('วันนี้เปิดไหม','Are you open today?'),
 'C18':('ตอนบ่ายสาม PC ว่างไหม','Is PC available at 15:00?'),
 'C19':('PC ว่างไหม แล้วจองยังไง','Is PC available now and how do I book PC?'),
 'C20':('เกมเอทดลอง คือเกมอะไร และ เกมบีทดลอง คือเกมอะไร','What is Game A Fixture and what is Game B Fixture?'),
 'C21':('กฎ ROV ก่อนกับหลัง First Blood ต่างกันยังไง','ROV competition rules before and after First Blood'),
 'C22':('ไม่ใช่บุคลากร PSU ใช้ราคา PC ไหน','I am not PSU staff. Which PC price applies?'),
 'C23':('ราคา PC สำหรับบุคคลภายนอก','PC price for external visitors'),
 'C24':('PC','PC'),'C25':('PC','PC'),'C26':('PC','PC'),
 'C27':('มีอุปกรณ์ไหม','Is there any equipment?'),'C28':('มีอุปกรณ์ไหม','Is there any equipment?'),
 'C29':('เกมเอทดลอง เล่นได้ที่ไหน','Where can I play Game A Fixture?'),
 'C30':('อธิบายกฎ ROV เรื่องเกมหลุดเป็นอังกฤษ','Explain ROV competition disconnection rules in English'),
 'C31':('ช่วยเล่าภาพความคิดของ เกมเอทดลอง ให้เข้าใจที','I would love a guided sense of the idea behind Game A Fixture'),
 'C32':('ช่วยเล่าภาพความคิดของ เกมเอทดลอง ให้เข้าใจที','I would love a guided sense of the idea behind Game A Fixture'),
 'C33':('เกมเพิ่มใหม่ออโรร่า เล่นยังไง','How do I play Aurora Newly Added Fixture?'),
 'C34':('ใช้สูตรโปรโมชันแบบใหม่คิดราคา PC ให้ที','Apply a new unsupported promotion formula to the PC price'),
 'C35':('VALORANT ใช้ผู้เล่นกี่คน','How many players does VALORANT use?'),
 'C36':('ไม่ใช่ ขอวิธีจอง PC','No, how do I book PC instead?'),
 'C37':('ศูนย์อยู่ที่ไหน แล้วราคาเท่าไร','Where is the studio and what is the price?')}

def variants(q,lang):
    if lang=='th':return [q,'ขอถามหน่อย '+q+' ครับ',q.replace('กฎ','กฏ').replace('ราคา','ราาคา')+'?',q+' ตอบสั้น ๆ']
    return [q,'Could you help me with this: '+q,q.replace('What','Waht').replace('price','prcie')+'?',q+'. Please be brief.']
def artifact(r):return (r.decision_artifact or {}) if r else {}
def statuses(r):return {x.get('status') for x in artifact(r).get('need_results',[])}
def has(r,token):return r is not None and token.lower() in r.answer.lower()
def hit(r,rid,field=None):return r is not None and any(h.get('record_id')==rid and (field is None or h.get('field')==field) for h in r.hits)

def execute(cid,f,q,locale):
    """Returns the actual answer and source/precondition-specific invariants."""
    checks=[];history=None;contexts=contextlib.ExitStack();store=None
    lang='th' if locale=='th' else 'en'
    def check(label,ok):checks.append({'assertion':label,'passed':bool(ok)})
    def pending():
        firstq='ราคาสำหรับบุคคลภายนอก 2 ชั่วโมง' if lang=='th' else 'Prices for external visitors for 2 hours'
        first=f.ask(firstq,locale);check('precondition targeted pending exists',first is not None and artifact(first).get('response_type')=='clarification')
        return f.history(firstq,first) if first else []
    def rate_unknown():
        r=f.store.get('fx_rate')['record'];r['validity']={'state':'unknown','effective_from':None,'effective_until':None};f.save(r)
    if cid in {'C02','C03','C24','C25','C26','C36'}:history=pending()
    if cid in {'C12','C13'}:rate_unknown()
    if cid=='C09':
        # Only the other game's rule exists. The first candidates may contain
        # that rule, but no CS2 source is permitted to be fabricated.
        check('precondition only ROV rule exists',f.store.get('fx_rule')['record']['fields']['competition_id']['value']=='fx_event')
    if cid=='C10':
        for i in range(20):
            gid='fx_extra_'+str(i);f.new('game',gid,{'title':bi('เกมเพิ่มเติม '+str(i),'Extra Fixture '+str(i)),'summary':bi('ภาพรวมเพิ่มเติม','Extra overview')})
            f.new('game_service','fx_offer_extra_'+str(i),{'game_id':gid,'service_id':'fx_pc','offered':True})
    if cid=='C11':
        for platform,rid in [('PS5','fx_ps5'),('Switch','fx_switch')]:
            f.new('service',rid,{'name':bi(platform,platform),'platform':platform,'resource_ids':['fx_resource'],'session_minutes':60,'occupancy_minutes':60})
            f.new('game_service','fx_offer_'+rid,{'game_id':'fx_a','service_id':rid,'offered':True})
    if cid=='C17':
        r=f.store.get('fx_schedule')['record'];r['fields']['open_periods']={'status':'unknown','value':None,'evidence_refs':[],'note':'Physical opening not confirmed'}
        r['fields']['bookable_periods']['value']=[];f.save(r)
    if cid=='C18':
        snap=f.live();contexts.enter_context(patch('app.booking.live_status.get_live_booking_status',return_value=snap))
    if cid=='C21':
        f.new('competition_rule','fx_rule_after',{'competition_id':'fx_event','section_number':'2','facet':'in_match_operations','heading':bi('หลัง First Blood','After First Blood'),
          'text':bi('หลัง First Blood ห้ามเริ่มใหม่ ยกเว้นกรรมการอนุญาต AFTER_EXCEPTION','After First Blood do not restart unless the referee permits it. AFTER_EXCEPTION'),'depends_on_ids':[],'completeness':'complete'})
        f.edit('fx_rule',{'text':bi('ก่อน First Blood หยุดได้ BEFORE_FACT อ่านข้อ 2 ด้วย','Before First Blood pause is allowed BEFORE_FACT; also read clause 2.'),'depends_on_ids':['fx_rule_after']})
    if cid=='C23':
        r=f.new('faq','fx_conflict',{'question':bi('ราคา PC ภายนอก','External PC price'),'answer':bi('ราคา 200 บาท','Price 200 THB'),'topic':'price'})
        r['claim_bindings']=[f.binding('current_rate','fx_pc','fx_conflict','answer',actors=['fx_external'],services=['fx_pc'],unit='per_hour',duration=60,projection='currency_literal',path='/en')]
        f.save(r)
    if cid=='C24':
        f.pub([x['record_id'] for x in f.store.list_heads()],'all-before-edit')
        f.edit('fx_rate',{'amount_minor':15100});f.pub(['fx_rate'],'new-price');
        from app.knowledge.common.snapshot_provider import PinnedSnapshotView
        store=f.store
    if cid=='C25':f.store.withdraw('fx_rate',actor='isolated')
    if cid=='C26':f.new('contact','fx_contact',{'purpose':bi('ติดต่อทดลอง','Fixture contact'),'channel':'email','value':'test@example.invalid'})
    if cid=='C27':
        r=f.new('faq','fx_inventory',{'question':bi('รายการอุปกรณ์ครบ','Complete equipment inventory'),'answer':bi('ยืนยันรายการอุปกรณ์ว่างในศูนย์ทดลอง','Confirmed empty fixture studio equipment inventory'),'topic':'equipment','related_ids':[]})
        r['claim_bindings']=[f.binding('equipment_inventory','fx_center','fx_inventory','related_ids')];f.save(r)
    if cid=='C29':
        f.store.withdraw('fx_offer_fx_a',actor='isolated')
    if cid=='C33':f.new('game','fx_new_game',{'title':bi('เกมเพิ่มใหม่ออโรร่า','Aurora Newly Added Fixture'),'how_to_play':bi('เดินตามแสง NEW_PLAY_FACT','Follow the lights NEW_PLAY_FACT')})
    if cid=='C34':
        from app.knowledge.common.registry import schema_errors
        bad=f.store.get('fx_rate')['record'];bad['fields']['calculation_rule']['value']='arbitrary_model_formula'
        check('unsupported operator rejected by schema',bool(schema_errors(bad)))
    if cid=='C35':
        # Invalid staged data is isolated from the store; publication has its
        # own guard. This simulates a damaged incoming relation for runtime.
        from app.knowledge.common.snapshot_provider import DraftSnapshotView
        snap=DraftSnapshotView(f.store).snapshot();snap['release']['records']['fx_mode']['fields']['platform']['value']='UNKNOWN_PLATFORM'
        class Overlay(DraftSnapshotView):
            def snapshot(self):return snap
        store=Overlay(f.store)
    if cid=='C08':
        firstq='ถ้าเกมหลุดตอนแข่งขันทำยังไง' if lang=='th' else 'What should I do if I disconnect in a competition?'
        first=f.ask(firstq,locale);history=f.history(firstq,first) if first else []
        check('precondition game selection pending',first is not None and artifact(first).get('response_type')=='clarification')
    if cid=='C31':
        class InvalidBody:
            def __enter__(self):return self
            def __exit__(self,*a):pass
            def read(self,*a):return b'{"response":"not valid plan JSON"}'
        contexts.enter_context(patch('urllib.request.urlopen',return_value=InvalidBody()))
        contexts.enter_context(patch('app.pipeline.llm_health.record_llm_failure',return_value=None))
    if cid=='C32':
        from app.pipeline.request_deadline import request_deadline
        contexts.enter_context(request_deadline(.001));time.sleep(.003)
    with contexts:r=f.ask(q,locale,history,store=store)
    a=artifact(r);need_states=statuses(r)
    check('answer exists',r is not None)
    if r is None:return r,checks
    check('runtime validation',r.validation.ok)
    if cid=='C01':
        receipt=a.get('query_plan',{}).get('set_receipt',{})
        check('exhaustive two service price scope',receipt.get('total_members')==2 and receipt.get('returned_members_count')==2)
        check('external audience preserved',not hit(r,'fx_staff_rate','amount_minor'))
    elif cid in {'C02','C03','C24','C26'}:
        check('price task preserved',any(n['task']=='price' for n in a.get('request_plan',{}).get('needs',[])))
        check('correct current external value',has(r,'302') if cid=='C24' else has(r,'200') or has(r,'100'))
        check('staff price not selected',not hit(r,'fx_staff_rate','amount_minor'))
    elif cid=='C04':check('supported refund wrapper',has(r,'REFUND_FACT'))
    elif cid=='C05':check('closing source selected',hit(r,'fx_schedule','open_periods') and has(r,'18:00'))
    elif cid=='C06':check('linked mode count',hit(r,'fx_mode','players_max') and any(n.get('status')=='supported' for n in a.get('need_results',[])))
    elif cid=='C07':check('material context question',a.get('response_type')=='clarification' and not has(r,'RULE_EXCEPTION'))
    elif cid=='C08':check('disconnect scope inherited',has(r,'RULE_EXCEPTION') and hit(r,'fx_rule'))
    elif cid=='C09':check('wrong game rule rejected',not hit(r,'fx_rule') and not has(r,'RULE_EXCEPTION'))
    elif cid=='C10':check('full offering catalog not top K',all(has(r,'Extra Fixture '+str(i)) or has(r,'เกมเพิ่มเติม '+str(i)) for i in range(20)))
    elif cid=='C11':check('offering scopes read',not has(r,'GAME_A') and (has(r,'Game A Fixture') or has(r,'เกมเอทดลอง')) and hit(r,'fx_offer_fx_ps5') and hit(r,'fx_offer_fx_switch'))
    elif cid=='C12':check('independent booking survives price gap',has(r,'BOOK_STEPS') and not has(r,'100.00'))
    elif cid=='C13':check('no derived hours from unknown current price',not any(p.get('predicate')=='budget' and p.get('status')=='supported' for p in a.get('claim_packets',[])) and a.get('response_type')!='answer')
    elif cid=='C14':
        calculations=a.get('query_plan',{}).get('clauses',[])
        check('two bound tuples retained',len(a.get('request_plan',{}).get('needs',[]))==2)
        check('amounts reflect PC2h and VR30m',has(r,'200') and has(r,'60'))
    elif cid=='C15':check('rental source not hourly extrapolation',hit(r,'fx_rental','amount_minor') and has(r,'777'))
    elif cid=='C16':check('date and confirmed opening',a.get('query_plan',{}).get('day_status')=='open' and ('2026' in r.answer or '2569' in r.answer))
    elif cid=='C17':check('bookability does not assert closed',a.get('query_plan',{}).get('day_status')=='unconfirmed' and not r.hits)
    elif cid=='C18':check('explicit future slot observation',a.get('live_booking',{}).get('status')=='confirmed' and has(r,'15:00'))
    elif cid=='C19':check('live gap keeps independent booking',has(r,'BOOK_STEPS') and any(n.get('status')=='live_unavailable' for n in a.get('need_results',[])))
    elif cid=='C20':check('both same task subjects answered',has(r,'GAME_A') and has(r,'GAME_B') and len(a.get('need_results',[]))==2)
    elif cid=='C21':check('before/after linked clauses preserved',has(r,'BEFORE_FACT') and has(r,'AFTER_EXCEPTION'))
    elif cid=='C22':check('negated audience not quoted',not hit(r,'fx_staff_rate','amount_minor'))
    elif cid=='C23':check('cross-source conflict detected','conflict' in need_states and bool(a.get('claim_conflicts')) and not r.hits)
    elif cid=='C25':check('withdrawn price not resurrected',not hit(r,'fx_rate') and not has(r,'100.00'))
    elif cid=='C27':check('known empty exact scope',a.get('scope_receipt',{}).get('total_members')==0 and 'supported' in need_states)
    elif cid=='C28':check('unknown not asserted empty',not (a.get('scope_receipt',{}).get('completeness')=='explicit_source_declared' and a.get('scope_receipt',{}).get('total_members')==0))
    elif cid=='C29':check('platform support not studio offering',not hit(r,'fx_offer_fx_a') and not any(p.get('predicate')=='offered_game_location' and p.get('status')=='supported' for p in a.get('claim_packets',[])))
    elif cid=='C30':check('exception survives English output',has(r,'RULE_EXCEPTION') and has(r,'unless'))
    elif cid=='C31':check('invalid model JSON is not missing source','temporary_failure' in need_states or a.get('response_type')=='unavailable')
    elif cid=='C32':check('shared deadline not reset',a.get('request_context',{}).get('budget',{}).get('global_timeout_sec',99)<=.001 and a.get('request_context',{}).get('semantic_attempts',0)<=1)
    elif cid=='C33':check('data-only new game how-to',has(r,'NEW_PLAY_FACT') and hit(r,'fx_new_game','how_to_play'))
    elif cid=='C34':check('unsupported promotion not computed',a.get('response_type') not in {'answer','list'} or not any(x.get('derived') for x in a.get('claim_packets',[])))
    elif cid=='C35':check('broken mode relation does not assert count','broken_relation' in need_states and not r.hits)
    elif cid=='C36':check('explicit task reset',has(r,'BOOK_STEPS') and not hit(r,'fx_rate','amount_minor'))
    elif cid=='C37':check('supported address and scoped price question',has(r,'ADDRESS_FACT') and len(a.get('need_results',[]))==2 and 'needs_user_slot' in need_states)
    return r,checks
