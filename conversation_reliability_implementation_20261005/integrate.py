from pathlib import Path
import shutil, hashlib, json
ROOT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
HERE = Path(__file__).resolve().parent

def edit(rel, old, new, count=1):
    p=ROOT/rel
    original=p.read_text(encoding='utf-8-sig')
    if original.count(old) < count:
        raise ValueError(f'Expected {count} occurrences in {rel}: {old[:100]!r}')
    backup=HERE/'before'/rel
    if not backup.exists():
        backup.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,backup)
    p.write_text(original.replace(old,new,count),encoding='utf-8',newline='')

edit('app/pipeline/engine.py', '        keyboard_layout_direction: str | None = None,\n    ) -> PipelineAnswer:', '        keyboard_layout_direction: str | None = None,\n        request_plan: dict | None = None,\n    ) -> PipelineAnswer:')
edit('app/pipeline/engine.py', '            canonical_started = time.perf_counter()', '''            from app.session.conversation_plan import resolve_request_plan
            from app.pipeline.conversation_fee import build_price_plan_answer
            from app.pipeline.dialogue_choice import review_pending_choice
            typed_plan = request_plan or resolve_request_plan(cue_preflight, recent_history, locale=resolved_locale.effective)
            if typed_plan is not None:
                typed_plan, choice_trace = review_pending_choice(typed_plan, resolved_locale.effective, bool(experimental_allow_llm))
                fee_result = build_price_plan_answer(typed_plan, resolved_locale.effective)
                if fee_result is not None:
                    contract = fee_result['metadata']
                    trace = [*entry_timings, PipelineTrace('conversation_request', typed_plan['act'], 1.0,
                             'typed slots preserve user filters; assistant options are not selections',
                             {'request_plan': typed_plan, 'outcome': contract.get('outcome')}),
                             *([choice_trace] if choice_trace else []), *fee_result['trace']]
                    if not any(t.stage == 'conversation_contract' for t in trace):
                        trace.append(PipelineTrace('conversation_contract', contract['outcome'], 1.0, 'targeted dialogue clarification', contract))
                    return self._build_result(fee_result['answer'], fee_result['hits'], started,
                        fee_result['mode'], .98, fee_result['route'], fee_result['entities'], fee_result['validation'], trace)
            canonical_started = time.perf_counter()''')
edit('app/pipeline/engine.py', '    keyboard_layout_direction: str | None = None,\n) -> PipelineAnswer:', '    keyboard_layout_direction: str | None = None,\n    request_plan: dict | None = None,\n) -> PipelineAnswer:')
edit('app/pipeline/engine.py', '        keyboard_layout_direction=keyboard_layout_direction,\n    )', '        keyboard_layout_direction=keyboard_layout_direction,\n        request_plan=request_plan,\n    )')
edit('app/pipeline/engine.py', '        if not bool(selection.get("execution_allowed", True)) and question_frame.operation == "unknown":', '        if not bool(selection.get("execution_allowed", True)) and question_frame.operation == "unknown" and not (route.category == "general" and route.risk == "low" and looks_like_clear_general_request(pre.clean_query)):')

edit('app/web_api/pipeline_supervisor.py', '                    recent_history=task.get("recent_history"),', '                    recent_history=task.get("recent_history"),\n                    request_plan=task.get("request_plan"),')
edit('app/web_api/pipeline_supervisor.py', '        recent_history: list[dict[str, Any]] | None = None,\n    ) -> SupervisedCall:', '        recent_history: list[dict[str, Any]] | None = None,\n        request_plan: dict | None = None,\n    ) -> SupervisedCall:')
edit('app/web_api/pipeline_supervisor.py', '                    "recent_history": list(recent_history or [])[-10:],', '                    "recent_history": list(recent_history or [])[-10:],\n                    "request_plan": request_plan,')

