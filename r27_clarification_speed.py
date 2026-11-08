import json,sys,time,urllib.request,statistics
from r27_fixture import REPORT
port=sys.argv[1];run=sys.argv[2]
queries=[('th','กติกาแข่งขันมีอะไรบ้าง'),('en','What are the tournament rules?'),('th','สอบถามหน่อยครับ กฎการแข่งขันมีอะไรบ้าง'),('en','Hello, what are the competition rules?')]
rows=[]
for iteration in range(2):
    for locale,q in queries:
        start=time.perf_counter();payload={'question':q,'locale':locale,'experimental_allow_llm':True,'experimental_rag_fallback':True,'recent_history':[],'debug':True}
        response=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:'+port+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
        rows.append({'question':q,'iteration':iteration,'locale':locale,'elapsed':round(time.perf_counter()-start,4),'passed':'clarification' in response['mode'] and response['route_category']=='competition_rules','response':response})
result={'total':len(rows),'passed':sum(r['passed'] for r in rows),'median':statistics.median(r['elapsed'] for r in rows),'max':max(r['elapsed'] for r in rows),'cases':rows}
with (REPORT/(run+'_clarification_speed.json')).open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
