import json,hashlib,difflib,subprocess,urllib.request,statistics
from pathlib import Path
from datetime import datetime
from two_turn_grader_r39 import OUT
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
PACKAGE=OUT/'release_r39_3'/'PSU_Esports_Chatbot_Local'
with urllib.request.urlopen('http://127.0.0.1:8094/health',timeout=5) as r:health=json.load(r)
assert health['runtime']['version']=='2026.10.06-two-turn-r39.3'
started=datetime.fromisoformat(health['runtime']['started_at']).timestamp()
api=[(p,json.loads(p.read_text(encoding='utf-8'))) for p in OUT.glob('api_summary_8094_*.json') if p.stat().st_mtime>started]
base=max((x for x in api if x[1]['case_file']=='cases.json'),key=lambda x:x[0].stat().st_mtime)
extra=max((x for x in api if x[1]['case_file']=='extra_cases_r39.json'),key=lambda x:x[0].stat().st_mtime)
negative_path=max((p for p in OUT.glob('negative_summary_*.json') if p.stat().st_mtime>started),key=lambda p:p.stat().st_mtime)
negative=json.loads(negative_path.read_text(encoding='utf-8'))
for result in (base[1],extra[1],negative):assert result['passed']==result.get('conversations',result.get('cases'))
runtime_files=['app/session/context_resolver.py','app/session/conversation_store.py','app/pipeline/bilingual_english.py','app/pipeline/engine.py','app/pipeline/game_edition_guard.py']
hashes={}
for f in runtime_files:
    a=hashlib.sha256((ROOT/f).read_bytes()).hexdigest();b=hashlib.sha256((PACKAGE/f).read_bytes()).hexdigest()
    assert a==b,f
    hashes[f]=dict(source_sha256=a,package_sha256=b,match=True)
diff=[]
for f in runtime_files:
    old=OUT/'before'/f
    before=old.read_text(encoding='utf-8').splitlines(keepends=True) if old.exists() else []
    after=(ROOT/f).read_text(encoding='utf-8').splitlines(keepends=True)
    diff.extend(difflib.unified_diff(before,after,fromfile='before/'+f,tofile='after/'+f))
with (OUT/'changes_this_turn_final.diff').open('x',encoding='utf-8') as stream:stream.write(''.join(diff))
git=subprocess.run(['git','status','--short'],cwd=ROOT,capture_output=True,text=True)
with (OUT/'git_status_after_final.txt').open('x',encoding='utf-8') as stream:stream.write(git.stdout+git.stderr)
check=subprocess.run(['git','diff','--check'],cwd=ROOT,capture_output=True,text=True)
baseline=json.loads((OUT/'baseline_final_oracle_regrade_r38_5.json').read_text(encoding='utf-8'))
times=[];responses=[]
for _,s in (base,extra):
    for line in (OUT/s['raw']).read_text(encoding='utf-8').splitlines():
        record=json.loads(line);times.append(record['elapsed_sec']);responses.append(record['response'])
sorted_times=sorted(times);p95=sorted_times[min(len(times)-1,int(.95*len(times)))]
summary=dict(runtime=health['runtime'],baseline=dict(passed=baseline['passed'],conversations=baseline['conversations']),
             final_normal=dict(passed=base[1]['passed'],conversations=base[1]['conversations'],summary=base[0].name),
             final_extra=dict(passed=extra[1]['passed'],conversations=extra[1]['conversations'],summary=extra[0].name),
             final_negative=dict(passed=negative['passed'],cases=negative['cases'],summary=negative_path.name),
             final_api_requests=base[1]['requests']+extra[1]['requests']+negative['requests'],
             positive_latency_seconds=dict(min=min(times),median=statistics.median(times),p95=p95,max=max(times)),
             positive_timeouts=sum(bool(r.get('timed_out')) for r in responses),package_source_hashes=hashes,
             git_diff_check=dict(exit_code=check.returncode,stdout=check.stdout,stderr=check.stderr),
             owner_review_completed=False,live_wordpress_status_truth_checked_this_turn=False)
