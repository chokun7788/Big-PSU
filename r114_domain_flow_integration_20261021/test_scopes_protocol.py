"""Independent synthetic source cases for scope and parser invariants."""
import json,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.model import parse_items,EvidenceSelector
from app.knowledge.common.domain_flow.contracts import RequestBudget
from app.knowledge.common.domain_flow.scope import contains,requested_years
from app.knowledge.common.domain_flow.routing import route,split_needs

def fact(cat,rid,facet,subject,label,val,**extra):
    return {'id':f'{cat}:{rid}:{facet}','category':cat,'record_id':rid,'facet':facet,'subject':{'th':subject,'en':subject},
      'label':{'th':label,'en':label},'value':{'th':val,'en':val},'aliases':[],'evidence_refs':[{'source_id':'synthetic','locator':'/'+rid+'/'+facet}],'fixture':True,**extra}

class ScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fs=[fact('C12','pc1','live_status','PC1 / 2026-10-21 09:00','live availability','Available',provider_state='available'),
          fact('C12','pc10','live_status','PC10 / 2026-10-21 09:00','live availability','Booked',provider_state='booked'),
          fact('C06','aurora','amount','Aurora / Student','price','70',numeric=70,confirmation_ref='owner-current'),
          fact('C13','aurora_rule','rule_clause','Aurora 2026 Tournament','1.2 Maps','Map Aurora'),
          fact('C08','extend','owner_policy','extend session','conditions','Book next if available'),
          fact('C09','over','owner_policy','overpayment','conditions','Credit for future session'),
          fact('C09','under','owner_policy','underpayment additional slip','conditions','Send additional slip'),
          fact('C03','aurora_pad','controllers','Aurora Pad','controllers per console','3',numeric=3)]
        cls.engine=Engine({'facts':cls.fs,'records':{}})
    def answer(self,cat,q):return self.engine.answer(q,'en',category=cat,at='2026-10-21T12:00:00+07:00',allow_llm=False)
    def test_numeric_name_boundary(self):
        self.assertFalse(contains('PC10','PC1'));self.assertTrue(contains('PC1 ว่างไหม','PC1'))
    def test_unknown_resource_has_no_claim(self):
        r=self.answer('C12','PC99 / 2026-10-21 09:00 available?');self.assertEqual(r['claims'],[])
    def test_resource_slot_exact(self):
        r=self.answer('C12','PC10 / 2026-10-21 09:00 available?');self.assertEqual(r['claims'][0]['record_id'],'pc10')
    def test_resource_time_never_nearest(self):
        r=self.answer('C12','PC1 / 2026-10-21 14:00 available?');self.assertEqual(r['claims'],[])
    def test_resource_without_time_needs_input(self):self.assertEqual(self.answer('C12','PC1 available?')['status'],'missing_input')
    def test_space_and_buddhist_year(self):self.assertEqual(requested_years('ราคาในปี ๒๕๗๑'),{2028})
    def test_future_price_no_current_rate(self):
        r=self.answer('C06','ราคา Aurora / Student ในปี 2028');self.assertEqual(r['status'],'not_current');self.assertEqual(r['claims'],[])
    def test_future_rule_no_current_map(self):
        r=self.answer('C13','Aurora 2028 Tournament maps');self.assertEqual(r['claims'],[])
    def test_same_event_clause(self):
        r=self.answer('C13','Aurora 2026 Tournament 1.2 Maps');self.assertEqual(r['status'],'answer')
    def test_policy_action_separates_delta(self):
        r=self.answer('C09','โอนขาดไป ต้องส่งสลิปเพิ่มยังไง');self.assertEqual([c['record_id'] for c in r['claims']],['under'])
    def test_unknown_expiry_not_borrow_credit_policy(self):
        self.assertEqual(self.answer('C09','เครดิตเงินโอนเกินหมดอายุแน่นอนกี่วัน')['claims'],[])
    def test_unbound_entity_cannot_offer_the_entire_domain_to_model(self):
        def forbidden(_):raise AssertionError('Model must not see unrelated entities')
        e=Engine({'facts':self.fs,'records':{}},selector=EvidenceSelector(transport=forbidden))
        r=e.answer('What is the quantity of my unknown personal device?','en',category='C03',allow_llm=True)
        self.assertEqual(r['claims'],[]);self.assertEqual(r['model_events'],[])
    def test_multi_need_keeps_both_and_citations(self):
        r=self.engine.answer('Aurora Pad กี่จอย แล้วขอกำลังเล่นอยากต่อเวลา','th',at='2026-10-21T12:00:00+07:00',allow_llm=False)
        self.assertEqual({c['record_id'] for c in r['claims']},{'aurora_pad','extend'});self.assertIn('[S2]',r['answer'])
    def test_price_arithmetic(self):
        r=self.answer('C06','ราคา Aurora / Student รวม 3 รอบ');self.assertEqual(r['claims'][0]['numeric'],210)
    def test_invalid_price_counts_are_not_silently_rounded(self):
        for count in ['0','-2','1.5']:
            with self.subTest(count=count):
                r=self.answer('C06',f'Aurora / Student price for {count} people')
                self.assertEqual(r['claims'],[]);self.assertEqual(r['status'],'missing_input')
    def test_qualifier_after_separator_remains_with_price(self):
        self.assertEqual(split_needs('PC price; I am not External Visitors'),['PC price I am not External Visitors'])
        self.assertEqual(len(split_needs('PC price; what games are available?')),2)
    def test_game_edition_year_is_not_tournament_year(self):
        from app.knowledge.common.domain_flow.scope import event_years
        records={'synthetic_year_game':{'record_id':'synthetic_year_game','kind':'game','aliases':{},'fields':{'title':{'status':'known','value':{'th':'F1 2023','en':'F1 2023'}}}}}
        index=Engine({'facts':self.fs,'records':records}).index
        self.assertEqual(event_years(index,'F1 2023 Tournament 2026'),{2026})
    def test_rule_dependency_chain_is_complete_and_event_bound(self):
        fs=[fact('C13','r1','rule_clause','Aurora 2026 Tournament','1.2 Maps','First',event_id='event1',depends_on_ids=['r2']),
            fact('C13','r2','rule_clause','Aurora 2026 Tournament','2.1 Conditions','Second',event_id='event1',depends_on_ids=['r3']),
            fact('C13','r3','rule_clause','Aurora 2026 Tournament','3.1 Exception','Third',event_id='event1')]
        e=Engine({'facts':fs,'records':{}})
        r=e.answer('Aurora 2026 Tournament 1.2 Maps','en',category='C13',allow_llm=False)
        self.assertEqual({c['record_id'] for c in r['claims']},{'r1','r2','r3'})
        fs[2]['event_id']='other_event'
        r=Engine({'facts':fs,'records':{}}).answer('Aurora 2026 Tournament 1.2 Maps','en',category='C13',allow_llm=False)
        self.assertEqual(r['claims'],[])
    def test_all_fourteen_routes(self):
        qs={'C01':'ศูนย์อยู่ตึกไหน','C02':'บุคลากรมีหน้าที่อะไร','C03':'อุปกรณ์มีกี่เครื่อง','C04':'มีเกมอะไรบ้าง','C05':'กระโดดต้องกดปุ่มไหน',
          'C06':'ราคาเล่นต่อรอบเท่าไร','C07':'เหมาโซนราคาเท่าไร','C08':'ต้องจองก่อนไหม','C09':'โอนขาดทำไง','C10':'เอาคีย์บอร์ดตัวเองมาได้ไหม',
          'C11':'วันนี้เปิดไหม','C12':'PC1 ตอนนี้ว่างไหม','C13':'กติกาการแข่งขัน Aurora','C14':'ข่าวกิจกรรมล่าสุด'}
        for cat,q in qs.items():
            with self.subTest(category=cat):self.assertEqual(route(self.engine.index,q),cat)

