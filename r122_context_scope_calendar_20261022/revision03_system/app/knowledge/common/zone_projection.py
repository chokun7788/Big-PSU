"""Project offering -> service -> resource -> zone using sourced FKs only."""
from dataclasses import replace
import re
from .registry import value
from .read_graph import all_of,fact,evaluate

def apply(result,need,snap,at,lang,store):
    if need.predicate!='offered_game_location' or not re.search(r'โซน|เล่นได้ที่ไหน|\bzone\b|where can.*play',need.query,re.I):return result
    art=dict(result.decision_artifact or {})
    if art.get('zone_projection') or art.get('response_type') not in {'answer','list'}:return result
    records=snap['release']['records'];obs=art.get('obligations',[])
    offerings={o.get('record_id') for o in obs if records.get(o.get('record_id'),{}).get('kind')=='game_service' and o.get('status')=='known'}
    zones={};receipts=[]
    # A source-declared venue zone is a separate, shorter proof branch. Some
    # migrated offerings have no physical resource FK yet; do not invent one.
    for gid in need.record_ids:
        game=records.get(gid,{})
        if game.get('kind')!='game':continue
        for zid in value(game,'venue_zone_ids') or []:
            if zid not in records:continue
            proof=evaluate(all_of(fact(gid,'venue_zone_ids'),fact(zid,'name')),snap,at,need.id,need.predicate)
            if proof['status']=='supported':zones[zid]=records[zid];receipts.extend(proof['receipts'])
    for rid in offerings:
        offering=records[rid]
        if value(offering,'offered') is not True:continue
        service_id=value(offering,'service_id');service=records.get(service_id)
        if not service:continue
        for resource_id in value(service,'resource_ids') or []:
            resource=records.get(resource_id)
            if not resource:continue
            zid=value(resource,'zone_id')
            if zid not in records:continue
            graph=all_of(fact(rid,'offered'),fact(rid,'service_id'),fact(service_id,'resource_ids'),fact(resource_id,'zone_id'),fact(zid,'name'))
            proof=evaluate(graph,snap,at,need.id,need.predicate)
            if proof['status']=='supported':zones[zid]=records[zid];receipts.extend(proof['receipts'])
    if not zones:return result
    from .answer import title
    from .evidence import enrich_hit
    hits=list(result.hits);body=result.answer+'\n\n'+('โซนที่ให้บริการ: ' if lang=='th' else 'Studio zone: ')
    labels=[]
    for zid,r in zones.items():
        f=r['fields']['name'];ref=f['evidence_refs'][0];src=snap['release']['sources'][ref['source_id']];marker='S'+str(len(hits)+1)
        hit={'id':zid+':name','record_id':zid,'field':'name','title':title(r,lang),'text':title(r,lang),'source_id':ref['source_id'],'snapshot_sha256':src['sha256'],'locator':ref['locator'],'citation_label':marker,'source_url':src.get('public_url') or ''}
        hits.append(enrich_hit(hit,snap,store));labels.append(title(r,lang)+' ['+marker+']')
        obs=[*obs,{'record_id':zid,'field':'name','status':'known','evidence_refs':f['evidence_refs']}]
    body+=' / '.join(labels)
    art.update(zone_projection={'zone_ids':list(zones),'receipts':receipts,'method':'source_bound_forward_relation'},obligations=obs)
    return replace(result,answer=body,hits=hits,decision_artifact=art)
