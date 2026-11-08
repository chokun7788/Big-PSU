import json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision04_system';os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse
from app.knowledge.common.domain_flow.meaning_review import review
engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot())
row=json.loads((R/'ellipsis01/trained/RESULTS.jsonl').read_text('utf8').splitlines()[1]);u=row['response']['decision_artifact']['understanding'];q=u['event']['input_question']
meaning=parse(u['event']['raw_content'],q);meaning.event['raw_content']=u['event']['raw_content'];meaning=review(q,engine.index,meaning)
result=engine.answer(q,'en',at='2026-10-21T12:00:00+07:00',allow_llm=False,understanding=meaning)
first,booking=result['needs'];periods={c['value'] for c in first['claims'] if c['facet']=='duration_minutes'}
checks={'compares_both_source_periods':periods=={'30','60'},'booking_has_source_claims':bool(booking['claims']),'booking_not_temporary_failure':booking['status'] not in {'unavailable','missing_source','missing_input'},'no_extra_model_calls':not result['model_events'],'comparison_not_summed_as_purchase':'Total:' not in first['answer'],'source_versions_disclosed':bool(booking['plan']['metadata'].get('policy_source_variants'))}
(R/'COMPARISON_VERIFICATION.json').write_text(json.dumps({'all_passed':all(checks.values()),'checks':checks,'question':q,'result':result},ensure_ascii=False,indent=2),'utf8')
print(json.dumps(checks,indent=2));assert all(checks.values())
