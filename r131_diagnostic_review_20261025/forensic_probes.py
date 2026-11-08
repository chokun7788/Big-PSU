"""Deterministic read-only code-path probes, not assistant/model requests."""
import collections,gzip,hashlib,json,sqlite3,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025';sys.path.insert(0,str(P/'system'))
from app.knowledge.common.domain_flow.projection import compile_snapshot,title,value
from app.knowledge.common.domain_flow.index import FactIndex
from app.knowledge.common.domain_flow.scope import contains,norm
from app.knowledge.common.domain_flow.precision import equipment
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.readers import rules_reader,policy
from app.knowledge.common.domain_flow.scope import reference_time
from dataclasses import asdict
def load(p):return json.loads(p.read_text('utf-8-sig'))
def lines(p):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for s in f:yield json.loads(s)
c=sqlite3.connect((P/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN')
records={x['record_id']:json.loads(x['payload']) for x in c.execute('SELECT r.* FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')}
pairs={x['source_id']:(json.loads(x['payload']),x['snapshot']) for x in c.execute('SELECT * FROM cc_sources')};meta=dict(c.execute('SELECT key,value FROM cc_meta'))
withdrawn=[x[0] for x in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]
payload={'active':'migration-preview-r69','epoch':int(meta['epoch']),'records':records,'sources':{k:v[0] for k,v in pairs.items()},'source_pairs':pairs,'withdrawn':withdrawn}
logical=hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert logical==load(P/'SOURCE_SNAPSHOT_BEFORE.json')['sha256']
snapshot={'active':payload['active'],'epoch':payload['epoch'],'release':{'records':records,'sources':payload['sources']},'source_pairs':pairs,'withdrawn':withdrawn,'evaluation_draft_only':True,'allow_demo':False}
idx=FactIndex(compile_snapshot(snapshot));probes=[]
deep={x['key']:x for x in lines(R/'DEEP_REVIEW_CASES.jsonl.gz')}
key=next(k for k in deep if k.startswith('f6a75fef'));q=deep[key]['question'];pool=idx.bind('C03',q)
probe={'case':'gpu_binding','key':key,'question':q,'returned_plan':asdict(equipment(idx,q)),'bound_facts':[(f['record_id'],f['facet']) for f in pool],
 'matched_subject_labels':[s for s in idx.subject_labels['C03'] if contains(q,s)],
 'matched_entity_labels':[{'label':s,'records':sorted({f['record_id'] for f in fs})} for s,fs in idx.entity_labels['C03'].items() if contains(q,s)],
 'correct_record_has_gpu':any(v.get('key')=='GPU' for v in value(records['equipment_gaming_pc'],'specifications')),
 'correct_record_in_bound_pool':any(f['record_id']=='equipment_gaming_pc' for f in pool),
 'code':'domain_flow/index.py FactIndex.bind; precision.py equipment: fallback only if pool empty'}
assert probe['correct_record_has_gpu'] and not probe['correct_record_in_bound_pool'];probes.append(probe)
for prefix in ['eede3e9b','06563f1a','cc40820b','0c25d981','21fe7ed0']:
 key=next(k for k in deep if k.startswith(prefix));row=deep[key];q=row['question'];at=reference_time('2026-10-16T12:00:00+07:00')
 native=propose(idx,q);rule=rules_reader(idx,norm(q),at)
 facts=[idx.byid[fid] for fid in rule.ids if fid in idx.byid]
 probes.append({'case':'native_and_rule_source_selection','key':key,'question':q,'native_proposal':native.as_dict() if native else None,'rule_plan':asdict(rule),
  'selected_rule_facts':[{'fact_id':f['id'],'record_id':f['record_id'],'label':f['label'],'value':f['value'],'record_facet':value(records[f['record_id']],'facet')} for f in facts],
  'heading_value_equal_in_any_locale':[f['id'] for f in facts if any(f['value'].get(l)==f['label'].get(l) for l in ['th','en'])],
  'code':'native_intents.propose policy fallback after nonmatching rule source; obligation_verifier.assess substantive heuristic lines130-132'})
for prefix in ['934b6162','9749c57f']:
 key=next(k for k in deep if k.startswith(prefix));q=deep[key]['question'];native=propose(idx,q)
 from app.knowledge.common.domain_flow.legacy_profile import plan as legacy_profile
 legacy=legacy_profile(idx,'C03',q)
 probes.append({'case':'target_words_overrode_requested_action','key':key,'question':q,
  'bound_equipment_facts':[(f['record_id'],f['facet']) for f in idx.bind('C03',q)],
  'matching_equipment_aliases':[{'label':s,'records':sorted({f['record_id'] for f in fs})} for s,fs in idx.entity_labels['C03'].items() if contains(q,s)],
  'native_proposal':native.as_dict() if native else None,'legacy_profile_plan':asdict(legacy) if legacy else None,
  'saved_understanding':(deep[key]['result'].get('decision_artifact') or {}).get('understanding'),
  'code':'scope.contains ASCII-only boundary; native_inventory_presence_record / legacy_profile plan ignores request predicate'})
# Every invocation here is a pure local projection/reader; no model/HTTP calls.
out={'source_logical_digest':logical,'source_before_matches':True,'model_http_calls':0,'assistant_end_to_end_queries':0,'probes':probes,'scope':'deterministic mechanism reproduction on existing saved questions; no runtime/source change'}
(R/'DETERMINISTIC_CAUSAL_PROBES.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'probes':len(probes),'gpu_pool':probe['bound_facts'],'gpu_matched_labels':probe['matched_entity_labels'],'native_frames':[(x['question'],(x.get('native_proposal') or {}).get('reason'),[(t.get('category'),t.get('canonical_operation')) for t in (x.get('native_proposal') or {}).get('tasks',[])]) for x in probes[1:]]},ensure_ascii=False))
