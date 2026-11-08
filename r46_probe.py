import sys,json,uuid,shutil,hashlib
from pathlib import Path
import r45_probe as prior
BASE=Path(__file__).resolve().parent
pointer=BASE/'r46_current_path.txt'
if not pointer.exists():
    out=BASE/('r46_english_rental_20261007_'+uuid.uuid4().hex[:8]);out.mkdir()
    pointer.write_text(str(out))
    manifest={}
    for folder in ('app','tests','data/curated','web_chat'):
        for p in (prior.r.p.ROOT/folder).rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts:
                rel=p.relative_to(prior.r.p.ROOT);dest=out/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
                manifest[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    (out/'before_manifest.json').write_text(json.dumps(manifest,indent=2))
OUT=Path(pointer.read_text());prior.r.p.OUT=OUT
def c(name,qs,targets=('pc',),groups=('external',),periods=('full_day',),**kw):
    return dict(id='en-'+name,locale='en',turns=qs if isinstance(qs,list) else [qs],expected=prior.r.expected(targets,groups,periods),**kw)
start='PC rental price for external organizations full day'
def cases():
    rows=[
      c('polite-hire','Could you quote the full-day hire cost for PC for external organizations?'),
      c('polite-rent','I would like to rent PC for a full day. What is the cost for external organizations?'),
      c('whole-day','PC whole-day rental price for external organizations'),
      c('halfday','PC halfday hire fees for external organizations',periods=['half_day']),
      c('polite-selection',[start,'Only the half day please'],periods=['half_day']),
      c('different-zone',[start,'What about VR?'],targets=['vr']),
      c('different-group',[start,'internal instead'],groups=['internal']),
      c('equipment',[start,'What equipment comes with it?'],targets=[],required=['10','PC']),
      c('seats',[start,'How many seats does it have?'],targets=[],required=['43']),
      c('people',[start,'How many people can it accommodate?'],targets=[],required=['43']),
      c('duration',[start,'How long is a full day?'],targets=[],missing=['duration_definition']),
      c('staff',[start,'Is staff overtime included?'],targets=[],missing=['overtime']),
      c('reserve',[start,'How can I reserve it?'],targets=[],missing=['booking']),
      c('booking-procedure',[start,'What is the booking procedure?'],targets=[],missing=['booking']),
      c('effective',[start,'When do these prices take effect?'],targets=[],missing=['effective_date']),
      c('cost-after-details',[start,'What equipment comes with it?','How much would that be?']),
      c('typo-cockpit','cockpitt full-day rental cost for external organizations',targets=['cockpit']),
      c('typo-nintendo','nintndo switch full-day rental cost for external organizations',targets=['nintendo_switch']),
      c('unknown-code','PS55 full-day rental cost for external organizations',targets=[],missing=['unresolved_targets']),
      c('unknown-product','Xbox full-day rental cost for external organizations',targets=[],missing=['unresolved_targets']),
      c('exclude-period','PC rental price for external organizations, not half-day'),
      c('exclude-group','PC full-day rental cost, not internal organizations'),
      c('exclude-target','All rental rates except VR',targets=[t for t in prior.r.ids if t!='vr'],groups=['external','internal'],periods=['half_day','full_day']),
      c('generic-exclusion','Rental prices except VR',targets=[t for t in prior.r.ids if t!='vr'],groups=['external','internal'],periods=['half_day','full_day']),
      c('custom-bundle','Entire studio rental excluding PC',targets=[],missing=['custom_package']),
      c('individual','Full-day PC rental price for an individual',groups=['external','internal'],missing=['eligibility']),
      c('hourly','PC hourly rental price',targets=[],missing=['hourly_rental']),
      c('per-machine','PC full-day rental price per machine',groups=['external','internal'],missing=['per_unit']),
      c('compound-and','PC full-day rental external organizations and VR half-day rental internal organizations',targets=[]),
      c('compound-versus','PC full-day rental external organizations versus VR half-day rental internal organizations',targets=[]),
      c('compound-with','Compare PC full-day rental for external organizations with VR half-day rental for internal organizations',targets=[]),
      dict(id='en-topic-games',locale='en',turns=[start,'What games are available on PC?'],negative=True),
      dict(id='en-topic-rules',locale='en',turns=[start,'Competition rules for CS2'],negative=True),
    ]
    for row in rows:
        if 'compound-' in row['id']:
            row['expected']={**prior.r.expected(['pc'],['external'],['full_day']),**prior.r.expected(['vr'],['internal'],['half_day'])}
    return rows
prior.r.p.cases=cases;prior.r.p.grade=prior.grade
if __name__=='__main__':prior.r.p.run(sys.argv[1],sys.argv[2])
