from pathlib import Path
ROOT=Path(__file__).parent
for name in ['r32_known_booking.py','r32_sessions.py']:
    s=(ROOT/name).read_text(encoding='utf-8').replace('r32_report_path.txt','r33_report_path.txt').replace('r32_full_corpus','r33_full_corpus').replace('R32_KNOWN','R33_KNOWN').replace('FINAL10_SESSION','R33_SESSION').replace('candidate6_inventory.json','candidate_D_inventory.json')
    (ROOT/name.replace('r32_','r33_')).write_text(s,encoding='utf-8')
f=ROOT/'r33_partial_http.py';s=f.read_text(encoding='utf-8').replace("ROOT.with_name(ROOT.name).joinpath('r33_report_path.txt')","ROOT/'r33_report_path.txt'")
# Keep grouping for Path arithmetic before read_text.
s=s.replace("Path(ROOT/'r33_report_path.txt'.read_text().strip())","Path((ROOT/'r33_report_path.txt').read_text().strip())")
f.write_text(s,encoding='utf-8')
f=ROOT/'r33_freeze.py';s=f.read_text(encoding='utf-8').replace('Candidate6 full corpus uses this runtime; later additions are documentation/tools/tests only unless explicitly recorded.','Full r33 candidate_D execution uses the frozen D runtime; subsequent replay/deployment must name its runtime manifest explicitly.')
f.write_text(s,encoding='utf-8')
print('created known-fixture and session runners with fresh output names')
