"""Agent review of every migrated person role; keep unverified names in Thai."""
import sys,json,copy,re,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now
from app.knowledge.records import canonical_json
from app.knowledge.common.translation import protected
status=json.loads((B/'FINAL_final09/STATUS.json').read_text(encoding='utf-8'));assert status.get('complete') and status.get('database_unchanged')
roles={'ประชาสัมพันธ์':'Public relations','ผู้จัดการ':'Manager','กรรมการ':'Committee member','ประธาน':'Chair','นักวิชาการคอมพิวเตอร์':'Computer technical officer','คณบดี':'Dean','รองอธิการบดี':'Vice president','ผู้ช่วยอธิการบดีฝ่ายวิชาการ':'Assistant to the president for academic affairs','รองประธาน':'Vice chair','อธิการบดี':'President','เหรัญญิก':'Treasurer','เลขานุการ':'Secretary','นักศึกษาสหกิจ Web & AI Developer':'Cooperative education student: Web & AI Developer','นักศึกษาสหกิจ Game and 3D Developer':'Cooperative education student: Game and 3D Developer','นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer':'Intern in the Super AI SS6 project; role: AI Chat Bot Developer'}
s=CommonStore(B/'common.sqlite')
with s.connect() as c:rs=s.heads(c);active=dict(c.execute('SELECT * FROM cc_meta'))['active']
changes=[];reviewed=[]
for rid,r0 in rs.items():
 if r0['kind']!='person':continue
 r=copy.deepcopy(r0);fields={};lineage=[]
 for field in ('display_name','role'):
  v=value(r,field)
  if not isinstance(v,dict) or not v.get('th'):continue
  target=v['th'] if field=='display_name' and re.search(r'[\u0e00-\u0e7f]',v['th']) else roles.get(v['th'],v.get('en'))
  if field=='role' and re.search(r'[\u0e00-\u0e7f]',v['th']) and v['th'] not in roles:raise ValueError('Unreviewed role: '+v['th'])
  reviewed.append({'record_id':rid,'field':field,'th':v['th'],'reviewed_en':target,'official_romanization_verified':False})
  if target==v.get('en'):continue
  assert protected(v['th'])==protected(target)
  item={'record_id':rid,'field':field,'previous_en':v.get('en'),'en':target,'th':v['th'],'original_field_evidence':r0['fields'][field]['evidence_refs'],'reason':'Keep original Thai personal name; official English spelling unavailable' if field=='display_name' else 'Agent-reviewed role translation in its organization context','owner_reviewed':False};changes.append(item);lineage.append(item);v['en']=target;fields[field]=v
 if not fields:continue
 raw=canonical_json({'mapped_fields':fields,'translation_lineage':lineage,'agent_semantics_reviewed':True,'owner_semantics_reviewed':False});sid='r66_person_review_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'translation://r66-person-review/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['person'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None};s.add_source(source,raw,actor='r66-person-translation-review')
 for field,v in fields.items():r['fields'][field]['value']=v;r['fields'][field]['evidence_refs']=[{'source_id':sid,'locator':'/mapped_fields/'+field}]
 r['localization'].update(en_status='agent_translated',source_revision_hash=None);s.save(r,actor='r66-person-translation-review',expected_version=r0['revision'],change_note='Correct role mistranslations/rank inflation; retain original Thai personal names, do not invent official Romanization')
with s.connect() as c:assert dict(c.execute('SELECT * FROM cc_meta'))['active']==active
(B/'PERSON_TRANSLATION_REVIEW.json').write_text(json.dumps({'reviewed_fields':reviewed,'corrections':changes,'published':False,'owner_reviewed':False,'code_modified':False},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'reviewed_fields':len(reviewed),'changed_fields':len(changes),'published':False}))
