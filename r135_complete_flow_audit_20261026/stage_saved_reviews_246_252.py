"""Four individually source-read labels; no model calls or cohort admission."""
from staged_manual_review import stage_batch
from review_saved_labels_batch007 import add_slots

notes={
246:(
 'One request asks for rulebook evidence about TEKKEN 8 competition format; politeness is presentation.',
 'competition_rules/rule_lookup/rule_clause retains a competition-specific source lookup, not device specifications or studio rules.',
 'Preserve compettition format as the exact requested_scope and official as a requested source-authority qualifier.',
 'No actual platform, match format, player count, duration or earlier rulebook identity is supplied by the question.',
 'The word official asks for authority verification; it does not certify the authority of a retrieved record.',
 'Pinned TEKKEN8 section002 revision5 explicitly maps competition_format and records offline, PS5, singles and format clauses; completeness and dependencies remain unknown.',
 'No source format values, round counts, tie outcome, authority verdict or equipment fact enters the language target.'),
248:(
 'One conditional question asks liability if a Cockpit wheel breaks; verified-source framing is style.',
 'rules/detail/owner_policy with damage focus is a responsibility question, not a separate equipment-usage lookup.',
 'Keep the literal if-clause locally and add Cockpit wheel plus responsible as the device and responsibility scopes.',
 'Remove the duplicated top-level context quote; no prior cause, negligence, repair quote, damage severity or actual incident is supplied.',
 'The hypothetical breakage does not prove user fault, a specific fine, or permission to charge the user.',
 'Pinned damage_responsibility revision6 explicitly preserves Thai/English liability-condition differences: English limits to improper/negligent use while Thai does not state that restriction. A wheel-specific cause is unproven.',
 'No penalty amount, liability decision, inferred negligence, payment obligation or compensating business answer is taught.'),
250:(
 'One Thai question asks the function of the explicitly named L (Left Stick) in Super Mario Odyssey on Nintendo Switch.',
 'game_controls/control/input_bindings is one game-specific control lookup; the named controller part does not add equipment usage.',
 'Retain the supplied platform and add the full exact L (Left Stick) scope rather than collapsing it to L.',
 'Remove the duplicated top-level platform context; no second task, game edition, controller preset or history is supplied.',
 'Do not confuse stick movement with L shoulder, stick click, R or R3; the wording does not supply a click gesture.',
 'Pinned controls_nintendo_super_mario_odyssey revision6 has an explicit L (Left Stick) binding separate from R and R3; game version, input_device and preset remain unknown and coverage needs manual verification.',
 'No movement answer, fabricated click gesture, preset, edition or source-verification verdict enters the language label.'),
252:(
 'One English question asks whether Friday afternoon is open; verified stuudio information is a style/source request.',
 'schedule/detail/open_periods with opening_hours focus retains the requested opening predicate rather than substituting bookable periods or live occupancy.',
 'Keep Friday as the weekday constraint and add afternoon as an exact local time scope.',
 'Remove duplicated top-level Friday context; do not invent a calendar date, timezone from the user, clock time or prior booking.',
 'An opening query is not an assertion that the whole Friday is closed or that a service slot is available.',
 'Pinned migrated_schedule_4 revision4 has morning bookable periods, afternoon maintenance and service slots, but physical open_periods is unknown; service_closed false does not prove afternoon physical access.',
 'No hours, open/closed verdict, permission to enter, date conversion or availability conclusion is taught.')}

def local_only(*pairs):
 def apply(p):
  p['context_quotes']=[];add_slots(*pairs)(p)
 return apply

ids={246:['competition_competition_rules_tekken8_psu_esports_section_002'],248:['migrated_faq_rule_damage_responsibility'],250:['controls_nintendo_super_mario_odyssey'],252:['migrated_schedule_4']}
edits={246:add_slots(('requested_scope','compettition format'),('requested_scope','official')),248:local_only(('requested_scope','Cockpit wheel'),('requested_scope','responsible')),250:local_only(('requested_scope','L (Left Stick)')),252:local_only(('time','afternoon'))}
issues={246:[('Competition-format content does not certify official authority or complete rulebook coverage.','Preserve requested authority and format scope; verify actual authority separately.')],248:[('Source locales differ on liability conditions; a hypothetical wheel failure does not establish negligence.','Keep local conditional scope and unresolved source conflict.')],250:[('Controller labels are specific and recorded source coverage needs manual verification.','Match full stick label; do not add click or current-version certainty.')],252:[('Bookable and maintenance slots do not fill unknown physical open_periods.','Preserve afternoon predicate and unknown physical-access conclusion.')]}
if __name__=='__main__':stage_batch(notes,ids,edits,issues)
