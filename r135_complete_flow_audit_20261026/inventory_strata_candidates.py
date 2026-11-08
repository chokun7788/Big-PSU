"""Inventory candidate strata from real reviewed rows, without semantic closure.

Flags are search aids. They are not proof of semantic coverage, a new gold
review, a fresh holdout, or permission to optimize a stale dataset.
"""
import collections,copy,json,re,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha,digest
W=R/'training_review_workbench_1793037663397671000';A=W/'protocol_v3_admission_1793109982985437000';O=R/('strata_candidate_inventory_'+str(time.time_ns()));O.mkdir()
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(x) for x in p.read_text('utf8').splitlines() if x.strip()]
examples=rows(A/'EXAMPLES.jsonl');reviews={x['question_key']:x for x in rows(A/'REVIEWS.jsonl')};admission={x['question_key']:x for x in read(A/'bundle/ADMISSION.json')['rows']};amend=read(W/'semantic_amendments_round014/AMENDMENT_266.json')
assert len(examples)==len(reviews)==len(admission)==289
families=collections.defaultdict(set);cores=collections.defaultdict(set);counts=collections.Counter();candidates={str(i):[] for i in range(1,9)};items=[]
for x in examples:
 row=x['annotation_provenance']['historical_review_ref']['line']-1;q=x['raw_question'];label=copy.deepcopy(x['plan_label']);r=reviews[x['question_key']];a=admission[x['question_key']]
 if row==266:
  assert amend['question_key']==x['question_key'];label=copy.deepcopy(amend['reviewed_label'])
 tasks=label['tasks'];constraints=[c for t in tasks for c in t.get('constraints',[])];issues=r.get('unresolved_issues',[]);issue_text=json.dumps(issues,ensure_ascii=False).casefold()
 domain_set={t['domain'] for t in tasks};locale='th' if re.search(r'[\u0e00-\u0e7f]',q) else 'en'
 flags=[len(tasks)==1 and tasks[0]['domain']!='general',len(domain_set)>1,bool(label.get('shared_bindings')),any(c.get('slot') in {'negation','condition'} for c in constraints),any(t.get('operation') in {'compare','list','count'} for t in tasks),any(t.get('ambiguous') for t in tasks),any(s in issue_text for s in ['conflict','validity','unavailable','currentness','effective interval']),any(t.get('domain')=='competition_rules' for t in tasks) and bool(re.search(r'20\d\d|edition|rulebook|rule|กติกา|แข่ง',q,re.I))]
 for n,flag in enumerate(flags,1):
  if flag:candidates[str(n)].append(row)
 for family in [x['family'],*x['original_families']]:families[family].add(x['split'])
 cores[' '.join(q.casefold().split())].add(x['split']);counts[(x['split'],locale)]+=1
 items.append({'original_row':row,'question_key':x['question_key'],'raw_question':q,'split':x['split'],'locale_candidate':locale,'source_review_state':r['adjudication_status'],'current_admission_eligible':a['eligible'],'passes_existing_dataset_gate_excluding_stale_label':False if row==266 else a['eligible'],'pending_semantic_amendment':row==266,'task_domains':sorted(domain_set),'candidate_strata':[n for n,f in enumerate(flags,1) if f],'unresolved_source_issues':issues})
assert len({x['question_key'] for x in items})==289
report={'version':'r135-strata-candidate-inventory-v1','input_refs':{n:{'path':str((A/n).resolve()),'sha256':file_sha(A/n)} for n in ['EXAMPLES.jsonl','REVIEWS.jsonl','SUMMARY.json']},'row266_amendment_sha256':file_sha(W/'semantic_amendments_round014/AMENDMENT_266.json'),'original_questions':289,'candidate_strata_names':{'1':'single need possibly answerable','2':'multi-domain','3':'shared binding','4':'negation or condition','5':'compare/list/count','6':'ambiguity','7':'recorded source uncertainty/conflict candidate','8':'competition edition/dependency review candidate'},'candidate_counts':{k:len(v) for k,v in candidates.items()},'candidate_rows':candidates,'split_locale_counts':{a+'/'+b:n for (a,b),n in sorted(counts.items())},'known_family_cross_split':{k:sorted(v) for k,v in families.items() if len(v)>1},'normalized_exact_core_cross_split':{k:sorted(v) for k,v in cores.items() if len(v)>1},'fresh_holdout_count':sum(x['split']=='holdout' for x in examples),'stale_amendment_rows':[266],'semantic_stratum_membership_proven':False,'cross_language_paraphrase_families_exhaustively_reviewed':False,'source_truth_or_model_accuracy_proven':False,'optimization_authorized':False,'whole_flow_complete':False,'limitations':['These automatic structural and text flags are candidates for individual semantic review, not evidence of complete coverage.','Known family keys and exact normalized text cannot detect all unrecorded paraphrase or translation relationships.','A frozen historical test exposed to development is not a fresh holdout.','Source unknown/conflict/provider failure cannot be proven by labels or keyword presence.']}
(O/'ITEMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in items),'utf8');report['items_sha256']=file_sha(O/'ITEMS.jsonl');(O/'REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'counts':report['candidate_counts'],'family_cross_split':len(report['known_family_cross_split']),'core_cross_split':len(report['normalized_exact_core_cross_split']),'holdout':report['fresh_holdout_count'],'semantic_coverage_proven':False}))
