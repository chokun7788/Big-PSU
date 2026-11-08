"""Source-backed synthetic fixtures for the integrated batch. No top-level work."""
from pathlib import Path
from datetime import datetime
import dataclasses,copy,contextlib,json,urllib.request
from unittest.mock import patch

AT=datetime.fromisoformat('2026-10-20T12:00:00+07:00')
def bi(th,en):return {'th':th,'en':en}
class Fixture:
    @classmethod
    def clone(cls,path,source):
        import sqlite3
        from app.knowledge.common.store import CommonStore
        path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
        with sqlite3.connect(Path(source).resolve().as_uri()+'?immutable=1',uri=True) as a,sqlite3.connect(path) as b:a.backup(b)
        obj=cls.__new__(cls);obj.path=path;obj.store=CommonStore(path);obj.calls=[];obj.results=[];return obj
    def __init__(self,path):
        from app.knowledge.common.store import CommonStore
        self.path=Path(path);self.store=CommonStore(self.path);self.store.initialize(allow_demo=True);self.calls=[];self.results=[]
        self.active=True;self.base()
    def new(self,kind,rid,fields,aliases=None):
        from app.knowledge.common.registry import template
        r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
        r['validity']={'state':'known','effective_from':'2020-01-01T00:00:00+07:00','effective_until':'2035-01-01T00:00:00+07:00'}
        if aliases:r['aliases']={k:list(dict.fromkeys(v)) for k,v in aliases.items()}
        return self.save(r,fields,0)
    def save(self,r,fields=None,version=None,**kwargs):
        from app.knowledge.common.owner_server import save_owner_record
        r=copy.deepcopy(r)
        for k,v in (fields or {}).items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':'R102 SYNTHETIC ONLY — not studio policy'}
        return save_owner_record(self.store,r,r['revision'] if version is None else version,'r102-isolated-fixture',source_title='SYNTHETIC ACCEPTANCE ONLY',**kwargs)['record']
    def edit(self,rid,fields=None,**kwargs):return self.save(self.store.get(rid)['record'],fields,**kwargs)
    def pub(self,ids,key):
        for rid in ids:
            r=self.store.get(rid);self.store.approve(rid,r['record']['revision'],r['hash'],actor='r102-isolated-fixture')
        return self.store.publish(ids,actor='r102-isolated-fixture',expected_active=self.store.snapshot()['active'],request_key=key)
    def base(self):
        self.new('center','fx_center',{'name':bi('ศูนย์เนบิวลาทดลอง','Nebula Fixture Studio'),'operator':bi('มหาวิทยาลัยทดลอง','Fixture University'),'description':bi('ข้อมูลทดลอง CENTER_FACT','Synthetic CENTER_FACT'),'address':bi('อาคารทดลอง 5 ชั้น 1 ADDRESS_FACT','Fixture Building 5 Floor 1 ADDRESS_FACT'),'timezone':'Asia/Bangkok'})
        self.new('zone','fx_zone',{'name':bi('โซนเนบิวลา','Nebula Zone')})
        self.new('resource','fx_resource',{'name':bi('เครื่องเนบิวลา','Nebula Device'),'zone_id':'fx_zone','physical_pool_key':'FX_POOL','operational_status':'in_service'})
        self.new('audience','fx_external',{'name':bi('บุคคลภายนอก','External Visitors'),'eligibility':bi('สิทธิ์ทดลองภายนอก','Synthetic external eligibility')},{'th':['คนนอก','บุคคลภายนอก'],'en':['external visitors','visitors']})
        self.new('audience','fx_staff',{'name':bi('บุคลากร PSU','PSU Staff'),'eligibility':bi('สิทธิ์ทดลองบุคลากร','Synthetic staff eligibility')},{'th':['บุคลากร PSU'],'en':['PSU staff']})
        for rid,name,platform,minutes in [('fx_pc','PC','PC',60),('fx_vr','VR','VR',30)]:
            self.new('service',rid,{'name':bi(name,name),'platform':platform,'resource_ids':['fx_resource'],'session_minutes':minutes,'occupancy_minutes':minutes},{'th':[name],'en':[name]})
        for rid,s,a,amount in [('fx_rate','fx_pc','fx_external',10000),('fx_staff_rate','fx_pc','fx_staff',5000),('fx_vr_rate','fx_vr','fx_external',12000)]:
            self.new('rate',rid,{'service_id':s,'audience_id':a,'amount_minor':amount,'currency':'THB','unit':'per_hour','duration_minutes':60,'calculation_rule':'linear'})
        self.new('rental_package','fx_rental',{'name':bi('เหมา PC เต็มวันทดลอง','PC Full-Day Fixture Rental'),'zone_ids':['fx_zone'],'audience_id':'fx_external','period_label':'full_day','duration_minutes':480,'amount_minor':77700,'currency':'THB','terms':bi('แพ็กเกจทดลอง RENTAL_FACT','Synthetic package RENTAL_FACT')})
        self.new('schedule','fx_schedule',{'timezone':'Asia/Bangkok','zone_ids':[],'weekday':AT.weekday(),'open_periods':[{'start':'09:00','end':'18:00'}],'bookable_periods':[{'start':'09:00','end':'17:00'}],'maintenance_periods':[]})
        self.new('faq','fx_booking',{'question':bi('วิธีจอง PC ทำยังไง','How do I book PC?'),'answer':bi('จองผ่านระบบ BOOK_STEPS','Book through the reservation system BOOK_STEPS'),'topic':'booking','related_ids':['fx_pc']})
        self.new('faq','fx_refund',{'question':bi('ขอคืนเงินได้ไหม','Can I get a refund?'),'answer':bi('เงื่อนไขคืนเงินทดลอง REFUND_FACT ยกเว้นเงื่อนไขที่ระบุ','Synthetic refund policy REFUND_FACT, except the stated exception.'),'topic':'refund'})
        self.new('procedure','fx_procedure',{'name':bi('วิธีจอง','Booking procedure'),'topic':'booking','preconditions':[],
          'steps':[{'order':1,'instruction':bi('เลือกบริการ BOOK_STEPS','Choose the service BOOK_STEPS'),'contact_id':None}],'required_documents':[]})
        for rid,th,en,marker in [('fx_a','เกมเอทดลอง','Game A Fixture','GAME_A'),('fx_b','เกมบีทดลอง','Game B Fixture','GAME_B'),('fx_val','VALORANT','VALORANT','VAL_FACT'),('fx_rov','ROV','ROV','ROV_FACT'),('fx_cs','CS2','Counter-Strike 2','CS_FACT')]:
            self.new('game',rid,{'title':bi(th,en),'summary':bi('ภาพรวม '+marker,'Overview '+marker),'how_to_play':bi('วิธีเล่น '+marker+'_PLAY','Play instructions '+marker+'_PLAY'),'supported_platforms':['PC']}, {'th':[th]+(['CS2'] if rid=='fx_cs' else []),'en':[en]+(['CS2'] if rid=='fx_cs' else [])})
        self.new('game_mode','fx_mode',{'game_id':'fx_val','mode_name':bi('ทีมทดลอง','Fixture team'),'platform':'PC','players_min':2,'players_max':5})
        for gid in ['fx_a','fx_b']:
            self.new('game_service','fx_offer_'+gid,{'game_id':gid,'service_id':'fx_pc','offered':True})
        self.new('competition','fx_event',{'game_id':'fx_rov','event_name':bi('แข่ง ROV ทดลอง','ROV Fixture Tournament'),'rulebook_release':'R102_FIXTURE','coverage':'complete'})
        self.new('competition_rule','fx_rule',{'competition_id':'fx_event','section_number':'1','facet':'in_match_operations','heading':bi('เกมหลุด','Disconnection'),
          'text':bi('เกมหลุดให้แจ้งกรรมการ ห้ามเริ่มใหม่เอง ยกเว้นกรรมการอนุญาต RULE_EXCEPTION','On disconnect notify the referee. Do not restart unless the referee permits it. RULE_EXCEPTION'),'depends_on_ids':[],'completeness':'complete'})
    def binding(self,predicate,subject,rid,field,*,bid='claim_one',actors=None,services=None,unit=None,duration=None,projection='identity',path='',quote=None):
        return {'binding_id':bid,'predicate':predicate,'subject_ref':subject,'unit':unit,'actor_scope':{'status':'known','value':actors or []},
          'value_ref':{'record_id':rid,'field':field,'path':path,'projection':projection,'quote':quote},'condition_refs':[],'exception_refs':[],
          'conditions_status':'known','exceptions_status':'known','applicability':{'status':'known','service_ids':services or [],'duration_minutes':duration,'platform':None,
          'effective_from':'2020-01-01T00:00:00+07:00','effective_until':'2035-01-01T00:00:00+07:00'},
          'authority_refs':[],'dependency_refs':[],'supersedes_refs':[],'evidence_refs':[]}
    def ask(self,q,locale='en',history=None,*,llm=True,store=None):
        from app.knowledge.common.answer import CommonAnswerer
        from app.knowledge.common.snapshot_provider import DraftSnapshotView
        from app.pipeline.request_deadline import request_deadline
        from app.core.locale import resolve_locale
        from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult
        language=resolve_locale(q,requested=locale).effective
        def unavailable(q):return PipelineAnswer(answer='Live status is unavailable in the controlled fixture.',hits=[],elapsed=0,mode='pipeline:live_booking_unavailable',confidence=0,route=PipelineRoute('booking','live',0,'live_unavailable','low','synthetic provider'),entities=EntityBundle(),validation=ValidationResult(True),decision_artifact={'response_type':'live_unavailable','live_booking':{'status':'unavailable'}})
        native=urllib.request.urlopen
        def observed(req,*a,**kw):
            row={'url':getattr(req,'full_url',str(req)),'opened':False};self.calls.append(row)
            try:r=native(req,*a,**kw);row['opened']=True;return r
            except Exception as e:row['error']=type(e).__name__;raise
        with request_deadline(25),patch('urllib.request.urlopen',side_effect=observed):
            r=CommonAnswerer(store or DraftSnapshotView(self.store),external_executor=unavailable).answer(q,locale=language,history=history,at=AT,planner=(lambda *a:None) if llm else None)
        self.results.append({'question':q,'locale':locale,'effective_locale':language,'result':dataclasses.asdict(r) if r else None})
        return r
    @staticmethod
    def history(q,r):
        from app.knowledge.common.dialogue import state_from_answer
        return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
    def live(self):
        self.new('live_binding','fx_live',{'service_id':'fx_pc','provider':'wordpress_booking','external_resource_key':'FX_POOL','physical_pool_key':'FX_POOL','timezone':'Asia/Bangkok',
          'status_mapping':[{'raw':'FREE','normalized':'free'},{'raw':'BUSY','normalized':'occupied'}],
          'freshness_policy':bi('ข้อมูลทดลองอายุไม่เกิน 30 วินาที','Synthetic observed_at must be within 30 seconds'),'freshness_max_age_seconds':30})
        from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot
        return LiveBookingSnapshot(True,AT.date().isoformat(),AT.isoformat(),AT.isoformat(),'remote_csv_live',True,'fixture',(),
          (LiveResource('FX_POOL','Fixture pool',1,'FREE',1,(LiveSlot('15:00','16:00','FREE',0,0,1),)),))
