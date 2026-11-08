# R132 — แก้และใส่ Flow ต่อ ตาม authorization เดิมของผู้ใช้

ผู้ใช้ตำหนิว่ารู้จุดดีขึ้นแล้วทำไมไม่ใส่ ทั้งที่สั่งให้เดินต่อและทำFlowครบ ให้ดำเนิน implementation/verification/activation ที่พิสูจน์ว่าดีขึ้นต่อเอง ไม่ถามอนุญาตซ้ำ ไม่ใช้subagents ไม่จบแค่รายงาน/แผน ขอบเขต76requirements/14หมวดคงเดิม

## สร้างcandidateแล้ว

- R132/system สำเนาR130 ไม่แก้R130/R131หรือผลเดิม ตรวจparentfreeze2361filesก่อนcopyผ่าน
- SQLite readonly backupรวมcommittedWALเป็นR132/common.sqlite ข้อมูล/approvalsเดิม847active/24withdrawnไม่แก้ SOURCE_DATABASE_LINEAGE.json
- prepare_r132.pyที่rootสร้างcopy, PARENT_FREEZE.json, PARENT_REQUIREMENTS_TRACEABILITY.json/REQUIREMENTS/FULL_JOBS copied
- source codeหลายไฟล์แก้แล้ว AST365Pythonผ่านก่อนpatchท้าย ยังต้องverifyอีก

## การแก้ที่ลงไปแล้ว แต่ต้องตรวจรับจริง/แก้ต่อ

- scope.entity_contains และFactIndex.bind +dialogue_task.mentions กันaliasไทยสั้นจอที่อยู่ในจอง/การ์ดจอ ใช้lexicaloperationprecedence ไม่เปลี่ยนcontainsทั่วไป
- precision.equipment maskชื่อcomponentจากbindingqueryและเสริมdevice_typeแม้poolผิดชนิดไม่ว่าง ตอนlocalGPUอ่านRTX5060จากsourceได้แล้ว
- rule_semantics.py แยกtopics format/pause/settings/macro/install/watch/bug/protest/equipment/responsibility/food/prep; sourcevaluesยังอ่านจากrecords ไม่มีIDs/คำตอบธุรกิจในruntime
- readers.rules_reader topiccoverageก่อนheadingmatch รักษาdependencyในevent; formatเลือกsourceที่มีสาระformatมากกว่าheadingtitle
- obligation_verifierไม่ตัดsubstantiveclauseเพราะvalue==heading ตรวจpredicateแทน และยังปฏิเสธallowed-equipmentheading/overviewtitle
- native_intents รักษาwholeexplicitcompetitionqueryก่อนcompoundsplit/policyfallback รวมfoodและหลายneeds; addedeligibility/publicpurelegacyintentfunction->currentpolicy, offsitescope, staticcatalog, explicitgamepresence inclblockedPC10, actionprioritydamage/cancel/booking, centerbuilding/floor และweekdaybookable
- vocabularybookingstartpatternแก้wordboundariesกันstartingplayersถูกจับbooking
- damage_intentเพิ่มsource damage_responsibility + causefilter และliteraltext-extensionเลือกsourceเต็ม ไม่ใช่กฎเครื่องเสียเอง (patchท้ายยังไม่เคยverify)
- context_guard/context_bindings clearC05missinggameambiguityหลังreferentbound แต่readerยังตรวจplatform; canonical_missing_control_game pluralbuttonsเป็นlist (patchท้ายยังไม่verify)
- meaning_readerเก็บword-countsevenbuttons ถ้าsource14entriesแต่subset7ไม่ระบุให้partialพร้อมnotice
- integrationแยกstaticgamecatalogจากliveprovider gate
- precision.game_presence PC#10 ต้องมีinstalled_resource_idsจริง ถ้าไม่ยืนยันblocked ไม่ขยายzone==everymachine; nativeproposalpatchท้ายต้องตรวจให้C04แทนC03 และpositiveexactPC1ยังต้องทำreceipt/renderให้ระบุเครื่องจริง
- guardC07 offsiteไม่เอาonsitepackagesมาใช้; renderunknownตรงเรื่อง
- graph_protocolSYSTEMระบุJSON/rootkeys/versionliteralชัด; selectorpromptระบุplans/i/choices/noinputecho
- model_gatewayreservectxหลังadmission; llm_healthreservepipelinebudgetหลังได้slot คืนslotเมื่อbudgetfailและclearhalfopen flags; concurrencydefault15sec max60 boundeddeadline (harnessenvอย่าตรึง0.2โดยไม่ตั้งใจ)
- RequestBudget.cancel_unattempted คืนreservationเมื่อdeniedก่อนHTTP; contextเพิ่มmodel_calls_attempted/transport_completed (ต้องทดสอบcompatibilitybudgetครบ)

