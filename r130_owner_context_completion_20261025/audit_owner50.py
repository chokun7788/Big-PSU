"""Exhaustive submission-to-record scope audit, not a new answer test."""
import hashlib,json,re,sys,unicodedata
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import value
def norm(s):return re.sub(r'[^\w\u0e00-\u0e7f]','',unicodedata.normalize('NFKC',s).casefold())
origin=B/'r107_owner_questions_20261020/owner_update_50';source=json.loads((origin/'SOURCE_OWNER_50.json').read_text('utf8'));prefill=json.loads((origin/'PREFILL_PAYLOAD.json').read_text('utf8'))['answers'];later=json.loads((B/'r109_owner_answers_20261020/SOURCE_STATE.json').read_text('utf8'))['responses']['answers']
snapshot=MigratedView(R/'system/data/knowledge/common.sqlite').snapshot();records=snapshot['release']['records'];rows=[]
for item in source['source_items']:
 number=item['number'];forms={k:v for k,v in prefill.items() if number in v.get('source_items',[])};matched=[]
 for rid,r in records.items():
  if r['kind']!='faq':continue
  question=value(r,'question') or {};qs=list(question.values()) if isinstance(question,dict) else [str(question)]
  exact=any(norm(q)==norm(item['question']) for q in qs)
  form_keys=[k for k in forms if re.fullmatch(r'Q\d+',k) and rid.lower()=='r114_'+k.lower()+'_owner_policy']
  if exact or form_keys:matched.append({'record_id':rid,'matching_basis':'exact_original_question' if exact else 'known_intake_question_mapping','form_keys':form_keys,'question':question,'answer':value(r,'answer'),'scope_note':value(r,'scope_note'),'revision':r['revision']})
 groups=[k for k in forms if k.startswith('inventory:')]
 row={'number':number,'question':item['question'],'original_answer':item['answer'],'original_usable':item['usable_answer'],'intake_form_keys':list(forms),'intake_scope_notes':list(dict.fromkeys(v.get('note','') for v in forms.values() if v.get('note'))),'matched_active_records':matched,'later_clarifications':{k:later[k] for k in forms if k in later},'inventory_confirmation':later.get('group_inventory') if groups else None,'scope_requires_semantic_review':True}
 rows.append(row)
result={'items':rows,'source_items_reviewed':len(rows),'active_snapshot':{'release_id':snapshot['active'],'epoch':snapshot['epoch']},'no_business_fact_inferred_from_matching':True,'matching_is_not_source_completeness_proof':True}
(R/'OWNER50_SCOPE_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
for row in rows:print(str(row['number'])+' '+row['question']+' => '+','.join(r['record_id'] for r in row['matched_active_records'])+' | forms '+','.join(row['intake_form_keys'])+' | later '+','.join(row['later_clarifications']))
