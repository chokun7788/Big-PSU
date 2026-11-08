"""Review retained sources and freeze identity alignment before HTTP answers."""
import collections,hashlib,json,re,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.projection import compile_snapshot,value
def read(p):return json.loads(p.read_text('utf8'))
def write(name,v):(R/name).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
base=read(B/'r113_multi_flow_benchmark_20261021/COMMON_READ_MODEL.json');old={f['id']:f for f in base['facts']}
snapshot=DraftSnapshotView(CommonStore(R/'system/data/knowledge/common.sqlite')).snapshot();records=snapshot['release']['records']
native=compile_snapshot(snapshot);bykey=collections.defaultdict(list)
for f in native['facts']:
    bykey[(f['record_id'],f['facet'])].append(f)
    if f.get('source_record_id'):bykey[(f['source_record_id'],f['facet'])].append(f)
alignment={};missing=[];drift=[]
for fid,f in old.items():
    matches=list({n['id']:n for n in bykey[(f['record_id'],f['facet'])]}.values())
    if f.get('fixture'):alignment[fid]={'kind':'fixture_absent_from_native','legacy':f};continue
    if len(matches)!=1:
        alignment[fid]={'kind':'projection_gap' if f['record_id'] in records else 'source_mapping_gap','legacy':f,'matches':[n['id'] for n in matches]};missing.append(fid);continue
    n=matches[0];alignment[fid]={'kind':'aligned','legacy':f,'native':n}
    if f['value']!=n['value']:drift.append({'id':fid,'native_id':n['id'],'legacy_value':f['value'],'native_value':n['value'],'numeric':n.get('numeric')})
