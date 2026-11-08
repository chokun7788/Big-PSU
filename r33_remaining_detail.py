import sys,json
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P))
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
reg={json.loads(l)['id'] for l in (R/'full_D_PAIRED.jsonl').open(encoding='utf-8') if json.loads(l)['v2']['regression']}
for line in (R/'candidate_D_all_results.jsonl').open(encoding='utf-8'):
 x=json.loads(line)
 if not any(g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl' and g['id'] in reg and g['variant']=='noisy' for g in x['grades']):continue
 z=x['result'];print(json.dumps(dict(id=[g['id'] for g in x['grades'] if g['id'] in reg],question=x['question'],mode=z['mode'],answer=z['answer'][:600],trace=[t for t in z['trace'] if any(k in str(t).lower() for k in ('recover','clean_query','preprocess'))]),ensure_ascii=False))
from app.core.intent_cue_recovery import recover_intent_cue_sequence
q='Could you please help me with thus: What are the studio rules'
print(recover_intent_cue_sequence(q))
