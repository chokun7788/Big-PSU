"""Render manually curated methods/mappings; never query model or edit runtime data."""
import collections,csv,datetime,hashlib,json,re
from pathlib import Path
from research_data import REFERENCES,METHODS
from issue_mapping import ISSUES,GAP_METHODS

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
PROJECT=BASE.parent
AUDIT=PROJECT/'r135_complete_flow_audit_20261026'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda name,data:(HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
esc=lambda s:str(s).replace('|',r'\|').replace('\n',' ')
refs={r['id']:r for r in REFERENCES};methods={m['id']:m for m in METHODS}
expected=read(BASE/'ISSUE_AUDIT_MANIFEST.json')['grouped_issue_ids']
assert set(expected)==set(ISSUES) and len(ISSUES)==100
gaps=read(AUDIT/'AUDIT_GAPS.json')['gaps']
assert {int(g['id'][1:]) for g in gaps}==set(GAP_METHODS)
for m in METHODS:
    assert set(m['refs'])<=refs.keys()
    assert set(m['combine'])<=methods.keys()
for i in ISSUES.values():assert set(i['methods'])<=methods.keys()
for v in GAP_METHODS.values():assert set(v)<=methods.keys()

def method_links(ids):return ', '.join(f'[{x}](#method-{x.lower()})' for x in ids)
def ref_links(ids):return ', '.join(f'[{x}: {refs[x]["title"]}]({refs[x]["url"]})' for x in ids)

path=BASE/'RESEARCH_METHODS_FOR_ALL_ISSUES_TH.md'
text=path.read_text(encoding='utf8').split('<!-- GENERATED_RESEARCH -->')[0].rstrip()
lines=[text,'','<!-- GENERATED_RESEARCH -->','## 10. รายละเอียดเทคนิคทั้ง 26 กลุ่ม','',
       'ทุกช่อง “นำมาใช้” ด้านล่างเป็นข้อเสนอPSUที่สังเคราะห์ขึ้นจากหลักฐาน ไม่ใช่การอ้างว่าผู้วิจัยทดสอบimplementationนี้แล้ว หลายส่วนมีอยู่ในcandidateบางขอบเขต ให้ตรวจcode/data/config/HTTPล่าสุดก่อนตัดสินว่าต้องเพิ่มส่วนใด','']
for m in METHODS:
    lines += [f'<a id="method-{m["id"].lower()}"></a>',f'### {m["id"]} — {m["name"]}','',
              f'- **หลักฐานต้นฉบับ:** {ref_links(m["refs"])}',
              f'- **วิธีนำมาใช้กับPSU:** {m["proposal"]}',
              f'- **จุดเชื่อม:** {m["where"]}',
              f'- **เกณฑ์ที่ต้องตรวจ:** {m["acceptance"]}',
              f'- **ข้อจำกัด/สิ่งที่ห้ามสรุป:** {m["limit"]}',
              f'- **ใช้ร่วมกับ:** {method_links(m["combine"])}',
              f'- **ลักษณะต้นทุนที่ประเมินเชิงออกแบบ:** {m["cost"]} — ยังไม่ใช่เวลาหรือbenchmarkใหม่','']

issue_rows={}
for line in (BASE/'ALL_KNOWN_ISSUES_TH.md').read_text(encoding='utf8').splitlines():
    match=re.match(r'^\| ((?:D|T|I|L|F|V|O|Q)\d{2}) /',line)
    if match:
        cells=line.split('|');issue_rows[match.group(1)]=dict(status=cells[1].strip(),finding=cells[2].strip())
assert set(issue_rows)==set(expected)
lines += ['## 11. จับคู่ครบ 100 ประเด็นจากรายงานปัญหา','',
          'ช่องวิธีหลักเป็นlinksไปmethodcardsซึ่งมีprimarycitationsและข้อจำกัดครบ ไม่ใช่แนะนำลง26เทคนิคพร้อมกันทุกคำถาม เลือกเฉพาะdependencyที่เกี่ยวกับoperationนั้น ส่วนstateเดิมคงไว้ไม่เปลี่ยนเป็นfixed','']
groups={'D':'ข้อมูล/ต้นทาง','T':'เวลา/โมเดล','I':'เจตนา/ตีโจทย์','L':'คำผิด','F':'ราคา/จอง/เวลา','V':'ตัวตรวจ/ความครบ','O':'คำตอบ/อ้างอิง','Q':'owner/runtime/eval/training'}
for prefix,label in groups.items():
    lines += [f'### กลุ่ม {prefix} — {label}','','| ID/สถานะเดิม | ปัญหาที่ใช้จับคู่ | เทคนิคหลัก | การปรับที่เสนอ | สิ่งที่ต้องพิสูจน์ |','|---|---|---|---|---|']
    for id in expected:
        if not id.startswith(prefix):continue
        i=ISSUES[id];old=issue_rows[id]
        lines.append('| '+' | '.join([esc(old['status']),esc(old['finding']),method_links(i['methods']),esc(i['change']),esc(i['verify'])])+' |')
    lines.append('')

lines += ['## 12. เชื่อม historical audit gaps ทั้ง 143 ID','',
          'เป็นmanual method assignmentจากfindingที่บันทึก ไม่ใช่keywordauto-classificationและไม่เปลี่ยนstateเดิม กรณีที่componentเคยแก้แล้วควรใช้วิธีนี้ตรวจregression/portabilityก่อน ไม่แก้ซ้ำโดยไม่มีfailureใหม่ ให้เปิดfindingเต็มและevidenceในALL_KNOWN_ISSUES_TH.md/AUDIT_GAPS.jsonประกอบ','',
          '| Gap | Requirements ที่เกี่ยว | Finding เดิม | เทคนิคที่ใช้ประกอบ | สถานะเดิม |',
          '|---|---|---|---|---|']
for gap in gaps:
    lines.append('| '+' | '.join([gap['id'],', '.join(gap.get('requirements',[])),esc(gap.get('finding','')),method_links(GAP_METHODS[int(gap['id'][1:])]),'`'+esc(gap.get('state',''))+'`'])+' |')

ledger=read(AUDIT/'COMPLETION_LEDGER.json')['requirements']
requirement_map={}
lines += ['','### เชื่อมกลับไป requirement ledger ทั้ง 76 ข้อ','',
          'ตารางนี้รวมการจับคู่จาก gap IDs ข้างต้น ไม่ใช่การ audit หรือคิดวิธีแก้ requirement ใหม่ทุกข้อ ช่องเทคนิคแสดงไม่เกิน5กลุ่มที่ปรากฏบ่อย รายการเต็มอยู่ requirement_method_map.json หากข้อใดไม่มี gap เชื่อม ห้ามสรุปว่าผ่าน: ต้องทบทวนขอบเขตนั้นแยกและใช้ M24/M21 เป็นกระบวนการตรวจ ไม่ใช่คำตอบเชิง implementation','',
          '| Requirement | ชื่อที่บันทึก | Gap ที่เชื่อม | เทคนิคจาก gaps (สรุปไม่เกิน5) | acceptance state เดิม |',
          '|---|---|---|---|---|']
for row in ledger:
    related=[g for g in gaps if row['id'] in g.get('requirements',[])]
    counts=collections.Counter(x for g in related for x in GAP_METHODS[int(g['id'][1:])])
    top=[x for x,n in counts.most_common(5)]
    requirement_map[row['id']]=dict(gaps=[g['id'] for g in related],all_methods=sorted(counts),acceptance=row.get('behavior_acceptance_state'),inferred_from_gap_mapping=True,independent_requirement_review=False)
    lines.append('| '+' | '.join([row['id'],esc(row.get('title','')),', '.join(g['id'] for g in related) or 'ไม่มี gap เฉพาะที่ผูกในทะเบียน',method_links(top) if top else 'ต้องทบทวนเฉพาะข้อ;กระบวนการ M24/M21',esc(row.get('behavior_acceptance_state',''))])+' |')

lines += ['','## 13. ทะเบียนแหล่งอ้างอิงและขอบเขตที่อ่านจริง','',
          'R01–R31 เป็นงานวิจัย E01–E11 เป็นเอกสารทางการ;manualrelevance0–10เป็นความเกี่ยวข้องกับปัญหา ไม่ใช่คะแนนคุณภาพงานหรือcitationimpact ตัวเลือกที่ควรเลื่อนไว้ภายหลังยังถูกเก็บเพื่ออธิบายเหตุผลไม่ใช้ทันที','']
for r in REFERENCES:
    label=str(r['year']) if r['year'] else 'เอกสารทางการ;ตรวจ11Nov2026'
    lines += [f'### {r["id"]} — {r["title"]} ({label})','',
              f'- **ต้นฉบับ:** [{r["title"]}]({r["url"]})',
              f'- **สิ่งที่นำมาอ้าง:** {r["contribution"]}',
              f'- **ขอบเขต/ข้อจำกัด:** {r["limit"]}',
              f'- **ระดับที่ตรวจ:** {r["reading_level"]};manualrelevance={r["manual_relevance"]}/10']
    if r.get('doi'):lines.append(f'- **DOI:** `{r["doi"]}`')
    lines.append('')

lines += ['## 14. สิ่งที่รายงานนี้ยังตอบแทนการทดลองไม่ได้','',
          '- ยังไม่รู้ว่าการรวมชุดA–Gทำให้คะแนนPSUดีขึ้นกี่เปอร์เซ็นต์หรือใช้เวลากี่ชั่วโมงจบ ต้องเปลี่ยนcandidateและวัดผลจริงภายหลัง',
          '- ยังไม่รู้thresholdของtypo/clarification/admissionที่เหมาะกับข้อมูลจริง จึงไม่เอาค่าตั้งต้นไปเรียกcalibratedconfidence',
          '- ไม่มีpaperใดให้authority/effectivedates/operatorrole/attachmentcontentที่เจ้าของหรือเว็บยังไม่ยืนยัน',
          '- ไม่มีผลtraining/distillationหรือการpromoteweightsใหม่ และไม่มีสิทธิ์ใช้evaluationholdoutเป็นtrainingแล้วอ้างunseenเหมือนเดิม',
          '- การจับคู่ครบ100+143เป็นความครอบคลุมรายการปัญหาที่มี ไม่ใช่เปอร์เซ็นต์ครอบคลุมงานวิจัยหรือหลักฐานว่าระบบไม่มีunknownbugs',
          '- ควรทำsmallestsharedcontractchangeแล้วfocusedpositive/negative/affectedregression ก่อนbroadrun ไม่เพิ่มmodelcallทุกชั้นเพื่อให้ดูมีtechniqueครบ','']
rendered='\n'.join(lines)
# Separate Thai prose from Latin technical terms without rewriting URLs/IDs.
rendered=re.sub(r'([\u0e00-\u0e7f])([A-Za-z])',r'\1 \2',rendered)
rendered=re.sub(r'([A-Za-z])([\u0e00-\u0e7f])',r'\1 \2',rendered)
path.write_text(rendered,encoding='utf8')
write('references.json',REFERENCES)
write('methods.json',METHODS)
write('issue_method_map.json',{id:{**ISSUES[id],**issue_rows[id]} for id in expected})
write('gap_method_map.json',{g['id']:dict(methods=GAP_METHODS[int(g['id'][1:])],original_state=g.get('state'),finding=g.get('finding')) for g in gaps})
write('requirement_method_map.json',requirement_map)
with (HERE/'papers.csv').open('w',encoding='utf-8-sig',newline='') as f:
    fields=['id','title','year','kind','doi','url','manual_relevance','reading_level','contribution','limit']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:r.get(k) for k in fields} for r in REFERENCES)
