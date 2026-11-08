"""Build transparent cross-version comparisons from preserved actual outputs."""
import collections,json
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf-8-sig'))
def lines(p):return [json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()]
def link(p,label=None):
 p=Path(p);p=p if p.is_absolute() else R/p
 return '['+(label or p.name)+'](<'+p.resolve().as_posix()+'>)'
teacher=lines(R/'teacher02/RESULTS.jsonl');base=lines(R/'candidate04_final/RESULTS.jsonl');focused=lines(R/'candidate05_final_checks/RESULTS.jsonl')
api_config=read(R/'LIVE_API_PROCESS.json');api_dir=Path(api_config['output']);api=read(api_dir/'LATEST_API_PROBES.json');api_ver=read(api_dir/'LATEST_API_VERIFICATION.json')
assert api_ver['all_passed'] and len(api)==13 and 'revision05_system' in api_config['candidate']
old={x['key']:x for x in teacher};new={x['key']:x for x in base};targeted={x['key']:x for x in focused};actual_api={x['key']:x for x in api if x['key']}
assert set(old)==set(new) and len(old)==61
notes={
'ef5c0b5a':'อ่าน CS2 clause เต็มเรื่อง brightness/resolution/crosshair; สะกดผิดไม่ควรเปลี่ยนเจตนาหรือขยายสิทธิ์นอกเกม/จอ',
'2d97cb1b':'teacher ไปตอบแนวเกม Sports; ใหม่ผูกอุปกรณ์ Nintendo ได้ แต่ความครบทั้งโซนยังไม่พิสูจน์ จึงคง partial',
'd91ee50a':'แยกปุ่ม Tekken กับราคา PC; source มี 12 entries ไม่ระบุ subset 8 ปุ่ม จึงถามเพิ่มเฉพาะส่วนปุ่ม; teacher ตกส่วน controls',
'490a5b13':'สิทธิ์ผู้ใช้ภายนอกทั่วไปต้องไม่เอา eligibility แข่ง CS2 มาปน',
'e57f0296':'คำตอบนำอาหาร/เครื่องดื่มเข้าได้มีอยู่เดิม; projection/topic ทำให้เข้าไม่ถึง แก้แล้วและทดสอบถอน/แก้ source แบบ memory',
'0a00000d':'โจทย์ถามต้องเลือกบริการใดเพื่อเล่น FF16 ไม่ใช่ขั้นตอนจอง; ใช้ game→offering',
'a603ab1a':'สอง task booking+weekly calendar; อ่าน typed calendar ก่อน model selection; weekly list ยังมี completeness qualification',
'1cf7db38':'เจตนาถามเอกสาร ไม่ใช่สิทธิ์บุคคลภายนอก; source หลายรุ่นให้รายการเอกสารไม่เหมือนกันทั้งหมด เก็บ scope ไม่แต่งรวมสิทธิ์',
'044f6671':'เลือก General Adult/PS5/120 นาที คำนวณจาก rate และ owner confirmation วันที่20 ไม่สร้าง effective interval ใหม่',
'1806def7':'filter เกมหลายโซนจาก explicit relations; ไม่เอาทั้ง catalogue มาตอบ; ความครบทุกเกมยังไม่พิสูจน์',
'8570a28b':'เลือก zone relation ของ Tekken8 เท่านั้น ไม่ใช่ catalogue ทั้งโซน',
'9813e160':'รายการ controls จาก source binding set; complete ในขอบเขตข้อมูลที่บันทึก ไม่ใช่ยืนยัน installed preset',
'9efbf2ac':'permission ถ่ายคน/ห้องยังไม่มี source ยืนยัน; คำอนุญาต capture ภาพในเกมไม่ได้ให้สิทธิ์ filming ภายในศูนย์โดยอัตโนมัติ',
'a9ecf2e1':'maintenance เป็น facet แยกจาก open_periods conflict; ไม่ทิ้งตาราง maintenance ที่ยืนยันได้',
'b2ff4f05':'อ่าน bindings ทั้งชุดพร้อม source coverage note; ไม่อ้างว่าได้ตรวจ preset เครื่องจริง',
'f10707b2':'วันอังคารเวลาเล่น09–12,13–16 แยกจาก dashboard open09–16',
'00301c15':'คืน query profile จากข้อมูลเดิมให้เข้าถึงนโยบายระงับสิทธิ์ชั่วคราวพร้อมเงื่อนไข',
'0d05eaf6':'adult VR60 นาทีต้องเลือก rate60 ไม่ใช้30นาทีคูณโดยไม่มี declared arithmetic',
'0f5e0fd0':'R03ตีคำถามมีเมาส์ไหมเป็น list และเตือนความครบเกินจำเป็น; R05แก้เป็น detail ของอุปกรณ์ที่ผูก source ได้ ไม่ยืนยันเครื่องว่างจริง',
'104194c2':'teacherอ่านเพียงบางโทษ; ใหม่อ่าน source section family ครบ5ประเภทพร้อมขอบเขตรายการแข่ง',
'11f9129c':'คืน profile คำถามพบปัญหาเครื่องให้เลือกแจ้งเจ้าหน้าที่จาก native policy',
'1f7c4f9a':'เกม→โซน Nintendo จาก offering; ไม่เดาจากชื่อแพลตฟอร์ม',
'2204b0a8':'ศุกร์ maintenance13–16 ใช้ source calendar facet ตรง',
'2c110689':'R03 binding effective ถูกเทียบกับ semantic date21ก่อนbindingcreated23จน false mapping gap; R04แยก binding/freshness clock เป็น wall clock และเก็บ booking date แยก; ผล live ต่างเวลาห้ามเทียบเป็น accuracy',
'2ee7827c':'ชื่ออังกฤษกับ role ผูก native profile ได้; source-version difference และ recorded role ไม่ยืนยันปัจจุบันทุกกรณี',
'3020765f':'ใช้ canonical center address เก็บอาคาร5ชั้น1ไม่ตกจาก generic FAQ',
'36c23990':'booking procedure มีหลาย source variants; ตอบข้อความที่มีแต่ยัง wordy/partial ไม่อ้างว่ามี authority reconciliation สมบูรณ์แล้ว',
'3a769b08':'เลือก game summary ไม่ใช่บริการ/controls',
'3cc3c5c3':'R03 single-letter parser เลือก R ท้าย Shift+Q/W/E/R; R04เลือก whole recorded compound ก่อน single key ยืนยันผ่าน API',
'3df1eea3':'อุปกรณ์→location PC Zone จาก current native record',
'4b0fb4a4':'explicit AOV competition context ต้องอ่านอุปกรณ์การแข่งขันพร้อมข้อห้าม/เงื่อนไขจาก event เดียว',
'546c4490':'Beat Saber→VR rates แสดง audience/duration options ไม่เดาราคาหนึ่งเดียวเมื่อโจทย์ไม่ระบุ',
'5b2d0e13':'presence ในโซนที่ระบุอ่าน offering ตรง ไม่ใช่ live vacancy',
'69812416':'เปิดตอนนี้เป็น recorded play calendar ไม่ใช่ live machine occupancy; runtimeจริงใช้วัน23 ส่วน CLI reference21 จึงไม่เทียบคำตอบ literalข้ามclock',
'6d26c7fe':'cancellation policy ตามเวลาแจ้งล่วงหน้า ไม่เพิ่มrefund/rescheduleเอง',
'6f6cb1e0':'keyboard→location source',
'790d4406':'จันทร์เช้า maintenance09–12 ไม่อนุมานจาก dashboard open12–16 ว่ารอบเล่นเริ่ม12',
'83ff647f':'teacherสับสน checkin เล่นVALORANT กับ checkinการแข่งขัน; ใหม่เลือก studio checkin action ก่อนgame context',
'88b3a23b':'native GPU sourceใหม่RTX5060; teacherไม่มีคำยืนยันเดียวกัน จึงไม่ใช่ causal gainจากFlowล้วน',
'8acac2d3':'R2ตรงแพลตฟอร์มและmodifier L1; เก็บคำเตือนsecondary source/installed preset',
'96ef8f71':'HadesIIไม่มี sourceยืนยัน ไม่ควรแทนเกมใกล้ชื่อหรือสรุปไม่มีบริการถาวร',
'981fa8d4':'fragmentที่อยู่แบบไม่มี referent อื่นใช้ center address; unknown named subject มี guard ไม่ตอบที่อยู่ศูนย์แทน',
'9be5826b':'R03 map poolถูกตีC03; R04ให้event-ruleก่อนequipment และอ่านheading+numberedchild7maps ไม่รับheadingล้วนเป็นคำตอบครบ',
'9db7acd1':'รองรับ X buttonและbutton X โดยเลือกbindingจริง ไม่ไปgamepresence',
'a1c90b6e':'PartI/PartIIแยกเป้าหมาย; PartIIฐานยังไม่มีofferingedgeที่เท่ากับRemastered จึงคงpartial ไม่รวมeditionเอง',
'a87e6d58':'Cockpit ratesทุกaudienceตามsource เมื่อไม่ระบุผู้ใช้ ไม่เลือกแพ็กเกจเหมาแทน',
'aefe9911':'fragmentเครื่องดื่มพื้นที่อ่านconsumption policyไม่ใช่bring permission',
'b32fb6ba':'ศุกร์บ่ายmaintenance13–16 ไม่ใช้rawopen_periodsที่ขัดกันตอบ',
'c43bbed1':'PC70บาท/60นาทีสำหรับGeneralAdult พร้อมsourceconfirmationและรายการPCที่มีrateเท่ากัน',
'c8d9c78f':'Sunday regular play closed ตามตาราง ไม่ใช่ยืนยันspecialevent/liveทุกกรณี',
'da13326d':'R03ตอบNintendo catalogueกว้างเกินโจทย์; alias overcookedชนOvercooked!กับOvercooked2 แก้R05ถามeditionจากชื่อในsource ไม่เลือกแทน',
'df43bd38':'LittleNightmaresII→NintendoZoneจากoffering; controlsPS5sourceไม่ได้เป็นหลักฐานว่ามีPS5serviceติดตั้งเกมนี้',
'e7a3582e':'คืนprofileข้อความของหาย/อุปกรณ์เปียก รักษาเงื่อนไขความรับผิดตามsource',
'e8694671':'inverse role→peopleจากnativepublicprofile ไม่สลับชื่อกับหน้าที่',
'eafe23b9':'sourceมีเพียงpartialofficial ไม่ใช่fullbuttonlayout; R04เปลี่ยนterminalเป็นpartial แม้ส่งครบrowsที่มี',
'f683a42c':'whichdevicecanplay→gameofferedservices ไม่ใช่การบอกhardwarecompatibilityทั่วไป',
'42582c1e':'definitionอุปกรณ์OLED→usage ไม่ใช่nameechoหรือข้อมูลเกมแทน',
'c7ef53bc':'PSUStaffPS5120นาทีตามrate0บาท/คน รักษาaudienceไม่ใช้GeneralAdult',
'8711c0d5':'ศุกร์บ่ายตอบปิดช่วงเล่นเพราะmaintenance13–16แบบscopeชัด',
'5d18afc2':'genericcontrollerusage→recordedbindinglistพร้อมplatform/sourcequalification ไม่สรุปinstalledmappingใหม่',
'dcddcfd2':'consumptionเฉพาะพื้นที่กำหนด ไม่ทำให้bringpermissionกลายเป็นห้ามนำเข้า'
}
def evidence(result):
 art=result.get('decision_artifact') or {};sources=[];paths=[]
 for h in result.get('hits') or []:
  sources.append({'hit_id':h.get('id'),'metadata':h.get('metadata',{})})
 for n in art.get('need_results',[]):
  for c in n.get('claim_packets',[]):sources.append({'record_id':c.get('record_id'),'fact_id':c.get('fact_id'),'evidence_refs':c.get('evidence_refs',[])})
 for t in result.get('trace') or []:
  if t.get('stage')!='timing':paths.append({'stage':t.get('stage'),'decision':t.get('decision'),'detail':t.get('detail'),'metadata':t.get('metadata')})
 return {'sources':sources,'route':result.get('route'),'observable_trace':paths,'execution_contract':art.get('execution_contract'),'need_results':art.get('need_results')}
