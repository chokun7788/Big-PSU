from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/session/task_memory.py',"intent in ('games_lookup','list')","intent in ('games_lookup','list','game_list')")
edit('app/pipeline/user_service_facts.py',"(?:เปลี่ยน|ย้าย).{0,8}เวลา|", "(?:เปลี่ยน|ย้าย).{0,8}เวลา|(?:เปลี่ยน|ย้าย).{0,8}รอบ.*จอง|")
edit('app/pipeline/user_service_facts.py',"('game_account_policy',r'บัญชี|account',r'steam|", "('game_account_policy',r'บัญชี|account|steam.*(?:ตัวเอง|ล็อกอิน|log.?in|own)',r'steam|")
edit('app/pipeline/service_query_completion.py',r'(?:มี)?เกม(?:อะไร|ไร|ไหน|กี่)|มีเกม|(?:เล่นเกมอะไร)',r'(?:มี)?เกม(?:อะไร|ไร|ไหน|กี่)|เกมทั้งหมดกี่|(?:เล่นเกมอะไร)')
edit('app/pipeline/service_query_completion.py',"    if game_list and not re.search(r'ปุ่ม|กฎ|กติกา|แข่ง|ราคา|จ่าย|บัญชี|", "    if game_list and not re.search(r'ติดตั้ง|โหลด|ลงเพิ่ม|ห้าม|ไม่เอา|ปุ่ม|กฎ|กติกา|แข่ง|ราคา|จ่าย|บัญชี|")
# Context for a budget eligibility clarification is anchored in the prior
# request, not a personal profile or a guessed rate.
edit('app/session/context_resolver.py',"    service_followup=resolve_service_fact_followup(original,recent_history,locale)", """    items=_history_dict_items(recent_history)
    if len(items)>=2:
        user,reply=items[-2:]
        from app.session.conversation_plan import customer_filter
        scope,groups=customer_filter(original)
        if (user.get('role')=='user' and reply.get('role')=='assistant'
            and reply.get('route_intent')=='budget_group' and len(groups)==1
            and len(original)<=65
            and all(x.get('context_eligible') is not False and x.get('contextEligible') is not False for x in (user,reply))):
            return ResolvedQuestion(original,str(user.get('text') or '')+' '+original,True,
                context_domain='service_fee',context_operation='affordability',reason='budget_customer_group_slot')
    service_followup=resolve_service_fact_followup(original,recent_history,locale)""")
edit('app/pipeline/engine.py',"        final_validation_started = time.perf_counter()\n        source_validation", """        final_validation_started = time.perf_counter()
        # Editorial cleanup of one identified mixed-language source sentence.
        # Preserve raw source and its unresolved physical-control verification.
        contamination='ขยับทิศทางของตัวละคร بشكلทั่วไป'
        if 'control' in mode and contamination in answer:
            answer=answer.replace(contamination,'ขยับทิศทางของตัวละครทั่วไป')
            trace.append(PipelineTrace('display_editorial_correction','mixed_language_removed',1.0,
                'Thai rendering cleanup; original source unchanged; mapping not verified',
                {'source_row_id':'game_control_ps5_tekken_8_08_move','original_fragment':contamination,'physical_mapping_verified':False}))
        source_validation""")
print('web findings and bounded catalog safeguards fixed')
