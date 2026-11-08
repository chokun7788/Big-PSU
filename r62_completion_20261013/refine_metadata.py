from pathlib import Path
import json
R=Path(__file__).resolve().parent.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common'
p=R/'schema_descriptions.json';d=json.loads(p.read_text(encoding='utf-8'))
f=d['fields']
f['required_proofs'].setdefault('intent_terms',[]).extend(['เอาอะไรมาแสดง','แสดงสิทธิ์','ยืนยันสิทธิ์'])
f['equipment_included']['intent_groups']=[['kit','equipment','อุปกรณ์'],['covered','included','รวม','ครอบคลุม']]
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=R/'answer_profiles.json';d=json.loads(p.read_text(encoding='utf-8'))
d['kinds']['contact']={'context':[{'when':['channel'],'include':['value']}]}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
