"""One-time UI revision for transparent partial answers and remaining-only view."""
from pathlib import Path
R=Path(__file__).resolve().parent
p=R/'app.js';s=p.read_text('utf8')
def sub(old,new):
 global s
 if new in s:return
 if s.count(old)!=1:raise RuntimeError('Unexpected UI source: '+old[:65])
 s=s.replace(old,new)
sub("answered:'ให้คำตอบแล้ว',unknown:","answered:'ให้คำตอบแล้ว',partial:'ตอบแล้วบางส่วน',unknown:")
sub("note:''}}","note:'',remaining_question:''}}")
old="function stats(){let all=data.questions.length,done=data.questions.filter(q=>answer(q.id).status==='answered').length,untouched=data.questions.filter(q=>answer(q.id).status==='unanswered').length,other=all-done-untouched;$('#stats').replaceChildren();for(let [n,t] of [[all,'ข้อทั้งหมด'],[done,'ให้คำตอบแล้ว'],[untouched,'ยังไม่ตอบ'],[other,'ระบุสถานะอื่นแล้ว']]){let s=el('div','stat');s.append(el('strong','',n),document.createTextNode(t));$('#stats').append(s)}nav()}"
new="function stats(){let all=data.questions.length,done=data.questions.filter(q=>['answered','no_policy','not_applicable'].includes(answer(q.id).status)).length,partial=data.questions.filter(q=>answer(q.id).status==='partial').length;$('#stats').replaceChildren();for(let [n,t] of [[all,'ข้อเดิมทั้งหมด'],[done,'ปิดข้อได้แล้ว'],[partial,'ตอบแล้วบางส่วน'],[all-done,'ยังต้องตอบ/เติม']]){let s=el('div','stat');s.append(el('strong','',n),document.createTextNode(t));$('#stats').append(s)}nav()}"
sub(old,new)
sub("q.section===name).length));b.onclick", "q.section===name&&!['answered','no_policy','not_applicable'].includes(answer(q.id).status)).length+' ค้าง'));b.onclick")
sub("box.append(top,el('h3','',q.title),el('p','question',q.question));", "box.append(top,el('h3','',q.title),el('p','question',a.status==='partial'&&a.remaining_question?'ยังต้องตอบเพิ่ม: '+a.remaining_question:q.question));if(a.status==='partial'&&a.remaining_question){let original=el('details');original.append(el('summary','','ดูคำถามเดิมเต็มข้อ'),el('p','',q.question));box.append(original)}")
sub("index+' / '+data.questions.length", "'ข้อ '+index")
sub("labels[a.status]);top.append(badge)", "labels[a.status]||'ยังไม่ตอบ');top.append(badge)")
sub("(status==='all'||answer(q.id).status===status)","(status==='all'||(status==='pending'?!['answered','no_policy','not_applicable'].includes(answer(q.id).status):answer(q.id).status===status))")
sub("q.why,data.categories[q.category],answer(q.id).text", "q.why,data.categories[q.category],answer(q.id).text,answer(q.id).remaining_question")
sub("if(a.note)lines.push('หมายเหตุ: '+a.note,'');", "if(a.note)lines.push('หมายเหตุ: '+a.note,'');if(a.status==='partial'&&a.remaining_question)lines.push('ยังต้องตอบเพิ่ม: '+a.remaining_question,'');")
sub("stats();render();mark('พร้อมกรอก", "if(data.owner_update){$('#ownerUpdate').textContent='จับคู่คำตอบจากแชท '+data.owner_update.source_items+' ข้อให้แล้ว • เปิดอ่านคำตอบที่เติมไว้ในแต่ละข้อได้'}stats();render();mark('พร้อมกรอก")
p.write_text(s,'utf8')
p=R/'index.html';s=p.read_text('utf8');s=s.replace('<option value="all">ทุกสถานะ</option>','<option value="pending" selected>ยังต้องตอบ / เติมส่วนที่ขาด</option><option value="all">ทุกสถานะ</option>');s=s.replace('<option value="answered">ให้คำตอบแล้ว</option>','<option value="answered">ให้คำตอบแล้ว</option><option value="partial">ตอบแล้วบางส่วน</option>');p.write_text(s,'utf8')
print('Partial-answer UI enabled; existing question IDs and dataset hash retained.')
