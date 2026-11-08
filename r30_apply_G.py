import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
paths=['app/core/runtime_input_quality_guard.py','app/web_api/server.py','app/pipeline/competition_detail.py','app/pipeline/competition_targets.py']
for rel in paths:
    dest=r/'before_G'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as f:f.write((p/rel).read_bytes())
def replace(rel,old,new):
    f=p/rel;s=f.read_text(encoding='utf-8');assert s.count(old)==1,(rel,old);f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
replace(paths[0],'    @property\n    def action(self)', '''    @property
    def locale_layout_direction(self) -> str | None:
        """Only a classified mismatch may influence response language.

        The detector computes a best mapping direction even for ordinary
        text with negligible layout score. That candidate is not a decision.
        """
        return self.features.layout_direction if "keyboard_layout_mismatch" in self.flags else None

    @property
    def action(self)''')
replace(paths[1],'layout_direction = input_quality.features.layout_direction if input_quality else None','layout_direction = input_quality.locale_layout_direction if input_quality else None')
replace(paths[2],"r'เปลี่ยน(?:แปลง)?สมาชิก|change (?:team )?members|teams? change|member changes'", "r'เปลี่ยน(?:แปลง)?สมาชิก|เปลี่ยนตัว(?!ละคร)|สลับผู้เล่น|เปลี่ยนรายชื่อ|change (?:team )?members|teams? change|member changes|(?:swap|replace|change).{0,20}(?:players?|starters?)'")
replace(paths[2],"    DetailConcept('withdrawal',", "    DetailConcept('team_player_count', ('cs2',), r'ผู้เล่น(?:หลัก|ตัวจริง).{0,20}(?:กี่|จำนวน)|(?:ส่ง|ต้องมี).{0,12}ผู้เล่น.{0,12}(?:กี่|คน)|(?:how many|number of).{0,20}(?:starting players|starters)|(?:starting players|starters).{0,20}(?:how many|number)', r'องค์ประกอบทีม.*ผู้เล่น 5 คน|Team composition.*5 players'),\n    DetailConcept('withdrawal',")
replace(paths[2],"r'เริ่ม.*ช้า|starts?.*late|start.*minutes late'", "r'เริ่ม.*ช้า|มาสาย|starts?.*late|start.*minutes late|(?:arrive|arrival|team is).{0,15}late'")
replace(paths[2],"r'ช้าเกินกว่า.*15 นาที|starts.*15 minutes'", "r'ช้าเกินกว่า.*15 นาที|starts.*15 minutes'") if False else None
replace(paths[2],"    return CompetitionDetail(render_rule_reply(selected[0], selected[1:], used[0], locale),tuple(used),tuple(c.name for c in concepts))", '''    answer = render_rule_reply(selected[0], selected[1:], used[0], locale)
    if any(c.name == 'rov_lateness' for c in concepts) and re.search(r'มาสาย|arriv', query, re.I):
        # The source regulates a delayed match start, not an independent
        # arrival deadline. Preserve that condition rather than inventing one.
        note = ("This clause applies when the match starts more than 15 minutes after the scheduled time. It does not establish a separate arrival deadline."
                if locale == 'en' else "ข้อนี้กำหนดกรณีเริ่มการแข่งขันช้ากว่าเวลาที่กำหนดเกิน 15 นาที ไม่ได้ระบุเส้นตายการมาถึงแยกต่างหากครับ")
        marker = '\\nRulebook:' if locale == 'en' else '\\nอ้างอิงจากกติกา:'
        answer = answer.replace(marker, '\\n' + note + marker, 1)
    return CompetitionDetail(answer,tuple(used),tuple(c.name for c in concepts))''')
replace(paths[3],"        return has_rule_signal or has_context_signal",'''        # Participant roles and a paired display-setting request express a
        # rulebook proposition without requiring the word "rules". Bind these
        # to an exact game; changing a character is not changing a roster.
        roles = bool(re.search(r"ผู้เล่น(?:หลัก|ตัวจริง).{0,20}(?:กี่|จำนวน)|(?:ส่ง|ต้องมี).{0,12}ผู้เล่น.{0,12}(?:กี่|คน)|(?:how many|number of).{0,20}(?:starting players|starters)", query, re.I))
        cs2_roster = any(t.game_id == 'cs2' for t in target.targets) and bool(re.search(r"เปลี่ยนตัว(?!ละคร)|สลับผู้เล่น|เปลี่ยน(?:แปลง)?สมาชิก|(?:swap|replace|change).{0,20}(?:players?|starters?)", query, re.I))
        valo_display = any(t.game_id == 'valorant' for t in target.targets) and bool(re.search(r"ปิด.{0,20}(?:เลือด|ศพ)|(?:เลือด|ศพ).{0,20}ปิด|turn.{0,12}off.{0,25}(?:blood|bodies)|(?:blood|bodies).{0,25}(?:off|display|settings)", query, re.I))
        rov_late = any(t.game_id == 'rov' for t in target.targets) and bool(re.search(r"มาสาย|(?:เริ่ม|เริ่มแข่ง).{0,15}ช้า|(?:arrive|arrival|team is|starts?).{0,15}late", query, re.I))
        return has_rule_signal or has_context_signal or roles or cs2_roster or valo_display or rov_late''')
manifest={str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')}
with (r/'app_freeze_G.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,indent=2)
print(json.dumps({'changed':paths,'freeze_files':len(manifest)}))
