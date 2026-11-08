"""Preserve model proposals; write source-compared, agent-revised copies."""
import json,hashlib,copy,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.translation import validate_translation
src=B/'CONTROL_NOTE_PROPOSALS';out=B/'CONTROL_NOTE_REVIEWED';assert not out.exists();assert json.loads((src/'COMPLETE.json').read_text())['notes']==390
FIXES={
'controls_nintendo_animal_crossing_new_horizons':{
5:'Pick up an item from the ground.',6:'Open the tool wheel to select a tool quickly.',7:'Switch to another tool in your pockets by cycling left or right.',8:'Immediately put the tool you are holding back into your pockets.',9:'Open the applications on the NookPhone.'},
'controls_nintendo_luigi_s_mansion_3':{
2:'Summon, switch to, or put away Gooigi, a jelly-like companion who helps solve puzzles.',5:'Shine a special light to reveal hidden, invisible, or cursed objects.',6:"Shoot a plunger onto an object or a ghost's shield, then use the vacuum to pull it and break obstacles."},
'controls_nintendo_super_smash_bros_ultimate':{
5:'Raise a shield to block attacks; combine it with the left stick to dodge-roll.',6:'Grab an opponent to throw them; this is effective against opponents who are shielding.'},
'controls_nintendo_the_legend_of_zelda_breath_of_the_wild':{
0:'Control walking, or sidestep while locked onto a target.',5:'Put away your weapon, or hold to run using the stamina gauge.',10:'Whistle to call your horse so it runs toward you.',15:'Open the Sheikah map to check your route.'},
'controls_pc_counter_strike_2':{0:'W moves forward, A moves left, S moves backward, and D moves right.',14:'Y opens global chat; U opens team chat.'},
'controls_pc_league_of_legends':{0:'Right-click to move or command an attack on a target.',7:'Hold to make the camera follow your champion.'},
'controls_pc_pubg_battlegrounds':{3:'Lie prone.',13:'Holster the weapon you are holding.'},
'controls_pc_valorant':{0:'W moves forward, A moves left, S moves backward, and D moves right.',8:'Use the Spike, such as planting or defusing it, depending on the situation.'},
'controls_ps5_call_of_duty_warzone':{9:'Raise the weapon to aim down its sights.',10:'Pull the trigger to fire the weapon.',12:'Strike with the butt of the weapon.'},
'controls_ps5_ea_sports_fc_24':{
1:'Lob the ball overhead, cross from the wing, or make a headed clearance.',3:'Shoot at goal, head the ball toward goal, or volley.',9:'Hold to jockey when defending, or shield the ball while dribbling.',10:'Hold to push the ball forward and sprint at maximum speed.'},
'controls_ps5_gran_turismo_7':{5:'Pull the handbrake to slide or drift.'},
'controls_ps5_hogwarts_legacy':{8:'Activate the Protego shield to defend against attacks; hold to counterattack with Stupefy.',9:'Roll to dodge attacks that cannot be parried, indicated by a red warning.',15:'Drink a healing potion (Wiggenweld Potion).'},
'controls_ps5_it_takes_two':{10:'Use a grappling hook to swing across designated points in the scene.'},
'controls_ps5_marvel_s_spider_man_2':{1:'Perch on a narrow point, or dive toward the ground while in mid-air.'},
'controls_ps5_monster_hunter_rise':{4:'Hold to sprint; this is available when your weapon is sheathed.',5:'Crouch, roll to dodge attacks, or jump.',7:'Use the selected item, or sheath your weapon.'},
'controls_ps5_naruto_x_boruto_ultimate_ninja_storm_connections':{3:'Channel chakra to use ninjutsu or a Secret Technique.'},
'controls_ps5_overcooked':{3:'Dash forward to increase movement speed.'},
'controls_ps5_resident_evil_village':{3:'Crouch to pass through narrow spaces, hide, or avoid attacks at eye level.',6:'Pull the trigger to fire the weapon you are holding, or swing a melee weapon such as a knife.'},
'controls_ps5_tekken_8':{2:"Kick with the left leg to intercept or attack and create an opening in the opponent's defense.",3:'Deliver a powerful right-leg kick, often for range control or a high-damage low sweep.',7:'Move the character in general directions, including moving forward and backward.'},
'controls_ps5_the_last_of_us_part_i':{0:'Control walking and sneaking movement.',3:'Click to toggle the flashlight in dark areas; shake the controller when the flashlight goes out.',7:'Press to reload, or hold to use a healing item; pressing while aiming fires the weapon.',13:'Open the backpack to inspect items, upgrade the character, or craft explosives and pocket knives.'},
'controls_ps5_uncharted_legacy_of_thieves_collection':{4:'Hold to raise the weapon and aim, or brake to slow down or reverse when driving.',5:'Throw a grappling hook to swing across gaps, climb walls, or pull objects in the scene.',9:'Press while moving to dodge-roll, or press near an obstacle to take cover against a wall.'},
'controls_vr_horizon_call_of_the_mountain':{2:'The official game page states that PS VR2 Sense controllers have a grip button for grabbing in-game objects.'},
'controls_ps5_god_of_war_ragnar_k':{5:'Ready your weapon to throw it.',9:'Recall the axe to your hand, or charge the weapon with elemental power while holding L1.',13:'Draw the Leviathan Axe.',15:'Draw the Draupnir Spear.',16:"Switch your companion's arrow type."},
'controls_ps5_the_last_of_us_part_ii':{0:'Control walking, sneaking, or running through the scene.',5:'Hold to raise a firearm, bow, or throwable explosive for aiming.',8:'Open doors, gather crafting materials, squeeze through narrow passages, or grab an enemy from behind.',9:'Press once to crouch and sneak out of sight, or hold to lie prone and crawl along the ground or through grass to hide.',10:'Immediately attack in melee by punching, slapping, or swinging the bladed weapon or wooden plank you are holding.',13:'Open the backpack to inspect all items, craft items, or spend skill upgrade points.'}
}
out.mkdir();changes=[];hashes={};count=0
for p in sorted(src.glob('controls_*.json')):
 d=json.loads(p.read_text(encoding='utf-8'));rid=d['record_id'];lines=d['new_en'].splitlines()
 for n in d['notes']:
  i=n['line'];new=FIXES.get(rid,{}).get(i,n['en']);validate_translation(n['th'],new)
  if new!=n['en']:
   changes.append({'record_id':rid,'line':i,'th':n['th'],'model_en':n['en'],'reviewed_en':new,'reason':'Restore source meaning, conditions, roles or omitted detail; do not add external gameplay instructions'})
   n['en']=new;parts=[x.strip() for x in lines[i].split('|')];parts[2]=new;lines[i]=' | '.join(parts)
  count+=1
 d['new_en']='\n'.join(lines);d['review_method']='Agent read every Thai/English note pair; literal guard retained. Source gameplay facts themselves are not revalidated against current patches.'
 target=out/p.name;target.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8');hashes[p.name]=hashlib.sha256(target.read_bytes()).hexdigest()
assert count==390 and len(hashes)==36
review={'all_proposals_read':True,'all_thai_sources_read':True,'notes_reviewed':count,'records':len(hashes),'source_gameplay_facts_revalidated':False,'unresolved_errors':[],'manual_semantic_revisions':changes,'additional_numeric_manual_override':str(B/'CONTROL_NOTE_MANUAL_OVERRIDES.json'),'proposal_hashes':hashes,'owner_reviewed':False,'proper_name_references':['https://zelda.nintendo.com/features/','https://www.playstation.com/en-us/god-of-war']}
(B/'CONTROL_NOTE_AGENT_REVIEW.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'records':len(hashes),'notes_reviewed':count,'manual_semantic_revisions':len(changes),'owner_reviewed':False}))
