"""Standalone result viewer; opens directly without JSON tooling or a server."""
import datetime,json,pathlib
R=pathlib.Path(__file__).resolve().parent
def read(p,default):
 try:return json.loads(p.read_text(encoding='utf8'))
 except (OSError,ValueError):return default
rows=[]
p=R/'evaluation/RESULTS.jsonl'
if p.exists():
 for line in p.read_text(encoding='utf8').splitlines():
  try:
   x=json.loads(line);rows.append({'question':x['question'],'answer':x.get('response',{}).get('answer',x.get('error','')),'key':x['key'],'transport_ok':x.get('transport_ok'),'seconds':x.get('elapsed_seconds')})
  except (ValueError,KeyError):pass
data={'generated':datetime.datetime.now().astimezone().isoformat(),'status':read(R/'STATUS.json',{}),'gates':read(R/'GATES.json',{}),'batch':read(R/'FOCUSED_BATCH.json',{}),'progress':read(R/'evaluation/PROGRESS.json',{'completed':0,'total':1056,'running':False}),'scores':read(R/'evaluation/SCORES_LITERAL.json',{}),'rows':rows}
payload=json.dumps(data,ensure_ascii=False).replace('<','\\u003c')
html='''<!doctype html><html lang="th"><meta charset="utf-8"><title>ผล R135 รุ่นผสม</title>
<style>body{font:16px system-ui;max-width:1120px;margin:32px auto;padding:0 18px;color:#18253a;background:#f6f8fc}h1{font-size:28px}section,article{background:white;border:1px solid #d7dfeb;border-radius:12px;padding:18px;margin:16px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit}input{width:95%;padding:12px}summary{cursor:pointer;font-weight:600}small{color:#536179}.notice{border-left:5px solid #dfa52c}button{padding:8px 14px}</style>
<h1>R135 รุ่นทดลองแบบผสม</h1><p>ใช้แกน R135 และ reader ของ R134 ผ่านตัวตรวจร่วม</p>
<section class="notice">คะแนนตรวจข้อความเป็น literal matching ของเกณฑ์ที่ตรวจได้ ไม่ใช่เปอร์เซ็นต์คำตอบถูกตามความหมาย และผลทดสอบย่อยไม่ใช่การรับรองครบ 48/76 ข้อ</section>
<section><h2>สถานะ</h2><pre id="status"></pre></section><section><h2>คะแนนรอบ 5%</h2><pre id="scores"></pre></section>
<section><h2>ผลตรวจเฉพาะส่วน</h2><pre id="focused"></pre></section>
<section><h2>คำถามและคำตอบ</h2><input id="search" placeholder="ค้นหาคำถามหรือคำตอบ"><p id="count"></p><div id="answers"></div><button id="more">แสดงเพิ่ม</button></section>
<script>const D=__DATA__;let limit=40;const $=id=>document.getElementById(id);$('status').textContent=JSON.stringify({updated:D.generated,phase:D.status.phase,evaluation:D.progress,blockers:D.status.blockers||[],known_limits:D.gates.limits||[]},null,2);$('scores').textContent=Object.keys(D.scores).length?JSON.stringify(D.scores,null,2):'ยังไม่มีคะแนนรอบ 5% ของรุ่นผสม';$('focused').textContent=JSON.stringify({batch_completed:D.batch.completed,total:D.batch.total,all_passed:D.batch.all_passed,source_gates:D.gates.source_critical_checks_passed,http_smoke:D.gates.http_smoke_passed},null,2);
function render(){const q=$('search').value.toLowerCase(),a=D.rows.filter(x=>(x.question+' '+x.answer).toLowerCase().includes(q));$('count').textContent='แสดง '+Math.min(limit,a.length)+' จาก '+a.length+' คำตอบ; จำนวนคำตอบไม่ใช่คะแนนความถูกต้อง';$('answers').replaceChildren();for(const x of a.slice(0,limit)){const d=document.createElement('details'),s=document.createElement('summary'),p=document.createElement('pre'),m=document.createElement('small');s.textContent=x.question;p.textContent=x.answer;m.textContent='HTTP/transport: '+x.transport_ok+' | '+x.seconds+' วินาที | '+x.key;d.append(s,m,p);$('answers').append(d)}}$('search').oninput=()=>{limit=40;render()};$('more').onclick=()=>{limit+=40;render()};render();</script></html>'''.replace('__DATA__',payload)
(R/'RESULTS_VIEW.html').write_text(html,encoding='utf8');print(json.dumps({'report':str(R/'RESULTS_VIEW.html'),'recorded_answers':len(rows)}))
