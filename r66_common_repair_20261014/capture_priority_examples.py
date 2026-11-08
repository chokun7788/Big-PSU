import sys,json,os
from pathlib import Path
os.environ['PSU_ESPORTS_NOW']='2026-10-14T12:00:00+07:00'
B=Path(__file__).resolve().parent;tag=sys.argv[1];out=B/('PRIORITY_EXAMPLES_'+tag+'.json');assert not out.exists()
sys.path[:0]=[str(B),str(B/'system')]
from test_r66_reader import answer
from grade_legacy import plain
from harness import init,execute
rows=[]
for q,lang in [('ถ้าทำ PS5 เสียหาย ต้องเสียค่าปรับกี่บาท','th'),('If I damage a PS5, how much is the fine?','en'),('How do I cancel a paid booking?','en'),('Is PC #03 available for Warzone today at 15:00?','en')]:
 r=answer(q,lang);rows.append({'question':q,'locale':lang,'common_result':plain(r) if r else None})
init('common',False);q=rows[-1]['question'];pipeline=execute({'key':'r66_priority_capture','question':q,'locale':'en','reference_date':'','entries':[]})
out.write_text(json.dumps({'tag':tag,'llm_enabled':False,'common_config':True,'clock':'2026-10-14T12:00:00+07:00','new_actual_wordpress_oracle':False,'reader_examples':rows,'live_pipeline_example':pipeline},ensure_ascii=False,indent=2),encoding='utf-8');print(out)
