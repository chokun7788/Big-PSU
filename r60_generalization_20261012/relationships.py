import sys,json
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
from evaluate import score
store=t.OneReleaseStore(t.DB).freeze();records=store.frozen['release']['records'];a=t.CommonAnswerer(store)
rows=[]
for lang in ('th','en'):
    for kind,keys in [('game_service',['offered']),('game_service',['game_version']),('game_service',['installed_resource_ids']),('game_service',['account_policy_id']),('control_set',['input_device']),('control_set',['preset']),('control_set',['limitations']),('game_mode',['network_requirement'])]:
        parent=t.rid('game',3);child=t.rid(kind,3)
        q=records[parent]['aliases'][lang][0]+' '+' '.join(keys)
        c={'id':kind+'-'+keys[0]+'-'+lang,'rid':child,'kind':kind,'lang':lang,'question':q,'expected_fields':keys}
        ans=a.answer(q,locale=lang,at=t.AT);ok,why,quality=score(ans,c,records)
        rows.append({**c,'passed':ok,'reasons':why,'quality':quality,'answer':ans.answer if ans else None,'decision':ans.decision_artifact if ans else None})
with (B/'RELATIONSHIP_RESULTS.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
summary={'cases':len(rows),'passed':sum(r['passed'] for r in rows),'failed':[{k:r[k] for k in ['id','reasons']} for r in rows if not r['passed']],'llm':False,'db_unchanged':store.still_current(store.frozen)}
(B/'RELATIONSHIP_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(summary)
