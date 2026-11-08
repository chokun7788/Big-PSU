import json,shutil
from pathlib import Path
from prepare import B,SYSTEM,ROOT,PACK,sha,dbhash
log=(B/'installed_project_guards.log').read_text(encoding='utf-8-sig')
assert 'Ran 36 tests' in log and '\nOK' in log and 'FAILED' not in log,log[-1000:]
r=json.loads((B/'DELIVERY_RECEIPT.json').read_text())
for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
 for name,h in r['source_hashes'][label].items():assert sha(root/name)==h
for path,h in r['before_db_hashes'].items():assert dbhash(Path(path))==h
p=B/'RESULTS_TH.md';text=p.read_text(encoding='utf-8').replace('sourcefolderจะsyncหลังguardsแล้ว','sourcefoldersyncแล้ว').replace('sourcehash/DBhash/GitstatusจะตรวจในDELIVERY_RECEIPTก่อนนำเข้า','sourcehash/DBhash/Gitstatusตรวจแล้วในDELIVERY_RECEIPTก่อนนำเข้า')
text+='\n## ตรวจหลังนำเข้าโปรเจกต์จริง\n\ninstalled_project_guards.log:36/36ผ่าน;sourcehashทั้ง3ชุดตรงกัน;DBlogicalhashทั้ง4เท่าเดิม;Gitentriesก่อนเริ่ม325รายการยังอยู่ครบ;ไม่restartผู้ใช้/ไม่publishownerfacts/ไม่rebuildZIP. ทดสอบล่าสุดsharedgateได้8/8ในsample ไม่ใช่productioncapacityguarantee\n'
p.write_text(text,encoding='utf-8')
note='''# การใช้ r61 ที่ส่งเข้าแล้ว

sourceในโปรเจกต์จริงและโฟลเดอร์ready_packageอัปเดตแล้ว 11ไฟล์เดิม+9ไฟล์ใหม่ มีbefore/diffsและreceipt. LLMยังเปิดตามlauncherปกติ

ปิดแล้วเปิดระบบชุดนั้นใหม่ตามปกติเพื่อโหลดโค้ด; processที่ค้างยังไม่เปลี่ยนตามไฟล์ ไม่ได้หยุดserver/โมเดลของผู้ใช้ระหว่างทำงาน. `/health` รุ่นใหม่มีcommon_loaded_build เพื่อดูโค้ดที่โหลด;owner `/api/status` มีbuildแยกactive/epoch

planner8s queue12sยังถูกจำกัดด้วยglobaldeadlineจริง;preview10sอาจมีเวลารอน้อยกว่าweb19s. ไม่ใช้sample8requestsเพื่อโฆษณาว่ารองรับ8usersต่อเนื่องทุกคำถาม

อ่าน RESULTS_TH.md เพื่อดูรายการS01–S16:ยังไม่ครบทั้งหมดของFlow. ข้อมูลจริง41draftsไม่มีapproval/release;OWNER_REVIEW_PACKETอยู่workspaceสำหรับreview ไม่คัดลอกrawpacketเข้าdistributionและไม่publishเอง

ZIPเดิมยังไม่ใช่buildนี้ ส่วนที่อัปเดตคือsourcefolders. งานต่อหลัก:field-levellegacybridge/independentcontextgold →budget/compare/sharedstate →Thaierror →calibration/long-runload →ownerapproval/activation/rebuildสองvariants
'''
with (B/'DELIVERY_NOTE.md').open('x',encoding='utf-8') as f:f.write(note)
for root in [SYSTEM,ROOT,PACK]:
 d=root/'docs/common_content_r61_20261013'
 for name in ['RESULTS_TH.md','DELIVERY_NOTE.md']:shutil.copy2(B/name,d/name)
result={'client_date':'2026-10-13','implementation_incomplete_against_full_16_item_plan':True,'installed_tests':36,'installed_passed':36,'source_copies_match':True,'four_databases_unchanged':True,'old_git_entries_preserved':325,'llm_enabled_by_default':True,'actual_llm_regression':{'cases':100,'passed':100,'before_shared_queue_change':True},'related_regression':{'cases':5056,'passed':5056},'pipeline':{'cases':12,'passed':12},'preview_http':{'cases':12,'passed':12},'load_sample':{'requests':8,'passed':8,'median_seconds':8.746874499949627,'max_seconds':14.664772700052708,'not_production_capacity_proof':True},'owner_records_approved_or_published':False,'archives_rebuilt':False,'user_processes_restarted':False}
with (B/'FINAL_VERIFICATION.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print('Installed tests, source and databases verified; remaining work explicitly recorded')
