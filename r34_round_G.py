from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=P/'app/core/task_frame_recovery.py';s=p.read_text(encoding='utf-8')
old="re.finditer(r'ไม่|ห้าม|อย่า|เกิน|กี่นาที";assert s.count(old)==1
s=s.replace(old,"re.finditer(r'ไม่|ห้าม|อย่า(?!ง)|เกิน|กี่นาที")
old="if any(n in observed and n not in target for n in ('ไม่','ห้าม','อย่า','เกิน')):continue";assert s.count(old)==1
s=s.replace(old,"if any(n in observed and n not in target for n in ('ไม่','ห้าม','เกิน')) or (re.search(r'อย่า(?!ง)',observed) and not re.search(r'อย่า(?!ง)',target)):continue")
p.write_text(s,encoding='utf-8');print('Round G: disambiguate negation อย่า from interrogative อย่างไร')
