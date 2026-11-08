"""Candidate launchers, isolated evaluation identity and evidence summary."""
import json,pathlib,hashlib
R=pathlib.Path(__file__).resolve().parent;repo=R.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
text=(repo/'r135_eval5_20261107/Start-Eval.ps1').read_text(encoding='utf-8-sig')
text=text.replace('[int]$Port = 8115','[int]$Port = 8125').replace('data\knowledge\eval5.sqlite','data\knowledge\common.sqlite')
text=text.replace("& (Join-Path (Split-Path -Parent $taskRoot) 'PSU_Esports_Chat_Current_R134\Start-Model.ps1')", "& (Join-Path $taskRoot 'Start-Model.ps1')")
text=text.replace('r135-eval5-experimental','r135-hybrid48-trial').replace('R135-eval5','R135-Hybrid48')
# Start the chat first with its existing model endpoint. Starting a missing
# model is a separate launcher, not an implicit change to a running model.
text=text.replace("& (Join-Path $taskRoot 'Start-Model.ps1')", "# Reuse the configured model; run Start-Model.ps1 separately if it is absent.")
(R/'Start-Trial.ps1').write_text(text,encoding='utf8')
model=(repo/'PSU_Esports_Chat_Current_R134/Start-Model.ps1').read_text(encoding='utf-8-sig')
model=model.replace("$taskName = 'model_r132_retained_'", "$taskName = 'model_hybrid48_retained_'")
model=model.replace("$taskProc = Start-Process", "$taskReceiptRoot = Join-Path $PSScriptRoot 'runtime\\model-receipts'\n[IO.Directory]::CreateDirectory($taskReceiptRoot) | Out-Null\n$taskReceiptPath = Join-Path $taskReceiptRoot $taskName\n$taskProc = Start-Process")
model=model.replace("'--output-name',$taskName", "'--output-name',('\"'+$taskReceiptPath+'\"')")
(R/'Start-Model.ps1').write_text(model,encoding='utf8')
editor=(repo/'PSU_Esports_Chat_Current_R134/Open-Data-Editor.ps1').read_text(encoding='utf-8-sig').replace('8116','8126').replace('R134 data editor','R135 Hybrid48 isolated data editor')
(R/'Open-Data-Editor.ps1').write_text(editor,encoding='utf8')
(R/'Open-Trial.cmd').write_text('@echo off\r\npowershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-Trial.ps1"\r\n',encoding='utf8')
ev=R/'evaluation'
p=ev/'run_eval.py';s=p.read_text(encoding='utf8').replace("ROOT=Path(__file__).resolve().parent.parent", "ROOT=Path(__file__).resolve().parents[2]")
s=s.replace('http://127.0.0.1:8118/','http://127.0.0.1:8125/').replace("BUILD='common-r134-resolution-scope'","BUILD='common-r135-hybrid48-trial'").replace('R135-eval5','R135-Hybrid48').replace('eval-r135-5pct-','eval-hybrid48-5pct-').replace('Fresh R134 HTTP sample','Fresh hybrid48 HTTP sample')
s=s.replace(" if x.get('runtime',{}).get('version')", " if x.get('common_loaded_build',{}).get('build_id')!=BUILD:raise RuntimeError('wrong candidate build')\n if x.get('runtime',{}).get('version')")
s=s.replace("progress(True)\nwith (OUT/", "if (OUT/'RESULTS.jsonl').exists():raise RuntimeError('existing measured results must not be overwritten or resumed silently')\nprogress(True)\nwith (OUT/")
p.write_text(s,encoding='utf8')
p=ev/'score_results.py';s=p.read_text(encoding='utf8').replace("O=Path(__file__).resolve().parent;R=O.parent", "O=Path(__file__).resolve().parent;R=O.parent.parent")
s=s.replace("sys.path.insert(0,str(R/'r132_flow_repairs_20261025/system'))", "sys.path.insert(0,str(O.parent/'system'))")
p.write_text(s,encoding='utf8')
latest=json.loads((R/'FOCUSED_BATCH.json').read_text('utf8'))
summaries={}
for group in ['hybrid_routes','hybrid_finance','hybrid_ranges']:
    p=sorted(R.glob(group+'_*/RESULT.json'))[-1];summaries[group]={'path':str(p.relative_to(R)),**json.loads(p.read_text('utf8'))}
ready=latest['all_passed'] and all(x['all_passed'] for x in summaries.values())
gates={'source_critical_checks_passed':ready,'http_smoke_passed':False,'ready_for_eval':False,'summaries':summaries,
 'focused_batch':'FOCUSED_BATCH.json','limits':['mechanical subtype definition intentionally withheld','operator FAQ target/authority unresolved','range labels do not establish allocation/group billing','14-category bounded lanes are not full operation acceptance','model and live backend not established by source tests']}
(R/'GATES.json').write_text(json.dumps(gates,ensure_ascii=False,indent=2),'utf8')
policy=R/'system/app/knowledge/common/domain_flow/hybrid_routes.json';data=json.loads(policy.read_text('utf8'))
for key,row in data['routes'].items():
 row['acceptance']='experimental_runtime_receipt_checks_required'
 row['evidence']='FOCUSED_BATCH.json; GATES.json; semantic acceptance remains per request'
 if key=='C03|detail|device_type':row['acceptance']='bounded_source_lifecycle_and_natural_route_passed';row['evidence']=summaries['hybrid_routes']['path']
policy.write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf8')
(R/'CAPABILITY_MATRIX.json').write_text(json.dumps({'rows':[{'key':k,**v} for k,v in sorted(data['routes'].items())],'whole_category_acceptance':False,'request_source_and_coverage_verification_required':True},ensure_ascii=False,indent=2),'utf8')
files=[{'path':str(p.relative_to(R)).replace('\\','/'),'sha256':sha(p)} for p in sorted((R/'system').rglob('*')) if p.is_file() and p.suffix in {'.py','.json','.js','.html','.css'} and '__pycache__' not in p.parts and 'data' not in p.relative_to(R/'system').parts]
(R/'CANDIDATE_MANIFEST.json').write_text(json.dumps({'files':files,'source_snapshot_sha256':sha(R/'system/data/knowledge/common.sqlite'),'selection_sha256':sha(ev/'SELECTED_5_PERCENT_v2.jsonl'),'frozen_for_measurement':False,'model_unchanged':True},indent=2),'utf8')
print(json.dumps({'source_gates':ready,'route_count':len(data['routes']),'files':len(files)}))
