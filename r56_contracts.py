"""Frozen, source-bound requirements for the existing 156 shop cases.

Transport, mandatory content and live booking truth have separate verdicts.
This is an evaluator, not a runtime confidence score or a human approval.
"""
import json,re,ast,hashlib,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT))
from app.calculator.service_fee import SERVICE_FEES
from app.pipeline.conversation_fee import GROUP_EN
facts=json.loads((ROOT/'data/curated/user_service_facts_20261008.json').read_text(encoding='utf-8'))
catalog={}
for line in (ROOT/'data/curated/service_game_availability.jsonl').read_text(encoding='utf-8').splitlines():
    r=json.loads(line);catalog.setdefault(r['zone'],set()).update(r['games'])
pending={}
for node in ast.walk(ast.parse((ROOT/'app/pipeline/user_service_facts.py').read_text(encoding='utf-8'))):
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='pending_conditions' for t in node.targets):
        pending={x[0]:{'th':x[3],'en':x[4]} for x in ast.literal_eval(node.value)}
def norm(s):return re.sub(r'\s+','',s).casefold()
def build(c):
    i=int(c['id'][1:]);l=c['locale'];d=dict(id=c['id'],question=c['question'],locale=l,requires=[],forbids=[],fees=[],catalog=[],source_basis=[],classification='recorded_source_contract')
    def need(*v):d['requires'].extend(v)
    def claim(k):need(facts['claims'][k]['answers'][l]);d['source_basis'].append('data/curated/user_service_facts_20261008.json#'+k)
    def price(k,g='general_adult',sessions=1):
        f=SERVICE_FEES[k];d['fees'].append(dict(package=k,group=g,unit=f['prices'][g],sessions=sessions,total=f['prices'][g]*sessions,minutes=f['minutes_per_session']))
        d['source_basis'].append('app/calculator/service_fee.py#'+k+':'+g)
        need('2026-07-27' if k=='pc' else '2026-03-31')
    def games(z=None):
        d['catalog']=sorted({g for zone,gs in catalog.items() if z is None or z==zone for g in gs});d['source_basis'].append('data/curated/service_game_availability.jsonl#'+(z or 'all'))
    if c.get('claim'):claim(c['claim'])
    if i in (58,59,121,123):price('pc')
    if i in (60,61,152,153):price('pc',sessions=2);need('120','140')
    if i==64:price('nintendo_switch_3_4');need('3-4')
    if i in (65,66,106,110):
        for k in SERVICE_FEES:
            for g in ('general_student','general_adult'):price(k,g)
    if i in (104,108):
        for g in ('general_student','general_adult'):price('pc',g)
    if i==122:
        price('vr_30');price('vr_60')
    if i in (62,137):need('PC','1 แพ็กเกจ','เหลือ 30','60')
    if i in (63,138):need('PC','1 whole package','30 THB','60')
    rentals={67:['PC','4,000'],68:['PC','4,000'],69:['All Zones','6,000','12,000','50'],70:['PC','4,000','VR','1,500','Internal','External'],117:['PC','4,000'],118:['43','10'],119:['PC','4,000']}
    if i in rentals:need(*rentals[i]);d['source_basis'].append('data/curated/zone_rental_fees_20261006.json')
    if i in (67,68,69,70,117,119):need('ชั่วโมง' if l=='th' else 'hours')
    if i==71:need('ไม่ได้ระบุ' if l=='th' else 'does not','ชั่วโมง' if l=='th' else 'hours')
    if i==72:need('PS55');d['classification']='protected_unknown_device'
    if i==120:need('does not specify','booking procedure')
    if i in (73,74,111,112,152,153):games('PC Zone')
    if i in (75,76):games('Nintendo Switch Zone')
    if i==77:games('PlayStation 5 Zone')
    if i==78:games('Cockpit Zone')
    if i==79:games('VR Zone')
    if i==80:games();need('42')
    overview={81:'cs2',82:'rov',83:'tekken8',84:'valorant',87:'rov',114:'cs2',116:'tekken8',124:'rov'}
    if i in overview:d['overview_game']=overview[i];d['source_basis'].append('data/competition_rules#'+overview[i])
    if i in (85,86):d['full_rules']=True;d['source_basis'].append('data/competition_rules')
    if i==88:need('2030');d['classification']='unconfirmed_event_edition'
    live={89:[],90:[],91:['15:00'],92:['15:00'],93:['PC #01','10:00'],94:['09:00','10:00'],125:['PC #01','10:00'],126:['PC #02','10:00'],149:['09:00','10:00'],150:['09:00','10:00'],151:['PC #01','PC #02','10:00','11:00']}
    if i in live:d['classification']='live_format_only_status_truth_not_asserted';need(*live[i]);d['source_basis'].append('read-only live booking transport; no known booking oracle')
    missing={95:'technical_fault_compensation',96:'game_installation_permission',97:'game_account_policy',99:'minor_guardian_policy',100:'streaming_permission',102:'update_time_charging'}
    if i in missing:need(pending[missing[i]][l]);d['classification']='missing_owner_field';d['source_basis'].append('unanswered user service field:'+missing[i])
    if i==98:need('No separate grace period','automatically cancelled','no refund')
    if i==101:need('เปลี่ยนวันได้','เลื่อนวันแทนคืนเงินไม่ได้','ยืนยัน')
    if i in (103,105,107,109):need('PC','PlayStation','Nintendo','Cockpit','VR');d['classification']='clarification_required'
    if i in (113,115):need('Counter-Strike 2','VALORANT','RoV','Tekken');d['classification']='clarification_required'
    if i in (127,128,129,130,131,132):
        need('09:00','12:00','13:00','16:00')
        if i in (127,129,131):need('เสาร์','อาทิตย์')
        if i in (128,130):need('Saturday','Sunday')
        if i==132:need('Building')
        d['source_basis'].append('app/calendar/service_calendar.py#regular_calendar')
    if i==133:need('เลือกบริการ','วันและรอบเวลา','อีเมล','โอน','แนบสลิป','ยืนยันการจอง')
    if i==134:need('Select a service','date and time','user information','Review','bank transfer','payment slip')
    if i==135:need('Siam Commercial Bank','795-276244-1','แนบสลิป','เงินสด','ยืนยัน')
    if i==136:need('cash','not been confirmed')
    if i in (139,140):need('Left Mouse Button','R:', 'รีโหลด' if l=='th' else 'Reload','ยังไม่ได้ตรวจยืนยัน' if l=='th' else 'secondary')
    if i in (141,142):
        buttons=[json.loads(t)['button'] for t in (ROOT/'data/curated/game_control_facts.jsonl').read_text(encoding='utf-8').splitlines() if json.loads(t).get('game')=='TEKKEN 8' and json.loads(t).get('button')]
        need(*buttons,'ยังไม่ได้ตรวจยืนยัน' if l=='th' else 'secondary');d['forbids'].append('بشكل')
    if i in (143,144):need('i5-14400','32GB','5060','local' if l=='en' else 'บันทึก')
    multi={145:['membership','parking','checkin_documents'],146:['membership','parking','checkin_documents'],147:['personal_keyboard_mouse','change_machine'],148:['personal_keyboard_mouse','player_identity'],154:['player_identity'],155:['spectators'],156:['parking']}
    for k in multi.get(i,[]):claim(k)
    if i==155:need('ยังไม่ได้ระบุ' if l=='th' else 'not been confirmed')
    if i==156:need('ยังไม่ได้ระบุ' if l=='th' else 'not been specified')
    d['requires']=list(dict.fromkeys(d['requires']));d['source_basis']=list(dict.fromkeys(d['source_basis']))
    assert d['requires'] or d['catalog'] or d.get('overview_game') or d.get('full_rules') or i in live,c['id']
    return d
