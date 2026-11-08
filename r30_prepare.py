import json,sys,os,hashlib,subprocess,uuid,ast
from pathlib import Path
from datetime import datetime
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=project/'reports'/('r30_full_improvement_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);report.mkdir()
(root/'r30_report_path.txt').write_text(str(report),encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before={}
for dirname in ('app','tests'):
    for p in (project/dirname).rglob('*.py'):
        relative=p.relative_to(project);target=report/'before'/relative;target.parent.mkdir(parents=True,exist_ok=True);target.open('xb').write(p.read_bytes());before[relative.as_posix()]=sha(p)
protected={}
for dirname in ('data','booking_dashboard'):
    for p in (project/dirname).rglob('*'):
        if not p.is_file() or any(part in {'logs','__pycache__','question_bank_runs','audits'} for part in p.relative_to(project).parts):continue
        protected[p.relative_to(project).as_posix()]=sha(p)
for name,value in [('before_manifest.json',before),('protected_manifest.json',protected)]:
    with (report/name).open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8',check=True).stdout
(report/'git_status_before.txt').open('x',encoding='utf-8').write(status)
inventory=[]
for p in sorted((project/'data/eval').glob('*')):
    if not p.is_file() or p.suffix not in {'.json','.jsonl'}:continue
    try:
        if p.suffix=='.jsonl':rows=[json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
        else:
            value=json.loads(p.read_text(encoding='utf-8-sig'));rows=value if isinstance(value,list) else next((value[k] for k in ('cases','questions','records','items') if isinstance(value.get(k),list)),[])
        example=next((r for r in rows if isinstance(r,dict)),{})
        entry={'file':p.relative_to(project).as_posix(),'rows':len(rows),'sha256':sha(p),'keys':list(example),'sample':{k:example[k] for k in ('id','question','query','input','text','expected_route','expected_route_categories','expected_answer_status','answer_contract','locale','clean_question') if k in example}}
        inventory.append(entry)
    except Exception as e:inventory.append({'file':str(p),'error':str(e)})
test_inventory=[]
for p in sorted((project/'tests').glob('*.py')):
    if not p.name.startswith(('test_','smoke_test_')):continue
    tree=ast.parse(p.read_text(encoding='utf-8-sig'));test_inventory.append({'file':p.relative_to(project).as_posix(),'type':'smoke' if p.name.startswith('smoke') else 'unittest','sha256':sha(p),'classes':[n.name for n in tree.body if isinstance(n,ast.ClassDef)],'has_main':any(isinstance(n,ast.If) and '__main__' in ast.unparse(n.test) for n in tree.body)})
with (report/'test_inventory_initial.json').open('x',encoding='utf-8') as f:json.dump({'corpora':inventory,'scripts':test_inventory},f,ensure_ascii=False,indent=2)
flow='''# Flow r30 — วิเคราะห์ ปรับแก้ และทดสอบชุดทั้งหมด

## จุดตั้งต้นและลำดับความสำคัญ

1. P1 ราคาแบบหลายระยะเวลา: parserใช้durationเดียวทำให้ตัวเลือกที่เหลือหาย. เพิ่ม typed alternatives, ไม่เปลี่ยนราคา/สิทธิ์/VRbooking roundingpolicy.
2. P1 ปุ่มที่ถามเฉพาะ: lexicaldescriptionชนกับชื่อปุ่มหรือgame title; ให้ explicitbutton targetชนะและตรวจสิ่งที่ไม่ควรปน พร้อมsecondary-source note.
3. P1 จองเพื่อเล่นเกม: แยกบริการที่ต้องเลือกจากขั้นตอนจอง ใช้game→serviceจากcatalogเดิม; ไม่ส่งคำสั่งจอง/สร้างbooking.
4. P2 source gapกับmissingtranslation: route/rendererต้องไม่บอกว่าไม่มีคำแปลเมื่อจริงๆไม่มีpolicy. แสดงnoAnswerพร้อมคำถามเจ้าของที่ตรง ไม่เดาอนุญาต/ห้าม.
5. P1 evaluation: ต้องตรวจcontentครบ/ห้ามผิดเรื่อง/เลข/กลุ่ม/เงื่อนไข/แหล่งข้อมูล ไม่ถือrouteผ่านเป็นคำตอบถูก. เกณฑ์เก่าที่ขัดกับsourceแยกเป็นgraderissue ไม่แก้Goldต้นฉบับให้ผ่าน.
6. P2 failuretaxonomy/trace: inputguard→recovery→entity/intent→selectionscore→retrieval→render→validation→API. ทุกfailureต้องมีคำถาม/คำตอบจริง/expectedsource/เหตุผลที่เลือก/การแก้.

## ขั้นตอนทำงาน

1. สำรองapp/testsเดิมและhashruntime/eval/ownerdata; เก็บGitstatus. Inventorydatasetsและtestscriptsทั้งหมดก่อนเริ่ม.
2. ตรวจFlowหาจุดเสี่ยง: ตัวเลขช่วงเวลาvsduration, alternativesvscomparisons, negatedgroups, ปุ่มที่มีหลายชื่อ, gamefamilyambiguous, sourcegapvslocalization, ownerapproval.
3. สร้างsource-backed fixturesใหม่TH/ENพร้อมclean/noisy/negativecontrols. ทดสอบbaselineก่อนแก้และเก็บtrace. Expectationsต้องมาจากdata/confirmedpolicy ไม่ใช่คำตอบruntime.
4. แก้เฉพาะหลักฐานชัดทีละส่วน; retestและตรวจFlowหลังพบปัญหา. ไม่เพิ่มaliasทั้งประโยคเพื่อไล่จำชุดทดสอบ.
5. รันtest_*.pyทุกmodule, smoke_test_*.pyแยกprocessพร้อมtimeout/outputใหม่. Testที่ต้องบริการภายนอก/เขียนข้อมูลจริงใช้safe fixtureหรือระบุblockedพร้อมเหตุผล.
6. รันcorporaทั้งหมดที่มีquestion/expectation; JSON/JSONLซ้ำกันหรือTH/ENsplitsที่ตรงกับbilingualparentบันทึกaliascoverage. Historicalversionsยังgradeตามcontractของแต่ละรุ่น; ไม่รวมผ่านทับกัน. Guard-only/route-only/answer/contentreviewต้องแยก.
7. Bookingcorrectnessใช้knownfixtureพร้อมtestclockอย่างชัดเจน; real APIตรวจpath/transportเท่านั้นเพราะuserพักrealoracle. เก็บsource-conflicts/missing-owner-policyเป็นpendingไม่guess.
8. วิเคราะห์ทุกfailureแยกconfirmeddefect, unsupported/missingdata, staleGold/weakgrader, environment/dependency, timeout และambiguousinput. จัดอันดับตามseverity/count/blastradiusและลิสต์วิธีแก้.
9. แก้confirmeddefectsที่ทำได้จากข้อมูลในรอบนี้ แล้วรันrelevantcases+finalfullsweepหลังfreeze; optionaltestไม่วนซ้ำเมื่อไม่มีriskใหม่.
10. Buildpackageใหม่ → actualHTTPregressionไทย/อังกฤษ+newfixtures → hashprotection → เปลี่ยน8090เฉพาะownedlauncher → smoke → รายงานผลและข้อจำกัด. เก็บแพ็กเกจ/logsเก่า.

## เกณฑ์รับผลและสิ่งที่ห้ามสรุปเกินหลักฐาน

ต้องมีinventoryระบุทุกdataset/scriptว่ารัน/alias/notexecutable/blockedเพราะอะไร. ต้องแยกunit,smoke,guard,legacyGT,strongcontentcontracts,liveHTTPและhuman/ownerapproval. Synthetic/translatedGoldไม่ใช่เจ้าของรับรอง. หากมีfailureต้องรายงานจำนวน/หมวด/ตัวอย่าง/trace/expectedfact ไม่แปลงเป็นpassโดยแก้ต้นฉบับ. 8090เปลี่ยนได้เมื่อrelevantreleasegatesไม่มีnewwronganswerและknownlimitationsแสดงครบ.

## รายการที่ต้องเจ้าของให้ข้อมูล

Tekkenpauseconflict,RoV6.1.5.1ขาด,rulebookversion/scope,officialENnames,controllercounts/models,photo/video/public/foodpolicy,age/registrationfeeที่ไม่มีในsource. ใช้แบบฟอร์มเดิมและเพิ่มเฉพาะคำถามที่พบใหม่. Realbookingoracleยังพัก.
'''
for p in [report/'flow_initial.md',project/'docs/130_full_improvement_r30_flow_20261002.md']:
    p.open('x',encoding='utf-8').write(flow)
print(json.dumps({'report':str(report),'snapshots':len(before),'protected':len(protected),'datasets':len(inventory),'scripts':len(test_inventory)},ensure_ascii=False))
for entry in inventory:
    if entry['rows']:print(json.dumps({k:entry[k] for k in ('file','rows','keys')},ensure_ascii=False))
