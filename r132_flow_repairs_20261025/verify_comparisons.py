import copy,json,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.projection import title,value
from app.knowledge.common.domain_flow.scope import reference_time,requested_minutes
from app.knowledge.common.domain_flow.comparison_executor import names
from app.knowledge.common.domain_flow.contracts import RequestBudget
engine=Engine.from_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot());index=engine.index;at=reference_time('2026-10-24T12:00:00+07:00');checks={};details=[]
packages=[rid for rid,r in index.records.items() if r['kind']=='rental_package'];pair=None
for a in packages:
 for b in packages:
  ra,rb=index.records[a],index.records[b]
  if a!=b and value(ra,'zone_ids')==value(rb,'zone_ids') and value(ra,'audience_id')==value(rb,'audience_id') and value(ra,'period_label')!=value(rb,'period_label'):pair=(a,b);break
 if pair:break
assert pair
labels=[title(index.records[rid])['th'] for rid in pair];q='เปรียบเทียบราคา '+labels[0]+' กับ '+labels[1];u=Understanding([MeaningTask(q,'rental','C07','compare','amount_thb')],True)
checks['exact_package_names_not_broadened_by_short_aliases']=set(names(index,'rental_package',q))==set(pair)
r=engine.answer(q,'th',at=at,allow_llm=False,understanding=u,budget=RequestBudget(max_model_calls=0));details.append(r)
checks['both_package_options_execute']=set(c['record_id'] for c in r['claims'])==set(pair)
checks['package_comparison_is_table']='|---' in r['answer'] and all(label in r['answer'] for label in labels)
checks['comparison_does_not_sum_options']='รวม ' not in r['answer']
q='นักศึกษา PSU เทียบราคา PC กับ PS5 เล่นอย่างละ 2 ชั่วโมง';u=Understanding([MeaningTask(q,'service_fee','C06','compare','amount')],True)
r=engine.answer(q,'th',at=at,allow_llm=False,understanding=u,budget=RequestBudget(max_model_calls=0));details.append(r)
checks['rate_comparison_is_table']='|---' in r['answer'];checks['no_combined_purchase_total']='รวม ' not in r['answer']
checks['compound_hour_minute_is_single_duration']=requested_minutes('VR 1 ชั่วโมง 30 นาที')==90
q='เปรียบเทียบกติกาแข่งขัน';u=Understanding([MeaningTask(q,'competition_rules','C13','compare','rule_clause')],True)
r=engine.answer(q,'th',at=at,allow_llm=False,understanding=u,budget=RequestBudget(max_model_calls=0));details.append(r)
checks['rule_compare_requires_explicit_editions']=not r['claims'] and r['status']=='missing_input'
out=R/('comparison_verification_'+str(time.time_ns()));out.mkdir();result={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'real_data_changed':False};(out/'RESULT.json').write_text(json.dumps(result,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps(result));print(out);assert result['all_passed']
