import sys,json,sqlite3,zlib
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
s=CommonStore(B/'common.sqlite')
with s.connect() as c:
 rs=s.heads(c);sources=s.sources(c)
 for rid in ['competition_competition_rules_cs2_psu_phuket_2026','competition_competition_rules_cs2_psu_phuket_2026_section_053']:
  r=rs[rid];print('RECORD',json.dumps(r,ensure_ascii=False))
  sid=r['fields']['rulebook_release' if r['kind']=='competition' else 'text']['evidence_refs'][0]['source_id'];print('SOURCE',sources[sid][1][:15000])
c=sqlite3.connect((B.parent/'r65_detailed_failure_analysis_20261014/evidence.sqlite').as_uri()+'?mode=ro',uri=True)
print('BASELINE_SCHEMA',c.execute('PRAGMA table_info(results)').fetchall());print('BASELINE_ARMS',c.execute('SELECT DISTINCT arm FROM results').fetchall())
