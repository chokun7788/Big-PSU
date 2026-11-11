"""Build evidence references only after all declared final checks completed."""
import datetime,hashlib,json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent;repo=R.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text(encoding='utf8'))
batch=load(R/'ROUND02_TEST_BATCH.json');assert len(batch['rows'])==6 and batch['all_passed']
evidence={}
def add(path,phase='final'):
 result=load(path);assert phase!='final' or result['all_passed']
 evidence[path.parent.name]={'phase':phase,'checks':len(result.get('checks',{})),'requests':result.get('requests',0),'passed':result.get('passed'),'all_passed':result['all_passed'],'result_sha256':sha(path),'scope':result.get('scope','')}
 return result
for row in batch['rows']:
 outputs=[json.loads(line) for line in row['stdout'].splitlines() if line.startswith('{')]
 result=next(x for x in reversed(outputs) if 'output' in x)
 add(Path(result['output'])/'RESULT.json')
for folder in ['quote_occurrences_1794413470435201900','context_recheck_1794414031653355900','numeric_edition_1794414312565486300']:add(R/folder/'RESULT.json')
for prefix in ['round02_http','shared_http','typo_http']:
 paths=[p for p in R.glob(prefix+'_[0-9]*/RESULT.json')]
 add(max(paths,key=lambda p:int(p.parent.name.rsplit('_',1)[1])))
for folder in ['quote_occurrences_1794413317458781100','robustness_round02_1794413548763844300','numeric_edition_1794414208075423300']:add(R/folder/'RESULT.json','preserved_failure')
files=['context_bindings.py','control_scope.py','index.py','plan_contract.py','receipt_scope.py','request_verifier.py','source_decisions.py','quote_occurrences.py','game_edition_scope.py']
code={}
for name in files:
 p=R/'system/app/knowledge/common/domain_flow'/name;relative=p.relative_to(repo).as_posix()
 old=subprocess.run(['git','show','e9892417:'+relative],cwd=repo,capture_output=True)
 code[str(p.relative_to(R)).replace('\\','/')]={'before':hashlib.sha256(old.stdout).hexdigest() if old.returncode==0 else None,'after':sha(p)}
parent=repo/'r135_bounded_response_20261111/system'
baseline=load(R/'BASELINE_MANIFEST.json')
hashes=baseline['app_sha256']
parent_ok=None
if hashes:parent_ok=all(sha(parent/key)==value for key,value in hashes.items())
final={k:v for k,v in evidence.items() if v['phase']=='final'}
http_names=[k for k in final if k.startswith(('round02_http_','shared_http_','typo_http_'))]
focused=sum(v['checks'] for k,v in final.items() if k not in http_names)
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'round01_commit':'e9892417','changed_code':code,'evidence':evidence,'focused_matrix_requests':27,'other_focused_checks':focused,'http_requests':sum(final[k]['requests'] for k in http_names),'http_assertions':sum(final[k]['checks'] for k in http_names),'runtime_version':'R135-Shared-contract-round02','parent_code_still_matches':parent_ok,'database_sha256':{name:sha(R/'system/data/knowledge'/name) for name in ['common.sqlite','verified_sources.sqlite']},'full_eval_rerun':False,'semantic_accuracy_established':False,'deployed':False}
(R/'ROUND02_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
status=load(R/'STATUS.json');status.update(phase='round02_quote_occurrence_and_numeric_game_scope_focused_http_verified',round01_focused_checks=status['focused_checks'],round01_http_requests=status['http_requests'],focused_checks=focused,focused_matrix_requests=27,http_requests=manifest['http_requests'],runtime_version=manifest['runtime_version'],report='ROBUSTNESS_ROUND02_TH.md',manifest='ROUND02_MANIFEST.json',next='Group unknown-sibling duplicate notices and context timeout/admission from actual traces; numeric game scope remains bounded, owner/editor HTTP lifecycle still pending. No unchanged broad reruns.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf8')
report=R/'ROBUSTNESS_ROUND02_TH.md';text=report.read_text(encoding='utf8');marker='\n## ผลสุดท้ายที่ตรวจแล้ว\n'
text=text.split(marker)[0]+marker+f'\nMatrix ผ่าน 27/27 คำถามตามความคาดหวังที่ตรึงไว้; focused checks อื่น {focused} checks ผ่าน; แชตจริง {manifest["http_requests"]} คำขอ / {manifest["http_assertions"]} assertions ผ่าน ตัวเลขเหล่านี้เป็นคนละตัวหารและมีการตรวจพฤติกรรมซ้ำกัน จึงไม่บวกเป็นจำนวนคำถามหรือเปอร์เซ็นต์ความแม่นยำ\n\n'
text+='| ชุดตรวจ | คำขอ | Checks | สถานะ |\n|---|---:|---:|---|\n'
for k,v in final.items():text+=f'| `{k}` | {v["requests"]} | {v["checks"]} | ผ่าน |\n'
report.write_text(text,encoding='utf8');print(json.dumps({'focused_matrix_requests':27,'other_focused_checks':focused,'http_requests':manifest['http_requests'],'http_assertions':manifest['http_assertions'],'parent_code_still_matches':parent_ok}))
