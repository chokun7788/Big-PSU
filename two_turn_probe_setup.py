import json, hashlib, subprocess, time
from pathlib import Path
WORK=Path(__file__).parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=WORK/('two_turn_choices_20261005_'+time.strftime('%H%M%S'))
OUT.mkdir()
(WORK/'two_turn_current_path.txt').write_text(str(OUT),encoding='utf-8')
cases=[]
def case(id,locale,q,choice,category,contains,clarify=True,detail=False):
    cases.append(dict(id=id,locale=locale,initial=q,choice=choice,expected_category=category,expected_contains=contains,requires_clarification=clarify,full_detail=detail))
for locale,price,rules,controls,devices,games in [
 ('th','อยากรู้ราคาของบุคคลภายนอก','ขอรายละเอียดกติกาการแข่งขัน','ขอดูปุ่มควบคุมเกม','PC มีอะไรบ้าง','มีเกมอะไรให้เล่นบ้าง'),
 ('en','What are the service prices for external users?','I want detailed competition rules','Show me the game controls','What does PC have?','What games can I play?')]:
    for target,label in [('PC','PC'),('PS5','PlayStation 5'),('Nintendo','Nintendo Switch'),('Cockpit','Cockpit'),('VR','VR')]:
        case(locale+'-price-'+target,locale,price,target,'service_fee',[label])
    for target,label in [('CS2','Counter-Strike'),('RoV','RoV'),('TEKKEN 8','TEKKEN'),('VALORANT','VALORANT')]:
        case(locale+'-rules-'+target,locale,rules,target,'competition_rules',[label],detail=True)
    for target in ['VALORANT','Mario Kart 8 Deluxe','Beat Saber']:
        case(locale+'-controls-'+target,locale,controls,target,'game_control',[target])
    for choice,category,contains in [('เกม' if locale=='th' else 'games','games',['PC','VALORANT']),('อุปกรณ์' if locale=='th' else 'equipment','equipment',['PC']),('ราคา' if locale=='th' else 'prices','service_fee',['PC','70']),('จอง' if locale=='th' else 'booking','reservation',['จอง' if locale=='th' else 'book'])]:
        case(locale+'-pc-domain-'+category,locale,devices,choice,category,contains)
    case(locale+'-game-zone',locale,games,'PS5','games',['PlayStation','God of War'],clarify=False)
case('th-cod-warzone','th','ขอรายละเอียดเกม Call of Duty','Warzone','games',['Warzone'])
case('en-cod-mw3','en','Tell me about Call of Duty','Modern Warfare III','games',['Modern Warfare'])
(OUT/'cases.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2),encoding='utf-8')
print(str(OUT));print('Conversations:',len(cases))
