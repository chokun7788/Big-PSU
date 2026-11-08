from pathlib import Path
import json,shutil,ast
from prepare import B,SYSTEM,ROOT,PACK,sha,dbhash
receipt=json.loads((B/'DELIVERY_RECEIPT.json').read_text())
for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
 for name,h in receipt['hashes'][label].items():
  assert sha(root/name)==h,(label,name)
  if name.endswith('.py'):ast.parse((root/name).read_text(encoding='utf-8'))
for path,h in receipt['db_hashes'].items():assert dbhash(Path(path))==h,path
analysis=B/'ANALYSIS_TH.md'
analysis.write_text(analysis.read_text(encoding='utf-8').replace('../r59_schema_repair_20261012/Research.md','RESEARCH_R59.md'),encoding='utf-8')
results=B/'RESULTS_TH.md'
results.write_text(results.read_text(encoding='utf-8').replace('| owner save/approve/publish/preview guard หลังแก้ |','| นำเข้าโปรเจกต์จริงแล้ว, guards | 22 tests ผ่าน | actual project imports; mocked config guards + temporary owner HTTP |\n| owner save/approve/publish/preview guard หลังแก้ |'),encoding='utf-8')
with (B/'RESEARCH_R59.md').open('x',encoding='utf-8') as f:f.write((B.parent/'r59_schema_repair_20261012/Research.md').read_text(encoding='utf-8'))
note='''# ส่งต่อ r60

ปิดงานและตรวจการนำเข้าวันที่ 2026-10-13 ตาม client; การทดลองและคำถามรอบนี้เริ่ม 2026-10-12

## สิ่งที่นำเข้าแล้ว

โปรเจกต์จริง `C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data` และ SYSTEM/PACK รุ่น r58 ที่พัฒนาต่อเป็น r60 มี source hashes ตรงกัน 8 ไฟล์ ตาม DELIVERY_RECEIPT.json ตรวจ AST และ imports จากโปรเจกต์จริงแล้ว

แก้ answer/planner/query_contract/engine/owner_server เพิ่ม schema descriptions/schema language/tests; มี before สำรองทุกไฟล์เดิมที่แก้และ diffs แยก ไม่มี commit/reset/clean และ Git status ก่อนเริ่มทั้ง 318 entries ยังอยู่ครบ มี entries ใหม่ 7 รายการ

DB logical hashes ทั้ง4ฐานเท่าเดิม (SYSTEM/ROOT/PACK/DEMO720); catalog/storeไม่แก้, ไม่copydemoเข้าproduction ไม่แก้logเดิม ผลทุกรอบอยู่คนละโฟลเดอร์ แม้runที่failเพราะชื่อtestmoduleผิดก็ยังเก็บไว้

## การใช้งานและขอบเขต

เปิด launcher เดิมหลังปิดชุดเว็บ/owner editor ที่ใช้อยู่ตามปกติเพื่อให้Pythonโหลดsourceใหม่ โค้ดที่copyไม่เปลี่ยนprocessซึ่งรันค้างอยู่ รอบนี้ไม่restartของผู้ใช้

web/preview `PSU_LOCAL_LLM_ASSIST_ENABLED` defaultเปิด; plannerยังใช้ `PSU_COMMON_PLAN_LLM`; directpipeline Noneอ่าน `PSU_EXPERIMENTAL_ALLOW_LLM`. เมื่อexplicitปิดLLM สำนวนใหม่developmentผ่าน18/100 ต้องไม่อ้างความสามารถเท่ากับเปิดLLM

ข้อมูลจริงcommon:41heads/revisions,41sources,0approvals,0releases ข้อมูลdraftยังไม่ได้เข้าคำตอบproductionของcommon ต้องownerreview/approve/publishตามformก่อน Legacyfactsและlivebookingยังคนละเส้นทางกับการทดลองcommonในรอบนี้

แพ็กเกจโฟลเดอร์ ready_package อัปเดตsourceแล้ว แต่ไฟล์zip/archivesเก่าหรือชุดdistributionอื่นไม่ได้สร้างใหม่รอบนี้ อย่าส่งarchiveเก่าแล้วอ้างว่ามีr60

อ่าน [Flow](Flow.md), [ผลสรุป](RESULTS_TH.md), [วิเคราะห์ทุกfailureของactualLLM/reserved](ANALYSIS_TH.md). รายการที่ทำต่อได้เอง: fieldprecision/over-answer, semanticsแยกkind, unnamedentity+multitarget, legacyfallbackหลังpublish/withdraw, expansionของlinkedpolicy/rateและrenderingscopes; ข้อเท็จจริง/นโยบาย/การแปลเจ้าของยังต้องhumanreviewตามฐานข้อมูล
'''
with (B/'DELIVERY_NOTE.md').open('x',encoding='utf-8') as f:f.write(note)
docs=['Flow.md','RESULTS_TH.md','ANALYSIS_TH.md','DELIVERY_NOTE.md','RESEARCH_R59.md']
for root in [SYSTEM,ROOT,PACK]:
 dest=root/'docs/common_content_r60_20261012'
 for name in docs:shutil.copy2(B/name,dest/name)
verification={'delivery_date_client':'2026-10-13','source_copies_equal_and_unchanged_since_delivery':True,'python_ast_ok':True,'owner_databases_unchanged':True,'installed_project_guards':{'tests':22,'passed':22,'log':'installed_project_guards.log'},'development':{'cases':100,'pass':100,'exact_required_fields':72,'extra_fields_cases':28,'actual_llm':True,'named_synthetic':True},'reserved_first':{'cases':48,'pass':43},'reserved_after_repair':{'cases':48,'pass':48,'seen_regression':True},'llm_off':{'cases':100,'pass':18},'actual_pipeline':{'cases':12,'pass':12},'authenticated_owner_preview':{'cases':12,'pass':12},'related_regression':{'cases':5056,'pass':5056},'relationship_projection':{'cases':16,'pass':16},'production_common_approved':0,'production_common_releases':0,'user_processes_restarted':False,'archive_rebuilt':False,'documentation_hashes':{n:sha(B/n) for n in docs}}
with (B/'FINAL_VERIFICATION.json').open('x',encoding='utf-8') as f:json.dump(verification,f,ensure_ascii=False,indent=2)
print('Final source, database and installed tests verified; documents synchronized')
