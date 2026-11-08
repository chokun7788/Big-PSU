"""Build a fresh R135 training bundle only from artifact-bound reviewed rows.

No model/optimizer is loaded. Historical files are inputs, never overwritten.
The consumer must call training_contract.load_admitted_dataset before training.
"""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app.knowledge.common.domain_flow.training_contract import Artifacts,runtime_contract,prepare_dataset

def main():
    p=argparse.ArgumentParser();p.add_argument('--examples',required=True);p.add_argument('--reviews',required=True);p.add_argument('--inventory',required=True);p.add_argument('--source-ref',required=True);p.add_argument('--tokenizer-config',required=True);p.add_argument('--chat-template');p.add_argument('--model-profile',required=True);p.add_argument('--artifact-root',action='append',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    def read(path):return json.loads(Path(path).read_text('utf8'))
    def rows(path):return [json.loads(line) for line in Path(path).read_text('utf8').splitlines() if line.strip()]
    template=Path(a.chat_template) if a.chat_template else Path(a.tokenizer_config).with_name('chat_template.jinja')
    inventory=read(a.inventory);runtime=runtime_contract(read(a.tokenizer_config),chat_template=template.read_text('utf8') if template.is_file() else None,model_profile=read(a.model_profile));artifacts=Artifacts(*a.artifact_root)
    report=prepare_dataset(a.output,rows(a.examples),rows(a.reviews),artifacts,read(a.source_ref),runtime,expected_keys=inventory['question_keys'],known_exposed=inventory['known_exposed_question_keys'])
    print(json.dumps({'output':str(Path(a.output).resolve()),'ready_for_optimization':report['ready_for_optimization'],'inventory_individually_adjudicated':report['inventory_individually_adjudicated'],'eligible_split_counts':report['eligible_split_counts'],'dataset_issues':report['dataset_issues'],'optimizer_started':False}))
    return 0 if report['ready_for_optimization'] else 2

if __name__=='__main__':raise SystemExit(main())
