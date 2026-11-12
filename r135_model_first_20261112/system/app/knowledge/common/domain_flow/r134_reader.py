"""R134 plan algorithm, shared R135 index/helpers/renderer/verifier.
Not an independent R134 runtime or an authority bypass.
"""
from .scope import reference_time
from .readers import read,blocked

def plan(engine,category,question,at=None,meaning=None):
    from .source_decisions import plan as source_decision
    scoped=source_decision(engine.index,question,reference_time(at),category)
    if scoped is not None:return scoped
    if meaning is not None and meaning.ambiguous:
        from .meaning_reader import apply
        return apply(engine.index,question,meaning,blocked(category,'meaning_requires_clarification','missing_input'),reference_time(at))
    from .comparison_executor import execute as compare
    comparison=compare(engine.index,category,question,meaning,reference_time(at))
    if comparison is not None:return comparison
    if category=='C04':
        from .precision import ambiguous_game_variants
        ambiguity=ambiguous_game_variants(engine.index,question)
        if ambiguity is not None:return ambiguity
    from .source_operations import native_operation
    native=native_operation(engine.index,category,question,meaning)
    if native is not None:
        if meaning is not None and meaning.operation=='compare':
            native.metadata['operator']='compare'
            if category=='C06' and meaning.facet=='amount':native.metadata.setdefault('comparison_options',{fid:question for fid in native.ids})
        return native
    result=read(engine.index,category,question,reference_time(at))
    if meaning is not None:
        from .meaning_reader import apply
        result=apply(engine.index,question,meaning,result,reference_time(at))
        if meaning.operation=='compare':
            result.metadata['operator']='compare'
            if category=='C06' and meaning.facet=='amount':result.metadata.setdefault('comparison_options',{fid:question for fid in result.ids})
    return result
