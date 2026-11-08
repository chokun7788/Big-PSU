import sys,json
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1];p=B/('BEFORE_AFTER_'+tag+'.md');assert not p.exists()
def rows(t):return {r['question']:r for r in [json.loads(s) for s in (B/('MATRIX_'+t+'_llm.jsonl')).read_text(encoding='utf-8').splitlines()]}
after=rows(tag);before={x:rows(x) for x in ('final16','final18','final19')}
cases=[('What happens if I damage equipment?','final16','คำแปลขาดช่วงค่าปรับจริง → source-bound revision คืนตัวเลขและเงื่อนไขครบ'),('Can a visitor plug in their own laptop?','final18','source มีอยู่ แต่รอ model selector จน timeout → policy topic selection จาก FAQ heading'),('What is the studio policy for return equipment games?','final19','source มีนโยบายคืนอุปกรณ์ แต่ต้องรอ model → เลือก return-equipment policy ตามความหมายและ scope')]
lines=['# ตัวอย่างก่อน/หลังจากคำถามเดียวกัน','','ใช้ matrix pipeline แบบ serialized บนเครื่องนี้ และ fixture booking เดียวกัน frozen clock 2026-10-14 ไม่ใช่ browser end-to-end/load test และไม่ควรอนุมานความเร็วทุกคำถามจากเวลาเพียงหนึ่งครั้ง คำตอบใหม่ยังเป็น evaluation draft ไม่มีการ owner approve','']
for q,t,why in cases:
 a=before[t][q];z=after[q];lines+=['## '+q,'','**สาเหตุ/การแก้:** '+why,'','### ก่อน — '+t,'','เวลา '+f"{a['elapsed_wall']:.3f}"+' s; mode '+a['result']['mode'],'',a['result']['answer'],'','### หลัง — '+tag,'','เวลา '+f"{z['elapsed_wall']:.3f}"+' s; mode '+z['result']['mode'],'',z['result']['answer'],'','### Query plan หลังแก้','','```json',json.dumps((z['result'].get('decision_artifact') or {}).get('query_plan'),ensure_ascii=False,indent=2),'```','']
p.write_text('\n'.join(lines)+'\n',encoding='utf-8');print(p)
