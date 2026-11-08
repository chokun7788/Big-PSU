import json,re
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r55_current_path.txt').read_text())
rows=json.loads((OUT/'controls_final7.json').read_text(encoding='utf-8'));checks=[]
requirements={
 'c123':['PC','70','บุคคลทั่วไป'],
 'c124':['Arena of Valor','รูปแบบการแข่งขัน','อุปกรณ์การแข่งขัน','การหยุดเกม','บทลงโทษ'],
 'c139':['Left Mouse Button','R:','ยังไม่ได้ตรวจยืนยัน'],
 'c140':['Left Mouse Button','R: Reload','secondary'],
 'c141':['TEKKEN 8','Square','Triangle','Cross','Circle','L1','R1','Options','ตัวละครทั่วไป','ยังไม่ได้ตรวจยืนยัน'],
 'c142':['TEKKEN 8','Square','Triangle','Cross','Circle','L1','R1','Options','secondary'],
 'c143':['i5-14400','32GB','5060','โปรเจกต์'],
 'c144':['i5-14400','32GB','5060','local','does not independently confirm'],
 'c152':['VALORANT','Counter-Strike 2','140','120'],
 'c153':['VALORANT','Counter-Strike 2','140','120'],
}
for row in rows:
    z=row['job']['result'];cid=row['case']['id'];a=z['answer']
    errors=['missing:'+s for s in requirements[cid] if s.casefold() not in a.casefold()]
    if 'بشكل' in a:errors.append('source_language_contamination')
    if cid=='c124' and z['mode']!='pipeline:competition_rule_overview_source':errors.append('missing_broad_overview')
    if cid=='c124':
        overview=next((t['metadata'] for t in z.get('trace',[]) if t.get('stage')=='competition_overview'),{})
        if overview.get('game_ids')!=['rov'] or len(set(overview.get('section_ids',[])))<3:errors.append('missing_multi_section_source_evidence')
    if cid=='c141' and len(re.findall(r'^•',a,re.M))!=12:errors.append('incomplete_12_control_rows')
    checks.append(dict(case_id=cid,kind='source_content_audit',required_terms=requirements[cid],errors=errors))
with (OUT/'controls_semantic_audit_v2.json').open('x',encoding='utf-8') as f:json.dump(dict(checks=checks,oracle_revision='Original audit incorrectly required the heading ข้อห้าม. Existing RoV overview defines format/equipment/pause/penalty facets; verify these source-backed facets and multi-section evidence instead. No new pipeline run.',previous_result_preserved='controls_semantic_audit.json'),f,ensure_ascii=False,indent=2)
print(json.dumps(checks,ensure_ascii=False,indent=2));assert not any(c['errors'] for c in checks)
