from pathlib import Path
import json

project = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
path = project / 'app/web_api/pipeline_supervisor.py'
text = path.read_text(encoding='utf-8')
assert 'def _maybe_recycle_slot(self, slot: _WorkerSlot) -> None:' in text
text = text.replace('self._maybe_recycle_slot(slot)', 'self._maybe_recycle_slot(slot, request_id=request_id or task_id)')
text = text.replace('def _maybe_recycle_slot(self, slot: _WorkerSlot) -> None:', 'def _maybe_recycle_slot(self, slot: _WorkerSlot, *, request_id: str) -> None:')
old = 'emit_parent("worker_recycle", "pipeline", worker_id='
assert text.count(old) == 4
text = text.replace(old, 'emit_parent("worker_recycle", "pipeline", request_id=request_id, worker_id=')
path.write_text(text, encoding='utf-8')

path = project / 'tests/test_worker_recycle_r27_20261001.py'
text = path.read_text(encoding='utf-8')
text = text.replace('from unittest.mock import Mock, patch', 'from unittest.mock import Mock, patch, create_autospec')
text = text.replace('from app.web_api.pipeline_supervisor import', 'from app.pipeline.performance_trace import ParentPerformanceLogger\nfrom app.web_api.pipeline_supervisor import')
text = text.replace('obj._performance=Mock()', 'obj._performance=create_autospec(ParentPerformanceLogger, instance=True)')
text = text.replace('obj._maybe_recycle_slot(old)', 'obj._maybe_recycle_slot(old, request_id="test-recycle")')
text += '''
    def test_spawn_failure_preserves_active_worker_and_records_request(self):
        old=slot(1,True);obj=self.supervisor(old)
        with patch.object(obj,'_new_slot',side_effect=OSError('fixture spawn failure')):
            obj._maybe_recycle_slot(old,request_id='spawn-failure')
        self.assertIs(obj._slots[0],old);self.assertIsNone(old.replacement)
        self.assertGreater(old.recycle_retry_after,time.perf_counter())
        obj._performance.emit_parent.assert_called_once()
        self.assertEqual(obj._performance.emit_parent.call_args.kwargs['request_id'],'spawn-failure')
        self.assertEqual(obj._performance.emit_parent.call_args.kwargs['status'],'spawn_failed')
'''
path.write_text(text, encoding='utf-8')

base=Path(__file__).parent
with (base/'r27_verified_web_check.py').open('x',encoding='utf-8') as f:
    f.write((base/'r27_final_web_check.py').read_text(encoding='utf-8').replace('2026.10.01-competition-contract-r27-final','2026.10.01-competition-contract-r27-verified'))
print(json.dumps({'modified':['app/web_api/pipeline_supervisor.py','tests/test_worker_recycle_r27_20261001.py']}))
