"""Actual local dependency positive/negative controls, without model loading."""
import hashlib,json,os,subprocess,sys,time,urllib.request
from verification_support import R
from app.knowledge.common.domain_flow.model_environment import PYTHON,PACKAGES
O=R/('model_environment_'+str(time.time_ns()));O.mkdir();probe=R/'system/tools/check_selected_model_environment.py';checks={};details=[]
def health():
 with urllib.request.urlopen('http://127.0.0.1:12921/health',timeout=5) as response:return json.load(response)
before=health();details.append({'current_serving_before':before})
for name,python in [('selected',str(PYTHON)),('bundled',sys.executable)]:
 env=dict(os.environ);env.pop('PYTHONPATH',None)
 proc=subprocess.run([python,'-B',str(probe)],capture_output=True,text=True,env=env,timeout=30)
 observed=json.loads(proc.stdout);details.append({'case':name,'exit_code':proc.returncode,'observation':observed})
 checks[name+'_no_model_or_weights_touched']=not observed['model_loaded'] and not observed['inference_performed'] and not observed['weights_or_packages_modified']
 if name=='selected':checks['existing_selected_runtime_dependencies_match']=proc.returncode==0 and observed['selected_runtime_compatible'] and all(observed['packages'][k]['version']==v for k,v in PACKAGES.items())
 else:checks['bundled_runtime_missing_torch_cannot_pass']=proc.returncode!=0 and not observed['selected_runtime_compatible'] and 'missing_or_different_package:torch' in observed['issues']
proc=subprocess.run(['powershell','-NoProfile','-File',str(R/'Start-Model.ps1'),'-CheckOnly'],capture_output=True,text=True,timeout=60)
checks['candidate_normal_launcher_dependency_and_accelerator_check']=proc.returncode==0 and json.loads(proc.stdout)['cuda_available']
details.append({'case':'candidate_launcher_check_only','exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
proc=subprocess.run(['powershell','-NoProfile','-File',str(R/'Start-Model.ps1')],capture_output=True,text=True,timeout=15)
checks['healthy_selected_endpoint_reused_without_restart']=proc.returncode==0
after=health();details.append({'current_serving_after':after});checks['actual_serving_pid_and_weight_identity_preserved']=before==after
script=R/'Start-Model.ps1';report={'all_passed':all(checks.values()),'checks':checks,'candidate_launcher_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'actual_model_loads_inferences_training':0,'protected_model_stopped':False,'installed_launcher_modified':False,'cold_start_via_candidate':'pending normal-entrypoint installation acceptance; current protected endpoint deliberately reused','not_whole_flow_acceptance':True}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
