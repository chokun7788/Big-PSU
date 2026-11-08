import json,csv,html,urllib.request,re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text());P=OUT/'papers';P.mkdir(exist_ok=True)
papers=[
 ('FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation',2023,'2023.emnlp-main.741','https://aclanthology.org/2023.emnlp-main.741/','EMNLP','แยกคำตอบเป็นข้อกล่าวอ้างและตรวจหลักฐานประกอบ; การตอบน้อยหรือไม่ตอบอาจทำ precision ดูดี จึงต้องรายงาน coverage และ abstention ด้วย','นำหลักการ evidence scope และแยก answer delivered มาใช้; ยังไม่ได้ทำ atomic extraction/evaluator เต็มระบบ'),
 ('xCOMET: Transparent Machine Translation Evaluation through Fine-grained Error Detection',2024,'2024.tacl-1.54','https://aclanthology.org/2024.tacl-1.54/','TACL','ให้คะแนนและตำแหน่งข้อผิดพลาดพร้อม severity; WMT22/23 evaluation ที่อ่านไม่ใช่คู่ไทย–อังกฤษ โมเดล XL/XXL มีขนาด 3.5B/10.7B','ยืมวิธีจัดหมวด accuracy/addition/coverage/factuality ไม่ได้ติดตั้งหรืออ้างคะแนน xCOMET'),
 ('Guiding Large Language Models to Post-Edit Machine Translation with Error Annotations',2024,'2024.findings-naacl.265','https://aclanthology.org/2024.findings-naacl.265/','Findings NAACL','external MQM feedback ใช้ชี้การแก้คำแปล; ผล fine-grained prompting ไม่ชัดเท่า fine-tuning ในงานนี้; tested zh-en/en-de/en-ru','ส่งเหตุผลที่ตรวจได้และคำอธิบายวิธีแก้กลับเพียงหนึ่งครั้งภายใต้งบเวลา ไม่ย้ายผลทดลองมาอ้างเป็นภาษาไทย'),
 ('Chain-of-Verification Reduces Hallucination in Large Language Models',2023,'2309.11495','https://arxiv.org/abs/2309.11495','arXiv preprint','ร่าง→คำถามตรวจสอบ→ตอบตรวจอย่างอิสระ→แก้ร่าง; งานยังมี hallucination และใช้การคำนวณเพิ่ม','นำแนวคิดตรวจเงื่อนไขก่อนปล่อยมาใช้ร่วม external facts; ไม่ได้ติดตั้ง CoVe สี่ขั้นเต็มทุกคำขอ'),
 ('When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs',2024,'2024.tacl-1.78','https://aclanthology.org/2024.tacl-1.78/','TACL','survey แยกเงื่อนไขและคุณภาพ feedback; reliable external feedback เป็นเงื่อนไขสำคัญ ไม่ควรถือการสั่งโมเดลตรวจตนเองว่าเชื่อถือได้เสมอ','ใช้ deterministic constraints และ reference cards แทนการขอโมเดลรับรองตนเองโดยไม่มีหลักฐาน'),
 ('Can LLMs Detect Intrinsic Hallucinations in Paraphrasing and Machine Translation?',2025,'2025.gem-1.13','https://aclanthology.org/2025.gem-1.13/','GEM workshop','ประเมิน hallucination ใน translation/paraphrase; detector ผลต่างตาม model และ NLI มีผลเทียบได้ในงานที่ศึกษา','NLI/learned evaluator เป็นทางเลือกต่อไป ต้องทดสอบไทยและ false positive ก่อนเพิ่ม runtime; ยังไม่ได้ติดตั้ง'),
 ('Syllable-based Neural Thai Word Segmentation',2020,'2020.coling-main.407','https://aclanthology.org/2020.coling-main.407/','COLING','ไทยมีปัญหาขอบเขตคำ; งานเสนอ syllable-based segmentation ไม่ใช่การนับช่องว่าง','คง Thai word-count unverified; ขั้นถัดไปเลือก tokenizer/version และทดสอบข้อความผสมไทย–อังกฤษก่อนใช้รับรอง 500 คำ'),
 ('FactCorrector: A Graph-Inspired Approach to Long-Form Factuality Correction of Large Language Models',2026,'2601.11232','https://arxiv.org/abs/2601.11232','arXiv preprint','ใช้ structured factual feedback; VELI5 สร้าง errors ที่มี corrections เพื่อประเมินการแก้','นำแนวคิด bad/good paired fixtures มาใช้ ไม่ได้ติดตั้ง graph pipeline หรืออ้างผล benchmark ว่าจะเกิดบนเครื่องนี้'),
]
rows=[dict(title=t,year=y,id=i,url=u,venue=v,finding=f,application=a) for t,y,i,u,v,f,a in papers]
def bib(row):
 if 'aclanthology' not in row['url']:
  return '@misc{'+row['id'].replace('.','_')+',\n title={'+row['title']+'},\n year={'+str(row['year'])+'},\n howpublished={arXiv preprint},\n eprint={'+row['id']+'},\n url={'+row['url']+'}\n}\n'
 try:
  raw=urllib.request.urlopen(row['url'].rstrip('/')+'.bib',timeout=15).read().decode('utf-8')
  if not raw.lstrip().startswith('@'):raise ValueError('not BibTeX')
  # Export citation only; abstracts are not copied into the report.
  raw=re.sub(r',?\s*abstract\s*=\s*".*?"(?=\s*[,}])','',raw,flags=re.S)
  row['metadata_source']='publisher_bibtex';return raw
 except Exception as e:
  row['metadata_source']='verified_title_year_url_only';row['export_error']=type(e).__name__
  return '@misc{'+row['id'].replace('.','_')+',\n title={'+row['title']+'},\n year={'+str(row['year'])+'},\n url={'+row['url']+'}\n}\n'
