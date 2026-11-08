import sys,runpy,os
from pathlib import Path
import r41_variations as variations
import r40_targeted_probe as old
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r41_current_path.txt').read_text(encoding='utf-8'))
port=int(sys.argv[1])
variations.probe.run(str(port),'final_r41_3_variations')
old.OUT=OUT
os.environ.pop('R40_CASE_FILE',None)
old.run(port,'final_r41_3_regression_targeted')
for filename,label in [('r40_holdout_cases.json','transfer'),('r40_boundary_cases.json','boundary'),('r40_mixed_cases.json','mixed')]:
    os.environ['R40_CASE_FILE']=filename
    old.run(port,'final_r41_3_regression_'+label)
sys.argv=['r40_adjacent_http.py',str(port)]
runpy.run_path(str(BASE/'r40_adjacent_http.py'),run_name='__main__')