jobs=list(map(json.loads,(R/'EXISTING_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()))
expected=[]
for j in jobs:
    goals=[]
    lang=j['locale'] if j['locale']!='auto' else ('th' if re.search('[\u0e00-\u0e7f]',j['question']) else 'en')
    for c in j['expected']['claims']:
        a=alignment[c['fact_id']];n=a.get('native');goal={'legacy_fact_id':c['fact_id'],'alignment_kind':a['kind'],'legacy_expected':c}
        if n:
            numeric=c.get('numeric')
            if numeric is not None and n.get('numeric')!=a['legacy'].get('numeric'):
                numeric=n.get('numeric')
                if n['category']=='C06' and n['facet']=='amount' and numeric is not None:numeric*=j['expected'].get('sessions',1)
            goal.update(native_fact_id=n['id'],native_record_id=n['record_id'],facet=n['facet'],value=n['value'][lang],numeric=numeric,
                evidence_refs=n['evidence_refs'],legacy_record_id=a['legacy']['record_id'])
        goals.append(goal)
    expected.append({'id':j['id'],'category':j['category'],'locale':lang,'expected_status':j['expected']['status'],'goals':goals,
        'fixture_only_goal':bool(goals) and all(g['alignment_kind']=='fixture_absent_from_native' for g in goals)})
write('NATIVE_SOURCE_REFERENCE.json',native);write('SOURCE_ALIGNMENT.json',{'alignment':alignment,'missing':missing,'value_drift':drift,
 'basis':'source identities and current pinned fields compiled before observing HTTP answers; not an independent semantic oracle'})
write('NATIVE_EXPECTATIONS.json',{'questions':expected,'questions_changed':False,'native_reference_uses_shared_projection':True,
 'metric_limits':'Identity/value/source contract and literal coverage only; source compilation defects require source review; no human accuracy claim'})
calendar=[]
for rid,r in records.items():
    if r['kind']=='schedule':calendar.append({'id':rid,'validity':r['validity'],'fields':{k:r['fields'].get(k) for k in ['weekday','zone_ids','open_periods','bookable_periods','maintenance_periods']}})
statements=read(B/'r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json')['statements']
opening=[s for s in statements if s.get('source_question_id')=='R108_OPEN_16_18']
billing=[s for s in statements if s.get('source_question_id')=='Q049']
rate_reviews=[{'record_id':rid,'fields':{k:r['fields'].get(k) for k in ['service_id','audience_id','amount_minor','unit','persons_min','persons_max','duration_minutes','calculation_rule']},'validity':r['validity']} for rid,r in records.items() if r['kind']=='rate' and 'vr' in rid.lower()]
with sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as c:
    source_evidence={row[0]:{'metadata':json.loads(row[1]),'snapshot':json.loads(row[2])} for row in c.execute('select source_id,payload,snapshot from cc_sources') if row[0] in {ref['source_id'] for r in rate_reviews for f in r['fields'].values() if f for ref in f.get('evidence_refs',[])}}
review_rows=[]
for x in map(json.loads,(B/'r114_domain_flow_integration_20261021/verification/comparison06/analysis/ALL_FAILURES.jsonl').read_text('utf8').splitlines()):
    if x['category']!='C13':continue
    returned=[old[c['fact_id']] for c in x['result']['claims']];paragraphs=[]
    for f in returned:
        ref=f['evidence_refs'][0];doc=ref['source_id'].split(':')[-1];extract=read(B/f'r108_owner_intake_20261020/{doc}_EXTRACT.json')
        number=int(re.search(r'paragraph\[(\d+)\]',ref['locator'])[1]);p=next(p for p in extract['paragraphs'] if p['paragraph']==number)
        assert p['text']==f['value']['th'] and extract['sha256']==ref['source_sha256']
        paragraphs.append({'paragraph':number,'text':p['text'],'source_sha256':extract['sha256'],'heading':f['label']['th']})
    review_rows.append({'id':x['question_id'],'question':x['question'],'source_verified_paragraphs':paragraphs,
        'review_decision':'heading-level question covers the returned same-heading source paragraphs; original one-paragraph oracle under-specifies that request',
        'original_strict_failure_retained':True,'no_question_rerun':True})
write('SOURCE_REVIEW.json',{'schedules':calendar,'owner_opening_confirmation':opening,'owner_billing_confirmation':billing,'vr_rates':rate_reviews,
 'vr_raw_sources':source_evidence,'six_rulebook_reviews':review_rows,'real_data_changed':False,'approvals_created':0})
lines=['# ขั้น 1 — ตรวจหลักฐานเดิมก่อนยิงแชทจริง','','## เวลาเปิด','',
 'เจ้าของยืนยันเฉพาะวันจันทร์–ศุกร์ 16:00–18:00 ว่าปิด ไม่ได้ยืนยันช่วงเปิดทั้งหมด ตาราง native วันธรรมดา open_periods=conflicted; zone_ids และ validity ยัง unknown จึงไม่เปลี่ยนเป็นเปิด 09:00–16:00 โดยไม่มีหลักฐาน ตารางจอง/เวลาเหมาเป็นคนละ predicate',
 '', '## ราคา VR','',
 'Q049 ยืนยัน “ทั้งหมดคิดต่อคน” ซึ่ง R114 ผูกกับ hash ของ rates เดิมไว้แล้ว ตาราง VR มีช่วงจำนวนคน 1–5; unit และ calculation_rule เดิมยัง unknown คำยืนยันต่อคนไม่ยืนยันส่วนลด การปัดเศษ การเพิ่ม capacity หรือ booking eligibility เกินช่วง ดังนั้นตรวจผลรวมหลายรอบตามหน่วยที่ยืนยันแยกจากการอนุญาตให้จอง และจะไม่ขยายช่วงราคา/จำนวนคนเอง',
 '', '## กติกา 6 ข้อ','',
 'ไม่ได้ส่งคำถามเพิ่มหรือรันทดสอบซ้ำทั้ง 6 ข้อ ใช้คำตอบ/log เดิม อ่านย่อหน้าจาก snapshot เอกสารและตรวจ SHA/text ตรงกับต้นฉบับที่เก็บไว้ คำถามถามทั้งหัวข้อ การคืนหลายย่อหน้าหัวข้อเดียวกันจึงมีเหตุผลตาม source; คงผล strict เดิมไว้และแยกเป็นข้อบกพร่องความละเอียดของ oracle ไม่บังคับให้ตอบเพียงย่อหน้าสุ่ม',
 '', '## เกณฑ์รอบ HTTP','',
 'ส่งข้อความ/locale ของคำถามเดิม 1,400 ข้อเท่านั้น ไม่มี category hint คง expected เดิม และเก็บการจับคู่ record/facet กับ native ก่อนดูคำตอบ รอบนี้ไม่ใส่ fake live/news fixture ลงฐานข้อมูลจริง ข้อ fixture ที่ไม่มี source จะแยกจากคะแนนเนื้อหาที่ตอบได้ ไม่เอาการตอบ unavailable มาบวกเป็น answered accuracy',
 '',f"Native facts {len(native['facts'])}; legacy facts aligned {sum(a['kind']=='aligned' for a in alignment.values())}; mapping/projection gaps {len(missing)}; source value/presentation differences {len(drift)}",'',
 'เกณฑ์ native ใช้ projection ร่วมเพื่อจัด identity/รูปแบบ จึงต้องตรวจ drift และ source แยก ไม่ใช่ independent human semantic evaluation','']
for x in review_rows:
    lines += ['## '+x['id'],'',x['question'],'']
    for p in x['source_verified_paragraphs']:lines += [f"- ย่อหน้า {p['paragraph']}: {p['text']}"]
    lines+=['']
(R/'01_SOURCE_REVIEW_TH.md').write_text('\n'.join(lines),'utf8')
print(json.dumps({'native_facts':len(native['facts']),'aligned':sum(a['kind']=='aligned' for a in alignment.values()),'gaps':len(missing),'drifts':len(drift),'rule_reviews':len(review_rows),'existing_questions':len(expected)}))
