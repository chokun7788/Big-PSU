"""Platform-scoped offered relations, separate from supported game platforms."""
import json
from .projection import value,title

def offerings(index,game_id,requested=()):
    from .dialogue_task import platforms
    rows=[]
    for r in index.records.values():
        if r.get('kind')!='game_service' or value(r,'game_id')!=game_id or value(r,'offered') is not True:continue
        service=index.records.get(value(r,'service_id'),{})
        if service.get('kind')!='service':continue
        if requested and not set(requested)&set(platforms(index,str(value(service,'platform') or ''))):continue
        rows.append((r,service))
    return rows

def relation_projection(index,fact,question):
    from .dialogue_task import platforms
    requested=platforms(index,question);game=index.records.get(fact['record_id'],{})
    if game.get('kind')!='game' or fact['facet'] not in {'studio_services','zone'}:return None
    if fact['facet']=='zone' and not requested:return None
    refs=[];paths=[];targets={}
    def field(r,key):refs.extend(r.get('fields',{}).get(key,{}).get('evidence_refs',[]))
    field(game,'title')
    for offer,service in offerings(index,game['record_id'],requested):
        for r,key in [(offer,'game_id'),(offer,'service_id'),(offer,'offered'),(service,'name'),(service,'platform')]:field(r,key)
        if fact['facet']=='studio_services':
            targets[service['record_id']]=title(service);paths.append([game['record_id'],offer['record_id'],service['record_id']]);continue
        for zid in value(service,'studio_zone_ids') or []:
            zone=index.records.get(zid,{})
            if zone.get('kind')=='zone':
                targets[zid]=title(zone);field(service,'studio_zone_ids');field(zone,'name');paths.append([game['record_id'],offer['record_id'],service['record_id'],zid])
        for rid in value(service,'resource_ids') or []:
            resource=index.records.get(rid,{})
            if resource.get('kind')!='resource':continue
            zone=index.records.get(value(resource,'zone_id'),{})
            if zone.get('kind')!='zone':continue
            targets[zone['record_id']]=title(zone)
            for r,key in [(service,'resource_ids'),(resource,'zone_id'),(zone,'name')]:field(r,key)
            paths.append([game['record_id'],offer['record_id'],service['record_id'],rid,zone['record_id']])
    return {'fact_id':fact['id'],'facet':fact['facet'],'requested_platforms':requested,'target_ids':list(targets),'value':{l:'; '.join(t[l] for t in targets.values()) for l in ['th','en']},'source_paths':paths,'source_revisions':{rid:index.records[rid]['revision'] for path in paths for rid in path},'evidence_refs':list({json.dumps(r,sort_keys=True):r for r in refs}.values()),'supported_platforms_do_not_establish_offering':True}
