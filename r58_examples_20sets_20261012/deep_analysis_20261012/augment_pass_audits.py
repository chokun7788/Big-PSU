"""Add complete Markdown for passed-quality audits; retain initial annotation version."""
import build_deep_report as d
import json,collections
def main():
    ann=json.loads((d.OUT/'CASE_ANNOTATIONS_5056.json').read_text(encoding='utf-8'))
    extra={r['id']:r for r in json.loads((d.OUT/'PASSED_EXTRA_UNKNOWN_MESSAGES.json').read_text(encoding='utf-8'))}
    bundle={r['id']:r for r in json.loads((d.OUT/'PASSED_DEFAULT_BUNDLE_COVERAGE.json').read_text(encoding='utf-8'))}
    refs=collections.defaultdict(list)
    for r in json.loads((d.OUT/'PASSED_INTERNAL_REFERENCE_RENDERING.json').read_text(encoding='utf-8')):refs[r['id']].append(r)
    nested=[]
    for r in d.ALL:
        if not r['passed']:continue
        for o in (r.get('decision') or {}).get('obligations',[]):
            rr=d.REC.get(o.get('record_id'))
            if rr and o.get('field')=='steps':
                for step in d.t.prior.value(rr,'steps') or []:
                    rid=step.get('contact_id')
                    if rid in d.REC and d.a.title(d.REC[rid],r['lang'])==rid and rid in r['answer']:
                        item={'id':r['id'],'kind':r['kind'],'field':'steps.order_'+str(step['order'])+'.contact_id','reference_id':rid,'target_kind':'contact'};nested.append(item);refs[r['id']].append(item)
    weak={r['id'] for r in d.ALL if r['passed'] and d.tags(r)}
    flags={}
    for r in ann:
        rid=r['case_id'];q=[]
        if rid in extra:q.append('extra_unknown_not_in_gold')
        if rid in bundle:q.append('gold_fields_covered_by_defaults_or_domain_bundles')
        if rid in refs:q.append('technical_reference_id_displayed')
        if rid in weak:q.append('unresolved_field_or_broad_trigger_review')
        r['quality_audit_flags']=q
        if q:r['explanation']+='; additional quality audit flags='+', '.join(q)
        flags[rid]=q
    d.put('CASE_ANNOTATIONS_5056_V2.json',ann)
    d.put('PASSED_NESTED_REFERENCE_RENDERING.json',nested)
    selected=[r for r in d.ALL if r['passed'] and flags[r['id']]]
    text=f'# ตรวจเคสคะแนนผ่านเพิ่มเติมครบ {len(selected)} เคส\n\nผ่าน required-content ไม่เท่ากับทุกมิติถูกต้อง ภาคนี้รวบรวมเคสที่ detector พบอย่างน้อยหนึ่งข้อสังเกต: extra unknown, default/domain bundle, broad/field unresolved และ technical reference รวม top-level กับ contact_idในsteps. ไม่ย้ายทุกเคสเป็นผิดโดยอัตโนมัติ เพราะบาง bundleจำเป็นและบาง ambiguityต้องทวนภาษา\n\n'
    for r in selected:
        rid=r['id'];text+='\n### ประเด็น audit ของ Case '+rid+'\n\n'+', '.join(flags[rid])+'\n'
        if rid in extra:text+='\nมีข้อความ unknown ของหัวข้อที่ goldไม่ได้ขอ:'+d.block(extra[rid]['extra_unknown'])+'\nตรวจว่า keyนี้ไม่มีใน target schema หรือมีrelationไม่ครบ ไม่ควรเหมารวมเป็นข้อมูลของผู้ใช้ขาด\n'
        if rid in bundle:text+='\nGoldที่ไม่ได้อยู่ในrequestedแต่ได้มาจากrender defaults/bundles:'+d.block(bundle[rid])+'\nประเด็นนี้ยืนยันการเลือกหัวข้อยังไม่ครบ ไม่ได้แปลว่าบริบทกฎ/ราคาที่แนบมาผิดทุกกรณี\n'
        if rid in refs:
            info=[]
            for ref in refs[rid]:
                target=d.REC[ref['reference_id']]
                info.append({**ref,'target_fields':{k:f for k,f in target['fields'].items() if k in {'topic','channel','value','purpose'}}})
            text+='\nReference IDที่แสดงกับข้อมูลปลายทางที่มีอยู่จริงในfixture:'+d.block(info)+'\nการแก้rendererควรใช้ข้อมูลปลายทางที่เกี่ยวข้อง ไม่ลบรหัสstableของข้อมูลต้นฉบับ\n'
        text+=d.case_doc(r)
    d.put('PASSED_QUALITY_AUDITS_ALL.md',text)
    metadata={'passed_cases_with_any_quality_audit':len(selected),'extra_unknown_cases':len(extra),'default_bundle_cases':len(bundle),'technical_reference_cases_including_nested':len(refs),'nested_reference_occurrences':len(nested),'nested_reference_case_count':len({x['id'] for x in nested}),'weak_field_or_broad_cases':len(weak),'not_reclassified_as_failed_automatically':True,'annotations_v2_count':len(ann)}
    d.put('PASS_AUDIT_COVERAGE_V2.json',metadata)
    print(json.dumps(metadata,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
