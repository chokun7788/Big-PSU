exec(Path(__file__).with_name('r34_round_A.py').read_text().split("module='''")[0]) if False else None
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert s.count(old)==1,(rel,s.count(old));p.write_text(s.replace(old,new),encoding='utf-8')
p=P/'app/pipeline/source_task_signals.py'
p.write_text(p.read_text(encoding='utf-8')+'''
def payment_method_query(query: str) -> bool:
    return bool(re.search(r'(?:จ่าย|ชำระ)(?:เงิน)?(?:ยังไง|อย่างไร)|วิธี(?:จ่าย|ชำระ)|โอนเงิน|เลขบัญชี|\\b(?:how\\s+(?:do|can)\\s+(?:i|we)\\s+pay|payment\\s+method|bank\\s+account|(?:pay\\s+by|make\\s+a?)\\s+bank\\s+transfer)\\b', query, re.I))
''',encoding='utf-8')
edit('app/pipeline/protected_intents.py','    method = _has(q, "จ่ายยังไง", "จ่ายอย่างไร", "วิธีชำระ", "วิธีจ่าย", "โอนเงิน", "เลขบัญชี") or bool(re.search(\n        r"\\b(?:how\\s+(?:do|can)\\s+(?:i|we)\\s+pay|payment\\s+method|bank\\s+account)\\b", q\n    ))','    from app.pipeline.source_task_signals import payment_method_query\n    method = payment_method_query(q)')
edit('app/pipeline/question_frame.py','    # A zone/genre catalogue question asks for multiple games, even when the','    from app.pipeline.source_task_signals import payment_method_query\n    if payment_method_query(question):\n        return "booking_lookup", "reservation", 0.98\n    # A zone/genre catalogue question asks for multiple games, even when the')
edit('app/core/task_frame_recovery.py',"        if re.search(r'\\b(?:sessions?|minutes?|hours?)\\b',low) and _RESOURCE.search(text):targets.append('different')", "        if re.match(r'\\s+method\\b',after):targets.append('payment')\n        if re.search(r'\\b(?:sessions?|minutes?|hours?)\\b',low) and _RESOURCE.search(text):targets.append('different')")
edit('app/core/task_frame_recovery.py','    frames=[]','    frames=[]\n    if re.search(r"จ่าย|ชำระ",text) and re.search(r"ยังไง|ยงไง|อย่างไร",text):\n        frames += [("จ่ายเงินยังไง",1),("ชำระเงินยังไง",1),("ชำระเงินอย่างไร",1)]')
print('Round B payment operation and bounded method-word recovery saved')
