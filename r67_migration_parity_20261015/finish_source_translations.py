"""Apply agent-reviewed source translations; preserve all original revisions."""
import copy,hashlib,json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now,value
from app.knowledge.common.translation import validate_translation
from app.knowledge.records import canonical_json
store=CommonStore(B/'common.sqlite')
with store.connect() as c:rs=store.heads(c)
english=json.loads((B/'reviewed_description_english.json').read_text('utf8'))
notes={
 'efootball':['Control player movement and dribbling.','Use for low passes when attacking and pressing when defending.','The command depends on possession of the ball.','The command depends on possession of the ball.','The command depends on possession of the ball.','Press together with movement to dash.'],
 'overcooked_2':['Control the chef’s movement.','Chop ingredients or throw items.','Pick up or put down items.','Dash to move faster.','Use an emote to communicate.'],
 'the_finals':['Interact with objects and objectives.','Use the primary weapon.','Aim the weapon.','Sprint.','Use the specialization ability.','Reload the weapon.','Perform a quick melee attack.','Crouch or slide.','Switch or select a weapon.','Open the equipment wheel.']}
warning_translations=[
 ('Based on KONAMI', 'อ้างอิงคู่มือจอยอย่างเป็นทางการของ KONAMI ต้องตรวจการตั้งค่าคำสั่งในเกมก่อนเผยแพร่ เพราะปุ่ม eFootball อาจต่างกันตามการตั้งค่าคอนโซล/PC และการอัปเดตเกม'),
 ('Default PS5 controls', 'ชุดปุ่ม PS5 เริ่มต้นจากตารางปุ่มที่เผยแพร่ไว้ THE FINALS รองรับการตั้งค่าจอย ต้องตรวจปุ่มที่เปลี่ยนในเมนูตั้งค่าภายในเกม'),
 ('Default one-player', 'ชุดปุ่ม PlayStation สำหรับผู้เล่นหนึ่งคนตามคู่มือปุ่มที่เผยแพร่ ตัวเกมปรับปุ่มได้ เจ้าหน้าที่จึงควรตรวจผังปุ่มของเวอร์ชันที่ติดตั้งก่อนแนะนำผู้เล่น'),
 ('Epic official', 'ฝ่ายสนับสนุนอย่างเป็นทางการของ Epic อธิบายวิธีค้นหา/เปลี่ยนค่าเริ่มต้นของจอยและระบุ preset แต่บทความสาธารณะไม่ได้ให้ผังปุ่มเกมเพลย์ PS5 ครบทุกปุ่ม'),
 ('Official Nintendo page', 'หน้าอย่างเป็นทางการของ Nintendo ยืนยันการควบคุมที่เรียบง่ายและการใช้ Joy-Con หนึ่งข้าง แต่ไม่ได้ให้ผังปุ่มครบทุกปุ่มในหน้าสาธารณะ'),
 ('Official Nintendo support confirms', 'ฝ่ายสนับสนุนอย่างเป็นทางการของ Nintendo ยืนยันรูปแบบจอยที่รองรับและการควบคุมโหมด Leg-Strap ท่าทางของกีฬาแต่ละชนิดขึ้นกับกีฬาที่เลือก'),
 ('Official Nintendo support documents', 'เอกสารสนับสนุนอย่างเป็นทางการของ Nintendo อธิบายการใช้เมนูและแนวคิดควบคุมด้วย Ring-Con/Leg Strap การกระทำในเกมขึ้นกับท่าออกกำลังกายและจะแสดงบนหน้าจอ'),
 ('Official Nintendo/Play Nintendo', 'หน้าอย่างเป็นทางการของ Nintendo/Play Nintendo ยืนยันการควบคุมด้วยปุ่มและจอยที่รองรับ แต่ไม่ได้เผยแพร่ผังปุ่มชุดเดียวที่ครบทุกกระดาน/มินิเกมในหน้าสาธารณะ'),
 ('Official PlayStation support confirms', 'ฝ่ายสนับสนุนอย่างเป็นทางการของ PlayStation ยืนยันรูปแบบควบคุม Gesture และ Analogue แต่หน้าสนับสนุนสาธารณะไม่ได้ให้ผังปุ่มครบทุกปุ่ม'),
 ('Official sources confirm PS VR2', 'แหล่งอย่างเป็นทางการยืนยันว่าต้องใช้จอย PS VR2 Sense และเล่นด้วยการฟันตามจังหวะใน VR ยังไม่พบผังปุ่มเมนูอย่างละเอียดในแหล่งสาธารณะอย่างเป็นทางการ'),
 ('Official support is available', 'มีฝ่ายสนับสนุนอย่างเป็นทางการ แต่ระหว่างการปรับปรุงข้อมูลครั้งนั้นยังไม่พบตารางปุ่ม Nintendo Switch ที่คงที่จากแหล่งตรวจสอบได้ ต้องเก็บผังปุ่มเริ่มต้นของเวอร์ชันที่ติดตั้งในศูนย์ก่อนเผยแพร่'),
 ('Riot support confirms hotkeys', 'ฝ่ายสนับสนุน Riot ยืนยันว่าสามารถรีเซ็ต/จัดการ hotkey ได้ แต่หมายเหตุปุ่มเริ่มต้นอย่างละเอียดในชุดนี้อ้างคู่มืออีสปอร์ตจากแหล่งรอง ต้องตรวจใน League client ของศูนย์ก่อนระบุว่าครบ'),
 ('Riot support has a VALORANT', 'Riot มีศูนย์สนับสนุน VALORANT แต่ยังไม่พบตารางปุ่มเริ่มต้นฉบับเต็มที่เปิดเผยสาธารณะจากที่นั่น รายการละเอียดนี้อ้างคู่มือแหล่งรองและควรตรวจบน PC ของศูนย์ก่อนระบุว่าครบ'),
 ('The detailed key list', 'รายการปุ่มละเอียดมาจากคู่มือ GameFAQs ที่อัปเดตในปี 2026 คู่มือระบุว่าปุ่ม PC ปรับได้ จึงต้องตรวจบน PC ของศูนย์ก่อนระบุว่าครบ'),
 ('The official PlayStation page', 'หน้าอย่างเป็นทางการของ PlayStation ยืนยันการเปลี่ยนปุ่มพื้นฐานและคำแนะนำควบคุม แต่ระหว่างการปรับปรุงข้อมูลครั้งนั้นยังไม่พบตารางปุ่มเริ่มต้นที่คงที่จากแหล่งตรวจสอบได้ ต้องเก็บผังปุ่มเริ่มต้นของเวอร์ชันที่ติดตั้งในศูนย์ก่อนเผยแพร่'),
 ('Updated from incorrect FINAL', 'แก้ข้อมูลที่เดิมเป็นปุ่ม FINAL FANTASY XV ผิดภาคให้เป็นปุ่ม FINAL FANTASY XVI แบบ Type A แล้ว ตรวจเทียบกับ GameWith และ Jegged แต่ควรตรวจบน PS5 ของศูนย์ก่อนระบุว่าครบ'),
 ('Valve/Steam official', 'หน้าอย่างเป็นทางการของ Valve/Steam ยืนยันตัวเกม แต่ตารางปุ่มเริ่มต้นละเอียดนี้อ้างคู่มือจากแหล่งรอง ต้องตรวจบน PC ของศูนย์ก่อนระบุว่าครบ')]
