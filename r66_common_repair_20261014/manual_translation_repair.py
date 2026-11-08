"""Agent-reviewed source translations for protected-literal rejects; not owner review."""
import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.translation import protected
p=B/'TRANSLATIONS.jsonl';fails=[json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if not json.loads(x)['accepted']]
translations={
0:'1. Personnel during preparation: no more than 6 players are allowed.',
2:'Game pauses are divided into 3 main types for different reasons.',
4:'4. Timeouts: 4 per team, 30 seconds each, available during Freeze time.',
6:'3. Technical pauses: 2 per team, no more than 10 minutes each. Any issue must be reported to the referee immediately.',
8:'1. The competition lasts 1 day and takes place at PSU Esports Studio - Phuket, Prince of Songkla University, Phuket Campus.',
10:'7. Competition schedule: the bracket will be announced at least 1 day in advance. Participation must be confirmed before the match starts. Late arrival may result in disqualification.',
12:'''1. Tactical Timeout
* 2 requests per map during regulation (the first 24 rounds), 60 seconds each.
* In Overtime, each team receives 1 additional request. Unused regulation requests do not carry over.''',
13:'''Competition rules
* Offline competition.
* PlayStation 5 is used.
* Singles (1v1).
* Competition format:
* FT2: the winner is the first to win 2 games.
* Each game uses R3 (3 rounds per game) and 60S (60 seconds per round).
* At a 1-1 tie, a deciding game must be played.''',
14:'''Characters and settings
* Any character may be selected except DLC characters.
* Character customization is prohibited in all cases, including outfits, hairstyles, fighting effects and auras.
* Only default skins may be used.
* Assist buttons or special assistance systems are allowed.
* Bugs or glitches that provide an advantage are prohibited.
* Once a game starts, pausing for any reason is prohibited.
* Deliberately pausing immediately results in a loss of 1 round.''',
15:'''Competition area and regulations
* During Match Prep, no more than 6 players are allowed.
* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.
* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.
* Only drinking water in a sealed container and chewing gum are allowed.
Competition process''',
16:'''1. Competition schedule
1.1. Offline competition on 11 September 2568 (B.E.)
· 8.00-8.30 Registration
· 8.30-8.40 Bracket draw
· 8.40-10.00 Round of 5 teams: Single Elimination BO3
· 10.00-11.30 Semifinal 1: Single Elimination BO3
· 12.30-14.00 Semifinal 2: Single Elimination BO3
· 14.00-15.30 3rd-place match: Single Elimination BO3
· 15.30-17.00 Final: Single Elimination BO3''',
17:'''3. Player Emergency Pause
* 1 request per map.
* Total time must not exceed 10 minutes per match. If exceeded, that player may lose eligibility to continue and must be replaced by a substitute.
Bug rules
Bugs are unintended game errors. They are classified to determine the procedure:
* Play Through Bug: a bug with no significant effect on fairness. Players must continue and cannot request a Challenge.
* Major Bug: a bug with a major effect on gameplay or game mechanics and no immediate workaround. The team may request a Challenge for review.
* Game Breaking Bug: a bug that destroys the fairness of the round so its winner cannot be determined.
* Round Rollback:
* If a bug occurs before any damage is dealt, officials may roll back the round.
* After damage has been dealt, there is no rollback except through the Challenge procedure.
* For a Game Breaking Bug, officials will immediately roll back to the start of that round.
Exploit Adjudication''',
18:'''4.5.6.1.1. Physical interference between competitors, such as disturbances, disorder or loud noise disrupting the game.
4.5.6.1.2. A mobile device or software malfunctions.
4.5.6.1.3. Frame drops or increased PING outside the competitor's control.
4.5.6.1.4. The opposing competitor cheats or seriously insults others, for example.
4.6. Illness, injury or physical problems of a competitor are not acceptable reasons for that competitor to pause.
4.6.1. A pause caused by a mobile device overheating.
4.6.1.1. Staff may order a pause of no more than 5 minutes to cool the device if they consider that its heat is causing frame drops or increased Ping in the game.
4.6.2. A pause decided by a competitor without the referee's permission.
4.6.2.1. Staff have the right to warn and/or immediately declare that competitor's team to have lost.
4.6.2.2. Competitors are prohibited from talking, contacting others or otherwise communicating during the pause.
4.6.3. Penalties:
4.6.3.1. Occurrence 1: warning.
4.6.3.2. Occurrence 2: give the opposing side 1 additional hero ban.
4.6.3.3. Occurrence 3: give the opposing side 2 additional hero bans.''',
19:'''4. Competition regulations and rules
4.1. Basic rules
4.1.1. Character names or language that are rude or mock others are prohibited.
4.1.2. In the first game, the team at the top of the bracket takes the blue side. In subsequent games, the loser of the previous game chooses the side.
4.1.3. The referee announces the room number, and both teams must enter that room.
* The blue team is at the top.
* The red team is at the bottom.
4.1.4. If a side delays the start by more than 15 minutes beyond the scheduled time, it immediately loses the competition.
4.2. Competition rules
4.2.1. Every competitor must have at least 18 heroes to enter the competition 5v5 mode (formerly Tournament Mode).
4.2.2. Global Ban/Pick is used for hero bans and picks.
4.2.3. Runes and enhancements may be configured as desired.
4.2.4. All heroes may be selected during the competition.
4.2.5. Skins other than Default are prohibited.
4.2.6. Repeating a hero selection in the competition, or any other action causing a system problem, is prohibited in all cases.
4.3. Disconnect and Rematch
4.3.1. If a competitor disconnects, temporarily pause the game. Each team may pause 5 times, no more than 1 minute each. Beyond that time, the other team may immediately press Resume and continue normally.''',
20:'''4.3.2. For disconnections caused by force majeure, such as an area-wide internet provider outage or a game server error, the affected team must notify staff. Whether to allow a rematch is at the referee's discretion.
4.3.3. If there has been no First Blood and in-game time has not exceeded 2 minutes, the disconnected competitor's team may immediately notify the other team and request a new game. Every competitor must use the same hero and playing position as in the initial game.
4.3.4. After First Blood or once in-game time exceeds 2 minutes, neither team may request a new game except with the opponent's permission and/or as the referee considers appropriate.
4.3.5. If evidence shows a competitor deliberately paused at a critical moment or to disrupt play, their team immediately loses that game and is immediately disqualified from the competition.
4.4. Breaks
4.4.1. The referee will tell competitors how much time remains before the next game starts.
4.4.2. If competitors do not return within the specified time, the referee may declare their team to have lost.
4.4.3. Take a 5-minute break after every two games.
4.5. Pausing during competition
4.5.1. General pauses
4.5.1.1. If a competitor deliberately does not connect to the game without notifying the referee, the referee has the right to refuse that pause request.''',
21:'1 booking can include up to 3 Sessions.',
22:'Users must book through the online system at least 1 hour before the intended use time.',
23:'VR service fees for 30 minutes: PSU students/staff 0 baht; PSU alumni or General Student 190 baht; general public 525 baht.',
24:'GAME ON! introduces esports to 21 students in secondary year 3 (M.3) from Thaimuang Wittaya School.',
25:'VR service fees for 1 hour: PSU students/staff 0 baht; PSU alumni or General Student 375 baht; general public 1050 baht.',
26:'Repeated rule violations or serious misconduct may result in suspension of access for 1-7 days, depending on the nature of the violation.',
27:'The booking system offers 2 VR Station services: VR Station (1-5 Persons) 1 Hour 60 min and VR Station (1-5 Persons) 30 Mins 30 min.',
28:'On 25 April 2569 (B.E.), PSU Esports Studio - Phuket held the PSU Phuket CS 2 2026 Tournament for Counter-Strike 2.',
29:'Nintendo Switch service fees for 1-2 people per 60 minutes: PSU students/staff 0 baht; PSU alumni or General Student 50 baht; general public 140 baht.',
30:'Nintendo Switch service fees for 3-4 people per 60 minutes: PSU students/staff 0 baht; PSU alumni or General Student 100 baht; general public 280 baht.',
31:'Use time may be changed by notifying the studio at least 1 hour before the booked time. If notice is late or not given, the studio reserves the right to provide neither a refund nor replacement time.',
32:'Booking information cannot be edited after submission. To change it, cancel through the email at least 1 hour before use, then book again and attach the original payment slip.',
33:'On 27 February 2569 (B.E.), 11 Chinese master\'s students from the Faculty of Hospitality and Tourism took part in Game-based Learning at PSU Esports Studio - Phuket.',
34:'''PC Zone gaming computers for PC gaming and esports practice.
Choose PC Zone in the booking system, arrive for the booked session, then open the games/programs provided by the studio.
Specifications recorded in the project: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
Play VALORANT
Play Counter-Strike 2
Play PUBG: BATTLEGROUNDS
Play Call of Duty: Warzone
Play TEKKEN 8
Play League of Legends'''
}
for duplicate,original in [(1,0),(3,2),(5,4),(7,6),(9,8),(11,10)]:translations[duplicate]=translations[original]
assert len(fails)==35 and len(translations)==35
review=[]
for i,x in enumerate(fails):assert protected(x['th'])==protected(translations[i]),(i,protected(x['th']),protected(translations[i]))
already={json.loads(line)['slot_key'] for line in p.read_text(encoding='utf-8').splitlines() if json.loads(line).get('method')=='agent_source_review_translation'}
for i,x in enumerate(fails):
 target=translations[i]
 # Literal dates/section numbers retained, no CE conversion or invented units.
 assert protected(x['th'])==protected(target),(i,protected(x['th']),protected(target))
 new={**x,'en':target,'accepted':True,'method':'agent_source_review_translation','elapsed':0,'owner_reviewed':False,'prior_rejection_preserved':True}
 if x['slot_key'] not in already:
  with p.open('a',encoding='utf-8') as f:f.write(json.dumps(new,ensure_ascii=False)+'\n')
 review.append(new)
(B/'MANUAL_TRANSLATION_REPAIRS.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
print('35 reviewed translations appended; original rejected model rows preserved')
