from pathlib import Path
import json,re,shutil
OUT=Path(__file__).resolve().parent
p=json.loads((OUT/'owner_help_latest.json').read_text(encoding='utf-8'));RUN=Path(p['run']);stage=Path(p['stage'])
data=json.loads((RUN/'help_data.json').read_text(encoding='utf-8'))
js=(stage/'owner.js').read_text(encoding='utf-8')
def const(k):return json.loads(re.search(r'const '+k+r'=(.+?);\n',js).group(1))
labels=const('SUB_LABELS');options=const('OPTION_LABELS');simple=const('SIMPLE_FIELD_LABELS');special=const('SPECIAL_FIELD_LABELS')
cat=json.loads((OUT/'ready_package/PSU_Esports_Chatbot_Local/app/knowledge/common/catalog.json').read_text(encoding='utf-8'))
def readable(x):
    if x is None:return 'เว้นว่าง'
    if isinstance(x,bool):return 'ใช่ / มี / รองรับ' if x else 'ไม่ใช่ / ไม่มี / ไม่รองรับ'
    if isinstance(x,list):return 'ไม่เพิ่มรายการ' if not x else '; '.join('รายการ '+str(i+1)+': '+readable(v) for i,v in enumerate(x))
    if isinstance(x,dict):return ' • '.join(labels.get(k,k)+': '+readable(v) for k,v in x.items())
    return options.get(x,str(x))
doc=(RUN/'OWNER_EASY_GUIDE_TH.md').read_text(encoding='utf-8')
head=doc.split('## ตัวอย่างแต่ละหมวด')[0]
tail='## ข้อที่มักสับสน'+doc.split('## ข้อที่มักสับสน')[1]
body=['## ตัวอย่างแต่ละหมวด','', 'ตัวอย่างเป็นภาษาหน้ากรอก ไม่ต้องเขียน JSON หรือโค้ดเอง ราคาและวันที่ตัวอย่างไม่ใช่ข้อมูลจริงของศูนย์','']
for c in cat:
    h=data['categories'][c['kind']]
    body += ['### '+h['label'],'','**ใช้เมื่อ:** '+h['when'],'','**ช่วยตอบ:** '+h['question'],'','**จำง่าย ๆ:** '+h['tip'],'','**สร้างข้อมูลอื่นก่อนเฉพาะที่ใช้เชื่อม:** '+(' / '.join(data['categories'][k]['label'] for k in h['before'] if k!=c['kind']) or 'เริ่มหมวดนี้ได้เลย'),'','| ช่องที่เห็นในหน้าเว็บ | ต้องมีก่อนเผยแพร่ไหม | ตัวอย่างการกรอก |','|---|---|---|']
    for f in c['fields']:
        key=f['key'];ex=data['fields'][c['kind']][key]['example'];label=special.get(c['kind']+'.'+key,simple.get(key,f['meaning_th']))
        if key=='amount_minor':label='ราคา (บาท)';v=f'{ex/100:,.2f} บาท — กรอก {ex/100:.2f} ในช่อง'
        elif f['reference_kind'] and ex!=[]:v='เลือกชื่อจากหมวด '+(data['categories'][f['reference_kind']]['label'] if f['reference_kind']!='*' else 'ข้อมูลที่เกี่ยวข้อง')+' ที่สร้างไว้ก่อน ไม่ต้องพิมพ์รหัส'
        elif key=='weekday':v=['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์'][ex]
        else:v=readable(ex)
        body.append('| '+label.replace('|','/')+' | '+('★ ต้องมี' if f['publish_core'] else 'ยังไม่ทราบได้')+' | '+v.replace('|','/')+' |')
    body += ['', '**วิธีใช้ตัวอย่าง:** เปิดช่องนี้ในหน้าเว็บ เลือก “มีข้อมูลยืนยัน” แล้วใส่ข้อมูลจริงของศูนย์แทนค่าตัวอย่าง หากยังไม่มีข้อมูลจริงให้คง “ไม่ทราบ” และบันทึกเป็นร่างไว้','']
result=head+'\n'.join(body)+'\n'+tail
(RUN/'OWNER_EASY_GUIDE_TH.md').write_text(result,encoding='utf-8')
for base in (OUT/'ready_package/PSU_Esports_Chatbot_Local',OUT/'system/PSU_Esports_Chatbot_Local'):(base/'owner_content_docs/OWNER_EASY_GUIDE_TH.md').write_text(result,encoding='utf-8')
# Stage the same human-readable guide for a guarded source follow-up.
print('Guide now uses human examples for all 155 fields, no JSON required.')
