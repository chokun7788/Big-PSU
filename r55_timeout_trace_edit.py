from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:100]);p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/pipeline/performance_trace.py','import json\n','import json\nimport copy\nfrom collections import OrderedDict,deque\n')
edit('app/pipeline/performance_trace.py','        self._lock = threading.Lock()','        self._lock = threading.Lock()\n        self._recent_events = OrderedDict()')
edit('app/pipeline/performance_trace.py','    def _run(self) -> None:', '''    def request_snapshot(self,request_id: str) -> dict[str, Any]:
        """Bounded partial progress, never an inferred cause of a timeout."""
        with self._lock:
            events=copy.deepcopy(list(self._recent_events.get(str(request_id),())))
        return {'partial':True,'events':events,'last_reported_stage':events[-1]['stage'] if events else None,
                'cause_confirmed':False}

    def _run(self) -> None:''')
edit('app/pipeline/performance_trace.py','                    self._count += 1', '''                    self._count += 1
                    if event.get('event') in {'stage_started','stage_finished','stage_progress','stage_failed'}:
                        request_id=str(event.get('request_id') or '')
                        if request_id:
                            recent=self._recent_events.setdefault(request_id,deque(maxlen=16))
                            recent.append({key:event.get(key) for key in ('event','stage','status','sequence','elapsed_ms','remaining_ms')})
                            self._recent_events.move_to_end(request_id)
                            while len(self._recent_events)>64:self._recent_events.popitem(last=False)''')
edit('app/web_api/pipeline_supervisor.py','            except queue.Empty:\n                diagnostics = _worker_exit_diagnostics(slot.process.exitcode, timed_out=True)', '''            except queue.Empty:
                diagnostics = _worker_exit_diagnostics(slot.process.exitcode, timed_out=True)
                diagnostics['partial_progress']=self._performance.request_snapshot(request_id or task_id)''')
edit('app/web_api/server.py','worker_id: int, locale: LocaleDecision) -> dict[str, Any]:','worker_id: int, locale: LocaleDecision, diagnostics: dict[str, Any] | None = None) -> dict[str, Any]:')
edit('app/web_api/server.py','        "timeout_stage": "pipeline_worker_supervision",','        "timeout_stage": "pipeline_worker_supervision",\n        "processing_diagnostics": diagnostics or {"partial_progress":{"partial":True,"events":[],"cause_confirmed":False}},')
edit('app/web_api/server.py','                            locale=locale_decision,\n                        )\n                        _write_chat_log_async', '                            locale=locale_decision,\n                            diagnostics=supervised.diagnostics,\n                        )\n                        _write_chat_log_async')
edit('app/web_api/server.py','                            "timeout_stage": timeout_response["timeout_stage"],','                            "timeout_stage": timeout_response["timeout_stage"],\n                            "processing_diagnostics": timeout_response["processing_diagnostics"],')
edit('tests/test_service_repairs_r55.py','    def test_vr_hour_occupancy_fixture(self):', '''    def test_timeout_partial_progress_is_scoped_and_not_a_claimed_cause(self):
        import tempfile,queue,time,os
        from pathlib import Path
        from app.pipeline.performance_trace import ParentPerformanceLogger
        from app.web_api.server import _supervisor_timeout_response
        from app.core.locale import resolve_locale
        with tempfile.TemporaryDirectory(dir=os.getenv('PSU_TEST_TMP_DIR')) as folder:
            events=queue.Queue();logger=ParentPerformanceLogger(events,path=Path(folder)/'progress.jsonl');logger.start()
            events.put(dict(event='stage_finished',request_id='one',stage='retrieval',status='accepted',sequence=1,elapsed_ms=30,remaining_ms=100))
            deadline=time.monotonic()+1
            while logger.snapshot()['events_written']<1 and time.monotonic()<deadline:time.sleep(.02)
            partial=logger.request_snapshot('one');other=logger.request_snapshot('two');logger.stop()
            self.assertEqual(partial['last_reported_stage'],'retrieval');self.assertFalse(partial['cause_confirmed']);self.assertEqual(other['events'],[])
            response=_supervisor_timeout_response(request_id='one',started=time.perf_counter(),worker_id=0,locale=resolve_locale('hello',requested='en'),diagnostics={'partial_progress':partial})
            self.assertEqual(response['processing_diagnostics']['partial_progress']['last_reported_stage'],'retrieval')
    def test_vr_hour_occupancy_fixture(self):''')
print('bounded partial timeout diagnostics added')
