import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
assert (r/'final_G3_all_summary.json').exists(),'Keep the full sweep source frozen until complete.'
paths=['app/pipeline/competition_detail.py','app/pipeline/competition_targets.py','app/pipeline/protected_intents.py']
for rel in paths:
    dest=r/'before_G4'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as out:out.write((p/rel).read_bytes())
def replace(rel,old,new):
    f=p/rel;s=f.read_text(encoding='utf-8');assert s.count(old)==1,(rel,old);f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
replace(paths[0],"r'เวอร์ชัน|game version'", "r'เวอร์ชัน|game version|แพลตฟอร์ม|ดัดแปลงตัวเกม|\\bplatform\\b|(?:modif|modification).{0,25}(?:game|client)|(?:game|client).{0,25}modif'")
replace(paths[0],"r'\\broster\\b', r'องค์ประกอบทีม", "r'\\broster\\b.{0,20}(?:size|composition|how many|กี่คน)|(?:size|composition|how many|กี่คน).{0,25}\\broster\\b', r'องค์ประกอบทีม")
replace(paths[0],"r'หลัง.*ปิดรับสมัคร|after.*registration.*clos'", "r'หลัง.*ปิดรับสมัคร|ปิดรับสมัคร(?:ไป)?แล้ว|after.*registration.*clos|registration\\s+(?:(?:has|is|was)\\s+)?closed'")
replace(paths[0],"    DetailConcept('tekken_settings',", "    DetailConcept('tekken_round_count', ('tekken8',), r'แต่ละเกม.{0,18}กี่รอบ|เกมละ.{0,18}กี่รอบ|จำนวนรอบต่อเกม|how many rounds|rounds per game', r'จำนวนรอบต่อเกม|Rounds per game'),\n    DetailConcept('tekken_settings',")
replace(paths[1],"    matched.sort(key=lambda value: value[0])", '''    if any(_contains_alias(query, s) for s in _RULE_SIGNALS) or re.search(r'แต่ละเกม.{0,18}กี่รอบ|เกมละ.{0,18}กี่รอบ|how many rounds|rounds per game', query, re.I):
        # Infer a bare franchise only when precisely one registered edition
        # exists. Derive stems from the registered names; never ignore an
        # explicitly supplied different numeric/Roman edition.
        families = {}
        for target in _TARGETS:
            for alias in target.aliases:
                stem = re.sub(r'\\s*\\d+\\s*$', '', alias).strip()
                if stem == alias or len(stem) < 4:
                    continue
                families.setdefault(stem.casefold(), {})[target.game_id] = target
        for stem, editions in families.items():
            boundary = r'(?<![a-z0-9])' if stem.isascii() else ''
            pattern = boundary + re.escape(stem) + r'(?![a-z0-9])(?!\\s*(?:ภาค|เวอร์ชัน|version)?\\s*\\d)(?!\\s+[ivx]+\\b)'
            mention = re.search(pattern, query, re.I)
            if len(editions) == 1 and mention:
                target = next(iter(editions.values()))
                if not any(t.game_id == target.game_id for _,t,_ in matched):
                    matched.append((mention.start(), target, mention.group(0)))
    matched.sort(key=lambda value: value[0])''')
replace(paths[1],"        return has_rule_signal or has_context_signal or roles or cs2_roster or valo_display or rov_late", '''        cs2_client = any(t.game_id == 'cs2' for t in target.targets) and bool(re.search(r'ดัดแปลงตัวเกม|(?:modif|modification).{0,25}(?:game|client)|(?:game|client).{0,25}modif', query, re.I))
        skin_permission = any(t.game_id in {'rov','tekken8'} for t in target.targets) and bool(re.search(r'(?:ใช้|เลือก).{0,12}สกิน.{0,18}(?:ได้|อนุญาต|ห้าม)|(?:may|can|allowed|permitted).{0,25}skins?|skins?.{0,25}(?:allowed|permitted)', query, re.I))
        tekken_rounds = any(t.game_id == 'tekken8' for t in target.targets) and bool(re.search(r'แต่ละเกม.{0,18}กี่รอบ|เกมละ.{0,18}กี่รอบ|จำนวนรอบต่อเกม|how many rounds|rounds per game', query, re.I))
        return has_rule_signal or has_context_signal or roles or cs2_roster or valo_display or rov_late or cs2_client or skin_permission or tekken_rounds''')
