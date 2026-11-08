from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=ROOT/'app/booking/live_status.py';s=p.read_text(encoding='utf-8')
s=s.replace("q = re.sub(r'\\b\\d{4}-\\d{2}-\\d{2}\\b',' ',q)","q = re.sub(r'(?<!\\d)\\d{4}-\\d{2}-\\d{2}(?!\\d)',' ',q)")
s=s.replace(r'\b([01]?\d|2[0-3]):([0-5]\d)\s*',r'(?<![\d:])([01]?\d|2[0-3]):([0-5]\d)\s*')
s=s.replace(r'\b([01]?\d|2[0-3])\s*(?:โมง)?\s*(?:-|–|to|until|ถึง)\s*([01]?\d|2[0-3])\s*(?:โมง)?\b',r'(?<![\d:])([01]?\d|2[0-3])\s*(?:โมง)?\s*(?:-|–|to|until|ถึง)\s*([01]?\d|2[0-3])\s*(?:โมง)?(?![\d:])')
s=s.replace('    compact_station_patterns = (','    compact_station_patterns = (\n        ("vr", r"\\bvr\\s*#?\\s*0?\\d{1,2}\\b"),')
p.write_text(s,encoding='utf-8')
print('clock/date boundaries corrected')
