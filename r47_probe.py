import sys,json,uuid,shutil,hashlib,re
from pathlib import Path
import r46_probe as prior
BASE=Path(__file__).resolve().parent;ROOT=prior.prior.r.p.ROOT
pointer=BASE/'r47_current_path.txt'
if not pointer.exists():
    out=BASE/('r47_answer_content_20261007_'+uuid.uuid4().hex[:8]);out.mkdir();pointer.write_text(str(out))
    manifest={}
    for folder in ('app','tests','data/curated','data/rules','web_chat'):
        for p in (ROOT/folder).rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts:
                rel=p.relative_to(ROOT);dest=out/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
                manifest[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    (out/'before_manifest.json').write_text(json.dumps(manifest,indent=2))
OUT=Path(pointer.read_text());prior.prior.r.p.OUT=OUT
location=next(json.loads(line) for line in (ROOT/'data/rules/contact_rules.jsonl').read_text(encoding='utf-8').splitlines() if json.loads(line)['id']=='rule_contact_location')
ADDRESS_EN=location['answer_en'];ADDRESS_TH=location['answer_th'];URL=location['source_url']
def cases():
    queries=['Where is the venue?','Where is the studio located?','Where is PSU Esports Studio - Phuket?','What is the venue address?','What is the address of the studio?','Can you tell me the studio location?','Where can I find the studio?','I need the venue address','How do I get to the venue?','Could you please share the address of PSU Esports Studio - Phuket?','Studio address','Where is the centre?']
    rows=[dict(id='en-location-'+str(i+1),locale='en',turns=[q],kind='location') for i,q in enumerate(queries)]
    rows.extend([
      dict(id='en-location-after-rental',locale='en',turns=['PC rental full day external organizations','Where is the venue?'],kind='location'),
      dict(id='en-location-after-rules',locale='en',turns=['Competition rules for CS2','Where is the studio?'],kind='location'),
      dict(id='th-location',locale='th',turns=['ศูนย์อยู่ที่ไหน'],kind='location'),
      dict(id='th-location-address',locale='th',turns=['ขอที่อยู่ศูนย์'],kind='location'),
      dict(id='th-location-explicit',locale='th',turns=['ที่ตั้ง PSU Esports Studio อยู่ที่ไหน'],kind='location'),
      dict(id='en-equipment-location',locale='en',turns=['Where is the 65-inch TV located?'],kind='other',category='equipment',required=['Cockpit Zone'],forbidden=[ADDRESS_EN]),
      dict(id='en-game-location',locale='en',turns=['Can I play Beat Saber in the VR Zone?'],kind='other',category='games',required=['Beat Saber','VR'],forbidden=[ADDRESS_EN]),
      dict(id='en-competition-location',locale='en',turns=['Where is the RoV competition venue?'],kind='other',category='competition_rules',required=['Building 5','Floor 1'],forbidden=[ADDRESS_EN]),
      dict(id='en-fire-button-location',locale='en',turns=['Where is the fire button in Counter-Strike 2?'],kind='other',category='games',required=['Mouse'],forbidden=[ADDRESS_EN]),
      dict(id='en-studio-hours',locale='en',turns=['What are the venue opening hours?'],kind='other',category='schedule',required=['09:00','12:00','13:00'],forbidden=[ADDRESS_EN]),
      dict(id='en-pc-price-shift',locale='en',turns=['PC rental full day external organizations','PC hourly price for external users'],kind='other',category='service_fee',required=['PC','25 THB','70 THB','local://service_fee/pc_price_update_20260727'],forbidden=['Zone rental fees for organizations']),
      dict(id='en-pc-games-shift',locale='en',turns=['PC rental full day external organizations','PC games'],kind='other',category='games',required=['PC Zone','VALORANT','Counter-Strike 2','Call of Duty: Warzone','TEKKEN 8'],forbidden=['VR Zone','Zone rental fees for organizations']),
      dict(id='en-unknown-venue',locale='en',turns=['Where is the Xbox studio in Bangkok?'],kind='no_psu_address',forbidden=[ADDRESS_EN]),
    ])
    return rows
def grade(c,rs):
    b=rs[-1]['response'];answer=b.get('answer','');hits=b.get('sources',[])
    checks=dict(transport=rs[-1]['status']==200 and b.get('ok') is True,no_timeout=not b.get('timed_out'),english_no_thai=not re.search('[\u0e00-\u0e7f]',answer) if c['locale']=='en' else True)
    if c['kind']=='location':
        checks.update(category=b.get('route_category')=='contact',source_bound_address=(ADDRESS_EN if c['locale']=='en' else ADDRESS_TH) in answer,source_url=URL in answer,not_no_answer='no_answer' not in b.get('mode',''))
        if hits and b.get('mode')=='pipeline:structured_studio_location_en':checks['source_record_id']=any(h.get('id')=='curated_contact_location' for h in hits)
    else:
        checks.update(required_content=all(x.casefold() in answer.casefold() for x in c.get('required',[])),forbidden_content=not any(x.casefold() in answer.casefold() for x in c.get('forbidden',[])))
        if c.get('category'):checks['category']=b.get('route_category')==c['category']
    return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=b.get('mode'),answer=answer,records=rs)
prior.prior.r.p.cases=cases;prior.prior.r.p.grade=grade
if __name__=='__main__':prior.prior.r.p.run(sys.argv[1],sys.argv[2])
