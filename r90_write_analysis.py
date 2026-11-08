"""Problem taxonomy and side-by-side flow analysis from retained evidence."""
import ast,json,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;R=B/'r90_full_flow_analysis_20261018';C=B/'r88_full_common_llm_20261017/system';L=B/'r64_full_comparison_20261013/system'
M=json.loads((R/'DETAILED_METRICS.json').read_text('utf8'));D=json.loads((R/'DATA_INVENTORY.json').read_text('utf8'));PAIR=json.loads((B/'r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json').read_text('utf8'))
def link(root,rel,symbol=None,label=None):
 p=root/rel;assert p.exists(),p;line=1
 if symbol:
  found=[n.lineno for n in ast.walk(ast.parse(p.read_text('utf-8-sig'))) if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name==symbol];assert found,(p,symbol);line=found[0]
 return '['+(label or rel+(' :: '+symbol if symbol else ''))+']('+p.as_posix()+':'+str(line)+')'
def local(name,label=None):return '['+(label or name)+']('+(R/name).as_posix()+')'
def write(name,body):
 content=body.strip()+'\n';target=R/name
 if target.exists():
  assert target.read_text('utf8').rstrip()==content.rstrip(),('Existing artifact differs; preserve it',target)
  return
 with target.open('x',encoding='utf8') as f:f.write(content)
P=[]
def add(id,title,priority,status,count,stage,why,evidence,should,fix,verify,human,refs):
 P.append(dict(id=id,title=title,priority=priority,status=status,count=count,stage=stage,why=why,evidence=evidence,expected_behavior=should,solution=fix,verification=verify,human=human,source_refs=refs))