safe=lambda s:str(s).replace('{',r'\{').replace('}',r'\}')
bib=[]
for r in REFERENCES:
    if r['kind']!='paper':continue
    entry=[f'@misc{{psu_{r["id"].lower()},',f'  title = {{{safe(r["title"])}}},',f'  year = {{{r["year"]}}},',f'  url = {{{r["url"]}}}']
    if r.get('doi'):entry[-1]+=',';entry.append(f'  doi = {{{r["doi"]}}}')
    entry.append('}');bib.append('\n'.join(entry))
(HERE/'papers.bib').write_text('\n\n'.join(bib)+'\n',encoding='utf8')
manifest=dict(created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              report=str(path),references=len(REFERENCES),papers=sum(r['kind']=='paper' for r in REFERENCES),
              official_documents=sum(r['kind']=='official_documentation' for r in REFERENCES),
              method_families=len(METHODS),issue_ids=expected,historical_gap_ids=[g['id'] for g in gaps],
              requirement_ids=[r['id'] for r in ledger],requirement_mapping_basis='aggregation of gap mapping; not independent requirement acceptance',
              literature_coverage_estimate=None,new_inference_calls=0,new_benchmark_runs=0,
              implementation_changed=False,semantic_improvement_measured=False,
              bibliography_note='Minimal verified title/year/URL/DOI export; author/venue fields not fabricated. Use primary pages for full publication citations.',
              primary_issue_report_sha256=hashlib.sha256((BASE/'ALL_KNOWN_ISSUES_TH.md').read_bytes()).hexdigest(),
              gap_registry_sha256=hashlib.sha256((AUDIT/'AUDIT_GAPS.json').read_bytes()).hexdigest(),
              requirement_ledger_sha256=hashlib.sha256((AUDIT/'COMPLETION_LEDGER.json').read_bytes()).hexdigest(),
              report_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
manifest['artifacts']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in HERE.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
write('MANIFEST.json',manifest)
print(json.dumps({k:manifest[k] for k in ['report','references','papers','official_documents','method_families']}|{'mapped_issues':len(expected),'mapped_gaps':len(gaps),'lines':len(path.read_text(encoding='utf8').splitlines())},ensure_ascii=False))