edit('app/session/context_resolver.py', '    competition_followup = _resolve_competition_followup(original, recent_history)', '''    from app.session.conversation_plan import resolve_request_plan
    price_plan = resolve_request_plan(original, recent_history, locale=locale)
    if price_plan and price_plan.get('context_used'):
        return ResolvedQuestion(original, price_plan['resolved_query'], True, context_domain='service_fee',
                                context_operation='price_lookup', reason='typed_price_followup')
    competition_followup = _resolve_competition_followup(original, recent_history)''')
edit('app/session/context_resolver.py', '    for text in reversed(_history_text_items(recent_history)):\n        q = normalize_text(text)\n        if any(term in q for term in ("playstation 5 zone",', '''    # An assistant's list of options does not identify the user's zone.
    selected_history = [item for item in recent_history if isinstance(item, dict) and item.get('role') == 'user'] if isinstance(recent_history, list) else []
    for text in reversed(_history_text_items(selected_history)):
        q = normalize_text(text)
        if any(term in q for term in ("playstation 5 zone",''')

edit('app/web_api/server.py', 'from app.session.context_resolver import resolve_question_with_context', 'from app.session.context_resolver import resolve_question_with_context, ResolvedQuestion\nfrom app.session.conversation_store import STORE, TurnConflict')
edit('app/web_api/server.py', 'LOG_DIR = PROJECT_ROOT / "data" / "logs"', 'LOG_DIR = Path(os.getenv("PSU_CHAT_LOG_DIR") or PROJECT_ROOT / "data" / "logs")')
edit('app/web_api/server.py', '        recent_history = payload.get("recent_history") or []', '''        client_turn_id = str(payload.get('client_turn_id') or '').strip()
        if not is_valid_session_id(client_turn_id):
            client_turn_id = f'turn-{uuid.uuid4()}'
        last_seen_response_id = str(payload.get('last_seen_response_id') or '')[:128]
        recent_history = payload.get("recent_history") or []''')
edit('app/web_api/server.py', '                resolved = resolve_question_with_context(question, recent_history, locale=locale_decision.effective)', '''                recent_history = STORE.history(client_session_id, recent_history)
                if last_seen_response_id:
                    STORE.acknowledge(client_session_id, last_seen_response_id)
                try:
                    turn = STORE.begin(client_session_id, client_turn_id, question, locale=locale_decision.effective, history=recent_history)
                except TurnConflict:
                    self._send_json({'ok': False, 'error': 'client_turn_conflict', 'request_id': request_id}, 409)
                    return
                if turn['response']:
                    self._send_json(turn['response'], content_language=locale_decision.effective)
                    STORE.delivery(client_session_id, client_turn_id, 'server_written')
                    return
                request_plan = turn['plan']
                if request_plan:
                    resolved = ResolvedQuestion(question, request_plan['resolved_query'], request_plan.get('context_used', False),
                        context_domain='service_fee', context_operation='price_lookup', reason='parent_typed_request_plan')
                else:
                    resolved = resolve_question_with_context(question, recent_history, locale=locale_decision.effective)''')
edit('app/web_api/server.py', '                        recent_history=recent_history,\n                    )\n                    worker_id', '                        recent_history=recent_history,\n                        request_plan=request_plan,\n                    )\n                    worker_id')
edit('app/web_api/server.py', '                        keyboard_layout_direction=layout_direction,\n                    )', '                        keyboard_layout_direction=layout_direction,\n                        request_plan=request_plan,\n                    )')
edit('app/web_api/server.py', '                log_record = {', '''                contract = next((t.metadata for t in reversed(result.trace) if t.stage == 'conversation_contract'), {})
                actual_plan = contract.get('request_plan') or request_plan
                response['client_turn_id'] = client_turn_id
                response['request_plan'] = actual_plan
                response['conversation_outcome'] = contract.get('outcome', 'delegated_existing_pipeline')
                response['coverage'] = {k: contract.get(k) for k in ('expected_ids', 'returned_ids', 'missing_ids', 'temporal_validity', 'task_outcomes') if k in contract}
                if not response['timed_out']:
                    STORE.complete(client_session_id, client_turn_id, turn['revision'], response, plan=actual_plan)
                response['conversation_state'] = STORE.snapshot(client_session_id)
                log_record = {''')
