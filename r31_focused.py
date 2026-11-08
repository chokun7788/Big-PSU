import sys,os,json,time,collections
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p));r=Path(Path('r31_report_path.txt').read_text().strip())
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0';os.environ['PYTHONDONTWRITEBYTECODE']='1'
from app.pipeline.engine import answer_question_pipeline_debug
from app.booking.live_status import _unavailable
from unittest.mock import patch
cases=[]
def add(q,l,yes,no=()):cases.append({'id':'R31-'+str(len(cases)+1),'question':q,'locale':l,'must_contain':list(yes),'must_not_contain':list(no),'required_source':'competition_rules_cs2','outcome':None,'group':'r31_source'})
for q in ['สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน','CS2 สถานที่แข่งขันอยู่ที่ใด','กติกา CS2 บอกสถานที่จัดไว้ที่ไหน','CS2 แข่งที่ใดและใช้กี่วัน']:
    add(q,'th',['PSU Esports Studio','Phuket'],['ยังไม่พบ'])
for q in ['Where is the PSU Phuket CS2 2026 competition venue?','Where does the CS2 competition take place?','What is the location of the CS2 tournament?']:
    add(q,'en',['PSU Esports Studio','Phuket'],['could not find'])
for q in ['CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง','CS2 timeout ได้กี่ครั้ง ครั้งละกี่วินาที','CS2 ขอ timeout ระหว่าง Freeze time ได้กี่ครั้ง','กฎ CS2 เวลานอกช่วง freeze time ขอได้กี่ครั้ง']:
    add(q,'th',['4 ครั้ง','30 วินาที','Freeze time'],['1:55','15 วินาที'])
for q in ['How many CS2 timeouts during freeze time and how long is each?','How many timeouts are allowed in the CS2 tournament?','How long is each timeout under CS2 rules?']:
    add(q,'en',['4','30','Freeze'],['1:55'])
for q in ['ตาม rulebook เคานน์เตอร์สไตรก์ 2 การตั้งค่าในเกม ต้องทำยังไง','ตาม rulebook เคาน์เเตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง','ขออ้างอิงกติกา เคาน์เตอร์สไรก์ 2 ในหัวข้ออุปกรณ์ที่ใช้แข่งขัน หน่อย']:
    add(q,'th',['Counter-Strike 2'],['ต้องการดูกติกาของเกมใด'])
for q in ['What are the Counter strkie 2 competition equipment rules?','What are the Counter-Strikee 2 tournament rules?','What are the Couter Strike 2 competition settings?']:
    add(q,'en',['Counter-Strike 2'],["Which game's competition rules"])
if sys.argv[1]=='baseline':
    with (r/'focused_fixture.json').open('x',encoding='utf-8') as out:json.dump({'cases':cases,'scope':'source-derived and target-only recovery checks; independent corpus evaluation separate'},out,ensure_ascii=False,indent=2)
else:cases=json.loads((r/'focused_fixture.json').read_text(encoding='utf-8'))['cases']
run=sys.argv[1];rows=[]
with (r/(run+'_focused.jsonl')).open('x',encoding='utf-8') as out,patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline fixture',error_code='fixture_offline')):
    for c in cases:
        a=answer_question_pipeline_debug(c['question'],locale=c['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
        errors=['missing:'+v for v in c['must_contain'] if v.casefold() not in a.answer.casefold()]+['forbidden:'+v for v in c['must_not_contain'] if v.casefold() in a.answer.casefold()]
        if not any(c['required_source'] in str(h) for h in a.hits):errors.append('source_missing')
        if not a.validation.ok:errors.append('validation_rejected')
        row={'case':c,'answer':a.answer,'mode':a.mode,'hits':a.hits,'trace':[vars(t) for t in a.trace],'passed':not errors,'failures':errors};rows.append(row);out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush()
with (r/(run+'_focused_summary.json')).open('x',encoding='utf-8') as out:json.dump({'total':len(rows),'passed':sum(x['passed'] for x in rows),'failed':[{k:x[k] for k in ['case','answer','mode','failures']} for x in rows if not x['passed']]},out,ensure_ascii=False,indent=2)
print(json.dumps({'total':len(rows),'passed':sum(x['passed'] for x in rows),'failed_ids':[x['case']['id'] for x in rows if not x['passed']]}),flush=True)
