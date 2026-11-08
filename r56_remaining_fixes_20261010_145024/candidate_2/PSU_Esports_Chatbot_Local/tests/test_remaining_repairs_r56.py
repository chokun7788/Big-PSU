import unittest,tempfile,json,urllib.error,io
from pathlib import Path
from unittest.mock import patch
from app.pipeline.request_focus import explicit_request_focus
from app.pipeline.service_query_completion import split_service_operations
from app.session.conversation_plan import excluded_services,resolve_request_plan
from app.pipeline.user_service_facts import answer_user_service_facts
from app.web_api.chat_jobs import ChatJobQueue,JobError

class RemainingRepairs(unittest.TestCase):
    def test_negative_noun_does_not_negate_later_device(self):
        for q in ('ไม่ใช่นักศึกษา เล่น PC หนึ่งชั่วโมงเท่าไหร่','I am not a student. PC for one hour','not tournament rules, PC games'):
            with self.subTest(q=q):self.assertEqual(excluded_services(q),[])
        self.assertEqual(excluded_services('Not PS5. PC for two hours'),['ps5'])
        self.assertEqual(excluded_services('ทุกบริการยกเว้น VR'),['vr'])
        self.assertEqual(resolve_request_plan('Not PS5. PC for a general adult for two hours, how much?',[],locale='en')['tasks'][0]['targets'],['pc'])
    def test_explicit_correction_and_negative_policy(self):
        for q,needle in [('ไม่เอาราคา ขอรายชื่อเกม PC ทั้งหมด','รายชื่อเกม'),('I do not want prices, just list all PC games','list'),('ไม่ใช่กฎแข่ง ขอปุ่มยิงกับรีโหลด CS2','ปุ่ม'),('Not tournament rules. How do I shoot and reload in CS2?','shoot')]:
            with self.subTest(q=q):
                focus,trace=explicit_request_focus(q);self.assertIn(needle,focus);self.assertIsNotNone(trace)
        for q in ('I am not a student','ไม่ใช่นักศึกษา','Are personal mice not allowed?','ไม่เอารายการเกมอะไรแล้ว','Translate: not prices, list games'):
            self.assertEqual(explicit_request_focus(q),(q,None))
    def test_all_four_to_six_shop_clauses_survive(self):
        q='PC มีเกมอะไรบ้าง; บุคคลทั่วไปเล่น PC สองชั่วโมงเท่าไหร่; ต้องสมัครสมาชิกไหม; มีที่จอดรถไหม; ศูนย์อยู่ตึกอะไร; จ่ายเงินสดได้ไหม'
        self.assertEqual(len(split_service_operations(q)),6)
        self.assertIsNone(resolve_request_plan(q,[]))
        self.assertEqual(len(split_service_operations('How do I shoot and reload in CS2?')),1)
    def test_parking_is_not_monitor(self):
        r=answer_user_service_facts('ศูนย์อยู่ตึกอะไร แล้วมีที่จอดรถไหม')
        self.assertEqual(r['trace'][0].metadata['claim_ids'],['parking','location'])
        self.assertIn('อาคาร 5',r['answer'])
        self.assertNotIn('location',answer_user_service_facts('PC จออยู่ตึกอะไร มีที่จอดรถไหม')['trace'][0].metadata['claim_ids'])
    def test_player_not_listed_natural_order(self):
        r=answer_user_service_facts('ผมจองชื่อผมแต่คนเล่นไม่มีชื่อในรายการได้ไหม')
        self.assertIn('player_identity',r['trace'][0].metadata['claim_ids'])
    def test_mixed_language_logout_unknown(self):
        r=answer_user_service_facts('ลืม logout ต้องทำยังไง')
        self.assertIn('forgotten_logout_procedure',r['validation'].warnings)
    def test_job_times_terminal_stable_retry_admission_not_inference(self):
        with tempfile.TemporaryDirectory() as d:
            j=ChatJobQueue(Path(d)/'jobs.db','http://unused')
            with patch('app.web_api.chat_jobs.time.time',return_value=100):x=j.submit(dict(client_session_id='s',client_turn_id='t',question='PC'))
            with patch('app.web_api.chat_jobs.time.time',return_value=103):row=j._claim()
            with patch('app.web_api.chat_jobs.time.time',return_value=104):j._defer(row['id'],'server_busy')
            with patch('app.web_api.chat_jobs.time.time',return_value=105):
                q=j.get(x['job_id'],'s');self.assertEqual(q['timing']['active_dispatch_sec'],0)
                row=j._claim()
            with patch('app.web_api.chat_jobs.time.time',return_value=109):j._finish(row['id'],'completed',result={'answer':'ok'})
            a=j.get(x['job_id'],'s');b=j.get(x['job_id'],'s')
            self.assertEqual(a['timing'],b['timing']);self.assertEqual(a['timing']['elapsed_sec'],9)
            self.assertEqual(a['timing']['admission_wait_sec'],5);self.assertEqual(a['timing']['active_dispatch_sec'],4)
            self.assertEqual(a['dispatch_attempts'],2)
    def test_capacity_idempotency_and_no_ambiguous_replay(self):
        with tempfile.TemporaryDirectory() as d:
            j=ChatJobQueue(Path(d)/'jobs.db','http://unused',capacity=1)
            p=dict(client_session_id='s',client_turn_id='t',question='PC');x=j.submit(p)
            self.assertEqual(j.submit(p)['job_id'],x['job_id'])
            with self.assertRaises(JobError):j.submit(dict(p,question='VR'))
            with self.assertRaises(JobError):j.submit(dict(p,client_turn_id='t2'))
            row=j._claim()
            with patch('app.web_api.chat_jobs.urllib.request.urlopen',side_effect=urllib.error.URLError('socket lost')) as call:j._execute(row)
            self.assertEqual(call.call_count,1);self.assertEqual(j.get(x['job_id'],'s')['status'],'failed')
            self.assertIsNone(j._claim())
    def test_only_explicit_admission_rejection_is_retryable(self):
        with tempfile.TemporaryDirectory() as d:
            j=ChatJobQueue(Path(d)/'jobs.db','http://unused');p=dict(client_session_id='s',client_turn_id='t',question='PC');x=j.submit(p);row=j._claim()
            err=urllib.error.HTTPError('http://unused',503,'busy',{},io.BytesIO(json.dumps({'error':'server_busy'}).encode()))
            with patch('app.web_api.chat_jobs.urllib.request.urlopen',side_effect=err):j._execute(row)
            self.assertEqual(j.get(x['job_id'],'s')['status'],'queued')
            err=urllib.error.HTTPError('http://unused',500,'failure',{},io.BytesIO(b'{"error":"backend_error"}'))
            with patch('app.web_api.chat_jobs.time.time',return_value=10**12):
                # Expiration is a terminal failure, never a new backend attempt.
                self.assertIsNone(j._claim())
            self.assertEqual(j.get(x['job_id'],'s')['error'],'queue_expired')
