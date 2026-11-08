"""Two individually inspected queries; no business answers in targets."""
from staged_manual_review import stage_batch
from review_saved_labels_batch007 import add_slots

notes={
245:(
 'One English question requests the genre of the literal game alias Uncharted.',
 'games/detail/genre with target Uncharted expresses exactly that single need.',
 'There is no supplied platform, edition, player count, price or service-time constraint.',
 'No dialogue history is supplied and none is synthesized from the source title.',
 'The short alias is not a request for every franchise edition or permission to play.',
 'Pinned game_detail_uncharted revision8 contains a genre field with mapped-source provenance, while edition remains unknown. Its collection title does not establish every Uncharted edition.',
 'Keep the existing language label; do not insert the genre answer, collection title, platform or claim of current factual verification.'),
247:(
 'The Thai fragment asks who occupies a role, but the role word ends at ผู้จัดกา.',
 'members/role_lookup must request display_name rather than return the role itself.',
 'Preserve ผู้จัดกา as an exact requested_scope quote; no completed role word or person name is supplied by the user.',
 'There is no prior person, team, date or dialogue context to fill in the truncated role.',
 'Mark the incomplete role ambiguous rather than silently completing it to an authoritative person identification.',
 'Pinned member_17d23bd43ffdcfb0 revision5 has separately sourced display_name and ผู้จัดการ/Manager role fields; this is a possible source match, not proof of the intended completion.',
 'No employee name, completed role literal, tenure, authority or business answer is taught.')}

def inverse_role(p):
 t=p['tasks'][0];t['facet']='display_name';t['ambiguous']=True
 add_slots(('requested_scope','ผู้จัดกา'))(p)

if __name__=='__main__':
 stage_batch(notes,{245:['game_detail_uncharted'],247:['member_17d23bd43ffdcfb0']},{247:inverse_role},{245:[('Genre field is mapped source with an explicit factual-review caveat; edition is unknown.','Do not extend collection evidence to the entire franchise.')],247:[('Truncated role does not establish a unique intended role or employee.','Preserve literal scope and ambiguity before identifying a person.')]})
