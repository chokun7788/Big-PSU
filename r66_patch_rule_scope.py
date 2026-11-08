from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
def patch(path,old,new):
 p=S/path;t=p.read_text(encoding='utf-8');assert t.count(old)==1,(path,t.count(old));p.write_text(t.replace(old,new),encoding='utf-8')
patch('app/knowledge/common/answer.py',"        ids,query_operation=primary_ids(question,ids,records)","        matched_ids=list(ids)\n        ids,query_operation=primary_ids(question,ids,records)")
patch('app/knowledge/common/answer.py',"        q=strip_names(q,ids,names) if ids else normal(q)","        q=strip_names(q,list(dict.fromkeys(ids+matched_ids)),names) if ids else normal(q)")
patch('app/knowledge/common/answer.py',"                plan['rule_content_all']=broad_request(raw_query) or not detect_competition_facet(raw_query)","                plan['rule_content_all']=broad_request(q) or overview_request(q) or bool(re.search(r'มีอะไร(?:บ้าง|มั่ง)|ทั้งหมด|(?:what|which)\\s+(?:are\\s+)?(?:the\\s+)?rules\\s*(?:of|for|in|do)?\\s*$',q)) or bool(re.fullmatch(r'(?:กฎ|กฏ|กติกา|rules|rulebook|ตอน|แข่ง|\\s|[?!.,])+',q))")
patch('app/knowledge/common/answer.py',"                children,rule_audit=rule_selection(raw_query,children,full=plan.get('rule_content_all',False) or broad)","                children,rule_audit=rule_selection(q,children,full=plan.get('rule_content_all',False) or broad)")
# Schema lexicon correction is bounded and runs on entity-stripped text only.
patch('app/knowledge/common/answer.py',"        current_kinds={records[k]['kind'] for k in ids}","        current_kinds={records[k]['kind'] for k in ids}\n        if current_kinds:\n            from .schema_language import recover_schema_language\n            q,schema_recoveries=recover_schema_language(q,scope_kinds(current_kinds))\n        else:schema_recoveries=[]")
patch('app/knowledge/common/answer.py',"'confidence_calibrated':False,'request_focus':focus}","'confidence_calibrated':False,'request_focus':focus,'schema_language_recoveries':schema_recoveries}")
print('Rule overview vs specific topics and shared-entity spelling recovery')
