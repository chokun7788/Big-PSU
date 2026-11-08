import os, sys, runpy
from r40_targeted_probe import run
port=int(sys.argv[1])
minor=sys.argv[2] if len(sys.argv)>2 else '3'
os.environ.pop('R40_CASE_FILE',None)
run(port,f'final_r40_{minor}_targeted')
os.environ['R40_CASE_FILE']='r40_holdout_cases.json'
run(port,f'final_r40_{minor}_transfer')
os.environ['R40_CASE_FILE']='r40_boundary_cases.json'
run(port,f'final_r40_{minor}_boundary')
os.environ['R40_CASE_FILE']='r40_mixed_cases.json'
run(port,f'final_r40_{minor}_mixed')
sys.argv=['r40_adjacent_http.py',str(port)]
runpy.run_path('r40_adjacent_http.py',run_name='__main__')
