import json,sys,collections,hashlib,subprocess,re
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r32_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
load=lambda name:json.loads((R/name).read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
summary=load('final13_SUMMARY.json');paired=[json.loads(l) for l in (R/'final13_PAIRED.jsonl').open(encoding='utf-8')];reg={x['id']:x for x in paired if x['v2']['regression']};rawpairs={}
allfail=collections.Counter();groups=collections.Counter();provenance=collections.Counter()
for line in (R/'final13_all_results.jsonl').open(encoding='utf-8'):
 x=json.loads(line);provenance[x.get('execution_provenance','unknown')]+=1
 fs=[g for g in x['grades'] if not g['passed']]
 if fs:
  kinds=set()
  for g in fs:
   for e in g['failures']:
    kind='legacy_label_or_intent' if e.startswith(('intent:','legacy_','route:')) else 'status_or_abstention_contract' if e.startswith(('status:','outcome ')) else 'source_identity_contract' if 'evidence' in e or 'rulebook target' in e else 'text_or_content_contract' if e.startswith(('missing ','missing:')) else 'other_gate'
    kinds.add(kind)
  allfail.update(kinds)
 for g in x['grades']:
  if g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl' and g['id'] in reg:
   rawpairs.setdefault(g['id'],{})[g['variant']]=dict(question=x['question'],result=x.get('result',{}),expected=g['expected'],original_grade=g)

def classify(pair,score):
 z=pair['noisy']['result'];route=z.get('route',{}).get('category');stages={t['stage'] for t in z.get('trace',[])}
 if 'real_word_ambiguity' in stages:return 'คำจริงกำกวม ต้องถามกลับ', 'คำที่ผิดยังเป็นคำจริง เช่น pay/play; trace เลือกถามแทนการเปลี่ยนความหมาย การคาดว่าต้องตอบคำปกติจากสูตรสร้าง typo ไม่พิสูจน์เจตนาผู้ใช้จริง'
 if 'live' in z.get('mode','') or 'freshness' in z.get('mode',''):return 'ข้อมูลสดยังยืนยันไม่ได้', 'เส้นทางข้อมูลสด/ความสดไม่พร้อมใน fixture; ต้องตอบว่ายืนยันไม่ได้ ไม่อนุมานว่างจากตารางเปิดบริการ'
 if 'members' in score['domain']:return 'คำถามบุคคลและบทบาท', 'คำถามปกติและผิดอาจต่างเส้นทาง; ต้องตรวจชื่อจากต้นฉบับก่อน เพราะคำตอบรายชื่อรวมที่ผ่านเกณฑ์ route/status ไม่พิสูจน์บทบาทของบุคคลที่ถาม'
 if not score['v2']['noisy']['route_ok']:return 'คำสำคัญหรือหัวข้อเปลี่ยนเส้นทาง', 'trace แสดงหมวดคำตอบต่างจากสัญญาทดสอบ; ตรวจการกู้คำและการเลือกหัวข้อร่วมกับต้นฉบับก่อนขยายขอบเขตการแก้คำ'
 if not score['v2']['noisy']['content_ok']:return 'เนื้อหาไม่ครบตามสัญญา', 'ได้หมวด/สถานะที่ต้องการแต่ข้อความยังไม่ผ่านเงื่อนไขเนื้อหา; ตรวจว่าขาดข้อกฎจริงหรือเกณฑ์บังคับข้อความเก่าก่อนแก้ renderer'
 return 'สถานะคำตอบหรือเกณฑ์อื่น', 'ตรวจการถามกลับ/ไม่มีข้อมูล/เวลา จาก trace และสัญญารายข้อ; ยังไม่มีหลักฐานเพียงพอเรียกคำตอบนี้ผิดข้อเท็จจริงทุกกรณี'

details=[];md=['# วิเคราะห์คู่พิมพ์ผิดที่ยังไม่ผ่าน — r32\n','ข้อเท็จจริงที่อ่านได้จาก log แยกจากข้อสันนิษฐานสาเหตุ ตัวอย่างคำตอบปกติเป็น baseline ของระบบ ไม่ใช่คำตอบจริงที่เจ้าของยืนยัน\n','คะแนน confidence ของเส้นทางเร็วเป็นค่ากำหนด/heuristic; top_score และ margin ของตัวจับชื่อเป็นคะแนนภายใน ไม่ใช่ความน่าจะเป็นว่าคำตอบถูก\n']
for id,score in reg.items():
 pair=rawpairs[id];kind,reason=classify(pair,score);groups[kind]+=1;z=pair['noisy']['result'];trace=[t for t in z.get('trace',[]) if t.get('stage')!='timing']
 d=dict(id=id,locale=score['locale'],domain=score['domain'],classification=kind,classification_status='trace_observation_plus_hypothesis_not_human_adjudication',analysis=reason,positive_contract=score['v2']['noisy']['positive_contract_present'],score=score,clean=pair['clean'],noisy=pair['noisy']);details.append(d)
 md.extend([f'## {id} ({score["locale"]}) — {kind}\n',f'คำปกติ: {pair["clean"]["question"]}\n',f'คำผิด: {pair["noisy"]["question"]}\n',f'หมวดที่คาด: {pair["noisy"]["expected"].get("expected_route_categories")} / สถานะที่คาด: {pair["noisy"]["expected"].get("expected_answer_status")}\n',f'ข้อที่ไม่ผ่าน: {score["v2"]["noisy"]["failures"]}\n',f'มีเงื่อนไขเนื้อหาบวก: {d["positive_contract"]}; ถ้าไม่มี ยังพิสูจน์เนื้อหาคำตอบปกติไม่ได้\n',f'เหตุผล/ข้อจำกัดการวิเคราะห์: {reason}\n','### คำตอบปกติที่ระบบให้\n',pair['clean']['result'].get('answer','')+'\n','### คำตอบเมื่อพิมพ์ผิด\n',z.get('answer','')+'\n','### เงื่อนไขเนื้อหาเดิมที่ควรตรวจ\n','```json\n'+json.dumps(pair['noisy']['expected'].get('answer_contract',{}),ensure_ascii=False,indent=2)+'\n```\n','### การเลือกคำตอบและคะแนนที่บันทึกจริง\n','```json\n'+json.dumps(trace,ensure_ascii=False,indent=2)+'\n```\n'])
with (R/'REMAINING_107_FINAL13_DETAILED.jsonl').open('x',encoding='utf-8') as f:
 for x in details:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (R/'REMAINING_107_FINAL13_ANALYSIS_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(md))
guard=[json.loads(l) for l in (R/'native_guard_500/results.jsonl').open(encoding='utf-8')];guardmetrics=dict(total=len(guard),exact_flags=sum(x['expected_layout']==x['predicted_layout'] and x['expected_repeat']==x['predicted_repeat'] for x in guard),layout_flags_correct=sum(x['expected_layout']==x['predicted_layout'] for x in guard),repeat_false_negative=sum(x['expected_repeat'] and not x['predicted_repeat'] for x in guard),repeat_false_positive=sum(not x['expected_repeat'] and x['predicted_repeat'] for x in guard))
analysis=dict(full=summary,execution_provenance=provenance,failed_unique_multilabel_types=allfail,remaining_pairs=len(reg),remaining_positive=sum(x['positive_contract'] for x in details),remaining_by_locale=collections.Counter(x['locale'] for x in details),remaining_trace_hypothesis_groups=groups,native_guard=guardmetrics)
with (R/'FINAL13_ANALYSIS_METRICS.json').open('x',encoding='utf-8') as f:json.dump(analysis,f,ensure_ascii=False,indent=2)
# Correct a copied runner's legacy summary label with an explicit sidecar.
api=[]
for run in ['api8091_candidate6','api8091_candidate7','api8091_final9','api8091_final13']:
 h=load(run+'_health_before.json');s=load(run+'_http_summary.json')
 api.append(dict(run=run,legacy_summary_runtime_label=s.get('runtime'),verified_runtime_version=h['runtime']['version'],health_sha256=sha(R/(run+'_health_before.json')),results_sha256=sha(R/(run+'_http_results.jsonl')),passed=sum(x['passed'] for x in s['by_suite'].values()),total=sum(x['total'] for x in s['by_suite'].values()),note='Copied runner retained the literal r31 summary label. Health capture and package freeze identify r32; original output remains preserved.'))
with (R/'API_EXECUTION_PROVENANCE_FINAL13.json').open('x',encoding='utf-8') as f:json.dump(api,f,ensure_ascii=False,indent=2)
before=load('before_manifest.json');protected=load('protected_manifest.json');assert all(sha(P/k)==v for k,v in protected.items());changed_tests=[k for k,v in before.items() if k.startswith('tests/') and sha(P/k)!=v];assert not changed_tests
preservation=dict(protected_files_verified=len(protected),preexisting_test_files_verified=sum(k.startswith('tests/') for k in before),preexisting_tests_changed=changed_tests,before_snapshot_files=len(before),source_code_snapshot='before/',limitations='No initial all-log hash manifest was captured. Old artifacts were retained and new result files use exclusive creation; do not claim a cryptographic comparison of every historical log.')
with (R/'FINAL13_PRESERVATION.json').open('x',encoding='utf-8') as f:json.dump(preservation,f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=P,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (R/'git_status_final13.txt').open('x',encoding='utf-8') as f:f.write(status)
print(json.dumps({'remaining_groups':groups,'remaining_positive':analysis['remaining_positive'],'locales':analysis['remaining_by_locale'],'guard':guardmetrics,'preservation':preservation},ensure_ascii=False),flush=True)
