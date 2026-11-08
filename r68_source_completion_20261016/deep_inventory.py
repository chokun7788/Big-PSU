"""Account for source families outside curated, without promoting AI outputs."""
import collections,hashlib,json,re
from pathlib import Path
B=Path(__file__).resolve().parent;R=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
out={'root':str(R),'data_directories':{},'review_files':[],'knowledge_inbox':[],'raw_control_documents':[]}
for folder in sorted((R/'data').iterdir()):
 if not folder.is_dir():continue
 files=[p for p in folder.rglob('*') if p.is_file() and p.suffix in {'.json','.jsonl'}]
 out['data_directories'][folder.name]={'json_jsonl_files':len(files),'bytes':sum(p.stat().st_size for p in files)}
for p in sorted((R/'data/human_review').glob('*.jsonl')):
 rows=[json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()]
 decisions=collections.Counter(str(r.get('human_decision') or '') for r in rows)
 out['review_files'].append({'path':p.relative_to(R).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':len(rows),'human_decisions':dict(decisions),'classification':'evaluation_review_data_not_business_source'})
for p in sorted((R/'data/knowledge_inbox').glob('*.json')):
 r=json.loads(p.read_text('utf-8-sig'));out['knowledge_inbox'].append({'path':p.relative_to(R).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'id':r.get('id'),'status':r.get('status'),'classification':'schema_or_placeholder_not_real_published_content'})
p=R/'data/locales/en/approved_localizations.jsonl';out['approved_localizations']={'path':p.relative_to(R).as_posix(),'rows':sum(bool(s.strip()) for s in p.read_text('utf-8-sig').splitlines()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for p in sorted((B/'source_snapshot/data/control_game').rglob('*.json')):
 r=json.loads(p.read_text('utf-8-sig'));g=r.get('game_controls')
 if not g:continue
 rows=g.get('button_mappings') or []
 out['raw_control_documents'].append({'path':p.relative_to(B/'source_snapshot').as_posix(),'game':g.get('game_name'),'platform':g.get('platform'),'mapping_rows':len(rows),'row_keys':dict(collections.Counter(k for x in rows if isinstance(x,dict) for k in x)),'coverage_status':g.get('coverage_status')})
out['fact_projection_review_status']=dict(collections.Counter(json.loads(s).get('evidence_status') for s in (B/'source_snapshot/data/competition_rules/canonical/competition_rule_fact_projections.jsonl').read_text('utf-8-sig').splitlines() if s.strip()))
(B/'DEEP_SOURCE_FAMILY_ACCOUNTING.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'review_rows':sum(x['rows'] for x in out['review_files']),'nonempty_human_decisions':sum(n for x in out['review_files'] for d,n in x['human_decisions'].items() if d),'inbox_files':len(out['knowledge_inbox']),'approved_localizations':out['approved_localizations']['rows'],'raw_control_json_documents':len(out['raw_control_documents']),'raw_control_mapping_rows':sum(x['mapping_rows'] for x in out['raw_control_documents']),'fact_projection_review_status':out['fact_projection_review_status']},ensure_ascii=False))