def evaluate(result,c):
    answer=result.get('answer','');a=norm(answer);errors=[]
    for w in c['requires']:
        if norm(w) not in a:errors.append('missing_content:'+w)
    for w in c['forbids']:
        if norm(w) in a:errors.append('forbidden_content:'+w)
    for g in c['catalog']:
        if norm(g) not in a:errors.append('missing_game:'+g)
    traces=result.get('trace') or [];metas=[x.get('metadata',{}) for x in traces]
    for m in list(metas):
        for child in (m.get('children') if isinstance(m.get('children'),list) else []):
            metas.extend([t.get('metadata',{}) for t in child.get('source_traces',[])])
    rows=[r for m in metas for r in m.get('rows',[]) if isinstance(r,dict)]
    for f in c['fees']:
        match=[r for r in rows if r.get('package_id')==f['package'] and r.get('group_id')==f['group']]
        if not match or not any((r.get('unit_price'),r.get('sessions'),r.get('total'))==(f['unit'],f['sessions'],f['total']) for r in match):errors.append('fee_binding:'+f['package']+':'+f['group'])
        if norm(f"{f['total']:,}") not in a:errors.append('fee_amount_missing:'+str(f['total']))
    if c.get('overview_game'):
        overview=[m for m in metas if c['overview_game'] in m.get('game_ids',[]) and len(m.get('section_ids',[]))>=3]
        if not overview or result.get('mode')!='pipeline:competition_rule_overview_source':errors.append('overview_section_coverage')
    if c.get('full_rules'):
        cov=result.get('rule_coverage') or {};returned=cov.get('returned_ids',[]);expected=cov.get('expected_ids',[])
        if not returned or not expected or not set(returned)<=set(expected) or len(returned)!=len(set(returned)):errors.append('full_rule_coverage_metadata')
    verdict='FAIL' if errors else 'LIVE_FORMAT_CHECKED_TRUTH_UNVERIFIED' if c['classification'].startswith('live_format') else 'CONTENT_CONTRACT_CHECKED'
    return dict(verdict=verdict,errors=errors,required_fact_count=len(c['requires'])+len(c['catalog'])+len(c['fees']),limitation='mandatory source-bound assertions only; not exhaustive semantic or owner approval')
if __name__=='__main__':
    prior=Path((BASE/'r55_current_path.txt').read_text());rows=json.loads((prior/'web_final6.json').read_text(encoding='utf-8'));contracts=[build(r['case']) for r in rows]
    for name,value in [('answer_contracts_v2.json',contracts),('offline_r55_content_audit_v2.json',[dict(id=r['case']['id'],audit=evaluate(r['job'].get('result') or {},c)) for r,c in zip(rows,contracts)])]:
        with (OUT/name).open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2)
    audits=[evaluate(r['job'].get('result') or {},c) for r,c in zip(rows,contracts)]
    print('OFFLINE existing r55.6 outputs',len(audits),'FAIL',sum(bool(a['errors']) for a in audits))
    for c,a in zip(contracts,audits):
        if a['errors']:print(c['id'],a['errors'])
