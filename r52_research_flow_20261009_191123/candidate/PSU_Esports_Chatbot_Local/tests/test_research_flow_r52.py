import json, multiprocessing as mp, tempfile, time, unittest, os
from pathlib import Path
from unittest.mock import patch
from app.web_api.chat_jobs import ChatJobQueue, JobError
from app.pipeline.model_admission import ModelAdmissionBroker, RemoteModelGate
from app.pipeline.protected_intents import _is_price_without_service
from app.pipeline.preprocess import extract_entities, preprocess_input
from app.pipeline.query_signals import looks_like_clear_general_request
from app.pipeline.answer_contracts import _answer_types
from app.pipeline.schemas import PipelineRoute
import app.pipeline.experimental_fallback as f


class ResearchFlowTests(unittest.TestCase):
    def test_incidental_words_not_financial_or_control(self):
        q='Why can high frame rate still feel choppy?'
        self.assertFalse(_is_price_without_service(q.casefold(),None))
        self.assertFalse(extract_entities(preprocess_input(q)).price_intent)
        self.assertTrue(_is_price_without_service('What is the hourly rate for using equipment?'.casefold(),None))
        route=PipelineRoute('general','detail',.9,'fact','low','fixture')
        self.assertNotIn('controls',_answer_types('Delay across a network.',route))
        self.assertIn('controls',_answer_types('Press Cross to jump.',route))

    def test_task_and_profile_coverage(self):
        with patch.object(f,'effective_locale',return_value='en'):
            q='Give three steps for learning touch typing.'
            self.assertTrue(looks_like_clear_general_request(q))
            p=f.select_general_generation_profile(q)
            self.assertEqual(p.expected_items,3)
            self.assertFalse(f._general_output_contract('1. Practice accuracy.\n2. Practice speed.',p,{})[0])
            self.assertTrue(f._general_output_contract('1. Use home row.\n2. Avoid looking down.\n3. Practice accuracy.',p,{})[0])
            p=f.select_general_generation_profile('Write a two-sentence invitation to a study session.')
            self.assertFalse(f._general_output_contract('Join us.',p,{})[0])
            self.assertTrue(f._general_output_contract('Join us. We can learn together.',p,{})[0])
            p=f.select_general_generation_profile('Compare TCP and UDP, including one advantage and one disadvantage of each.')
            self.assertFalse(f._general_output_contract('TCP Pros: reliable; Cons: overhead.\nUDP Pros: fast.',p,{})[0])
            self.assertTrue(f._general_output_contract('TCP Pros: reliable; Cons: overhead.\nUDP Pros: low overhead; Cons: packet loss.',p,{})[0])
            p=f.select_general_generation_profile('Explain networks in approximately 500 words.')
            self.assertGreater(p.num_predict,128)
            self.assertFalse(f._general_output_contract('A network connects computers.',p,{})[0])
            self.assertFalse(f._general_output_contract(' '.join(['word']*500),p,{'ollama_done_reason':'length'})[0])

    def test_timeout_metadata_not_lost(self):
        with patch.object(f,'llm_call_allowed',return_value=(True,{})), patch.object(f,'record_llm_failure',return_value={}), patch.object(f,'_call_ollama',side_effect=TimeoutError('fixture timeout')):
            result=f._general_llm_fallback('Explain ping.',details=(),mode='general_llm_direct',decision='fixture')
        trace=result.trace.metadata['llm_call']
        self.assertEqual(trace['llm_failure_reason'],'model_timeout')
        self.assertEqual(trace['llm_error_type'],'TimeoutError')
        self.assertIn('llm_elapsed_ms',trace)
        self.assertIn('llm_answer_plan',trace)

    def test_stream_requires_done_and_records_partial(self):
        class Response:
            def __iter__(self):return iter([b'{"response":"partial"}\n'])
            def close(self):pass
        metadata={}
        with patch.object(f.urllib.request,'urlopen',return_value=Response()):
            with self.assertRaises(f.OllamaIncompleteResponseError):f._call_ollama('fixture',response_metadata=metadata)
        self.assertEqual(metadata['llm_partial_response_chars'],7)
        self.assertIsNotNone(metadata['llm_first_token_ms'])

    def test_job_persistence_conflict_capacity_order_and_restart(self):
        with tempfile.TemporaryDirectory(dir=os.getenv('PSU_TEST_TMP_DIR')) as folder:
            path=Path(folder)/'jobs.sqlite3'; jobs=ChatJobQueue(path,'http://unused',capacity=3)
            a=dict(question='first',client_session_id='session-abcdefghijk',client_turn_id='turn-abcdefghijk1')
            b=dict(a,question='second',client_turn_id='turn-abcdefghijk2')
            c=dict(a,question='other',client_session_id='session-otherabcdefgh')
            ja=jobs.submit(a); self.assertEqual(jobs.submit(a)['job_id'],ja['job_id'])
            with self.assertRaises(JobError) as cm:jobs.submit(dict(a,question='changed'))
            self.assertEqual(cm.exception.reason,'client_turn_conflict')
            jb=jobs.submit(b); jc=jobs.submit(c)
            with self.assertRaises(JobError):jobs.submit(dict(c,client_turn_id='turn-newabcdefgh'))
            first=jobs._claim(); other=jobs._claim()
            self.assertEqual(first['id'],ja['job_id']); self.assertEqual(other['id'],jc['job_id'])
            self.assertIsNone(jobs._claim())
            with self.assertRaises(JobError):jobs.cancel(ja['job_id'],a['client_session_id'])
            recovered=ChatJobQueue(path,'http://unused')
            self.assertEqual(recovered.get(ja['job_id'],a['client_session_id'])['error'],'worker_lost')
            self.assertEqual(recovered.get(jb['job_id'],a['client_session_id'])['status'],'queued')
            self.assertEqual(recovered.cancel(jb['job_id'],a['client_session_id'])['status'],'cancelled')
            with self.assertRaises(JobError):jobs.get(ja['job_id'],'wrong-session')

    def test_broker_limit_and_dead_owner_recovery(self):
        broker=ModelAdmissionBroker(mp.get_context('spawn'),limit=1); broker.start()
        channel1, channel2=broker.register(),broker.register()
        gate1,gate2=RemoteModelGate(*channel1),RemoteModelGate(*channel2)
        try:
            self.assertTrue(gate1.acquire(timeout=.5))
            self.assertFalse(gate2.acquire(timeout=.05))
            broker.revoke(channel1[2])
            self.assertTrue(gate2.acquire(timeout=.5))
            gate2.release();time.sleep(.05)
            self.assertEqual(broker.snapshot()['active'],0)
            self.assertEqual(broker.snapshot()['peak_active'],1)
        finally:broker.stop()

if __name__=='__main__':unittest.main()
