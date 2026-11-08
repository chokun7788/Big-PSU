"""Compare retained metrics only; no model or chatbot requests and no baseline reruns."""
import hashlib,json,re
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;sources={}
def read(relative):
 p=B/relative;sources[relative]=hashlib.sha256(p.read_bytes()).hexdigest();return json.loads(p.read_text('utf8'))
def pct(n,d):return round(100*n/d,2) if d else None
def link(relative,label=None):return f"[{label or relative}]({(B/relative).as_posix()})"
rows=[]
def row(name,scope,requests,passed,total,strict_pass=None,strict_total=None,locales=None,source='',notes=''):
 v={'flow':name,'scope':scope,'requests':requests,'positive_passed':passed,'positive_checked':total,'positive_percent':pct(passed,total),'strict_passed':strict_pass,'strict_total':strict_total,'strict_percent':pct(strict_pass,strict_total) if strict_pass is not None else None,'by_locale':locales or {},'source':source,'limits':notes};rows.append(v);return v

base=read('r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json');t=base['totals']
for role,name in [('old','Legacy เดิม — R64 LLM ON'),('new','Common — R88 LLM ON')]:
 loc={k:{'passed':v[role+'_positive_passed'],'checked':v['positive_checked'],'percent':pct(v[role+'_positive_passed'],v['positive_checked'])} for k,v in base['by_requested_locale'].items()}
 row(name,'full',t['requests'],t[role+'_positive_passed'],t['positive_checked'],t[role+'_strict_passed'],t['grades'],loc,'r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json','R89 ใช้ literal checker เดียวกันบนผล Legacy/R88 ที่เก็บไว้ แต่โค้ด/ข้อมูลต่างรุ่น ไม่ใช่ schema-only experiment')
r95=read('r95_merged_flow_implementation_20261018/full_analysis/ANALYSIS_FINAL.json');t=r95['totals']
row('Common ผสม — R95 LLM ON','full',r95['requests'],t['positive_passed'],t['positive_checked'],t['strict_passed'],r95['grades'],{k:{'passed':v['positive_passed'],'checked':v['positive_checked'],'percent':pct(v['positive_passed'],v['positive_checked'])} for k,v in r95['by_requested_locale'].items()},'r95_merged_flow_implementation_20261018/full_analysis/ANALYSIS_FINAL.json','ใช้ metric R95 เดิม; เทียบ R88 บน 24,909 positive grades เดียวกันได้')
r106=read('r106_complete_flow_20261020/full_analysis/SCORES.json');loc=r106['by_locale']
row('Common Flow V2 ที่พัฒนาต่อ — R106 LLM ON','full',r106['unique_keys'],sum(v['positive_content_checks_pass'] for v in loc.values()),sum(v['positive_checks'] for v in loc.values()),sum(v['strict_pass'] for v in loc.values()),sum(v['grades'] for v in loc.values()),{k:{'passed':v['positive_content_checks_pass'],'checked':v['positive_checks'],'percent':pct(v['positive_content_checks_pass'],v['positive_checks'])} for k,v in loc.items()},'r106_complete_flow_20261020/full_analysis/SCORES.json','เป็น partition-based metric ของ R106 ไม่เท่ากับ literal checker R95 ทุกเงื่อนไข; execution failure ตัด positive denominator ออก 18 grades; ดู paired R95↔R106 แยก')
pair=read('r106_complete_flow_20261020/full_analysis/REVIEW_R95_COMPARISON.json')['by_locale_same_grade_identities']
paired={k:{'shared_positive':v['shared_positive'],'r95_positive':v['r95_positive'],'r106_positive':v['r106_positive'],'r95_percent':pct(v['r95_positive'],v['shared_positive']),'r106_percent':pct(v['r106_positive'],v['shared_positive']),'delta_percentage_points':round(pct(v['r106_positive'],v['shared_positive'])-pct(v['r95_positive'],v['shared_positive']),2)} for k,v in pair.items()}
n=sum(v['shared_positive'] for v in pair.values());p95=sum(v['r95_positive'] for v in pair.values());p106=sum(v['r106_positive'] for v in pair.values())
paired['total']={'shared_positive':n,'r95_positive':p95,'r106_positive':p106,'r95_percent':pct(p95,n),'r106_percent':pct(p106,n),'delta_percentage_points':round((p106-p95)*100/n,2)}
r70=read('r70_half_common_llm_20261016/ANALYSIS_FINAL.json');t=r70['totals']
row('Common หลังย้ายข้อมูล — R70','half',t['requests'],t['positive_text_passed'],t['positive_text_checked'],t['raw_passed'],t['grades'],source='r70_half_common_llm_20261016/ANALYSIS_FINAL.json',notes='ครึ่งชุด; model transport 0/253 จึงเป็น ON setting ที่ไม่ได้ยืนยัน inference จริง ห้ามจัดอันดับข้าม full corpus')
r93path='r93_random_1000_common_on_20261018/REPORT_FINAL_TH.md'
sources[r93path]=hashlib.sha256((B/r93path).read_bytes()).hexdigest()
assert '765/1,140' in (B/r93path).read_text('utf8') and '248/2,609' in (B/r93path).read_text('utf8')
row('R92 — วัดใน R93 สุ่ม 1,000','sample1000',1000,765,1140,248,2609,source=r93path,notes='1,000 request keys / 998 ข้อความ; supplement อีก 2 requests แยกจากตารางหลัก ไม่เทียบ full R88 72.10 โดยตรง; R88 cohort เดียวกัน 758/1140=66.49%')
for name,path,candidate in [('R98 subset02','r98_flow_v2_implementation_20261019/subset02/COMPARISON.json','r98_candidate'),('R100 subset05','r100_contract_flow_implementation_20261019/subset05/COMPARISON.json','r100_candidate')]:
 a=read(path)[candidate];t=a['totals'];row(name,'development91',t['requests'],t['positive_literal_passed'],t['positive_grades'],t['strict_passed'],t['grades'],source=path,notes='91 request keys / 72 positive grades ที่ใช้พัฒนา ไม่ใช่ full accuracy; ใช้รอบหลังตามลำดับ ไม่เลือกผลสูงสุดจากหลายรอบ')
