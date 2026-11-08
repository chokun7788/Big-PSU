import hashlib,json,shutil,sqlite3
from pathlib import Path
OUT=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');target=ROOT/'data/knowledge/migration_r63_20261013'
check=json.loads((OUT/'INSTALLED_OWNER_CHECK.json').read_text(encoding='utf-8'))
before=set((OUT/'GIT_BEFORE_INSTALL_BUNDLED.txt').read_text(encoding='utf-8-sig').splitlines());after=set((OUT/'GIT_AFTER_INSTALL.txt').read_text(encoding='utf-8-sig').splitlines())
with sqlite3.connect((OUT/'round7/before.sqlite').as_uri()+'?mode=ro',uri=True) as b,sqlite3.connect((ROOT/'data/knowledge/approved.sqlite').as_uri()+'?mode=ro',uri=True) as original:
 unchanged=list(b.iterdump())==list(original.iterdump())
assert unchanged and not before-after and check['passed']==check['total']
append=f"\n\n## ตรวจหลังติดตั้ง\n\n- หน้ากรอกของ code โปรเจกต์จริงอ่านฐานแยกผ่าน HTTP ได้ **{check['passed']}/{check['total']}**: รายการร่าง 582 รายการและข้อมูลแก้ไขทุกหมวดที่มีในฐาน รวมร่าง center/policy เดิม\n- เซิร์ฟเวอร์ทดสอบหยุดแล้ว ไม่มีการหยุดเว็บแชท/โมเดลเดิมของผู้ใช้\n- SQLite ฐาน production เดิมเทียบ logical dump กับก่อนย้ายแล้วเหมือนเดิม\n- Git ตรวจ repository C:/Users/Chokhun/Downloads/Learn-LLM; ก่อนติดตั้งไม่มีรายการค้างที่ Git รายงาน หลังติดตั้งเพิ่มเฉพาะโฟลเดอร์ review ใหม่ ไม่มีการ reset/clean/commit\n- การตรวจ HTTP รอบแรกติดสิทธิ์ socket ของ sandbox ขอสิทธิ์ network ผ่านระบบแล้วตรวจใหม่ได้ ผลเดิมเก็บไว้ ไม่ใช่การแก้คะแนนคำตอบ\n"
report=(OUT/'RESULTS_TH.md').read_text(encoding='utf-8')+append
(OUT/'RESULTS_TH.md').write_text(report,encoding='utf-8')
(target/'RESULTS_TH.md').write_text(report.replace('round6/OLD_VS_DRAFT.jsonl','OLD_VS_DRAFT_BASELINE.jsonl').replace('round7/PENDING.json','PENDING.json'),encoding='utf-8')
shutil.copy2(OUT/'round6/OLD_VS_DRAFT.jsonl',target/'OLD_VS_DRAFT_BASELINE.jsonl')
shutil.copy2(OUT/'PENDING_SUMMARY_TH.md',target/'PENDING_SUMMARY_TH.md')
shutil.copy2(OUT/'INSTALLED_OWNER_CHECK.json',target/'INSTALLED_OWNER_CHECK.json')
p=target/'Open-Migrated-Drafts.ps1';text=p.read_text(encoding='utf-8-sig');text=text.replace('$args=@(', '$arguments=@(').replace("{$args+='--no-browser'}","{$arguments+='--no-browser'}").replace('& $python @args','& $python @arguments');p.write_text(text,encoding='utf-8-sig')
summary={'final_round':'round7','normal_db_unchanged':unchanged,'old_git_entries_retained':not bool(before-after),'draft_heads':582,'draft_records_prepared':580,'schema_lineage_scope_checks':{'passed':4922,'total':4922},'original_owner_questions_and_explicit_fields':{'passed':20,'total':20},'exploratory_without_llm':{'passed':2,'total':4,'remaining':['equipment generic details coverage','FAQ statement paraphrase selection']},'installed_owner':{'passed':check['passed'],'total':check['total']},'workbook_after_whitespace_review':{'passed':38,'total':38},'published':False,'production_response_engine_modified':False,'db':str(target/'approved.sqlite'),'db_sha256':hashlib.sha256((target/'approved.sqlite').read_bytes()).hexdigest(),'launcher':str(target/'Open-Migrated-Drafts.cmd')}
(OUT/'FINAL_VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');(target/'FINAL_VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))
