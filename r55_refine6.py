from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=ROOT/'app/pipeline/service_query_completion.py';s=p.read_text(encoding='utf-8');s=s.replace("r'ติดตั้ง|โหลด|ลงเพิ่ม|ห้าม", "r'ติดตั้ง|โหลด|ลง.{0,15}เกม|เกม.{0,15}เพิ่ม|ลงเพิ่ม|ห้าม");p.write_text(s,encoding='utf-8')
p=ROOT/'app/pipeline/user_service_facts.py';s=p.read_text(encoding='utf-8');s=s.replace("r'ลงเพิ่ม|โหลดเกม.*เอง|", "r'ลงเพิ่ม|(?:ขอ|ได้ไหม|ได้มั้ย).*ลง.{0,15}เกม|ลง.{0,15}เกม.*(?:ได้ไหม|ได้มั้ย|เพิ่ม)|โหลดเกม.*เอง|");p.write_text(s,encoding='utf-8')
print('installation versus game list kept separate')
