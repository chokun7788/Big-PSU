import json
from two_turn_grader_r39 import OUT
cases=[]
def add(id,lang,q,choice,category,contains,clarify=True,intent=None):
    cases.append(dict(id=id,locale=lang,initial=q,choice=choice,expected_category=category,
                      expected_contains=contains,requires_clarification=clarify,full_detail=False,expected_intent=intent))
for lang,q in [('th','ขอดูปุ่มควบคุมเกม'),('en','Show me the game controls')]:
    for choice in (['วาโลครับ','Valoant'] if lang=='th' else ['the VALORANT one','Valoant please']):
        add(lang+'-extra-controls-'+choice,lang,q,choice,'game_control',['VALORANT','W / A / S / D'])
    add(lang+'-extra-new-operation',lang,q,'VALORANT คืออะไร' if lang=='th' else 'What is VALORANT?',
        'games',['VALORANT'],'',intent='game_detail_lookup')
    add(lang+'-extra-zone-typo',lang,'มีเกมอะไรให้เล่นบ้าง' if lang=='th' else 'What games can I play?',
        'cockpik','games',['Gran Turismo 7'],False)
    add(lang+'-extra-zone-polite',lang,'มีเกมอะไรให้เล่นบ้าง' if lang=='th' else 'What games can I play?',
        'ขอ PS5 ครับ' if lang=='th' else 'the PS5 one','games',['God of War'],False)
add('en-extra-family-controls','en','What are the controls for Call of Duty?','Modern Warfare III','game_control',['Modern Warfare III','L2'])
add('en-extra-singular-control','en','Show me the game control','VALORANT','game_control',['VALORANT','W / A / S / D'])
for index,q in enumerate(['Can I see the game controls?','What buttons can I use?','How do I control the game?']):
    add('en-extra-control-rephrase-'+str(index),'en',q,'VALORANT','game_control',['VALORANT','W / A / S / D'])
add('en-extra-domain-fees','en','What does PS5 offer?','fees','service_fee',['PlayStation 5','150'])
add('en-extra-domain-booking','en',"What's in the VR zone?",'booking','reservation',['book'])
for c in cases:
    if 'zone-typo' in c['id']:
        c['forbidden_contains']=['PC Zone','PlayStation 5 Zone','Nintendo Switch Zone','VR Zone']
    if 'zone-polite' in c['id']:
        c['forbidden_contains']=['PC Zone','Nintendo Switch Zone','Cockpit Zone','VR Zone']
(OUT/'extra_cases_r39.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2),encoding='utf-8')
print('Extra conversations',len(cases))
