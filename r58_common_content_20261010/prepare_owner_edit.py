from pathlib import Path
import datetime,json,hashlib,shutil
OUT=Path(__file__).resolve().parent
PACK=OUT/'ready_package/PSU_Esports_Chatbot_Local';CAND=OUT/'system/PSU_Esports_Chatbot_Local'
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
RUN=OUT/('owner_edit_20261011_'+datetime.datetime.now().strftime('%H%M%S'));RUN.mkdir()
names=['app/knowledge/common/store.py','app/knowledge/common/owner_server.py','app/knowledge/common/ui/owner.js','app/knowledge/common/ui/index.html','app/knowledge/common/ui/owner.css']
before={}
for role,base in [('ready',PACK),('candidate',CAND),('source',ROOT)]:
    for name in names:
        f=base/name;b=RUN/'before'/role/name;b.parent.mkdir(parents=True,exist_ok=True);data=f.read_bytes();b.write_bytes(data);before[str(f)]=hashlib.sha256(data).hexdigest()
stage=RUN/'stage'
for name in names:
    f=stage/name;f.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(PACK/name,f)

f=stage/names[0];s=f.read_text(encoding='utf-8')
s=s.replace('CATALOG\n','CATALOG,aware\n',1)
s=s.replace('def save(self,record,*,actor,expected_version):','def save(self,record,*,actor,expected_version,change_note=None):\n        if change_note is not None and (not isinstance(change_note,str) or len(change_note)>1000):raise ValueError("Change note must be text of at most 1000 characters")')
s=s.replace("{'record_id':rid,'version':head+1,'hash':h})", "{'record_id':rid,'version':head+1,'hash':h,'change_note':(change_note or '').strip()})",1)
insert='''    @staticmethod
    def _revision(row):
        if row is None:raise ValueError('Unknown revision')
        item=dict(row);record=json.loads(item.pop('payload'))
        if digest(record)!=item['hash']:raise ValueError('Revision integrity mismatch')
        return {**item,'record':record}
    def revision(self,rid,version):
        if type(version) is not int or version<1:raise ValueError('Positive revision number required')
        with self.connect() as c:
            row=c.execute('SELECT r.*,a.hash AS approved_hash FROM cc_revisions r LEFT JOIN cc_approvals a ON a.record_id=r.record_id AND a.version=r.version WHERE r.record_id=? AND r.version=?',(rid,version)).fetchone()
            return self._revision(row)
    def edit_context(self,rid,limit=50):
        if type(limit) is not int or not 1<=limit<=100:raise ValueError('History limit must be 1 to 100')
        with self.connect() as c:
            row=c.execute('SELECT r.*,h.withdrawn,a.hash AS approved_hash FROM cc_revisions r JOIN cc_heads h ON h.record_id=r.record_id AND h.head=r.version LEFT JOIN cc_approvals a ON a.record_id=r.record_id AND a.version=r.version WHERE r.record_id=?',(rid,)).fetchone()
            latest=self._revision(row)
            meta=dict(c.execute('SELECT key,value FROM cc_meta'))
            release=c.execute('SELECT * FROM cc_releases WHERE release_id=?',(meta['active'],)).fetchone()
            published=None
            if release:
                data=json.loads(release['payload'])
                if digest(data)!=release['hash'] or data['schema_version']!=VERSION:raise ValueError('Release integrity/version mismatch')
                if not latest['withdrawn']:published=data['records'].get(rid)
            notes={}
            for audit in c.execute("SELECT detail FROM cc_audit WHERE event='save' AND json_extract(detail,'$.record_id')=? ORDER BY id",(rid,)):
                d=json.loads(audit[0]);notes[d['version']]=d.get('change_note','')
            history=[]
            for row in c.execute('SELECT r.version,r.hash,r.actor,r.at,a.hash AS approved_hash FROM cc_revisions r LEFT JOIN cc_approvals a ON a.record_id=r.record_id AND a.version=r.version WHERE r.record_id=? ORDER BY r.version DESC LIMIT ?',(rid,limit)):
                item=dict(row);item['change_note']=notes.get(item['version'],'');item['published']=bool(published and published['revision']==item['version']);history.append(item)
            total=c.execute('SELECT count(*) FROM cc_revisions WHERE record_id=?',(rid,)).fetchone()[0]
            return {'latest':latest,'published':published,'active':meta['active'],'epoch':int(meta['epoch']),'history':history,'total_revisions':total}
'''
s=s.replace('    def approve(self,rid,version,expected_hash,*,actor):',insert+'    def approve(self,rid,version,expected_hash,*,actor):',1)
s=s.replace("records[rid]=json.loads(r['payload'])", "candidate=json.loads(r['payload'])\n                start=candidate['validity'].get('effective_from')\n                if rid in records and start and aware(start)>aware(now()):raise ValueError('Future replacement must remain a draft until its effective date: '+rid)\n                records[rid]=candidate",1)
f.write_text(s,encoding='utf-8')

