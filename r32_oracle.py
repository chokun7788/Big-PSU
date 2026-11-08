"""Independent IDs/whole clauses + clean/noisy pairs; no result-derived oracle."""
import os,sys,json,re,hashlib,time,concurrent.futures
from pathlib import Path
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path((ROOT/'r32_report_path.txt').read_text().strip());sys.path.insert(0,str(P))
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0';os.environ['PYTHONDONTWRITEBYTECODE']='1'
from r32_full import execute
from app.pipeline.retrieval import load_curated_rows
from app.knowledge.localization import approved_localization
from app.pipeline.competition_presentation import source_clause_lines
rows={str(r['id']):r for r in load_curated_rows() if r.get('id') and not r.get('_canonical_projection')}
specs=[('cs2',['17','18','12'],['กติกา CS2 คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน','กติกา CS2 คุณสมบัตติ รายชื่อผู้เล่น และการลงทะเบียน','กติกา CS2 คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบีบน'],['CS2 competition eligibility, roster and registration','CS2 competition eligibilty, roster and registration','CS2 competition eligibility, roster and registraton']),('cs2',['23','24','25','26','27'],['กติกา CS2 การตั้งค่าในเกม','กติกา CS2 การตัง้ค่าในเกม','กติกา CS2 การตั้งคาในเกม'],['CS2 tournament in-game settings','CS2 tournament in-game settngs','CS2 tournament in-gmae settings']),('cs2',['41','42','43'],['กติกา CS2 อุปกรณ์ที่ใช้แข่งขัน','กติกา CS2 อุปกรณืที่ใช้แข่งขัน','กติกา CS2 อุปกรณ์ที่ใช้แข่งขั'],['CS2 tournament equipment rules','CS2 tournament equiment rules','CS2 tournament equipment rulse']),('cs2',['04','05','06','08','09'],['กติกา CS2 ขอบเขตและข้อมูลของรายการ','กติกา CS2 ขอบเขตตและข้อมูลของรายการ','กติกา CS2 ขอบเขตและข้อมูลของรายการ'],['CS2 rules: scope and event information','CS2 rules: scopw and event information','CS2 rules: scope and event informaton']),('rov',['06'],['กติกา RoV จำนวนผู้เล่นต่อทีม','กติกา RoV จำนวผู้เล่นต่อทีม','กติกา RoV จำนวนผู็เล่นต่อทีม'],['RoV competition rules team size','RoV competition rules team sze','RoV competition rules teem size'])]
def main():
 cases=[]
 for game,sections,th,en in specs:
  prefix='competition_rules_cs2_psu_phuket_2026' if game=='cs2' else 'competition_rules_rov_blueket_2025_men'
  for locale,qs in [('th',th),('en',en)]:
   required=[];source_ids=[]
   for s in sections:
    row=rows[prefix+'_s'+s+'_c01'];source_ids.append(row['id']);txt=approved_localization(row,'text') if locale=='en' else row['text'];assert txt
    # RoV s06 contains many distinct clauses; use only exact clause4.2.1.
    clauses=source_clause_lines(txt)
    if game=='rov':clauses=[c for c in clauses if c.startswith('4.2.1')]
    required+=clauses
   for i,q in enumerate(qs):cases.append(dict(id=f'{game}-{sections[0]}-{locale}-{i}',question=q,locale=locale,source_ids=source_ids,clauses=required,oracle_version='independent-source-IDs-r32-v1'))
 fixture=dict(cases=cases,source_hashes={id:hashlib.sha256(json.dumps(rows[id],ensure_ascii=False,sort_keys=True).encode()).hexdigest() for c in cases for id in c['source_ids']},evidence='registered source clauses and current hash-bound translations, not owner policy confirmation')
 if (R/'R32_POSITIVE_SOURCE_ORACLE.json').exists():assert json.loads((R/'R32_POSITIVE_SOURCE_ORACLE.json').read_text(encoding='utf-8'))==fixture
 else:
  with (R/'R32_POSITIVE_SOURCE_ORACLE.json').open('x',encoding='utf-8') as out:json.dump(fixture,out,ensure_ascii=False,indent=2)
 def run(c):
  job=dict(key=c['id'],question=c['question'],locale=c['locale'],reference_date='',entries=[]);raw=execute(job);z=raw['result'];body=re.sub(r'\s+',' ',z['answer']).casefold();errs=[]
  for clause in c['clauses']:
   if re.sub(r'\s+',' ',clause).casefold() not in body:errs.append('missing_complete_clause:'+clause)
  for id in c['source_ids']:
   if not any(h.get('id')==id for h in z['hits']):errs.append('missing_source:'+id)
  if not z['validation']['ok']:errs.append('validation_rejected')
  if z['mode']!='pipeline:competition_rule_detail_source':errs.append('source_answer_required:'+z['mode'])
  return dict(case=c,result=z,passed=not errs,failures=errs)
 records=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool,(R/(sys.argv[1]+'_source_oracle.jsonl')).open('x',encoding='utf-8') as out:
  for x in pool.map(run,cases):records.append(x);out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush();print(json.dumps({'id':x['case']['id'],'passed':x['passed'],'failures':x['failures']},ensure_ascii=False),flush=True)
 with (R/(sys.argv[1]+'_source_summary.json')).open('x',encoding='utf-8') as out:json.dump(dict(total=len(records),passed=sum(x['passed'] for x in records)),out)
if __name__=='__main__':main()
