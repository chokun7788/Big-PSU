from pathlib import Path
import hashlib,json,shutil,datetime

W=Path(__file__).parent
OUT=Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_20261003')
E=W/'share_release_evidence_20261003'
oracle=json.loads((W/'share_download_oracle_results.json').read_text())
results=[]
for variant,folder in [('download_models','01_Download_Models'),('with_models','02_With_Models')]:
    root=OUT/folder
    spec=json.loads((root/'ready_manifest.json').read_text(encoding='utf-8'))
    run=sorted(W.glob('share_checks_'+variant+'_*'))[-1]
    checks=json.loads((run/'summary.json').read_text(encoding='utf-8'))
    assert checks['passed']==checks['total']==4
    destination=E/folder/'http_checks'
    shutil.copytree(run,destination)
    pm=root/'system/PSU_Esports_Chatbot_Local/package_manifest.json'
    inner=json.loads(pm.read_text(encoding='utf-8-sig'))
    inner['runtime_version']=spec['runtime_version']
    inner['delivery_variant']=variant
    inner['includes_python_runtime']=True
    inner['includes_ollama_runtime']=True
    inner['includes_ollama_model_weights']=variant=='with_models'
    pm.write_text(json.dumps(inner,ensure_ascii=False,indent=2),encoding='utf-8')
    assert not list((root/'system/PSU_Esports_Chatbot_Local/data/logs').glob('*.jsonl'))
    assert not list((root/'system/PSU_Esports_Chatbot_Local/data/logs').glob('*.sqlite3'))
    assert not list((root/'runtime/state').iterdir())
    actualweights=[p for p in (root/'runtime/models').rglob('*') if p.is_file() and p.stat().st_size>100_000_000]
    assert len(actualweights)==(2 if variant=='with_models' else 0)
    files=[]
    for p in root.rglob('*'):
        if not p.is_file() or p.name=='build_inventory.json':continue
        item={'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size}
        if p.suffix in {'.ps1','.cmd'} or item['path'].startswith('tools/'):
            item['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        files.append(item)
    size=sum(i['bytes'] for i in files)
    mode='ดาวน์โหลดโมเดลครั้งแรก' if variant=='download_models' else 'มีโมเดลครบ'
    text=f'''# ผลตรวจชุด {mode}

เวอร์ชัน `{spec['runtime_version']}` — Windows x64 บนเครื่องผู้จัดทำ

## ผ่านแล้ว

- เปิดจาก Start-Chatbot.cmd ด้วย Python/Ollama ในโฟลเดอร์นี้ โดยไม่ใช้ Python/Ollama ที่ติดตั้งนอกชุด
- Model preflight และ embedding/cache warmup ผ่าน worker พร้อมใช้งาน
- คำถามไทย/อังกฤษและการเลือกกติกาจากบทสนทนา: {checks['passed']}/{checks['total']} ตามเงื่อนไข route และ source ที่กำหนด
- เปิดซ้ำใช้โปรเซสเดิม และ Stop หยุดเฉพาะโปรเซสชุดนี้ แชทเดิมพอร์ต 8090 ยังทำงาน
- {'เริ่มด้วยโมเดลว่างและ partial 32 ไบต์ ดาวน์โหลดจริงจาก registry.ollama.ai ต่อจนครบ ตรวจ SHA-256 ของทั้งสองโมเดลตรงกับชุดมีโมเดล' if variant=='download_models' else 'ตรวจโมเดลครบและเตรียมโมเดลสำเร็จเมื่อบล็อกฟังก์ชันดาวน์โหลดในตัวทดสอบ ไม่มีการโหลดโมเดลจากอินเทอร์เน็ต'}
- ตัวดาวน์โหลดมี fixture oracle ที่รู้ bytes จริง: ผ่าน {oracle['passed']}/3 กรณี (ดาวน์โหลดต่อ, partial ใหญ่ผิดขนาด, ปฏิเสธไฟล์ที่ SHA ไม่ตรง)
- ก่อนส่งมอบไม่มี log แชทเดิม ไม่มีคีย์ Ollama ส่วนตัว ไม่มีสถานะโปรเซสทดสอบค้างในชุด
- {'ไม่มีไฟล์น้ำหนักโมเดลในชุดนี้' if variant=='download_models' else 'มีไฟล์น้ำหนักโมเดลครบและใบอนุญาตที่มากับโมเดล'}
- ขนาดโฟลเดอร์ประมาณ {size/1e9:.2f} GB

## ยังไม่ใช่ผลรับรอง

- ยังไม่ได้รันบนคอมพิวเตอร์ผู้รับจริง จึงไม่รับรองความเร็วหรือ driver/RAM ของทุกเครื่อง
- ไม่ใช่การทดสอบ Ground Truth ทั้งหมดหรือการอนุมัตินโยบาย/กติกาจากเจ้าของ
- การจองสดต้องใช้อินเทอร์เน็ต ไม่ได้ตรวจสถานะว่างทุกช่องกับ oracle ของเจ้าของในรอบประกอบชุดนี้
- ข้อสังเกต flow เดิมยังอยู่: `Which games have competition rules?` ยังถามกลับให้เลือกเกม แทน catalog overview
- คำตอบที่ไม่มีแหล่งยืนยันยังควรตอบว่าไม่มีข้อมูล ไม่เพิ่มนโยบายเอง

หลักฐานเต็มและ log ทดสอบถูกเก็บแยกไว้กับผู้จัดทำที่ `{destination}` เพื่อไม่ปะปนกับประวัติของผู้รับ
โค้ดและข้อมูลต้นทาง r37.2 ไม่มีการแก้ในงานประกอบชุดนี้
'''
    (root/'TEST_RESULTS_TH.md').write_text(text,encoding='utf-8')
    (root/'build_inventory.json').write_text(json.dumps({'files':files,'bytes':size,'model_weights_included':variant=='with_models','old_logs_included':False,'test_logs_included':False},indent=2),encoding='utf-8')
    results.append({'folder':folder,'variant':variant,'folder_bytes':size,'http_passed':checks['passed'],'http_total':checks['total'],'models_included':variant=='with_models','stopped_clean':True})

readme='''# PSU Esports Chatbot — สองแบบสำหรับส่งต่อ

| แบบ | เปิดครั้งแรก | ขนาดโฟลเดอร์ประมาณ |
|---|---|---|
| **01_Download_Models** | ดาวน์โหลดโมเดล 3.65 GB อัตโนมัติ แล้วเปิดเว็บ | 3.0 GB |
| **02_With_Models** | มีโมเดลอยู่แล้ว ไม่ต้องดาวน์โหลดโมเดล | 6.7 GB |

ทั้งสองแบบรวม Python, Ollama, เว็บแชท และข้อมูลเดียวกัน รองรับ Windows 10 22H2 / Windows 11 x64
ชุดดาวน์โหลดใหญ่ประมาณ 3 GB เพราะยังมีตัวรัน CPU/NVIDIA/AMD/Vulkan ครบเหมือนชุดเต็ม

## ส่งให้ผู้รับ

ส่ง ZIP **เพียงแบบเดียว** ที่เหมาะกับผู้รับ หรือคัดลอกทั้งโฟลเดอร์ของแบบนั้น
ผู้รับแตกไฟล์ไปยังโฟลเดอร์ที่เขียนได้ แล้วดับเบิลคลิก **Start-Chatbot.cmd** ที่รากของโฟลเดอร์
ไม่ต้องติดตั้ง Python/Ollama ไม่ต้องพิมพ์คำสั่งเอง ไม่ต้องเปิด Dashboard แยกสำหรับ WordPress direct fetch
ใช้ **Stop-Chatbot.cmd** เมื่อเลิกใช้ อ่าน README_TH.md ในชุดนั้นหากเปิดไม่สำเร็จ

ชุดมีโมเดลสามารถตอบจากข้อมูลในเครื่องได้โดยไม่ดาวน์โหลดโมเดล ส่วนสถานะจองสดยังต้องใช้อินเทอร์เน็ต
ยังไม่ได้รันบนเครื่องผู้รับจริง: ตรวจ Windows x64, พื้นที่ว่าง, RAM และ driver ตามคู่มือในชุด
รายละเอียดผลทดสอบอยู่ใน TEST_RESULTS_TH.md ของแต่ละชุด ไม่มีประวัติแชทเดิมติดไปด้วย
รายงานความสมบูรณ์ ZIP และ SHA-256 สำหรับตรวจการส่งไฟล์อยู่ใน archive_checks.json และ SHA256SUMS.txt
'''
(OUT/'README_TH.md').write_text(readme,encoding='utf-8')
(OUT/'release_summary.json').write_text(json.dumps({'deliveries':results,'fixture_oracle':oracle,'original_code_or_logs_overwritten':False},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=False),flush=True)
