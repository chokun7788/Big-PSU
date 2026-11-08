from pathlib import Path
R=Path(__file__).resolve().parent.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
p=R/'app/knowledge/common/ui/index.html';s=p.read_text(encoding='utf-8')
mark='<div id="fields"></div>'
s=s.replace(mark,'<div class="actions"><button id="translate_draft" class="secondary">ช่วยแปลไทยเป็นอังกฤษ (ร่าง)</button><label class="check"><input type="checkbox" id="translate_replace">แปลทับอังกฤษเดิมในร่างนี้ด้วย</label></div><p>ปุ่มแปลยังไม่บันทึกและไม่เผยแพร่ กรุณาตรวจความหมาย โดยเฉพาะคำว่า ห้าม/อนุญาต และเงื่อนไข ร่างที่แปลยาวมากให้แบ่งตามส่วนของข้อมูลหรือกรอกอังกฤษเอง</p>'+mark,1)
p.write_text(s,encoding='utf-8')
p=R/'app/knowledge/common/ui/owner.js';s=p.read_text(encoding='utf-8')
mark="$('save').onclick="
s=s.replace(mark,"$('translate_draft').onclick=()=>task(async()=>{let note=$('change_note').value;let x=await api('/api/translate',{record:collect(),replace_existing:$('translate_replace').checked});render(x.record,saved);$('change_note').value=note;$('translation_reviewed').checked=false;dirty=true;updateReadiness();message('แปลเป็นร่างแล้ว '+x.translated_count+' ช่อง ยังไม่บันทึกหรือเผยแพร่ กรุณาตรวจความหมายแล้วบันทึก');});\n"+mark,1)
p.write_text(s,encoding='utf-8')
