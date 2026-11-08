import sys,json,os
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p))
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from app.core.locale import _catalog_title_pattern
g=RuntimeInputQualityGuard.from_environment();pattern=_catalog_title_pattern()
for q in [',u Call of Duty: Modern Warfare III wss,',',u Delta Force wss,','Is Delta Force available?','Can u play Delta Force?','u, Delta Force is free?','Delta Force','Is The Last of Us Part I available?','มี Call of Duty: Modern Warfare III ไหม','CS2 uses Steam','I like Delta Force, u?']:
    stripped=pattern.sub(' ',q) if pattern else q
    a=g.detector.analyze(q);b=g.detector.analyze(stripped)
    print(json.dumps({'q':q,'residual':stripped,'original_score':a.layout_score,'residual_score':b.layout_score,'residual_reason':b.layout_reason,'direction':b.layout_direction},ensure_ascii=False),flush=True)
    if a.repeat_score>=.55:
        print(json.dumps({'repeat':a.repeat_candidate_preview,'spans':[vars(x) for x in a.repeat_spans]},ensure_ascii=False),flush=True)
        if a.repeat_candidate_preview:
            c=g.detector.analyze(pattern.sub(' ',a.repeat_candidate_preview))
            print(json.dumps({'composed_score':c.layout_score,'composed_reason':c.layout_reason},ensure_ascii=False),flush=True)
