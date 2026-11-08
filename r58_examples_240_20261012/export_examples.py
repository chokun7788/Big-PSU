import json,collections
from pathlib import Path
BASE=Path(__file__).resolve().parent
def display(v):
    if isinstance(v,dict) and set(v)=={'th','en'}:return '**ไทย:** '+str(v['th'])+'\n\n**English:** '+str(v['en'])
    return '`'+json.dumps(v,ensure_ascii=False)+'`'
for folder in sorted((BASE/'records').iterdir()):
    lines=['# ตัวอย่างหมวด '+folder.name+' — 10 รายการ','','**DEMO ONLY: ข้อมูลแยก ไม่เกี่ยวกับข้อมูล Product จริง ห้ามใช้ยืนยันบริการ ราคา กฎ หรือสถานะจริงของ PSU**','','คำแปลจัดทำโดยระบบ ยังไม่ได้ตรวจโดยเจ้าของ ข้อมูลเกมอ้างอิงผู้พัฒนา แต่การติดตั้ง เครื่อง ราคา กฎ และปุ่มจำลองไม่ใช่ข้อเท็จจริงของศูนย์','']
    for path in sorted(folder.glob('*.json')):
        r=json.loads(path.read_text(encoding='utf-8'));lines+=['## '+r['aliases']['th'][0],'','รหัส: `'+r['record_id']+'`','']
        for key,f in r['fields'].items():lines+=['### '+key,'',('สถานะ: '+f['status'])+'\n\n'+display(f['value']), '']
    (BASE/('EXAMPLES_'+folder.name+'.md')).write_text('\n'.join(lines),encoding='utf-8')
print('Exported 24 readable category guides')
