from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip())
path=P/'app/pipeline/competition_source_gaps.py'
with (R/'candidate9_source_year_before_bounds.py').open('xb') as f:f.write(path.read_bytes())
s=path.read_text(encoding='utf-8');old='    requested = set(re.findall(r"(?<![\\d.])(?:19|20)\\d{2}(?![\\d.])", query))\n';assert old in s
new='''    requested = set()
    for match in re.finditer(r"(?<![\\d.])(?:19|20)\\d{2}(?![\\d.])", query):
        before = query[max(0, match.start() - 40):match.start()]
        after = query[match.end():match.end() + 24]
        # Four-digit amounts and birth years do not request a rulebook edition.
        if re.search(r"(?:born(?:\\s+in)?|birth\\s+year|เกิด(?:ใน)?\\s*(?:ปี)?|ราคา|fee(?:\\s+of)?|costs?)\\s*$", before, re.I):
            continue
        if re.match(r"\\s*(?:บาท|baht\\b|THB\\b|USD\\b|years? old\\b)", after, re.I):
            continue
        requested.add(match.group(0))
'''
path.write_text(s.replace(old,new),encoding='utf-8')
path=P/'tests/test_competition_recorded_year_r32.py';s=path.read_text(encoding='utf-8');s+='''
    def test_birth_year_and_four_digit_fee_are_not_editions(self):
        for q in ['CS2 tournament entry fee 2027 baht', 'CS2 born in 2007 eligibility', 'กติกา CS2 เกิดปี 2007 สมัครได้ไหม', 'กติกา CS2 ค่าสมัคร 2027 บาท']:
            with self.subTest(q=q):
                self.assertIsNone(_recorded_year_guard(q,'en','competition_rules_cs2_psu_phuket_2026'))
        self.assertIsNotNone(_recorded_year_guard('CS2 rules 2027: born in 2007 eligible?','en','competition_rules_cs2_psu_phuket_2026'))
''';path.write_text(s,encoding='utf-8')
