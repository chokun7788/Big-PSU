import json,sys,os,time
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).parent;P=Path(sys.argv[2]) if len(sys.argv)>2 else Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P))
sys.path.append(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
R=Path((ROOT/'r30_report_path.txt').read_text().strip());run=sys.argv[1]
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0';os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
from app.pipeline.engine import answer_question_pipeline_debug
from app.core.locale import resolve_locale
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from app.pipeline.input_recovery import inspect_surface_input
from app.booking.live_status import _unavailable
from tools.run_master_ground_truth_eval import actual_status
g=RuntimeInputQualityGuard.from_environment();cases=[]
def add(q,l,group,must=(),forbid=(),source='',outcome='answer',not_category=''):
    cases.append(dict(id='G-%03d'%(len(cases)+1),question=q,locale=l,group=group,must_contain=list(must),must_not_contain=list(forbid),required_source=source,outcome=outcome,not_category=not_category))
for q in ['Counter-Strike 2 ต้องส่งผู้เล่นหลักกี่คน','CS2 ส่งผู้เล่นกี่คน','CS2 ต้องมีผู้เล่นหลักจำนวนกี่คน','CS2 ผู้เล่นตัวจริงกี่คน']:
    add(q,'th','team_roles',['ผู้เล่น 5 คน'],source='competition_rules_cs2_psu_phuket_2026')
for q in ['How many starting players must a CS2 team send?','How many starters does CS2 need?','What is the number of starting players for CS2?']:
    add(q,'en','team_roles',['5 players'],source='competition_rules_cs2_psu_phuket_2026')
for q in ['CS2 เลทแล้วเปลี่ยนตัวตอนหน้างานได้ไหม','CS2 เปลี่ยนตัวผู้เล่นได้ไหม','CS2 สลับผู้เล่นระหว่างรายการได้ไหม','CS2 เปลี่ยนสมาชิกในทีมได้หรือเปล่า']:
    add(q,'th','roster',['ไม่มีการเปลี่ยนแปลงสมาชิก'],['โน้ต'],source='competition_rules_cs2_psu_phuket_2026')
for q in ['Can a CS2 team replace players on site?','Can we swap CS2 starters?','Can CS2 teams change members during the tournament?']:
    add(q,'en','roster',['member changes'],['notes'],source='competition_rules_cs2_psu_phuket_2026')
for q in ['วาโลต้องปิดเลือดกับศพไหม','VALORANT ต้องปิดเลือดไหม','วาโล ปิดศพด้วยหรือเปล่า','กฎวาโลตั้งค่า Blood กับ Bodies ยังไง']:
    add(q,'th','display_settings',['ปิด','เลือด','ศพ'],source='competition_rules_valorant_psu_phuket_2026')
for q in ['Do I need to turn off blood and bodies in VALORANT?','VALORANT blood display settings?','Should VALORANT bodies be off?']:
    add(q,'en','display_settings',['OFF','blood','bodies'],source='competition_rules_valorant_psu_phuket_2026')
for q in ['RoV มาสายเกิน 15 นาทีเป็นอะไร','RoV เริ่มแข่งช้าเกิน 15 นาทีจะโดนอะไร','กฎ RoV ถ้าเริ่มเกมช้ากว่าเวลาที่กำหนด 15 นาทีล่ะ']:
    add(q,'th','late_conditional',['15 นาที','ปรับแพ้'],source='competition_rules_rov_blueket_2025_men')
for q in ['What if a RoV team arrives late by over 15 minutes?','RoV starts more than 15 minutes late: what happens?']:
    add(q,'en','late_conditional',['15 minutes','forfeit'],source='competition_rules_rov_blueket_2025_men')
for q,l in [('CS2 เปลี่ยนตัวละครยังไง','th'),('CS2 เปลี่ยนสกินได้ไหม','th'),('Tekken 8 เปลี่ยนตัวละครยังไง','th'),('VALORANT มีตัวละครอะไรบ้าง','th'),('What games are available?','en'),('How do I change my character in Tekken 8?','en'),('PC 1 หรือ 2 ชั่วโมงกี่บาท','th'),('VR 30 or 60 minutes cost?','en')]:
    add(q,l,'negative_context',outcome='',not_category='competition_rules')
for q in ['ปุ่ม','เพลย์ห้าคิกตังเท่าไหรอะ','วันนี้เปืดั้ย','พลย์ห้าคิดตังเท่าไหรอ่าา','ติดต่าทาไงหน','วีอาราค่าเทาไหร','เพลย์ห้าคิดตังเท่าไหรอ่าา','เพลย์ห้าคิดตังเท่าไหรอะ']:
    add(q,'auto','ingress_locale',outcome='')
add('ฟสสนไำก','auto','true_wrong_layout',outcome='clarification')
fixture=R/'focused_fixture_G_new_v2.json'
if not fixture.exists():
    with fixture.open('x',encoding='utf-8') as f:json.dump({'cases':cases,'scope':'source-derived content and negative controls; not owner approved'},f,ensure_ascii=False,indent=2)
else:assert json.loads(fixture.read_text(encoding='utf-8'))['cases']==cases
records=[]
with (R/(run+'_competition_G_details.jsonl')).open('x',encoding='utf-8') as out:
    for c in cases:
        q=c['question'];quality=g.inspect(q);surface=inspect_surface_input(q)
        # Exercise the actual server binding for each package version.
        direction=getattr(quality,'locale_layout_direction',quality.features.layout_direction)
        decision=resolve_locale(q,requested=c['locale'],keyboard_layout_direction=direction,surface_language=surface.language if surface.should_review_intent else None)
        with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled test fixture',error_code='fixture_offline')):
            result=answer_question_pipeline_debug(q,locale=c['locale'],locale_decision=decision,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
        errors=['missing:'+v for v in c['must_contain'] if v.casefold() not in result.answer.casefold()]+['forbidden:'+v for v in c['must_not_contain'] if v.casefold() in result.answer.casefold()]
        if c['required_source'] and not any(c['required_source'] in str(row) for row in result.hits):errors.append('wrong_source')
        if c['outcome'] and actual_status(result.mode,result.answer,result.route.category)!=c['outcome']:errors.append('wrong_outcome')
        if c['not_category'] and result.route.category==c['not_category']:errors.append('false_competition_context')
        if c['group']=='ingress_locale' and decision.effective!='th':errors.append('incorrect_english_locale')
        if c['group']=='true_wrong_layout' and 'keyboard_layout_mismatch' not in quality.flags:errors.append('missed_true_layout')
        if not result.validation.ok:errors.append('validation_rejected')
        row={'case':c,'answer':result.answer,'mode':result.mode,'category':result.route.category,'hits':result.hits,'trace':[vars(x) for x in result.trace],'locale':vars(decision),'failures':errors,'elapsed':result.elapsed}
        records.append(row);out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush()
        if errors:print(json.dumps({'q':q,'answer':result.answer,'failures':errors},ensure_ascii=False),flush=True)
summary={'total':len(records),'passed':sum(not row['failures'] for row in records),'scope':'new confirmed competition facets and HTTP-equivalent locale binding; typed content, not owner confirmation'}
with (R/(run+'_competition_G_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary),flush=True)
