from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
relative='app/pipeline/competition_taxonomy.py';dest=report/'before'/relative;dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open('xb') as f:f.write((project/relative).read_bytes())
