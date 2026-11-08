"""Research checks for this generated schema subset, not a general JSON Schema implementation.
Production must use a maintained Draft 2020-12 validator plus semantic checks.
"""
import json,re,hashlib,copy,argparse
from datetime import datetime,date
from pathlib import Path
OUT=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
CAT={c['kind']:c for c in json.loads((OUT/'FIELD_CATALOG.json').read_text(encoding='utf-8'))}
TYPES={'string':str,'integer':int,'boolean':bool,'object':dict,'array':list,'null':type(None)}
SUPPORTED={'$schema','title','description','type','const','enum','properties','required','additionalProperties','items','minimum','maximum','minLength','minItems','maxItems','uniqueItems','pattern','format','oneOf','anyOf'}
def check(value,s,path='$'):
    errors=[]
    unsupported=set(s)-SUPPORTED
    if unsupported: raise RuntimeError('Unsupported schema keywords: '+str(unsupported))
    if 'oneOf' in s and sum(not check(value,x,path) for x in s['oneOf'])!=1:errors.append(path+': oneOf')
    if 'anyOf' in s and not any(not check(value,x,path) for x in s['anyOf']):errors.append(path+': anyOf')
    if 'type' in s:
        allowed=s['type'] if isinstance(s['type'],list) else [s['type']]
        if type(value) not in [TYPES[x] for x in allowed]:return errors+[path+': type']
    if 'const' in s and value!=s['const']:errors.append(path+': const')
    if 'enum' in s and value not in s['enum']:errors.append(path+': enum')
    if isinstance(value,dict):
        for key in s.get('required',[]):
            if key not in value:errors.append(path+': missing '+key)
        if s.get('additionalProperties') is False:
            errors.extend(path+': extra '+k for k in value.keys()-s.get('properties',{}).keys())
        for key,sub in s.get('properties',{}).items():
            if key in value:errors+=check(value[key],sub,path+'/'+key)
    if isinstance(value,list):
        if len(value)<s.get('minItems',0) or len(value)>s.get('maxItems',float('inf')):errors.append(path+': item count')
        if s.get('uniqueItems') and len({json.dumps(x,sort_keys=True) for x in value})!=len(value):errors.append(path+': duplicates')
        if 'items' in s:
            for i,x in enumerate(value):errors+=check(x,s['items'],path+'/'+str(i))
    if type(value) is int and (value<s.get('minimum',float('-inf')) or value>s.get('maximum',float('inf'))):errors.append(path+': bounds')
    if isinstance(value,str):
        if len(value)<s.get('minLength',0):errors.append(path+': length')
        if 'pattern' in s and not re.search(s['pattern'],value):errors.append(path+': pattern')
        if s.get('format') in ('date','date-time'):
            try:
                parsed=date.fromisoformat(value) if s['format']=='date' else datetime.fromisoformat(value.replace('Z','+00:00'))
                if s['format']=='date-time' and parsed.tzinfo is None:raise ValueError('timezone missing')
            except ValueError:errors.append(path+': date format/timezone')
    return errors
def scalar(r,k):
    f=r['fields'].get(k,{});return f.get('value') if f.get('status')=='known' else None
