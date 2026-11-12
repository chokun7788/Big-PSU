"""Runtime task contracts; owner facts and identities remain in the snapshot."""
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class TaskContract:
    task: str
    kinds: tuple
    fields: tuple
    operation: str = 'read'
    meaning: str = ''

ROWS = [
 ('game_overview',('game',),('summary','genre'),'game_overview','Identify or summarize the game: premise, genre, what kind of game it is or what it is about. Not the actions players perform.'),
 ('game_how_to_play',('game',),('how_to_play',),'game_how_to_play','Explain playing activities, goals, gameplay loop, what players do and how playing works or what it involves. Instructions for playing, not booking or paying.'),
 ('game_platforms',('game',),('supported_platforms',),'read','Platforms supported by the game'),
 ('game_at_studio',('game',),('offered','service_id','installed_resource_ids'),'read','Where this studio offers or installs this game; not live occupancy'),
 ('game_players',('game','game_mode'),('players_min','players_max','mode_name','studio_supported'),'read','Concurrent players and game modes'),
 ('game_controls',('game','control_set'),('bindings',),'read','Buttons/actions/input controls, respecting platform and preset'),
 ('game_account',('game','game_service'),('account_policy_id','details'),'policy','Game account provision/requirements'),
 ('game_version',('game','game_service','control_set'),('game_version',),'read','Installed game version'),
 ('equipment_explain',('equipment_model',),('name','device_type','specifications','usage'),'equipment','What this equipment is and how it is used'),
 ('equipment_specs',('equipment_model','resource','service'),('specifications',),'equipment','Hardware model/specifications'),
 ('equipment_location',('equipment_model',),('name','location'),'equipment','The source-declared zone reached through this model’s physical resource; specifications alone do not prove a location'),
 ('equipment_list',('zone','service','resource','equipment_model'),('name',),'equipment','List physical resources/models linked to a selected zone/service; a zone name itself is not equipment'),
 ('resource_capacity',('resource','service'),('capacity_persons','capacity_min','capacity_max'),'read','Concurrent capacity of the device/service, not room seats'),
 ('service_duration',('service',),('session_minutes','occupancy_minutes'),'read','Play duration versus reserved resource duration'),
 ('center_operator',('center',),('operator',),'read','Who owns/operates the studio'),
 ('center_location',('center',),('address','building','floor','map_url'),'read','Where the studio is; building/floor/map'),
 ('center_overview',('center',),('name','description'),'read','What this studio is and offers'),
 ('contact',('contact',),('purpose','channel','value','office_hours'),'read','Public contact details and response hours'),
 ('facility',('facility',),('name','location','usage_conditions','accessibility'),'read','Parking/rest area and facility conditions'),
 ('people',('person',),('display_name','role','team'),'read','Public staff/team directory'),
 ('audience',('audience',),('name','eligibility','required_proofs'),'read','Audience eligibility and proof'),
 ('price',('zone','service','resource','equipment_model','audience','rate'),('amount_minor',),'price','Fees by service/audience/duration; no invented rate'),
 ('rental',('rental_package','zone','service','resource','equipment_model','audience'),('amount_minor','terms','duration_minutes'),'price','Half/full-day or rental package; not hourly extrapolation'),
 ('policy',('policy','faq'),('answer','decision','conditions_all','exceptions','details','consequence'),'policy','Permission/prohibition with action and conditions'),
 ('procedure',('procedure','faq'),('answer','steps','preconditions','required_documents','outcome'),'booking','Booking/service procedure and prerequisites'),
 ('faq_content',('faq',),('answer',),'read','Answer the matched FAQ; preserve its scope'),
 ('competition_rules',('competition','competition_rule'),('text',),'rules','Rules of the named game/event/edition, including dependencies'),
 ('competition_metadata',('competition',),('event_name','division','rulebook_release','competition_dates'),'read','Event/edition/division/date metadata'),
 ('schedule',('schedule','closure'),('open_periods','bookable_periods','maintenance_periods'),'calendar','Opening/bookability/maintenance at the requested date'),
 ('news',('news',),('title','body','event_start','event_end','registration_url'),'read','Studio news/events/registration'),
 ('live_status',('live_binding','service','resource','zone'),(),'live','Live availability; transport and freshness required'),
]
TASKS = {r[0]:TaskContract(*r) for r in ROWS}
from .registry import CATALOG
TASKS['schema_attributes']=TaskContract('schema_attributes',tuple(CATALOG),(),'read','Explicit typed attributes of a resolved record; deterministic only')

def catalog(kinds=None):
    return [asdict(t) for t in TASKS.values() if t.task!='schema_attributes' and (not kinds or set(t.kinds)&set(kinds))]

def fields_for(task, ids, records):
    """Do not require optional absent fields, but retain related-read needs."""
    from .planner import allowed_schema
    _, allowed, _ = allowed_schema(ids,records)
    return [f for f in TASKS[task].fields if f in allowed]
