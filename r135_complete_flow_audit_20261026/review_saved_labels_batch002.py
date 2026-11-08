"""Individual source adjudications for saved rows20-44, preserving round001.

The explicit decisions below follow reading the raw questions, prior plans and
pinned source fields. They certify neither answer accuracy nor missing facts.
"""
import copy,json
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import *

W=R/'training_review_workbench_1793037663397671000';S=W/'review_round_001';O=W/'review_round_002'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(x) for x in p.read_text('utf8').splitlines() if x.strip()]
def write(name,value):
 p=O/name;p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in value) if name.endswith('.jsonl') else json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf8');return p

notes={
20:(
 'One studio-contact need; both polite verification prefixes are style.',
 'contact/detail/value asks a contact channel, not the physical address.',
 'No named person or particular channel is supplied; keep the target empty.',
 'There is no inherited contact or history to supply a person or department.',
 'No exclusion or competing contact is present; source incompleteness alone is not ambiguity.',
 'contact_studio_facebook records a studio channel and its value; unknown office hours must not be invented.',
 'No URL, account name or office hours is placed in the plan.'),
21:(
 'One tournament-rule question asks how a forfeit score is recorded.',
 'competition_rules/rule_lookup/rule_clause is correct; add the specific score-recording scope.',
 'VALORANT is game target; ปรับแพ้บันทึกคะแนน is the requested rule scope, not a numeric score.',
 'No event year or edition is quoted and none is imported from a source title.',
 'เท่าไร is a question about a result, not an assertion that a particular score applies.',
 'r114_valorant_42_rule_clause explicitly concerns forfeit score recording; 75-77 concern different penalty levels and are not substitutes.',
 'The source score 13-0 is deliberately absent from the label.'),
22:(
 'One broad studio-rules need; concise is style, not a second task.',
 'rules/list/owner_policy preserves the collection request.',
 'No particular game, event or equipment is supplied as target.',
 'The studio scope is current question scope; no tournament context is inherited.',
 'No negative filter or single rule is specified; do not narrow the collection arbitrarily.',
 'migrated_faq_rule_en_general_studio_rules is an actual studio-rules summary, separate from event rule records.',
 'No policy text, permission or penalty is copied into the plan.'),
23:(
 'One food-bringing permission need; briefly is style.',
 'rules/detail/owner_policy is retained; bringing and consuming are different actions.',
 'bring food into the studio is an exact action quote; no consumption action is invented.',
 'The action belongs only to this current studio-policy question.',
 'Can I is an interrogative, not evidence that bringing is allowed.',
 'Pinned food FAQs speak about consumption in designated areas; they do not prove a separate bringing permission.',
 'The label records the requested action only, with no yes/no or designated-area answer.'),
24:(
 'One named-person position request despite the typo มีตแหน่ง.',
 'members/role_lookup/role asks the named person role.',
 'นายชนะชัย สิริพันธ์วราภรณ์ is the complete quoted person target.',
 'No role, team or contact from prior dialogue is available.',
 'A spelling error in the request does not create a competing identity.',
 'member_17d23bd43ffdcfb0 has the exact Thai display name and published role/team fields.',
 'The Manager role remains source output, not part of the supervised plan.'),
25:(
 'One inverse personnel lookup asks who holds the specified role.',
 'Use members/role_lookup/display_name, not facet role, because the requested result is a person.',
 'Web & AI Developer is role target/scope; PSU student is an affiliation condition, not a named person.',
 'Both qualifiers are local to one directory lookup; no preceding person is inherited.',
 'Internship wording must not fabricate a current placement or collapse another developer role into this one.',
 'member_b71d33c7b6468ebc records Cooperative education student: Web & AI Developer with PSU affiliation and a stated period; retain that source wording.',
 'No person name or placement dates are supplied as training targets.'),
26:(
 'One action-to-button lookup for grabbing/lifting.',
 'game_controls/control/input_bindings requests a mapping rather than the full controller list.',
 'Moving Out 2 is full game target; จับ / ยก is the exact requested action.',
 'No platform is quoted; do not insert Nintendo Switch just because the retained layout uses it.',
 'The slash joins the stated action synonyms and does not mean two separate service tasks.',
 'controls_nintendo_moving_out_2 contains Grab / จับ / ยก with several buttons; source platform and combinations stay with the reader.',
 'No L/ZL/R/ZR button answer is taught in the label.'),
27:(
 'One ordinary PS5 play-cost calculation; the typo-bearing polite prefix is style.',
 'service_fee/price_calculate/amount requests total cost for the quoted duration.',
 'บุคคลทั่วไป is audience; PS5 service/platform; 2 ชั่วโมง requested duration, not source billing period.',
 'All price constraints are local; no shared binding or booking action exists.',
 'No person count or session count is specified, so neither is fabricated.',
 'migrated_rate_playstation_5_60_1_2_general_adult is the current general-adult PS5 rate and billing rule.',
 'The stored 15000 minor-unit rate and any calculated total stay out of labels.'),
28:(
 'One catalog query asks which games occur in more than one zone.',
 'games/list/zone plus the quoted หลายโซน filter preserves the requested relation.',
 'No single game is named; do not invent a target from the source catalog.',
 'The multiple-zone qualifier scopes the one game-list task, not a global equipment list.',
 'หลายโซน is a cardinality filter, not an instruction to return every zone or all games.',
 'game_detail_tekken_8 has explicit PC and PS5 studio-zone relations, while game_detail_new_super_mario_bros has only Nintendo; these demonstrate why the filter matters.',
 'No specific game or zone becomes the model answer target.'),
29:(
 'One named-game location question; verification text is style.',
 'games/detail/zone asks studio location, not service price or a booking transaction.',
 'TEKKEN 8 is a game target; remove the erroneous service slot containing the game title.',
 'The named game scopes this location task only; no platform is supplied.',
 'A clear location request remains clear even when more than one recorded zone is returned.',
 'game_detail_tekken_8 explicitly has studio_zone_ids zone_pc and zone_ps5; supported_platforms is unknown and cannot replace studio location.',
 'No source zone name is taught as a generated answer.'),
30:(
 'One complete recorded-controls list for Call of Duty: Warzone.',
 'game_controls/list/input_bindings preserves all the buttons scope.',
 'The full game title and all the buttons quote are retained; no individual action is guessed.',
 'No platform or preset is stated in the input; recorded layout scope stays at execution.',
 'All means the requested list, not proof that the source covers every version or preset.',
 'controls_ps5_call_of_duty_warzone has thirteen recorded entries plus an L1/L2 and R1/R2 swapping note, while version/preset are unknown.',
 'No mapping, button count or unsupported completeness claim enters the plan.'),
31:(
 'One permission request concerns recording video inside the premises.',
 'rules/detail/owner_policy retains studio recording scope, separate from game controls.',
 'record video inside the studio is the exact action quote; no in-game capture subject is invented.',
 'No prior game or subject is supplied to narrow this to gameplay capture.',
 'May I requests permission and cannot be converted into a positive capture permission.',
 'r114_q033_owner_policy has a Thai premises/people question but an answer restricted to in-game capture; preserve this answer-source scope issue.',
 'No permission, deletion requirement or commercial-use policy is taught in the label.'),
32:(
 'One maintenance-window request; visit planning and verified-information prefixes are context/style.',
 'schedule/list/maintenance_periods is appropriate when no particular weekday is supplied.',
 'Maintenance is the requested timetable concept, not an equipment name or literal date.',
 'Do not inherit a day from another question or the training clock.',
 'A weekly list request need not invent a single day merely because some entries have no maintenance.',
 'migrated_schedule_0 through6 explicitly separate maintenance, bookable periods and service slots.',
 'No weekday, interval or open/closed answer is learned.'),
33:(
 'One full binding-list request for God of War Ragnarök.',
 'game_controls/list/input_bindings retains ปุ่มทั้งหมด as list scope.',
 'The accented game title stays exactly as quoted; no platform is fabricated.',
 'No prior preset or controller is available in the saved input.',
 'All buttons does not authorize dropping modifier combinations or claiming unknown version completeness.',
 'controls_ps5_god_of_war_ragnar_k contains recorded PS5 actions and a modifier note for L1/L2; source spelling differs without changing the raw target.',
 'No button mappings, modifier answers or recorded entry count is supervised.'),
34:(
 'One Tuesday opening-time request despite typo อพดี.',
 'schedule/detail/open_periods is the available opening-period facet; closing_time would reverse the request.',
 'วันอังคาร remains an exact date/weekday constraint, not an absolute date.',
 'The weekday is local to one timetable task; no visit date is imported.',
 'A clear question does not become language ambiguity because the source has conflicting opening fields.',
 'migrated_schedule_1 retains conflicted open_periods with separate known service_slots/bookable_periods; source authority must resolve or display that distinction.',
 'No 09:00 value or inferred authoritative opening interval enters the target.'),
35:(
 'One temporary suspension policy request; visit-planning wording is not another need.',
 'rules/detail/owner_policy is retained, adding the exact requested penalty scope.',
 'ระงับสิทธิ์ชั่วคราว must stay distinct from permanent suspension and ordinary equipment faults.',
 'No current alleged violation, actor, cause or prior sanction is asserted.',
 'Asking for information does not admit a violation or imply any sanction applies to this user.',
 'migrated_faq_curated_penalty_temp_suspension specifies temporary suspension and conditions; the permanent suspension FAQ is a separate policy.',
 'No duration range, sanction or violation judgment is taught.'),
36:(
 'One VR ordinary-play price request for an adult for one hour.',
 'service_fee/price_calculate/amount preserves the calculation need.',
 'adult is audience; one hour is requested duration; VR is service, not a game title.',
 'All quotes are local to this one calculation.',
 'No number of people or sessions is explicit; do not substitute the source 1-5 capacity for a user count.',
 'migrated_rate_vr_60_1_5_general_adult binds the sixty-minute VR service, general-adult audience and session_ceil rule.',
 'No amount_minor value or computed total enters the plan.'),
37:(
 'One gaming-mouse inventory/presence request; the visit-planning prefix is style.',
 'equipment/detail/name asks whether the named device is recorded, not its specifications.',
 'Preserve the full typo-bearing target เมาส์เกใมิ่ง rather than silently losing the gaming qualifier.',
 'No PC station or quantity is supplied locally or in history.',
 'The recognizable typo does not prove any physical quantity or live availability.',
 'equipment_gaming_mouse records Gaming Mouse and PC Zone use; it does not supply a current live inventory count.',
 'No yes/no, quantity or mouse specifications are added to targets.'),
38:(
 'One VALORANT competition-penalties collection request despite the leading typo.',
 'competition_rules/list/rule_clause preserves the penalties collection.',
 'บทลงโทษ is requested_scope; the whole sentence should not be mislabeled as a condition.',
 'VALORANT scopes this rule task; no particular event edition is quoted.',
 'Wanting to compete is context and not an admission of cheating or a cause for a specific penalty.',
 'r114_valorant_75/76/77 distinguish round loss, map forfeit and match forfeit under different causes; the collection must retain these distinctions.',
 'No penalty, exception or misconduct ruling enters the model target.'),
39:(
 'The fragment ขอข้อมูลเรื่องพบปัญหา เครื่อง leaves the requested information incomplete.',
 'Use general/unknown with ambiguity, rather than guessing equipment/usage.',
 'No particular machine, problem, action or desired remedy is stated.',
 'There is no previous machine or incident in the saved context to complete the fragment.',
 'The ambiguous flag reflects the absent referent/need; do not invent damage cause or compensation.',
 'No exact source clause is established by this fragment; named equipment presence would not resolve the intended problem.',
 'No troubleshooting step, liability, policy or permission is fabricated.'),
40:(
 'One location request for New Super Mario Bros. U Deluxe.',
 'games/detail/zone asks studio zone; no service-fee or reservation operation exists.',
 'Retain the full game target and remove its erroneous service constraint.',
 'No platform is quoted or inherited from history.',
 'Clear named-game location is not player-count or game-description intent.',
 'game_detail_new_super_mario_bros explicitly relates the title to zone_nintendo; its player-description footnote cannot alter the location label.',
 'No Nintendo zone answer or player count enters the model target.'),
41:(
 'One Friday maintenance-information request.',
 'schedule/detail/maintenance_periods keeps maintenance distinct from opening periods.',
 'วันศุกร์ is an exact weekday constraint; maintenance is the requested facet.',
 'The weekday scopes this current task only and does not borrow a calendar date.',
 'No all-day closure is asserted by the user phrase.',
 'migrated_schedule_4 records afternoon maintenance separately from its morning bookable period.',
 'No 13:00-16:00 interval or closed/open conclusion is supervised.'),
42:(
 'One current resource-availability request at a quoted time; verified-information text is style.',
 'live/availability/live_status is retained rather than general opening hours.',
 'pc2 is the explicit resource target omitted by the old label; 3pm remains the exact time quote.',
 'Resource and time belong to one availability task; no date is inherited.',
 'Availability is a question; a future time without date does not establish a real booking or free machine.',
 'resource_pc_02 establishes the named resource identity only; its operational_status is unknown and no live reservation evidence is fabricated.',
 'No free/busy status, calendar date or slot availability enters the plan.'),
43:(
 'One named-person position request.',
 'members/role_lookup/role correctly asks for a role rather than inverse person lookup.',
 'Ms. Kamlawan Nuansai remains the exact raw target, not a normalized replacement.',
 'No other member from saved or imagined dialogue may supply the answer.',
 'A transliteration difference does not justify inventing a different identity or role.',
 'member_18a751d710b9b30c has Thai name กมลวรรณ นวลสาย and alias Miss Kamolwan Nuansai; raw Kamlawan spelling is preserved for reader disambiguation.',
 'No Committee member answer or private contact is learned.'),
44:(
 'One physical-location request despite typo-bearing polite text.',
 'contact/detail/address asks where the studio is, not how to message it.',
 'No separate building/floor-only need is requested, so the target remains empty.',
 'The studio is the current question subject; no named person or earlier location is inherited.',
 'The informal suffix อะ is not ambiguity or a second requested action.',
 'center_psu_phuket and migrated_owner_claim_location include Building5/Floor1 and address; legacy address FAQs are less specific, so current source authority stays with execution.',
 'No building number, postal address or map URL enters the planner label.'),
}
ids={20:['contact_studio_facebook'],21:['r114_valorant_42_rule_clause'],22:['migrated_faq_rule_en_general_studio_rules'],23:['migrated_faq_curated_rule_food_drinks','migrated_faq_rule_food_drink'],24:['member_17d23bd43ffdcfb0'],25:['member_b71d33c7b6468ebc'],26:['controls_nintendo_moving_out_2'],27:['migrated_rate_playstation_5_60_1_2_general_adult'],28:['game_detail_tekken_8','game_detail_new_super_mario_bros'],29:['game_detail_tekken_8'],30:['controls_ps5_call_of_duty_warzone'],31:['r114_q033_owner_policy'],32:['migrated_schedule_'+str(i) for i in range(7)],33:['controls_ps5_god_of_war_ragnar_k'],34:['migrated_schedule_1'],35:['migrated_faq_curated_penalty_temp_suspension','migrated_faq_curated_penalty_permanent_suspension'],36:['migrated_rate_vr_60_1_5_general_adult'],37:['equipment_gaming_mouse'],38:['r114_valorant_'+str(i)+'_rule_clause' for i in [75,76,77]],39:[],40:['game_detail_new_super_mario_bros'],41:['migrated_schedule_4'],42:['resource_pc_02'],43:['member_18a751d710b9b30c'],44:['center_psu_phuket','migrated_owner_claim_location','migrated_faq_rule_contact_location']}
source_issues={
23:('Food source speaks about consumption rather than a separate bringing permission.','Do not infer bringing permission from consumption or teach it in the planner label.'),
31:('The retained Thai premises/people recording question is paired with an answer restricted to in-game capture.','Preserve premises action in the label and keep answer-source scope review pending.'),
34:('open_periods is conflicted while service_slots and bookable_periods are separately known.','Do not train a selected authoritative opening time; preserve source authority/conflict handling at execution.'),
43:('The raw English name Kamlawan differs from the recorded English alias Kamolwan.','Keep the exact raw person span; do not teach an unverified identity substitution or role answer.'),
}

