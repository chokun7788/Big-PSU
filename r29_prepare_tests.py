from pathlib import Path
root=Path(__file__).parent
text=(root/'r28_unit_check.py').read_text(encoding='utf-8').replace('r28_report_path.txt','r29_report_path.txt').replace('names=[',"names=['tests.test_input_guard_context_r29_20261002',")
with (root/'r29_unit_check.py').open('x',encoding='utf-8') as f:f.write(text)
