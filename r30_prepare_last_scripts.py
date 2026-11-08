from pathlib import Path
root=Path(__file__).parent
s=(root/'r30_extra_G.py').read_text(encoding='utf-8').replace('FINAL_G_EXTRA_CORPUS','FINAL_G3_EXTRA_CORPUS')
with (root/'r30_extra_G3.py').open('x',encoding='utf-8') as f:f.write(s)
s=(root/'r30_extra_analyze_G.py').read_text(encoding='utf-8').replace('FINAL_G_EXTRA_CORPUS','FINAL_G3_EXTRA_CORPUS')
with (root/'r30_extra_analyze_G3.py').open('x',encoding='utf-8') as f:f.write(s)
s=(root/'r30_build_G3_analysis.py').read_text(encoding='utf-8')
s=s.replace('contract: FAILURE_EXAMPLES.json','contract: FINAL_G3_FAILURE_EXAMPLES.json').replace('ใน FAILURE_INVENTORY.jsonl','ใน FINAL_G3_FAILURE_INVENTORY.jsonl')
s=s.replace("'## วิธีอ่านคะแนนและเหตุผลเลือก'", "'## วิธีอ่านคะแนนและเหตุผลเลือก'")
(root/'r30_build_G3_analysis.py').write_text(s,encoding='utf-8')
