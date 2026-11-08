import json,sys
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project));report=Path((root/'r30_report_path.txt').read_text(encoding='utf-8').strip())
from app.calculator.service_fee import SERVICE_FEES
from app.pipeline.structured_tools import _control_rows,_booking_services_for_game
cases=[]
def add(identifier,group,locale,q,required=(),forbidden=(),outcome='answer'):
    cases.append({'id':identifier,'group':group,'locale':locale,'question':q,'must_contain':list(required),'must_not_contain':list(forbidden),'outcome':outcome,'oracle':'published local source/unchanged fee constants; not owner approval'})
for locale in ('th','en'):
    for service,key,label in [('PC','pc','PC'),('PS5','ps5','PlayStation 5'),('Cockpit','cockpit','Cockpit'),('VR','vr_60','VR')]:
        prices=SERVICE_FEES[key]['prices'];groups=[('บุคคลทั่วไป','a general adult','general_adult'),('ศิษย์เก่า PSU','PSU alumni','general_student'),('นักศึกษา PSU','a PSU student','psu_student_staff')]
        for j,(th,en,g) in enumerate(groups):
            q=f'{th} เล่น {service} 1 ชั่วโมงหรือ 2 ชั่วโมงราคาเท่าไหร่' if locale=='th' else f'How much does it cost for {en} to play {service} for 1 hour or 2 hours?'
            totals=[prices[g],prices[g]*2];required=[f'{n:,} บาท' if locale=='th' else f'{n:,} THB' for n in totals]+(['60 นาที','120 นาที'] if locale=='th' else ['60 minutes','120 minutes'])
            add(f'price-{locale}-{key}-{j}','duration_alternatives',locale,q,required)
    q='บุคคลทั่วไป Nintendo Switch 3 คน เล่น 1 หรือ 2 ชั่วโมงราคาเท่าไหร่' if locale=='th' else 'How much does Nintendo Switch cost for a general adult with 3 people for one or two hours?'
    add(f'price-{locale}-switch-shared-unit','duration_alternatives',locale,q,['280 บาท','560 บาท','120 นาที'] if locale=='th' else ['280 THB','560 THB','120 minutes'])
    q='ศิษย์เก่า PSU VR 30 นาทีหรือ 1 ชั่วโมงราคาเท่าไหร่' if locale=='th' else 'How much does VR cost for PSU alumni for 30 minutes or 1 hour?'
    add(f'price-{locale}-vr-mixed-unit','duration_alternatives',locale,q,['190 บาท','375 บาท'] if locale=='th' else ['190 THB','375 THB'])
    q='บุคคลทั่วไป Cockpit 1.5 ชั่วโมงหรือ 2.5 ชั่วโมงกี่บาท' if locale=='th' else 'How much does Cockpit cost for a general adult for 1.5 hours or 2.5 hours?'
    add(f'price-{locale}-fractional','duration_alternatives',locale,q,['400 บาท','600 บาท','90 นาที','150 นาที'] if locale=='th' else ['400 THB','600 THB','90 minutes','150 minutes'])
for locale in ('th','en'):
    for game,button,forbid in [('Little Nightmares II','Options','Circle:'),('TEKKEN 8','R1','L1:'),('Mario Kart 8 Deluxe','L (Left Stick)','A:'),('The Last of Us Part I','D-Pad (Up / Down / Left / Right)','Options:'),('Super Mario Odyssey','D-Pad Down','D-Pad Right:')]:
        row=next(r for r in _control_rows() if r['game']==game and r['button']==button)
        q=f'ในเกม {game} ปุ่ม {button} ใช้ทำอะไร' if locale=='th' else f'What does the {button} button do in {game}?'
        action=row.get('action_th') if locale=='th' else row.get('action_en')
        add(f'control-{locale}-{len(cases)}','explicit_button',locale,q,[button,action or '',row['source_url']],[forbid])
    for game,zone in [('Beat Saber','VR'),('Uncharted','PlayStation 5'),('The Last of Us Part I','PlayStation 5'),('League of Legends','PC'),('Super Mario Odyssey','Nintendo Switch'),('Gran Turismo 7','Cockpit')]:
        q=f'ถ้าจะเล่น {game} ต้องจองอะไร' if locale=='th' else f'What do you need to book to play {game}?'
        add(f'book-{locale}-{len(cases)}','booking_service_selection',locale,q,[zone,game])
    q='ถ่ายวิดีโอภายในศูนย์ได้ไหม' if locale=='th' else 'May I record video inside the studio?'
    add(f'source-gap-{locale}','source_gap',locale,q,['ยังไม่พบ' if locale=='th' else 'could not find'],['approved English localization'],'no_answer')
# Focused mutation checks. These are development cases; no claim of unseen traffic.
base=list(cases)
for c in base:
    if c['locale']=='en' and c['group']=='duration_alternatives':
        noisy=c['question'].replace('cost','csot').replace('student','stydent')
        cases.append({**c,'id':c['id']+'-noise','question':noisy,'kind':'synthetic_transposition_and_neighbor_key'})
with (report/'focused_fixture_v1.json').open('x',encoding='utf-8') as f:json.dump({'scope':'all expected prices derive from frozen SERVICE_FEES; controls from published rows; booking zone from catalog; fixture controls not hardware verification','cases':cases},f,ensure_ascii=False,indent=2)
print(json.dumps({'cases':len(cases),'groups':sorted({c['group'] for c in cases})}))
