"""Read-only source inventory; unknowns are never filled to satisfy a grade."""
import collections,hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import CATALOG,value
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.capabilities import matrix
from app.knowledge.common.domain_flow.projection import title
db=R/'system/data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest();snap=MigratedView(db).snapshot();records=snap['release']['records'];engine=Engine.from_snapshot(snap)
gaps={'record_missing':[],'relation_missing':[],'applicability_missing':[],'conflict':[],'optional_unknown_fields':[]}
counts=collections.Counter(r['kind'] for r in records.values())
for kind in CATALOG:
 if not counts[kind]:gaps['record_missing'].append({'kind':kind,'status':'no_record_of_this_kind','not_proof_owner_omitted_required_data':True})
for rid,r in records.items():
 for spec in CATALOG[r['kind']]['fields']:
  key=spec['key'];f=r['fields'].get(key,{})
  if f.get('status')=='conflicted':gaps['conflict'].append({'record_id':rid,'field':key,'status':'source_conflicted','evidence_refs':f.get('evidence_refs',[])})
  if spec.get('reference_kind'):
   v=value(r,key);refs=v if isinstance(v,list) else [v] if v else []
   missing=[x for x in refs if x not in records]
   if missing or spec.get('publish_core') and f.get('status')!='known':gaps['relation_missing'].append({'record_id':rid,'field':key,'missing_target_ids':missing,'field_status':f.get('status'),'required_for_publish':spec.get('publish_core')})
  elif f.get('status') not in {'known','conflicted'}:gaps['optional_unknown_fields'].append({'record_id':rid,'field':key,'field_status':f.get('status'),'required_for_publish':bool(spec.get('publish_core'))})
 if r.get('validity',{}).get('state')=='unknown' and r['kind'] in {'rate','rental_package','schedule','policy','news','competition_rule'}:
  gaps['applicability_missing'].append({'record_id':rid,'kind':r['kind'],'reason':'effective_interval_not_confirmed','source_validity':r.get('validity')})
owner=[]
for p in [R.parent/'r109_owner_answers_20261020/REMAINING_OWNER_QUESTIONS.json',R.parent/'r109_owner_answers_20261020/REMAINING_LIMITS.json',R.parent/'r109_owner_answers_20261020/SOURCE_STATE.json',R.parent/'r108_owner_intake_20261020/OWNER_CLARIFICATIONS.json']:
 if p.is_file():owner.append({'path':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'historical_report_not_current_missing_count':True,'content':json.loads(p.read_text('utf-8-sig'))})
preserved=json.loads((R/'PARENT_FREEZE.json').read_text('utf8'));files=preserved.get('files',preserved)
if isinstance(files,list):files={x['path']:x['sha256'] for x in files}
proof={str(p):hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in files.items() if isinstance(h,str) and Path(p).is_file()}
result={'source_snapshot':{'release_id':snap['active'],'epoch':snap['epoch'],'migration_preview_only':True},'active_records':len(records),'withdrawn_records':len(snap.get('withdrawn',[])),'kinds':dict(counts),'gap_counts':{k:len(v) for k,v in gaps.items()},'gaps':gaps,'owner_submission_history':owner,'database_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest(),'parent_files_unchanged':all(proof.values()),'parent_files_checked':len(proof),'real_data_changed':False,'approvals_changed':False,'source_data_complete_claimed':False,'capability_matrix':matrix()}
(R/'SOURCE_DIAGNOSTICS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
lines=['# ตรวจข้อมูลและความสัมพันธ์ R129','','ข้อมูลที่ขาดกับ Flow ที่อ่านข้อมูลไม่ครบเป็นคนละสาเหตุ รายงานนี้อ่าน snapshot จริงโดยไม่แก้ข้อมูลหรือสถานะอนุมัติ','',f"- Active records: {len(records)}; withdrawn: {len(snap.get('withdrawn',[]))}",'- ไม่ตีความชนิด record ที่ไม่มีว่าเจ้าของต้องเพิ่มทุกชนิด และไม่เติมข้อมูลเพื่อให้คะแนนผ่าน','', '| กลุ่ม | จำนวนรายการ |','|---|---:|',*[f'| {k} | {len(v)} |' for k,v in gaps.items()],'','## การใช้ข้อมูลเจ้าของ','', 'ประวัติคำตอบและคำถามคงค้างต้นฉบับแนบใน SOURCE_DIAGNOSTICS.json พร้อม SHA256 รายงานเก่าไม่ใช่จำนวนข้อมูลที่ขาด ณ ปัจจุบัน ต้องเทียบ record/field/ความสัมพันธ์ใน snapshot นี้','', '## ข้อจำกัดที่ยังเป็นข้อมูลจริง','', '- ไม่มี game_mode จึงไม่อ้างว่าได้ยืนยันโหมด/จำนวนผู้เล่นของทุกเกมจากแคตตาล็อกชื่อเกมอย่างเดียว','- ช่วง effective interval ที่ไม่ยืนยันยังเป็น unknown; การยืนยันราคาวันหนึ่งไม่ยืนยันราคาทุกวันในอนาคต','- Source conflict ต้องแสดงขอบเขตที่ต่างกันหรือขอคำยืนยัน; trust flag หรือวันที่ใหม่กว่าไม่พอสำหรับเลือกแทนนโยบายเก่า','- Live provider unavailable ใน workload เป็น fixture; ไม่ใช่หลักฐานว่าบริการจริงล่ม','', '## หลักฐานการคงข้อมูล','',f"Database unchanged: {result['database_unchanged']}; parent files unchanged: {result['parent_files_unchanged']} ({len(proof)} files)."]
(R/'SOURCE_DIAGNOSTICS_TH.md').write_text('\n'.join(lines)+'\n','utf8');print(json.dumps({k:result[k] for k in ['active_records','withdrawn_records','gap_counts','database_unchanged','parent_files_unchanged','parent_files_checked']}))
