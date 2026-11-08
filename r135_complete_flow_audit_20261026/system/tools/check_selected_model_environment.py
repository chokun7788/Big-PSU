"""Local dependency preflight only; does not load a model or run a question."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app.knowledge.common.domain_flow.model_environment import inspect_environment,inspect_accelerator
parser=argparse.ArgumentParser();parser.add_argument('--accelerator',action='store_true');args=parser.parse_args()
result=inspect_environment()
if args.accelerator:result=inspect_accelerator(result)
print(json.dumps(result));sys.exit(0 if result['selected_runtime_compatible'] else 2)
