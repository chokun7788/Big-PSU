"""Plan conservative development moves from pinned individual family reviews.

This does not build a dataset or authorize optimization. Callers must freeze
and enforce the plan and perform the complete semantic-family review separately.
"""
import copy
from pathlib import Path
from .training_contract import ArtifactError,example_sha

def apply_reviewed_family_moves(examples,family_refs,artifacts):
    result=copy.deepcopy(examples);bykey={x['question_key']:x for x in result};seen=set();moves=[]
    if len(bykey)!=len(result):raise ArtifactError('family_plan_duplicate_examples')
    for ref in family_refs:
        group=artifacts.read(ref)
        if group.get('version')!='r135-family-review-v1' or not isinstance(group.get('semantic_rationale'),str) or not group['semantic_rationale'].strip():raise ArtifactError('family_plan_review_required')
        members=group.get('members')
        if not isinstance(members,list) or len(members)<2:raise ArtifactError('family_plan_members_required')
        for m in members:
            key=m.get('question_key')
            if key in seen or key not in bykey:raise ArtifactError('family_plan_duplicate_or_unknown_key')
            seen.add(key);x=bykey[key];original=artifacts.read(m['example_ref']);review=artifacts.read(m['review_ref'])
            if review.get('question_key')!=key or review.get('adjudication_status') not in {'accepted','corrected'}:raise ArtifactError('family_plan_review_identity_mismatch')
            if original.get('question_key')!=key or original.get('raw_question')!=m.get('question') or x.get('raw_question')!=m.get('question') or original.get('family')!=m.get('original_family') or x.get('family')!=m.get('original_family') or original.get('original_families')!=m.get('original_families') or x.get('original_families')!=m.get('original_families') or example_sha(x)!=example_sha(original) or x.get('exposure')!=original.get('exposure') or x['annotation_provenance']['origin_ref']!=original['annotation_provenance']['origin_ref']:raise ArtifactError('family_plan_identity_changed')
            if original.get('split')!=m.get('current_split') or x.get('split')!=m.get('current_split') or m.get('proposed_split')!='development':raise ArtifactError('family_plan_split_invalid')
            origin=x['annotation_provenance']['origin_ref'];artifacts.read(origin);saved=Path(origin['path']).stem
            if saved not in {'train','validation','test'} or (x['split']=='train' and saved!='train'):raise ArtifactError('family_plan_historical_split_invalid')
            if x['split'] not in {'train','development'}:raise ArtifactError('family_plan_current_split_invalid')
            if x['split']=='train':moves.append({'question_key':key,'from':'train','to':'development','saved_split':saved,'family_review_ref':ref})
            x['split']='development'
    artifacts.verify_pinned_files()
    return result,moves
