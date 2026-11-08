from pathlib import Path
import json
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());inventory=[]
for f in sorted([*(p/'data/ground_truth').rglob('*.jsonl'),*(p/'data/human_review').glob('*eval*.jsonl')]):
    rows=[json.loads(l) for l in f.read_text(encoding='utf-8-sig').splitlines() if l.strip()];c=rows[0] if rows else {}
    entry={'file':str(f.relative_to(p)),'rows':len(rows),'keys':list(c),'sample':c};inventory.append(entry)
    print(f.name,len(rows),json.dumps(c,ensure_ascii=False)[:1100])
with (r/'extra_corpus_inventory.json').open('x',encoding='utf-8') as f:json.dump(inventory,f,ensure_ascii=False,indent=2)
