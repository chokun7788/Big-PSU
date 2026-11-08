"""Focused diagnostic replay of only 131 CommonAnswerer misses. No code fixes."""
import sys,json,functools,collections,time,hashlib
from pathlib import Path
OUT=Path(__file__).resolve().parent;DATA=OUT.parent
sys.path.insert(0,str(DATA));import experiment as t
from app.knowledge.common import answer as module
def main():
    fails=json.loads((DATA/'content_final/FAILURES.json').read_text(encoding='utf-8'));qs=[r for r in fails if r.get('decision') is None]
    store=t.OneReleaseStore(t.DB).freeze();reader=t.CommonAnswerer(store);fixed=store.frozen['release']['names']
    real_named=module.named;real_seq=module.SequenceMatcher;alias_scores={}
    def observed_seq(*a,**kw):
        seq=real_seq(*a,**kw);span=a[1];alias=a[2]
        class Observed:
            def ratio(self):
                score=seq.ratio()
                if alias not in alias_scores or score>alias_scores[alias]['score']:alias_scores[alias]={'score':score,'span':span}
                return score
        return Observed()
    module.SequenceMatcher=observed_seq
    @functools.lru_cache(maxsize=10000)
    def cached(q):
        ids,method=real_named(q,fixed);return tuple(ids),method
    def named(q,names):
        if names!=fixed:raise RuntimeError('Name map changed')
        ids,method=cached(q);return list(ids),method
    module.named=named
    target_code=reader.answer.__func__.__code__;results=[];buckets=collections.Counter()
    with (OUT/'NONE_ROUTE_REPLAY_V2.jsonl').open('x',encoding='utf-8') as f:
        for n,c in enumerate(qs,1):
            alias_scores.clear();observed={}
            def trace(frame,event,arg):
                if frame.f_code is not target_code:return None
                if event=='return':
                    observed.update(return_line=frame.f_lineno,locals={k:frame.f_locals.get(k) for k in ['q','ids','method','kind','requested','broad']})
                return trace
            sys.settrace(trace)
            try:answer=reader.answer(c['question'],locale=c['lang'],history=c['history'],at=t.AT)
            finally:sys.settrace(None)
            if answer is not None:raise RuntimeError('Diagnostic replay diverged for '+c['id'])
            loc=observed['locals'];reason='unknown_return_branch'
            if not loc['ids'] and loc['kind'] is None:
                reason='followup_history_gate_not_satisfied' if c['style']=='followup' else 'name_unresolved_and_kind_fallback_not_applicable'
            row={'id':c['id'],'question':c['question'],'style':c['style'],'lang':c['lang'],'kind_expected':c['kind'],'record_expected':c['rid'],'history':c['history'],'replayed_none':True,'observed':observed,'diagnostic':reason}
            if c['style']=='name_repeat':
                ranked=[]
                for rid,aliases in fixed.items():
                    available=[(alias_scores[t.normal(a)]['score'],t.normal(a),alias_scores[t.normal(a)]['span']) for a in aliases if t.normal(a) in alias_scores] if hasattr(t,'normal') else [(alias_scores[module.normal(a)]['score'],module.normal(a),alias_scores[module.normal(a)]['span']) for a in aliases if module.normal(a) in alias_scores]
                    if available:
                        score,alias,span=max(available);ranked.append({'record_id':rid,'score':score,'alias':alias,'span':span})
                ranked.sort(key=lambda x:(x['score'],x['record_id']),reverse=True)
                accepted=[x for x in ranked if x['score']>=.88]
                margin=(accepted[0]['score']-accepted[1]['score']) if len(accepted)>1 else None
                row['fuzzy']={'threshold':.88,'margin_required':.06,'accepted_candidates':len(accepted),'best_two_margin':margin,'top5':ranked[:5],'expected_record_score':next((x['score'] for x in ranked if x['record_id']==c['rid']),None),'rejection':'margin_below_0.06' if len(accepted)>1 and margin<.06 else 'no_candidate_above_0.88' if not accepted else 'inspect_original_branch'}
            results.append(row);buckets[reason]+=1;f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
            if n%10==0:print(f'none routes {n}/{len(qs)}',flush=True)
    assert store.still_current(store.frozen)
    with (OUT/'NONE_ROUTE_SUMMARY_V2.json').open('x',encoding='utf-8') as f:json.dump({'queries':len(results),'diagnostics':dict(buckets),'fuzzy_rejections':dict(collections.Counter(r['fuzzy']['rejection'] for r in results if 'fuzzy' in r)),'scope':'Observed original CommonAnswerer return line plus original SequenceMatcher.ratio values; pure name cache only in diagnostic process; no LLM/WordPress/production changes','source_sha256':hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()},f,ensure_ascii=False,indent=2)
    print(json.dumps({'complete':len(results),'diagnostics':dict(buckets)},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