add('P01','เปลี่ยน data format พร้อมเปลี่ยนเส้นทาง interpreter โดยไม่ย้าย behavioral contract ครบ','P1','C: ยืนยันลำดับจากโค้ด; ผลกระทบทั้งระบบต้องแยกรายกรณี','ทั้ง20,554requestsเข้าprofileใหม่; ไม่ใช่จำนวนคำตอบผิด20,554','engine entry → migrated dispatcher',
'Engineใหม่ return migrated_answer ก่อน legacy request focus, cue preflight, typed fee/compound และ _answer_single ที่มีpreprocess/handlers จึงไม่เกิดความสามารถเดิมจากการมีข้อมูลเท่านั้น R87นำกลับบางส่วนแต่ยังไม่ใช่ parityทั้งต้นไม้',
'R87finalbridgesรวม202requests: intent16, rental5, equipment166, overview13, protest2; ชุดย่อย55/55ไม่ได้พิสูจน์ว่ากลุ่มอื่นผ่านด้วย',
'แยกการตีความงานออกจากfacts provider ให้task contractเดิมที่ยังถูกต้องส่งต่อไปcurrent common recordsได้ โดยรักษาowner source/validityใหม่',
'ทำadapterชั้นtask/operation/slots/qualifiers ไม่เรียกlegacy answer loader; map old output contractsไปschema/joinsปัจจุบัน; เลือกdomainที่มีช่องว่างจริงก่อน',
'ใช้คำถามเดิม/ใหม่คู่กันแล้วตรวจentity, operation, fields, qualifiers, output coverageและ source revision รวมnegative/ambiguous cases ไม่ใช้scoreรวมอย่างเดียว',
'ทำโค้ด/การวิเคราะห์เองได้; ไม่ต้องให้เจ้าของออกนโยบายใหม่',[('common','app/pipeline/engine.py','answer'),('common','app/pipeline/migrated_chat.py','answer')])
add('P02','การฟื้นคำผิดของ task cue ไม่ได้ถูกเรียกเหมือนเดิม','P1','C: มีคู่คำถาม+traceและตำแหน่งโค้ด','known-name+no-fields1,979requestsเป็นอาการที่เกี่ยวข้อง ไม่ใช่ทั้งหมดเกิดจากtypo','raw input → task normalization',
'เดิมมีkeyboard-neighbor/transposition/multi-error/cue/game variants ส่วนcommon normalizeกับschema-language recoveryคนละช่วงและคนละเงื่อนไข ชื่อเกมที่exactได้ทำให้ไม่ต้องfuzzyชื่อ แต่คำกริยาหรือชนิดคำถามยังผิดอยู่',
'Zelda “คือกมอะๆร”: entityตรง, operationNone, requested_fieldsว่าง, unresolved clauseยังอยู่ ข้อมูลsummary/genre/how_to_play/official_descriptionในฐานกลางknownแล้ว',
'ฟื้นความหมายของoperationโดยรักษาrawและedit trace ไม่แก้ชื่อเครื่อง ตัวเลข edition/วันที่/negationแบบเดา',
'แชร์pure recovery/task cue helpersของเดิมก่อนsemantic field selection พร้อมcandidate/margin/anchor protection ไม่เพิ่มaliasประโยคทีละข้อ',
'ตรวจdouble/delete/transpose/neighbor/multiple editsในtaskและentityแยกกัน มีhard-negativeชื่อคล้าย/PC1กับPC11/CS2กับVALORANT',
'ทำเองได้ในขอบเขตข้อความและfactsเดิม',[('legacy','app/pipeline/preprocess.py','preprocess_input'),('common','app/knowledge/common/query_contract.py','normalize'),('common','app/knowledge/common/answer.py','named')])
add('P03','Exact entity ถูกเข้าใจผิดว่าเข้าใจคำถามแล้ว','P1','C: ยืนยันจากaggregateและtrace','exact10,179; exactแต่ไม่มีrequested fields1,979; selected entityไม่มีfieldsรวม3,747','entity match → operation/field selection',
'exactแปลว่าพบชื่อ/alias ไม่ได้บอกว่าuserขอoverview, price, controls, permissionหรือstatus ตัวกลางยังอาจเหลือgenericfield menuแม้subjectแน่นอนแล้ว',
'Zeldaได้recordถูกแต่ถามชื่อเกมอย่างเป็นทางการ; SF-006ได้PCscopeแต่คำว่าอุปกรณ์ยังไม่ลงrender contract',
'ระบุobjectและtaskคนละslot แล้วตรวจว่ามีคำตอบสำหรับtaskที่ถาม ไม่เสนอmenuภายในเพียงเพราะรู้kind',
'เพิ่มtyped request contractที่มีoperation/needs/constraints/unknown slotsก่อนเลือกfield; field menuควรเกิดเมื่อuserยังไม่ระบุเจตนาจริงเท่านั้น',
'ชุดexact-name+clean task, exact-name+typo task, unnamed task, multi-target และshort followup ต้องเลือกทางต่างกันถูก',
'ทำเองได้',[('common','app/knowledge/common/answer.py','named'),('common','app/knowledge/common/query_scope.py','primary_ids')])
add('P04','Regex/priority ของเดิมไม่ได้กลายเป็นความหมายของaliasesโดยอัตโนมัติ','P1','C: source+R86audit; จำนวนผลเสียเฉพาะยังไม่แยก','legacy intent final16requests; routing stageพบ23events','trusted patterns → current FAQ',
'legacy matchercompilepatternและpriority ขณะที่common namedescapealiasเป็นliteral R87bridgeรับเฉพาะwhole-query coverageและunique currentintent รวมทั้งexcludeหลายoperation จึงมีขอบเขตต่างจากrouterเก่ามาก',
'R86พบregex-looking aliases61FAQ/308entriesในsnapshotที่auditไว้ ไม่ใช้ตัวเลขนั้นอ้างว่าทั้ง308กำลังตอบผิด R87FAQadvance timeแก้ได้ แต่ยังไม่ใช่ทุกparaphrase',
'routing configurationใช้เพื่อระบุtask ส่วนanswerอ่านจากcommon intent_key/sourceปัจจุบันเสมอ',
'ทำintent compiler/adaptorที่ประกาศcoverageและexclusionsชัด รองรับคำสุภาพ/กรอบคำถามแบบsemantic ไม่compileทุกowner aliasเป็นregex',
'เปลี่ยนanswerในDB/ถอนrecordแล้วrouterต้องไม่คืนanswerเก่า; patternชนกัน/หลายintentต้องถามเพิ่มอย่างจำเพาะ',
'ทำเองได้',[('legacy','app/rules/matcher.py','RuleMatcher'),('common','app/knowledge/common/legacy_intent_bridge.py','select')])
add('P05','Candidate recall และ independent-topic anchor ปิดทางก่อน LLM เห็น source','P1','C: policyในโค้ด; H: ไม่ใช่ทุก no_candidate เป็นfalse negative','global diagnostic audit no_candidate1,403 / no_independent_topic_anchor1,733; เป็นeventsจากตัววิเคราะห์เดิม ไม่ใช่requestไม่ซ้ำ','entity_search retrieval → pre-inference guard',
'boundedtrigram, excerptbudget, allowed kinds, numbered/broad/live gatesและtitle/topic overlapช่วยกันมั่วแต่ทำให้unseen wordingบางคำไม่ถึงโมเดล การมีคำตอบอยู่ท้ายfieldหรืออีกrelatedrecordไม่ได้รับประกันว่าจะได้candidate',
'entity_searchจำกัด8candidatesและtask backstop4, threshold.16; topic_alignmentระบุเองว่าไม่ใช่entailment/calibrated score',
'เพิ่มrecallจากschema/task/relationsโดยยังรักษาquoted subjectและanti-confusion constraints ไม่ส่งทุกfactsให้LLMแล้วเชื่อทั้งหมด',
'วัดcandidate recallจากsource IDsที่รู้ผล แยกsource absent, retrieval miss, preguard rejection, model selection errorเป็นคนละเหตุ; รองรับtopic metadataที่ownerไม่ต้องเขียนregex',
'ใช้held-out paraphrase, tail facts, similar-policy negatives และnew recordsที่ไม่เพิ่มชื่อในcode; เก็บretrieved/rejected IDsพร้อมreason',
'ทำเองได้จากfactsที่มี; factsใหม่ที่ยังไม่มีไม่ควรสร้าง',[('common','app/knowledge/common/entity_search.py','candidates'),('common','app/knowledge/common/entity_search.py','topic_alignment')])
add('P06','LLM schema ผ่าน แต่ semantic guard ปฏิเสธเพราะ lexical intent ยังไม่รู้จัก','P1','C: มีauditและcodeชัด; ไม่ใช่พิสูจน์ว่าทุกแผนที่rejectควรถูกรับ','schemaผ่าน2,623events; finalรับ129; rejected_unverified_intent2,494events','planner checked_plan → semantic_guard',
'schemaตรวจว่าชื่อfield/shapeถูก แต่semantic_guardยังต้องมีstrong typed needs ถ้าparaphrase/typoไม่อยู่ในgrammarก็reject ถึงโมเดลจะเสนอsummaryหรือgenreมาแล้ว ในทางกลับกันบางแผนโมเดลก็กว้างเกินจริงจึงไม่ควรรับทั้งก้อน',
'Zelda transport/schemaTrue แต่finalFalse reasonrejected_unverified_intent; Fridaymaintenanceถามpolicyแต่โมเดลเสนอquestionและถูกปฏิเสธ',
'รับแผนที่ผูกแต่ละclauseกับoperation/fieldที่มีความหมายได้จริง และตัดเฉพาะextra fields; คงguardต่อunsupported facts/unknown target',
'ปรับrequest semantic bindingและsharedcue normalization; แยกunknown wordingจากunrelated task ไม่ใช้การปิดsemantic_guardเป็นวิธีแก้',
'ต้องมีpositive paraphraseที่เคยrejectและnegative JSONถูกแต่intentผิด วัดschema acceptance/semantic acceptance/answer contentแยกกัน',
'ทำเองได้',[('common','app/knowledge/common/planner.py','semantic_guard'),('common','app/knowledge/common/planner.py','_plan_fields_batch')])
add('P07','LLM เลือก field กว้างหรือผิดหน้าที่ แม้ JSON ถูกต้อง','P1','C: ตัวอย่างauditจริง; H: สัดส่วนmodel semantic errorsยังไม่ตีตราทุกcall','ดูproposalรายcall ไม่เท่ากับ4,206schema accepted auditเป็นคำตอบถูก','schema prompt → field proposal',
'promptอนุญาตfieldหลายชนิดของselectedkindและchildren โมเดลอาจเลือกmetadata/publisher/edition/venueทั้งหมดแทนgameoverview หรือเลือกFAQ.questionแทนanswer รูปแบบถูกแต่taskยังผิด',
'Zeldaเสนอ12fieldsรวมpublisher_url/age_rating/profile_roleที่ไม่ได้ขอ; ResidentEvilVillage “ราคเท่าไหร่”เสนอ[]',
'เลือกminimal sufficient fieldsต่อclauseให้ครอบคลุมสิ่งที่ถามและqualifier ไม่เพิ่มall_fieldsเพราะไม่แน่ใจ',
'ให้task-to-field profilesที่ใช้ร่วมทุกrecordและตัวตรวจunrequested fields; metadataช่วยอธิบายความหมายfield ไม่ใส่factsที่โมเดลไม่จำเป็นต้องgenerate',
'assert must-answer needsและmust-not-answer extra fields ทั้งtemplatequestionsและคำถามใหม่ ไม่วัดแค่JSON/schema',
'ทำเองได้',[('common','app/knowledge/common/planner.py','_plan_fields_batch'),('common','app/knowledge/common/query_contract.py','resolve_fields')])
add('P08','คำถามผสมมีส่วนขาด แล้วคำตอบที่มีหลักฐานถูกทิ้งทั้งก้อน','P1','C: rejected_candidateและcomposition paths; H: ไม่ใช่700กรณีควรตอบทุกส่วน','rejected_candidateถูกเปลี่ยนเป็นsafe response700requests; compound final262requests','clauses → partial coverage → outer migrated guard',
'บางpathcomposeเป็นpartialได้ แต่บางpathมีunresolved_query_clauseจนvalidationไม่ผ่าน แล้วmigrated dispatcherเปลี่ยนทั้งคำตอบเป็นขอแยกถาม ผู้ใช้จึงไม่ได้ส่วนที่ตอบได้',
'Cockpit30minutes+“howdoIboo” มีknown price needsแต่bookingclauseขาด และมีvalidityอีกชั้น ต้องแยกเหตุไม่ใช่อ้างtypoอย่างเดียว',
'ถ้าส่วนใดตอบได้อย่างอิสระตามsource ให้ตอบพร้อมขอบเขต แล้วถามเฉพาะส่วนที่ยังไม่ทราบ; ถ้าdependencyทำให้ตอบส่วนแรกไม่ได้ต้องอธิบายdependency',
'กำหนดper-clause status/obligationsและatomicityตามความสัมพันธ์ ไม่ล้างทุกส่วนหรือแสร้งว่าครบด้วยการตอบclauseเดียว',
'mixedknown/unknown, negative correction, shared subjectต่างperiod/audience และconditional dependency ต้องไม่สลับslot',
'ทำเองได้ภายใต้factsเดิม',[('common','app/knowledge/common/composition.py','compose'),('common','app/pipeline/migrated_chat.py','answer')])
add('P09','ระดับ Zone/Service/Resource และ relation projection ยังไม่ตรงกับคำถามบางแบบ','P1','C: traceตัวอย่าง; H: ไม่ใช่ทุกliteralชื่อzoneไม่ตรงคือplatformผิด','source-selection/coverage/wordingกลุ่มหลัก516requests; เป็นกลุ่มผสม','primary IDs → relations → labels',
'ระบบอาจเลือกserviceที่สัมพันธ์กับเกมถูกแต่renderเป็นบริการ1-2/1-4Persons แทนzoneที่ถาม หรือrootมีrelationอุปกรณ์แต่requestedfieldsไม่ยอมprojectionไปequipment_model',
'ZeldaถามwhichzoneตอบNintendoสองบริการแต่ไม่พูดNintendoSwitchZone; SF-006relation_edgesพบอุปกรณ์PCแล้วแต่ยังveto',
'คืนข้อมูลตามระดับที่ถามและมีsource relationshipรองรับ ไม่สร้างzone membership/FKเองเพื่อให้มีlabelตามoracle',
'มีtask-specific projectionplanและsemantic roleของroot/child แสดงzone+serviceรายละเอียดเมื่อมีหลักฐาน; ห้ามใช้name similarityแทนrelation',
'zone↔service↔resource↔equipment↔game-service tests รวมno-FK/withdrawn/multi-platformและlabel equivalence',
'ทำเองได้ถ้ามีrelation/source grouping; mappingที่ไม่มีต้องยืนยันแหล่ง',[('common','app/knowledge/common/query_scope.py','primary_ids'),('common','app/knowledge/common/relations.py','related_attributes')])
add('P10','การผูกกลุ่มราคา หน่วยเวลา และบริการยังต้องแยกจากการงดตอบเพราะราคาเก่า','P1','C: sourceและplans; H:107diagnosticsไม่ใช่107ราคาคิดผิดที่ยืนยันแล้ว','price_scope_validity_or_wording107requests; regular rate18มีknownexpiry/6unknownvalidity','price needs → audience/rates → billing',
'คำถามอาจมีVR30เป็นชื่อpackageและ3ชั่วโมงเป็นเวลาที่เล่น ต้องไม่เลือกเลขแรกเป็นเวลาสุดท้ายเสมอ กลุ่มภายนอกทั่วไป/GeneralStudent/PSUต่างกัน การรู้gameไม่พอคำนวณราคาโดยไม่รู้service',
'ตัวอย่างGeneralStudent VR30นาที3ชั่วโมง: เดิมตอบ30นาที190บาทจากsourceเก่า ใหม่งดราคาปัจจุบันเพราะexpiry; ผลนี้ไม่ยืนยันduration parserของฝั่งใดว่าถูกทุกเงื่อนไข',
'แยกservice package duration, requested play duration, reserved occupancy และaudience แสดงunknownเฉพาะที่มีผลต่อจำนวนเงิน',
'ใช้billing contractระบุหน่วย/rounding/minimum explicit และsource revision; หากcontradictory durationให้ถามเจาะจง ไม่คูณเองจากราคาเก่าที่หมดอายุ',
'boundary30/60minutes,3h,หลายservice,ต่างกลุ่ม,expired/unknown validity พร้อมexpected priceที่มีsourceและreference date',
'parserทำเองได้; ราคาปัจจุบัน/วันที่มีผลที่ไม่มีหลักฐานต้องเจ้าของ',[('common','app/knowledge/common/billing.py'),('common','app/knowledge/common/audience_scope.py'),('common','app/knowledge/common/price_comparison.py')])
add('P11','ราคาเหมาอ่านได้แล้ว แต่ไม่ใช่ทุกเงื่อนไขการเช่ามีนโยบายให้ตอบ','P1/ข้อมูล','C: bridge/fixtureและinventory; D: unknownที่ถูกต้อง','24packages validityunknown; rentalbridgefinal5requestsในcorpusนี้','rental interpretation → current package + followup',
'คำว่าครึ่งวัน/เต็มวันในsourceไม่ได้ให้ชั่วโมงหรือเงื่อนไขmulti-day/hourly/custompackageเสมอ การเหมาexcludeVRบางรูปแบบไม่เท่ากับมีแพ็กเกจใหม่ที่เอาราคามาลบกันได้',
'R87fixtureแก้ราคา/เพิ่มAurora/ถอนpackageได้และรักษาPCexternalfull→half→internal แต่ไม่ได้ยืนยันevery rental paraphrase/ownerbookingterms',
'ตอบราคาที่บันทึกและscopeที่ตรง ชี้ว่าไม่มีข้อมูลชั่วโมง/การยกเลิก/มัดจำถ้าไม่มีsource ไม่คำนวณส่วนลดเอง',
'คงtuplecontractและdynamiccatalog เพิ่มgeneral paraphrasecoverageตามtask; ระบุunknown validity/termsเป็นdata readinessแยกจากcode',
'compoundtuples,customduration,PS6unknown,cancelstate,all-exceptและrevisionupdate/withdrawในisolatedfixtures',
'โค้ด/stateทำเอง; เงื่อนไขใหม่/จำนวนชั่วโมง/วันมีผลต้องมีsourceเจ้าของ',[('common','app/knowledge/common/rental_bridge.py','answer')])
add('P12','ข้อมูลเกมมีอยู่แล้ว แต่ overview/description operation ยังไม่ครอบคลุมรูปประโยค','P1','C: known field+traceครบ','ตัวอย่างZelda; ไม่ได้สรุปว่า51gamesผิดทุกเกม','game target → overview needs',
'known genre/summary/how_to_play/official_descriptionไม่ได้ช่วยถ้าoperationNoneหรือdefaultmenuมองว่าuserขอtitle field ตัวใหม่บางเกมตอบได้ในcleanwording แต่ไม่ยืนยันว่าtask recoveryครอบคลุมทุกเกม',
'DATA_INVENTORYบันทึกknownfieldsของZeldaและR89มีคำตอบเก่าที่อธิบายได้กับคำถามtypoเดียวกัน',
'เมื่อถามเกมอะไรควรใช้summary/genreที่มีsource ส่วนofficialdescriptionยาวให้ตามระดับรายละเอียดที่ขอ ไม่เผยage/publisherเพียงเพราะfieldมี',
'ทำgame-overview contractที่ไม่ผูกชื่อเกม ใส่requestfocusและlength/scopeprojectionจากtask ไม่เพิ่มaliasทุกชื่อ+ทุกประโยค',
'เปลี่ยนชื่อเกม/เพิ่มเกมใหม่/ไทยอังกฤษ/คำขาดเบิ้ลและaskingallvsbrief พร้อมassertsubstantivegenre/actiondescription',
'ทำเองได้จากsourceเดิม',[('common','app/knowledge/common/query_scope.py','primary_ids'),('common','app/knowledge/common/answer.py','answer')])
add('P13','ปุ่มและวิธีเล่น: action/mode mapping กับ completeness ไม่ใช่แค่ชื่อปุ่มปรากฏ','P1','C: schema/projectionและบางdiagnostics; H:ต้องอ่านcontentรายข้อ','43controlsets;9requestsอยู่กลุ่มหลักcontrol_projection_or_wording','control request → set/action bindings',
'ชื่อเกมกับplatformอาจตรงแต่mode/actionไม่ตรง การแสดงปุ่มบางส่วนไม่ใช่ครบทุกปุ่ม sourceบางชุดไม่เคยตรวจphysical mapping ต้องไม่เพิ่มคำยืนยันเอง',
'MarioKartLivebindingsectionมีthแต่ไม่มีen11จุด; R87MarioPartybuttoncaseผ่านแต่ไม่ครอบคลุมทั้ง43sets',
'ตอบactionที่ถามพร้อมbinding/เงื่อนไขของโหมด ถ้าขอทั้งหมดให้ครบscopeที่sourceมีและระบุpartialsource/mappingreview',
'มาตรฐานcontrolaction/mode/sourceclauseและcoveragecounter; รักษาunknowncontroller/missingmodeไม่สร้างmappingใหม่',
'singleaction/allbuttons/multi-mode/unknownplatform/partialset/Englishsectionและquestiontypos',
'โค้ดและแปลจากsourceทำเอง; physicalmappingที่ไม่ยืนยันไม่รับรองแทนผู้ตรวจ',[('common','app/knowledge/common/control_rows.py'),('common','app/knowledge/common/query_scope.py','control_projection')])
add('P14','กติกาแข่งขัน: เล่มถูกไม่ได้แปลว่าเลือก proposition/ข้อยกเว้นครบ','P1','C: source/clausesและdiagnostics; H:330ไม่ใช่จำนวนsemanticผิดทั้งหมด','330requestsในกลุ่มหลัก; English301/Thai29ตามdiagnostic','competition target → facet → clause projection',
'ขอบเขตปี/edition, facetและpropositionต่างกัน มีทางเลือกliteral source/topicที่ยังตอบส่วนใหญ่เกินหรือขาดconditions/penaltiesได้ R87overview/protestbridgeเป็นเพียงบางงาน',
'R88summarybridge13/protest2requests; TekkenetiquetteบางcaseขาดexactEnglishclauseทั้งที่sourceใช้คำแปลอีกสำนวน ต้องอ่านทั้งความหมายและcompletenessก่อนลงว่าเลือกผิด',
'ให้ครบทุกpropositionที่ถามและqualifier รวมdependencies ไม่เปลี่ยนเกมเอง; ถ้าไม่มีrulebookของเกมนั้นให้บอกขอบเขต',
'ใช้target-locked clausecontracts/relation graph, distinguishsummary/all/detail และsemanticequivalence checkที่ไม่ลบตัวเลข/negation/conditions',
'4rulebooks หลายfacet/compoundtopic,unknownedition,summaryvsall,consequence/exception,TH/ENparaphraseและtypo',
'โค้ด/การเลือกข้อทำเอง; เอกสารขัดกัน/รายการใหม่ที่ไม่มีsourceต้องผู้จัด',[('common','app/knowledge/common/query_scope.py','rule_selection'),('common','app/knowledge/common/competition_bridge.py','answer')])
add('P15','Open / bookable / Maintenance ยังมีความขัดแย้งใน metadata ที่ต้องแยกความหมาย','P1/ข้อมูล','C:5fieldsconflicted; มีownerconfirmationเดิมบางส่วนแล้ว','schedule7records; open_periodsconflicted5','schedule facts → day status / booking windows',
'migrationเก็บความต่างระหว่างdashboardกับchatcalendarเป็นconflict ห้ามเอาช่วงจองไม่ได้ไปสรุปข้อเท็จจริงอื่นที่ยังไม่ทราบ และห้ามลืมข้อมูลที่ผู้ใช้ยืนยันแล้ว',
'5conflict notesระบุopen/bookable/พักเที่ยง/Maintenance; ผู้ใช้ยืนยัน12–13ไม่มีให้จองและVR30กันชั่วโมงเต็มแล้ว',
'การตอบวันที่เปิดใช้service/bookableตามsourceที่ยืนยัน แยกวันMaintenance/เวลาเข้าพื้นที่/occupancy ไม่ตอบweekdaydebugแทนวันนี้วันที่...เปิด/ปิด',
'ทำseparate typed fieldsกับauthority mapping ใช้confirmationเดิมแก้ได้เท่าที่รองรับ ไม่ขอให้ยืนยันซ้ำเรื่องจอง12–13; คำถาม physical access ที่ยังไม่มีคำตอบค่อยถามเฉพาะประเด็น',
'ก่อน/ตรง/หลังขอบเวลา,bookablegap,Maintenance,TH/ENday/dateและavailabilityต้องไม่ขัดกัน',
'ทำmapping/ตรรกะเองได้; หากต้องระบุสิ่งอื่นนอกbookabilityที่ยืนยันแล้วต้องsourceเพิ่ม',[('common','app/knowledge/common/open_day.py','answer'),('common','app/calendar/service_calendar.py'),('common','app/knowledge/common/registry.py','validate')])
add('P16','วันปิดพิเศษ วันหยุด และวันที่อ้างอิงต้องมี precedence ที่สม่ำเสมอ','P1','C: date/closurecode; H:aggregateไม่ชี้ว่าทุกclosureผิด','closure3knownvalidity; bulkใช้reference16ต.ค.2026','relative date → calendar/closure precedence',
'วันนี้/พรุ่งนี้/weekdayกับclosure rangeไม่ควรยึดweekday FAQแทนวันที่จริง จุดเริ่ม/สิ้นสุดแบบexclusiveกับtimezoneมีผลต่อstatus',
'R88มีcalendar/date methodsแยกจากcompactopenstatus; fullbulkไม่ใช้วันที่18ต.ค.ที่อ่านรายงานเป็นreferenceทุกข้อ',
'ตอบวันที่ไทยและสถานะตามวันที่ถาม/closureที่ครอบ ไม่ใช้สถานะวันนี้ไปตอบวันอื่นและไม่อ้างliveoccupancyจากcalendar',
'รวมcalendardecisioncontractพร้อมsource precedence/affectedzones และtimebound ไม่ให้FAQทั่วไปoverrideข้อยกเว้นที่มีผล',
'closurestart/end,all-day/partialday,crossdate,unknownspecialholiday,ไทย/อังกฤษ และknownreferencecases',
'ตรรกะทำเอง; วันปิดใหม่ที่ไม่มีsourceห้ามเดา',[('common','app/knowledge/common/open_day.py','answer'),('common','app/calendar/service_calendar.py')])
add('P17','สถานะจองถูกจำลอง unavailable ในชุดใหญ่ จึงห้ามตีความว่า live จริงล่มหรือจองผิด','เงื่อนไขทดสอบ','D:ควบคุมโดยharness ไม่ใช่regressionoccupancy','live_unavailable1,074requests;18อยู่กลุ่มdiagnosticหลักนี้หลังจัดpriority','common defer → live adapter → controlled fixture',
'bulkตั้งget_live_booking_statusให้unavailableเพื่อไม่ให้เวลาทดสอบเปลี่ยนtruth การที่oracleอยากได้slotแต่ระบบตอบunavailableเป็นผลจากเงื่อนไขทดสอบนี้',
'RUN_SCOPE/runnerกำหนดfixture_offline; ผู้ใช้ยืนยันสถานะจริงถูกต้องมาก่อนแล้ว ไม่เปิดประเด็นเก็บtruthลูกค้าจริงใหม่ในรายงานนี้',
'แยกAPIreachable/schema validกับfree/booked correctness และเขียนevaluationconditionชัด ไม่อ้างfailure1074คือWordPressจริงเสีย',
'ใช้known-result staticbookingfixturesในการตรวจlogic และsourcevalidatedlivegroundtruthเฉพาะเมื่อพร้อม/ได้รับคำขอแยก',
'day/time/resource ranges,VR30fullhour,free-onlyallinventory,TH/EN และupstream unavailableแต่ไม่ใช้oldoccupancyแทนlive',
'fixtureทำเอง; ไม่ต้องให้เจ้าของยืนยันliveที่ยืนยันแล้วซ้ำ',[('common','app/booking/live_status.py','get_live_booking_status'),('common','app/booking/wordpress_status.py','fetch_wordpress_status')])
add('P18','ประวัติมาถึงแล้ว แต่ short follow-up ยังไม่กลายเป็น task ที่ตอบได้','P1','C: SF-006 traceพิสูจน์scopeและrelationsถูกส่งมา','sessions12/24turns; literalผ่าน23; positivecontract12turns','trusted history → state scope → follow-up operation',
'servercommonปิดlegacyrequest_planโดยตั้งใจแต่เก็บcommon_read_state SF006typed_common_stateมีPCservicesและrelationedges6อุปกรณ์ แต่คำว่าอุปกรณ์ไม่ผ่านfield/coverageguard ทำให้ไม่มีสาระตอบ',
'PCมีอะไรบ้าง→อุปกรณ์: stateไม่ได้หาย แต่requestedfieldsเลือกspecifications/usageและunresolved_query_clauseจึงouterveto',
'รับshortreplyในบริบทที่แยกambiguityได้แล้ว แล้วทำequipment-listprojectionของscopeเดิม ไม่ถามเกม/ราคาใหม่หรือทิ้งtargetโดยไม่มีเหตุ',
'ผูกofferedneed/pendingselectionกับcanonicaloperation ตรวจdeliveredstate/revision และปรับshortoperationcontractให้ตรงกับfullquestion',
'2–5turns เลือกชื่ออย่างเดียว/all/another/negative/cancel/changeaudience และไม่inheritเมื่อเปลี่ยนเรื่อง; HTTPและengineต้องรายงานแยก',
'ทำเองได้',[('common','app/web_api/server.py','do_POST'),('common','app/knowledge/common/dialogue.py','resolve_state'),('common','app/knowledge/common/equipment_bridge.py','answer')])
add('P19','Qualification และ unknown policy ต้องไม่ถูกแทนด้วยคำตอบใกล้เคียง','P1/ข้อมูล','C: code+fixture; D:การบอกunknownบางข้อถูกต้อง','specific_unconfirmed_request12methods;2requestsในกลุ่มหลักนี้','profile/task ownership → confirmed or unknown source',
'สลิปผิด≠ยืนยันตัวตนผิด≠ยอดเงินผิด นำอุปกรณ์ส่วนตัวใช้≠ให้ศูนย์เตรียมอุปกรณ์ การคล้ายคำไม่ให้ย้ายอำนาจsourceหรือทิ้งnegation',
'R87fixtureเพิ่มpolicyยอดเงินแล้วอ่านV1/V2/withdrawได้ แต่productionsnapshotยังไม่ใช่การอนุมัตินโยบายใหม่นั้น',
'ถ้าfactsเฉพาะไม่มีให้บอกว่าไม่ยืนยันเรื่องนั้น ถ้ามีsourceใหม่แล้วต้องไม่ติดoldunknowngate',
'ใช้typed task/subject/ownership/context/qualifier bindingsและcurrent-source-checkก่อนunconfirmed; yesยืนยันหัวข้อไม่ใช่อนุมัติfacts',
'slip/identity/amount/personal/competitionเงื่อนไขใกล้กัน newpolicyrevisionและwithdrawalไม่คืนค่าจากhistory',
'โค้ดทำเอง; นโยบายที่ยังไม่มีต้องownerหรือsourceจริง ไม่ใช้fixturesเป็นpolicyศูนย์',[('common','app/knowledge/common/qualified_reply.py'),('common','app/knowledge/common/unconfirmed_request.py'),('common','app/knowledge/common/legacy_intent_bridge.py','source_for_need')])
add('P20','ภาษาอังกฤษ: metadata, ค่าที่ขาด, proper names และคำแปลต้องแยกกัน','P1/ข้อมูล','C:scanknownvaluesและflags; H:Thai-characterflagไม่เท่ากับแปลผิด','agent_translated486records;metadata missing116;knownlocalizedobjectsไม่มีen11;Thai-in-en32objects;Englishanswerflag512requests','localized source values → English rendering',
'116คือrecord-levelstatus ไม่ใช่จำนวนrecordที่ไม่มีEnglishทั้งหมด 11actualmissingอยู่bindingsectionMarioKartLiveบางส่วน Thaiชื่อรายการ/หน่วยอาจติดflagแม้ไม่ใช่ประโยคที่ต้องแปล ส่วนclausetranslationอีกสำนวนทำให้literalfailได้',
'DATA_INVENTORYเก็บทุกmissingpathและen_thai_paths; Tekkenetiquetteมีsemanticใกล้เคียงแต่ถ้อยคำไม่ตรงoracle',
'อ่านEnglishsourceที่ผูกrevisionและรักษาตัวเลข เงื่อนไข negation ปุ่ม/ชื่อเฉพาะ ถ้ายังไม่ครบให้บอกpartial/translationpendingตามขอบเขต',
'เติมเฉพาะ11ค่าที่มีต้นฉบับ, review32flagsเป็นชื่อเฉพาะหรือprose, ทำclauseequivalence checksแต่ไม่ทิ้งliteralcriteriaเดิม และไม่เปลี่ยนagenttranslatedเป็นowner-reviewedจากคะแนน',
'TH↔ENsamefact parity, amounts/dates/negation, controlbuttonidentity, names/mixedlanguageและmissinglocalizednestedobjects',
'แปลและตรวจตัวเลขทำเอง; factual/translationreviewโดยownerไม่อ้างว่าเกิดแล้ว',[('common','app/knowledge/common/answer.py','text'),('common','app/knowledge/common/translation.py'),('common','app/knowledge/common/registry.py','validate')])
add('P21','Output ยังเผยชื่อ field ภายในหรือ label ที่ไม่ช่วยตอบคำถาม','P2','C:คำตอบจริง; H:ต้องแยกUIdebugกับbody','ตัวอย่างVR Service/platform/playtime/bookingoccupancy และZeldaถามtitle','projection → human-readable answer',
'schemafieldใช้สร้างform/LLMplanได้ แต่ไม่ใช่รายการตัวเลือกที่ผู้ใช้ต้องรู้จักเมื่อtaskชัด citationtitleถูกเปลี่ยนเป็นdraftgenericก็ช่วยprovenanceระดับmodeแต่ไม่ได้อธิบายsourceหัวข้อจริงทั้งหมด',
'VRpermissioncaseตอบmenufieldแทนสิทธิ์เข้าใช้;Zeldaเกมอะไรตอบ“ชื่อเกมอย่างเป็นทางการ?”',
'ตอบข้อเท็จจริงที่ถามด้วยภาษาผู้ใช้ หากต้องถามเพิ่มให้ถามslotที่มีผลต่อคำตอบ ไม่ถามfieldtechnical',
'แยกpresentationcontractจากcatalog/schema ใช้domaincaptionและscope/partial explanation พร้อมแหล่งอ้างอิงที่ติดตามได้; debugอยู่ส่วนdebug',
'ถามกว้าง/เฉพาะ/all/brief ทั้งสองภาษา ต้องไม่มีopaqueID/fieldtechnicalในmainanswerเว้นแต่userขอdebug',
'ทำเองได้',[('common','app/knowledge/common/rendering.py'),('common','app/knowledge/common/answer.py','title')])
add('P22','Validation/score ดูดีไม่ได้รับรองว่าเข้าใจเจตนาถูก','P1ด้านการวัด','C:โค้ดและcounts','confidence.8พบ10,969requests;uncalibratedflag15,892requests','finish validation → confidence/status interpretation',
'common finishให้.8คงที่สำหรับanswer/list ส่วนschema/evidenceตรวจfieldที่เลือก ไม่ตรวจว่าควรเลือกfieldนั้นตั้งแต่แรก FinalsafeclarificationอาจvalidTrueหลังvetoคำตอบที่ผิด',
'fieldplanner schemaTrueแต่finalFalseได้; old_build_resultหลังvetoกลับvalidTrueพร้อมwarnings; migrationtrace1.0คือเลือกprofileไม่ใช่factual100%',
'แยกexecution validity, schema validity, source support, intent/task coverage, semantic correctnessและapproval status',
'เพิ่มper-need coverage/unansweredneeds/counterevidence output contract ไม่เอาdefaultconfidenceไปปรับranking/โชว์เปอร์เซ็นต์ความถูกต้อง',
'wrongfieldbutknownsource,correctfieldbutexpired,correctcitationwronggame,safeclarification,unverifiedtranslationต้องให้สถานะแยก',
'ทำเองได้',[('common','app/knowledge/common/answer.py','finish'),('legacy','app/pipeline/engine.py','_build_result')])
add('P23','Model transport, JSON/schema, binding และคำตอบต้องวัดแยก','P0เฉพาะล่ม/P1คุณภาพ','C:calllogsและaudit','4,412HTTPattempts;4,376transportobservations;36TimeoutErrors;31requestsถูกจัดprimarytransportfailure','model admission → HTTP → body/parse → semantics',
'LLMONเป็นสิทธิ์ให้เรียก ไม่ใช่ทุกคำถามต้องเรียก HTTPobserverบันทึกสำเร็จเมื่อurlopenคืนresponse ไม่ใช่รับรองbody/schema/answerทั้งก้อน แต่plannerมีbody/parse/semantic auditแยก',
'จำนวนschemaacceptedaudits4,206ไม่เท่ากับ4,206คำตอบถูก; จำนวนcallกับrequestsต่างกันเพราะrequestอาจมีหลายcall',
'ตรวจservedmodel+จริงgenerationpreflightแล้วเก็บphasefailureรายcall อธิบายfallbackโดยไม่สลับOFFเงียบๆ',
'root-causeตามtransport/read/schema/binding/semanticsและdeadline ไม่เพิ่มaliasหรือแก้factsเพื่อรักษาคะแนนเมื่อติดต่อโมเดลไม่ได้',
'available/refused/permission/timeout/malformedJSON/schemawrong/bindingwrong/semanticwrongต้องแยกและpreserverawresult',
'ทำเองได้ในสภาพเครื่อง; ไม่สรุปnetwork permissionเป็นpolicyข้อมูลผิด',[('common','app/pipeline/llm_health.py'),('common','app/knowledge/common/planner.py','_plan_fields_batch'),('common','app/knowledge/common/entity_search.py','select')])
add('P24','Bug ฝั่งเดิม: ownership_blocked ไม่อยู่ใน scope ของ retrieve_curated','P0ในlegacy snapshot','C:exception2692และตำแหน่งcode','legacyONNameError2,692requests + harness timeout2 = exceptions2,694','legacy curated retrieval trace construction',
'ใช้ownership_blockedที่returnของretrieve_curated แต่assignmentที่พบอยู่ในretrieve_competition_fact_cardsคนละfunction จึงล้มเมื่อเข้าbranchนั้น ไม่ใช่LLMไม่รู้คำตอบ',
'R65resultsexceptionและR90exceptiontypesตรวจตรงกัน; strictscoreสูงของเดิมไม่ลบล้างbugนี้',
'ทุกbranchต้องมีownershipauditที่ถูกscopeและจริงตามguardไม่ใช่ใส่ตัวแปรว่างเพื่อซ่อนข้อผิดพลาด',
'หากนำlegacyhelperกลับมา ใช้pureinterpretationที่จำเป็น ไม่คัดลอกretrievalทั้งชุด; แก้auditflowพร้อมtestownerblocked/unmanaged/nohitsbranchในงานซ่อมภายหลัง',
'branchcoverageทั้งมี/ไม่มีownershipblock,sourceconflict,emptyhitsและlexicalfallback; ไม่rerunlegacyใหญ่เพื่อไล่คะแนนในงานเอกสารนี้',
'ทำเองได้ แต่รอบนี้ยังไม่แก้โค้ดเก่าหรือโค้ดใช้งาน',[('legacy','app/pipeline/retrieval.py','retrieve_curated'),('legacy','app/pipeline/retrieval.py','retrieve_competition_fact_cards')])
add('P25','ข้อมูลหมดอายุ: คะแนนเดิมดีขึ้นได้จากการตอบค่าที่ระบบใหม่ไม่ควรยืนยัน','ข้อมูล/Oracle','C:18ratesexpiryชัด; D:refusalcurrentpriceอาจถูกต้อง','not_current1,113requests;500อยู่primaryvaliditydiagnostic','source validity → answer status → historical expected',
'referenceOct2026อยู่หลังexpiryก่อน1Apr2026 oracleบางข้อยังคาดบาท/ฟรีหรือราคาเดิม การเทียบcorrectnessต้องดูวันมีผลและหน่วย ไม่ใช้การมีตัวเลขเป็นproof',
'VRGeneralStudentcaseใหม่ระบุendtimestampตรงsource เดิมคืน190จากตารางเก่าตามคำถามที่มีdurationซ้อน',
'ห้ามใช้ราคาเก่าเป็นcurrentโดยไม่มีหลักฐาน หากuserถามราคาประวัติในช่วงที่มีผลจึงตอบแบบhistoricalscopeได้',
'แยกhistoricalvscurrentoracleและvaliditygroundtruth เก็บเกณฑ์เก่าเป็นcompatibilityresult ไม่ลบenddate/ย้ายclockเพื่อให้ผ่าน',
'ก่อน/ตรง/หลังexpiry;no-current-rate;historicalpriceexplicit;unknownvalidityและpackageaudienceunits',
'logic/analysisทำเอง; ราคาปัจจุบันหรือวันมีผลใหม่ต้องsourceที่ยืนยัน',[('common','app/knowledge/common/answer.py','active'),('common','app/knowledge/common/billing.py')])
add('P26','Draft preview ไม่ใช่ production authority หรือ owner approval','P0ก่อนcutover','C:store/previewprofile/metadata','602heads;581validityunknown;5conflictedfields;R88ไม่มีapproval/publicationใหม่','owner save/preview → approve/publish → runtime reader',
'MigratedViewอ่านlatestdraftheadsและตั้งproduction_publication_verifiedFalse ขณะที่normalstoreอ่านactivepublishedrelease การเห็นข้อมูลใหม่ในpreviewจึงไม่เท่ากับปล่อยใช้จริงได้ด้วยapprovalเดิม',
'time-sensitive publishต้องknownvalidityและtrustreview; forecastallunknown581ไม่ใช่581recordsต้องownerกรอกทุกอย่าง เพราะบางkindไม่ต้องtime-sensitiveและfieldsoptional',
'แยกmodeให้ชัดและเลือกcutovercontractที่รักษาreview/revision/publish semantics ไม่ปล่อยdraftหรือfixtureเป็นownerpolicy',
'ทำreadinessreportตามrequired/publish_coreต่อkind sourceauthority/translationhash/relations ไม่ผ่อนvalidatorเพื่อผ่านbatch',
'draftnotvisibleinpublished,revisioneditinvalidatesapproval,withdraw/rollback,currentepochandsourcepointertestsโดยไม่แก้ownerfacts',
'โค้ดและreadinessทำเอง; factualapproval/policyconfirmationจริงไม่ทำแทนเจ้าของ',[('common','app/knowledge/common/migrated_view.py','snapshot'),('common','app/knowledge/common/store.py','approve'),('common','app/knowledge/common/store.py','publish')])
add('P27','Data-only extensibility ยังจำกัดด้วย vocabulary, relation และ runtime contract','P1','C:สัญญาในโค้ด; R:ไม่อ้างว่าnewrecordทุกประเภทถูกทดสอบแล้ว','fixtureR87growth19checks+rule7checksไม่ใช่ทุกkind/paraphrase','owner new record → discover → plan → render',
'เพิ่มrecordในschemaเดียวกันอาจไม่ต้องแก้code แต่ถ้าoperation/fieldmeaning/relationships/newgameeditionไม่เข้าresolverหรือadapterก็ยังตอบไม่ได้ ข้อมูลอย่างเดียวไม่สอนtaskgrammarใหม่โดยอัตโนมัติ',
'newAurorapackageราคา/อุปกรณ์ในfixtureผ่าน แต่ไม่ทดสอบliveproductmappingใหม่หรือallpropositionsของทุกหมวด',
'เพิ่มข้อมูลชนิดที่รองรับแล้วต้องเข้าสู่candidate/schema/rendererตามregistryเดียวกัน โดยไม่แก้aliasต่อคำถามหรือใช้sourcefixtureแทนจริง',
'taskregistry/schema-description/profilemetadataและrelation-awareprojectionร่วมกันสำหรับknownkinds; schemaใหม่จริงต้องมีversion/migration/rendererdecisionชัด',
'newrecord-only,update/withdraw,newname,heldoutquestionsทุกหมวดและemptyrelatedsource ต้องตรวจdiscoverability+answercoverageไม่ใช่saveได้อย่างเดียว',
'โค้ดทำเอง; เนื้อหานโยบายใหม่ต้องsource',[('common','app/knowledge/common/registry.py'),('common','app/knowledge/common/entity_search.py'),('common','app/knowledge/common/relations.py')])
add('P28','คะแนน strict ถูกผูก route/mode/source IDs เดิม','Compatibility','C:countsและsame-checkerpairedresults','31,649gradesprotocol-only;10,606requestsอยู่primaryprotocol-onlynoliteralfailure','result protocol → historical grader',
'commonใช้knowledge/common_read/common_answerและtypedrecordIDs ต่างจากservice_fee/rules/competition modesเดิม แม้bodyบางข้อผ่านliteralก็strictfail บางข้อไม่มีpositivecontractจึงยังบอกไม่ได้ว่าตอบครบ',
'legacystrict76.33%กับnew9.02%; samepositivecheckerต่างกัน94.41%กับ72.10% แสดงว่าปัญหาไม่ได้มีแค่protocolแต่ก็ห้ามเรียกstrict9%ว่าaccuracy9%',
'รายงานcompatibility, positivecontent, taskoutcome, source lineageและhumanreviewแยก ไม่เปลี่ยนexpectedให้เข้ากับoutputใหม่เพียงเพื่อคะแนน',
'สร้างadapterของevaluatorที่อ่านtypedoutcome/source lineageโดยเก็บstrictlegacycriterionไว้ และทบทวนความหมายของcategory/statusเฉพาะที่อ้างได้',
'bodyเดียวกันrouteใหม่ต้องcontentเท่าเดิมแต่strictต่างได้; wrongprice/wronggameต้องยังfailแม้routeถูก',
'ทำเองได้',[('common','app/knowledge/common/answer.py','finish'),('legacy','app/pipeline/engine.py','_build_result')])
add('P29','Literal checker มีทั้ง false mismatch และเงื่อนไขที่อ่อนเกินกว่าจะยืนยันคำตอบถูก','P1ด้านการวัด','C:ตัวอย่างคำตอบคู่; H:ยังไม่คำนวณsemanticaccuracyแท้','positive24,909grades; noadditional literal23,714grades','expected contract → pass/fail interpretation',
'คำแปลคนละสำนวน/ชื่อserviceแทนzoneอาจfailแม้relatedfactsถูก ขณะเดียวกันแค่มีคำหรือmarkerบางคำอาจpassทั้งที่scopeยังไม่ครบ ตัวตรวจwordingไม่ใช่semanticjudgeที่รับรองfacts',
'ปุ่มยิงกดอะไร:ทั้งคู่ขอชื่อเกม แต่ใหม่ไม่มีหนึ่งในmarker“ยังไม่แน่ใจ/ขอ/ไม่มี”ตามoracleจึงfail; TekkenEnglishclausesอีกสำนวนเช่นกัน',
'เกณฑ์ควรตรวจentity/requiredpropositions/qualifiers/numbers/negation/citations/out-of-scopeextrasพร้อมsource ไม่ยึดstringอย่างเดียวหรือให้LLMjudgeแทนtruth',
'เก็บrawliteralscoreเดิม เพิ่มstructuredneed/sourcecontractและsemanticreviewชั้นต่างหากพร้อมuncertainty ไม่เลื่อนคะแนนใหม่มาแทนเดิมเงียบๆ',
'meaning-preservingparaphraseต้องแยกจากmeaning-changingnumber/negation/edition และคำตอบยาวที่มีkeywordแต่wrongtaskต้องไม่ถือครบ',
'ทำตัวตรวจและanalysisเอง; semanticreview/factualapprovalยังไม่อ้างว่ามนุษย์ทำครบแล้ว',[('common','tools/eval_contract_v2.py'),('common','tools/run_competition_contract_r27.py')])
add('P30','ชุดเฉพาะจุดผ่าน ไม่ได้แทน distribution ของ full corpus','การทดสอบ','C:ชุดคำถาม/จำนวนbridgesและfullscores','R87web55/55; R88positive17,960/24,909; ไม่ใช่ตัวชี้วัดชุดเดียวกัน','regression selection → coverage claim',
'ชุด55เน้นปัญหาที่เพิ่งแก้และกรณีที่รู้ผล Fullมีwrapper,typo,operation,domainและoracleหลากหลายกว่า ความสำเร็จในfixedcasesไม่แปลว่าระบบgeneralizeทุกหมวด',
'bridgeprotest2/summary13/rental5finalmethodในfull ขณะที่หลายพันคำถามยังไปexact/ordinaryreader/clarification paths',
'ระบุcoverage matrixตามtask/language/style/needs/sourcekind และใช้heldoutcasesที่ไม่เลือกจากข้อที่รู้ว่าผ่าน',
'ทำtargetedrepair→nearneighbors→heldoutstratified→fullภายหลังตามคำสั่ง ไม่เพิ่มaliasเฉพาะข้อสอบหรือรันซ้ำจนเลือกanswerที่ผ่าน',
'ตรวจschema/intent/source/equivalenceและstrongnegativeพร้อมpairedbeforeafterจากผลเดิม ไม่อ้าง55/55เป็นproductionaccuracy',
'ทำเองได้',[('common','app/knowledge/common/legacy_intent_bridge.py'),('common','app/knowledge/common/competition_bridge.py')])
add('P31','Root cause บางข้อระบุไม่ได้จาก final answer อย่างเดียว ต้องรักษา rejected plan และ phase timing','P1ด้านวินิจฉัย','C:loggingpaths/timeoutcases; R:instrumentation gapsบางช่วง','watchdog2requestsไม่มีfinalworkerresult; no_common_method4,691ไม่เท่ากับalllosthistory','trace/audit/progress → diagnosis',
'outervetoอาจทำให้top-levelplanหายแต่ยังมีrejected_candidate; watchdogอาจไม่มีmodelcallที่กำลังค้างมาถึงparent จึงไม่ควรนับmodel_calls[]ว่าไม่ได้พยายามเรียก; composite/recursiveplansทำให้นับauditซ้ำได้',
'SF006traceยืนยันPCscope+relations; foodwatchdog28sไม่มีbodyจึงยังไม่ชี้ว่าsourceขาดหรือโมเดลเป็นต้นเหตุ',
'เก็บstageenter/exit, queuewait,selected/rejectedcandidate, perclauseneeds, source/revision, request/call IDs และfinaldelivery โดยไม่นำข้อมูลองค์กรที่ไม่จำเป็นมารั่วในchat',
'เพิ่มstructuredphaseobservabilityที่ไม่แก้decision และanalysisให้นับcall/request/grade/auditeventแยก',
'inducedparserfailure/modeltimeout/workerrestart/cancellationต้องเก็บphaseเดิมครบและไม่retryคำตอบแล้วทับผลครั้งแรก',
'ทำเองได้',[('common','app/pipeline/migrated_chat.py','answer'),('common','app/web_api/pipeline_supervisor.py'),('common','app/knowledge/common/planner.py','_plan_fields_batch')])
add('P32','Latency และ concurrency มี queue หลายชั้น ไม่ใช่เปิด LLM แล้วตอบพร้อมกันได้ทุกคำขอ','P1performance','C:config/admission/elapsed; R:ไม่ใช่loadcapacityรับรอง','R88worker2/modelslot1; bulk8,833.08sรวมgrading; watchdog28s/global18s','web admission → worker → model gate → HTTP',
'typed/CPUงานบางส่วนขนานได้ แต่โมเดลถูกจำกัด1slotเพื่อทรัพยากรเครื่อง queuewaitกินdeadlineก่อนgeneration ทำให้requestที่รออาจไม่มีbudgetพอ FieldplannereventZeldaรอ5.85sแล้วทำงาน3.46s',
'R64ใช้evalmatchingoptimizationsต่างจากruntime; R88coreคำถามเดี่ยว+batchworkersไม่ใช่การวัดเวลาผู้ใช้หนึ่งคนหรือจำนวนuserproduction',
'รายงานqueue/service/totalและp95/p99ตามcohortจริง ไม่ใช้HTTPelapsedของobserverที่หยุดที่headersแทนเวลารวมทุกphase',
'ลดLLMที่ถูกเรียกแต่โดนsemanticrejectซ้ำ, cacheเฉพาะแผนที่invalidateตามschema/source, typedtaskfastpaths และadmission/deadlinecontract; ไม่เพิ่มthreadsไม่จำกัดบนGPUเดิม',
'หลังcorrectnessคงที่ค่อยวัดsingle/concurrentmixโดยแยกwarm/coldและtimeout/gate/content ไม่ใช้fullbatchเป็นSLA',
'ทำโค้ด/การวัดเองได้; ไม่ปรับทรัพยากรระบบหรือซื้อบริการโดยอนุมาน',[('common','app/pipeline/model_admission.py'),('common','app/pipeline/request_deadline.py'),('common','app/pipeline/llm_health.py')])
add('P33','Unknown/conflicted fields ไม่ใช่หลักฐานว่าข้อมูลหายทั้งหมด และบางข้อไม่ต้องถามคนใหม่','ข้อมูล/การตัดสิน','C:inventoryและsourceconflictpaths','known2,951/unknown1,431/conflicted5fields; 5conflictsเป็นopen_periods','source readiness → task applicability',
'optionalmetadataว่างกับข้อเท็จจริงrequiredที่ขาดมีผลต่างกัน recordมีfieldunknownไม่ได้แปลว่าตอบอะไรไม่ได้; ข้อมูลที่ผู้ใช้ยืนยันในsessionแล้วควรใช้เป็นหลักฐานเดิม ไม่ถามซ้ำเพราะmigrationnoteยังเก่า',
'5scheduleconflictsnoteค้างเรื่องopen/bookable;12–13bookabilityและVRoccupancyมีhumanconfirmationเดิมอยู่แล้ว',
'ทำtask-levelmissingfacts inventoryว่าอะไรบล็อกคำถามใด และถามเฉพาะข้อที่ต้องตัดสินใหม่จริง',
'แยกrequiredtopublish/requiredtoanswer/optional, มีprovenanceของconfirmationเดิม และระบุunknownที่ไม่กระทบคำถามไม่ต้องถาม',
'fieldoptionalunknownต้องยังตอบneedknownได้; requiredconflictห้ามเลือกข้างเอง; confirmationเดิมไม่ถูกลืม',
'ทำinventory/mappingเอง; businessfactที่ไม่มีsourceจริงค่อยขอผู้รับผิดชอบ',[('common','app/knowledge/common/registry.py','validate'),('common','app/knowledge/common/answer.py','effective')])
add('P34','Archive comparison ไม่ใช่ controlled experiment ของ schema อย่างเดียว','การวัดผล','C:hash/corpus/configของR64/R88/R89','20,554keys/55,811gradesตรงกัน; dates/engine/data revisionsต่างกัน','test provenance → causal conclusion',
'samecheckerช่วยเทียบคำตอบที่เก็บไว้ แต่old/currentมีvaliditypolicy,source602vsข้อมูลเดิม,interpreter,LLMbudget,caching,referenceclockและerrorpathsต่างกัน จึงไม่ยืนยันว่าJSONschemaกลางทำให้แย่ลงด้วยตัวมันเอง',
'R89ไม่มีmodelcalls/requestsใหม่และตรวจhashชุดโจทย์; strictและpositiveคนละความหมาย; ชุดnative/HTTPเก่าคนละsurfaceกับenginebulkใหม่',
'สรุปได้ว่าระบบใหม่ตามผลเดิมไม่ทันตามเกณฑ์นี้ พร้อมชี้causalmechanismจากcode/traceเฉพาะที่มีหลักฐาน',
'เมื่อแก้ให้ใช้frozenfacts/cohort/dates/tasksเดียวกันเท่าที่ปลอดภัย แยกcompatibility/history/currenttruth; ไม่ทำbaselineใหม่ถ้าผู้ใช้ไม่ขอ',
'coverage/hash/no-duplicate/gradealignment/sourceimmutabilityและdenominatorทุกตารางต้องตรง',
'ทำเองได้',[('common','app/knowledge/common/migrated_view.py'),('legacy','app/pipeline/engine.py','answer')])
add('P35','ติดตั้ง R78 แล้ว ไม่ได้แปลว่า portable package/เครื่องอื่นมีการแก้ล่าสุดครบ','P1ก่อนแจก','R:ขอบเขตที่ยังไม่ได้ยืนยัน ไม่ใช่ข้อผิดพลาดที่วัดแล้วในR88','R87ติดตั้ง6codefilesในR78; R88เป็นsnapshot ไม่ได้rebuildportable','package manifest → runtime config → real device',
'bridgeใหม่ใช้legacygrammar/routingconfigเป็นdependency ถ้าเอาเฉพาะcommonfilesไปโดยไม่มีmodules/data/rulesที่ต้องใช้ อาจหาintentไม่ได้หรือimportfail ส่วนOllama/model/downloadและtransportmodeต้องตรงเครื่องปลายทาง',
'R87reportระบุไม่rebuildpackage; R88ตรวจcodehashกับsnapshot ไม่ใช่ทดสอบcleanWindows/อีกเครื่อง',
'แจกpackageที่มีexactbuild manifest/config/data/modeloptionชัด และhealthบอกversion/profile/model/knowledge sourceจริง',
'ทำreproduciblepackagingdependencyinventoryและstartupdiagnosticsภายหลัง ไม่เปลี่ยนproductionlaunchersในงานเอกสารนี้',
'clean-copy offline/online-model variants,relativepaths,portinuse,modelmissing,sourceupdatesและsame-questioncanary',
'เตรียมโค้ด/แพ็กเกจทำเองได้ภายหลัง; การติดตั้ง/เผยแพร่จริงตามscopeที่ได้รับอนุญาต',[('common','app/knowledge/common/build_info.py'),('common','app/web_api/server.py')])
add('P36','Input guard ตรวจ layout/repeat ได้บางชนิด แต่ไม่ได้แก้เจตนาทั้งประโยค','P1สำหรับtypo','C:guardmetricsและstageorder','500layoutcasesผ่าน500;repeatdetect471/500 ไม่ใช่accuracytypoของทั้งบอต','input quality guard → recovery → semantic task',
'guardบอกว่าข้อความอาจผิดหรือเตือนเบิ้ล แต่commonยังต้องparseoperationต่างหาก ตัวเลขรุ่น/เครื่องต้องป้องกันไม่ลบซ้ำผิด เช่นPC11ไม่ใช่PC1; ไทยไม่มีช่องว่างและcombiningmarksทำให้editตำแหน่งเดี่ยวไม่พอในหลายcue',
'Zeldatasktypoแม้ชื่อชัดยังreject; displaywarningที่พบrepeatไม่ควรแปลว่าคำตอบเลือกintentถูกแล้ว',
'แบ่งdetection,recovery,taskselection,answercorrectnessเป็นคนละmetric และใช้contextเฉพาะที่เชื่อถือได้ช่วยจำกัดcandidate',
'แชร์language-awareerrorchannelsและtaskvocabularyพร้อมmargin/negation/numberprotection ไม่reduceallrepeatsหรือใช้neighborทุกตำแหน่งโดยไม่ดูcontext',
'Thai/Englishmixedscript,diacritics,missing/repeatedchar,multipleworderrors,legitimateelongation,numericIDsandunknowntexts',
'ทำเองได้จากsourceและรูปแบบภาษา; ไม่ใช้caseรายคำเป็นpolicyใหม่',[('common','app/core/runtime_input_quality_guard.py'),('legacy','app/pipeline/preprocess.py','preprocess_input')])
add('P37','Owner preview กับแชทจริงใช้ dispatcher/authority surface ต่างกัน','P1ก่อนcutover','C:callpathsต่างกัน; R:ยังไม่วัดfailureทุกหมวดของpreview','preview_answerเรียกCommonAnswererตรง; actualchatมีengine+migrated+serverstate/liveadapter','owner form preview → production-like chat path',
'previewอาจไม่มีproductscope/greeting/livefallback/outercandidatevetoหรือpersistentdeliveryเหมือนwebchat และdraftpreviewreleaseมีโครงประกอบต่างจากMigratedViewบางส่วน การpreviewผ่านจึงไม่รับรองว่าfullchatถามต่อ/เลือกข้อมูลเหมือนกัน',
'owner_server.preview_answerและmigrated_chat.answerเป็นสองentrypointsที่เห็นจากsource ไม่อ้างจำนวนข้อผิดโดยไม่มีการรัน',
'เลือกcanonicalanswercontractเดียวกันหรือประกาศscopepreviewให้ตรงความจริง พร้อมtestconformanceระหว่างpreview/engine/HTTP',
'ทำthinadapterใช้snapshotprovider/dispatcher contractร่วมกันโดยไม่แอบpublishdraftหรือเอาlegacyfactsกลับมา',
'newrecord/update/withdraw,sourceinvalid,qualifiedfollowup,livequery,unknownscopeและsame-questionoutputcontractข้ามsurface',
'โค้ดและconformanceทำเองได้; ไม่ให้previewสร้างownerapprovalแทนเจ้าของ',[('common','app/knowledge/common/owner_server.py','preview_answer'),('common','app/pipeline/migrated_chat.py','answer')])
write('PROBLEM_CATALOG_REVIEWED.json',json.dumps(P,ensure_ascii=False,indent=2))
head=r'''
# วิเคราะห์ปัญหาทั้งหมดที่พบ — Legacy R64 เทียบ Common R88

## 0. คำว่า “ทั้งหมด” และระดับหลักฐาน

ครอบคลุมโครงสร้างโค้ดทั้งสองsnapshot, ผล20,554request/55,811gradesต่อแขนON, ประเภทเหตุไม่ผ่านทุกชนิดที่logsเก็บไว้, state/translation/data/source/transport/publicationและข้อจำกัดของตัวตรวจ ไม่ได้อ้างว่าอ่านเจตนาถูกด้วยมนุษย์ครบทุกคำถามหรือรู้rootcauseทุกกรณีจากkeywordfailureเพียงอย่างเดียว

- **C — Confirmed:** ยืนยันเส้นทาง/ค่า/traceหรือsourceโดยตรง
- **H — Hypothesis:** เป็นคำอธิบายที่ต้องตรวจรายกรณี ไม่เอาจำนวนกลุ่มอัตโนมัติมาเท่ากับจำนวนsemanticbugs
- **D — Designed/controlled:** guard/fixture/unknownที่อาจเป็นผลที่ถูกต้อง ไม่ใช่ต้องทำให้ตอบเพื่อผ่าน
- **R — Risk/unverified:** โครงสร้างต่างหรือขอบเขตที่ยังไม่ได้ตรวจจริง ไม่อ้างว่าเป็นfailureที่เกิดแล้วทุกกรณี

งานนี้อ่านโค้ดและผลเดิมเท่านั้น ไม่รันchatbot/LLMใหม่ ไม่แก้ownerfacts,productioncode,approvalsหรือlogsเดิม

## 1. สรุปตัวเลขที่เทียบได้

| ตัวชี้วัด | Legacy ON R64 | Common ON R88 | ความหมาย |
|---|---:|---:|---|
| Requests / Grades |20,554 /55,811|20,554 /55,811|ชุดโจทย์และkeyตรงกัน|
| Strictทุกเกณฑ์เดิม |42,601/55,811 =76.33%|5,033/55,811 =9.02%|รวมroute/intent/mode/statusเดิม ไม่ใช่เนื้อหาล้วน|
| Positive literalตัวตรวจเดียวกัน |23,517/24,909 =94.41%|17,960/24,909 =72.10%|ข้อความ/ข้อกฎที่ต้องปรากฏ ไม่ใช่semanticaccuracyทั้งคำตอบ|
| คำถามที่ผ่านpositiveทุกแถวของตัวเอง |8,160/8,907 =91.61%|5,962/8,907 =66.94%|อีกส่วนของ20,554ไม่มีpositivecontractชนิดนี้ ไม่อ้างว่าถูกครบ|
| Execution exceptions |2,694|2|คนละruntime/deadline; แยกความเสถียรจากเนื้อหา|

Positivepaired: ทั้งคู่ผ่าน17,596 / เดิมผ่านใหม่ไม่ผ่าน5,921 / ใหม่ผ่านเดิมไม่ผ่าน364 / ทั้งคู่ไม่ผ่าน1,028 grades ความต่างไม่ใช่แค่route แต่จำนวนliteralfailก็ยังรวมคำแปลคนละสำนวนและguardราคาหมดอายุด้วย

ตามlocaleในคำขอที่คงcohortเดียวกัน: ไทยเดิม95.47%→ใหม่73.61%; อังกฤษ96.00%→70.79%; auto81.83%→68.88% ไม่ใช้effective-languageต่างรุ่นสลับdenominatorไปมา

**ข้อสรุปที่รับผิดชอบได้:** ความสามารถตีความ/เลือกข้อมูล/ประกอบคำตอบของใหม่ยังมีช่องว่างจากของเดิมจริง แต่schemaกลางไม่ได้เป็นสาเหตุเพียงตัวเดียว และไม่ควรเอาคำตอบราคาที่หมดอายุหรือข้อมูลที่ยังไม่ยืนยันกลับมาตอบเพื่อทำคะแนน

## 2. ปัญหากระจุกที่ขั้นใด

| หลักฐานจากR88 | จำนวน | สิ่งที่บอก/สิ่งที่ยังไม่บอก |
|---|---:|---|
| exactentitymethod |10,179requests|เจอชื่อ ไม่ได้แปลว่ารู้task|
| exactentityแต่ไม่มีrequestedfields |1,979requests|ช่องว่างชื่อ→operation/field; ไม่ใช่typoทุกข้อ|
| มีselectedIDsแต่ไม่มีfields |3,747requests|อาจเป็นclarification/list/metadata; ต้องดูtaskก่อนตีว่าerror|
| semantic_review_needed |2,289requests|เคสที่grammarไม่พอ ไม่ใช่ทุกข้อผิด|
| schemaผ่านแต่semanticguardrejectunverified |2,494audit events|เหตุหลักหนึ่งที่LLMตอบJSONถูกแต่ไม่ได้ใช้แผน; ไม่ใช่2,494uniqueusers|
| field-plannerfinalaccepted |129audit events|finalmethodbounded_llm_schema_fieldsพบ62requests เนื่องจากcallย่อย/outerpath|
| clarification |6,090requests|รวมการถามเพิ่มที่จำเป็นกับfalseclarification ต้องแยก|
| rejectedcandidate→saferesponse |700requests|validationทำงาน แต่ผู้ใช้อาจไม่ได้ส่วนที่ตอบได้|
| ModelHTTPtransporttimeout |36calls|ไม่ใช่คำอธิบายของcontentfailทั้งหมด|
| fixedconfidence.8 |10,969requests|ค่าคงที่ ไม่ใช่ความถูกต้อง80%|

Countsของfinalplan,recursiveaudits,HTTPcalls,gradeeventsและuniquequestionsเป็นคนละหน่วย ไม่บวกข้ามกันเพื่อสร้างจำนวนปัญหาที่มากกว่าrequests

## 3. กลุ่มอัตโนมัติที่ครอบคลุมทุก raw-failed request

กลุ่มหลักจากDEEP_ANALYSISมี18,824requestsที่ไม่ผ่านอย่างน้อยหนึ่งเกณฑ์ แต่ละrequestได้กลุ่มหลักเพียงหนึ่งกลุ่มตามpriority ของตัวจัดหมวด ไม่ใช่ยืนยันว่าเหตุอื่นไม่มี ดูรายละเอียดทุกgradeในFAILURE_EVIDENCE.sqliteและดัชนีท้ายชุดนี้

{{DIAGNOSTIC_TABLE}}

**ห้ามตีความ** 10,606protocol-onlyเป็นsemanticcorrect10,606ข้อ เพราะบางข้อไม่มีpositivecontract และห้ามเรียก4,467clarificationว่า4,467falseclarificationsโดยยังไม่อ่านsource/needs

## 4. รายการปัญหาและแนวแก้รายประเภท
'''
diag=json.loads((B/'r88_full_common_llm_20261017/DEEP_ANALYSIS.json').read_text('utf8'))['failure_request_counts'];head=head.replace('{{DIAGNOSTIC_TABLE}}','| กลุ่มหลัก | Requests |\n|---|---:|\n'+'\n'.join(f'| {k} | {v:,} |' for k,v in diag.items()))
lines=[head]
for p in P:
 lines += ['\n### '+p['id']+' — '+p['title'],'', '**ลำดับ/สถานะหลักฐาน:** '+p['priority']+'; '+p['status'],'','**จำนวน/ขอบเขตที่เกี่ยวข้อง:** '+p['count'],'','**จุดใน Flow:** '+p['stage'],'','**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**','',p['why'],'','**หลักฐานที่พบ**','',p['evidence'],'','**สิ่งที่ควรตอบหรือควรทำแทน**','',p['expected_behavior'],'','**แนวแก้ที่รักษาข้อมูลจริง**','',p['solution'],'','**วิธีตรวจหลังแก้**','',p['verification'],'','**ต้องใช้มนุษย์หรือไม่**','',p['human'],'','**Source code:**','']
 for ref in p['source_refs']:
  mode,rel,*symbols=ref
  lines.append('- '+link(C if mode=='common' else L,rel,symbols[0] if symbols else None))
