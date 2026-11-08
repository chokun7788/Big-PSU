"""Native schema/lifecycle acceptance beyond the retained R113 projection."""
import dataclasses,json,os,sys
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
os.environ.update(PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-20T12:00:00+07:00')
from scenario_support import Fixture,bi,AT
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.projection import compile_snapshot
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
out=R/'verification'/sys.argv[1];out.mkdir(parents=True,exist_ok=False)
f=Fixture.clone(out/'SYNTHETIC_ONLY.sqlite',R/'fixtures/BASE_SYNTHETIC.sqlite');checks=[]

def check(name,ok,detail=None):
    row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
    with (out/'CHECKS.jsonl').open('a',encoding='utf8') as h:h.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
    print(name,bool(ok),flush=True)

def ask(q,lang='en'):
    with patch('urllib.request.urlopen',side_effect=AssertionError('No model/network in deterministic native schema checks')):
        return CommonAnswerer(DraftSnapshotView(f.store)).answer(q,locale=lang,at=AT)

try:
    game=f.new('game','fx_native_nova',{'title':bi('เกมโนวาใหม่','Native Nova Game'),'summary':bi('ภาพรวม NOVA_NEW','Overview NOVA_NEW'),
      'how_to_play':bi('เล่น NOVA_PLAY','Play NOVA_PLAY'),'supported_platforms':['PC']})
    f.new('game_service','fx_native_offer',{'game_id':game['record_id'],'service_id':'fx_pc','offered':True})
    r=ask('What games are available on PC?');check('Data-only offered relation included in full PC catalog','Native Nova Game' in r.answer)
    f.store.withdraw('fx_native_offer',actor='r114-synthetic-native')
    r=ask('What games are available on PC?');check('Withdrawn offering is removed from next catalog','Native Nova Game' not in r.answer)
    r=ask('VALORANT เล่นได้กี่คน','th');check('Game mode player count read from native relation','5' in r.answer and r.validation.ok,dataclasses.asdict(r))
    p=f.new('policy','fx_native_policy',{'topic':'synthetic_borrow','subject':bi('อุปกรณ์โอไรออน','Orion Accessory'),
      'decision':'allowed','conditions_all':[{'field':'supervisor_ORION_CONDITION','operator':'eq','value':True}],
      'exceptions':bi('ห้ามช่วงซ่อม ORION_EXCEPTION','Not during maintenance ORION_EXCEPTION'),
      'details':bi('กฎทดลอง ORION_POLICY','Synthetic ORION_POLICY')})
    r=ask('May I use Orion Accessory?');check('Native conditional permission preserves condition and exception','ORION_CONDITION' in r.answer and 'ORION_EXCEPTION' in r.answer,dataclasses.asdict(r))
    unknown=f.new('policy','fx_native_incomplete',{'topic':'synthetic_incomplete','subject':bi('อุปกรณ์ค้างข้อมูล','Incomplete Accessory'),
      'decision':'allowed','details':bi('คำอนุญาตที่เงื่อนไขยังไม่ครบ','Permission with incomplete conditions')})
    r=ask('May I use Incomplete Accessory?');check('Unknown conditions cannot establish unconditional permission',r is None or r.decision_artifact.get('response_type') not in {'answer','list'})
    proc=f.new('procedure','fx_native_procedure',{'name':bi('จองบริการเซเลสท์','Celeste Booking Procedure'),'topic':'booking','preconditions':[],
      'steps':[{'order':1,'instruction':bi('เลือกบริการ CELESTE_STEP','Choose a service CELESTE_STEP'),'contact_id':None}],
      'required_documents':[]})
    r=ask('How do I follow Celeste Booking Procedure?');check('Native procedure steps read without per-record code','CELESTE_STEP' in r.answer,dataclasses.asdict(r))
    r=ask('PC price for External Visitors for 2 sessions');check('Native typed rate arithmetic','200' in r.answer,dataclasses.asdict(r))
    r=ask('PC External Visitors 45 minutes price');check('Declared linear rule computes a supported fractional hour','75' in r.answer,dataclasses.asdict(r))
    f.edit('fx_rate',{'calculation_rule':'no_extrapolation'})
    r=ask('PC External Visitors 45 minutes price');check('Undeclared fractional calculation does not borrow a full rate',r is None or r.decision_artifact.get('response_type')!='answer',dataclasses.asdict(r) if r else None)
    f.edit('fx_rate',{'calculation_rule':'linear'})
    rate=f.store.get('fx_rate')['record'];f.edit('fx_rate',{'amount_minor':14000})
    r=ask('PC price for External Visitors for 2 sessions');check('Data-only rate amount edit reaches calculator','280' in r.answer and '200' not in r.answer,dataclasses.asdict(r))
    f.edit('fx_rate',{'unit':'per_group','persons_min':1,'persons_max':4})
    r=ask('PC External Visitors price for 2 people total');check('A per-group rate is not multiplied by players','Total: 140 THB' in r.answer and '280' not in r.answer,dataclasses.asdict(r))
    f.edit('fx_rate',{'unit':'per_person'})
    r=ask('PC External Visitors price for 2 people total');check('A per-person rate scales by players','Total: 280 THB' in r.answer,dataclasses.asdict(r))
    r=ask('PC price; I am not External Visitors');check('Negated audience does not select its nested positive alias',r is None or '140 THB' not in r.answer,dataclasses.asdict(r) if r else None)
    f.new('rate','fx_short_rate',{'service_id':'fx_pc','audience_id':'fx_external','amount_minor':9000,'currency':'THB','unit':'per_person','duration_minutes':30,'calculation_rule':'linear'})
    r=ask('PC External Visitors price for 2 people total for 2 sessions, 30 minutes per session');check('Explicit per-session duration selects the matching native rate and multiplies sessions','Total: 360 THB' in r.answer,dataclasses.asdict(r))
    q='PC External Visitors price for 2 people total for 2 sessions';pending=ask(q)
    from app.knowledge.common.dialogue import state_from_answer
    history=[{'role':'user','text':q},{'role':'assistant','text':pending.answer,'common_read_state':state_from_answer(pending),'delivery_status':'server_written'}]
    f.edit('fx_short_rate',{'amount_minor':9500})
    r=CommonAnswerer(DraftSnapshotView(f.store)).answer('30 minutes',locale='en',history=history,at=AT)
    check('Trusted missing-period reply reads newly edited price, not a prior answer','Total: 380 THB' in r.answer,dataclasses.asdict(r))
    history[-1]['delivery_status']='not_delivered'
    r=CommonAnswerer(DraftSnapshotView(f.store)).answer('30 minutes',locale='en',history=history,at=AT)
    check('Undelivered financial context cannot supply service and audience',r is None or 'Total: 380 THB' not in r.answer,dataclasses.asdict(r) if r else None)
    r=ask('วันนี้เปิดไหม','th');check('Native day status returns concise date and service state','20 ตุลาคม 2569' in r.answer and 'เปิดให้บริการ' in r.answer and len(r.answer)<180,dataclasses.asdict(r))
    r=ask('วันนี้เปิดไหม; ศูนย์เนบิวลาทดลองอยู่ตรงไหน','th');check('Calendar and address keep their native readers in a compound request','20 ตุลาคม 2569' in r.answer and 'ADDRESS_FACT' in r.answer and len(r.decision_artifact.get('need_results',[]))==2,dataclasses.asdict(r))
    r=ask('Is the studio open today?','auto');check('Auto locale preserves English in native calendar adapter','20 October 2026' in r.answer and 'open' in r.answer.lower(),dataclasses.asdict(r))
    # Test cache invalidation and delivery invalidation independently. A
    # changed snapshot must not leave stale claim values in debug artifacts.
    view=DraftSnapshotView(f.store);snap=view.snapshot()
    class ChangedView:
        path=view.path
        def snapshot(self):return snap
        def still_current(self,s):return False
        def sources(self,c):return view.sources(c)
        def connect(self,**kw):return view.connect(**kw)
    r=CommonAnswerer(ChangedView()).answer('What is Native Nova Game?',locale='en',at=AT)
    check('Snapshot changed before delivery erases stale domain claims',r.decision_artifact.get('response_type')=='retry' and not r.decision_artifact.get('domain_flow',{}).get('typed_claims') and not r.hits,dataclasses.asdict(r))
except Exception as exc:
    import traceback
    check('native acceptance completed',False,{'error':repr(exc),'traceback':traceback.format_exc()})
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],
 'synthetic_only':True,'production_approvals_changed':False,'model_calls':0}
(out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary));raise SystemExit(bool(summary['failed']))
