import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision04_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze=json.loads((R/'ellipsis01/RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in freeze.items())
shutil.copytree(R/'revision03_system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'));D=S/'app/knowledge/common/domain_flow'
p=D/'meaning_reader.py';x=p.read_text('utf8');needle="    # Keep financial calculations, policies, live providers and rule dependency"
code="""    if cat=='C06' and meaning.operation=='compare' and facet=='duration_minutes':
        from .financial import rate_pool
        from .scope import requested_minutes
        durations=[c['quote'] for c in meaning.constraints if c['slot']=='duration']
        options={requested_minutes(execution_query(index,s,meaning)):s for s in durations}
        options.pop(None,None)
        if len(options)>=2 and not re.search(r'\\d+\\s*(?:คน|people|persons?|players?|sessions?|รอบ)',question,re.I):
            scope=question
            for text in durations:scope=scope.replace(text,' ')
            fs=[f for f in rate_pool(index,scope) if value(index.records.get(f['record_id'],{}),'duration_minutes') in options and f['facet'] in {'duration_minutes','amount'}]
            if fs:
                result=confirmed(cat,fs,'source_rate_duration_comparison',operator='compare',
                    comparison_options={f['id']:execution_query(index,options[value(index.records[f['record_id']],'duration_minutes')],meaning) for f in fs},
                    comparison_scope='recorded_duration_and_rate_only')
                missing=set(options)-{value(index.records[f['record_id']],'duration_minutes') for f in fs}
                if missing:result.status='partial';result.metadata['unanswered_comparison_minutes']=sorted(missing)
                result.locked=True;return result
"""
assert needle in x;x=x.replace(needle,code+needle);ast.parse(x);p.write_text(x,'utf8')
p=D/'engine.py';x=p.read_text('utf8').replace("calc=unit_calculation(self.index,f,question)","calc=unit_calculation(self.index,f,plan.metadata.get('comparison_options',{}).get(f['id'],question))")
x=x.replace("if computations and (billing or people and len(computations)==1):","if not plan.metadata.get('comparison_options') and computations and (billing or people and len(computations)==1):")
needle="        if plan.metadata.get('calendar_source_limits'):"
code="""        if plan.metadata.get('comparison_options'):
            blocks.insert(0,'เปรียบเทียบเฉพาะระยะเวลาและอัตราที่บันทึกไว้ แต่ละบรรทัดเป็นทางเลือก ไม่ใช่ยอดรวมทุกทางเลือก' if lang=='th' else 'Comparison of recorded durations and rates only. Each line is an alternative, not a combined total.')
            if plan.metadata.get('unanswered_comparison_minutes'):
                blocks.append(('ยังไม่มีอัตราที่ตรงสำหรับนาที: ' if lang=='th' else 'No exact recorded rate for minutes: ')+', '.join(map(str,plan.metadata['unanswered_comparison_minutes'])))
        if plan.metadata.get('policy_source_variants'):
            blocks.insert(0,'พบข้อความขั้นตอนการจองหลายฉบับ ด้านล่างคงข้อความแต่ละฉบับไว้ ยังไม่ได้รวมเป็นนโยบายฉบับเดียว' if lang=='th' else 'Multiple recorded versions of the booking steps follow. They are retained separately rather than merged into a single policy.')
"""
assert needle in x;x=x.replace(needle,code+needle);ast.parse(x);p.write_text(x,'utf8')
p=D/'readers.py';x=p.read_text('utf8');needle="    # Quantified/extra predicates must have evidence of their own."
code="""    if cat=='C08' and len(intents)==1 and names=={'booking_steps'} and candidates:
        # Present source variants explicitly. Do not ask the selector to choose
        # an authority among same-action procedure versions or silently merge.
        variants={}
        for f in candidates:variants.setdefault(norm(f['value'].get('th') or f['value'].get('en')),f)
        result=confirmed(cat,list(variants.values()),'recorded_booking_procedure_variants',policy_intents=['booking_steps'],policy_source_variants=True)
        result.status='partial';result.locked=True;return result
"""
assert needle in x;x=x.replace(needle,code+needle);ast.parse(x);p.write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in freeze.items())
x=(R/'serve_candidate03.py').read_text('utf8').replace('revision03_system','revision04_system');(R/'serve_candidate04.py').write_text(x,'utf8')
(R/'REVISION04_BUILD.json').write_text(json.dumps({'parent':'R122 revision03','parent_frozen_unchanged':True,'data_unchanged':sha(S/'data/knowledge/common.sqlite')==sha(R/'revision03_system/data/knowledge/common.sqlite'),'changes':['source duration comparison reads every explicit option without combining alternatives','booking source variants presented separately without spending model budget'],'production_installed':False},indent=2),'utf8')
print('Revision04 built; source data, approvals and prior measurements unchanged')