class ProtocolTests(unittest.TestCase):
    def test_identity_mismatch_is_not_transport_failure(self):
        selector=EvidenceSelector(transport=lambda _: {'model':'wrong-model','message':{'content':'{}'}},model='test')
        plans,e=selector.select([{'question':'test','facts':[fact('C01','test','address','Studio','address','Address')]}],RequestBudget())
        self.assertTrue(e['transport_ok']);self.assertFalse(e['identity_verified']);self.assertEqual(plans[0].reason,'model_identity_mismatch')
    def test_preserves_valid_items_when_middle_missing(self):
        plans,d=parse_items('{"plans":[{"i":0,"choices":[1]},{"i":2,"choices":[1]}]}',[{1:'a'},{1:'b'},{1:'c'}])
        self.assertEqual(plans[0].ids,['a']);self.assertEqual(plans[1].status,'unavailable');self.assertEqual(plans[2].ids,['c']);self.assertEqual(d['valid_items'],2)
    def test_duplicate_identity_rejects_only_its_item(self):
        p,d=parse_items('{"plans":[{"i":0,"choices":[]},{"i":0,"choices":[1]},{"i":1,"choices":[1]}]}',[{1:'a'},{1:'b'}])
        self.assertEqual(p[0].status,'unavailable');self.assertEqual(p[1].ids,['b'])
    def test_bool_not_integer_choice(self):
        p,_=parse_items('{"plans":[{"i":0,"choices":[true]}]}',[{1:'a'}]);self.assertEqual(p[0].status,'unavailable')
    def test_fabricated_identifier_rejected(self):
        p,_=parse_items('{"plans":[{"i":0,"choices":[99]}]}',[{1:'a'}]);self.assertEqual(p[0].ids,[])
    def test_unknown_is_valid_empty_plan(self):
        p,_=parse_items('{"plans":[{"i":0,"choices":[]}]}',[{1:'a'}]);self.assertEqual(p[0].status,'missing_source')
    def test_request_model_budget(self):
        count=[]
        def transport(payload):count.append(payload);return {'model':'test','message':{'content':'{"plans":[{"i":0,"choices":[]}]}'}}
        selector=EvidenceSelector(transport=transport,model='test');b=RequestBudget(max_model_calls=1)
        task=[{'question':'unknown','facts':[fact('C01','test','address','Test Studio','address','Synthetic address')]}]
        selector.select(task,b);p,_=selector.select(task,b);self.assertEqual(len(count),1);self.assertEqual(p[0].status,'unavailable')

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    out=R/'verification';out.mkdir(exist_ok=True)
    target=out/('SCOPE_PROTOCOL_run'+str(len(list(out.glob('SCOPE_PROTOCOL*')))+1).zfill(2)+'.json')
    target.write_text(json.dumps({'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful()},indent=2),'utf8')
    raise SystemExit(not result.wasSuccessful())
