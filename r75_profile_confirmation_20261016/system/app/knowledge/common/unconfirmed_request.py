"""Describe an unresolved need precisely; never infer a missing owner policy."""
import re
from .query_contract import normalize
def topic(question):
 q=normalize(question)
 if re.search(r'โอนเกิน|จ่ายเกิน|\b(?:overpaid|overpay|paid too much)\b|\b(?:payment|amount)\s+(?:was|is)\s+too\s+high\b',q):return 'overpayment'
 if re.search(r'โอนขาด|จ่ายขาด|(?:โอน|จ่าย|ชำระ).{0,15}ไม่ครบ|\b(?:underpaid|underpay|paid too little)\b|\b(?:payment|amount)\s+(?:was|is)\s+too\s+low\b',q):return 'underpayment'
 if re.search(r'(?:จ่าย|ชำระ|โอน).{0,20}(?:ยอดผิด|จำนวนผิด)|\b(?:wrong|incorrect)\s+(?:payment\s+)?amount\b',q):return 'wrong_amount'
 if re.search(r'ผ่อน(?:จ่าย|ชำระ)?|\binstallments?\b',q):return 'installments'
 # Account destination is not transfer latency. Require an arrival event AND
 # time/delay language in Thai before suppressing a known payment method.
 thai_arrival=bool(re.search(r'ถึงบัญชี|เข้าบัญชี|เงิน(?:เข้า|ถึง)|ยอด(?:เข้า|ถึง)',q))
 thai_delay=bool(re.search(r'กี่(?:วัน|นาที|ชั่วโมง)|นาน(?:ไหม|แค่ไหน|เท่าไหร่)|เมื่อ(?:ไหร่|ไร)|ระยะเวลา|ยังไม่|ไม่(?:เข้า|ถึง)|ช้า|เร็ว',q))
 if (thai_arrival and thai_delay and re.search(r'โอน|เงิน|ชำระ|จ่าย|ยอด',q)) or re.search(r'\b(?:transfer|payment)\b.{0,45}\b(?:arrive|processing|clear)\b',q):return 'transfer_processing'
 if re.search(r'อายุ|ผู้ปกครอง|\b(?:minimum age|age limit|years? old|guardian|parental)\b',q):return 'age_guardian'
 return None
LABELS={
 'overpayment':('วิธีจัดการเมื่อโอนเกิน','how overpayments are handled'),
 'underpayment':('วิธีจัดการเมื่อโอนขาด','how underpayments are handled'),
 'wrong_amount':('วิธีแก้ไขเมื่อชำระยอดผิด','how to correct an incorrect payment amount'),
 'installments':('เงื่อนไขการผ่อนชำระ','whether installment payments are permitted'),
 'transfer_processing':('ระยะเวลาที่เงินโอนเข้าถึงบัญชี','how long a transfer takes to reach the account'),
 'age_guardian':('เงื่อนไขอายุและผู้ปกครองสำหรับเข้าใช้ศูนย์','the age and guardian requirements for using the studio'),
}
def message(key,lang):
 label=LABELS[key][lang=='en']
 body=('จากข้อมูลที่อ่านได้ ยังยืนยัน'+label+'ไม่ได้ครับ กรุณาติดต่อเจ้าหน้าที่เพื่อยืนยันก่อนดำเนินการ' if lang=='th' else 'The information I could read does not confirm '+label+'. Please contact the studio staff to confirm before proceeding.')
 if key=='wrong_amount':body+=('\nยอดที่ชำระเกินหรือขาดจากยอดจองครับ? ตอนนี้ยังยืนยันวิธีแก้รายการหรือเงื่อนไขคืนเงินให้ไม่ได้' if lang=='th' else '\nWas the payment above or below the booking amount? I cannot yet confirm a correction or refund procedure.')
 return body
