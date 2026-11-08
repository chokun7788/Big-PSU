"""The server-owned history boundary, shared with offline input reconstruction."""
import copy

def history_from_record(record,session_id,fallback=None):
    own=record['history']
    if own:
        result=copy.deepcopy(own[-16:])
        deliveries={t['response'].get('request_id'):t['delivery'] for t in record['turns'].values() if t['response']}
        refs={t['response'].get('request_id'):{'session_id':session_id,'turn_id':tid,'response_id':t['response'].get('request_id'),'origin':'server_session_store'} for tid,t in record['turns'].items() if t['response']}
        for item in result:
            if item.get('role')=='assistant':
                item['delivery_status']=deliveries.get(item.get('request_id'),'uncertain')
                item.pop('_server_history_ref',None)
                if item.get('request_id') in refs:item['_server_history_ref']={**refs[item['request_id']],'delivery_status':item['delivery_status']}
        return result
    if not isinstance(fallback,list):return []
    result=copy.deepcopy([r for r in fallback[-10:] if isinstance(r,dict) and r.get('role') in {'user','assistant'} and isinstance(r.get('text'),str) and len(r['text'])<=16000])
    for item in result:
        item['delivery_status']='uncertain'
        item.pop('_server_history_ref',None)
    return result
