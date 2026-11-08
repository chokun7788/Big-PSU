"""Author new questions from content needs, freeze before evaluating.

This is a synthetic development/reserved set, not an independently human blind
test. Reserved wording is not evaluated until fixes based on development finish.
"""
import json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
# kind: fields, dev TH/EN, reserved TH/EN; no fixture-specific question aliases.
Q={
'center':(['building','floor'],'ต้องขึ้นไปชั้นไหนของตึกอะไร','Which floor of which building should I head to?','ไปตึกไหนแล้วขึ้นชั้นไหนถึงจะเจอศูนย์','What building do I enter, and what floor do I go to?'),
'zone':(['room_seats'],'ที่ตรงนี้นั่งได้รวมกี่ที่','How many chairs can visitors sit on here?','บริเวณนี้มีเก้าอี้ทั้งหมดกี่ที่นั่ง','How many seats are provided in this area altogether?'),
'equipment_model':(['specifications'],'บอกคุณสมบัติของเครื่องแต่ละอย่างที','Could you break down the hardware specifications?','รายละเอียดฮาร์ดแวร์รุ่นนี้เป็นอย่างไร','What hardware does this model come with?'),
'resource':(['capacity_persons'],'เครื่องเดียวให้คนเล่นได้พร้อมกันสูงสุดเท่าไร','What is the simultaneous user limit for a single station?','ใช้เครื่องนี้พร้อมกันได้มากที่สุดกี่คน','How many people may use one station at the same time?'),
'service':(['session_minutes','occupancy_minutes'],'เวลาเล่นจริงกับเวลาที่ล็อกเครื่องเอาไว้เท่ากันไหม กี่นาที','How does actual play time compare with the time reserved on the machine?','รอบนี้เล่นกี่นาที แล้วระบบกันเครื่องไว้กี่นาที','How long is playtime, and how long is the device blocked for the booking?'),
'game':(['how_to_play'],'เริ่มเล่นแล้วต้องทำอะไรให้ผ่านเกมนี้','What should a beginner do to complete this game?','เป้าหมายเวลาเล่นคืออะไร ต้องทำแบบไหน','Explain the objective and the basic gameplay loop.'),
'audience':(['required_proofs'],'จะพิสูจน์สิทธิ์กลุ่มนี้ต้องยื่นอะไร','What should I present to verify my eligibility?','ต้องเอาอะไรมาแสดงว่าเป็นคนในกลุ่มนี้','Which evidence proves that I belong to this visitor group?'),
'contact':(['value','office_hours'],'จะทักผู้ดูแลไปทางไหนและเขาตอบตอนกี่โมง','How do I reach support, and when do they reply?','ขอช่องทางช่วยเหลือพร้อมช่วงเวลาที่ติดต่อได้','Give me the support channel and its response hours.'),
'procedure':(['steps','required_documents'],'ช่วยไล่สิ่งที่ต้องทำและของที่ต้องเตรียมที','Guide me through what to do and which paperwork to prepare.','ขอวิธีดำเนินการทีละขั้นและหลักฐานที่ต้องใช้','Outline the process and the documents I should bring.'),
'policy':(['decision','exceptions'],'ข้อนี้ทำได้หรือห้าม แล้วกรณียกเว้นมีอะไร','Is this permitted, and when is an exception made?','ทำแบบนี้ได้ไหม มีกรณีไหนที่ยกเว้นให้','Can I do this, and are there exceptions to the restriction?'),
'facility':(['location','accessibility'],'จุดนี้อยู่แถวไหน รถเข็นเข้าได้ยังไง','Where do I find it, and how can a wheelchair user access it?','ทางเข้าอยู่ตรงไหนและมีการช่วยคนเดินไม่สะดวกไหม','Where is this amenity and what access help is available?'),
'game_service':(['offered','game_version'],'เกมนี้ลงให้เล่นในรอบนี้หรือยัง เป็นรุ่นอะไร','Is this game actually offered here, and which version is installed?','ที่บริการนี้มีเกมให้เล่นใช่ไหม เวอร์ชันไหน','Can I play this game through this service, and which build is installed?'),
'game_mode':(['players_min','players_max'],'ต้องรวมคนอย่างน้อยกี่คน แล้วมากสุดกี่คน','What is the smallest and largest group that can play this mode?','เล่นโหมดนี้ต้องกี่คนเป็นอย่างต่ำและมากสุดเท่าไหร่','What are the lower and upper limits on the number of players?'),
'control_set':(['bindings'],'เวลาจะทำแต่ละท่าต้องกดตรงไหนบ้าง','Which inputs trigger each action while playing?','ขอการกดปุ่มของแต่ละคำสั่งเวลาเล่น','How do the buttons correspond to the actions?'),
'rate':(['amount_minor','unit'],'จ่ายเท่าไหร่ ราคานี้คิดต่ออะไร','What do I pay, and what is the charging unit?','จำนวนเงินเท่าไรและคิดเป็นรายอะไร','How much is charged and is it per session or per hour?'),
'rental_package':(['equipment_included','amount_minor'],'แพ็กนี้แถมเครื่องอะไรมาบ้าง แล้วต้องจ่ายเท่าไร','What equipment comes with this package, and what do I pay?','ค่าเหมาเท่าไหร่ มีเครื่องไหนรวมมาในแพ็กบ้าง','What kit is covered by the rental price?'),
'schedule':(['open_periods','bookable_periods'],'เวลาให้เข้าพื้นที่กับเวลาที่รับจองมีช่วงไหนบ้าง','When can I enter the venue, and when can I book a play slot?','เปิดให้เข้าได้เวลาไหน แล้วจองเล่นได้ช่วงใด','Are opening hours different from the periods available for reservations?'),
'closure':(['state','reason'],'ประกาศนี้ให้เปิดหรือหยุดบริการ เพราะอะไร','Does this notice suspend service or keep it open, and why?','วันตามประกาศเปิดไหม เพราะเหตุใด','What does this notice say about closure, and what is the reason?'),
'competition':(['rulebook_release','competition_dates'],'แข่งกันวันไหนและยึดกฎฉบับใด','When is the tournament held and which edition of the rulebook governs it?','รายการนี้ใช้กติกาเวอร์ชันไหน จัดวันอะไร','What are the event dates and the applicable rulebook version?'),
'competition_rule':(['text','completeness'],'ขอข้อกติกานี้แบบไม่ตัดข้อความ แล้วตรวจครบหรือยัง','Give the entire rule wording and say whether the section is complete.','เขียนกติกาข้อนี้มาเต็มๆ และบอกว่าส่วนนี้ครบหรือไม่','Show the full clause and its completeness status.'),
'news':(['body','event_start','event_end'],'ในข่าวแจ้งเรื่องอะไร แล้วจัดตั้งแต่ตอนไหนถึงตอนไหน','What does the bulletin announce and when does the event begin and finish?','กิจกรรมนี้ประกาศอะไร เริ่มเวลาไหน สิ้นสุดเวลาไหน','Summarize the announcement and give the event start and end times.'),
'person':(['role','public_contact_id'],'คนนี้ดูแลเรื่องไหน ติดต่อเรื่องงานทางไหน','What is this person responsible for, and how can I contact them for work?','หน้าที่ของผู้ดูแลนี้คืออะไร แล้วมีช่องทางติดต่อไหม','What duties does this person have and what is their public work contact?'),
'faq':(['answer','scope_note'],'ช่วยตอบข้อนี้ แล้วใช้กับสถานการณ์แบบไหน','Please answer this enquiry and explain the situations it applies to.','คำตอบข้อนี้ว่าอย่างไร มีขอบเขตใช้กับอะไร','What is the response to this FAQ, and when does it apply?'),
'live_binding':(['status_mapping','freshness_policy'],'รหัสสถานะถูกแปลว่าอะไร แล้วข้อมูลหมดอายุเมื่อไหร่','What do provider status codes mean, and when does the data expire?','สถานะที่ได้จากระบบหมายความว่าอะไร แล้วข้อมูลสดแค่ไหน','Explain the provider status translation and how long cached data stays fresh.'),
}
def damage(q):
    # Three separated edits, deterministic; never edits digits or entity aliases.
    if any('\u0e00'<=c<='\u0e7f' for c in q):
        positions=[i for i,c in enumerate(q) if '\u0e01'<=c<='\u0e2e']
    else:positions=[i for i,c in enumerate(q) if c.isalpha()]
    edits={positions[len(positions)//4]:'repeat',positions[len(positions)//2]:'delete',positions[3*len(positions)//4]:'repeat'}
    return ''.join('' if edits.get(i)=='delete' else c+c if edits.get(i)=='repeat' else c for i,c in enumerate(q))
def build():
    dev=[];reserved=[]
    for k,(keys,th,en,hth,hen) in Q.items():
        for lang,plain,later in [('th',th,hth),('en',en,hen)]:
            def case(q,style,index):return {'id':f'{k}-{lang}-{style}','kind':k,'lang':lang,'profile':index,'phrase':q,'expected_fields':keys,'style':style}
            dev.append(case(plain,'clean_new',3));dev.append(case(damage(plain),'sentence_noise',3))
            reserved.append(case(later,'reserved_new',7))
    # Negative correction must not select rejected price; history still focuses
    # current fields, not an arbitrary field from the previous question.
    for lang,q in [('th','ไม่เอาราคา ขอเวลาเล่นอย่างเดียว'),('en','I do not want the price; just tell me the play duration')]:
        dev.append({'id':'negative-service-'+lang,'kind':'service','lang':lang,'profile':3,'phrase':q,'expected_fields':['session_minutes'],'forbidden_fields':['amount_minor'],'style':'negative_correction'})
    for lang,q in [('th','แล้วแบบนี้ต้องยื่นอะไรล่ะ'),('en','So what should I bring to prove I qualify?')]:
        dev.append({'id':'context-audience-'+lang,'kind':'audience','lang':lang,'profile':3,'phrase':q,'expected_fields':['required_proofs'],'style':'context_new','history':True})
    for name,rows in [('DEVELOPMENT.json',dev),('RESERVED.json',reserved)]:
        data=json.dumps(rows,ensure_ascii=False,indent=2)
        with (B/name).open('x',encoding='utf-8') as f:f.write(data)
    manifest={'development':len(dev),'reserved':len(reserved),'reserved_hash':hashlib.sha256((B/'RESERVED.json').read_bytes()).hexdigest(),'synthetic_not_human_blind':True,'no_gold_to_model_or_resolver':True,'new_wording_not_r58_templates':True}
    (B/'QUESTION_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8');print(manifest)
if __name__=='__main__':build()