thai_warning_english={
 'Layout นี้ย้ายปุ่มกระโดดและสไลด์เพื่อให้ผู้เล่นสามารถทำ Movement ไปพร้อมกับการหมุนอนาล็อกเล็งปืนได้โดยไม่ต้องยกนิ้วหัวแม่มือออก':'This layout moves the jump and slide buttons so players can move while aiming with the analog stick without lifting their thumb.',
 'ตัวเกมออกแบบมาให้สามารถกดคำสั่งเดียวกันได้จากหลายปุ่ม เพื่อความถนัดของผู้เล่นแต่ละคน':'The game allows the same command to be activated with several buttons to suit different players.',
 'ตัวเกมใช้ระบบกดค้าง (Hold) ที่ปุ่ม L1 และ R1 เป็นตัวสลับ (Modifier) เพื่อใช้สกิลพิเศษและแก็ดเจ็ต':'The game uses Hold on L1 and R1 as Modifier buttons for special abilities and gadgets.',
 'ปุ่ม R2 มีความสำคัญมาก กดรัวเพื่อโจมตีปกติ หรือกดค้างเพื่อใช้เป็นปุ่ม Shift สำหรับเลือกใช้คาถาที่ติดตั้งไว้ 4 ช่อง':'R2 is especially important: press repeatedly for normal attacks, or hold it as a Shift button to select spells assigned to 4 slots.',
 'เกมมีระบบการกดปุ่มผสม โดยใช้ L1 (Block) และ L2 (Aim) เป็นปุ่ม Modifier เพื่อเปลี่ยน Action ของปุ่มอื่นๆ':'The game supports button combinations, using L1 (Block) and L2 (Aim) as Modifier buttons that change the Action of other buttons.',
 'เกมเน้นความรวดเร็วในการกดคอมโบและการชิงจังหวะด้วยคาถาสลับร่าง (L2) รวมถึงการสลับตัวละครแบบเรียลไทม์ (RS)':'The game emphasizes fast combos and gaining an opening with substitution jutsu (L2), together with real-time character switching (RS).',
 'เกมเน้นความสมจริง ปุ่ม R2 และ L2 จะมีการใช้ฟีเจอร์ Adaptive Triggers ของจอย DualSense เพื่อจำลองน้ำหนักของคันเร่งและแป้นเบรก':'For realism, R2 and L2 use the DualSense controller’s Adaptive Triggers to simulate resistance from the accelerator and brake pedals.',
 'โหมดการเล่น Battle Royale โดยมีออปชั่นเสริมให้สลับปุ่ม L1/L2 และ R1/R2 ได้จากหน้าเมนูเพื่อความถนัดของผู้เล่น':'Battle Royale mode provides an option in the menu to swap L1/L2 and R1/R2 to suit the player.'}
