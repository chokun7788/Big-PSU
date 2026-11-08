"""Apply the evidence-backed native API fixes after the immutable baseline ends."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';base=R/'runs/http01'
assert json.loads((base/'TEST_COMPLETE.json').read_text('utf8'))['complete']
assert (base/'SERVER_STOPPED.json').exists()
assert not (R/'IMPLEMENTED.json').exists()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
frozen=json.loads((base/'RUN_FREEZE.json').read_text('utf8'))['files']
assert all(sha(Path(p))==h for p,h in frozen.items())
# Windows long-path aware archival: preserve the original candidate code/DB.
archive=base/'frozen_system'
def extended(p):return '\\\\?\\'+str(p.resolve())
shutil.copytree(extended(S),extended(archive),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.sqlite-wal','*.sqlite-shm'))
changed=[]
def patch(rel,old,new):
    p=S/rel;text=p.read_text('utf8');assert text.count(old)==1,(rel,old[:70],text.count(old))
    before=sha(p);p.write_text(text.replace(old,new),'utf8');changed.append({'file':rel,'before':before,'after':sha(p)})
D='app/knowledge/common/domain_flow/'

patch(D+'vocabulary.py','\ndef matches(pattern,text):',r'''
# The router and reader share these predicate frames. A generic word such as
# "announced" must not bypass a missing-predicate guard via another domain.
PREDICATE_GAPS={
 'C03':[(r'ประกัน|warranty',r'ประกัน|warranty')],
 'C07':[(r'โอที|overtime',r'โอที|overtime')],
 'C08':[(r'รับประกัน.*เครื่องสำรอง|เครื่องสำรอง.*รับประกัน|guarantee.*backup',r'เครื่องสำรอง|backup guarantee'),
        (r'ประวัติบัญชี.*ย้อนหลัง|account.*history.*days',r'ประวัติบัญชี|account history'),
        (r'ชื่อบริษัท.*สิทธิ์|company.*privilege|จองเป็นชื่อบริษัท',r'ชื่อบริษัท|company booking')],
 'C09':[(r'คริปโต|crypto',r'คริปโต|crypto'),(r'เครดิต.*หมดอายุ|credit.*expir',r'หมดอายุเครดิต|credit expiry'),
        (r'คืนเงิน.*ภายใน.*กี่วัน|refund.*within.*days|บัตรเครดิต.*กี่วัน',r'กำหนดเวลาคืนเงิน|refund deadline')],
 'C10':[(r'อายุขั้นต่ำ|ขั้นต่ำ.*(?:กี่ขวบ|กี่ปี)|minimum age',r'อายุขั้นต่ำ|minimum age'),
         (r'ถ่าย.*(?:ใบหน้า|คนอื่น|บุคคล)|film.*(?:people|other customers)',r'ถ่าย.*(?:บุคคล|คนอื่น)|film.*people'),
         (r'ค่าปรับ.*(?:ทุกชนิด|ตายตัว|กี่บาท)|ความเสียหายทุกชนิด',r'ค่าปรับตายตัว|fixed damage fine')],
}

def predicate_domain(q):
    # A backup guarantee is an operation policy, not equipment warranty.
    for cat in ['C08','C09','C10','C07','C03']:
        if any(matches(pattern,q) for pattern,_ in PREDICATE_GAPS[cat]):return cat
    return None

def matches(pattern,text):''')

p=S/(D+'readers.py');text=p.read_text('utf8');start=text.index('    predicate_gaps={');end=text.index('    for asked_pattern,source_pattern',start)
patch(D+'readers.py',text[start:end], '    from .vocabulary import PREDICATE_GAPS\n    predicate_gaps=PREDICATE_GAPS\n')

patch(D+'index.py','    def rank(self,cat,question,pool=None,limit=12):', '''    def record_mentions(self,question):
        # Native identifiers are opaque entity labels, never a bag of words.
        mentions=[rid for rid in self.byrecord if contains(question,rid)]
        return [rid for rid in mentions if not any(rid!=other and rid in other for other in mentions)]

    def rank(self,cat,question,pool=None,limit=12):''')
patch(D+'index.py','        q=norm(question);labels=self.subject_labels[cat]', '''        explicit=[f for rid in self.record_mentions(question) for f in self.byrecord[rid] if f['category']==cat]
        if explicit:return explicit
        q=norm(question);labels=self.subject_labels[cat]''')

patch(D+'routing.py','    strong={cat:', '''    # Bind a complete current record ID before interpreting words embedded in
    # it (e.g. a rate ID can contain "staff" or "availability").
    explicit={f['category'] for rid in index.record_mentions(q) for f in index.byrecord[rid]}
    if len(explicit)==1:return next(iter(explicit))
    from .vocabulary import predicate_domain
    guarded=predicate_domain(q)
    if guarded:return guarded
    strong={cat:''')

patch(D+'financial.py',"    records=index.records;services={k:r for k,r in records.items() if r['kind']=='service'}",'''    records=index.records
    explicit={rid for rid in index.record_mentions(q) if records.get(rid,{}).get('kind')=='rate'}
    if explicit:return [f for f in index.bycat['C06'] if f['record_id'] in explicit]
    services={k:r for k,r in records.items() if r['kind']=='service'}''')

patch('app/pipeline/chatbot_identity.py','"เป็น model อะไร", "เป็นโมเดลอะไร", "ชื่ออะไร",','"เป็น model อะไร", "เป็นโมเดลอะไร",')
patch('app/pipeline/chatbot_identity.py',r'นาย(?!เป็น|เปน|คือ|นี่|นี|ทำ|ช่วย)[ก-ฮ]{2,}',r'(?:นางสาว|นาง|นาย)(?!เป็น|เปน|คือ|นี่|นี|ทำ|ช่วย|ตอบ|ชื่อ|ไคร|ใคร)[ก-๙]{2,}')
patch('app/pipeline/chatbot_identity.py','    if any(term in query for term in _IDENTITY_TERMS):', '''    if re.fullmatch(r"ชื่ออะไร(?:ครับ|ค่ะ|คะ)?[ ?!.]*",query):
        return True
    if any(term in query for term in _IDENTITY_TERMS):''')

patch(D+'readers.py',"    return field_reader(index,'C11',q)\n",'''    result=field_reader(index,'C11',q)
    limits=[]
    for fid in result.ids:
        f=index.byid[fid];record=index.records.get(f['record_id'],{})
        if record.get('kind')!='schedule':continue
        if record.get('fields',{}).get('zone_ids',{}).get('status')!='known':limits.append('zone_scope_unknown')
        if record.get('validity',{}).get('state','unknown')=='unknown':limits.append('effective_period_unknown')
        if record.get('fields',{}).get('open_periods',{}).get('status')=='conflicted':limits.append('opening_hours_conflicted')
    if limits:
        result.metadata['calendar_source_limits']=sorted(set(limits))
        if any(index.byid[f]['facet']=='bookable_periods' for f in result.ids):
            result.status='partial';result.reason='recorded_periods_applicability_unconfirmed'
    return result
''')

patch(D+'integration.py',"    if len(split_needs(question))==1 and cat=='C11':\n",'''    if len(split_needs(question))==1 and cat=='C11':
        # A recorded weekday period must not be replaced by a broad old FAQ
        # when the typed schedule's zone/effective scope is unknown.
        recorded=engine.plan('C11',question,at)
        if recorded.ids and all(engine.index.byid[f]['facet'] in {'bookable_periods','maintenance_periods'} for f in recorded.ids):
            result=engine.answer(question,locale,at=at,allow_llm=False,budget=budget)
            return package(reader,snap,started,question,result)
''')

patch(D+'integration.py',"    if len(split_needs(question))==1 and cat=='C12':\n",'''    if len(split_needs(question))==1 and cat=='C12':
        guard_plan=engine.plan('C12',question,at)
        if guard_plan.locked and guard_plan.reason in {'unknown_exact_resource','booking_reference_unconfirmed'}:
            return package(reader,snap,started,question,engine.answer(question,locale,at=at,allow_llm=False,budget=budget))
''')

patch(D+'engine.py',"        if computations and (billing or people and len(computations)==1):",'''        if plan.metadata.get('calendar_source_limits'):
            blocks.insert(0,('ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)' if lang=='th' else 'Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.'))
        if lang=='en' and any(f.get('english_translation_missing') for f in selected):
            blocks.insert(0,'A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.')
        if computations and (billing or people and len(computations)==1):''')

patch('app/knowledge/common/build_info.py','common-r114-domain-flow','common-r115-native-http-guards')
(R/'IMPLEMENTED.json').write_text(json.dumps({'baseline_preserved':str(archive),'data_changed':False,'approvals_changed':False,'changes':changed},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'changes':len(changed),'baseline_preserved':True,'data_changed':False}))
