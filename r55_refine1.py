from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:90]);p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/pipeline/user_service_facts.py',"q,recoveries=recover_service_fact_query(question);en=locale=='en'", """q,recoveries=recover_service_fact_query(question);en=locale=='en'
    if _has(q,r'สลิป|payment slip'):
        candidate=re.sub(r'ผืด','ผิด',q)
        if candidate!=q:recoveries.append(dict(observed='ผืด',intended='ผิด',method='payment_subject_anchored_diacritic_substitution'));q=candidate""")
edit('app/pipeline/service_query_completion.py',"    if is_fee_request(q):return 'fee'", """    if is_fee_request(q) or (re.search(r'เท่าไหร่|เท่าไร|\\b(?:cost|how much)\\b',q,re.I) and re.search(r'เล่น|ชั่วโมง|นาที|\\b(?:play|hours?|minutes?)\\b',q,re.I)):return 'fee'""")
edit('app/pipeline/service_query_completion.py',"    if en and re.search(r'\\b(?:shoot|reload)\\b',q):", """    if (re.search(r'maintenance',q,re.I) or re.fullmatch(r'(?:what (?:are|is) (?:your|the) (?:opening|service|business) hours|opening hours|เปิดกี่โมง ปิดกี่โมง|วันอาทิตย์เปิดไหม)[ ?!.]*',q,re.I)) and not re.search(r'วันนี้|พรุ่งนี้|\\d{4}-\\d{2}-\\d{2}|\\b(?:today|tomorrow)\\b',q,re.I):
        from app.pipeline.protected_intents import _weekly_schedule,RESERVATION_URL
        return _result(_weekly_schedule(locale)+'\\n'+('Source: ' if en else 'แหล่งข้อมูล: ')+RESERVATION_URL,HITS['reservation'],'schedule','schedule_query',dict(basis='regular_service_calendar',not_live=True))
    if en and re.search(r'\\b(?:shoot|reload)\\b',q):""")
edit('app/pipeline/bilingual_english.py',"if re.search(r'\\b'+action+r'\\b',query,re.I)","if re.search(r'\\b'+action+r'\\b',query,re.I)") if False else None
edit('app/pipeline/bilingual_english.py',"else tuple(action for action in ('shoot','reload') if re.search(r'\\b'+action+r'\\b',query,re.I))", "else tuple(term for action,terms in (('shoot',('fire',)),('reload',('reload',))) if re.search(r'\\b'+action+r'\\b',query,re.I) for term in terms)")
edit('app/pipeline/engine.py',"            typed_plan = request_plan or resolve_request_plan(cue_preflight, recent_history, locale=resolved_locale.effective)","""            from app.pipeline.service_query_completion import answer_budget
            budget_result = answer_budget(cue_preflight,resolved_locale.effective)
            if budget_result:
                return self._build_result(budget_result['answer'],budget_result['hits'],started,
                    budget_result['mode'],.98,budget_result['route'],EntityBundle(),budget_result['validation'],
                    [*entry_timings,*budget_result['trace']])
            typed_plan = request_plan or resolve_request_plan(cue_preflight, recent_history, locale=resolved_locale.effective)""")
print('refine loop1 complete')
