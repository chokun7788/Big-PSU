from pathlib import Path
import runpy
HERE=Path(__file__).parent.resolve()
s=(HERE/'finalize_artifacts.py').read_text(encoding='utf-8')
s=s[:s.index('# Keep the new functional')] + s[s.index("notes='''"):]
for old,new in [('release_r38_3','release_r38_4'),('r38.3','r38.4'),('r38_3.zip','r38_4.zip'),('changed_paths.txt','changed_paths_r38_4.txt'),('added_paths.txt','added_paths_r38_4.txt'),('after_manifest.json','after_manifest_r38_4.json'),('archive_verification.json','archive_verification_r38_4.json'),('21 test methods','23 test methods')]:
    s=s.replace(old,new)
finalizer=HERE/'finalize_r38_4.py'
with finalizer.open('x',encoding='utf-8') as f:f.write(s)
runpy.run_path(str(finalizer),run_name='__main__')
h=(HERE/'extracted_holdout_check.py').read_text(encoding='utf-8')
h=h.replace('psu_r38_archive_check_20261005','psu_r38_4_archive_check_20261005').replace('r38_3.zip','r38_4.zip').replace('extracted_holdout_results.json','extracted_holdout_results_r38_4.json')
h=h.replace(" ('en','the Nintendo Switch option thanks',['nintendo_switch'],4),", " ('en','the Nintendo Switch option thanks',['nintendo_switch'],4),\n ('en','Give me every service rate',['pc','ps5','nintendo_switch','cockpit','vr'],14),\n ('th','ราคา PC สำหรับบุคคลทั่วไป',['pc'],1),")
holdout=HERE/'extracted_holdout_check_r38_4.py'
with holdout.open('x',encoding='utf-8') as f:f.write(h)
runpy.run_path(str(holdout),run_name='__main__')
