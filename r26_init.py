import hashlib,json,subprocess,uuid
from datetime import datetime
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=project/'reports'/('r26_competition_content_speed_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6])
report.mkdir()
Path(__file__).with_name('r26_report_path.txt').write_text(str(report),encoding='utf-8')
files=['app/pipeline/engine.py','app/pipeline/retrieval.py','app/pipeline/competition_presentation.py','app/pipeline/bilingual_english.py','docs/125_competition_format_r25_flow_20261001.md']
manifest={}
for relative in files:
 path=project/relative; dest=report/'before'/relative; dest.parent.mkdir(parents=True,exist_ok=True)
 with dest.open('xb') as handle:handle.write(path.read_bytes())
 manifest[relative]=hashlib.sha256(path.read_bytes()).hexdigest()
for relative in ['data/competition_rules/competition_rule_chunks.jsonl','data/eval/competition_user_r24_2000_20261001.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','data/locales/en/CURRENT','booking_dashboard/center_schedule.json']:
 manifest[relative]=hashlib.sha256((project/relative).read_bytes()).hexdigest()
with (report/'before_manifest.json').open('x',encoding='utf-8') as handle:json.dump(manifest,handle,indent=2)
with (report/'git_status_before.txt').open('x',encoding='utf-8') as handle:handle.write(subprocess.run(['git','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8').stdout)
print(report)
for line in (project/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines():
 row=json.loads(line)
 if 'valorant_psu_phuket_2026' in row['id'] and any(row['id'].endswith(f'_s{number:02d}_c01') for number in range(11,16)):print(json.dumps({'id':row['id'],'text':row['text']},ensure_ascii=False))
