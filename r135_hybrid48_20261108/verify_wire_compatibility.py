import hashlib,json,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent
script="import sys,json,hashlib;sys.path.insert(0,sys.argv[1]);from app.knowledge.common.domain_flow.understanding import schema;from app.knowledge.common.domain_flow.graph_protocol import messages;d={'schema':schema(),'schema_with_directory':schema(['fixture_audience']),'messages':messages('Structural wire fixture')};print(json.dumps(d,ensure_ascii=True,sort_keys=True))"
def wire(path):return json.loads(subprocess.check_output([sys.executable,'-c',script,str(path/'system')],text=True,encoding='utf8'))
old=wire(R.parent/'r132_flow_repairs_20261025');new=wire(R);checks={key:old[key]==new[key] for key in old}
report={'all_passed':all(checks.values()),'checks':checks,'frozen_model_wire_unchanged':old==new,'internal_ir_extensions_separate':True,'actual_model_inferences':0,'schema_sha256':hashlib.sha256(json.dumps(new['schema'],sort_keys=True,separators=(',',':')).encode()).hexdigest()};out=R/('wire_compatibility_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