lines+=['\n## 5. สิ่งที่ควรแก้ก่อนตามผลกระทบจริง','',
'1. **Task semantic contract/recovery → field selection:** P01–P08/P12/P18 มีผลกว้างต่อคำถามที่ข้อมูลอยู่แล้วและถามเพิ่มผิดประเด็น','2. **Projection/completeness:** P09/P10/P13/P14/P21/P22 ให้ตอบเฉพาะสิ่งที่ขอพร้อมconditions/relatedfactsครบ ไม่รับbroadplanทุกfield','3. **Observability/timeouts:** P23/P31/P32 เก็บphasefailureชัดและลดLLMที่เรียกแต่rejectอย่างไม่จำเป็น ไม่ขยายtimeoutเป็นวิธีแก้ความหมาย','4. **Data readinessตามหลักฐาน:** P11/P15/P16/P20/P25/P26/P33 แก้metadata/translationที่ทำเองได้ แยกpolicy/validityที่ต้องowner; ไม่ถามซ้ำสิ่งที่ยืนยันแล้ว','5. **Evaluator/coverage:** P28–P30/P34 ทำคู่strictกับsemantic/sourcecontractที่เข้มขึ้น เก็บข้อเก่าไว้ ไม่แก้expectedให้รับคำตอบผิด','6. **Preview/deployment:** P27/P35/P37 เมื่อcoreถูกค่อยทำconformanceและpackagecutover; แก้buglegacyP24เฉพาะหากต้องใช้branchนั้นจริง ไม่ดึงlegacyfactfallbackมาแทน', '',
'## 6. สิ่งที่ทำเองได้กับสิ่งที่ต้องsourceเพิ่ม','',
'ทำเองได้: sharednormalization,task/fieldadapters,relationprojection,qualifiedfollowup,LLMbinding/guardvalidation,source-lineageanalysis,English11knownsectiontranslations,scoring/coverage/packagemanifest และตรวจsourceที่มีอยู่แล้ว','',
'ต้องsource/ผู้รับผิดชอบเมื่อยังไม่มีจริง: ราคาปัจจุบันหลังexpiry,วันมีผลที่จำเป็นต่อpublication,จำนวนชั่วโมงhalf/full-day,เงื่อนไขมัดจำ/ยกเลิก/เหมารายชั่วโมง/หลายวัน,ความหมายphysicalopenที่นอกเหนือbookabilityที่ยืนยัน และrulebook/physicalcontrollerpolicyใหม่ที่sourceไม่รองรับ','',
'ไม่ต้องให้เจ้าของยืนยันซ้ำ:12–13ไม่มีช่องจอง,VR30นาทีกันชั่วโมงเต็ม,liveสถานะเดิมที่ผู้ใช้ตรวจแล้วถูกต้อง ส่วนEnglishผ่านautomatedtestไม่เปลี่ยนเป็นowner-reviewedเอง','',
'## 7. ดัชนีและหลักฐานทุกกรณี','',
'- '+local('COMMON_FAILURE_INDEX_ALL.md')+' —18,824raw-failedrequests พร้อมkey/ภาษา/คำถาม/กลุ่ม/จำนวนgradeที่ไม่ผ่าน','- '+local('LEGACY_FAILURE_INDEX_ALL.md')+' —5,689requestsจากlegacyONที่ไม่ผ่านอย่างน้อยหนึ่งเกณฑ์','- '+local('ALL_FAILURE_REASON_TYPES.md')+' —ใหม่620reasonstrings/เดิม318reasonstrings เก็บครบ ไม่ตัดเหลือเฉพาะตัวอย่าง','- '+local('DETAILED_METRICS.json')+' —stagecounts/planneraudits/data scan พร้อมหน่วยที่นับ','- '+local('DATA_INVENTORY.json')+' —5conflicts/11missingENpaths/validity/readinessและknownZeldafields','- '+local('CODE_SYMBOLS.json')+' และ '+local('ENGINE_SINGLE_BRANCHES.json')+' —จุดอ้างอิงทุกsymbolและsingle-enginebranchindex','- '+local('SOURCE_MANIFEST.json')+' —hashของsourceที่อ่าน; rawlogsและknowledgeเดิมไม่ถูกแก้', '',
'การตรวจรายละเอียดแต่ละคำถามให้ใช้keyค้นในR88 FAILURE_EVIDENCE.sqlite และR65 evidence.sqlite ไม่ใช้indexกลุ่มอัตโนมัติเป็นrootcauseที่ยืนยันแล้วแทนtrace/source']
write('03_PROBLEM_ANALYSIS_ALL_TH.md','\n'.join(lines))