english_source_thai={
 'migrated_game_mario_kart_live_home_circuit':'ควบคุมรถ Mario Kart จริงด้วย Nintendo Switch แล้วดูรถมีชีวิตขึ้นมาในเกม! แข่งรถ Mario Kart™ จริงในบ้านของคุณ ใช้เครื่อง Nintendo Switch™ ควบคุมรถและดูการตอบสนองต่อสิ่งที่เกิดขึ้นในเกม ขณะเร่งความเร็วและดริฟต์สู่ชัยชนะ สนามในบ้านจะปรากฏบนหน้าจอผ่านมุมมองจากด้านหลังที่นั่งคนขับ',
 'source_listing_our_games_scraped_overcooked_overcooked_2':'เตรียมพร้อมกับความสนุกทำอาหารร่วมกันสองเท่า เมื่อ Overcooked! และ Overcooked! 2 มารวมกันอย่างโกลาหล ใน Overcooked! เล่นคนเดียวหรือร่วมเล่นบนเครื่องเดียวกันได้สูงสุดสี่คน ทั้งโหมดร่วมมือและแข่งขัน ต้องทำอาหารหลากหลายเมนูและทำงานร่วมกันให้เป็นทีมที่มีประสิทธิภาพ ส่วน Overcooked! 2 กลับมาพร้อมแอ็กชันทำอาหารสุดวุ่นวายชุดใหม่!...'}
saved=[];reviews=[]
for rid,r0 in rs.items():
 r=copy.deepcopy(r0);changed={}
 d=value(r,'official_description')
 if d:
  if rid in english_source_thai:new={'th':english_source_thai[rid],'en':d['th']}
  else:new={'th':d['th'],'en':english[rid]};validate_translation(d['th'],new['en'])
  changed['official_description']=new
 if rid.startswith('recovered_controls_') and value(r,'bindings'):
  key=rid.removeprefix('recovered_controls_ps5_');rows=copy.deepcopy(value(r,'bindings'));assert len(rows)==len(notes[key])
  for row,en in zip(rows,notes[key]):validate_translation(row['notes']['th'],en);row['notes']['en']=en
  changed['bindings']=rows
 warning=value(r,'verification_note')
 if warning:
  if warning.get('en') and not warning.get('th'):
   original=warning['en'];translated=next((th for prefix,th in warning_translations if original.startswith(prefix)),None)
   if translated is None and original in thai_warning_english:changed['verification_note']={'th':original,'en':thai_warning_english[original]}
   elif translated:changed['verification_note']={'th':translated,'en':original}
   else:raise ValueError('Unreviewed warning: '+original)
 changed={key:v for key,v in changed.items() if value(r,key)!=v}
 if not changed:continue
 data={'mapped_fields':changed,'translation_lineage':[{'field':key,'original_field_evidence':r['fields'][key]['evidence_refs'],'source_value':value(r,key),'translated_value':v,'method':'agent source-by-source translation; no owner approval; no new gameplay verification'} for key,v in changed.items()]}
 raw=canonical_json(data);sid='r67_reviewed_'+hashlib.sha256((rid+raw).encode()).hexdigest()[:24]
 store.add_source({'source_id':sid,'kind':'derived_curated','path':'translation://r67/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[r['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='r67-source-translation-review')
 for key,v in changed.items():r['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/mapped_fields/'+key}],'note':'Agent translation checked against source; original revisions retained; not owner approved'}
 r['localization']['en_status']='agent_translated';saved.append(store.save(r,actor='r67-source-translation-review',expected_version=r['revision'],change_note='Source-preserving bilingual draft; retain exceptions, numbers and source warnings'))
 reviews.append({'record_id':rid,'fields':list(changed),'agent_semantic_reviewed':True,'owner_reviewed':False})
(B/'SOURCE_TRANSLATION_REVIEW.json').write_text(json.dumps({'saved':saved,'reviews':reviews,'local_model_calls_succeeded':0,'local_model_limitation':'socket access denied by sandbox; proposals not used','review_basis':'agent read original source text directly'},ensure_ascii=False,indent=2),encoding='utf8')
print('Saved agent-reviewed bilingual source fields in',len(saved),'records')
