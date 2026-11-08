from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system/app/knowledge/common';D=S/'domain_flow'
def edit(path,old,new):
 s=path.read_text('utf8');assert old in s,(path,old[:80]);path.write_text(s.replace(old,new,1),'utf8')
edit(S/'answer.py',"    def answer(self,question,*,locale='th',history=None,at=None,planner=None,_composing=False,_snapshot=None):\n", """    def answer(self,question,*,locale='th',history=None,at=None,planner=None,_composing=False,_snapshot=None):
        if _composing:return self._answer_unified(question,locale=locale,history=history,at=at,planner=planner,_composing=True,_snapshot=_snapshot)
        from .domain_flow.engine import Engine
        from .domain_flow.dialogue_task import resolve,attach
        snapshot=_snapshot if _snapshot is not None else self.store.snapshot()
        if not snapshot.get('release'):return self._answer_unified(question,locale=locale,history=history,at=at,planner=planner,_snapshot=snapshot)
        engine=Engine.from_snapshot(snapshot,cache_key=self.store.path.resolve())
        context=resolve(engine.index,question,history,snapshot['active'])
        self.dialogue_context=context
        from .domain_flow.request_provenance import derived_input
        if context['execution_question']!=question:
            derived_input(context['execution_question'],'r128_delivered_task_resolution',[{'origin':'current_user','text':question},{'origin':'delivered_intent_slots','text':context['execution_question']}],facts_inherited=False,inherited_slots=context['inherited_slots'])
        out=self._answer_unified(context['execution_question'],locale=locale,history=history,at=at,planner=planner,_snapshot=snapshot)
        return attach(out,context) if out is not None else out

    def _answer_unified(self,question,*,locale='th',history=None,at=None,planner=None,_composing=False,_snapshot=None):
""")
edit(S/'dialogue.py',"    if generic_pending:result['flow_pending']=generic_pending", "    if generic_pending:result['flow_pending']=generic_pending\n    if isinstance(art.get('dialogue_task'),dict):result['dialogue_task']=art['dialogue_task']")
edit(D/'integration.py',"        if isinstance(original,str) and original and len(original)<=4000:interpretation_question=original", "        if isinstance(original,str) and original and len(original)<=4000:interpretation_question=original\n        if getattr(reader,'dialogue_context',None):interpretation_question=reader.dialogue_context['execution_question']")
# Preserve all non-overlapping explicit aliases rather than the globally longest label.
edit(D/'index.py',"        top=max(map(len,matches))\n        return list({f['id']:f for s in matches if len(s)==top for f in aliases[s]}.values())", """        spans=[(m.start(),m.end(),s) for s in matches for m in re.finditer(re.escape(s),q)]
        chosen={s for a,b,s in spans if not any(c<=a and b<=d and d-c>b-a for c,d,_ in spans)}
        return list({f['id']:f for s in sorted(chosen) for f in aliases[s]}.values())""")
# The game-definition rule must precede related service/equipment matches.
edit(D/'meaning_review.py',"    elif re.search(r'คืออะไร|", """    elif index.bind('C04',q) and any(index.records.get(f['record_id'],{}).get('kind')=='game' for f in index.bind('C04',q)) and re.search(r'คือ(?:เกม)?อะไร|\\bwhat (?:is|kind of game)\\b',q) and not competing:
        frame=('games','C04','detail','summary');basis='current_game_and_definition_request'
    elif re.search(r'คืออะไร|""")
# Build a policy proposal for any declared policy action, before paying for interpretation.
edit(D/'integration.py',"        proposed=review(interpretation_question", """        from .native_intents import propose
        native=propose(engine.index,interpretation_question)
        proposed=native if native is not None else review(interpretation_question""")
# proposal whitelist for dynamic policy/source-backed operation adapters
edit(D/'integration.py',"            'explicit_catalog_count_request','explicit_offered_game_catalog_request'}:","            'explicit_catalog_count_request','explicit_offered_game_catalog_request','canonical_source_operation'}:")
edit(D/'engine.py',"return [f for _,f in self.index.rank(category,question,pool=pool,limit=8)]", "return [f for _,f in self.index.rank(category,question,pool=pool,limit=24)]")
edit(D/'model.py',"candidates=t['facts'][:8]", "candidates=t['facts'][:24]")
edit(D/'model.py',"'format':output_schema(len(tasks),8)", "'format':output_schema(len(tasks),24)")
# Application source-list exposes private/draft citation descriptors without publishing evidence URLs.
web=R/'system/app/web_api/server.py'
edit(web,"            if metadata.get('common_approved') is not True:\n                continue", "            if metadata.get('common_approved') is not True and metadata.get('content_view') not in {'evaluation_draft','synthetic_demo'}:\n                continue")
edit(web,"source_id = str(metadata.get('title') or 'Approved center information')", "source_id = str(metadata.get('title') or ('Draft center information' if metadata.get('content_view')=='evaluation_draft' else 'Approved center information'))")
print('Core patched')
