import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
assert (r/'final_G4_all_summary.json').exists(),'Do not change a source while its complete sweep is running.'
for rel in ['app/core/runtime_input_quality_guard.py','app/pipeline/competition_detail.py','app/pipeline/competition_targets.py','app/pipeline/protected_intents.py','tests/test_r30_remaining_source_contracts.py']:
    dest=r/'before_G5'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as out:out.write((p/rel).read_bytes())
f=p/'app/pipeline/competition_detail.py';s=f.read_text(encoding='utf-8');old=r"r'\broster\b.{0,20}(?:size|composition|how many|กี่คน)|(?:size|composition|how many|กี่คน).{0,25}\broster\b'";new=r"r'\broster\b.{0,20}(?:size|composition|how many|กี่คน)|(?:size|composition|how many|กี่คน).{0,25}\broster\b|(?:^|[,;])\s*roster\s*(?=[,;?]|$)|\broster\s+(?:rules|requirements)\b'";assert s.count(old)==1;f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
f=p/'app/pipeline/competition_detail.py';s=f.read_text(encoding='utf-8');old=r"r'ภาษาอะไร|ภาษา.*ประท้วง|which language|official language'";new=r"r'ภาษาอะไร|ภาษา.*ประท้วง|ประท้วง.*ภาษา|which language|official language|(?:protest|objection).{0,45}(?:English|Thai|language)|(?:English|Thai|language).{0,45}(?:protest|objection)'";assert s.count(old)==1;f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
f=p/'app/pipeline/competition_targets.py';s=f.read_text(encoding='utf-8');old="        return has_rule_signal or has_context_signal or roles or cs2_roster or valo_display or rov_late or cs2_client or skin_permission or tekken_rounds";new="        cs2_event_version = any(t.game_id == 'cs2' for t in target.targets) and bool(re.search(r'รายการ.{0,35}เวอร์ชัน|เวอร์ชัน.{0,35}รายการ', query, re.I))\n        return has_rule_signal or has_context_signal or roles or cs2_roster or valo_display or rov_late or cs2_client or skin_permission or tekken_rounds or cs2_event_version";assert s.count(old)==1;f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
from r30_guard_composition_payload import PAYLOAD
f=p/'app/core/runtime_input_quality_guard.py';s=f.read_text(encoding='utf-8')
for old,new in [('from dataclasses import dataclass','from dataclasses import dataclass, replace'),('PROFILE_FORMAT_VERSION = "keyboard-profile-v1"','PROFILE_FORMAT_VERSION = "keyboard-profile-v1"\nRUNTIME_LAYOUT_COMPOSITION_REVISION = "catalog-repeat-layout-r30-G5"'),("digest.update((LAYOUT_SCORING_REVISION + '\\n').encode('utf-8'))","digest.update((LAYOUT_SCORING_REVISION + '\\n' + RUNTIME_LAYOUT_COMPOSITION_REVISION + '\\n').encode('utf-8'))"),('    elapsed_ms: float\n','    elapsed_ms: float\n    composition_evidence: dict[str, object] | None = None\n'),('            "repeat_reason": self.features.repeat_reason,','            "repeat_reason": self.features.repeat_reason,\n            "composition_evidence": self.composition_evidence,'),('    def inspect(self, text: str) -> InputQualityDecision:',PAYLOAD+'    def inspect(self, text: str) -> InputQualityDecision:'),('        features = self.detector.analyze(text)\n','        features = self.detector.analyze(text)\n        features, composition_evidence = self._composed_layout_features(features)\n'),('                elapsed_ms=elapsed_ms,','                elapsed_ms=elapsed_ms,\n                composition_evidence=composition_evidence,')]:
    assert s.count(old)==1,(f,old);s=s.replace(old,new)