def revision_hash(r):
    relevant={k:v for k,v in r.items() if k not in ('review','lifecycle','localization')}
    return hashlib.sha256(json.dumps(relevant,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def validate_bundle(bundle,root=ROOT):
    errors=[];ids={};sources={}
    for s in bundle['sources']:
        shape_errors=check(s,json.loads((OUT/'schemas/source.schema.json').read_text(encoding='utf-8')))
        if shape_errors:errors+=shape_errors;continue
        if s['source_id'] in sources:errors.append('duplicate source ID')
        sources[s['source_id']]=s
        p=(root/s['path']).resolve()
        if not p.is_relative_to(root.resolve()):errors.append('source path escapes approved root');continue
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=s['sha256']:errors.append('source hash mismatch')
    for r in bundle['records']:
        if not isinstance(r,dict) or r.get('kind') not in CAT:errors.append('unsupported kind');continue
        shape_errors=check(r,json.loads((OUT/f"schemas/{r['kind']}.schema.json").read_text(encoding='utf-8')))
        if shape_errors:errors+=shape_errors;continue
        if r['record_id'] in ids:errors.append('duplicate record ID')
        ids[r['record_id']]=r
    if errors:return errors
    for r in bundle['records']:
        kind=r['kind']
        for f in CAT[kind]['fields']:
            field=r['fields'][f['key']]
            for ref in field['evidence_refs']:
                src=sources.get(ref['source_id'])
                if src is None:errors.append('missing source reference')
                elif kind not in src['authority_for']:errors.append('source outside registered authority')
            if field['status']=='known' and f['reference_kind']:
                values=field['value'] if isinstance(field['value'],list) else [field['value']]
                for target in values:
                    rr=ids.get(target)
                    if rr is None:errors.append('missing record reference')
                    elif f['reference_kind']!='*' and rr['kind']!=f['reference_kind']:errors.append('wrong reference kind')
        v=r['validity'];a=v['effective_from'];b=v['effective_until']
        if v['state']=='unknown' and (a is not None or b is not None):errors.append('unknown validity with asserted date')
        if a and b and datetime.fromisoformat(a)>=datetime.fromisoformat(b):errors.append('inverted validity')
        for mn,mx in [('capacity_min','capacity_max'),('persons_min','persons_max'),('players_min','players_max')]:
            if scalar(r,mn) is not None and scalar(r,mx) is not None and scalar(r,mn)>scalar(r,mx):errors.append('inverted capacity')
        for name in ('open_periods','bookable_periods','maintenance_periods'):
            periods=scalar(r,name)
            if periods is None:continue
            intervals=sorted((p['start'],p['end']) for p in periods)
            if any(x>=y for x,y in intervals) or any(intervals[i][1]>intervals[i+1][0] for i in range(len(intervals)-1)):errors.append('invalid or overlapping periods')
        if kind=='schedule' and scalar(r,'bookable_periods') is not None:
            for p in scalar(r,'bookable_periods'):
                if not any(o['start']<=p['start'] and p['end']<=o['end'] for o in scalar(r,'open_periods') or []):errors.append('bookable outside open hours')
                if any(p['start']<m['end'] and m['start']<p['end'] for m in scalar(r,'maintenance_periods') or []):errors.append('bookable overlaps maintenance')
        if kind=='closure' and scalar(r,'state')=='closed' and (scalar(r,'open_periods') or scalar(r,'bookable_periods')):errors.append('closed with open/bookable periods')
        if kind=='service' and scalar(r,'occupancy_minutes') is not None and scalar(r,'session_minutes') is not None and scalar(r,'occupancy_minutes')<scalar(r,'session_minutes'):errors.append('occupancy shorter than session')
        if r['localization']['en_status']=='reviewed' and r['localization']['source_revision_hash']!=revision_hash(r):errors.append('stale translation binding')
        if r['lifecycle'] in ('approved','published'):
            rev=r['review']
            if not rev['actor_id'] or not rev['reviewed_at'] or rev['revision_sha256']!=revision_hash(r):errors.append('missing or stale review')
            for f in CAT[kind]['fields']:
                field=r['fields'][f['key']]
                if f['publish_core'] and (field['status']!='known' or field['value']==[]):errors.append('publish core incomplete')
            if any(x['status']=='conflicted' for x in r['fields'].values()):errors.append('unresolved conflict at publication')
    return errors
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle',type=Path,help='Validate a custom research bundle without publishing or running the chatbot.')
    parser.add_argument('--source-root',type=Path,default=ROOT,help='Root against which immutable source paths resolve.')
    args=parser.parse_args()
    if args.bundle:
        b=json.loads(args.bundle.read_text(encoding='utf-8-sig'))
        if not isinstance(b,dict) or b.get('schema_version')!='studio-content-3.0-design' or not isinstance(b.get('records'),list) or not isinstance(b.get('sources'),list):
            print(json.dumps({'valid':False,'errors':['bundle envelope requires schema_version, records[], sources[]']}));raise SystemExit(2)
        errs=validate_bundle(b,root=args.source_root)
        missing={} if errs else {r['record_id']:[f['key'] for f in CAT[r['kind']]['fields'] if f['publish_core'] and r['fields'][f['key']]['status']!='known'] for r in b['records']}
        print(json.dumps({'valid_research_draft_structure':not errs,'errors':errs,'unknown_publish_core_fields':missing,'scope':'Research-only subset and selected semantic checks; not approval, factual certification, or chatbot integration.'},ensure_ascii=False,indent=2))
        raise SystemExit(0 if not errs else 2)
    results=[]
    for path in sorted((OUT/'templates').glob('*.json')):
        r=json.loads(path.read_text(encoding='utf-8'));errs=check(r,json.loads((OUT/f"schemas/{r['kind']}.schema.json").read_text(encoding='utf-8')))
        results.append({'name':'draft template '+r['kind'],'expected':'valid draft','passed':not errs,'errors':errs})
    original=json.loads((OUT/'examples/actual_source_drafts.bundle.json').read_text(encoding='utf-8'))
    results.append({'name':'6 actual source drafts + references + source bytes','passed':not validate_bundle(original),'errors':validate_bundle(original)})
    def bad(name,mutate):
        b=copy.deepcopy(original);mutate(b);errs=validate_bundle(b)
        results.append({'name':name,'expected':'reject','passed':bool(errs),'errors':errs})
    bad('unknown cannot carry zero',lambda b:b['records'][5]['fields']['duration_minutes'].update(value=0))
    bad('known amount cannot be string',lambda b:b['records'][5]['fields']['amount_minor'].update(value='4000'))
    bad('negative price',lambda b:b['records'][5]['fields']['amount_minor'].update(value=-1))
    bad('missing field',lambda b:b['records'][1]['fields'].pop('genre'))
    bad('extra undeclared field',lambda b:b['records'][1]['fields'].update(secret_override=True))
    bad('unknown enum kind',lambda b:b['records'][1].update(kind='free_general_knowledge'))
    bad('missing source reference',lambda b:b['records'][1]['fields']['title']['evidence_refs'][0].update(source_id='missing'))
    bad('source authority mismatch',lambda b:b['sources'][0].update(authority_for=['game']))
    bad('source snapshot mismatch',lambda b:b['sources'][0].update(sha256='0'*64))
    bad('duplicate record ID',lambda b:b['records'].append(copy.deepcopy(b['records'][0])))
    bad('orphan zone ID',lambda b:b['records'][5]['fields']['zone_ids'].update(value=['zone_missing']))
    bad('wrong reference kind',lambda b:b['records'][5]['fields']['zone_ids'].update(value=['game_valorant']))
    bad('publication without approval',lambda b:b['records'][5].update(lifecycle='published'))
    bad('translation review without binding',lambda b:b['records'][1]['localization'].update(en_status='reviewed',source_revision_hash='0'*64))
    bad('validity is not automatic infinity',lambda b:b['records'][5]['validity'].update(state='unknown',effective_from='2026-10-10T00:00:00+07:00'))
    bad('end before start',lambda b:b['records'][5]['validity'].update(state='known',effective_from='2026-10-10T00:00:00+07:00',effective_until='2026-01-01T00:00:00+07:00'))
    bad('localization source language typo',lambda b:b['records'][1]['localization'].update(source_language='thaiii'))
    # Shape edge cases from the same field schema, without pretending they test real schedules.
    period_schema=json.loads((OUT/'schemas/schedule.schema.json').read_text(encoding='utf-8'))['properties']['fields']['properties']['bookable_periods']
    for text in ('24:00','9:00','12:60'):
        field={'status':'known','value':[{'start':text,'end':'16:00'}],'evidence_refs':[{'source_id':'fixture','locator':'synthetic'}],'note':''}
        results.append({'name':'reject invalid time '+text,'expected':'reject','passed':bool(check(field,period_schema))})
    report={'scope':'Research-only schema subset validator and selected semantic checks; no LLM/web/API integration test; no general JSON Schema conformance certification. Sources/hash prove bytes, not truth or approval.','total':len(results),'passed':sum(x['passed'] for x in results),'results':results}
    (OUT/'VALIDATION_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='results'},ensure_ascii=False))
    raise SystemExit(0 if all(x['passed'] for x in results) else 1)
if __name__=='__main__':main()
