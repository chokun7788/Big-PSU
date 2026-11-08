"""Find trace-backed candidates for the reviewed causes. Not semantic gold."""
import collections,gzip,json,re,time
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025';groups=collections.defaultdict(list)
for p in sorted((P/'full01').glob('RESULTS_*.jsonl.gz')):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for line in f:
   x=json.loads(line);a=(x.get('result') or {}).get('decision_artifact') or {};q=x['question'].casefold();r=x.get('result') or {};hits=r.get('hits',[]);ids={h.get('record_id') for h in hits};answer=r.get('answer','');c=a.get('execution_contract') or {};tasks=(c.get('request_plan') or {}).get('tasks',[])
   def add(name,evidence):groups[name].append({'key':x['key'],'question':x['question'],'answer':answer,'evidence':evidence,'semantic_status':'candidate_review_required_not_bulk_adjudicated'})
   residual=q.replace('การ์ดจอ','').replace('จอง','')
   if 'equipment_gaming_monitor' in ids and ('จอง' in q or 'การ์ดจอ' in q) and not re.search(r'จอ|monitor|display',residual):add('thai_substring_monitor_leak',{'source_ids':sorted(ids),'residual_after_removing_booking_gpu_terms':residual})
   if re.search(r'ชดเชย|เสียหาย|\bcompensation\b|\bdamag\w*\b',q) and 'migrated_faq_rule_equipment_pc_zone' in ids:add('damage_to_inventory',{'source_ids':sorted(ids)})
   if a.get('live_booking') and re.search(r'\b(?:which|what) games?\b|เกม.*(?:อะไรบ้าง|อะไรมั่ง)',q) and not re.search(r'วันนี้|พรุ่งนี้|ตอนนี้|\b(?:now|today|tomorrow|tonight)\b|\d{1,2}:\d{2}|20\d\d[-/]',q):add('static_catalog_to_live',{'live_status':a['live_booking'].get('status')})
   cats=(a.get('domain_flow') or {}).get('categories',[])
   if re.search(r'กติกา|แข่ง|\btournament\b|\bcompetition\b',q) and 'C10' in cats and any(h.get('record_id','').startswith(('r114_','migrated_faq_','r130_owner_')) for h in hits):add('tournament_to_general_studio_policy',{'categories':cats,'source_ids':sorted(ids)})
   if re.search(r'competition format|รูปแบบ.*แข่ง|format.*tournament',q) and any(i and i.endswith('tekken8_psu_esports_section_001') for i in ids):add('tekken_format_to_document_title',{'source_ids':sorted(ids)})
   for t in tasks:
    if t.get('bindings') and t.get('target_scope')=='shared' and 'legacy_meaning_requires_clarification' in t.get('ambiguities',[]) and t.get('bound_record_ids'):
     add('resolved_binding_still_ambiguous',{'task_id':t['id'],'target_span':t.get('target_span'),'bound_record_ids':t['bound_record_ids'],'bindings':t['bindings'],'ambiguities':t['ambiguities']});break
out={'created_at':time.time(),'cohorts':{k:{'unique_requests':len({x['key'] for x in v}),'cases':v} for k,v in groups.items()},'all_labels_are_diagnostic_candidates_not_confirmed_semantic_failures':True,'no_runtime_queries':True,'source_unchanged':True}
(R/'RELATED_TRACE_COHORTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v['unique_requests'] for k,v in out['cohorts'].items()}))
