"""Exhaustively enumerate source-backed offering joins, never retrieval top K."""
import re,time
from .registry import value
from .query_contract import strip_names

def answer(reader,need,snap,at,lang):
    if need.task!='game_at_studio':return None
    records=snap['release']['records'];names=snap['release']['names']
    roots=[k for k in need.record_ids if k in records];games=[k for k in roots if records[k]['kind']=='game']
    q=need.query
    # Single-game location uses the normal graph; this lane proves catalog scope.
    if games and not re.search(r'ทั้งหมด|ทุกเกม|\b(?:all|list|games)\b',strip_names(q,games,names),re.I):return None
    from .answer import effective
    services={k for k in roots if records[k]['kind']=='service'}
    resources={k for k in roots if records[k]['kind']=='resource'}
    zones={k for k in roots if records[k]['kind']=='zone'}
    resources.update(k for k,r in records.items() if r['kind']=='resource' and value(r,'zone_id') in zones)
    services.update(k for k,r in records.items() if r['kind']=='service' and resources.intersection(value(r,'resource_ids') or []))
    offers=[r for r in records.values() if r['kind']=='game_service' and value(r,'offered') is True and effective(r,at,records)
        and (not services or value(r,'service_id') in services) and (not games or value(r,'game_id') in games)]
    offers=[r for r in offers if value(r,'game_id') in records and value(r,'service_id') in records and effective(records[value(r,'game_id')],at,records) and effective(records[value(r,'service_id')],at,records)]
    if not offers:return None
    gids=list(dict.fromkeys(value(r,'game_id') for r in offers))
    from .source_rows import render
    rows=[(k,['title']) for k in gids]+[(r['record_id'],['game_id','service_id','offered']) for r in offers]
    receipt={'release_id':snap['active'],'epoch':snap['epoch'],'scope':'offered_games_in_selected_snapshot','service_ids':sorted(services),'member_ids':gids,'total_members':len(gids),'returned_members':len(gids),'enumeration':'exhaustive_snapshot_scan','outside_snapshot_completeness_claimed':False}
    result=render(reader,snap,rows,lang,{'method':'r103_offering_catalog','task_plan':{'task':'game_at_studio'},'scope_receipt':receipt,'catalog_game_ids':gids},response='list',caption='เกมที่มีในข้อมูลบริการ' if lang=='th' else 'Games in the service records')
    from dataclasses import replace
    return replace(result,decision_artifact={**result.decision_artifact,'scope_receipt':receipt})
