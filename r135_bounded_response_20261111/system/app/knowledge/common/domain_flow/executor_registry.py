"""Declared operation contracts, not a Cartesian product of category/fields."""
import re
SOURCE_KINDS={
 'C01':['center','contact','facility','faq'],'C02':['person','faq'],'C03':['equipment_model','resource','zone','service','faq'],
 'C04':['game','game_service','service','resource','zone','game_mode','control_set','faq'],'C05':['control_set'],
 'C06':['rate','service','audience','faq'],'C07':['rental_package','zone','audience','faq'],
 'C08':['procedure','policy','faq'],'C09':['policy','faq'],'C10':['policy','faq'],
 'C11':['schedule','closure','faq'],'C12':['live_binding','resource','service'],
 'C13':['competition','competition_rule','faq'],'C14':['news','faq','competition']}
SEMANTICS={
 'field_lookup':('bound entity + requested field','exact field or explicit missing source'),
 'relation_lookup':('bound relation root','all confirmed edges in requested relation scope'),
 'action_lookup':('game/platform/action or button','matching binding set, modifiers preserved'),
 'list':('declared collection scope','exact projected set or confirmed subset explicitly labelled'),
 'count':('declared collection and counting unit','deduplicated member identities, never top-K length'),
 'group_list':('collection + grouping key','group membership receipts'),
 'group_count':('collection + grouping key + counting unit','deduplicated members per group'),
 'unit_rate':('service/audience/session basis','recorded rate with validity'),
 'calculate_total':('service/audience/quantities/declared billing rule','recomputed Decimal arithmetic receipts'),
 'compare_services':('at least two service options and matching audience/period','one result per option, no aggregate purchase total'),
 'compare_durations':('at least two source duration options','all duration options per audience'),
 'compare_packages':('at least two package options','option scope, inclusions and terms retained separately'),
 'condition_lookup':('source action and condition scope','all applicable conditions/exceptions or unresolved status'),
 'procedure_lookup':('source procedure action','ordered steps and preconditions retained'),
 'permission_lookup':('action/subject/condition scope','source decision and exceptions, never inferred permission'),
 'weekday_timetable':('weekday and service/access distinction','source weekday periods'),
 'dated_service_state':('Bangkok date/time scope','calendar computation + closure precedence receipts'),
 'weekly_timetable':('week scope','seven weekdays or explicit missing day'),
 'maintenance_lookup':('weekday or week scope','maintenance periods only'),
 'resource_availability':('exact mapped resource/date/time/window','provider identity, requested date, freshness and slot coverage'),
 'rule_dependency_lookup':('event/edition/clause scope','complete clause + declared dependencies'),
 'compare_rules':('explicit event/edition options','separate scoped clauses per option'),
 'clarification_required':('unresolved referent/required slot','targeted question preserving independent completed needs'),
}
def describe(task,question):
 cap=dict(task.capability);operation=cap['operation'];q=question
 if task.category=='C08' and task.canonical_operation=='policy.booking_steps':operation='procedure_lookup'
 elif task.category in {'C08','C09','C10'} and re.search(r'ได้ไหม|ได้หรือ|อนุญาต|\b(?:can|may|allowed|permitted)\b',q,re.I):operation='permission_lookup'
 elif task.category=='C11':
  operation='maintenance_lookup' if task.facet=='maintenance_periods' else 'dated_service_state' if re.search(r'20\d\d-\d\d-\d\d|วันนี้|พรุ่งนี้|\b(?:today|tomorrow|now)\b',q,re.I) else 'weekly_timetable' if task.operation=='list' else 'weekday_timetable'
 elif task.category=='C07' and task.operation=='compare':operation='compare_packages'
 elif task.category=='C13' and task.operation=='compare':operation='compare_rules'
 elif task.category=='C04' and task.facet=='players_max':operation='relation_lookup'
 if task.ambiguities:operation='clarification_required'
 inputs,completeness=SEMANTICS.get(operation,('unsupported operation','must report unsupported_operation'))
 return {**cap,'contract_version':'r135-executors-v3','semantic_operation':operation,'input_requirements':inputs,
  'allowed_source_kinds':SOURCE_KINDS.get(task.category,[]),'completeness_rule':completeness,
  'external_dependency':'wordpress' if task.category=='C12' else None,'cost_class':'live_read' if task.category=='C12' else 'local_read',
  'response_contract':'r135-executor-result-v3','arbitrary_unlisted_operations_supported':False}