f.write_text(s,encoding='utf-8',newline='\n')
f=p/'app/pipeline/protected_intents.py';s=f.read_text(encoding='utf-8');old="    resource_status = bool(re.search(r'ว่าง|ถูกจอง|\\b(?:free|booked|vacant|available)\\b', q, re.I)) and bool(re.search(r'เครื่อง|อุปกรณ์|\\b(?:pc|ps5|vr|cockpit|nintendo|equipment|station)(?:\\s*#?\\s*\\d+)?\\b', q, re.I))";new="""    numbered_resource = bool(re.search(r'\\b(?:pc|ps5|vr|cockpit|nintendo|equipment|station)\\s*#?\\s*\\d+\\b', q, re.I))
    generic_periods = not asks_current_slot and not numbered_resource and bool(re.search(r'\\b(?:which|what)\\s+(?:days?|hours?|time\\s+periods?)\\b|\\b(?:days?\\s+and\\s+time\\s+periods?|weekly\\s+schedule)\\b', q, re.I))
    status_predicate = bool(re.search(r'ว่าง|ถูกจอง|\\b(?:free|booked|vacant)\\b', q, re.I)) or (not generic_periods and bool(re.search(r'\\bavailable\\b', q, re.I)))
    resource_status = status_predicate and bool(re.search(r'เครื่อง|อุปกรณ์|\\b(?:pc|ps5|vr|cockpit|nintendo|equipment|station)(?:\\s*#?\\s*\\d+)?\\b', q, re.I))""";assert s.count(old)==1;f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
f=p/'tests/test_r30_remaining_source_contracts.py';s=f.read_text(encoding='utf-8')
s += '''
    def test_enumerated_roster_topic_keeps_the_count_without_action_collision(self):
        a=lookup_competition_reply('What do the CS2 tournament rules say about eligibility, roster, and registration?','en').answer
        for term in ['Open only to students','5 players','not permitted after']:self.assertIn(term,a)
    def test_available_general_periods_is_schedule_not_device_occupancy(self):
        for q in ['Which days and time periods are available for PC booking?','Which time periods are available for PC booking?']:
            with self.subTest(q=q):self.assertTrue(is_weekly_booking_window_query(q))
        for q in ['Which PC1 booking slots are available on Friday afternoon?','Which time periods is PC1 available today?']:
            with self.subTest(q=q):self.assertFalse(is_weekly_booking_window_query(q))
    def test_event_version_and_protest_language_are_rule_propositions(self):
        self.assertTrue(looks_like_competition_rule_query('รายการ CS2 ใช้เวอร์ชันเกมแบบไหน'))
        for q,l,term in [('CS2 ถ้าจะประท้วงใช้ภาษาอังกฤษได้ไหม หรือบังคับไทย','th','ภาษาไทย'),('May CS2 protests be submitted in English or must they use Thai?','en','Thai')]:
            with self.subTest(q=q):self.assertIn(term,lookup_competition_reply(q,l).answer)
    def test_catalog_name_repeat_layout_review_requests_retype_without_mutation(self):
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        guard=RuntimeInputQualityGuard.from_environment();guard.mode='enforce'
        for q in [',u Call of Duty: Modern Warfare III wss,',',u Delta Force wss,']:
            with self.subTest(q=q):
                d=guard.inspect(q);self.assertTrue(d.should_short_circuit)
                self.assertEqual(d.features.input_text,q)
                self.assertIn('keyboard_layout_mismatch',d.flags)
                self.assertFalse(d.composition_evidence['raw_input_mutated'])
    def test_catalog_name_layout_review_does_not_block_ordinary_prose(self):
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        guard=RuntimeInputQualityGuard.from_environment();guard.mode='enforce'
        for q in ['Is Delta Force available?','Can u play Delta Force?','I like Delta Force, u?','มี Call of Duty: Modern Warfare III ไหม','Is Call of Duty: Modern Warfare III available?','Can I play Delta Force?','Can I pllay Delta Force?']:
            with self.subTest(q=q):self.assertNotIn('keyboard_layout_mismatch',guard.inspect(q).flags)
'''
f.write_text(s,encoding='utf-8',newline='\n')
cases=json.loads((r/'focused_fixture_G4_source.json').read_text(encoding='utf-8'))['cases']
for q,yes,mode in [('What do the CS2 tournament rules say about eligibility, roster, and registration?',['Open only to students','5 players','not permitted after'],None),('Which days and time periods are available for PC booking?',['09:00-12:00','13:00-16:00','not live station availability'],'pipeline:protected_booking_window'),('Which time periods are available for PC booking?',['09:00-12:00','13:00-16:00','not live station availability'],'pipeline:protected_booking_window')]:
    cases.append(dict(id='G5-'+str(len(cases)+1),locale='en',question=q,must_contain=yes,must_not_contain=[],required_source='competition_rules_cs2' if mode is None else '',group='source_G5',outcome=None,mode_prefix=mode))