gap=r'''
# เทียบ Full Flow และแผนผสานที่รักษา facts กลาง

## 1. ตารางจุดต่าง: เดิมทำอะไร กลางทำอะไร ผลกระทบอยู่ตรงไหน

| ชั้น | Legacy R64 | Common R88/R87 | จุดที่ต้องรักษา/พัฒนา |
|---|---|---|---|
| ขอบเขตธุรกิจ |studio/scope/boundaryและprotectedhandlers|studioก่อนmigrated; commonno-factualfallback|คงร้านเกมscopeและไม่เปิดgeneralตอบทุกเรื่อง|
| Recovery |หลายerrorchannelsในpreprocess/cuepaths|normalize/schema-recovery/typedcueคนละช่วง|แชร์taskrecoveryก่อนearlyreturnอย่างมีanchor|
| Entity |aliases/resolvers/targetlockของแต่ละdomain|exact/spans/one-repeat/fuzzyและboundedentityLLM|exactsubjectไม่ใช่taskproof; numeric/gameeditionต้องปลอดภัย|
| Intent |routepriority/universal/frame/capabilities|operation/roles/profiles/schema-fieldneeds|ทำcanonicaltaskcontractที่อ่านจากknownsourceได้ทุกrecord|
| Score |rulepriority/capabilityscore+margin|namesimilarity/trigram/guard/binding/defaultconfidence|แยกscoreแต่ละชั้น ไม่ใช่accuracy|
| Factsource |rules/static/structured/curated/canonicalหลายprovider|currenttypedrecordsและsourcepointers|นำlogicกลับมา ไม่ดึงanswer/priceเก่ากลับมา|
| ราคา |typedfeeplan+เฉพาะformula/source|rate/packagejoins,billing+validity|preserveaudience/durationtupleและcurrentvalidity|
| Controls |specializedquery/controlcontract|controlset/action/modeprojection|sharedactionintentพร้อมsourcecompleteness|
| Competition |lockedtargets/detail/overview/sourceclauses|parent/childfacets,rule_selectionและ2bridges|sharedpropositioncontractกับcommonclausefacts|
| FAQ |trustedregexpattern+priority→sourceanswer|intentindex/profiles/semanticselectorและnarrowbridge|concept-levelcoverage;ไม่compileowneraliasเป็นregex|
| Broad/all |domain-specificfull-list/overview|broad_request/fields/relatedrecords/summarybridge|allของscopeไหน;summaryบางข้อห้ามอ้างครบ|
| Qualification |specializedpolicy/compoundtools|quotedprofilebinding/ownership/context/clauses|ห้ามขยายสลิปเป็นidentity/amountpolicy|
| State |typedrequest_plan/resolve_question/contextcontracts|common_read_state/confirmationfingerprint/request_contract|สองแบบต้องmapoperation/slotsได้ ไม่copyfactsจากhistory|
| LLM |planner/intent/toolrouter/scopedgenerationตามgate|record/profileindexหรือfieldJSON;factsอ่านจากDB|schema/binding/semantics/answerproofต้องแยก|
| Validation |source/language/taskcontracthardveto|typedfields/evidence/currentepoch+outerveto|validateถูกstructureไม่ใช่intentcorrectness|
| Updates |หลายsourcefile/index/provider|stableID/revision/source/approve/publishหรือdraftview|ownerบันทึกง่ายแต่ต้องquerydiscoverableด้วย|
| Live |dashboardหรือWordPressตามflags|adapterเดิมหลังcommondefer|ไม่ใช้staticfactsเป็นlive;API200≠slottruth|
| Render |domain-humanformattedanswers|genericfieldrenderer+somebridges|task-specificpresentationบนfactproviderเดียว|
| Production |legacyruntimeตามsnapshot|migrationpreview ยังไม่publishedcutover|อย่าเอาdraftvisibleเท่ากับownerapproved|

## 2. Causal chain ที่อธิบายว่าข้อมูลอยู่แล้วแต่ยังไม่ตอบ

```mermaid
flowchart TD
 A["ข้อมูลsummary/price/ruleอยู่ในDB"] --> B["คำถามต้องถูกแปลงเป็นtask/needsที่ถูกก่อน"]
 B --> C{"ได้taskและsubjectครบหรือไม่?"}
 C -- "ไม่" --> D["exactentityอย่างเดียว หรือcandidate/anchor miss"]
 D --> E["schemafieldmenu / LLMproposal / clarification"]
 C -- "ได้" --> F["เลือกrelation/field/clauseและqualifier"]
 F --> G{"scopeครบและsourceมีผล?"}
 G -- "ไม่ครบ" --> H["partial/unknown/not_currentอย่างจำเพาะ"]
 G -- "ครบ" --> I["renderเนื้อหาที่ขอพร้อมevidence"]
 E --> J{"proposalผูกกับเจตนาได้?"}
 J -- "ไม่ได้" --> K["semanticguardreject แม้JSONผ่าน"]
 J -- "ได้" --> F
 K --> H
```

**ไม่แก้ที่ข้อมูลเพียงอย่างเดียว:** Zeldaknownfieldsมีแล้วแต่taskcueไม่ผ่าน; SF006historyและrelationsมีแล้วแต่shorttaskถูกveto; modelHTTPสำเร็จแต่semanticguardยังไม่รับ; คำแปลตรงความหมายบางข้อliteralไม่รับ

## 3. Target flow ที่แนะนำ (proposal ไม่ใช่ของที่ติดตั้งแล้ว)

```mermaid
flowchart TD
 A["Raw + locale + trusted delivered state"] --> B["Safe normalization/recovery พร้อมedit traceและanchor locks"]
 B --> C["Canonical request: tasks,targets,qualifiers,constraints,requested scope"]
 C --> D{"มีข้อขาดที่มีผลต่อคำตอบจริง?"}
 D -- "มี" --> E["ถามเฉพาะslotที่ขาด + เก็บtaskstate"]
 D -- "ไม่มี" --> F["Schema-aware current common snapshot provider"]
 F --> G["Task adapters: pricing/rental/games/controls/rules/calendar/FAQ/live"]
 G --> H["Relation/field/clause projection + source/date/authority checks"]
 H --> I{"ต้องใช้LLMช่วยinterpretation?"}
 I -- "ต้อง" --> J["Bounded structuredproposal + quoted semantics + perclause needs"]
 J --> K["Independent contract check: numbers,negation,scope,extra fields"]
 K --> H
 I -- "ไม่ต้อง" --> L["Per-need coverage: answered/unknown/conflicted/not_current"]
 L --> M["Human-facing rendererตามtask ไม่เผยschemaเมื่อตอบได้"]
 M --> N["Evidence + freshness + output completeness + delivery/state commit"]
```

ลูกศรย้อนจากLLMเป็นlogicalone-passproposal/review ไม่อนุญาตให้retryไม่จำกัดหรือเปลี่ยนfactsเพื่อให้accept ต้องมีattempt/deadlinebudgetชัด

## 4. Step-by-step repair flow หลังงานวิเคราะห์นี้

### รอบ A — ตรึงหลักฐานและนิยามคำว่า “ตอบถูก”

1. ยึดsamekey/corpus/sourceversionกับR88และเก็บR64answersสำหรับเทียบ ไม่ทับlogs
2. จัดแต่ละcaseเป็นcurrentfact/historicalfact/missingfact/wording/protocol/testfixtureตามsourceจริง
3. สร้างneedcontractว่าต้องมีอะไร ต้องไม่สรุปอะไร เช่นprotestdeadline+after-match+captain/coach หรือpermissionไม่ใช่playtime
4. แยกschema/transport/semantic/source/ownerapprovalในผลประเมิน

### รอบ B — นำ interpreter กลับมาอย่างมีขอบเขต

1. แชร์purelegacytypo/cue recoveryก่อนcommontaskresolution โดยเก็บraw/editsและไม่เปลี่ยนexplicitgame/numbers/negation
2. ทำcanonicaltaskprofileเช่นgame_overview/equipment_list/booking_policy/competition_protest/rental_price ไม่ผูกกับชื่อrecordทีละรายการ
3. ส่งcontractไปcommonprovider ไม่เรียกbuildanswer/priceจากlegacyJSON
4. ให้LLMเติมหรือเสนอrequestneedsที่grammarยังไม่รู้จัก แต่ผูกinput spans/qualifiers/sourcekindได้ ไม่ต้องบังคับทุกparaphraseกลับไปเข้าregexเดิมก่อน
5. ตัดunrequestedfieldsแต่ไม่ยอมรับแผนที่ambiguous/wrongsubjectเพียงเพราะschemaผ่าน

### รอบ C — ทำ projection/coverage ให้ตรงงาน

1. source/record/field/relatedchildต้องอ่านตามtask ไม่ใช่เอาdefaultfieldsของkindมาตอบทุกครั้ง
2. gameoverviewอ่านsummary/genre; permissionอ่านpolicyanswer; equipmentlistอ่านequipmentchildren; rulesอ่านclause/conditionsที่ตรง
3. multi-taskเก็บแต่ละneedและdependency ไม่ตอบครบเทียมหรือทิ้งส่วนที่ตอบได้ทั้งหมด
4. followupใช้pendingtask/operationและscopeที่ส่งจริง พร้อมrevisionfingerprint ไม่เก็บราคาหรือpolicyfactsในstate
5. captionsตอบระดับzone/service/resourceตามที่ถามโดยอาศัยverifiedrelations

### รอบ D — Data-only lifecycle และ preview/chat parity

1. ตรวจknownrequiredfields/relations/source/validityที่มีผลต่อtask แยกoptionalunknown
2. เติมEnglish11sectionvaluesจากต้นฉบับที่มีจริง ตรวจ32Thai-in-enflagsว่าเป็นชื่อเฉพาะหรือprose
3. ใช้confirmationเดิมเรื่องbookability/VRoccupancy ไม่ขอซ้ำ ถ้าต้องการfactsอื่นค่อยตั้งคำถามเจาะจง
4. แยกdraftpreview/publishedrelease/migrationprofile และใช้dispatchercontractที่สอดคล้องกัน
5. ทดสอบrecordใหม่/แก้ราคา/แก้rule/ถอนข้อมูลในฐานแยกโดยไม่approveproductionแทนowner

### รอบ E — ตรวจผลหลังแก้แบบไม่ overfit

1. Small root-cause regression: Zelda task typo, Friday maintenance policy, SF006อุปกรณ์, qualifiedpayment, scopedrules และpriceexpiryprotectivecase
2. Neighbor casesหลายรูปแบบ+counterexamples: เปลี่ยนเกม/ภาษา/กลุ่ม/เวลา/negation/จำนวน โดยเป้าหมายเดิม
3. Held-outstrataที่ไม่เลือกจากข้อที่ผ่าน และnewdata-onlyfixturesทุกsupportedkind
4. ตรวจtransport/schema/binding/task/source/renderแยก โดยเปิดLLMตามproductiongates
5. Fulltestครั้งถัดไปเมื่อได้รับคำขอ ไม่รันหรือแก้ระบบในงานเอกสารนี้อัตโนมัติ

## 5. เงื่อนไขออกจากงานซ่อมแต่ละหมวด

| หมวด | เงื่อนไขที่ต้องเห็น |
|---|---|
| Recovery | taskcueฟื้นได้และcounterexampleไม่เปลี่ยนentity/negation/numericID |
| Fieldplanning | knownneedไม่หาย, extraunaskedfieldsไม่ถูกอ่าน, unknownwordingไม่ถูกrejectอย่างไร้เหตุ |
| Relations | targetlevelและjoinsตรงsource; no-FKไม่ถูกเดาสร้าง |
| Compound/state | ทุกclauseมีสถานะ, contextไม่รั่วข้ามtask, shortreplyที่จำแนกได้ตอบถูก |
| Rules/controls |ครบpropositions/bindingsตามscope พร้อมconditions/partial-sourcecaveat |
| Price/calendar |validity/timezone/closure/billing/occupancyไม่ปนกัน |
| English |factparityและpropernamepolicyชัด ไม่ใช้Thai-characterflagเป็นtranslationaccuracy |
| Publication |draft/review/releaseไม่ปนกัน ข้อมูลใหม่visibleในmodeที่ตั้งใจจริง |
| Evaluation |samecriteria/samekeys; strictและsemantic/sourcecriteriaแยก; ไม่ใช้passmarkerเป็นfactcertificate |

## 6. สิ่งที่ไม่ควรทำเพื่อแก้คะแนน

- ไม่เปิดlegacyfactsfallbackกลับมาเมื่อcommonหาไม่เจอ
- ไม่ปิดsemantic/source/validityvalidatorทั้งหมด หรือยอมทุกJSONจากLLM
- ไม่เพิ่มaliasรายคำถามจากข้อสอบแทนการแก้taskcontract
- ไม่ลบexpiryหรือเดาจำนวนชั่วโมง/ราคา/นโยบายเพื่อให้มีคำตอบ
- ไม่ย้ายmetadatafield/internaldebugขึ้นmainchatเพียงเพื่อให้oracleพบkeyword
- ไม่เปลี่ยนoracleเก่าให้เข้ากับoutputใหม่แล้วอ้างว่าaccuracyดีขึ้น โดยไม่รายงานคนละเกณฑ์
- ไม่ใช้targeted55/55,HTTP200หรือconfidence.8เป็นproductionapproval

งานนี้ส่งมอบFlow/หลักฐาน/แผน ไม่ได้ติดตั้งTargetflowหรือแก้runtimeระหว่างอ่านผล
'''
write('04_FLOW_GAP_AND_REPAIR_TH.md',gap)
print('Wrote',len(P),'problem categories, detailed report and flow gap/repair proposal')