with ThreadPoolExecutor(max_workers=4) as pool:bibs=list(pool.map(bib,rows))
for name,content in [('references.bib','\n'.join(bibs)),('references.ris','\n'.join('TY  - '+('JOUR' if r['venue']=='TACL' else 'GEN')+'\nTI  - '+r['title']+'\nPY  - '+str(r['year'])+'\nUR  - '+r['url']+'\nER  -\n' for r in rows))]:
 with (P/name).open('x',encoding='utf-8') as s:s.write(content)
with (P/'papers.json').open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2)
with (P/'papers.csv').open('x',encoding='utf-8-sig',newline='') as s:
 writer=csv.DictWriter(s,fieldnames=['title','year','id','url','venue','finding','application'],extrasaction='ignore');writer.writeheader();writer.writerows(rows)
md='''# Research → implementation r53

## ขอบเขตและวิธีค้น

ใช้ paper-search-pro วางกลุ่มคำค้น แต่ helper หยุดตามคำสั่ง Setup เพราะยังไม่มี OpenAlex key และ NCBI email ใช้ web search/open ไปยัง ACL Anthology และ arXiv โดยตรงเป็น targeted fallback เมื่อ 2026-10-09 รายการคำค้นและสิ่งที่ข้ามอยู่ใน ../query_plan.json ไม่มีการอ้าง saturation, PRISMA completeness หรือ journal rank การค้นนี้คัด 8 งานเพื่อแก้ปัญหาที่เห็น ไม่ใช่ systematic review รายงาน HTML เป็น static fallback ไม่ใช่ Shadcn renderer ของ skill

อ่าน abstract/metadata ทุกงาน และอ่าน PDF methods/evaluation ของ xCOMET, limitations ของ FActScore และ CoVe เพิ่ม ไม่ได้อ้างว่าอ่านเนื้อหาทุกหน้าของทุกงาน ไม่มีการนำผลภาษาอื่นมายืนยัน accuracy ภาษาไทยของระบบเรา

## งานที่เลือกและการนำมาใช้

'''
for n,r in enumerate(rows,1):md+=f"### {n}. [{r['title']}]({r['url']}) — {r['year']} / {r['venue']}\n\n- หลักฐาน: {r['finding']}\n- ใช้ในโปรเจกต์: {r['application']}\n\n"
md+='''## ข้อสรุปที่ใช้ตัดสินใจ

1. ข้อผิดพลาด routing ต้องแก้ก่อนประเมินคำแปล: quotation ของ booking/PC เป็นข้อมูลของงานแปล การเพิ่ม evaluator ไม่ช่วยถ้าระบบไม่ได้แปลตั้งแต่แรก
2. Output ผ่านจำนวนบรรทัด/stream done ยังไม่พอ ต้องรักษาตัวเลข หน่วย คำปฏิเสธ ชื่อเครื่อง และระดับความแน่นอน
3. คำตอบเทคนิคต้องมี facts และ version qualifier จากแหล่งต้นทาง การแนบ URL อย่างเดียวไม่ได้พิสูจน์ทุกประโยค
4. Repair ต้องระบุความผิดและเงื่อนไขแก้ให้เข้าใจได้ มี budget และตรวจผลซ้ำ ไม่ใช้ retry ไม่จำกัด
5. ค่าผ่าน fixtures คือคุณภาพตัวตรวจบนเคสที่ออกแบบ ค่าตอบสำเร็จคือผล runtime และ accuracy ต้องตรวจความหมายแยกจากสองค่านี้

## สิ่งที่ยังต้องทำต่อจากรอบนี้

negation หลาย clause, omission ที่ไม่ใช่เลขหรือศัพท์ในชุด, qualifiers ที่เกินรูปแบบตัวตรวจ และ semantic entailment ภาษาไทยทั่วไปยังตรวจไม่ครบ ต้องเพิ่ม evaluation set ที่แยก held-out กับตัวอย่างพัฒนา ก่อนพิจารณา learned evaluator ไม่มีการปรับ model หรือ fine-tuning ในรอบนี้
'''
with (P/'report.md').open('x',encoding='utf-8') as s:s.write(md)
page='<!doctype html><html lang="en"><meta charset="utf-8"><title>r53 targeted literature review</title><style>body{font:16px system-ui;max-width:1000px;margin:40px auto;padding:20px;line-height:1.6}article{border:1px solid #ddd;padding:18px;margin:16px 0}a{color:#164f9e}</style><h1>r53: Translation and factual answer quality</h1><p>Targeted primary-source fallback. Not a systematic review; helper configuration unavailable. Eight selected papers. Thai implementation notes below.</p>'
for r in rows:page+=f'<article><h2><a href="{html.escape(r["url"])}">{html.escape(r["title"])}</a></h2><p>{r["year"]} · {html.escape(r["venue"])}</p><p>{html.escape(r["finding"])}</p><p>{html.escape(r["application"])}</p></article>'
with (P/'report.html').open('x',encoding='utf-8') as s:s.write(page+'</html>')
print('selected papers',len(rows),'publisher citations',sum(r.get('metadata_source')=='publisher_bibtex' for r in rows))
