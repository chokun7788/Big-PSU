import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r31_report_path.txt').read_text().strip())
freeze={f.relative_to(p).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')}
with (r/'app_freeze_final_C.json').open('x',encoding='utf-8') as out:json.dump(freeze,out,indent=2)
replay=Path('r31_replay_B.py').read_text().replace('app_freeze_final_B.json','app_freeze_final_C.json').replace('complete_A_all_summary.json','final_B_all_summary.json').replace('final_B_all_results.jsonl','final_C_all_results.jsonl').replace('final_B_all_summary.json','final_C_all_summary.json')
# Sequential replacement above also changes the input summary; fix just its read.
replay=replay.replace("initial=json.loads((r/'final_C_all_summary.json').read_text())","initial=json.loads((r/'final_B_all_summary.json').read_text())")
replay=replay.replace("selected=(z.get('route',{}).get('category')=='competition_rules' or 'competition_' in z.get('mode','') or bool(re.search(r'cs2|counter.?strike|เคาน์|pause|timeout|หยุดเกม|เวลานอก',q+' '+normalized,re.I)))","selected=bool(re.search(r'pause|timeout|หยุดเกม|เวลานอก',q+' '+normalized,re.I))")
replay=replay.replace('r31 A unaffected by CS2 pause contract; V2 rescored separately','r31 A/B unaffected by local technical-timeout suppression; V2 rescored separately').replace('r31 B CS2/pause/competition conservative replay','r31 C local pause/timeout replay').replace('retained_A_requests','retained_previous_requests').replace('Full A sweep + conservative B replay. B was not a new execution of all 20327 inputs.','Full A sweep + conservative B competition replay + local C pause/timeout replay. C was not a new execution of all 20327 inputs.')
with Path('r31_replay_C.py').open('x',encoding='utf-8') as out:out.write(replay)
analysis=Path('r31_build_analysis_B.py').read_text().replace('final_B_all_summary.json','final_C_all_summary.json').replace('R31_B_','R31_C_').replace("reexecuted_B=summary['reexecuted_requests'],retained_A=summary['retained_A_requests']","reexecuted_C=summary['reexecuted_requests'],retained_previous=summary['retained_previous_requests']").replace('4370 competition/CS2/pause inputs replayed on B and other rows retained from complete A. B is not a new full execution.','Full A inputs plus 4370 competition/CS2/pause B replays and local C pause/timeout replays. C is not a new full execution.')
with Path('r31_build_analysis_C.py').open('x',encoding='utf-8') as out:out.write(analysis)