for file,data in [('health_r39_3_final.json',health),('FINAL_SUMMARY_R39_3.json',summary)]:
    with (OUT/file).open('x',encoding='utf-8') as stream:json.dump(data,stream,ensure_ascii=False,indent=2)
rows=[]
for r in base[1]['results']+extra[1]['results']:
    c=r['case'];rows.append('| '+ ' | '.join([c['id'],c['initial'],c['choice'],r['second_mode'],'ผ่าน' if r['passed'] else 'ไม่ผ่าน'])+' |')
report=f'''# รายงานบทสนทนาสองรอบและปัญหาคงเหลือ — r39.3

วันที่: 6 ตุลาคม 2026 เวลาไทย โฟลเดอร์หลักฐานคงชื่อ `20261005` ตามชื่อที่สร้างตอนเริ่มรอบ

## สรุป

ตรวจ r38.5 จริงผ่านเว็บ 36 บทสนทนา/72 คำขอ ใช้เกณฑ์ครบทั้งสองรอบผ่าน **23/36** หลังแก้ r39.3 ผ่านชุดเดิม **36/36** ชุดคำถามเพิ่มเติม **17/17** และเคสกันผิด/เปลี่ยนเรื่อง/แยก session **8/8** รวมเว็บฉบับสุดท้าย **123 คำขอ** จาก 61 เคส (53 บทสนทนาปกติหรือเพิ่มรูปแบบ และ 8 เคสตรวจพฤติกรรมผิด/แยก session)

ผลนี้ยืนยันตามเงื่อนไขที่ตรวจ ไม่ใช่การรับรองคำถามทุกแบบหรือข้อเท็จจริงทุกข้อมูลในศูนย์

## ปัญหาที่พบและเหตุผลที่เคยตอบแบบนั้น

| ปัญหา | สาเหตุ/การเลือกทางเดิม | ผลที่แก้ |
|---|---|---|
| ถามปุ่มแล้วพิมพ์ VALORANT/Mario Kart/Beat Saber | ตัวตรวจชื่อเกมอยู่ก่อนตัวเติมส่วนที่ขาด จึงถือว่าเป็นคำถามชื่อเกมใหม่ และไปคำอธิบายเกม | ตรวจงานที่กำลังรอก่อนรับชื่อเกมเป็นคำถามใหม่ |
| อังกฤษ Show me the game controls ตอบ 42 เกม | ไม่มีเส้นทางขอชื่อเกมสำหรับคำขอปุ่มทั่วไป ทำให้ show/game เข้าเส้นทางรายชื่อเกม | มีคำถามยืนยันชื่อเกมสำหรับคำขอปุ่มทั่วไปและรูปประโยคอื่น |
| What does PC have? ไม่ถามเลือกเรื่อง | เส้นทางอังกฤษเลือกเกม PC ทันที ต่างจากไทย | ถาม games/equipment/prices/booking แล้วเติมเฉพาะหัวข้อที่เลือก |
| ตอบ prices/booking แล้วไม่เข้าใจ | การรับคำตอบสั้นและการสร้างคำถามจากตัวเลือกก่อนหน้ายังไม่ครบอังกฤษ | รองรับ prices/fees/rates/booking และสร้างคำถามอังกฤษ |
| เลือก PS5 หลังรายชื่อเกมแล้วหลุดเรื่อง | ไม่มีตัวกรองโซนจากตัวเลือกสั้นของรายการล่าสุด | คงงานรายชื่อเกมและกรองโซน มี assertion กันข้อมูลโซนอื่น |
| Tell me about Call of Duty → Modern Warfare III กลายเป็นรายการเกม/ยืนยันมีเกมอย่างเดียว | รายการตระกูลและ operation รายละเอียดไม่ถูกเก็บร่วมกัน | ให้เลือกจากสองชื่อที่มีจริงและตอบรายละเอียดของชื่อที่เลือก รวมกรณีถามปุ่มของตระกูลด้วย |
| TEKKEN 9 ตอบ TEKKEN 8 | ตัวเติมบริบทกับตัวค้นหามีคนละเส้นทาง ถึงกัน fuzzy ในบริบทแล้ว ตัวค้นหายังจับ alias tekken | ตรวจเลขภาคก่อนค้น/แต่งคำตอบ แจ้งภาคที่ยังไม่มีหลักฐานแทนเปลี่ยนเป็น 8 |
| Minecraft หลังถามปุ่ม แสดง catalog/ถามชื่อซ้ำ | ชื่อไม่รู้จักตกออกจากงานปุ่ม และ fallback ไม่แยกได้รับชื่อแล้วแต่ไม่มีข้อมูล | คงงานปุ่มกับชื่อที่ยังไม่ยืนยัน และตอบสถานะไม่มีข้อมูลสำหรับเกมที่ระบุ |

ชื่อเกมพิมพ์คลาดเคลื่อนใช้ resolver เดิมและเงื่อนไขคะแนน/ส่วนต่าง ไม่เพิ่ม alias ให้ทุกประโยค รูปประโยคทั่วไปยังมีการใช้คำบ่งชี้งานและตัวกรองเพื่อแยกเจตนา

## เกณฑ์ให้ผ่านและความหมายของคะแนน

ตรวจรอบแรกว่าถามส่วนที่ขาดจริง รอบสองตรวจหมวด **และงาน** เนื้อหาที่ต้องมี ขอบเขตโซน และรายละเอียดกติกา ปุ่มต้องได้คำตอบปุ่มจริง ชื่อเกมอย่างเดียวในคำอธิบายเกมไม่ผ่าน

ราคาบุคคลภายนอกตรวจ rows ของสองกลุ่ม ราคาแต่ละแพ็กเกจและ expected/returned IDs กับ fixture ของข้อมูลที่บันทึก ไม่ถือว่าอัตราเหล่านี้ได้รับอนุมัติให้ใช้ปัจจุบันแล้ว

เกณฑ์แรกแบบหยาบให้ 26/36 เพราะเช็คหมวด controls ไม่ตรง schema และไม่ได้ตรวจคำถามรอบแรก/รายละเอียดตระกูลครบ เก็บผลเดิมไว้ และคำนวณใหม่จาก raw log ด้วย oracle เดียวกับฉบับส่งมอบ จึงใช้ 23/36 ในการเปรียบเทียบ

ค่าความมั่นใจใน trace บอกเหตุผลเลือกเส้นทาง ไม่แทนความถูกต้องของข้อเท็จจริง การกันเลขภาคมีคะแนนเส้นทาง 1.0 แต่แสดงสถานะ **ไม่ยืนยันข้อมูล** อยู่ ไม่ได้หมายถึงรู้ข้อเท็จจริงของภาคนั้น 100%

## ผลทดสอบและหลักฐาน

- ใหม่: `tests/test_two_turn_choices_r39.py` **16/16 methods** ผ่าน รวมตัวเลือก ชื่อสุภาพ typo การเปลี่ยนงาน เลขรุ่น session และ TTL
- regression ราคา/กติกา r38 **23/23** ผ่าน; บริบทกติกา r35 **18/18** ผ่านในรอบตรวจหลังปรับบริบท; English game target smoke ผ่าน
- เว็บ r39.3: `{base[0].name}`, `{extra[0].name}`, `{negative_path.name}`
- ผลก่อนแก้ที่ใช้เกณฑ์เดียวกัน: `baseline_final_oracle_regrade_r38_5.json`; raw ก่อนแก้ `api_8093_000042.jsonl`
- ผลรวม/hash/health: `FINAL_SUMMARY_R39_3.json`, `health_r39_3_final.json`
- diff เฉพาะรอบนี้เทียบสำเนาก่อนแก้: `changes_this_turn_final.diff`; ก่อนแก้ 4 ไฟล์ใน `before/`
- เทียบ source กับแพ็กเกจผ่าน **5/5 runtime files**; Git diff check exit code {check.returncode}
- ระหว่างพัฒนามี unit test พบ alias สั้น evil ชน Resident Evil 4 และ negative test พบ TEKKEN 9 ผิดจริง เก็บหลักฐานที่ผิดไว้ ไม่เรียกผลก่อนแก้ว่าเป็นผลผ่าน
- ตัวตรวจ negative ช่วงหนึ่งเทียบ Minecraft แบบ case sensitive จึงตีความตัวพิมพ์เล็กใน resolved query เป็น failure แก้เฉพาะตัวตรวจให้ไม่ขึ้นกับตัวพิมพ์ และเพิ่มเงื่อนไขห้ามถามเหมือนยังไม่ได้รับชื่อ
- เคยเรียก API ระหว่าง server ยังเริ่มต้นและเจอ connection refused จากนั้นตรวจ health ของรุ่นที่ถูกต้องก่อนรันใหม่ ไม่รวมคำขอที่ยังไม่ถึง server ในยอด 123

เวลารับ input ถึง output ของ **106 คำขอในเคสปกติ/เพิ่มเติม** บนเครื่องนี้หลังระบบพร้อม: ค่ากลาง **{statistics.median(times):.3f} วินาที**, P95 **{p95:.3f} วินาที**, ช่วง **{min(times):.3f}–{max(times):.3f} วินาที**; timeout {summary['positive_timeouts']} ครั้ง ตัวเลขนี้ไม่ใช่เวลาจองสดหรือ SLA

## ตัวอย่างที่ลองจริง

| ถามรอบแรก | ตอบชื่อ/หมวดรอบสอง | ควรตอบ |
|---|---|---|
| อยากรู้ราคาของบุคคลภายนอก | PC / PS5 / Nintendo / Cockpit / VR | ราคาเฉพาะบริการ โดยคงกลุ่มภายนอก |
| ขอรายละเอียดกติกาการแข่งขัน | CS2 / RoV / TEKKEN 8 / VALORANT | รายละเอียดกติกาเกมที่เลือก คง full_sections และแบ่งหน้า |
| ขอดูปุ่มควบคุมเกม | VALORANT / Mario Kart 8 Deluxe / Beat Saber | ปุ่มของเกมนั้น |
| PC มีอะไรบ้าง | เกม / อุปกรณ์ / ราคา / จอง | หัวข้อที่เลือกของ PC |
| What does PC have? | games / equipment / prices / booking | เช่นเดียวกับไทย |
| Tell me about Call of Duty | Modern Warfare III | รายละเอียดภาคที่เลือก |
| What are the controls for Call of Duty? | Modern Warfare III | ปุ่มของภาคที่เลือก |
| มีเกมอะไรให้เล่นบ้าง | PS5 / cockpik | เกมเฉพาะโซนที่เลือก |
| Show me the game controls | Valoant please | ปุ่ม VALORANT |
| Show me the game controls | TEKKEN 9 | แจ้งยังไม่มีข้อมูลยืนยัน ไม่ตอบภาค 8 |

## สิ่งที่ยังติด/ควรเสริมตามลำดับ

1. **ยืนยันข้อมูลจริงกับเจ้าของ:** ราคาเดิมที่มีวันสิ้นสุด 31 มีนาคม 2026 ยังใช้หรือไม่? ขอรายการอัตรา/กลุ่มผู้ใช้/วันที่มีผล และยืนยันราคา PC ที่ปรับ 27 กรกฎาคม 2026 กติกา RoV ส่วน `competition_rules_rov_blueket_2025_men_s08_c01` ขอประโยคเต็มของ “…ออกจาก” และข้อ 6.1.5; Tekken ขอข้อ pause ที่ใช้จริงและข้อยกเว้น
2. **ปุ่มตรงกับเครื่องศูนย์:** บางเกม เช่น VALORANT มีคำเตือนว่าเป็นข้อมูลจากแหล่งรอง ยังไม่เทียบกับ keybindings ที่ติดตั้งจริง ผลเลือกเกมถูกไม่ได้ยืนยันค่าปุ่มทุกค่าที่เครื่องจริง
3. **ความถูกต้องสถานะจองสด:** รอบนี้ไม่ทดสอบ WordPress เทียบรายการว่าง/ถูกจองจากเจ้าหน้าที่ การต่อ API สำเร็จยังแยกจากสถานะจริงถูกต้องตามที่ตกลงไว้
4. **บริบทหลายงาน/หลายรอบ:** typed state ยังครบเฉพาะบางงาน หลายหมวดใช้ประวัติและ mode ข้อความเลือกยาวมาก การเลือกหลายเกมพร้อมกัน และภาษาไทยปนอังกฤษ/ผิดหลายตำแหน่งไม่ได้รับประกันหมด
5. **เก็บประวัติข้าม restart:** parent memory TTL ปัจจุบัน 30 นาที ไม่คงอยู่เองข้ามปิด server ถ้าต้องการคงข้ามเปิดเครื่องควรออกแบบ persistence พร้อม version/expiry
6. **ข้อมูลรุ่นเกมและ fault:** guard ใหม่เน้นเลขอารบิกที่ติดกับชื่อจาก aliases ของ catalog ยังไม่รับประกันเลขโรมัน/ชื่อภาคใหม่ทุกแบบ; crash/hang/network interruption ทุกจังหวะยังไม่ได้ทดสอบครบในรอบนี้

สิ่งที่ต้องเจ้าของยืนยันไม่ถูกแก้โดยเดา ไม่มีการเปลี่ยนตารางเจ้าของ ราคา หรือข้อความกติกาต้นฉบับในรอบนี้ ผลอัตโนมัติและการตรวจของคนยังแยกกัน

## วิธีลองใช้และไฟล์

เปิด [เว็บรุ่น r39.3](http://127.0.0.1:8094/) ตอนนี้ได้ รุ่นเก่าที่ 8090–8093 ยังอยู่ตามเดิม หากปิดเครื่อง ให้เปิด `Open-PSU-Esports-Background.cmd` ในโฟลเดอร์ `release_r39_3/PSU_Esports_Chatbot_Local` ตัวเปิดอาจเลือกพอร์ตว่างอื่น

แพ็กเกจใหม่ใช้ Python/Ollama/โมเดลที่มีบนเครื่องนี้ ไม่ใช่ชุดรวมโมเดลสำหรับส่งเครื่องใหม่พร้อมใช้ทันที แพ็กเกจทดลอง r39/r39.1/r39.2 หยุดแล้วและเก็บโฟลเดอร์/log ไว้เป็นหลักฐาน รุ่นส่งมอบคือ r39.3

Flow ฉบับที่ใช้: `FLOW_TWO_TURN_CHOICES_R39_TH.md`

## ผลรายเคสปกติ/เพิ่มเติม

| ID | รอบแรก | คำตอบสั้น | โหมดที่ตอบรอบสอง | ผล |
|---|---|---|---|---|
'''+ '\n'.join(rows)+'\n'
with (OUT/'REPORT_TWO_TURN_CHOICES_R39_3_TH.md').open('x',encoding='utf-8') as stream:stream.write(report)
print(json.dumps({k:v for k,v in summary.items() if k in ['final_normal','final_extra','final_negative','final_api_requests','positive_latency_seconds','positive_timeouts']},ensure_ascii=False,indent=2))
print('Report:',OUT/'REPORT_TWO_TURN_CHOICES_R39_3_TH.md')
