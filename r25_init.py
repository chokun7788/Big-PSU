import hashlib,json,shutil,subprocess,uuid
from datetime import datetime
from pathlib import Path
root=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=root/'reports'/('r25_competition_format_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6])
report.mkdir()
Path(__file__).with_name('r25_report_path.txt').write_text(str(report),encoding='utf-8')
paths=['app/pipeline/retrieval.py','app/pipeline/bilingual_english.py','app/pipeline/competition_overview.py','app/pipeline/competition_targets.py','app/pipeline/competition_taxonomy.py','web_chat/app.js','web_chat/styles.css']
manifest={}
for relative in paths:
 src=root/relative;dest=report/'before'/relative;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest);manifest[relative]=hashlib.sha256(src.read_bytes()).hexdigest()
for relative in ['data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','data/competition_rules/canonical/competition_rule_releases.jsonl','data/eval/competition_user_r24_2000_20261001.jsonl','data/locales/en/CURRENT','booking_dashboard/center_schedule.json']:
 manifest[relative]=hashlib.sha256((root/relative).read_bytes()).hexdigest()
(report/'before_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
status=subprocess.run(['git','status','--short'],cwd=root,text=True,encoding='utf-8',capture_output=True)
(report/'git_status_before.txt').write_text(status.stdout,encoding='utf-8')
print(report)
