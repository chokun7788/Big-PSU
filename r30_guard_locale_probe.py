import sys,json,os
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p))
os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from app.pipeline.input_recovery import inspect_surface_input
g=RuntimeInputQualityGuard.from_environment()
for q in ['ปุ่ม','เพลย์ห้าคิกตังเท่าไหรอะ','วันนี้เปืดั้ย','วีอาราค่าเทาไหร','ติดต่าทาไงหน','ฟสสนไำก','The Last of Us Part I / Part II ราคาเท่าไหร่']:
    a=g.inspect(q);print(json.dumps({'q':q,'guard':a.to_log_dict(),'surface':vars(inspect_surface_input(q))},ensure_ascii=False))
