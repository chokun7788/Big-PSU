"""Verify actual training coverage and optimizer telemetry from saved records."""
import collections,json,math,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;T=R/'train02'
rows=lambda p:list(map(json.loads,p.open(encoding='utf8')))
train=rows(R/'train.jsonl');losses=rows(T/'TRAINING_LOSS.jsonl');journal=rows(T/'STATUS_JOURNAL.jsonl')
steps=[r for r in journal if r['phase']=='training']
assert [r['micro_step'] for r in losses]==list(range(1,733))
assert [r['optimizer_step'] for r in steps]==list(range(1,94))
assert all(math.isfinite(r['completion_loss']) for r in losses)
assert all(math.isfinite(r['gradient_norm']) and r['gradient_norm']>0 for r in steps)
expected=collections.Counter(r['key'] for r in train);epochs={}
for epoch in [1,2,3]:
 values=[r for r in losses if r['epoch']==epoch]
 assert collections.Counter(r['sample_key'] for r in values)==expected
 epochs[epoch]={'micro_steps':len(values),'mean_completion_loss':statistics.mean(r['completion_loss'] for r in values),'max_completion_loss':max(r['completion_loss'] for r in values)}
proof=json.loads((T/'OPTIMIZATION_PROOF.json').read_text('utf8'))
assert proof['actual_weight_updates'] and proof['base_parameter_hash_unchanged'] and proof['initial_adapter']['sha256']!=proof['final_adapter']['sha256']
out={'verified':True,'micro_steps':len(losses),'optimizer_steps':len(steps),'every_training_example_used_once_per_epoch':True,'finite_loss_and_positive_finite_gradient_norms':True,'epochs':epochs,'peak_allocated_bytes':proof['peak_allocated_bytes'],'base_parameters_unchanged':True,'adapter_changed':True,'training_loss_is_not_accuracy':True}
(R/'TRAINING_VERIFICATION.json').write_text(json.dumps(out,indent=2),'utf8');print(json.dumps(out,indent=2))