rows=[];md=['# เทียบ Flow เดิมกับ R124 รายข้อ','', '61 unique retained development questions; ตารางนี้รวมหลักฐานต่าง revision ไม่ใช่ผลรัน61ข้อครั้งเดียวของR05 และไม่ใช้แทนเปอร์เซ็นต์ความถูกต้องทั้งระบบ','',
'ฐานเปรียบเทียบ: teacher02 กับ candidate04_final(R03) ใช้reference clock21ตุลาคม12:00; focused14ใช้R04ก่อนแก้mapbodyขั้นสุดท้าย; APIล่าสุดใช้R05และเวลาจริง23ตุลาคม รายข้อระบุ provenance เสมอ','']
for i,b in enumerate(base,1):
 key=b['key'];t=old[key];current=targeted.get(key,b);scope='candidate05_final_checks / R04 targeted CLI' if key in targeted else 'candidate04_final / R03 selected61 CLI';result=current['result'];origin=R/('candidate05_final_checks' if key in targeted else 'candidate04_final')/'RESULTS.jsonl'
 if key in actual_api:result=actual_api[key]['pipeline'];scope='revision05_system / actual latest HTTP API / real clock';origin=api_dir/'LATEST_API_PROBES.json'
 note=notes[key[:8]];te=evidence(t['result']);ne=evidence(result)
 row={'key':key,'question':b['question'],'locale':b['locale'],'review_note':note,'teacher':{'result':t['result'],'evidence':te,'raw_file':str(R/'teacher02/RESULTS.jsonl')},'r03_original':{'result':b['result'],'raw_file':str(R/'candidate04_final/RESULTS.jsonl')},'latest_available':{'scope':scope,'result':result,'evidence':ne,'raw_file':str(origin)}};rows.append(row)
 ids=list(dict.fromkeys(str(s.get('record_id') or s.get('hit_id')) for s in ne['sources'] if s.get('record_id') or s.get('hit_id')))
 md += [f'## {i}. {key[:8]}','',b['question'],'',f'**วิเคราะห์:** {note}','',f'**ผลใหม่ที่แสดง:** {scope}','', '**คำตอบเดิมจริง**','', '```text',t['result'].get('answer',''),'```','', '**คำตอบใหม่ล่าสุดที่มีหลักฐาน**','', '```text',result.get('answer',''),'```','', '**Source IDs ที่เลือก:** '+(', '.join(ids) or 'ไม่มี selected claim; ดูเหตุผล bounded response ใน JSON'),'', '**เส้นทางเดิม:** '+str(t['result'].get('mode'))+'; **เส้นทางใหม่:** '+str(result.get('mode')),'',link(origin,'หลักฐานผลใหม่')+' · '+link('teacher02/RESULTS.jsonl','ผลเดิมและtrace')+' · '+link('CASE_COMPARISON.json','source refs / contracts / trace ฉบับเต็ม'),'']