a=read('r101_complete_flow_20261019/release_subset09/ANALYSIS.json')['candidate_r101'];t=a['totals']
row('R101 release_subset09','development91',t['requests'],t['positive_pass'],t['positive'],t['strict_pass'],t['grades'],{k:{'passed':v['pass'],'checked':v['total'],'percent':pct(v['pass'],v['total'])} for k,v in a['locales'].items()},'r101_complete_flow_20261019/release_subset09/ANALYSIS.json','ยังเป็นชุดพัฒนาเดิม 91 requests ไม่ใช่ผลสุ่มทั้งหมด')
for ver,folder,run in [(103,'r103_complete_revision_20261020','analysis_integrated02'),(104,'r104_complete_flow_20261020','analysis_integrated03'),(105,'r105_complete_flow_20261020','analysis_integrated04')]:
 for suffix,scope in [('retained_91','development91'),('retained_holdout192','holdout192')]:
  path=f'{folder}/{run}/{suffix}_SCORES.json';a=read(path);v=a['by_locale']
  row(f'R{ver} {suffix}',scope,a['unique_keys'],sum(x['positive_content_checks_pass'] for x in v.values()),sum(x['positive_checks'] for x in v.values()),sum(x['strict_pass'] for x in v.values()),sum(x['grades'] for x in v.values()),{k:{'passed':x['positive_content_checks_pass'],'checked':x['positive_checks'],'percent':pct(x['positive_content_checks_pass'],x['positive_checks'])} for k,x in v.items()},path,'แสดงแยกชุดพัฒนา/holdout; data source และ scorer ต่างรุ่น ไม่ถือว่าทุกความต่างเป็น algorithm effect')

