from pathlib import Path
R=Path(__file__).resolve().parent;D=R/'system/app/knowledge/common/domain_flow'
def edit(name,old,new):
 p=D/name;s=p.read_text('utf8');assert old in s,(name,old[:70]);p.write_text(s.replace(old,new,1),'utf8')
edit('capabilities.py',"    if category=='C06' and operation=='compare' and facet=='duration_minutes':", "    if category=='C06' and operation=='compare' and facet=='amount':allowed=True;canonical='compare_services'\n    if category=='C04' and operation=='list' and facet=='players_max':allowed=True;canonical='filter_game_modes'\n    if category=='C06' and operation=='compare' and facet=='duration_minutes':")
edit('financial.py',"    if not groups or len(groups)<2:return None", "    if not groups or len(groups)<2 or not re.search(r'\\d+\\s*(?:คน|people|persons?|players?)',q):return None")
edit('financial.py',"    groups,denied=audience_mentions(index,q)", """    groups,denied=audience_mentions(index,q)
    if not groups and re.search(r'คนนอก|บุคคลภายนอก|external (?:visitor|user)|outsider',q,re.I):
        groups={rid for rid,r in records.items() if r['kind']=='audience' and re.search(r'general|ต่างสถาบัน|บุคคลทั่วไป', ' '.join(_labels(r)),re.I) and not re.search(r'organization|หน่วยงาน',' '.join(_labels(r)),re.I)}""")
edit('native_intents.py',"    for cat,domain in", """    if index.bind('C13',q) and re.search(r'ลงโทษ|penalt|punishment|sanction',q,re.I):
        return Understanding([MeaningTask(question,'competition_rules','C13','rule_lookup','rule_clause')],True,'canonical_rule_family',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'เกม.*(?:พร้อมกัน|เล่นด้วยกัน|เล่นได้|เล่นกับเพื่อน)|games?.*(?:players|people|together)',q,re.I) and re.search(r'\\d+\\s*(?:คน|players|people)',q,re.I):
        return Understanding([MeaningTask(question,'games','C04','list' if not index.bind('C04',q) else 'detail','players_max')],True,'canonical_game_mode',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'มีอุปกรณ์อะไร|อุปกรณ์.*บ้าง|มีของอะไร.*(?:เตรียม|ให้ใช้)|what equipment|which devices',q,re.I):
        return Understanding([MeaningTask(question,'equipment','C03','list','name')],True,'canonical_inventory',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    for cat,domain in""")
edit('distilled_policy.py',"r'บทลงโทษ|penalt(?:y|ies)|punishments?|sanctions?'", "r'บทลงโทษ|ลงโทษ.*(?:อะไรบ้าง|อย่างไร)|penalt(?:y|ies)|punishments?|sanctions?'")
# Native modes are evaluated as player counts, never resource/room capacities.
edit('engine.py',"        result=read(self.index,category,question,reference_time(at))", """        from .source_operations import native_operation
        native=native_operation(self.index,category,question,meaning)
        if native is not None:return native
        result=read(self.index,category,question,reference_time(at))""")
# All exact-source equipment definition fields participate in projection.
edit('meaning_reader.py',"    if cat in {'C01','C03','C04','C14'} and pool:", """    if cat=='C03' and re.search(r'คืออะไร|\\bwhat is\\b',question,re.I):
        models={f['record_id'] for f in pool if index.records.get(f['record_id'],{}).get('kind')=='equipment_model'}
        fields={'usage','device_type','quantity','location'}
        selected=[f for rid in models for f in index.byrecord[rid] if f['facet'] in fields]
        if selected:return confirmed(cat,selected,'equipment_definition_card',operator='detail')
    if cat in {'C01','C03','C04','C14'} and pool:""")
print('Operations patched')
