"""Fix the actual draft-preview boundary and preserve explicit source differences."""
import copy,hashlib,json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
p=H/'owner_server.py';s=p.read_text('utf8');s=s.replace("        class DraftView:\n            def snapshot(self):", "        class DraftView:\n            path=original_store.path\n            def connect(self,*,write=False):\n                if write:raise ValueError('Draft preview exposes read-only evidence access')\n                return original_store.connect()\n            @staticmethod\n            def sources(connection):return CommonStore.sources(connection)\n            def snapshot(self):");p.write_text(s,encoding='utf8')
catalog=json.loads((H/'catalog.json').read_text('utf8'));faq=next(c for c in catalog if c['kind']=='faq');vs={'type':'array','items':{'type':'object','properties':{'language':{'type':'string','enum':['th','en']},'text':{'type':'string','minLength':1},'reason':{'type':'string','minLength':1}},'required':['language','text','reason'],'additionalProperties':False}}
faq['fields'].append({'key':'source_variants','meaning_th':'ข้อความต้นทางที่แตกต่างกันและยังไม่เลือกเป็นนโยบายเดียว','publish_core':False,'reference_kind':None,'value_schema':vs});write(H/'catalog.json',catalog)
p=H/'schemas/faq.schema.json';schema=json.loads(p.read_text('utf8'));slot=copy.deepcopy(schema['properties']['fields']['properties']['topic']);slot['oneOf'][0]['properties']['value']=vs;schema['properties']['fields']['properties']['source_variants']=slot;write(p,schema)
p=H/'templates/faq.draft.json';t=json.loads(p.read_text('utf8'));t['fields']['source_variants']={'status':'unknown','value':None,'evidence_refs':[],'note':'ใช้เมื่อแหล่งเดิมมีความต่าง ไม่เลือกนโยบายแทนเจ้าของ'};write(p,t)
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now,value
from app.knowledge.records import canonical_json
store=CommonStore(B/'common.sqlite')
rows=[json.loads(s) for s in (B/'source_snapshot/data/rules/english_support_rules.jsonl').read_text('utf-8-sig').splitlines() if s.strip()];general=next(r for r in rows if r['id']=='rule_en_general_studio_rules')
thai='กฎหลักของศูนย์:\n• ฝากสัมภาระก่อนใช้บริการ ศูนย์ไม่รับผิดชอบทรัพย์สินที่สูญหาย\n• อาหารและเครื่องดื่มรับประทานได้เฉพาะพื้นที่ที่กำหนด\n• คืนอุปกรณ์และแผ่นเกมหลังใช้บริการ\n• หลีกเลี่ยงเสียงดังเกินควร การด่าทอ หรือคำพูดเสียดสี\n• ห้ามเคลื่อนย้ายอุปกรณ์หรือสิ่งของโดยไม่ได้รับอนุญาต และห้ามเสียบปลั๊กไฟส่วนตัวโดยไม่ได้รับอนุญาต\n• ห้ามสูบบุหรี่ ยาเสพติด แอลกอฮอล์ อาวุธ การทะเลาะวิวาท และการพนัน\n• ความเสียหายต่ออุปกรณ์อาจมีค่าซ่อมหรือค่าชดเชยตามระดับความเสียหาย'
repairs=[('migrated_faq_rule_en_general_studio_rules',{'answer':{'th':thai,'en':general['answer_en']}},'data/rules/english_support_rules.jsonl','Restored complete original English rule summary; Thai translated directly from that source; old short version retained')]
penalty=[json.loads(s) for s in (B/'source_snapshot/data/rules/penalty_rules.jsonl').read_text('utf-8-sig').splitlines() if s.strip()];damage=next(r for r in penalty if r['id']=='rule_damage_responsibility')
repairs.append(('migrated_faq_rule_damage_responsibility',{
 'source_variants':[{'language':'th','text':damage['answer_th'],'reason':'Thai source does not explicitly limit liability to improper or negligent use.'},{'language':'en','text':damage['answer_en'],'reason':'English source explicitly limits liability to improper or negligent use; not silently merged into Thai policy.'}],
 'scope_note':{'th':'ต้นฉบับไทยและอังกฤษระบุเงื่อนไขความรับผิดชอบไม่เท่ากัน: อังกฤษกล่าวถึงการใช้ผิดวิธีหรือประมาท แต่ไทยไม่ได้ระบุเงื่อนไขนี้ชัดเจน จึงยังยืนยันขอบเขตดังกล่าวไม่ได้ ตัวเลขข้างต้นเป็นอัตราที่บันทึกไว้','en':'The Thai and English sources differ on liability conditions: English refers to improper or negligent use, while Thai does not explicitly state that limitation. That scope remains unconfirmed; the figures above are the recorded amounts.'}
},'data/rules/penalty_rules.jsonl','Preserve both original source variants and disclose unresolved liability scope; no new policy selected'))
saved=[]
for rid,fields,rel,note in repairs:
 r=store.get(rid)['record'];data={'mapped_fields':fields,'source_path':rel,'source_sha256':hashlib.sha256((B/'source_snapshot'/rel).read_bytes()).hexdigest(),'previous_evidence':{k:r['fields'].get(k,{}).get('evidence_refs',[]) for k in fields},'change_reason':note}
 raw=canonical_json(data);sid='r67_source_difference_'+hashlib.sha256(raw.encode()).hexdigest()[:20]
 store.add_source({'source_id':sid,'kind':'derived_curated','path':'migration://r67/differences/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['faq'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='r67-source-difference-review')
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/mapped_fields/'+k}],'note':note}
 r['localization']['en_status']='agent_translated';saved.append(store.save(r,expected_version=r['revision'],actor='r67-source-difference-review',change_note=note))
write(B/'SOURCE_DIFFERENCE_REPAIRS.json',saved)
p=H/'answer_profiles.json';profiles=json.loads(p.read_text('utf8'));profiles['kinds']['faq']={'context':[{'when':['answer'],'include':['scope_note']}]};write(p,profiles)
p=H/'answer.py';s=p.read_text('utf8');needle="        def add(r,keys):\n            rows=[]"
assert needle in s;s=s.replace(needle,"        def add(r,keys):\n            rows=[]\n            if r['kind']=='faq' and value(r,'source_variants'):\n                plan.setdefault('scope_limits',[]).append({'record_id':r['record_id'],'reason':'unresolved_original_source_scope_difference'})");p.write_text(s,encoding='utf8')
manifest=[{'path':p.relative_to(B/'system').as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (B/'system/app').rglob('*') if p.is_file() and '__pycache__' not in p.parts]
write(B/'FROZEN_CODE_MANIFEST_final03.json',manifest)
print('Owner evidence proxy fixed; source summary restored; liability scope difference preserved')
