from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
def patch(path,old,new):
 p=S/path;t=p.read_text(encoding='utf-8');assert t.count(old)==1,(path,t.count(old));p.write_text(t.replace(old,new),encoding='utf-8')
patch('app/knowledge/common/answer.py','operation_faqs,control_projection','operation_faqs,control_projection,calendar_ids')
patch('app/knowledge/common/answer.py',"        scope_ids=list(ids)\n        procedure_ids", "        scope_ids=list(ids)\n        if query_operation=='calendar':\n            calendar_scope,target_date=calendar_ids(question,records,at)\n            if calendar_scope:\n                ids=calendar_scope;scope_ids=list(ids);method='common_calendar_date_scope'\n                # Closure validity is evaluated at the requested local date.\n                if any(records[rid]['kind']=='closure' for rid in ids):\n                    from zoneinfo import ZoneInfo\n                    at=datetime.combine(target_date,datetime.min.time(),tzinfo=ZoneInfo('Asia/Bangkok'))\n        if query_operation=='people' and not ids:\n            ids=[rid for rid,r in records.items() if r['kind']=='person'];method='common_people_directory'\n        procedure_ids")
patch('app/knowledge/common/answer.py',"        if method=='common_procedure_topic':requested=['answer'];broad=False", "        if method=='common_calendar_date_scope':\n            requested=(['state','reason','open_periods','bookable_periods'] if any(records[rid]['kind']=='closure' for rid in ids) else field_requests(q,{'schedule'}) or ['bookable_periods','maintenance_periods']);broad=False\n        if method=='common_people_directory':requested=['display_name','team','role'];broad=False\n        if method=='common_procedure_topic':requested=['answer'];broad=False")
patch('app/knowledge/common/answer.py',"        if method in {'common_procedure_topic','published_semantic_candidates'}", "        if method in {'common_calendar_date_scope','common_people_directory'}:review=False;gaps=[]\n        if method in {'common_procedure_topic','published_semantic_candidates'}")
# Presentation meanings, not factual content.
import json
p=S/'app/knowledge/common/answer_profiles.json';d=json.loads(p.read_text(encoding='utf-8'));d.setdefault('labels',{})
for kind,labels in {'competition_rule':{'heading':'Rule topic','text':'Rule details','section_number':'Section'},'control_set':{'bindings':'Controls','limitations':'Control notes','platform':'Platform'},'rate':{'amount_minor':'Price','service_id':'Service','audience_id':'User group','duration_minutes':'Duration (minutes)','persons_min':'Minimum users','persons_max':'Maximum users'},'person':{'display_name':'Name','team':'Group','role':'Role'}}.items():
 for key,v in labels.items():d['labels'].setdefault(kind,{}).setdefault(key,{})['en']=v
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('calendar/date/directory scopes and labels')
