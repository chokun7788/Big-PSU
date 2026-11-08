"""Audit all distinct saved differences, without assigning semantic scores."""
import collections,json,pathlib,re
R=pathlib.Path(__file__).resolve().parent
groups={}
for line in (R/'PAIRED_REVIEW_INPUT.jsonl').read_text('utf8').splitlines():
 x=json.loads(line);g=groups.setdefault(x['key'],{'key':x['key'],'question':x['question'],'locale':x['locale'],'categories':set(),'literal_changes':collections.Counter(),'old_answer':x['r134_answer'],'previous_r135_answer':x['r135_answer']})
 g['categories'].update(x['categories']);g['literal_changes'][x['outcome']]+=1
for g in groups.values():
 q=g['question'];a=g['previous_r135_answer'];g['categories']=sorted(g['categories']);g['literal_changes']=dict(g['literal_changes'])
 if re.search('operates PSU',q,re.I):
  g.update(review_group='source_identity_authority_gap',disposition='preserve_unknown',basis='EVAL5_OPERATOR_DIAGNOSIS_20261107.json: legacy FAQ lacks unique center binding; typed center operator differs. No authority conclusion.')
 elif 'mechanical' in q.lower():
  g.update(review_group='subtype_definition_not_established',disposition='known_limitation',basis='Generic keyboard usage/label cannot establish a mechanical-switch definition; current guard intentionally withholds.')
 elif 'ระยะเวลาถูกระบุซ้ำ' in a:
  g.update(review_group='duplicate_duration_needs_clarification',disposition='preserve_clarification',basis='Two duration mentions are not independently established as repetition or two sessions; old literal price is not semantic ground truth.')
 elif '13:00–16:00' in a:
  g.update(review_group='formatting_and_calendar_scope',disposition='retain_scope_notice',basis='Hyphen/en-dash literal difference does not prove wrong time; recorded play periods do not prove booking or building hours.')
 elif 'ระบบตรวจสอบส่วนนี้ไม่พร้อม' in a:
  g.update(review_group='runtime_or_receipt_failure',disposition='requires_actual_trial_observation',basis='Saved response alone cannot distinguish source receipt rejection, model protocol, or backend failure. Do not train on it or call it semantic regression.')
 else:
  g.update(review_group='content_or_scope_change',disposition='requires_source_semantic_review',basis='A literal win/loss alone cannot prove applicability, completeness, or correct interpretation.')
 g['semantic_score_assigned']=False
report={'distinct_questions':len(groups),'groups':dict(collections.Counter(g['review_group'] for g in groups.values())),'rows':list(groups.values()),'limitations':'triage of actual saved keys, not causal regression attribution or semantic grading; old R134 conditions differ'}
(R/'PAIRED_REVIEW.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'questions':len(groups),'groups':report['groups']},ensure_ascii=False))
