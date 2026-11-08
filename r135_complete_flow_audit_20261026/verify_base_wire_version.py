"""Exercise base validation across v2/v3 without loading model or frameworks."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow import training_optimizer as o
from app.knowledge.common.domain_flow.training_contract import runtime_contract
out=R/('base_wire_version_controls_'+str(time.time_ns()));out.mkdir();base=out/'synthetic_base';base.mkdir()
config={'fixture':'synthetic'};template='synthetic template only';(base/'tokenizer_config.json').write_text(json.dumps(config),'utf8');(base/'chat_template.jinja').write_text(template,'utf8');(base/'config.json').write_text('{}','utf8');(base/'model.safetensors').write_bytes(b'synthetic-not-a-model')
profile={'base_repository':o.CONFIG['base_repository'],'base_revision':o.CONFIG['base_revision'],'precision':o.CONFIG['precision'],'selector_profile':'synthetic','generic_profile':'synthetic'}
manifest={'model_profile':profile,'files':o._files(base)};checks={};errors={}
def allowed(name,rt):
 try:o.verify_base(base,manifest,rt);checks[name]=True
 except Exception as e:checks[name]=False;errors[name]=str(e)
def blocked(name,rt):
 try:o.verify_base(base,manifest,rt);checks[name]=False
 except (ValueError,KeyError) as e:checks[name]=True;errors[name]=str(e)
v2=runtime_contract(config,chat_template=template,model_profile=profile);v3=runtime_contract(config,chat_template=template,model_profile=profile,wire_version='r135-plan-v3');allowed('v2_valid',v2);allowed('v3_valid',v3)
bad=copy.deepcopy(v3);bad['schema_sha256']='0'*64;blocked('forged_v3_schema',bad)
bad=copy.deepcopy(v3);bad['wire_version']='unsupported';blocked('unsupported_wire',bad)
bad=copy.deepcopy(v3);bad['chat_template_sha256']='0'*64;blocked('changed_template',bad)
result={'checks':checks,'errors':errors,'all_passed':all(checks.values()),'synthetic_bytes_only':True,'actual_training':False};(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n','utf8');print(json.dumps({'path':str(out),**result}));assert result['all_passed']
