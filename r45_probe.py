import sys,json,uuid,time,hashlib,shutil,re
from pathlib import Path
import r44_probe as r
BASE=Path(__file__).resolve().parent
if not (BASE/'r45_current_path.txt').exists():
    out=BASE/('r45_rental_cases_'+time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);out.mkdir()
    (BASE/'r45_current_path.txt').write_text(str(out))
    before={}
    for folder in ('app','tests','data/curated'):
        for p in (r.p.ROOT/folder).rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts:
                rel=p.relative_to(r.p.ROOT);dest=out/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest);before[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    (out/'before_manifest.json').write_text(json.dumps(before,indent=2))
r.p.OUT=Path((BASE/'r45_current_path.txt').read_text())
def case(name,q,targets,groups=('external','internal'),periods=('half_day','full_day'),locale='th',**kwargs):
    return dict(id=name,locale=locale,turns=q if isinstance(q,list) else [q],expected=r.expected(targets,groups,periods),**kwargs)
def cases():
    cs=[
      case('th-colloquial-pc','ค่าเช่าคอมครึ่งวันของหน่วยงานภายนอกเท่าไหร่',['pc'],['external'],['half_day']),
      case('th-long-question','อยากทราบราคาเช่าโซน PlayStation 5 สำหรับหน่วยงานภายนอกแบบเต็มวันครับ',['ps5'],['external'],['full_day']),
      case('en-half-cost','PC half-day cost for external organizations',['pc'],['external'],['half_day'],'en'),
      case('en-long-question','Could you tell me the price to rent Nintendo Switch for a half day for internal organizations?',['nintendo_switch'],['internal'],['half_day'],'en'),
      case('th-typo-cockpit','ขอราคาเหมา cockpitt ครึ่งวัน',['cockpit'],periods=['half_day']),
      case('th-typo-switch','ราคาเหมา nintndo switch เต็มวัน',['nintendo_switch'],periods=['full_day']),
      case('en-typo-cockpit','cockpik rental price for full day',['cockpit'],periods=['full_day'],locale='en'),
      case('en-typo-playstation','playstaton rental price for half day',['ps5'],periods=['half_day'],locale='en'),
      case('th-price-typo','ราคาเหมา PC หน่วยงานภายนอกครึ่งวันเท่าไหร',['pc'],['external'],['half_day']),
      case('th-double-letter','ราคาเหมา PC ครึ่งวันน',['pc'],periods=['half_day']),
      case('th-selective-groups','ราคาเหมา PC เต็มวัน ไม่เอาราคาหน่วยงานภายใน',['pc'],['external'],['full_day']),
      case('en-selective-groups','PC full day rental price excluding internal organizations',['pc'],['external'],['full_day'],'en'),
      case('th-selective-period','ราคาเหมา VR ไม่เอาครึ่งวัน เอาเต็มวัน',['vr'],periods=['full_day']),
      case('en-selective-period','VR rental price for full day, not half day',['vr'],periods=['full_day'],locale='en'),
      case('th-exclude-followup',['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','ทั้งหมด ยกเว้น VR'],[t for t in r.ids if t!='vr'],['external'],['half_day']),
      case('en-exclude-followup',['PC rental price for external organizations half day','all rental rates except VR'],[t for t in r.ids if t!='vr'],['external'],['half_day'],'en'),
      case('th-period-followup',['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','แล้วถ้าเต็มวันล่ะ'],['pc'],['external'],['full_day']),
      case('en-group-change',['PC rental price for external organizations half day','internal instead'],['pc'],['internal'],['half_day'],'en'),
      case('th-unknown-selection',['ขอราคาเหมา','Xbox'],[],missing=['unresolved_targets']),
      case('en-unknown-selection',['Show rental rates','Xbox'],[],locale='en',missing=['unresolved_targets']),
      case('th-ps55','ราคาเหมา PS55 เต็มวัน',[],periods=['full_day'],missing=['unresolved_targets']),
      case('en-ps55','PS55 rental price full day',[],periods=['full_day'],locale='en',missing=['unresolved_targets']),
      case('th-included-then-price',['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','รวมอะไรบ้าง','ราคาเท่าไหร่'],['pc'],['external'],['half_day']),
      case('en-included-then-price',['PC rental price external half day','What is included?','How much does it cost?'],['pc'],['external'],['half_day'],'en'),
      case('th-bundle-subset','ราคาเหมาทั้งศูนย์ยกเว้น PC',[],missing=['custom_package']),
      case('en-bundle-subset','Whole studio rental price except PC',[],locale='en',missing=['custom_package']),
      case('th-context-explicit',['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','แล้วราคาเหมา VR ล่ะ'],['vr'],['external'],['half_day']),
      case('en-context-explicit',['PC rental price external half day','And the rental price for VR?'],['vr'],['external'],['half_day'],'en'),
      case('th-two-zones-same','ราคาเหมา PC และ VR หน่วยงานภายนอกครึ่งวัน',['pc','vr'],['external'],['half_day']),
      case('en-two-zones-same','PC and VR half day rental prices for external organizations',['pc','vr'],['external'],['half_day'],'en'),
      case('th-overtime-followup',['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','รวมค่าเจ้าหน้าที่ไหม'],[],missing=['overtime']),
      case('en-book-followup',['PC rental price external half day','How do I book it?'],[],locale='en',missing=['booking']),
      case('th-book-followup',['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','จองยังไง'],[],missing=['booking']),
      case('th-period-info',['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','ครึ่งวันเริ่มกี่โมง'],[],missing=['duration_definition']),
    ]
    for lang in ('th','en'):
        en=lang=='en'
        for name,q,exp in [
          ('different-periods','PC rental full day and VR rental half day for external organizations' if en else 'ราคาเหมา PC เต็มวัน และ VR ครึ่งวัน หน่วยงานภายนอก',{**r.expected(['pc'],['external'],['full_day']),**r.expected(['vr'],['external'],['half_day'])}),
          ('different-groups','PC rental full day external organizations and VR rental half day internal organizations' if en else 'ราคาเหมา PC เต็มวันหน่วยงานภายนอก และ VR ครึ่งวันหน่วยงานภายใน',{**r.expected(['pc'],['external'],['full_day']),**r.expected(['vr'],['internal'],['half_day'])}),
          ('same-zone-period-groups','PC rental full day external organizations and PC rental half day internal organizations' if en else 'ราคาเหมา PC เต็มวันหน่วยงานภายนอก และ PC ครึ่งวันหน่วยงานภายใน',{**r.expected(['pc'],['external'],['full_day']),**r.expected(['pc'],['internal'],['half_day'])}),
        ]:cs.append(dict(id=f'{lang}-{name}',locale=lang,turns=[q],expected=exp))
    return cs
original_grade=r.grade
def grade(c,rs):
    result=original_grade(c,rs)
    result['checks']['no_timeout']=all(not rec['response'].get('timed_out') for rec in rs)
    if c['id']=='en-resume-compound':
        result['checks']['intermediate_rule_topic']=rs[1]['response'].get('route_category')=='competition_rules'
    result['passed']=all(result['checks'].values())
    return result
r.p.cases=cases;r.p.grade=grade
if __name__=='__main__':r.p.run(sys.argv[1],sys.argv[2])
