"""A game per match and a round per game are different source quantities."""
import json,time,copy
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.rule_semantics import requested_topics,select_topics
e=Engine.from_snapshot(snapshot());checks={};rows=[]
for label,q,locale in [('games','How many games are played in a Tekken 8 match?','en'),('thai_games','Tekken 8 แข่งกี่เกมต่อแมตช์','th'),('rounds','How many rounds per game are used in a Tekken 8 match?','en')]:
 u=Understanding([MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause')],True,'controlled_format_quantity',{'model_called':False});r=e.answer(q,locale,at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);rows.append({'q':q,'result':r});checks[label+'_uses_complete_source_clause']=bool(r['claims']) and any('FT2' in c['value'] and 'R3' in c['value'] for c in r['claims']) and all(not n['execution_contract']['fatal'] for n in r['needs'])
fragment=next(f for f in e.index.bycat['C13'] if 'R3' in ' '.join(f['value'].values()) and 'FT2' not in ' '.join(f['value'].values()))
checks['rounds_only_fragment_cannot_answer_games_per_match']=not select_topics(e.index,'How many games are played in a match?',[fragment])['facts']
checks['catalog_quantity_not_competition_format']='format' not in requested_topics('How many games are available on PC?')
checks['player_quantity_not_games_per_match']='format' not in requested_topics('How many players are in a team?')
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'real_source_changes':0,'saved_measurement_regraded':False};out=R/('format_quantity_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