for q,l,yes,no in [('รายการ CS2 ใช้เวอร์ชันเกมแบบไหน','th',['CS2','Steam','ล่าสุด'],['Call of Duty']),('CS2 ถ้าจะประท้วงใช้ภาษาอังกฤษได้ไหม หรือบังคับไทย','th',['ภาษาไทย','ประท้วง'],['มีปุ่มอะไรบ้าง']),('May CS2 protests be submitted in English or must they use Thai?','en',['Thai','protests'],['controls'])]:
    cases.append(dict(id='G5-'+str(len(cases)+1),locale=l,question=q,must_contain=yes,must_not_contain=no,required_source='competition_rules_cs2',group='source_G5',outcome=None,mode_prefix='pipeline:competition_rule_detail_source'))
for q in [',u Call of Duty: Modern Warfare III wss,',',u Delta Force wss,']:
    cases.append(dict(id='G5-'+str(len(cases)+1),locale='auto',question=q,must_contain=[],must_not_contain=[],required_source='',group='true_wrong_layout',outcome=None,mode_prefix='input_guard_layout_retype'))
for q in ['Is Delta Force available?','Can u play Delta Force?','I like Delta Force, u?','Is Call of Duty: Modern Warfare III available?']:
    cases.append(dict(id='G5-'+str(len(cases)+1),locale='en',question=q,must_contain=[],must_not_contain=[],required_source='',group='guard_negative',outcome=None,mode_prefix=None,not_mode_prefix='input_guard_layout_retype'))
