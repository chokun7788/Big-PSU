"""Owner task readiness compiled from the SAME graph registry as chat."""
from .task_contracts import TASKS
from .read_graph import compile
from .registry import value,CATALOG

def check(node,records,lang):
    if node.op=='field':
        r=records.get(node.record_id,{})
        f=r.get('fields',{}).get(node.key,{})
        v=f.get('value');missing=[]
        if f.get('status')!='known':missing.append({'record_id':node.record_id,'field':node.key,'reason':f.get('status','unknown')})
        elif isinstance(v,dict) and set(v)=={'th','en'} and not v.get(lang):missing.append({'record_id':node.record_id,'field':node.key,'reason':'missing_language'})
        return {'ready':not missing,'missing':missing}
    if node.op=='not_applicable':return {'ready':True,'missing':[]}
    if node.op=='missing':return {'ready':False,'missing':[{'relation':node.reason,'reason':'missing_relation_or_field'}]}
    rows=[check(c,records,lang) for c in node.children]
    if node.op=='optional':return {'ready':True,'missing':[],'optional':rows}
    if node.op=='any_of' and any(r['ready'] for r in rows):return {'ready':True,'missing':[]}
    return {'ready':bool(rows) and all(r['ready'] for r in rows),'missing':[m for r in rows for m in r['missing']]}

def readiness(record,records,locale='th'):
    scope={**records,record['record_id']:record};rows=[]
    for task,contract in TASKS.items():
        if record['kind'] not in contract.kinds or task=='schema_attributes':continue
        graph,ids,edges=compile(task,[record['record_id']],scope,fields=contract.fields)
        report=check(graph,scope,locale)
        rows.append({'task':task,'meaning':contract.meaning,'status':'data_ready' if report['ready'] else 'needs_data',
          'missing':report['missing'],'read_paths':edges,'record_ids':ids,'same_runtime_graph':True})
    return {'version':'r101','tasks':rows,'publication_approval_created':False,'runtime_semantics_verified':False}
