from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
assert not (OUT/'EDIT3_DONE').exists()
def edit(name,old,new):
 p=ROOT/name;t=p.read_text(encoding='utf-8');assert old in t,name;p.write_text(t.replace(old,new,1),encoding='utf-8')
edit('app/pipeline/engine.py','        if self._deadline_is_exceeded(trace, "after_multi_children"):', '''        evidence_stages = {'conversation_contract','source_operation','user_service_facts','competition_overview','rulebook_coverage'}
        trace.append(PipelineTrace('compound_source_evidence','child_source_bindings',1.0,
            'preserve recorded assertions per child; execution coverage is not accuracy',
            {'children': [{'question': part, 'mode': result.mode,
                'source_traces': [{'stage': t.stage, 'decision': t.decision, 'metadata': t.metadata}
                    for t in result.trace if t.stage in evidence_stages]}
                for part, result in zip(display_parts, results)]}))
        if self._deadline_is_exceeded(trace, "after_multi_children"):''')
edit('app/booking/live_status.py','import json\n','import json\nfrom contextlib import contextmanager\nfrom contextvars import ContextVar\n')
edit('app/booking/live_status.py','_FETCH_LOCK = threading.Lock()','''_FETCH_LOCK = threading.Lock()
_REQUEST_SNAPSHOTS = ContextVar('booking_request_snapshots', default=None)

@contextmanager
def booking_request_snapshots():
    """One aggregate snapshot per date/transport within an answer only.

    copy_context shares this state with compound children. It expires at
    the end of the request; the next question uses the configured transport.
    """
    if _REQUEST_SNAPSHOTS.get() is not None:
        yield
        return
    token = _REQUEST_SNAPSHOTS.set({'lock': threading.Lock(), 'values': {}})
    try:
        yield
    finally:
        _REQUEST_SNAPSHOTS.reset(token)''')
edit('app/booking/live_status.py','    fetch_elapsed_ms: float = 0.0','    fetch_elapsed_ms: float = 0.0\n    request_reused: bool = False')
edit('app/booking/live_status.py','            "fetch_elapsed_ms": self.fetch_elapsed_ms,','            "fetch_elapsed_ms": self.fetch_elapsed_ms,\n            "request_reused": self.request_reused,')
edit('app/booking/live_status.py','def get_live_booking_status(selected_date: str) -> LiveBookingSnapshot:\n', '''def get_live_booking_status(selected_date: str) -> LiveBookingSnapshot:
    scope = _REQUEST_SNAPSHOTS.get()
    if scope is None:
        return _fetch_live_booking_status(selected_date)
    config = live_booking_runtime_config()
    key = (config['fetch_mode'], _status_url(), selected_date)
    with scope['lock']:
        if key in scope['values']:
            return replace(scope['values'][key], request_reused=True)
        result = _fetch_live_booking_status(selected_date)
        scope['values'][key] = result
        return result


def _fetch_live_booking_status(selected_date: str) -> LiveBookingSnapshot:
''')
edit('app/pipeline/engine.py','        with request_deadline(global_timeout_sec):','        from app.booking.live_status import booking_request_snapshots\n        with request_deadline(global_timeout_sec), booking_request_snapshots():')
(OUT/'EDIT3_DONE').write_text('compound source evidence and request-local booking snapshot consistency',encoding='utf-8');print('request scoped evidence and booking snapshots added')