replace(paths[1],"    for other in resolve_competition_targets(query).targets:", "    resolution = resolve_competition_targets(query)\n    for index, other in enumerate(resolution.targets):")
replace(paths[1],"        for alias in sorted(other.aliases, key=len, reverse=True):", "        mentioned = resolution.explicit_mentions[index] if index < len(resolution.explicit_mentions) else ''\n        for alias in sorted(set((*other.aliases, mentioned)) - {''}, key=len, reverse=True):")
replace(paths[2],"    return asks_booking and asks_weekly_period and not (asks_slot and asks_current_slot)", '''    # A generic weekly maintenance question can use the recorded schedule;
    # adding a station/status, date, or current-time request still needs live
    # data. Do not allow the new period vocabulary to swallow that request.
    resource_status = bool(re.search(r'ว่าง|ถูกจอง|\\b(?:free|booked|vacant|available)\\b', q, re.I)) and bool(re.search(r'เครื่อง|อุปกรณ์|\\b(?:pc|ps5|vr|cockpit|nintendo|equipment|station)\\b', q, re.I))
    added_policy_period = not asks_current_slot and not resource_status and _has(q, 'ช่วงเช้า', 'ช่วงบ่าย', 'ปิดดูแลเครื่อง', 'บำรุงรักษา')
    return asks_booking and (asks_weekly_period or added_policy_period) and not (asks_slot and asks_current_slot) and not resource_status''')
with (p/'tests/test_r30_remaining_source_contracts.py').open('x',encoding='utf-8') as out:out.write('''import unittest
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.pipeline.competition_targets import resolve_competition_targets,looks_like_competition_rule_query,competition_query_for_target
from app.pipeline.protected_intents import is_weekly_booking_window_query
class R30RemainingSourceTests(unittest.TestCase):
    def test_client_multi_proposition_binds_one_source_before_split(self):
        q='CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม'
        self.assertTrue(looks_like_competition_rule_query(q))
        a=lookup_competition_reply(q,'th').answer
        self.assertIn('Steam',a);self.assertIn('ห้ามใช้การดัดแปลง',a)
        self.assertNotIn('ส่งเสียงดัง',a)
    def test_closed_registration_does_not_answer_roster_count(self):
        for q,l,term in [('CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ','th','หลังจากปิดรับสมัคร'),('CS2 registration is closed; can we add a teammate to the roster?','en','not permitted after')]:
            with self.subTest(locale=l):
                a=lookup_competition_reply(q,l).answer
                self.assertIn(term,a);self.assertNotIn('5 players',a);self.assertNotIn('ผู้เล่น 5 คน',a)
    def test_implicit_skin_permission_is_not_a_catalog_request(self):
        a=lookup_competition_reply('RoV ใช้สกินพิเศษได้หรือเปล่า','th').answer
        self.assertIn('ห้ามใช้สกินนอกจากสกิน Default',a)
        self.assertFalse(looks_like_competition_rule_query('RoV มีสกินอะไรบ้าง'))
    def test_bare_franchise_respects_explicit_other_edition(self):
        self.assertEqual(resolve_competition_targets('เทคเคนแต่ละเกมแข่งกี่รอบ').targets[0].game_id,'tekken8')
        for q in ['Tekken 7 tournament rules','เทคเคนภาค 7 กฎแข่ง','Tekken VII tournament rules']:
            with self.subTest(q=q):self.assertNotEqual(resolve_competition_targets(q).status,'exact')
        a=lookup_competition_reply('เทคเคนแต่ละเกมแข่งกี่รอบ','th').answer
        self.assertIn('จำนวนรอบต่อเกม (Round): 3',a)
        compared='เปรียบเทียบกฎ CS2 กับเทคเคน'
        self.assertEqual(len(resolve_competition_targets(compared).targets),2)
        focused=competition_query_for_target(compared,'cs2')
        self.assertEqual(resolve_competition_targets(focused).targets[0].game_id,'cs2')
        self.assertEqual(len(resolve_competition_targets(focused).targets),1)
    def test_generic_maintenance_policy_does_not_need_live_station_data(self):
        self.assertTrue(is_weekly_booking_window_query('วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง'))
        for q in ['PC1 ว่างไหมวันศุกร์ช่วงบ่าย','วันนี้บ่าย3 PC1 ว่างไหม','Is PC1 free on Friday afternoon?']:
            with self.subTest(q=q):self.assertFalse(is_weekly_booking_window_query(q))
''')
manifest={str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')}
with (r/'app_freeze_G4.json').open('x',encoding='utf-8') as out:json.dump(manifest,out,indent=2)
print(json.dumps({'changed':paths,'new_unit_tests':5}))
