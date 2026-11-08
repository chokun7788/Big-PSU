"""Resolve material play/competition ambiguity and read explicit linked clauses."""
import re,time
from .registry import value
from .query_contract import normalize,strip_names
from .followup_scope import delivered_state

def answer(reader,question,snap,records,names,lang,history,at):
    from .answer import named,title
    q=normalize(question).strip(' ?!.,');state=delivered_state(history) or {};pending=state.get('r98_pending_context') or {}
    ids,_=named(question,{k:a for k,a in names.items() if k in records and records[k]['kind']=='game'},allow_fuzzy=False)
    explicit_comp=bool(re.search(r'แข่ง|กติกา|กฎ|กฏ|\b(?:competition|tournament|rulebook)\b',q))
    phase=None;parents=[]
    if pending.get('version')==1:
        prior=[k for k in pending.get('game_ids',[]) if k in records and records[k]['kind']=='game']
        if pending.get('phase')=='context' and re.fullmatch(r'แข่ง|แข่งขัน|ตอนแข่ง|กติกา|competition|tournament|during a match',q):
            ids=prior;explicit_comp=True;phase='competition'
        elif pending.get('phase')=='context' and re.fullmatch(r'เล่นทั่วไป|เล่นปกติ|ทั่วไป|general play|normal play|casual play',q):
            ids=prior;phase='general_play'
        elif pending.get('phase')=='event':
            choices={k:names.get(k,[]) for k in pending.get('competition_ids',[]) if k in records and records[k]['kind']=='competition'}
            selected,_=named(question,choices,allow_fuzzy=False)
            if len(selected)==1:parents=selected;ids=prior;explicit_comp=True;phase='competition'
        if phase and not ids:
            return reader.finish(snap,time.perf_counter(),'รายการเกมเปลี่ยนแล้ว กรุณาระบุเกมอีกครั้งครับ' if lang=='th' else 'The selected game changed. Please specify the game again.',[],{'record_ids':[],'requested_fields':[],'method':'r98_context_target_changed'},[],response='clarification')
    if not phase:
        if len(ids)!=1:return None
        residue=strip_names(question,ids,names)
        residue=re.sub(r'กติกา|กฎ|กฏ|การแข่งขัน|แข่งขัน|ตอนแข่ง|แข่ง|\b(?:tournament|competition|rulebook|rules|during a match)\b',' ',residue).strip(' ?!.,')
        if not re.fullmatch(r'(?:ถ้า)?(?:เกม)?(?:หลุด|หลุดจากเกม)(?:ต้อง)?(?:ทำยังไง|ทำอย่างไร|ทำไง)|what (?:do|should) i do (?:if|when) (?:the game|i) disconnect(?:s)?',residue):return None
        phase='competition' if explicit_comp else 'context'
    started=time.perf_counter();caption=' / '.join(title(records[k],lang) for k in ids)
    if phase=='context':
        body=('หมายถึงเกมหลุดระหว่างเล่นทั่วไป หรือระหว่างการแข่งขันของ '+caption+' ครับ?' if lang=='th' else 'Do you mean a disconnection during normal play or during a '+caption+' competition?')
        plan={'record_ids':ids,'requested_fields':[],'operation':'context','method':'r98_material_context_question','r98_pending_context':{'version':1,'phase':'context','topic':'disconnection','game_ids':ids,'options':['general_play','competition']}}
        return reader.finish(snap,started,body,[],plan,[],response='clarification')
    if phase=='general_play':
        body=('ยังไม่มีขั้นตอนที่ยืนยันได้สำหรับเกมหลุดระหว่างเล่นทั่วไปของ ' if lang=='th' else 'No source-backed normal-play disconnection procedure is recorded for ')+caption
        return reader.finish(snap,started,body,[],{'record_ids':ids,'requested_fields':[],'operation':'procedure','method':'r98_missing_normal_play_source'},[],response='unconfirmed')
    if not parents:parents=[k for k,r in records.items() if r['kind']=='competition' and value(r,'game_id') in ids]
    if len(parents)>1:
        body=('ต้องการกติกาของรายการแข่งขันใดครับ: ' if lang=='th' else 'Which tournament rulebook do you mean: ')+ ' / '.join(title(records[k],lang) for k in parents)
        plan={'record_ids':ids,'requested_fields':[],'operation':'rules','method':'r98_event_scope_question','r98_pending_context':{'version':1,'phase':'event','topic':'disconnection','game_ids':ids,'competition_ids':parents}}
        return reader.finish(snap,started,body,[],plan,[],response='clarification')
    children=[k for k,r in records.items() if r['kind']=='competition_rule' and value(r,'competition_id') in parents and re.search(r'หลุด|การเชื่อมต่อ|disconnect|reconnect|connection issue',str(value(r,'text') or {}),re.I)]
    if not children:
        return reader.finish(snap,started,('ยังไม่พบข้อกติกาที่ยืนยันกรณีเกมหลุดสำหรับ ' if lang=='th' else 'No verified disconnection clause is recorded for ')+caption,[],{'record_ids':parents or ids,'requested_fields':[],'operation':'rules','method':'r98_missing_disconnection_clause'},[],response='unconfirmed')
    plan={'record_ids':children,'scope_ids':parents,'requested_fields':['heading','text'],'operation':'rules','all_fields':False,'platform':None,'method':'r98_linked_disconnection_clauses','unresolved_clauses':[],'game_scope':ids,'semantic_plan_accepted':True,'task_plan':{'task':'competition_rules','predicate':'rule_clause'},'clause_selection':{'predicate':'explicit disconnection wording within the selected game/event','parent_ids':parents,'selected_ids':children}}
    return reader.execute_task(question,snap=snap,at=at,lang=lang,plan=plan)
