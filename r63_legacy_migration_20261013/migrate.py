"""Read production sources, append drafts into a NEW SQLite backup only."""
from __future__ import annotations
import collections,copy,hashlib,json,re,shutil,sqlite3,sys,unicodedata
from datetime import date,timedelta
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent
if '--out' in sys.argv:
    OUT=Path(sys.argv[sys.argv.index('--out')+1]).resolve();OUT.mkdir(parents=True,exist_ok=True)
SYSTEM=BASE/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(SYSTEM))
from app.knowledge.common.registry import CATALOG,template,now,pointer,validate,value
from app.knowledge.common.store import CommonStore
from app.knowledge.records import canonical_json,digest

def dump(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'[^\w]','',unicodedata.normalize('NFKC',s).casefold())
def sid(s):return re.sub('[^a-z0-9_]+','_',s.lower()).strip('_') or hashlib.sha256(s.encode()).hexdigest()[:12]
def localized(th,en=None):return {'th':th or None,'en':en or None}
def stable_id(s):
    v=re.sub('[^a-z0-9_:-]','_',s.lower())
    return v if len(v)<=100 else v[:78]+'_'+hashlib.sha256(s.encode()).hexdigest()[:20]

def main():
    db=OUT/'review/approved.sqlite'
    if db.exists():raise SystemExit('Existing review database preserved; choose a new output directory for another run')
    db.parent.mkdir(parents=True)
    original_db=ROOT/'data/knowledge/approved.sqlite'
    with sqlite3.connect(original_db.as_uri()+'?mode=ro',uri=True) as c,sqlite3.connect(db) as dest:c.backup(dest)
    shutil.copy2(db,OUT/'before.sqlite')
    store=CommonStore(db);store.initialize()
    with store.connect() as c:existing=store.heads(c)
    before=store.snapshot()
    drafts={};sources=[];mapping=[];coverage=[];issues=[];files={}

    def read(rel):
        p=ROOT/rel;data=p.read_bytes();h=hashlib.sha256(data).hexdigest()
        if rel not in files:
            backup=OUT/'original_files'/rel;backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(data)
            files[rel]={'path':rel,'sha256':h,'bytes':len(data)}
        if p.suffix=='.xlsx':return None
        if p.suffix=='.jsonl':return [json.loads(x) for x in data.decode('utf-8-sig').splitlines() if x.strip()]
        if p.suffix=='.json':return json.loads(data.decode('utf-8-sig'))
        return data.decode('utf-8-sig')
    def rec(kind,rid,aliases=None):
        rid=stable_id(rid)
        if rid in drafts:return drafts[rid]
        r=copy.deepcopy(existing[rid]) if rid in existing else template(kind)
        if r['kind']!=kind:raise ValueError('Identity kind changed '+rid)
        r['record_id']=rid
        if aliases:
            for lang in ('th','en'):r['aliases'][lang]=list(dict.fromkeys(r['aliases'][lang]+aliases.get(lang,[])))
        drafts[rid]=r;return r
    def put(r,key,v,rel,loc='',rule='exact',note=None):
        if v is None or v=='':return
        if isinstance(v,dict) and set(v)=={'th','en'} and not (v['th'] or v['en']):return
        spec=next(x for x in CATALOG[r['kind']]['fields'] if x['key']==key)
        if spec['reference_kind']:v=[stable_id(x) for x in v] if isinstance(v,list) else stable_id(v)
        original=read(rel);orig=pointer(original,loc)
        old=r['fields'][key]
        if old['status']=='known':
            if old['value']==v:return
            # Existing localized translation is retained; fill only missing locale.
            if isinstance(v,dict) and set(v)=={'th','en'} and isinstance(old['value'],dict):
                if all(not v[k] or not old['value'].get(k) or old['value'][k]==v[k] for k in ('th','en')):
                    merged={k:old['value'].get(k) or v[k] for k in ('th','en')}
                    if merged==old['value']:return
                    v=merged;rule+='; retain existing locale'
                else:
                    issues.append({'record_id':r['record_id'],'field':key,'reason':'Existing draft differs; retained','existing':old['value'],'incoming':v,'source':rel,'locator':loc});return
            else:
                issues.append({'record_id':r['record_id'],'field':key,'reason':'Existing draft differs; retained','existing':old['value'],'incoming':v,'source':rel,'locator':loc});return
        r['fields'][key]={'status':'known','value':v,'evidence_refs':[],'note':note or 'ย้ายจากต้นฉบับเดิมเป็นร่าง: '+rule}
        mapping.append({'record_id':r['record_id'],'field':key,'source_path':rel,'source_sha256':files[rel]['sha256'],'locator':loc,'source_value':orig,'mapped_value':v,'transform':rule})
    def pending(r,key,reason):
        if r['fields'][key]['status']=='unknown':r['fields'][key]['note']=reason
        issues.append({'record_id':r['record_id'],'field':key,'reason':reason})
    def faq(rid,title,text,rel,titleloc='',textloc='',en=None,topic=None,aliases=None):
        r=rec('faq',rid,aliases)
        put(r,'question',localized(title),rel,titleloc,'legacy title/label → question; no generated facts')
        put(r,'answer',localized(text,en),rel,textloc,'copy complete answer; preserve English status')
        if topic:put(r,'topic',topic,rel,titleloc,'legacy category → topic')
        return r

    canonical=[]
    for p in sorted((ROOT/'data/content').rglob('*.json')):
        if any(x in p.relative_to(ROOT/'data/content').parts for x in ('schema','review','projections','releases')):continue
        raw=json.loads(p.read_text(encoding='utf-8-sig'))
        if 'content_id' not in raw:continue
        rel=p.relative_to(ROOT).as_posix();row=read(rel);canonical.append((rel,row))
    games={};zones={};services={}
    for rel,row in canonical:
        if row['kind']!='game_profile':continue
        r=rec('game',row['content_id'],row['aliases']);th=row['locales']['th']['fields'];en=row['locales']['en']['fields']
        for k,old in [('title','title'),('summary','summary_th'),('how_to_play','how_to_play_th'),('genre','genre')]:
            if old in th:put(r,k,localized(th[old],en.get({'summary_th':'summary_en','how_to_play_th':'how_to_play_en'}.get(old,old))),rel,'/locales/th/fields/'+old,'localized copy; original English preserved without upgrading review')
        # Only source titles establish catalog identity. Broad search aliases
        # must not merge different editions or Overcooked! with Overcooked! 2.
        for label in [row['facts']['game'],th.get('title','')]:games[norm(label)]=r['record_id']
    def game(label,rel,loc):
        key=norm(label)
        if key not in games:
            r=rec('game','migrated_game_'+sid(label));put(r,'title',localized(label,label),rel,loc,'source game label → title');games[key]=r['record_id']
        return games[key]
    def zone(label,rel,loc):
        key=norm(label)
        if key not in zones:
            name={'PC Zone':'pc','Cockpit Zone':'cockpit','VR Zone':'vr','PlayStation 5 Zone':'ps5','Nintendo Switch Zone':'nintendo','All Zones':'all_zones'}.get(label,sid(label))
            rid='zone_'+name;r=rec('zone',rid);put(r,'name',localized(label,label),rel,loc,'source zone label → name');zones[key]=rid
        return zones[key]
    for rel,row in canonical:
        if row['kind']!='service_availability':continue
        f=row['facts'];zid=zone(f['zone'],rel,'/facts/zone');r=rec('service',row['content_id'],row['aliases'])
        put(r,'name',localized(f['service_label'],f['service_label']),rel,'/facts/service_label','copy service label')
        put(r,'session_minutes',f['duration_minutes'],rel,'/facts/duration_minutes')
        put(r,'platform',f['zone'].removesuffix(' Zone'),rel,'/facts/zone','remove literal Zone suffix')
        cap=[int(x) for x in re.findall(r'\d+',f['capacity_persons'])]
        put(r,'capacity_min',min(cap),rel,'/facts/capacity_persons','parse explicit persons range minimum')
        put(r,'capacity_max',max(cap),rel,'/facts/capacity_persons','parse explicit persons range maximum')
        resources=[]
        if 'machine_numbers' in f:
            for no in f['machine_numbers']:
                rid='resource_'+zid.removeprefix('zone_')+'_'+str(no).zfill(2);rr=rec('resource',rid)
                put(rr,'name',localized(f['zone'].removesuffix(' Zone')+' #'+str(no).zfill(2)),rel,'/facts/machine_numbers','expand explicitly numbered machine range; label from source zone')
                put(rr,'zone_id',zid,rel,'/facts/zone','FK to exact source zone')
                put(rr,'capacity_persons',max(cap),rel,'/facts/capacity_persons','parse explicit capacity maximum')
                put(rr,'physical_pool_key',rid,rel,'/facts/machine_numbers','stable local ID, NOT a WordPress key')
                pending(rr,'operational_status','รายการอุปกรณ์เดิมไม่ยืนยันสถานะ operational ปัจจุบัน; ไม่ใช้แทนสถานะจองสด')
                resources.append(rid)
            put(r,'resource_ids',resources,rel,'/facts/machine_numbers','expand explicitly numbered machines into resource FKs')
        else:pending(r,'resource_ids','ไม่มีรหัสเครื่องจริงในรายการนี้; ห้ามสร้างเครื่องเพิ่มหรือเดาว่าสองรายการใช้เครื่องเดียวกัน')
        pending(r,'occupancy_minutes','ไม่มีค่า occupancy ที่ผูกกับรายการนี้ในต้นฉบับ; โดยเฉพาะ VR 30 นาทีต้องตรวจการผูกเครื่องจริงก่อนเผยแพร่')
        services[row['content_id']]=r
        for i,label in enumerate(f['games']):
            gid=game(label,rel,'/facts/games/'+str(i));gr=rec('game_service','migrated_link_'+sid(row['content_id'])+'_'+sid(gid))
            put(gr,'game_id',gid,rel,'/facts/games/'+str(i),'FK to matching source game title')
            put(gr,'service_id',r['record_id'],rel,'/facts/service_label','FK to source service')
            put(gr,'offered',True,rel,'/facts/games/'+str(i),'explicit membership in service game list')
            if resources:put(gr,'installed_resource_ids',resources,rel,'/facts/machine_numbers','exact machine group listed for this game')
    for rel,row in canonical:
        kind=row['kind'];th=row['locales']['th']['fields'];en=row['locales']['en']['fields'];rid=row['content_id']
        if kind in {'game_profile','service_availability'}:coverage.append({'source':rel,'id':rid,'status':'typed','target':rid});continue
        if kind=='equipment':
            r=rec('equipment_model',rid,row['aliases']);put(r,'name',localized(th['item']),rel,'/locales/th/fields/item')
            blocks=[th[k] for k in ['what_th','how_to_use_th','note_th'] if th.get(k)]+th.get('use_cases_th',[])
            put(r,'usage',localized('\n'.join(blocks)),rel,'/locales/th/fields','join all equipment descriptions/use cases/notes without summarization')
            specs=[{'key':k,'value':str(v),'unit':None} for k,v in row['facts'].items() if k in {'zone','quantity'}]
            if specs:put(r,'specifications',specs,rel,'/facts','preserve literal zone/quantity attributes; no inferred hardware specifications')
        elif kind=='member':
            r=rec('person',rid,row['aliases']);put(r,'display_name',localized(th['name']),rel,'/locales/th/fields/name');put(r,'role',localized(th['role']),rel,'/locales/th/fields/role')
            put(r,'team',localized(row['facts']['group']),rel,'/facts/group')
        elif kind=='control_map':
            r=rec('control_set',rid,row['aliases']);f=row['facts'];gid=game(f['game'],rel,'/facts/game')
            put(r,'game_id',gid,rel,'/facts/game','FK to source title');put(r,'platform',f['platform'],rel,'/facts/platform')
            controls=th.get('controls',[]);english=en.get('controls',[])
            full='\n'.join(' | '.join(str(x.get(k,'')) for k in ['button','action_th','description_th','section']) for x in controls)
            enfull='\n'.join(' | '.join(str(x.get(k,'')) for k in ['button','action','description','section']) for x in english) or None
            put(r,'limitations',localized(full,enfull),rel,'/locales','lossless readable legacy controls; typed gesture/context remains unknown')
            pending(r,'bindings','ต้นฉบับไม่มี gesture/context แยกครบทุกแถว; เก็บปุ่มและคำอธิบายทั้งหมดใน limitations ไม่เดาว่าทุกปุ่มเป็น press')
        elif kind=='competition_document':
            f=row['facts'];r=rec('competition',rid,row['aliases']);gid=game(f['game'],rel,'/facts/game')
            put(r,'game_id',gid,rel,'/facts/game','FK to exact source game title');put(r,'event_name',localized(f['tournament']),rel,'/facts/tournament')
            put(r,'rulebook_release',f['document_id'],rel,'/facts/document_id')
            pending(r,'coverage','การย้ายครบทุก section ไม่ได้ยืนยันว่าเอกสารต้นฉบับครบหรือไม่ขัดกัน')
            for i,sec in enumerate(th['sections']):
                # Source section_index is NOT unique in RoV/VALORANT documents.
                # Preserve it as a field; use occurrence order for unique identity.
                sr=rec('competition_rule',rid+'_section_'+str(i+1).zfill(3))
                put(sr,'competition_id',rid,rel,'/facts/document_id','FK to source competition document')
                put(sr,'section_number',str(sec['section_index']),rel,'/locales/th/fields/sections/'+str(i)+'/section_index','legacy section_index → stable source order; not invented rule number')
                put(sr,'heading',localized(sec['section_title']),rel,'/locales/th/fields/sections/'+str(i)+'/section_title')
                put(sr,'text',localized(sec['text']),rel,'/locales/th/fields/sections/'+str(i)+'/text')
                pending(sr,'facet','คงหัวข้อ/ข้อความเดิม; ต้องตรวจหมวด facet และ dependency ก่อนนำเข้าเส้นทางตอบกติกาใหม่')
        elif kind=='service_closure':
            r=rec('closure',rid,row['aliases']);f=row['facts'];put(r,'local_date',f['date'],rel,'/facts/date');put(r,'state',f['status'],rel,'/facts/status')
            put(r,'reason',localized('\n'.join(th[k] for k in ['title','note'] if th.get(k))),rel,'/locales/th/fields','join full title and note')
            r['validity']={'state':'known','effective_from':f['date']+'T00:00:00+07:00','effective_until':(date.fromisoformat(f['date'])+timedelta(days=1)).isoformat()+'T00:00:00+07:00'}
        elif kind in {'knowledge_fact','service_fee_policy','policy_rule'}:
            category=row['facts'].get('route_category',row['category']);text=th.get('text') or th.get('answer')
            if not text or category in {'no_answer','english_support'}:
                coverage.append({'source':rel,'id':rid,'status':'preserved_engine_rule_not_business_fact','reason':'Routing/refusal/locale configuration retained byte-for-byte; not published as knowledge'});continue
            title=th.get('title') or next(iter(row['aliases']['th']),None) or row['facts'].get('intent',rid)
            r=faq('migrated_faq_'+sid(rid),title,text,rel,'/locales/th/fields','/locales/th/fields',en=en.get('text') or en.get('answer'),topic=category,aliases=row['aliases'])
            if kind=='service_fee_policy' or 'fee' in rid:pending(r,'scope_note','ข้อความราคาเดิมต้องตรวจความมีผลปัจจุบัน ห้ามเผยแพร่ FAQ นี้เพื่อเลี่ยง validation ของ rate')
        else:coverage.append({'source':rel,'id':rid,'status':'preserved_unmapped','reason':'No exact typed mapping'});continue
        coverage.append({'source':rel,'id':rid,'status':'typed' if kind not in {'knowledge_fact','service_fee_policy','policy_rule'} else 'full_text_faq','target':r['record_id']})

    # Additional curated facts not represented in canonical files.
    covered={row['content_id'] for rel,row in canonical}
    for rel in ['data/curated/curated_facts.jsonl','data/curated/curated_facts_data_fix_2026-06-29.jsonl','data/curated/curated_facts_service_fee_2026_aliases.jsonl']:
        for i,row in enumerate(read(rel)):
            if row['id'] in covered:continue
            r=faq('migrated_faq_'+sid(row['id']),row['title'],row['text'],rel,'/'+str(i)+'/title','/'+str(i)+'/text',topic=row['category'])
            if row['category']=='service_fee':pending(r,'scope_note','ราคาในข้อความเก่า ต้องใช้ช่วงวันที่ของต้นฉบับและตรวจข้อมูลปัจจุบันก่อนเผยแพร่')
            coverage.append({'source':rel,'id':row['id'],'status':'full_text_faq','target':r['record_id']});covered.add(row['id'])
    rel='data/sources/user_service_answers_20261008.json';raw=read(rel)
    confirmed_claims=read('data/curated/user_service_facts_20261008.json')['claims']
    represented_items={n for claim in confirmed_claims.values() if claim.get('status')=='user_confirmed' for n in claim['source_items']}
    for i,item in enumerate(raw['items']):
        # Preserve original shorthand in the source archive; avoid duplicate
        # runtime FAQs when a curated TH/EN claim explicitly references it.
        if item['number'] in represented_items:continue
        if item.get('status')=='user_confirmed' and item.get('answer'):
            faq('migrated_owner_faq_'+str(item['number']).zfill(2),item['question'],item['answer'],rel,'/items/'+str(i)+'/question','/items/'+str(i)+'/answer',topic='owner_service_answers')
        else:issues.append({'source':rel,'item':item['number'],'question':item['question'],'reason':'No confirmed owner answer; NOT inferred from similar question'})
    rel='data/curated/user_service_facts_20261008.json'
    user_facts=read(rel)
    if user_facts.get('pending_boundary'):issues.append({'source':rel,'reason':'Preserved owner policy boundary; not resolved by migration','boundary':user_facts['pending_boundary']})
    for key,claim in user_facts['claims'].items():
        if claim.get('status')!='user_confirmed':continue
        numbered=[(i,item) for i,item in enumerate(raw['items']) if item['number'] in claim['source_items']]
        if not numbered:raise ValueError('Owner claim has no original question '+key)
        r=rec('faq','migrated_owner_claim_'+key,{'th':[item['question'] for idx,item in numbered[1:]],'en':[]})
        idx,item=numbered[0]
        put(r,'question',localized(item['question']),'data/sources/user_service_answers_20261008.json','/items/'+str(idx)+'/question')
        put(r,'answer',localized(claim['answers']['th'],claim['answers'].get('en')),rel,'/claims/'+key+'/answers','complete curated owner answer; retain original translation status')
        put(r,'topic',claim['category'],rel,'/claims/'+key+'/category')
        r['localization']['en_status']='agent_translated'
    # Templates with placeholders are preserved, never interpolated to invent service scope.
    rel='data/curated/service_policy_answers.json'
    for key,claim in read(rel)['claims'].items():
        for mode,answer in claim['answers'].items():
            r=faq('migrated_policy_text_'+key+'_'+mode,key+' / '+mode,answer['th'],rel,'/claims/'+key,'/claims/'+key+'/answers/'+mode,en=answer.get('en'),topic='service_policy')
            if '{service}' in answer['th']:pending(r,'scope_note','มี placeholder {service} ในต้นฉบับ ต้องผูก service ก่อนเผยแพร่; ไม่เติมเป็นบริการทุกชนิดเอง')
    # Rental prices preserve workbook group/period, notes and currency exactly.
    rel='data/curated/zone_rental_fees_20261006.json';rent=read(rel)
    read(rent['source_file'])
    for grp,label in rent['customer_groups'].items():
        ar=rec('audience','audience_'+('external_org' if grp=='external' else 'internal_org'))
        put(ar,'name',localized(label),rel,'/customer_groups/'+grp)
        pending(ar,'eligibility','ต้นฉบับระบุชื่อกลุ่มหน่วยงาน แต่ไม่มีเงื่อนไข/หลักฐานยืนยันสิทธิ์ครบ')
    for i,row in enumerate(rent['rows']):
        zid=zone(row['label'],rel,'/rows/'+str(i)+'/label')
        for grp,prices in row['prices_thb'].items():
            for period,amount in prices.items():
                rid='rental_'+row['id']+'_'+grp+'_'+period;r=rec('rental_package',rid)
                put(r,'name',localized(row['label']+' '+rent['customer_groups'][grp]+' '+period),rel,'/rows/'+str(i)+'/label','label + source customer group + source period key')
                put(r,'zone_ids',[zid],rel,'/rows/'+str(i)+'/label','FK to exact source rental zone')
                put(r,'audience_id','audience_'+('external_org' if grp=='external' else 'internal_org'),rel,'/customer_groups/'+grp,'FK to source organization group')
                put(r,'period_label',period,rel,'/rows/'+str(i)+'/prices_thb/'+grp,'source period key')
                put(r,'amount_minor',amount*100,rel,'/rows/'+str(i)+'/prices_thb/'+grp+'/'+period,'THB ×100')
                put(r,'currency',rent['currency'],rel,'/currency')
                put(r,'equipment_included',localized(row['equipment_th'],row.get('equipment_en')),rel,'/rows/'+str(i),'localized equipment text')
                put(r,'room_seats',row['seats'],rel,'/rows/'+str(i)+'/seats')
                if row['id']=='all_zones':put(r,'terms',localized('\n'.join(x['text_th'] for x in rent['source_notes']),'\n'.join(x['text_en'] for x in rent['source_notes'])),rel,'/source_notes','notes apply only to all_zones_row, not individual zones')
                pending(r,'duration_minutes','ครึ่งวัน/เต็มวันในไฟล์ไม่มีจำนวนชั่วโมง; ไม่ตั้ง 4/8 ชั่วโมงเอง')
                issues.append({'record_id':rid,'field':'validity','reason':'Workbook effective_from/effective_until are null; received_on is NOT a validity start'})
    # Dated regular fee table: numeric extraction is independently checked later.
    rel='data/content/services/curated_service_fee_2026_full_table.json';fee=read(rel);text=fee['locales']['th']['fields']['text']
    groups=[('psu_student_staff','PSU Student and Staff'),('psu_alumni_general_student','PSU Alumni and General Student'),('general_adult','General Adult')]
    for group,label in groups:
        r=rec('audience','audience_'+group);put(r,'name',localized(label,label),rel,'/locales/th/fields/text','explicit group label substring')
    rows=re.findall(r'(PlayStation 5|Nintendo Switch|Cockpit|VR) (\d+) (ชั่วโมง|นาที) (\d+)(?:-(\d+))? คน: ([^.]+)\.',text)
    if len(rows)!=6:raise ValueError('Fee table expected 6 explicitly scoped rows; stop instead of guessing')
    for platform,qty,unit,lo,hi,body in rows:
        duration=int(qty)*(60 if unit=='ชั่วโมง' else 1);hi=hi or lo
        matches=[r for r in services.values() if value(r,'platform')==platform and value(r,'session_minutes')==duration and value(r,'capacity_max')==int(hi)]
        if platform=='Nintendo Switch' and hi=='4':matches=[services['availability_nintendo_1_4']]
        if platform=='Cockpit':matches=[services['availability_cockpit_01_02']]
        if len(matches)!=1:raise ValueError('Ambiguous fee service '+str((platform,duration,lo,hi)))
        amounts=[int(x) for x in re.findall(r'(\d+) บาท',body)]
        if len(amounts)!=3:raise ValueError('Fee row amount scope not explicit')
        for (group,label),amount in zip(groups,amounts):
            rid='migrated_rate_'+sid(platform)+'_'+str(duration)+'_'+lo+'_'+hi+'_'+group;r=rec('rate',rid)
            for k,v in [('service_id',matches[0]['record_id']),('audience_id','audience_'+group),('amount_minor',amount*100),('currency','THB'),('duration_minutes',duration),('persons_min',int(lo)),('persons_max',int(hi))]:put(r,k,v,rel,'/locales/th/fields/text','explicit fee row parse; amount THB ×100; FK matching duration and capacity')
            r['validity']={'state':'known','effective_from':'2026-02-01T00:00:00+07:00','effective_until':'2026-04-01T00:00:00+07:00'}
            pending(r,'unit','ต้นฉบับระบุคนและเวลา แต่ยังไม่ตั้ง billing basis ต่อคน/เครื่อง/กลุ่มเอง')
            pending(r,'calculation_rule','ไม่อนุมานว่าขยายราคาเป็นหลายชั่วโมงได้')
    # Weekly schedules preserve disagreement instead of selecting one source.
    rel='booking_dashboard/center_schedule.json';dashboard=read(rel)
    read('app/calendar/service_calendar.py')
    from app.calendar.service_calendar import regular_service_slots
    for day,config in dashboard['weekly'].items():
        wd=int(day);slots=regular_service_slots(date(2026,10,12)+timedelta(days=wd))
        opens=[{'start':s['start'],'end':s['end']} for s in slots if s['state']=='open']
        maintenance=[{'start':s['start'],'end':s['end']} for s in slots if s['state']=='maintenance']
        dashboard_opens=[{'start':a,'end':b} for a,b in config['open_periods']]
        r=rec('schedule','migrated_schedule_'+day)
        put(r,'weekday',wd,rel,'/weekly/'+day,'numeric weekly key')
        put(r,'reason',localized(config['reason']),rel,'/weekly/'+day+'/reason')
        for key in ['open_periods','bookable_periods']:
            if dashboard_opens==opens:put(r,key,opens,rel,'/weekly/'+day+'/open_periods','period tuples → start/end objects')
            else:
                payload={'dashboard':dashboard_opens,'chat_calendar':opens,'source_files':[rel,'app/calendar/service_calendar.py']}
                snap=canonical_json(payload);source_id='r63_schedule_conflict_'+day
                src={'source_id':source_id,'kind':'derived_curated','path':'migration://'+source_id,'sha256':hashlib.sha256(snap.encode()).hexdigest(),'authority_for':['schedule'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
                sources.append({'source':src,'snapshot':snap})
                r['fields'][key]={'status':'conflicted','value':None,'evidence_refs':[{'source_id':source_id,'locator':'/dashboard'},{'source_id':source_id,'locator':'/chat_calendar'}],'note':'สองต้นทางใช้ช่วงเวลาไม่ตรงกัน; รวมช่วงพักเที่ยงและเวลา Maintenance ต้องตรวจความหมายของ open/bookable ไม่เลือกแทนเจ้าของ'}
                issues.append({'record_id':r['record_id'],'field':key,'reason':'Dashboard vs chat calendar mismatch','values':payload})
        pending(r,'maintenance_periods','เก็บช่วง maintenance จาก chat calendar ในรายงาน; รอผูกนโยบายกลางกับ Dashboard')
        issues.append({'record_id':r['record_id'],'field':'validity','reason':'No effective date for weekly schedule in source','chat_maintenance':maintenance})

    # Evidence sources embed byte-backed originals and the complete transformation map.
    for rid,r in drafts.items():
        rows=[x for x in mapping if x['record_id']==rid]
        if not rows:continue
        mapped={x['field']:x['mapped_value'] for x in rows}
        payload={'mapped_fields':mapped,'field_lineage':rows,'migration_status':'draft_only_not_factually_approved'}
        snap=canonical_json(payload);source_id='r63_'+hashlib.sha256((rid+snap).encode()).hexdigest()[:28]
        src={'source_id':source_id,'kind':'derived_curated','path':'migration://r63/'+rid,'sha256':hashlib.sha256(snap.encode()).hexdigest(),'authority_for':[r['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
        sources.append({'source':src,'snapshot':snap})
        for key in mapped:r['fields'][key]['evidence_refs']=[{'source_id':source_id,'locator':'/mapped_fields/'+key}]
    print('Prepared',len(drafts),'records',len(mapping),'fields',flush=True)
    for item in sources:store.add_source(item['source'],item['snapshot'],actor='r63-draft-migration')
    pending_records=list(drafts.values());saved=[];skipped=[]
    while pending_records:
        remaining=[];errors={}
        for r in pending_records:
            old=existing.get(r['record_id'])
            if old and canonical_json(r)==canonical_json(old):skipped.append(r['record_id']);continue
            try:saved.append(store.save(r,actor='r63-draft-migration',expected_version=old['revision'] if old else 0,change_note='Exact legacy migration into separate review database; original revisions retained'))
            except ValueError as e:remaining.append(r);errors[r['record_id']]=str(e)
        if len(remaining)==len(pending_records):dump('IMPORT_ERRORS.json',errors);raise ValueError('Unresolved draft validation/import errors')
        pending_records=remaining
    after=store.snapshot()
    assert before['active']==after['active'] and before['release']==after['release']
    bundle={'schema_version':'studio-content-3.0','sources':sources,'records':list(drafts.values()),'mode':'draft_only','base_database':'before.sqlite','no_publication':True}
    dump('migration.bundle.json',bundle);dump('FIELD_LINEAGE.json',mapping);dump('SOURCE_MANIFEST.json',list(files.values()));dump('COVERAGE.json',coverage);dump('PENDING.json',issues)
    result={'saved':len(saved),'existing_unchanged':len(skipped),'draft_kinds':dict(collections.Counter(r['kind'] for r in drafts.values())),'canonical_sources':len(canonical),'source_files':len(files),'mapped_fields':len(mapping),'original_heads':len(existing),'result_heads':len(store.list_heads()),'active_release_unchanged':True,'new_approvals':0,'new_releases':0,'db':str(db),'pending':len(issues)}
    dump('MIGRATION_RESULT.json',result);print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
