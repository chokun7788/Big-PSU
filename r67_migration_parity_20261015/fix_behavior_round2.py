from pathlib import Path
H=Path(__file__).resolve().parent/'system/app/knowledge/common'
p=H/'answer.py';s=p.read_text('utf8')
s=s.replace('out=render_bindings(v,raw_query,lang)','out=render_bindings(v,q,lang)')
s=s.replace('out=control_projection(display,raw_query,lang) or text(display,lang)','out=control_projection(display,q,lang) or text(display,lang)')
s=s.replace("            if plan.get('uncovered_source_scope'):errors.append('uncovered_source_scope:'+plan['uncovered_source_scope'])\n",'')
s=s.replace("                plan['uncovered_source_scope']='outside_food_conditions'", "                plan['uncovered_source_scope']='outside_food_conditions'\n                plan.setdefault('scope_limits',[]).append({'requested':'outside_food_conditions','status':'not_confirmed','reason':'source_only_covers_consumption_area'})")
old="            ids=candidates[:1];method='common_faq_topic' if query_operation=='policy' else 'common_procedure_topic'\n            if query_operation not in {'checkin','policy'}:query_operation='booking'"
new="""            ids=candidates[:1]
            intent=value(records[ids[0]],'intent_key') or ''
            if 'food' in intent or 'drink' in intent:query_operation='policy'
            elif intent.startswith('schedule_'):query_operation='calendar'
            elif query_operation not in {'checkin','policy'}:query_operation='booking'
            method='common_faq_topic' if query_operation=='policy' else 'common_procedure_topic'"""
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf8')
print('Fixed entity-number leakage in control projection and scoped partial validation')
