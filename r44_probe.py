import json,sys,re
from pathlib import Path
import r41_probe as p
BASE=Path(__file__).resolve().parent
p.OUT=Path((BASE/'r44_current_path.txt').read_text())
x=json.loads((p.OUT/'WORKBOOK_EXTRACTION.json').read_text(encoding='utf-8'))
cells={c['cell']:c['value'] for row in x['sheets'][0]['rows'] for c in row}
ids=['all_zones','cockpit','vr','nintendo_switch','ps5','pc'];labels=['All Zones','Cockpit','VR','Nintendo Switch','PlayStation 5','PC']
def expected(targets,groups=('external','internal'),periods=('half_day','full_day')):
    cols={('external','full_day'):'B',('external','half_day'):'C',('internal','full_day'):'D',('internal','half_day'):'E'}
    return {f'{t}:{g}:{period}':int(cells[f'{cols[g,period]}{ids.index(t)+3}']) for t in targets for g in groups for period in periods}
def cases():
    cs=[]
    for lang in ('th','en'):
        en=lang=='en'
        for t,label in zip(ids,labels):
            for g in ('external','internal'):
                for period in ('half_day','full_day'):
                    group={'external':'หน่วยงานภายนอก','internal':'หน่วยงานภายใน'}[g]
                    thai_period={'half_day':'ครึ่งวัน','full_day':'เต็มวัน'}[period]
                    q=f'What is the {period.replace("_","-")} rental price for {label} for {g} organizations?' if en else f'ราคาเหมา {label} {group} {thai_period}'
                    cs.append(dict(id=f'{lang}-{t}-{g}-{period}',locale=lang,turns=[q],expected=expected([t],[g],[period])))
        cs+= [
          dict(id=f'{lang}-all-rates',locale=lang,turns=['Show all rental rates' if en else 'ขอราคาเหมาทุกแพ็กเกจ'],expected=expected(ids)),
          dict(id=f'{lang}-bundle',locale=lang,turns=['Whole studio rental price' if en else 'ราคาเหมาทั้งศูนย์'],expected=expected(['all_zones'])),
          dict(id=f'{lang}-four-selections',locale=lang,turns=['Show rental fees' if en else 'ขอราคาเหมา','PC','external' if en else 'ภายนอก','full day' if en else 'เต็มวัน'],expected=expected(['pc'],['external'],['full_day'])),
          dict(id=f'{lang}-expand-all',locale=lang,turns=['PC rental price for external organizations for half day' if en else 'ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','all of them' if en else 'ทั้งหมด'],expected=expected(ids,['external'],['half_day'])),
          dict(id=f'{lang}-resume',locale=lang,turns=['PC rental price for external organizations for half day' if en else 'ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','What are the competition rules for CS2?' if en else 'กฎการแข่งขัน CS2','back to rental prices' if en else 'กลับไปเรื่องราคาเหมาเมื่อกี้'],expected=expected(['pc'],['external'],['half_day'])),
          dict(id=f'{lang}-hours',locale=lang,turns=['PC rental price' if en else 'ราคาเหมา PC','How many hours?' if en else 'กี่ชั่วโมง'],expected={},missing=['duration_definition']),
          dict(id=f'{lang}-capacity',locale=lang,turns=['What is the seating capacity and included equipment for PC zone rental?' if en else 'เหมา PC รองรับกี่คน มีอุปกรณ์อะไร'],expected={},required=['43','10']),
          dict(id=f'{lang}-unknown',locale=lang,turns=['Xbox rental price for a full day' if en else 'ราคาเหมา Xbox เต็มวัน'],expected={},missing=['unresolved_targets']),
          dict(id=f'{lang}-partial-unknown',locale=lang,turns=['Rent PC and Xbox full day price' if en else 'ราคาเหมา PC และ Xbox เต็มวัน'],expected=expected(['pc'],periods=['full_day']),missing=['unresolved_targets']),
          dict(id=f'{lang}-typo',locale=lang,turns=['cockpik rental price for half day' if en else 'ราคาเหมา cockpik ครึ่งวัน'],expected=expected(['cockpit'],periods=['half_day'])),
          dict(id=f'{lang}-individual',locale=lang,turns=['PC rental price for a PSU student' if en else 'นักศึกษา PSU ราคาเหมา PC'],expected=expected(['pc']),missing=['eligibility']),
          dict(id=f'{lang}-single-machine',locale=lang,turns=['Full day PC1 rental price' if en else 'ราคาเหมา PC1 เต็มวัน'],expected=expected(['pc'],periods=['full_day']),missing=['per_unit']),
          dict(id=f'{lang}-date',locale=lang,turns=['When is the rental effective date?' if en else 'ราคาเหมาเริ่มใช้เมื่อไร'],expected={},missing=['effective_date']),
          dict(id=f'{lang}-booking',locale=lang,turns=['How do I book PC zone rental?' if en else 'จองเหมา PC ยังไง'],expected={},missing=['booking']),
          dict(id=f'{lang}-hourly-shift',locale=lang,turns=['PC rental price' if en else 'ราคาเหมา PC','PC hourly price for external users' if en else 'PC รายชั่วโมงของบุคคลภายนอกราคาเท่าไหร่'],negative=True),
          dict(id=f'{lang}-games-shift',locale=lang,turns=['PC rental price' if en else 'ราคาเหมา PC','PC games' if en else 'PC มีเกมอะไรบ้าง'],negative=True),
        ]
    return cs
def grade(c,rs):
    b=rs[-1]['response'];ts=b.get('trace') or []
    meta=b.get('zone_rental_contract') or next((t.get('metadata',{}) for t in ts if t.get('stage')=='zone_rental_contract'),{})
    rates={r['id']:r['value'] for r in meta.get('returned_rates',[])};answer=b.get('answer','')
    checks={'transport':rs[-1]['status']==200 and b.get('ok') is True}
    if c.get('negative'):checks['topic_shift']=b.get('mode')!='pipeline:zone_rental_fee'
    else:
        checks.update(operation=b.get('mode')=='pipeline:zone_rental_fee',original_cell_oracle=rates==c['expected'],
            source_sha256=meta.get('source_sha256')==x['sha256'],required_content=all(v in answer for v in c.get('required',[])),
            missing_fields=set(meta.get('missing_fields',[]))==set(c.get('missing',[])),
            rendered_all_prices=all(f'{v:,}' in answer for v in rates.values()),
            english_no_thai=not bool(re.search('[\u0e00-\u0e7f]',answer)) if c['locale']=='en' else True,
            validation=(b.get('validation') or {}).get('ok') is True)
    return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=b.get('mode'),answer=answer,records=rs)
p.cases=cases;p.grade=grade
if __name__=='__main__':p.run(sys.argv[1],sys.argv[2])