(R/'CASE_COMPARISON.json').write_text(json.dumps({'unique_keys':61,'single_revision_final61_run':False,'fresh_holdout':False,'accuracy_percent':None,'rows':rows},ensure_ascii=False,indent=2),'utf8')
(R/'CASE_COMPARISON_TH.md').write_text('\n'.join(md),'utf8')
# Select latest successful invariant checks, never conceal failed earlier probes.
groups=[('foundation','verification_*',35),('live','live_verification_*',16),('source guards','source_guard_verification_*',19),('stable FAQ','exact_faq_verification_*',5)]
gates=[]
for label,glob,count in groups:
 paths=sorted(R.glob(glob),key=lambda p:p.stat().st_mtime,reverse=True)
 found=next((p/'VERIFICATION.json' for p in paths if (p/'VERIFICATION.json').exists() and read(p/'VERIFICATION.json').get('all_passed')),None)
 assert found;data=read(found);assert len(data['checks'])==count
 gates.append({'label':label,'checks':count,'file':str(found),'all_passed':True})
runmd=['# ผลดำเนินงานและการตรวจ R124','', '## ผล pipeline จริงที่เก็บไว้','', '| ชุด | ระบบ | จำนวน | สถานะ |','|---|---|---:|---|']
for name,label in [('teacher01','legacy pilot'),('candidate01','early candidate pilot'),('teacher02','legacy baseline'),('candidate02','candidate iteration'),('candidate03','R03 focused'),('candidate04_final','R03 selected full61'),('candidate05_final_checks','R04 focused14')]:
 p=R/name/'COMPLETE.json'
 if p.exists():
  c=read(p);runmd.append(f"| {link(p,name)} | {label} | {c.get('questions')} | completed={c.get('complete')}; LLM allowed={c.get('llm_allowed')} |")
