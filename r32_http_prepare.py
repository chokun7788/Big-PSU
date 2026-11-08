from pathlib import Path
ROOT=Path(__file__).parent;p=ROOT/'r32_http_B.py';s=p.read_text(encoding='utf-8');anchor="counts=collections.defaultdict(collections.Counter);start=time.perf_counter();done=0";assert anchor in s;s=s.replace(anchor,'''# Actual occupancy collection remains paused. Offline/known live-path fixtures
# are checked separately; avoid WordPress reads from HTTP regression cases.
from app.booking.live_status import is_live_booking_question
from app.pipeline.competition_targets import looks_like_competition_rule_query
skipped=[];filtered=[]
for suite,cases in tasks:
    kept=[]
    for c in cases:
        if is_live_booking_question(c['question']) and not looks_like_competition_rule_query(c['question']):
            skipped.append(dict(suite=suite,case=c,reason='real_occupancy_collection_paused; known offline fixture tested separately'))
        else:kept.append(c)
    filtered.append((suite,kept))
tasks=filtered
with (r/(run+'_http_live_deferred.json')).open('x',encoding='utf-8') as out:json.dump(skipped,out,ensure_ascii=False,indent=2)
counts=collections.defaultdict(collections.Counter);start=time.perf_counter();done=0''',1);p.write_text(s,encoding='utf-8')
print('HTTP real-occupancy reads deferred; source/content regression remains enabled')
