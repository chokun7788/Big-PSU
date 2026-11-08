"""Offline consumer; failed admission exits before any model framework import."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app.knowledge.common.domain_flow.training_optimizer import AdmissionBlocked,Artifacts,run_optimizer

def main():
    p=argparse.ArgumentParser();p.add_argument('--dataset',required=True);p.add_argument('--runtime-contract',required=True);p.add_argument('--base',required=True);p.add_argument('--base-manifest-ref',required=True);p.add_argument('--protocol-ref',required=True);p.add_argument('--artifact-root',action='append',required=True);p.add_argument('--output');p.add_argument('--check-only',action='store_true');a=p.parse_args()
    if not a.check_only and not a.output:p.error('--output is required for optimization')
    def read(path):return json.loads(Path(path).read_text('utf8'))
    try:runtime=read(a.runtime_contract);manifest=read(a.base_manifest_ref);protocol=read(a.protocol_ref)
    except (ValueError,FileNotFoundError,KeyError) as exc:
        print(json.dumps({'phase':'configuration_rejected','admitted':False,'error':str(exc),'model_frameworks_loaded':[],'production_installed':False}));return 2
    try:
        result=run_optimizer(a.dataset,Artifacts(*a.artifact_root),runtime,a.base,manifest,protocol,a.output,check_only=a.check_only)
        print(json.dumps(result,ensure_ascii=False));return 0
    except AdmissionBlocked as exc:
        print(json.dumps({'phase':'admission_blocked','admitted':False,'error':str(exc),'model_frameworks_loaded':[m for m in ['torch','transformers','peft','bitsandbytes'] if m in sys.modules],'production_installed':False},ensure_ascii=False));return 2
    except Exception as exc:
        failed=Path(a.output or '')/'FAILED.json';state=read(failed) if failed.is_file() and not isinstance(exc,FileExistsError) else {}
        print(json.dumps({'phase':'failed_after_admission','admitted':True,'error':str(exc),'model_frameworks_loaded':[m for m in ['torch','transformers','peft','bitsandbytes'] if m in sys.modules],
                         'optimizer_steps_completed':state.get('optimizer_steps_completed'),'optimizer_step_attempts':state.get('optimizer_step_attempts'),'actual_weight_updates':state.get('actual_weight_updates'),'production_installed':False},ensure_ascii=False));return 1

if __name__=='__main__':raise SystemExit(main())