if __name__=='__main__':
 O.mkdir(exist_ok=False);source=read(W/'SOURCE_SNAPSHOT.json');source_ref=read(W/'SOURCE_REF.json');source_sha=digest(source_identity(source));examples=rows(S/'EXAMPLES.jsonl');reviews=rows(S/'REVIEWS.jsonl');index=read(S/'REVIEW_INDEX.json');lookup={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in examples}
 tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');runtime=runtime_contract(read(tokenizer),chat_template=tokenizer.with_name('chat_template.jinja').read_text('utf8'),model_profile=read(W/'DECLARED_MODEL_PROFILE.json'));write('RUNTIME_CONTRACT.json',runtime)
 for i,reasons in notes.items():
  x=lookup[i];prior=copy.deepcopy(x['plan_label']);p=x['plan_label'];t=p['tasks'][0]
  def slot(kind,quote):t['constraints'].append({'slot':kind,'quote':quote,'source_record_id':'','scope':'local'})
  if i==21:slot('requested_scope','ปรับแพ้บันทึกคะแนน')
  if i==23:slot('action','bring food into the studio')
  if i==25:
   t.update(facet='display_name',target='Web & AI Developer');slot('requested_scope','Web & AI Developer');slot('condition','PSU student')
  if i==26:slot('action','จับ / ยก')
  if i in [29,40]:t['constraints']=[c for c in t['constraints'] if c['slot']!='service']
  if i==31:slot('action','record video inside the studio')
  if i==35:slot('requested_scope','ระงับสิทธิ์ชั่วคราว')
  if i==37:t['target']='เมาส์เกใมิ่ง'
  if i==38:
   t['constraints']=[];slot('requested_scope','บทลงโทษ');p['context_quotes']=['VALORANT','บทลงโทษ']
  if i==39:p['focus']='unclear';t.update(domain='general',operation='unknown',facet='',target='',constraints=[],ambiguous=True)
  if i==42:t['target']='pc2'
  x['annotation_provenance'].update(method='manual_review_of_saved_question',runtime_contract_sha256=digest(runtime));x['messages']=messages(x['raw_question'])+[{'role':'assistant','content':json.dumps(p,ensure_ascii=False,separators=(',',':'))}]
  decision='accepted' if prior==p else 'corrected';reviewer={'id':'Codex-primary-agent-R135-source-adjudication','kind':'agent'};assert all(k in source['release']['records'] for k in ids[i]);issues=[{'scope':'answer_source','reason':source_issues[i][0],'handling':source_issues[i][1]}] if i in source_issues else []
  criteria={name:{'status':'passed','reason':reason,'raw_quotes':[x['raw_question']],'source_record_ids':ids[i] if name=='source_version_alignment' else []} for name,reason in zip(CRITERIA,reasons)}
  evidence={'question_key':x['question_key'],'example_sha256':example_sha(x),'adjudication_status':decision,'reviewer':reviewer,'source_identity_sha256':source_sha,'criteria':criteria,'unresolved_issues':issues,'historical_review_row':i,'prior_label':prior,'reviewed_label':p,'review_scope':'language plan only; not answer accuracy','source_field_evidence':{rid:{'revision':source['release']['records'][rid]['revision'],'record_sha256':digest(source['release']['records'][rid])} for rid in ids[i]}}
  path=write('ADJUDICATION_'+str(i).zfill(3)+'.json',evidence);reviews.append({'version':VERSION,'question_key':x['question_key'],'example_sha256':example_sha(x),'adjudication_status':decision,'reviewer':reviewer,'review_method':'individual_source_adjudication','source_version':source_ref,'adjudication_ref':{'path':str(path.resolve()),'sha256':file_sha(path)},'teacher_status':'not_applicable','teacher_trace_refs':[],'unresolved_issues':issues});index.append({'row':i,'question_key':x['question_key'],'decision':decision,'changed_label':prior!=p,'source_record_ids':ids[i]})
 # Round001 predates the final gate implementation hash. Repacking its unchanged
 # semantics does not create another adjudication; the current runtime is gated.
 for x in examples:
  reviewed=next((v for v in reviews if v['question_key']==x['question_key']),None)
  if reviewed:
   before=example_sha(x);x['annotation_provenance']['runtime_contract_sha256']=digest(runtime);x['messages']=messages(x['raw_question'])+[{'role':'assistant','content':json.dumps(x['plan_label'],ensure_ascii=False,separators=(',',':'))}];assert example_sha(x)==before==reviewed['example_sha256']
 write('EXAMPLES.jsonl',examples);write('REVIEWS.jsonl',reviews);write('REVIEW_INDEX.json',index)
 inventory=read(W/'INVENTORY.json');report=prepare_dataset(O/'admission_bundle',examples,reviews,Artifacts(R.parent),source_ref,runtime,expected_keys=inventory['question_keys'],known_exposed=inventory['known_exposed_question_keys']);bad=[x for x in report['rows'] if x.get('adjudication_status') and not x['eligible']];assert len(reviews)==46 and sum(x['eligible'] for x in report['rows'])==46,bad
 summary={'individually_adjudicated':46,'new_adjudications':25,'accepted':sum(x['decision']=='accepted' for x in index),'corrected_or_enriched':sum(x['decision']=='corrected' for x in index),'unreviewed':243,'total_original_inventory':289,'prior_adjudications_unchanged':reviews[:21]==rows(S/'REVIEWS.jsonl'),'training_ready':report['ready_for_optimization'],'source_answer_issues_remain':5,'new_model_inferences':0,'optimizer_started':False,'historical_files_modified':False,'complete':False};write('SUMMARY.json',summary);print(json.dumps({'output':str(O),**summary}))