## ผลlocalที่มีแล้ว

verify_source_cases.py ใช้167sourcecasesจากR131CONSOLIDATED_SOURCE_REVIEW ผ่านEngine/compiler/readersจริง แต่LLMOFFและบางnativeAPIadapterไม่อยู่ในenginepure จึงไม่ใช้เป็นfinalAPI/semanticaccuracy และไม่ใช้changed=improved

- local_1792930776438106100:135changed, exceptions0 (รอบแรก)
- local_1792931283385837900:146changed, exceptions0
- local_1792931528292906900:149changed, exceptions0 ล่าสุด **ก่อนpatchท้ายdamage/pluralcontrols**
- LATEST_LOCAL_REVIEW.jsonชี้ล่าสุด
- GPU, publiceligibility, Cockpitcatalog, Tekkenformat002, CS2watch+bug และeventfoodอ่านถูกsourceแล้ว
- ยังเห็นdamageไปself-failure(เพิ่งแก้ท้ายยังไม่verify), price+itcontrolsยังmissingเพราะoperationcontrol(เพิ่งแก้pluralเป็นlist), PC10ไปC03unknown(เพิ่งเพิ่มnativeC04frame), bookingURLและweekdayต้องดูหลังaliashelper/dialoguetaskpatch
- CS2macro3keysยังตอบrelatedrecords เพราะEnglish 'are strictly prohibited' ไม่ผ่านsubstantivepredicate ตอนท้ายเพิ่มprohibited/forbiddenแบบ>=5wordsแล้ว ยังไม่verify
- VALfullsource002ยาวหลายclauseได้ทั้งmacro/food แต่อาจrendererดึงทั้งเอกสารมากเกิน ต้องอ่านจริงไม่ถือidsถูกเท่ากับคำตอบดี

## Protocol/admission contracttests

vendorติดตั้งแยกเฉพาะR132 ไม่แก้primaryruntime: lm-format-enforcer0.11.3 +interegular0.3.3 ผ่านpip --no-deps LOG dependency_install.log
officialprimarydocs https://github.com/noamgat/lm-format-enforcer อ่านแล้ว รองรับHFprefix_allowed_tokens_fn

verify_protocol_and_admission.py ผ่าน16checks/inference0/network0 ->PROTOCOL_ADMISSION_VERIFICATION.json รวมJSONschema/root/version+inputquote guard, selectorrootrejectecho, substantiveequalheadingและrejectheadingonly, busyไม่กินctx/pipelinebudget และbudgetfailคืนslot
purecharparserต้องconfigalphabetเพิ่มThai; productionTokenizerDataจะตั้งalphabetเองจากtokenizer tree ตัวtokenizerbackendยังไม่verifyactualgeneration

## Backendเตรียมแล้วแต่ยังไม่activate — automaticapprovalblocked

serve_model.pyคัดจากR129แล้วแก้เป็นR132aliaspsu-r132/port13221; sameD:/CodexTraining/psu-r121-20261022/model +retainedR121/newR129pathsเดิม (newโหลดไว้แต่ยังไม่promote)
เพิ่มlmformatenforcerprefix tokenfilterเมื่อformatdict/json +provenance.schema_constrained_decoding/decoder, rawoutputบันทึกก่อนvalidationด้วย
ยังไม่เคยรันจริง/โหลดGPU/ยิงinference จึงห้ามอ้างconstraineddecodingทำงานแล้ว

**Tool automaticapprovalปฏิเสธ exec_command ที่รวมตรวจR130/R131complete+ตรวจPID/healthแล้วStop-Process42136เพื่อสลับไปR132server (reasonคืนเพียงblocked bypolicy)** ไม่มีคำสั่งในbatchนั้นได้ทำงาน ไม่มีserverถูกหยุด ไม่มีMODEL_PROCESS/HANDOFFไฟล์จากbatchนั้น ต้องไม่เลี่ยงการปฏิเสธด้วยkillผ่านPython/อีกshell
แจ้งผู้ใช้commentaryแล้วว่าautomaticapprovalblockedเฉพาะserverhandoff และจะใช้serverเดิมตรวจFlowต่อ เก็บdecoderhandoffเป็นfinalstepเมื่อมีresultreviewable อย่าถามapprovalตอนงานแก้ที่ไม่ติดblockยังไม่เสร็จ

