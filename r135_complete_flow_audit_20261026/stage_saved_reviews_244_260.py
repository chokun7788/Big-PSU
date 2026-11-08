"""Seven source/intent reviews; source gaps remain explicit."""
from staged_manual_review import stage_batch
from review_saved_labels_batch007 import add_slots
notes={
244:(
 'One Valorant rule query coordinates player conduct and sportsmanship; please/explain are style.',
 'Keep competition_rules/rule_lookup/rule_clause targeted to Valorant rather than general studio conduct or CS2.',
 'Add player conduct and sportsmanship as literal requested scopes under one rule purpose.',
 'No player, incident, penalty, tournament date or prior rulebook context is supplied.',
 'Verify asks for evidence and does not assert that a conduct rule or sportsmanship definition exists.',
 'Actual Valorant section014 revision4 records serious misconduct as a map-forfeit condition; that is not a complete sportsmanship definition. The explicit sportsmanship clause found in CS2 section036 belongs to another competition and cannot fill this gap.',
 'No CS2 conduct content, Valorant permission, definition, penalty amount or source-completeness claim enters the label.'),
249:(
 'One price comparison requests VR for either one hour or two hours for a PSU studenr.',
 'service_fee/compare/amount retains alternatives rather than adding the two durations or converting the question to a booking.',
 'Existing exact duration/service/audience quotes preserve the typo and both alternatives; no invented corrected quote is needed.',
 'Remove duplicated top-level duration/service context. No number of persons, booking product, date or history is supplied.',
 'Two hours is requested use duration, not proof that a two-hour product exists or that rates are linear.',
 'Pinned VR30/VR60 PSU student-staff rate records revision2 use session_ceil with person bands; source service records distinguish session durations. No explicit two-hour product or party size is supplied by the question.',
 'No zero price, default party count, chosen product, free-use entitlement or computed total is taught.'),
251:(
 'One Thai inventory question asks what VR Zone has available to use; doubled บ is a typo, not another need.',
 'equipment/list/name with VR Zone target is the inventory purpose, not games, prices or equipment instructions.',
 'No capacity, room seats, current occupancy, exact device model or rental package is requested.',
 'No prior service session, game edition, party size or live status is inherited.',
 'Inventory wording does not promise that a listed device is currently unoccupied or working.',
 'Pinned home-equipment VR Zone FAQ revision2 names the local device inventory; zone_vr revision2 has unknown room seats/location. Neither source is a live-availability feed.',
 'Keep the existing label; no device names, quantities, seats, prices or current availability answers enter it.'),
253:(
 'One CS2 rule lookup asks for before-match and on-site requirements; polite introduction is not another task.',
 'competition_rules/rule_lookup/rule_clause retains CS2 and the combined preparation/on-site purpose.',
 'Add exact ข้อกำหนดก่อนแข่ง and หน้างาน scopes rather than a generic whole-rulebook retrieval.',
 'No player count, arrival time, team roster, device, document or competition date is supplied by the user.',
 'The question does not authorize entry, certify registration or establish a breach.',
 'Actual CS2 sections049-053 distinguish venue heading, prep personnel, prohibited electronics, document exception and refreshments; source facets are mixed, so matching only primary eligibility_registration or only pre_match_on_site cannot prove complete coverage.',
 'No six-player limit, exception, device prohibition, drink permission, arrival deadline or source answer is taught.'),
254:(
 'One Thai question asks how to use a controller in Fortnite.',
 'game_controls/list/input_bindings keeps a game-specific control request, without adding general equipment usage.',
 'Add exact จอย as the requested input-device scope; the protocol has no input_device slot, so requested_scope preserves the literal.',
 'No PS5, Xbox, preset, custom layout, game version, button or dialogue history is supplied.',
 'A generic controller question cannot certify a platform or default binding layout from the only available source.',
 'Pinned controls_ps5_fortnite revision7 is PlayStation-specific partial_official evidence about menu/preset selection, explicitly not detailed layouts for every preset; input_device, game_version and preset fields are unknown.',
 'No invented platform quote, full-layout claim, preset choice or button-action business answer is taught.'),
256:(
 'One general language-writing request asks for two polite thank-you sentences; the second politeness phrase is a repeated style modifier.',
 'general/detail with empty facet and target remains a single writing request outside studio factual lookup.',
 'The complete task quote retains the two-sentence output requirement; it is not two persons, sessions, monetary units or a source fact.',
 'No studio record, recipient identity, purchase, event, prior dialogue or factual assertion is supplied.',
 'Writing a thank-you sample does not authorize sending a message to anyone.',
 'No owner source is needed or supplied for this language-only request; do not fabricate a business citation, source trace or verified studio fact.',
 'Keep the existing language label; no generated thank-you answer, outbound message, policy or fabricated source is taught.'),
260:(
 'One CS2 tournament-rule query asks permission to change three named settings and the allowed location of those changes.',
 'competition_rules/rule_lookup/rule_clause retains one compound rule purpose; Resolution is a display-setting noun here, not dispute resolution.',
 'Add Brightness, Resolution, Crosshair, may I change and where as exact requested scopes to preserve every predicate.',
 'No actual setting values, device model, prior dispute, operating-system permission or date is supplied.',
 'The permission question does not assert that modifications are allowed in every application or outside the game.',
 'Actual CS2 section045 revision4 explicitly restricts these three settings to game/computer-screen scope, but its primary facet is eligibility_registration; that mapping cannot stand as independent semantic proof of correct settings retrieval.',
 'No yes/no permission, setting values, allowed-location answer, dispute procedure or source authority verdict is taught.')}
