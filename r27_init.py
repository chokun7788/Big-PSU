import hashlib, json, shutil, subprocess, sys, uuid
from datetime import datetime
from pathlib import Path

project = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report = project / 'reports' / ('r27_competition_contract_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '_' + uuid.uuid4().hex[:6])
report.mkdir()
Path(__file__).with_name('r27_report_path.txt').write_text(str(report), encoding='utf-8')
files = ['app/pipeline/engine.py', 'app/pipeline/retrieval.py', 'app/pipeline/bilingual_english.py', 'app/pipeline/competition_presentation.py', 'app/pipeline/competition_taxonomy.py', 'app/pipeline/competition_targets.py', 'app/core/intent_cue_recovery.py', 'tools/competition_user_ground_truth_r24.py', 'web_chat/app.js']
protected = ['data/competition_rules/competition_rule_chunks.jsonl', 'data/eval/competition_user_r24_2000_20261001.jsonl', 'data/eval/competition_rules_rag_ground_truth_v1.jsonl', 'data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl', 'data/locales/en/CURRENT', 'booking_dashboard/center_schedule.json', 'docs/126_competition_content_speed_r26_flow_20261001.md']
manifest = {}
for relative in files + protected:
    src = project / relative
    dst = report / 'before' / relative
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open('xb') as handle: handle.write(src.read_bytes())
    manifest[relative] = hashlib.sha256(src.read_bytes()).hexdigest()
for relative in ['before_manifest.json', 'protected_manifest.json']:
    with (report / relative).open('x', encoding='utf-8') as handle:
        json.dump(manifest if relative.startswith('before') else {k: manifest[k] for k in protected}, handle, indent=2)
with (report / 'git_status_before.txt').open('x', encoding='utf-8') as handle:
    handle.write(subprocess.run(['git', 'status', '--short'], cwd=project, capture_output=True, text=True, encoding='utf-8').stdout)
sys.path.insert(0, str(project))
from app.knowledge.localization import approved_localization
rows = [json.loads(line) for line in (project / protected[0]).read_text(encoding='utf-8').splitlines() if line.strip()]
with (report / 'source_inventory.md').open('x', encoding='utf-8') as handle:
    for row in rows:
        handle.write('\n## ' + row['id'] + '\n\nTH: ' + row['text'] + '\n\nEN: ' + (approved_localization(row, 'text') or '[not approved]') + '\n')
print(report)
