from pathlib import Path
OUT=Path(__file__).resolve().parent;P=OUT/'system/PSU_Esports_Chatbot_Local/app/knowledge/common/ui/owner.js'
s=P.read_text(encoding='utf-8')
(OUT/'owner_ui_before_refine.js').write_text(s,encoding='utf-8')
s=s.replace("function message(s,error=false)","function message(s,error=false)")
anchor='async function api(path,body)'
dialog="""async function confirmAction(prompt){return new Promise(resolve=>{const d=node('dialog'),p=node('p',prompt),ok=node('button','ยืนยัน'),cancel=node('button','ยกเลิก');ok.onclick=()=>{d.close();d.remove();resolve(true);};cancel.onclick=()=>{d.close();d.remove();resolve(false);};d.addEventListener('cancel',e=>{e.preventDefault();d.close();d.remove();resolve(false);});d.append(p,cancel,ok);document.body.append(d);d.showModal();});}
"""
s=s.replace(anchor,dialog+anchor).replace('!confirm(', '!await confirmAction(')
P.write_text(s,encoding='utf-8')
print('Replaced blocking browser confirms with accessible DOM dialogs')