f=stage/names[1];s=f.read_text(encoding='utf-8')
s=s.replace('translation_reviewed=False):','translation_reviewed=False,change_note=None):',1)
s=s.replace('    # Attestations are immutable',"    if change_note is not None and (not isinstance(change_note,str) or len(change_note)>1000):raise ValueError('Change note must be text of at most 1000 characters')\n    # Attestations are immutable",1)
s=s.replace('store.save(record,expected_version=expected_version,actor=actor)','store.save(record,expected_version=expected_version,actor=actor,change_note=change_note)',1)
s=s.replace("if path=='/api/record':return", "if path=='/api/edit-context':return self.reply(200,store.edit_context(parse_qs(parsed.query).get('id',[''])[0]))\n                if path=='/api/revision':return self.reply(200,store.revision(parse_qs(parsed.query).get('id',[''])[0],int(parse_qs(parsed.query).get('version',['0'])[0])))\n                if path=='/api/record':return",1)
s=s.replace("translation_reviewed=body.get('translation_reviewed') is True))", "translation_reviewed=body.get('translation_reviewed') is True,change_note=body.get('change_note')))",1)
f.write_text(s,encoding='utf-8')

f=stage/names[3];s=f.read_text(encoding='utf-8')
s=s.replace('<h2>รายการข้อมูล</h2>','<h2>เพิ่มหรือแก้ไขข้อมูล</h2><button id="edit_existing" class="secondary">✎ แก้ไขข้อมูลเดิม</button><p id="list_help">เลือกหมวด แล้วค้นหาชื่อรายการเดิมด้านล่างเพื่อแก้ไข</p>',1)
s=s.replace('<div id="editor" hidden><h2 id="heading"></h2>', '''<div id="editor" hidden><h2 id="heading"></h2>
<div id="edit_tools" class="edit-tools" hidden><h3 id="edit_heading">แก้ไขรายการเดิม</h3><p id="edit_status"></p><p>แก้เฉพาะช่องที่เปลี่ยน รหัสเดิมและข้อมูลที่เชื่อมจะยังอยู่ ฉบับเก่าเก็บไว้ตรวจย้อนหลัง</p><p id="edit_timing"></p><label>เหตุผลที่แก้ไข (ไม่บังคับ)<textarea id="change_note" maxlength="1000" placeholder="เช่น ปรับราคาตามประกาศใหม่ หรือแก้รายละเอียดเกมจากเอกสารล่าสุด"></textarea></label><button id="compare_changes" class="secondary">ดูสิ่งที่เปลี่ยนก่อนบันทึก</button><button id="view_history" class="secondary">ดูประวัติฉบับเก่า</button><div id="change_summary"></div></div>''',1)
s=s.replace('กด “เพิ่ม…” หรือเลือกข้อมูลเดิมเพื่อแก้ไข','กด “เพิ่ม…” สำหรับข้อมูลใหม่ หรือกด “แก้ไขข้อมูลเดิม” แล้วค้นหาชื่อรายการ',1)
s=s.replace('รหัสรายการ (ตั้งครั้งเดียว)','รหัสรายการ (รายการเดิมใช้รหัสเดิม)',1)
f.write_text(s,encoding='utf-8')

