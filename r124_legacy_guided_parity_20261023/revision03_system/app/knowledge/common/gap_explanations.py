"""Known missing facts and source scope get specific terminals, not topic menus."""
import re,time
from dataclasses import replace
from .registry import value

def direct(reader,need,snap,at,lang):
    q=need.query
    if re.search(r'ข้อมูล.{0,25}(?:ไม่ได้อยู่|ไม่มี|นอก).{0,20}(?:เว็บ|ฐานข้อมูล)|\b(?:information|facts?)\b.{0,35}\b(?:not on|outside|not in)\b.{0,25}\b(?:website|database|sources?)\b',q,re.I):
        body=('แชทนี้ตอบจากข้อมูลของศูนย์ที่มีแหล่งอ้างอิงครับ สำหรับข้อมูลที่ไม่ได้อยู่ในชุดข้อมูลนี้ ยังไม่มีหลักฐานยืนยันให้ตอบได้' if lang=='th' else 'This chat answers from the studio’s sourced information. Information outside this data set is not confirmed by the available sources.')
        return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r102_source_scope_gap','bridge_status':'missing_source_scope'},[],response='unconfirmed')
    universal=bool(re.search(r'ทุกเกม|\b(?:all|every)\s+games?\b',q,re.I))
    eligibility=bool(re.search(r'คนนอก|บุคคลภายนอก|สิทธิ์|\b(?:visitors?|outsiders?|external|eligible|eligibility)\b',q,re.I))
    if not (universal and eligibility):return None
    from .claim_bindings import current_claims
    from .audience_scope import resolve
    from .registry import CATALOG
    groups,_=resolve(q,snap['release']['records']);groups=groups or []
    records=snap['release']['records'];games={k for k,r in records.items() if r['kind']=='game' and k not in snap.get('withdrawn',[])}
    mapped=current_claims(snap,at)
    declarations=[c for c in mapped if c['predicate']=='game_offerings' and isinstance(c['value'],list) and not c['condition_refs'] and not c['exception_refs'] and records.get(c['subject_ref'],{}).get('kind')=='center']
    declaration=declarations[0] if len(declarations)==1 else None
    if declaration:games=set(declaration['value'])
    claims=[c for c in mapped if c['predicate']=='game_access' and (not c['actors'] or set(c['actors'])&set(groups)) and not c['condition_refs'] and not c['exception_refs']]
    allowed={c['subject_ref'] for c in claims if c['value'] is True};denied={c['subject_ref'] for c in claims if c['value'] is False}
    # A universal positive additionally requires a declared offering universe;
    # just having game records does not prove the complete available catalog.
    offer_games={value(r,'game_id') for r in records.values() if r['kind']=='game_service' and value(r,'offered') is True}
    complete=bool(declaration and games) and all(k in records and records[k]['kind']=='game' for k in games) and offer_games==games and games<=allowed and not (games&denied)
    if complete:
        from .mapped_claims import render
        need.task='policy';need.predicate='game_access'
        from .read_graph import evaluate,fact
        proof=evaluate(fact(declaration['value_ref']['record_id'],declaration['value_ref']['field']),snap,at,need.id,'game_offerings')
        if proof['status']=='supported':
            return render(reader,need,[c for c in claims if c['subject_ref'] in games],snap,at,lang,
              scope={'scope':'all_confirmed_game_offerings','member_ids':sorted(games),'total_members':len(games),'scope_claim_id':declaration['claim_id'],
                'receipts':proof['receipts'],'release_id':snap['active'],'epoch':snap['epoch']})
    body=('ยังยืนยันไม่ได้ว่าบุคคลภายนอกเล่นได้ทุกเกมครับ ข้อมูลสิทธิ์การใช้แต่ละเกมหรือรายการเกมที่ให้บริการยังไม่ครบ จึงไม่ควรสรุปว่าใช้ได้ทั้งหมด' if lang=='th' else 'It is not confirmed that external visitors may play every game. Per-game eligibility or the complete offering scope is missing, so universal access cannot be confirmed.')
    return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r102_universal_eligibility_gap','bridge_status':'eligibility_not_complete',
      'missing_requirements':['confirmed_audience_scope','per_game_eligibility','complete_offering_scope']},[],response='unconfirmed')

def refine(result,plan,snap,lang):
    if result is None or len(plan.needs)!=1:return result
    need=plan.needs[0];art=result.decision_artifact or {};obs=art.get('obligations',[])
    if need.task=='price' and need.predicate=='current_rate' and any(o.get('field')=='validity' and o.get('status')=='unknown' for o in obs):
        ids=(art.get('query_plan') or {}).get('record_ids',[]);records=snap['release']['records']
        rates=[records[k] for k in ids if k in records and records[k]['kind']=='rate']
        if rates and all(r['validity']['state']=='unknown' for r in rates):
            body=('ยังยืนยันราคาปัจจุบันไม่ได้ครับ ข้อมูลราคาที่เกี่ยวข้องยังไม่มีช่วงวันที่มีผลที่ยืนยันแล้ว ผู้ดูแลต้องระบุวันมีผลก่อนจึงจะยืนยันอัตราที่ใช้ได้' if lang=='th' else 'The current price cannot be confirmed: the relevant rates do not have confirmed effective dates. The administrator needs to confirm their applicability first.')
            return replace(result,answer=body,hits=[],mode='pipeline:common_unconfirmed',decision_artifact={**art,'response_type':'unconfirmed','obligations':[],
              'owner_data_issues':[{'kind':'rate','field':'validity','record_ids':[r['record_id'] for r in rates],'reason':'effective_dates_unknown'}]})
    return result