strict64=[]
a=read('r64_full_comparison_20261013/ANALYSIS_LATEST.json')
for arm in a:
 # These counts are already documented in the original report; retain the
 # exact saved field names alongside the calculated display percentage.
 c=a[arm]['counts'];strict64.append({'arm':arm,'saved_counts':c})
completion={p:read(p) for p in ['r64_full_comparison_20261013/FULL_TEST_COMPLETE.json','r88_full_common_llm_20261017/FULL_TEST_COMPLETE.json','r95_merged_flow_implementation_20261018/FULL_TEST_COMPLETE.json','r106_complete_flow_20261020/FULL_TEST_COMPLETE.json']}
acceptance=[]
for ver,folder,run in [(103,'r103_complete_revision_20261020','analysis_integrated02'),(104,'r104_complete_flow_20261020','analysis_integrated03'),(105,'r105_complete_flow_20261020','analysis_integrated04')]:
 path=f'{folder}/{run}/SCENARIO_SCORES.json';a=read(path);p=sum(v['passed'] for v in a.values());n=sum(v['total'] for v in a.values());acceptance.append({'version':ver,'passed':p,'checked':n,'percent':pct(p,n),'source':path,'kind':'targeted_acceptance_not_full_accuracy'})
sources['r106_complete_flow_20261020/final_gate/REPORT_TH.md']=hashlib.sha256((B/'r106_complete_flow_20261020/final_gate/REPORT_TH.md').read_bytes()).hexdigest()
acceptance.append({'version':106,'passed':444,'checked':444,'percent':100,'source':'r106_complete_flow_20261020/final_gate/REPORT_TH.md','kind':'targeted_acceptance_not_full_accuracy'})

# Inventory every retained revision folder, including plans/data intake rather
# than pretending that each R number is a separately evaluated chatbot Flow.
inventory=[]
for folder in sorted(B.iterdir(),key=lambda p:p.name):
 m=re.match(r'r(\d+)_',folder.name)
 if not folder.is_dir() or not m or int(m[1])>=110:continue
 ver=int(m[1]);reports=list(folder.glob('*.md'));best=next((p for p in reports if any(t in p.name for t in ['REPORT_FINAL','RESULTS_TH','IMPLEMENTED_FLOW','FINAL_REPORT','FULL_FLOW','RECEIPT_AND','INTAKE_REVIEW'])),reports[0] if reports else None)
 if ver<=57:group='Flow เดิม/การแก้เฉพาะงานก่อน migration'
 elif ver<=63:group='schema กลาง/แผน/ย้ายข้อมูลก่อน R64'
 elif ver<=69:group='full comparison/วิเคราะห์/ซ่อมข้อมูล'
 elif ver<=87:group='Flow กลางซ่อมหมวดและการเชื่อมระบบ'
 elif ver<=95:group='Flow กลาง R88/R92/R95 และงานวิเคราะห์ประกอบ'
 elif ver<=106:group='งานวิจัย/R97 V2/การพัฒนา R98–R106'
 else:group='แบบฟอร์มและรับข้อมูลเจ้าของ ไม่ใช่ Flow ที่วัดใหม่'
 associated=[v['flow'] for v in rows if (f'R{ver} ' in v['flow'] or v['flow'].endswith(f'R{ver}'))]
 inventory.append({'revision':ver,'folder':folder.name,'group':group,'report':str(best.relative_to(B)).replace('\\','/') if best else None,'measured_rows':associated,'unscored_note':'ไม่สร้างเปอร์เซ็นต์รวมจาก unit/API/schema assertions หรือจากแผน Flow หากไม่มีผลชุดเทียบที่ระบุในตาราง'})