edit('app/web_api/server.py', '                    "event_type": "chat_exchange",\n                    "exchange_id": exchange_id,\n                    "channel": "web",\n                    "request_id": request_id,\n                    "client_session_id": client_session_id,\n                    "question": question,\n                    "resolved_question": resolved.resolved_question,', '''                    "event_type": "chat_exchange",
                    "exchange_id": exchange_id,
                    "channel": "web",
                    "request_id": request_id,
                    "client_session_id": client_session_id,
                    "client_turn_id": client_turn_id,
                    "conversation_state": response['conversation_state'],
                    "request_plan": actual_plan,
                    "conversation_contract": contract,
                    "question": question,
                    "resolved_question": resolved.resolved_question,''')
edit('app/web_api/server.py', '                self._send_json(response, content_language=(result.language or locale_decision).effective)\n                _write_chat_log_async(log_record)', '''                try:
                    self._send_json(response, content_language=(result.language or locale_decision).effective)
                    STORE.delivery(client_session_id, client_turn_id, 'server_written')
                except (BrokenPipeError, ConnectionResetError, OSError):
                    STORE.delivery(client_session_id, client_turn_id, 'uncertain')
                    log_record['delivery_status'] = 'uncertain'
                    _write_chat_log_async(log_record)
                    return
                log_record['delivery_status'] = 'server_written'
                _write_chat_log_async(log_record)''')

edit('web_chat/app.js', 'let clientSessionId = loadOrCreateSessionId();', 'let clientSessionId = loadOrCreateSessionId();\nlet lastSeenResponseId = "";')
edit('web_chat/app.js', '      answer_language: item.answerLanguage || "",', '      answer_language: item.answerLanguage || "",\n      request_plan: item.requestPlan || null,')
edit('web_chat/app.js', '      client_session_id: clientSessionId,', '      client_session_id: clientSessionId,\n      client_turn_id: makeSessionId(),\n      last_seen_response_id: lastSeenResponseId,')
edit('web_chat/app.js', 'const inputContextExcluded = inputRejected || inputQuality?.applied_action === "warn_and_continue";', 'const inputContextExcluded = inputRejected;')
edit('web_chat/app.js', '      requestId: data.request_id || "",', '      requestId: data.request_id || "",\n      requestPlan: data.request_plan || null,')
edit('web_chat/app.js', '    setStatus(true, copy().localApi);\n  } catch (error)', '    renderMessages();\n    lastSeenResponseId = data.request_id || lastSeenResponseId;\n    setStatus(true, copy().localApi);\n  } catch (error)')
edit('web_chat/app.js', '  clientSessionId = makeSessionId();', '  clientSessionId = makeSessionId();\n  lastSeenResponseId = "";')

edit('app/pipeline/query_signals.py', '    if has_any_signal(query, *_GENERAL_TRANSLATION_TERMS, *_GENERAL_CREATION_TERMS):', '''    # A complete causal/order question can be general even without a glossary term.
    # Domain operations still take precedence over broad syntax.
    if not re.search(r'ราคา|ค่าบริการ|จอง|ว่าง|กติกา|กฎ|แข่ง|ศูนย์|\\b(?:price|fee|book|available|rules?|tournament|studio)\\b', query, re.I) and re.search(r'อะไรเกิดก่อน|อะไรมาก่อน|ทำไม.+(?:ถึง|จึง)|\\b(?:which|what)\\b.+\\b(?:came|comes)\\s+first\\b|\\bwhy\\s+(?:do|does|is|are|can)\\b', query, re.I):
        return True
    if has_any_signal(query, *_GENERAL_TRANSLATION_TERMS, *_GENERAL_CREATION_TERMS):''')
print('Integrated typed dialogue in source, preserving backups.')
