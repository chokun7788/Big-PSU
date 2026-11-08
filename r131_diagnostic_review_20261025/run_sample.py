"""Reuse the unchanged measured R130 runner; only output directory/jobs differ."""
import os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025'
sys.path.insert(0,str(P));os.environ['PSU_PLANNER_PROFILE']='retained'
import run_common
run_common.R=R
run_common.S=P/'system'
if __name__=='__main__':raise SystemExit(run_common.main())