inventory.sort(key=lambda x:(x['revision'],x['folder']))
out={'created_at':datetime.now().astimezone().isoformat(),'method':'retained files only','llm_calls':0,'chatbot_requests':0,'rows':rows,'r95_r106_same_grade_identities':paired,'strict_r64_saved':strict64,'targeted_acceptance':acceptance,'inventory':inventory,'source_hashes':sources,'limits':['Positive/checkpoint scores are not independently adjudicated semantic answer accuracy.','Full/half/development/holdout/acceptance scores are not one ranking.','Historical oracle/data versions differ; owner R108/R109 facts have not been applied to an evaluated Flow.']}
(R/'COMPARISON.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
lines=['# เปรียบเทียบ Flow ที่มีจากผลเก็บไว้','',f"จัดทำ {out['created_at']} — อ่านผลเดิมเท่านั้น ไม่รันแชท ไม่เรียก LLM ไม่เปลี่ยน source หรือผลทดสอบเดิม",'',
'## 1. คำตอบสั้น','',
'- Flow เดิม Legacy มีคะแนน positive literal checkpoints สูงสุดในผล full ที่เก็บไว้: 23,517/24,909 = 94.41%',
'- ใน Flow กลางที่มี full test: R95 สูงกว่า R88 บน checker/positive grades ชุดเดียวกัน (74.59% เทียบ 72.10%)',
'- R106 พัฒนาโครงสร้างและผ่านเฉพาะส่วนได้ดี แต่ full corpus ยังต่ำกว่า R95 บน shared grade identities: 69.25% เทียบ 73.42% ภายใต้ตัววิเคราะห์ R106',
'- R108/R109 เป็นข้อมูลที่เพิ่งรับ ไม่ใช่ runtime Flow ใหม่ จึงไม่มีคะแนนหลังใส่ข้อมูลและไม่มีหลักฐานพอจะให้ประมาณเป็น 80/90/95%',
'- คะแนนในรายงานนี้เป็นการผ่านเกณฑ์ข้อความ/ข้อกำหนด ไม่ใช่เปอร์เซ็นต์คำตอบที่มนุษย์ตรวจความหมายว่าถูกทั้งหมด','',
'## 2. Full Test — 20,554 request keys / 55,811 grades','',
'| Flow ที่รันทดสอบจริง | Positive/checkpoint score | Strict score | แหล่ง |','|---|---:|---:|---|']
for v in [r for r in rows if r['scope']=='full']:lines.append(f"| {v['flow']} | {v['positive_passed']:,}/{v['positive_checked']:,} = {v['positive_percent']:.2f}% | {v['strict_passed']:,}/{v['strict_total']:,} = {v['strict_percent']:.2f}% | {link(v['source'],'หลักฐาน')} |")
lines+=['',
'Legacy/R88/R95 ใช้ 24,909 positive grades ตาม literal checker ฝั่ง R88/R95 โดย Legacy/R88 เทียบตรงกันใน R89. R106 มี positive denominator 24,891 ตามการวิเคราะห์เดิม และวิธี partition ไม่เท่ากับ literal R95 ทุกเงื่อนไข ตารางนี้เป็น dashboard ผลที่รายงานไว้ ไม่ใช่การจัดอันดับจาก grader เดียวกันทุกแถว','',
'### Strict ของ Common รุ่นแรก R64','',
'Legacy ปิด LLM 42,410/55,811 = 75.99%; เปิด LLM 42,601/55,811 = 76.33%. Common ปิด LLM 16,998/55,811 = 30.46%; เปิด LLM 12,517/55,811 = 22.43%. เป็น strict compatibility ดั้งเดิม ไม่ใช่ positive content score และไม่เอา 22.43% ไปเทียบกับ 74.59% ว่าเป็นเกณฑ์เดียวกัน',
link('r64_full_comparison_20261013/FINAL_FULL_TEST_REPORT.md','รายงาน R64'),'',
'## 3. แยกภาษา — Full Test','',
'| Flow | ไทย | อังกฤษ | Auto |','|---|---:|---:|---:|']
for v in [r for r in rows if r['scope']=='full']:
 l=v['by_locale'];lines.append(f"| {v['flow']} | {l['th']['percent']:.2f}% | {l['en']['percent']:.2f}% | {l['auto']['percent']:.2f}% |")
lines+=['','Auto คือ locale ที่ขอให้ระบบเลือก ไม่ใช่ภาษาที่สาม ทุกแถวอ้างอิง metric ของแต่ละรายงานดังข้อ 2','',
'## 4. R95 ↔ R106 บน grade identities เดียวกัน','',
'| Locale | R95 ภายใต้ checker R106 | R106 | ต่างกี่ percentage points |','|---|---:|---:|---:|']
for k in ['th','en','auto','total']:
 v=paired[k];lines.append(f"| {k} | {v['r95_positive']:,}/{v['shared_positive']:,} ({v['r95_percent']:.2f}%) | {v['r106_positive']:,}/{v['shared_positive']:,} ({v['r106_percent']:.2f}%) | {v['delta_percentage_points']:+.2f} |")
lines+=['',
'R95 74.59% ในข้อ 2 กับ R95 73.42% ในข้อนี้เป็นคำตอบชุด R95 เดียวกัน แต่ตัวแยกผ่าน/ไม่ผ่านและ positive denominator คนละแบบ ไม่ใช่ R95 ถูกนำไปรันใหม่แล้วลดลง',
'R106 มี watchdog exception 18 requests; input มี positive assertions 18 grades ที่ถูกตัดจาก denominator โดยระบบเดิม หากนับเป็นไม่ผ่านบน denominator เดิม 24,909 จะเป็น 17,238/24,909 = '+f'{pct(17238,24909):.2f}%'+'. ยังมี taxonomy defect เช่น keyword timeout/latency ถูกจัด performance และบาง wrong_category ถูกจัด content ดังนั้นไม่อ้าง metric นี้เป็น semantic accuracy',
'การเทียบนี้ยังมีข้อมูล migration/metadata ต่างรุ่นกัน จึงไม่ใช่ผลของ algorithm Flow ล้วน ๆ',link('r106_complete_flow_20261020/full_analysis/ROOT_CAUSE_REVIEW_TH.md','รายละเอียดข้อบกพร่อง metric และสาเหตุ'),'',
'## 5. ผลครึ่งชุด/สุ่ม — แยกจาก Full Test','',
'| Flow | ขอบเขต | คะแนน positive | ข้อจำกัด |','|---|---|---:|---|']
for v in [r for r in rows if r['scope'] in ['half','sample1000']]:lines.append(f"| {v['flow']} | {v['requests']:,} requests | {v['positive_passed']:,}/{v['positive_checked']:,} ({v['positive_percent']:.2f}%) | {v['limits']} {link(v['source'],'หลักฐาน')} |")
lines+=['','R93 cohort เดียวกัน: retained R88 758/1,140 = 66.49%; R92 765/1,140 = 67.11%; R95 795/1,140 = 69.74%. เทียบสามตัวนี้บน sample เดียวกันได้ แต่ใช้ sample สรุปเป็น full 20,554 ไม่ได้','',
'## 6. รุ่น R98–R105: ชุดพัฒนา 91 และ holdout 192','',
'| Flow/รอบ | ชุดคำถาม | คะแนน positive | แหล่ง |','|---|---|---:|---|']
for v in [r for r in rows if r['scope'] in ['development91','holdout192']]:lines.append(f"| {v['flow']} | {v['requests']} requests | {v['positive_passed']}/{v['positive_checked']} ({v['positive_percent']:.2f}%) | {link(v['source'],'หลักฐาน')} |")
lines+=['',
'91 ข้อเป็นชุดที่ใช้พัฒนาซ้ำ จึงมี selection/adaptation bias. R98 รอบแรก 55/72 เท่ากับ R95 cohort เดิม และ subset02 ภายหลังเป็น 61/72. R100 subset01 61/72; subset02/03/05 63/72. แสดงรอบหลังตาม lineage พร้อมเก็บข้อมูลรอบก่อน ไม่เลือกค่าสูงสุดมาทำนาย full accuracy',
'R103 ได้ 66/72 บนชุดพัฒนา แต่ holdout 150/249 ≈ 60.24%; R104/R105 เหลือ 62/72 และ holdout 148/249 ≈ 59.44%. ความต่างระหว่างชุดพัฒนากับชุดกว้าง/holdout เป็นหลักฐานว่าคะแนนสูงของชุดเล็กยังใช้รับรองภาพรวมไม่ได้',
'R102 มี integrated01 19 lanes ที่รันแล้ว แต่หน่วยของแต่ละ lane ต่างกัน ไม่สร้างคะแนนเฉลี่ยรวมขึ้นเอง; R101 361/361 assertions และ 3/3 LLM toy-game probes ไม่ใช้แทนเปอร์เซ็นต์คำถามจริงทั้งระบบ','',
'## 7. Acceptance tests ของงานเฉพาะส่วน','',
'| รุ่น | ผ่าน assertions ใน R97 acceptance | เปอร์เซ็นต์ |','|---|---:|---:|']
for a in acceptance:lines.append(f"| R{a['version']} | {a['passed']}/{a['checked']} | {a['percent']:.2f}% |")
lines+=['',
'นี่เป็น 37 scenarios × 3 locales × 4 variants รวม 444 assertions/เคสตาม suite ไม่ใช่สุ่มจาก full corpus และไม่ใช่ 444 independent user questions. R105 ตรวจ integrated 19 lanes ส่วน R106 ตรวจเฉพาะ branch ที่แก้ตาม LINEAGE แล้วทำ full test. การผ่าน acceptance 100% อยู่ร่วมกับ full positive 69.25% ได้ เพราะโจทย์และเกณฑ์คนละขอบเขต','',
'## 8. แต่ละ Flow เปลี่ยนอะไร และผลบอกอะไร','',
'- **Legacy เดิม:** ตัวเลือกหัวข้อ/ข้อมูล/answer contract ถูกทำเฉพาะโดเมนจำนวนมากและตรงกับ oracle ที่สร้างจากระบบเดิม จึงตอบ corpus เก่าได้สูงกว่า แต่ไม่ได้พิสูจน์ว่าเพิ่มข้อมูลชนิดใหม่แล้วตอบได้โดยไม่แก้ parser และไม่ได้ยืนยันข้อมูลนโยบาย ณ วันนี้',
'- **Common ช่วง R58–R70:** เพิ่ม schema/ฐานกลางและย้ายข้อมูล ปัญหาเป็นทั้ง mapping/English/relations/selector/transport ไม่ใช่ดูเพียงจำนวน records ที่ย้าย จึงใช้ข้อมูลครบอย่างเดียวอธิบายคะแนนไม่ได้',
'- **R88 (R87 stage 2):** เชื่อมพฤติกรรมเก่าบางส่วนเข้ากับข้อมูลกลาง ผล full positive 72.10%; ยังติดราคา/เวลาจอง/คำถามหลายเรื่อง/กฎ',
'- **R95:** ผสม typed execution/Task contract กับ compatibility parsers; improved 783 regressed 164 positive grades เทียบ R88 สุทธิ +619 หรือ +2.49 points. คะแนนสูงสุดในกลุ่ม common ที่มีหลักฐาน full ภายใต้ checker เดียวกับ R88',
'- **R96/R97:** เป็นงานวิจัย/แผน Flow V2 ไม่มี runtime full score แยกของตัวแผน R97; การทำจริงเป็น R98–R106 ไม่สามารถให้เปอร์เซ็นต์ว่า Astra plan ถูก 95% จากตัวแผนอย่างเดียว',
'- **R98–R101:** ลง implementation ทีละส่วนจน shared context/plan, tasks, owner lifecycle, semantic planner, conflict/live/rental routes; ชุดพัฒนาดีขึ้น แต่ยังต้องพิสูจน์การเลือก task บนคำถามกว้าง',
'- **R102–R106:** ทำ coverage/need selection/dependency/validity/field evidence/unknown checks มากขึ้น แต่ full R106 ยังมี gate กฎไม่ตอบแม้มีข้อความ, เลือก maintenance แทนเปิดบริการ, เลือก facet ผิด, fallback ยาว, multi-need ไม่ครบ และ nested English leakage',
'- **R107/R108/R109:** แบบฟอร์มและข้อมูลเจ้าของ เริ่มปิด source gaps เช่นเวลาเช่า/จอย/ราคาแยกกลุ่ม/กติกา Pause; ยังไม่ใช่การทดสอบ Flow หลังใช้ข้อมูลนั้น และไม่อ้างว่าการรับคำตอบทำให้คะแนนสูงขึ้นแล้ว','',
'## 9. ควรอ่านผลอย่างไรในตอนนี้','',
'1. ถ้าถามว่าใครตอบชุดเก่าดีที่สุด: Legacy มีหลักฐาน positive checkpoints 94.41% สูงสุดใน saved full runs ที่เทียบนี้ แต่ไม่ใช่ semantic correctness ของวันนี้',
'2. ถ้าถามว่า common ตัวไหนมีหลักฐาน full ดีที่สุด: R95 ดีกว่า R88 บน checker เดียวกัน และ R95 ดีกว่า R106 บน R106 shared-grade analysis',
'3. ถ้าถามว่าโครงสร้างรองรับข้อมูลเจ้าของตัวไหนใหม่กว่า: สาย R97→R106 มีงานด้านนี้เพิ่ม แต่คะแนนภาพรวมยังไม่ชนะ จึงต้องแก้จุดติด source-to-answer และทดสอบหลังรวมข้อมูลก่อนตัดสิน',
'4. ยังไม่มีเปอร์เซ็นต์ semantic accuracy ที่ตรวจโดยมนุษย์อย่างอิสระครบระบบของทุก Flow จึงไม่ให้ตัวเลขคาดเดาว่าตัวล่าสุดจะ 90% แล้ว',
'5. การข้ามหน่วยโทษ Pause Tekken ตามคำสั่งใน R109 เป็นข้อยกเว้นของงานทดสอบอนาคต ไม่ลบโจทย์/ปรับเปอร์เซ็นต์ historical results ในรายงานนี้','',
'## 10. บัญชีรุ่นที่พบทั้งหมด','',
'บาง R number เป็นแผน วิเคราะห์ ย้ายข้อมูล แบบฟอร์ม หรือ execution control ไม่ใช่ Flow ใหม่ทุกเลข ตารางนี้จึงระบุครบทุกรุ่นที่มีโฟลเดอร์ โดยเปอร์เซ็นต์ใช้ได้เฉพาะชุดหลักฐานข้างบน ไม่สร้าง % รวมจากรายงานการทำงานสำเร็จ','',
'| รุ่น/โฟลเดอร์ | กลุ่ม | คะแนนที่เปรียบเทียบในรายงานนี้ | เอกสารระดับโฟลเดอร์ |','|---|---|---|---|']
for x in inventory:lines.append(f"| {x['folder']} | {x['group']} | {'; '.join(x['measured_rows']) or 'ไม่มี % รวมที่ใช้จัดอันดับในตารางนี้'} | {link(x['report'],'เอกสาร') if x['report'] else 'ดูไฟล์ในโฟลเดอร์'} |")
lines+=['','## หลักฐานเครื่องอ่านและความคงเดิม','',
'COMPARISON.json เก็บ numerator/denominator/locale/source hashes ทุกตัวที่ใช้คำนวณ รวม snapshot metric R64 และบัญชีทุกโฟลเดอร์ อ่านข้อมูลผลเท่านั้น ไม่แก้ oracle/approvals/database/คำตอบผู้ใช้ ไม่ได้ทำ full test, baseline rerun หรือเรียก LLM เพิ่มในรอบนี้']
(R/'FLOW_COMPARISON_TH.md').write_text('\n'.join(lines),'utf8')
assert all(hashlib.sha256((B/path).read_bytes()).hexdigest()==h for path,h in sources.items())
print(json.dumps({'full':[{k:v[k] for k in ['flow','positive_percent','strict_percent','by_locale']} for v in rows if v['scope']=='full'],'paired':paired['total'],'folders_in_inventory':len(inventory),'saved_scores_compared':len(rows),'new_requests':0},ensure_ascii=False))
