"""Resolve observed field-projection false gaps without weakening set checks."""
import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision03_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
runs=[p for p in sorted(R.glob('verification_*/VERIFICATION.json')) if json.loads(p.read_text('utf8'))['all_passed']]
parent=next(p for p in reversed(runs) if any('/revision02_system/' in name.replace('\\','/') for name in json.loads((p.parent/'RUN_FREEZE.json').read_text('utf8'))))
freeze=json.loads((parent.parent/'RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in freeze.items())
shutil.copytree(R/'revision02_system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'));D=S/'app/knowledge/common/domain_flow'
p=D/'capabilities.py';x=p.read_text('utf8');needle="    if category=='C04' and operation=='group_list' and facet=='zone':allowed=True"
x=x.replace(needle,needle+"\n    if category=='C03' and operation=='count' and allowed:canonical='field_lookup'");ast.parse(x);p.write_text(x,'utf8')
p=D/'plan_contract.py';x=p.read_text('utf8').replace("if meaning.operation in {'list','count','group_count','group_list'}:","if task.capability['operation'] in {'list','count','group_count','group_list'}:");ast.parse(x);p.write_text(x,'utf8')
p=D/'obligation_verifier.py';x=p.read_text('utf8');needle="            if task.category=='C11' and obligation.expected in {'open_periods','bookable_periods','maintenance_periods'}:acceptable.add('service_periods')"
code="""
            if task.category=='C05' and obligation.expected=='input_bindings':
                from .precision import controls
                source_projection=controls(index,question)
                if source_projection and set(c['fact_id'] for c in claims)<=set(source_projection.ids):
                    acceptable.update(c['facet'] for c in claims if c['facet'].startswith('binding_'))
            if task.category=='C01' and obligation.expected=='value' and metadata.get('matched_profile_fact_ids'):
                from .legacy_profile import plan as source_profile
                matched=source_profile(index,task.category,question)
                if matched and set(c['fact_id'] for c in claims)<=set(matched.ids):acceptable.add('owner_policy')
"""
assert needle in x;x=x.replace(needle,needle+code);ast.parse(x);p.write_text(x,'utf8')
x=(R/'verify_foundation02.py').read_text('utf8').replace('revision02_system','revision03_system')
needle=" write('RETAINED_API_PROPOSAL_REPLAY.json',api_replays)"
code="""
 checks['button_projection_not_false_gap']=replays[3]['result']['status']=='answer'
 checks['legacy_value_profile_not_false_gap']=all(replays[i]['result']['status']=='answer' for i in [5,19])
 checks['count_of_capacity_is_field_scope']=all(not any(o['kind']=='collection_scope' for o in t['obligations']) for row in compiled_labels for t in row['plan']['tasks'] if t['category']=='C03' and t['operation']=='count')
 checks['unproven_equipment_list_remains_partial']=api_replays[1]['result']['status']=='partial'
 checks['no_source_fatal_on_retained_proposals']=not any(t.get('fatal') for row in replays+api_replays for t in row['result'].get('execution_contract',{}).get('tasks',[]))
"""
assert needle in x;x=x.replace(needle,needle+code);ast.parse(x);(R/'verify_foundation03.py').write_text(x,'utf8')
x=(R/'verify_packaging.py').read_text('utf8').replace('revision02_system','revision03_system');(R/'verify_packaging03.py').write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in freeze.items())
(R/'REVISION03_BUILD.json').write_text(json.dumps({'parent_verification':str(parent),'parent_frozen_unchanged':True,'changes':['input_bindings maps to independently matched native binding projections','C01 value maps to independently matched declared FAQ profiles','count of an explicit capacity/quantity field is not collection enumeration'],'production_installed':False},indent=2),'utf8')
print('Revision03 built; observed projection gaps addressed through source adapters')
