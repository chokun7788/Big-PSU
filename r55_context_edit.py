from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/session/context_resolver.py','    competition_followup = _resolve_competition_followup(original, recent_history)', '''    # A short replacement station keeps the last user's availability filters.
    # No assistant device list supplies missing time or date slots.
    items = _history_dict_items(recent_history)
    if len(items)>=2:
        user,reply=items[-2:]
        from app.booking.live_status import is_live_booking_question,_resource_scope,_requested_resource_number
        if (user.get('role')=='user' and reply.get('role')=='assistant'
            and all(x.get('context_eligible') is not False and x.get('contextEligible') is not False for x in (user,reply))
            and reply.get('route_intent')=='live_booking_status'
            and re.fullmatch(r'(?:แล้ว|ขอ|และ|what about|and)?\\s*(?:pc|ps5|vr|cockpit|switch)\\s*#?\\s*\\d{1,2}\\s*(?:ล่ะ|ครับ|ค่ะ|please)?[?! ]*',original,re.I)):
            prior=str(reply.get('resolved_text') or user.get('text') or '')
            from app.session.conversation_plan import service_mentions,SERVICE_LABELS
            prior_services=service_mentions(prior);new_services=service_mentions(original)
            if len(prior_services)==len(new_services)==1:
                from app.core.normalization import SERVICE_ALIASES
                aliases=sorted(SERVICE_ALIASES[prior_services[0]],key=len,reverse=True)
                pattern=r'(?:'+ '|'.join(re.escape(a) for a in aliases)+r')\\s*(?:#|เครื่อง|station)?\\s*\\d{1,2}(?!\\d|:)'
                candidate=re.sub(pattern,SERVICE_LABELS[new_services[0]]+' #'+str(_requested_resource_number(original,_resource_scope(original))),prior,count=1,flags=re.I)
                if candidate!=prior:
                    return ResolvedQuestion(original,candidate,True,context_domain='reservation',context_operation='availability_lookup',reason='replacement_station_preserves_user_date_time')
    competition_followup = _resolve_competition_followup(original, recent_history)''')
edit('app/booking/live_status.py','    if window is None or window.is_range or not window.explicit:\n        return window', '''    if window is None or not window.explicit:
        return window
    if window.is_range:
        # User-confirmed occupancy policy: a VR 30-minute visit consumes its
        # enclosing hour. Fee packages remain separate from occupied slots.
        if resources and all(_resource_family(r)=='vr' for r in resources):
            start_hour=int(window.start[:2]);end_hour=int(window.end[:2])
            end_hour+=int(window.end[3:]!='00')
            return TimeWindow(f'{start_hour:02}:00',f'{end_hour:02}:00',explicit=True)
        return window''')
# Period-labelled virtual resources count only for their appropriate period.
edit('app/booking/live_status.py','        if period:\n            period_selected', '''        if not period:
            window=requested_time_window(query,snapshot)
            if window and (not window.end or window.end<='12:00') and window.start<'12:00':period='morning'
            elif window and window.start>='13:00':period='afternoon'
        if period:
            period_selected''')
print('context and VR occupancy updated')
