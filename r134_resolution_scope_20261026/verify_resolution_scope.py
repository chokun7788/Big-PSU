import json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.rule_semantics import requested_topics,topic_matches
e=Engine.from_snapshot(snapshot());checks={};rows=[]
qs=[('dispute','Please check: How is dispute resolution handled in the Counter-Strike 2 tournament ruls? please.'),('settings','Please retrieve the official TEKKEN 8 rulebook evidence for in-game settings.'),('combined','Under CS2 tournamment ruls, where may Brightness, Resolution and Crosshair be changed, and are scripts or macros allowed?')]
for name,q in qs:
 a=e.answer(q,'en',allow_llm=False,understanding=propose(e.index,q));ids={c['record_id'] for c in a['claims']};rows.append({'name':name,'question':q,'result':a})
 if name=='dispute':checks['dispute_uses_protest_and_authority_sources']={f'competition_competition_rules_cs2_psu_phuket_2026_section_{n}' for n in ['057','058']}<=ids and not any(n.endswith('_045') for n in ids);checks['dispute_not_display_settings']='settings' not in requested_topics(q)
 if name=='settings':checks['settings_keep_round_timer_without_dispute']='competition_competition_rules_tekken8_psu_esports_section_004' in ids and 'competition_competition_rules_tekken8_psu_esports_section_008' not in ids
 if name=='combined':checks['display_and_macro_both_retained']={f'competition_competition_rules_cs2_psu_phuket_2026_section_{n}' for n in ['045','046']}<=ids
checks['multispace_dispute_heading_not_settings']=not topic_matches('settings','Dispute\n  Resolution')
checks['explicit_resolution_of_disputes_not_settings']='settings' not in requested_topics('resolution of disputes')
checks['screen_resolution_still_settings']='settings' in requested_topics('screen resolution')
out=R/('resolution_verification_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'rows':rows,'model_inferences':0,'source_changes':0};(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(R/'RESOLUTION_VERIFICATION_LATEST.json').write_text(json.dumps({'all_passed':report['all_passed'],'output':str(out),'checks':len(checks)},indent=2),'utf8');print(json.dumps({'checks':checks,'answers':[{'name':r['name'],'answer':r['result']['answer']} for r in rows]},ensure_ascii=False));assert report['all_passed']