runmd += ['', 'คำว่า full61 ในชื่อข้างต้นหมายถึงครบชุดคัดเลือก61ข้อ ไม่ใช่ Full Test20554keys/55811grades. Source framesที่ชัดใช้0generationcallsได้แม้LLMON ไม่ได้บังคับโมเดลทุกข้อ. การprofile function callsเพิ่มlatency จึงไม่ใช้เวลาCLIเป็นเวลาproductionAPI','', '## HTTP API รุ่นสุดท้าย','', f"R05: {api_config['url']} · {len(api)} requestsจริง =3liveWordPress+10retained · verification {len(api_ver['checks'])}/{len(api_ver['checks'])}", '',link(api_dir/'LATEST_API_PROBES.json','คำตอบและnativepipelineจริง')+' · '+link(api_dir/'LATEST_API_VERIFICATION.json','API checks')+' · '+link(api_dir/'HEALTH_VERIFIED.json','runtime health'),'', 'ข้อมูลสดเป็นbookingserviceที่providerรายงานพร้อมclock/cache/สถานะปิด ไม่ใช่การตรวจหน้างานทุกเครื่อง. Providertransport, modeltransport และคำตอบถูกต้องเป็นคนละเรื่อง','', '## Invariant gates','', '| Gate | ผ่าน | หลักฐาน |','|---|---:|---|']
for g in gates:runmd.append(f"| {g['label']} | {g['checks']}/{g['checks']} | {link(g['file'])} |")
runmd += ['', 'รวม75 invariant assertions ไม่ใช่accuracy75คำถาม และไม่ใช่100%semanticaccuracy. FAQ54question-languagepairsเป็นการเข้าถึงsource ไม่ใช่holdout. Live16checksใช้controlledaggregatefixturesแยกจาก3realWordPresscalls','', '## การแก้ที่ตรวจพบระหว่างรัน','', '- เก็บผลR03ที่mapไปอุปกรณ์, modifierถูกลดเหลือR, historicalbinding falsegap ไว้ ไม่แก้logย้อนหลัง','- R04แก้mapก่อนequipment, heading+child7maps, chordidentity, bindingwallclock และpartialofficial','- R05แก้inventoryexistenceไม่เป็นcollection และaliasหลายeditionให้ถามเลือก ไม่ส่งNintendocatalogueทั้งชุด','- API R05รอบแรกเก็บfailureedition_clarification=falseไว้ แล้วแก้source matching/routeและเปิดprocessใหม่; startupครั้งหนึ่งWinError10061เพราะhealthเรียกก่อนserverพร้อม ไม่มีคำถามส่งสำเร็จในattemptนั้น','', '## ขอบเขตและงานที่ยังมีข้อจำกัด','', '- ยังไม่มีคะแนนFullTestใหม่หรือfreshholdout จึงยังบอกไม่ได้ว่าเท่าหรือดีกว่าlegacyทั้งระบบกี่เปอร์เซ็นต์','- teacherกับcandidateต่างmodelprofile/sourceversion; GPU/roleใหม่ไม่ใช่causalgainของFlowล้วน','- open_periodsจริง5วันยังขัดกัน เก็บrawsourceไว้และตอบจากrecordedplaycalendar','- HadesII, physicalfilmingpermission, exactinstalledpreset และความครบทุกcollectionยังต้องsourceยืนยัน','- bookingprocedureหลายvariantsยังซ้ำ/ยาว และPartIIฐานกับRemasteredยังไม่รวมrelationเอง','- candidateใช้draftmigrationpreview ไม่ownerapprovedpublication และไม่ติดตั้งทับR78','',link('FINAL_PACKAGE_REVISION05.json','ตรวจoriginal/frozen unchanged')+' · '+link('FINAL_SOURCE_REVISION05.json','final hashes')]
(R/'RUN_RESULTS_TH.md').write_text('\n'.join(runmd),'utf8')
p=R/'REPORT_TH.md';text=p.read_text('utf8').replace('ตัวใช้งานใหม่: `revision03_system`','ตัวใช้งานใหม่: `revision05_system`').replace('รุ่นล่าสุดอยู่ใน `candidate04_final`','R03ครบชุด61ข้ออยู่ใน `candidate04_final`; R04ตรวจเฉพาะ14ข้อ และ R05ตรวจ APIล่าสุด13ข้อ ตาม RUN_RESULTS_TH.md').replace('[FINAL_SOURCE_FREEZE.json](FINAL_SOURCE_FREEZE.json)','[FINAL_SOURCE_REVISION05.json](FINAL_SOURCE_REVISION05.json)').replace('[FINAL_PACKAGE_CHECK.json](FINAL_PACKAGE_CHECK.json)','[FINAL_PACKAGE_REVISION05.json](FINAL_PACKAGE_REVISION05.json)')
text+='''

## 15. การแก้หลังเทียบครบ61ข้อ

- Map pool CS2: จัดลำดับบริบทกติกาก่อนคำว่า “คืออะไร” ของอุปกรณ์ แล้วอ่านหัวข้อพร้อม child clause ที่มี7แผนที่ ไม่รับหัวข้อเปล่าเป็นคำตอบครบ
- Binding controls: ให้ชื่อ compound ทั้งชุดมีลำดับก่อนตัว R ท้ายข้อความ “Shift + Q / W / E / R button”
- เวลา: binding validity และความสด provider ใช้ wall clock แยกจากวันที่ต้องการตรวจbooking
- Partial official controls: ส่งครบแถวที่มีไม่ได้หมายถึงมี full layout; คงสถานะ partial และ source warning
- ถามมีเมาส์ไหม: อ่าน inventory detail ที่sourceรองรับ ไม่ตีเป็นรายการทั้งหมดและเตือนความครบเกินจำเป็น
- Alias edition: Overcooked! และ Overcooked2มีชื่อย่อชนกัน; R05ถามให้เลือกeditionจากsource แทนตอบNintendocatalogueหรือเดาedition

ทั้งหมดมี retained/source regression และ HTTP API evidence แยกรุ่นไว้ในรายงานผล ไม่ใช่คำยืนยันว่าแก้semanticทุกparaphraseได้แล้ว
'''
p.write_text(text,'utf8')
final={'status':'implemented_and_targeted_verified','candidate':api_config['candidate'],'api':api_config['url'],'legacy_actual_questions':61,'r03_actual_questions':61,'r04_actual_focused_questions':14,'r05_actual_api_requests':13,'invariant_checks':75,'gates':gates,'api_verification':str(api_dir/'LATEST_API_VERIFICATION.json'),'comparison':str(R/'CASE_COMPARISON_TH.md'),'full_test_started':False,'fresh_holdout_accuracy':None,'production_installed':False,'remaining_source_limits':['conflicted raw open_periods','some partial control layouts / installed preset unknown','unconfirmed collection completeness','some game edition offering edges','physical filming permission / Hades II not confirmed','booking source variants presentation']}
assert read(R/'FINAL_PACKAGE_REVISION05.json')['all_protected_unchanged']
for name in ['STATUS.json','FINAL_REVIEW.json']:(R/name).write_text(json.dumps(final,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'comparison_keys':61,'actual_latest_api':13,'invariant_assertions':75,'reports_written':True},ensure_ascii=False))
