"""New report, same frozen facts. Gold changes only account for human enum display."""
import sys,json,time,os,collections,traceback
from pathlib import Path
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parent/'r60_generalization_20261012'))
import evaluate as e
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.planner import plan_fields
from app.pipeline.request_deadline import request_deadline
# Independent semantic oracle: do not import runtime rendering or field resolver.
ENUM_GOLD={
 'decision':{'allowed':('อนุญาต','Allowed'),'prohibited':('ไม่อนุญาต','Prohibited'),'required':('จำเป็น','Required'),'conditional':('มีเงื่อนไข','Conditional')},
 'calculation_rule':{'fixed':('ราคาคงที่ตามรายการ','Fixed rate'),'linear':('คำนวณตามสัดส่วนที่ระบุ','Confirmed proportional calculation'),'no_extrapolation':('ห้ามขยายราคาจากรายการนี้เอง','Do not extrapolate this rate')},
 'state':{'closed':('ปิดบริการ','Closed'),'modified_hours':('เปลี่ยนเวลาบริการ','Modified hours'),'open_override':('เปิดเป็นกรณีพิเศษ','Special opening')}}
OPS={'eq':('เท่ากับ','equals'),'ne':('ไม่เท่ากับ','does not equal'),'gte':('อย่างน้อย','at least'),'lte':('ไม่เกิน','at most'),'in':('อยู่ใน','is one of')}
old_leaves=e.leaves
def semantic_leaves(v,key,lang,records):
 if isinstance(v,str) and v in ENUM_GOLD.get(key,{}):return [ENUM_GOLD[key][v][lang=='en']]
 if key in {'conditions_all','preconditions'}:
  return [z for c in v for z in [c['field'].replace('_',' '),OPS.get(c['operator'],(c['operator'],c['operator']))[lang=='en'],*old_leaves(c['value'],'value',lang,records)]]
 return old_leaves(v,key,lang,records)
e.leaves=semantic_leaves
def main():
 mode=sys.argv[1];out=B/(sys.argv[2] if len(sys.argv)>2 else 'semantic_'+mode);out.mkdir(exist_ok=False)
 store=e.t.OneReleaseStore(e.t.DB).freeze();records=store.frozen['release']['records'];reader=CommonAnswerer(store)
 rows=json.loads((B.parent/'r61_implementation_20261013/DEVELOPMENT.json').read_text(encoding='utf-8'))
 rows+=json.loads((B.parent/'r60_generalization_20261012/RESERVED.json').read_text(encoding='utf-8'))
 result=[]
 with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f:
  for n,c in enumerate(rows,1):
   c=dict(c);c['rid']=e.t.rid(c['kind'],c['profile']);alias=records[c['rid']]['aliases'][c['lang']][0]
   c['question']=c['phrase'] if c.get('history') else alias+' '+c['phrase']
   history=[{'role':'user','content':alias+(' ขอข้อมูลทั้งหมด' if c['lang']=='th' else ' Show all information')}] if c.get('history') else []
   audits=[]
   def planner(q,recs,ids):return plan_fields(q,recs,ids,diagnostic=audits.append)
   started=time.perf_counter()
   try:
    with request_deadline(19):ans=reader.answer(c['question'],locale=c['lang'],history=history,at=e.t.AT,planner=planner if mode=='llm' else None)
    ok,why,quality=e.score(ans,c,records)
    r={**c,'passed':ok,'reasons':why,'quality':quality,'answer':ans.answer if ans else None,'decision':ans.decision_artifact if ans else None,'audits':audits,'elapsed_sec':time.perf_counter()-started}
   except Exception:r={**c,'passed':False,'reasons':['exception'],'exception':traceback.format_exc()}
   result.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
   if n%10==0:print(n,len(rows),sum(x['passed'] for x in result),flush=True)
 counts=collections.defaultdict(collections.Counter)
 for r in result:
  for key in ['all',r['lang'],r['style'],r['kind']]:counts[key]['passed' if r['passed'] else 'failed']+=1
 summary={'cases':len(result),'passed':sum(r['passed'] for r in result),'counts':dict(counts),'failures':[{'id':r['id'],'reasons':r['reasons']} for r in result if not r['passed']],'actual_llm_enabled':mode=='llm','fixture_only':True,'independent_expected_field_sets':True,'known_heldout_previously_seen':True,'semantic_correctness_universally_verified':False,'epoch_unchanged':store.still_current(store.frozen)}
 (out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