def clear(p):p['context_quotes']=[]
ids={244:['competition_competition_rules_valorant_psu_phuket_2026_section_014','competition_competition_rules_cs2_psu_phuket_2026_section_036'],249:['migrated_rate_vr_30_1_5_psu_student_staff','migrated_rate_vr_60_1_5_psu_student_staff','availability_vr_30','availability_vr_60'],251:['migrated_faq_curated_home_equipment_vr_zone','zone_vr'],253:[f'competition_competition_rules_cs2_psu_phuket_2026_section_{n:03d}' for n in range(49,54)],254:['controls_ps5_fortnite'],256:[],260:['competition_competition_rules_cs2_psu_phuket_2026_section_045']}
edits={244:add_slots(('requested_scope','player conduct'),('requested_scope','sportsmanship')),249:clear,253:add_slots(('requested_scope','ข้อกำหนดก่อนแข่ง'),('requested_scope','หน้างาน')),254:add_slots(('requested_scope','จอย')),260:add_slots(('requested_scope','Brightness'),('requested_scope','Resolution'),('requested_scope','Crosshair'),('requested_scope','may I change'),('requested_scope','where'))}
issues={244:[('Misconduct penalty is not a full sportsmanship rule; explicit CS2 conduct is cross-competition evidence.','Keep Valorant source gaps and reject cross-title substitution.')],249:[('Duration alternatives are not additive and party size/product choice is unspecified.','Keep both alternatives and source-specific calculation obligations.')],251:[('Static inventory does not establish current resource availability or room seats.','Keep inventory separate from live and capacity.')],253:[('Related on-site clauses have mixed source facet mappings.','Read source section ordering and completeness independently of primary facet tags.')],254:[('Only partial PlayStation menu/preset information is recorded.','Disclose source/platform limits instead of inventing a complete controller layout.')],256:[('Language-only request has no owner business source requirement.','Do not forge source or imply the generated text was sent.')],260:[('Actual settings clause has a misleading primary eligibility facet.','Verify exact clause and predicate scope; do not substitute dispute-resolution evidence.')]}
if __name__=='__main__':stage_batch(notes,ids,edits,issues)