เดิมmodel42136port12921 psu-r129:latest ยังอยู่, API37576port13024R130ยังอยู่ ตรวจPID/commandline/logก่อนสั่งการ ไม่stopR78 ปัจจุบันGPUtotal6141MiB used5641MiB จึงไม่ควรโหลดอีก4BบนGPUพร้อมกัน

start_candidate.pyคัดR130แล้วเปลี่ยนR132aliaspsu-r132/URL13221/port13224; **ต้องปรับเลือกใช้oldserver12921/aliaspsu-r129ได้ก่อนstartAPIตอนนี้** เพราะnewmodelยังblocked/notstarted
run_common.pyคัดR130มาแต่ยังไม่แก้hardcodedmodelalias/12921และreference_grader.pyยังไม่ได้copy ต้องตั้งให้ตรงactualserverและobserveURL ถูก (ตอนใช้oldserverก็เก็บเดิม) ห้ามrunbaselineใหม่

## ต้องทำต่อ

1. verify_source_casesหลังpatchท้าย อ่านactualQ/A/sourceของcriticalและ167cases แยกcorrectimprovement/remaining/regression อย่าaccept149changed=ดีทั้งหมด
2. เพิ่มmeaningful source-basedassertionsสำหรับGPU13/guard13/Tekken29/event36/booking10/damage10/anaphor2/catalog2 รวมwithdraw/sourcebad/hash/version/negativecontrolsและowner50/14categoryschemachecksเดิมที่ยังเกี่ยวข้อง
3. แก้remainingD01-D15/negativecancel/resourcepositive/tournamentcoverage/needledger/renderer/validityตามsource โดยไม่ใส่factsในruntimeหรือtrainซ้ำ
4. APIreadinesssingle/multi/owner50บนR132ที่ใช้actualserverเดิมก่อน เปิดR132port13224พร้อมlogsisolated source847เท่าเดิม
5. เมื่อfixesผ่านเตรียมfreezeใหม่ แล้วรันR131same2111jobs/5584gradesเพียงcandidatelatestใหม่ ไม่มีbaselineinference/regrading อย่าเริ่มfull20554ซ้ำจนneeded/gatesready
6. actualmodelwiregenerationยังต้องtestบนpromptใหม่ source-semanticreviewควบคู่ ไม่promotenewweightsที่criticalเคยถอยเพียงเพราะschemaผ่าน
7. เดินactivationที่พิสูจน์ดีกว่าให้ผู้ใช้ตามauthorizationเดิม ไม่จบแค่รายงานเตรียมพร้อม หากถึงserverhandoffblockจริงและต้องapproval จึงอธิบายautomaticrejection+exactaction+genericreason พร้อมผลreviewableหลังงานอื่นเสร็จ ตามdeveloper ไม่เลี่ยงpolicy
8. เก็บ76requirements traceabilityเดิมทั้งหมดในR132 updateหลักฐานจริง ไม่คิด%เอง ห้ามประกาศsemantic100%/Flowครบเพียงlocalchecks

## Installation discovery

Workspaceไม่มี.git root gitstatusบอกnotrepo ไม่มีAGENTS ancestors/relevantfolders
production bundleชื่อ PSU_Esports_Chat_New_R69/system/runtime +Start-New-Chat.ps1 defaultport8101, ownereditor8102; แม้ชื่อR69อาจมีR78patchinstalled ต้องอ่านruntime/build_info/healthก่อนแก้ ไม่writeproductionDBทับด้วยcandidateDBหรือapprovalsโดยไม่ตรวจ
R78workfolderชื่อr78_web_session_check_20261016 มีFLOW_R78_TH.md/BASELINE_MANIFEST ฯลฯ ไม่ใช่r78_integrated_common(ไม่มี)
rgworkspaceกว้างไปติดwork/r30_test_dependenciesaccessdeniedและvendornoise ใช้targetdirectoryหรืออ่านrootnamesตรง จำกัดsearchต่อ
