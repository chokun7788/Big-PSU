import os,sys,json,time,traceback,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path((OUT/'release_r42_2_path.txt').read_text(encoding='utf-8'))
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
from app.pipeline.retrieval import load_curated_rows,load_competition_fact_cards
from app.pipeline.vector_retrieval import load_vector_index,_game_alias_index
results=[]
for fn in (load_curated_rows,load_competition_fact_cards,load_vector_index,_game_alias_index):
    t=time.perf_counter()
    try:
        r=fn();row=dict(step=fn.__name__,ok=True,length=len(r))
    except Exception:
        row=dict(step=fn.__name__,ok=False,traceback=traceback.format_exc())
    row['elapsed']=round(time.perf_counter()-t,3);results.append(row);print(row,flush=True)
with (OUT/('retrieval_diagnostic_'+time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]+'.json')).open('x',encoding='utf-8') as f:json.dump(results,f,indent=2)