f=stage/names[2];s=f.read_text(encoding='utf-8')
s=s.replace('previewHistory=[];','previewHistory=[],editContext=null;',1)
s=s.replace("'Stale English review':'ข้อความเปลี่ยนแล้ว ต้องตรวจคำแปลอังกฤษฉบับนี้ใหม่'", "'Stale English review':'ข้อความเปลี่ยนแล้ว ต้องตรวจคำแปลอังกฤษฉบับนี้ใหม่','Stale or withdrawn revision':'มีคนบันทึกฉบับใหม่แล้ว หรือรายการนี้ถูกถอน กรุณาเปิดรายการล่าสุดก่อนแก้','Future replacement must remain a draft until its effective date':'ฉบับใหม่ยังไม่ถึงวันเริ่มใช้ เก็บเป็นร่างไว้ก่อน แล้วเผยแพร่เมื่อถึงวัน เพื่อให้แชทยังอ่านฉบับเดิม','Change note must be text of at most 1000 characters':'เหตุผลที่แก้ไขยาวได้ไม่เกิน 1000 ตัวอักษร'")
s=s.replace("showGuide(r.kind);updateReadiness();", "showGuide(r.kind);updateReadiness();renderEditTools();",1)
s=s.replace("let x=await api('/api/record?id='+encodeURIComponent(r.record_id));render(x.record,x);", "await openExisting(r.record_id);",1)
s=s.replace("let b=node('button',(r.label||r.record_id)", "let b=node('button','✎ แก้ไข: '+(r.label||r.record_id)",1)
s=s.replace("dirty=false;record=null;saved=null;$('editor').hidden", "dirty=false;record=null;saved=null;editContext=null;$('editor').hidden",1)
s=s.replace("return;render(await api('/api/template?kind='+$('kind').value));", "return;editContext=null;render(await api('/api/template?kind='+$('kind').value));",1)
s=s.replace("translation_reviewed:$('translation_reviewed').checked});let loaded=await api('/api/record?id='+encodeURIComponent(x.record_id));render(loaded.record,loaded);", "translation_reviewed:$('translation_reviewed').checked,change_note:$('change_note').value});await openExisting(x.record_id);",1)
s=s.replace("let x=await api('/api/record?id='+saved.record_id);render(x.record,x);", "await openExisting(saved.record_id);",1)
s=s.replace("});await refresh();message('เผยแพร่แล้ว", "});await openExisting(saved.record_id);await refresh();message('เผยแพร่แล้ว",1)
extra=r'''
async function openExisting(id){let x=await api('/api/edit-context?id='+encodeURIComponent(id));editContext=x;render(x.latest.record,x.latest);}
function renderEditTools(){let editing=!!saved;$('edit_tools').hidden=!editing;$('change_note').value='';$('change_summary').replaceChildren();if(!editing)return;$('edit_heading').textContent='✎ แก้ไขข้อมูลเดิม • ฉบับ '+saved.version;let p=editContext?.published;$('edit_status').textContent=p?'ฉบับที่แชทใช้: '+p.revision+' • ร่างล่าสุด: '+saved.version:'รายการนี้ยังไม่มีฉบับเผยแพร่ในฐานกลาง';$('edit_timing').textContent=['rate','rental_package','policy','competition_rule','competition','schedule','closure','news'].includes(record.kind)?'ถ้ามีวันเริ่มใช้ใหม่ ให้ปรับ “ข้อมูลนี้เริ่มใช้เมื่อไหร่?” ตามประกาศจริง ราคาหรือกฎที่เริ่มในอนาคตบันทึกเป็นร่างได้ แต่ยังไม่มีการเผยแพร่อัตโนมัติตามเวลา ต้องกดเผยแพร่เมื่อถึงวันเริ่มใช้':'แก้ชื่อหรือรายละเอียดได้โดยใช้รายการเดิม ถ้าเปลี่ยนเป็นอีกเกม อีกบริการ หรืออีกกลุ่มราคา ให้สร้างรายการใหม่';$('save').textContent='บันทึกเป็นฉบับร่างใหม่';}
function comparable(f){return {status:f?.status||'unknown',value:f?.status==='known'?f.value:null,note:f?.note||''};}
function recordChanges(a,b){let changes=[];for(let f of catalog[b.kind].fields){let old=comparable(a.fields[f.key]),next=comparable(b.fields[f.key]);if(JSON.stringify(old)!==JSON.stringify(next))changes.push({label:fieldLabel(f,b.kind),key:f.key,before:old,after:next,field:true});}for(let [key,label] of [['aliases','ชื่อที่ลูกค้าเรียก'],['validity','ช่วงวันที่มีผล']])if(JSON.stringify(a[key])!==JSON.stringify(b[key]))changes.push({label,key,before:a[key],after:b[key]});let lang=r=>({source_language:r.localization.source_language,en_status:r.localization.en_status});if(JSON.stringify(lang(a))!==JSON.stringify(lang(b)))changes.push({label:'สถานะภาษา',key:'localization',before:lang(a),after:lang(b)});return changes;}
function readableChange(v,key,field=false){let root=node('div');if(field){let statusText={known:'มีข้อมูลยืนยัน',unknown:'ยังไม่ทราบ',not_applicable:'ไม่เกี่ยวข้อง',conflicted:'ข้อมูลขัดกัน'};root.append(node('strong',statusText[v.status]));if(v.status==='known')root.append(key==='amount_minor'?node('p',(v.value/100).toLocaleString('th-TH',{minimumFractionDigits:2,maximumFractionDigits:2})+' บาท'):exampleView(v.value));if(v.note)root.append(node('small','หมายเหตุ: '+v.note));}else if(key==='validity'){root.append(node('p',v.state==='known'?'ยืนยันช่วงวันที่แล้ว':'ยังไม่ยืนยันช่วงวันที่'));for(let [k,l] of [['effective_from','เริ่มใช้'],['effective_until','สิ้นสุด']])root.append(node('p',l+': '+(v[k]?new Date(v[k]).toLocaleString('th-TH',{timeZone:'Asia/Bangkok'})+' (เวลาไทย)':'ยังไม่กำหนด')));}else if(key==='localization'){root.append(node('p','ภาษาต้นทาง: '+({th:'ไทย',en:'อังกฤษ',mixed:'ทั้งสองภาษา'}[v.source_language]||v.source_language)),node('p','คำแปล: '+({missing:'ยังไม่มี',draft:'ร่าง',agent_translated:'แปลโดยระบบ',reviewed:'ตรวจแล้ว',stale:'ต้องตรวจใหม่'}[v.en_status]||v.en_status)));}else root.append(exampleView(v));return root;}
function showComparison(a,b,host,caption){host.replaceChildren();host.append(node('h3',caption));let changes=recordChanges(a,b);if(!changes.length){host.append(node('p','ยังไม่มีเนื้อหาที่เปลี่ยนจากฉบับที่ใช้เปรียบเทียบ'));return;}let table=node('table');table.className='changes-table';let head=node('tr');['ช่องที่เปลี่ยน','ก่อนแก้','หลังแก้'].forEach(t=>head.append(node('th',t)));table.append(head);for(let c of changes){let row=node('tr'),old=node('td'),next=node('td');old.append(readableChange(c.before,c.key,c.field));next.append(readableChange(c.after,c.key,c.field));row.append(node('th',c.label),old,next);table.append(row);}let wrap=node('div');wrap.className='table-scroll';wrap.append(table);host.append(wrap);}
$('compare_changes').onclick=()=>task(async()=>{if(!saved)return;let base=editContext?.published||record;showComparison(base,collect(),$('change_summary'),'เปรียบเทียบกับ '+(editContext?.published?'ฉบับที่แชทใช้ '+base.revision:'ร่างที่เปิดมา '+saved.version));});
$('edit_existing').onclick=()=>{message('เลือกหมวดทางซ้าย แล้วค้นหาชื่อหรือเลือกปุ่ม “✎ แก้ไข…” ของรายการเดิมด้านล่าง');$('search').focus();};
$('change_note').addEventListener('input',()=>dirty=true);
$('view_history').onclick=()=>task(async()=>{if(!saved)return;let x=await api('/api/edit-context?id='+encodeURIComponent(saved.record_id));let d=node('dialog');d.className='history-dialog';let close=node('button','ปิดประวัติ');close.onclick=()=>{d.close();d.remove();};d.append(node('h2','ประวัติข้อมูลเดิม (ดูอย่างเดียว)'),node('p','แสดงล่าสุด '+x.history.length+' จาก '+x.total_revisions+' ฉบับ ประวัติเก่ายังอยู่ในฐานข้อมูล การเปิดดูไม่เปลี่ยนข้อมูลในแชท'),close);let list=node('div'),view=node('div');for(let h of x.history){let line=node('div');line.className='history-row';let btn=node('button','ดูฉบับ '+h.version+(h.published?' • แชทใช้อยู่':''));let info=node('p',new Date(h.at).toLocaleString('th-TH',{timeZone:'Asia/Bangkok'})+' เวลาไทย • ผู้แก้: '+h.actor+(h.change_note?' • เหตุผล: '+h.change_note:''));btn.onclick=async()=>{btn.disabled=true;try{let v=await api('/api/revision?id='+encodeURIComponent(saved.record_id)+'&version='+h.version);view.replaceChildren();view.append(node('h3','ข้อมูลในฉบับ '+h.version),node('p','ดูอย่างเดียว — ไม่ได้คืนค่าหรือเผยแพร่ฉบับนี้'));for(let f of catalog[v.record.kind].fields){let section=node('div');section.className='history-field';section.append(node('h4',fieldLabel(f,v.record.kind)),readableChange(comparable(v.record.fields[f.key]),f.key,true));view.append(section);}view.append(node('h4','ช่วงวันที่มีผล'),readableChange(v.record.validity,'validity'));}catch(e){view.replaceChildren(node('p',userError(e.message)));}finally{btn.disabled=false;}};line.append(btn,info);list.append(line);}d.append(list,view);d.addEventListener('close',()=>d.remove());document.body.append(d);d.showModal();});
'''
s+='\n'+extra
# New records should restore the new-record button text after editing an existing one.
s=s.replace("if(!editing)return;", "if(!editing){$('save').textContent='บันทึกฉบับร่าง';return;}",1)
f.write_text(s,encoding='utf-8')
f=stage/names[4];s=f.read_text(encoding='utf-8')+'''\n.edit-tools{padding:16px;border:1px solid #b9d0e5;border-radius:10px;background:#f2f8fd;margin:16px 0}.edit-tools h3{margin-top:0}.edit-tools p{line-height:1.7}.table-scroll{overflow-x:auto}.changes-table{width:100%;border-collapse:collapse;background:white;font-size:14px}.changes-table th,.changes-table td{padding:12px;border:1px solid #ccd9e7;text-align:left;vertical-align:top;min-width:140px;overflow-wrap:anywhere}.changes-table th{color:#183b61}.changes-table td{max-width:420px}.history-dialog{width:min(900px,90vw);max-width:900px;max-height:85vh;overflow:auto}.history-row{border-bottom:1px solid #ccd9e7;padding:10px}.history-row p{font-size:14px}.history-field{border-bottom:1px solid #dde5ee;padding:12px}.history-field h4{margin:5px 0}#list_help{font-size:14px;line-height:1.6}\n''';f.write_text(s,encoding='utf-8')

for base in (CAND,PACK):
    for name in names:
        f=base/name
        if hashlib.sha256(f.read_bytes()).hexdigest()!=before[str(f)]:raise SystemExit('Changed while preparing: '+str(f))
        shutil.copy2(stage/name,f)
plan={'run':str(RUN),'stage':str(stage),'names':names,'before_hashes':before,'ready':str(PACK),'candidate':str(CAND),'root':str(ROOT)}
(OUT/'owner_edit_latest.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'run':str(RUN),'files':names,'ready_candidate_updated':True},ensure_ascii=False))
