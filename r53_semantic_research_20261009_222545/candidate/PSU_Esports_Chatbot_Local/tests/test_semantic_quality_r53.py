import json,unittest
from unittest.mock import patch
import app.pipeline.experimental_fallback as f
from app.pipeline.semantic_quality import translation_request,translation_errors,evidence_for,semantic_errors

class SemanticQualityTests(unittest.TestCase):
    def test_translation_priority_and_target_are_explicit(self):
        with patch.object(f,'effective_locale',return_value='en'):
            q='Translate "Wait 15 minutes. Check your network." into Thai.'
            p=f.select_general_generation_profile(q)
            self.assertEqual(p.name,'translation')
            self.assertIn('into Thai',f._build_general_prompt(q,p))
            self.assertEqual(translation_request(q)['source'],'Wait 15 minutes. Check your network.')
            p=f.select_general_generation_profile('Translate "Write two sentences about networking." into Thai.')
            self.assertEqual(p.name,'translation')

    def test_translation_critical_constraints_and_paraphrases(self):
        for source,bad,good in (
            ('Wait 15 minutes.','รอ 50 นาที','โปรดรอ 15 นาที'),
            ('Use PC1 for 60 minutes.','ใช้ PC2 60 นาที','กรุณาใช้ PC1 เป็นเวลา 60 นาที'),
            ('You cannot cancel.','คุณยกเลิกได้','คุณไม่สามารถยกเลิกได้'),
            ('Check your network connection.','ตรวจสอบอินเทอร์เน็ต','ตรวจสอบการเชื่อมต่อเครือข่าย'),
            ('Wait 15 minutes.','รอ 15 ชั่วโมง','รอ ๑๕ นาที'),
        ):
            with self.subTest(source=source):
                self.assertTrue(translation_errors(source,bad,'th'))
                self.assertFalse(translation_errors(source,good,'th'))
        self.assertFalse(translation_errors('ตรวจสอบอินเทอร์เน็ต','Check the internet connection.','en'))

    def test_literal_note_and_instruction_text_is_translation_data(self):
        q='Translate "Note: Check your network." into Thai.'
        errors,meta=semantic_errors(q,'หมายเหตุ: ตรวจสอบเครือข่าย','translation')
        self.assertFalse(errors)
        self.assertFalse(meta['all_claims_verified'])
        self.assertFalse(meta['sources'])

    def test_scoped_evidence_does_not_replace_studio_or_writing(self):
        self.assertTrue(evidence_for('Explain RAM in two sentences.','two_sentences'))
        self.assertFalse(evidence_for('ราคา RAM ของศูนย์','general_concise'))
        self.assertFalse(evidence_for('Write an invitation to learn HTTP.','two_sentences'))
        self.assertFalse(evidence_for('Translate "HTTP uses TCP" into Thai.','translation'))

    def test_metadata_distinguishes_unknown_from_semantic_certification(self):
        errors,meta=semantic_errors('Translate this please.','ขอบคุณ','translation')
        self.assertFalse(errors)
        self.assertEqual(meta['translation_extraction'],'unresolved')
        self.assertEqual(meta['semantic_verification'],'bounded_constraints_only')
        self.assertFalse(meta['all_claims_verified'])

    def _generate(self,q,text,locale='en'):
        with patch.object(f,'effective_locale',return_value=locale),patch.object(f,'llm_call_allowed',return_value=(True,{})),patch.object(f,'_call_ollama',return_value=text),patch.object(f,'record_llm_success',return_value={}):
            return f._general_llm_answer_with_metadata(q)

    def test_translation_and_writing_outputs_can_be_copied_without_note(self):
        a,m=self._generate('Translate "Check your network." into Thai.','ตรวจสอบเครือข่าย')
        self.assertEqual(a,'ตรวจสอบเครือข่าย')
        self.assertTrue(m['llm_provenance_note_omitted_for_copy_task'])
        self.assertTrue(m['llm_provider_attempted'])
        a,m=self._generate('Write two sentences inviting friends to study.','Join our study session. We can learn together.')
        self.assertEqual(a,'Join our study session. We can learn together.')

    def test_model_note_does_not_suppress_provenance(self):
        a,m=self._generate('Explain latency briefly.','Latency is a delay. Note: It affects games.')
        self.assertIn('not verified by the PSU',a)
        self.assertFalse(m['llm_semantic_quality']['all_claims_verified'])

    def test_fact_context_and_failure_reason_are_visible(self):
        a,m=self._generate('Explain ping briefly.','Ping measures bandwidth in Mbps.')
        self.assertFalse(a)
        self.assertEqual(m['llm_output_rejected_reason'],'semantic_ping_bandwidth_claim')
        a,m=self._generate('Explain ping briefly.','Ping checks reachability and round-trip time using ICMP.')
        self.assertTrue(a)
        self.assertIn('learn.microsoft.com',a)
        self.assertEqual(m['llm_semantic_quality']['evidence_ids'],['ping'])

    def test_one_semantic_repair_is_bounded_and_serializable(self):
        bad={'llm_output_contract_ok':False,'llm_generation_profile':'translation','llm_output_rejected_reason':'semantic_number_preservation','llm_rejected_draft':'รอ 50 นาที'}
        with patch.object(f,'_general_llm_answer_with_metadata',side_effect=[('',bad),('รอ 15 นาที',{'llm_output_contract_ok':True})]) as call:
            result=f._general_llm_fallback('Translate "Wait 15 minutes." into Thai.',details=(),mode='general_llm_direct',decision='fixture')
        self.assertEqual(call.call_count,2)
        self.assertIn('semantic_number_preservation',call.call_args.kwargs['repair_reason'])
        json.dumps(result.trace.metadata)

    def test_semantic_failure_is_not_reported_as_provider_outage(self):
        bad={'llm_output_contract_ok':False,'llm_generation_profile':'translation','llm_output_rejected_reason':'semantic_number_preservation'}
        with patch.object(f,'_general_llm_answer_with_metadata',return_value=('',bad)),patch.object(f,'timeout_for_call',return_value=0):
            result=f._general_llm_fallback('Translate "Wait 15 minutes." into Thai.',details=(),mode='general_llm_direct',decision='fixture')
        self.assertEqual(result.trace.metadata['llm_call']['llm_failure_reason'],'output_meaning_unverified')

if __name__=='__main__':unittest.main()