with (r/'focused_fixture_G5_source.json').open('x',encoding='utf-8') as out:json.dump({'cases':cases,'scope':'source contracts plus full-suite regression cases'},out,ensure_ascii=False,indent=2)
with (r/'app_freeze_G5.json').open('x',encoding='utf-8') as out:json.dump({str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')},out,indent=2)
for old,new in [('r30_extra_G4.py','r30_extra_G5.py'),('r30_extra_analyze_G4.py','r30_extra_analyze_G5.py'),('r30_build_G4_analysis.py','r30_build_G5_analysis.py'),('r30_http_G4.py','r30_http_G5.py'),('r30_source_G4_tests.py','r30_source_G5_tests.py')]:
    s=Path(old).read_text(encoding='utf-8').replace('G4','G5')
    if new=='r30_build_G5_analysis.py':
        original='ตัวอย่าง Direct runner: `The Last of Us Part I / Part II ราคาเท่าไหร่` ตอบว่าแป้นอาจผิด แต่ API จริงในโหมด Auto ตอบราคา PS5 ภาษาไทยได้ถูกทาง ตรวจโค้ดแล้วพบว่า server ส่ง surface_language ให้ resolve_locale ขณะที่ engine โดยตรงไม่ส่งขั้นตอนนี้ จึงเป็นความต่างของทางเข้า ไม่ใช่หลักฐานว่าเว็บยังตอบกรณีนี้ผิด เก็บ auto/th/en probe และตรวจซ้ำ Auto ทุก input ด้วยการเลือกภาษาแบบ server โดยคงคะแนนเดิมแยกไว้ ควรรวม adapter ของการทดสอบให้ตรงกับทางเข้าใช้งาน'
        revised='Ingress/locale: F direct กับ API ใช้ surface binding ต่างกัน จากนั้น G2 แก้ candidate layout direction ที่ยังไม่จำแนก และ G3 แยก source game titles จากหลักฐานภาษา Full sweep G2/G3/G4/G5 ใช้ binding แบบ server แล้ว Mixed-title fixture ตรวจ 8 ข้อแยกภาษา การเทียบ G2→G3 พบ 45 grades ดีขึ้นและ 4 grades แย่ลงทั้งหมดเป็น latency ของ Minecraft ประโยคเดียวที่คำตอบไม่เปลี่ยน จึงไม่เหมารวมเป็น content regression'
        assert original in s;s=s.replace(original,revised)
        original='บางคำถาม เช่น “วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง” เข้า live path แล้วเมื่อ fixture ถูกกำหนด unavailable จึงแจ้งดึงสดไม่ได้ ทั้งที่สามารถตอบนโยบาย Maintenance ทั่วไปได้บางส่วน ควรตอบส่วนตารางที่ยืนยันได้พร้อมแยกว่ารอบจริงยังต้องดึงสด ไม่แปลง offline fixture เป็นหลักฐานว่าจองจริงผิด'
        revised='คำถาม Maintenance ทั่วไปแก้ G4 ให้ตอบ weekly policy จากตารางเดิม และแยก PC1/status เป็น live path G4 unit พบ available for generic days/time periods ถูกกันผิด จึงแก้ G5 พร้อม regression tests คำถามวัน/เวลา/เครื่องจริงตรวจ path แยกจาก occupancy oracle ห้ามแปลง controlled unavailable fixture เป็นหลักฐานว่าข้อมูลจองจริงผิด'
        assert original in s;s=s.replace(original,revised)
        s=s.replace("headers+=['','## เปรียบเทียบ", "headers+=['','## ข้อผิดเพิ่มเติมที่แก้ G4/G5','', 'G4: CS2 platform/client clause, after-closed registration action, RoV Default skin, Tekken rounds และ bare franchise edition qualifier; G5: restored enumerated roster topic, generic booking-period available, CS2 event version ก่อน catalog target lock และ protest-language ลำดับคำสองทิศ ตรวจ source literals ไม่สร้างนโยบายใหม่ หลักฐานก่อน/หลังใน *_source_G5_results.jsonl และ Flow final', '', '## เปรียบเทียบ")
        s=s.replace('บล็อกตาม policy ถูก 498/500 อีก 2 เคส mixed game title ไม่จับ layout และตอบข้อมูลเกมแทนคำถาม availability','G2/G3 บล็อกตาม policy ถูก 498/500; G5 ตรวจ accidental repeat ที่มีหลักฐานจาก corpus ก่อนประเมิน wrong layout ใน residual รอบชื่อเกม exact โดยไม่เปลี่ยนข้อความ และตรวจ corpus 500 อีกครั้ง ผลล่าสุดดู final_G5_runtime_guard500_summary.json; corpus นี้ยังไม่มี content oracle ครบ')
    if new=='r30_http_G5.py':s=s.replace("'source_G4'","'source_G5'")
    if new=='r30_http_G5.py':s=s.replace("if required_mode and not response['mode'].startswith(required_mode):errors.append('mode_contract:'+response['mode'])","if required_mode and not response['mode'].startswith(required_mode):errors.append('mode_contract:'+response['mode'])\n                    if c.get('not_mode_prefix') and response['mode'].startswith(c['not_mode_prefix']):errors.append('forbidden_mode:'+response['mode'])")
    if new=='r30_source_G5_tests.py':s=s.replace("if not a.validation.ok:errors.append('validation_rejected')","if c.get('not_mode_prefix') and a.mode.startswith(c['not_mode_prefix']):errors.append('forbidden_mode:'+a.mode)\n        if not a.validation.ok:errors.append('validation_rejected')")
    with Path(new).open('x',encoding='utf-8') as out:out.write(s)
with Path('r30_guard_runtime500_G5.py').open('x',encoding='utf-8') as out:out.write(Path('r30_guard_runtime500.py').read_text(encoding='utf-8').replace('final_G_runtime','final_G5_runtime'))
with Path('r30_compare_G3_G5.py').open('x',encoding='utf-8') as out:out.write(Path('r30_final_compare.py').read_text(encoding='utf-8').replace('G3','G5').replace('G2','G3'))
print(json.dumps({'regressions_fixed':2,'additional_confirmed_route_defects_fixed':2,'focused_source_cases':len(cases)}))
