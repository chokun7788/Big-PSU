import sys,runpy,shutil
from pathlib import Path
import harness
mode=sys.argv[1];p=Path(sys.argv[2]);out=harness.B/(mode+'_smokes');db=out/(p.stem+'.sqlite')
harness.test_temp(mode+'_smoke_'+p.stem)
shutil.copy2(harness.B/(mode+'.sqlite'),db)
harness.configure(mode,False,db)
sys.argv=[str(p),*sys.argv[3:]]
runpy.run_path(str(p),run_name='__main__')
