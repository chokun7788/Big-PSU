"""Task roles before FAQ selection. Language meaning, never answers or IDs.

Keys refer to FAQ semantic metadata. Scope exceptions remain unconfirmed.
"""
import re
from .query_contract import normalize
from .registry import value
ROLE_INTENTS={'payment_method':{'bank_account'},'payment_deadline':{'payment_timeout'},'booking_quota':{'booking_max_sessions'},'studio_rules':{'studio_rules_summary'}}
LABELS={'payment_method':('วิธีชำระเงิน','Payment method'),'payment_deadline':('กำหนดชำระเงิน','Payment deadline'),'booking_quota':('จำนวนรอบต่อการจอง','Sessions per booking'),'studio_rules':('กฎศูนย์','Studio rules')}
def exceptional_payment(question):
 q=normalize(question)
 from .unconfirmed_request import topic
 if topic(q) in {'overpayment','underpayment','wrong_amount','installments','transfer_processing'}:return True
 return bool(re.search(r'โอนเกิน|โอนขาด|จ่ายเกิน|จ่ายขาด|สลิปผิด|(?:จ่าย|ชำระ|โอน).{0,15}ผิด|\b(?:wrong|incorrect|overpaid|underpaid|overpay|underpay|installments?)\b|\b(?:transfer|payment)\b.{0,35}\b(?:arrive|arrives|processing|clear|clears)\b',q))
def analyze(question):
 q=normalize(question)
 if re.search(r'แข่ง|กติกา|\b(?:tournament|competition|rulebook)\b',q):return []
 # Mask explicit unwanted topics only, not conditions such as "do not pay".
 ignored=[]
 for pattern in (r'\b(?:do not|don.t)\s+(?:need|want|show|include)\s+(?:the\s+)?(?:bank(?:\s+(?:account|details))?|account(?:\s+details)?)(?:\s+(?:account|details))?',r'ไม่(?:เอา|ต้องการ|ต้องแสดง|ต้องบอก)(?:เลข)?บัญชี'):
  for m in re.finditer(pattern,q):ignored.append(m.group())
  q=re.sub(pattern,' ',q)
 payment=bool(re.search(r'ชำระ|จ่าย|โอนเงิน|\b(?:pay|payment|paid|transfer)\b',q))
 method=payment and bool(re.search(r'วิธี|ช่องทาง|ยังไง|อย่างไร|บัญชีไหน|ธนาคาร|เลขบัญชี|\b(?:how\s+(?:(?:do|can|should)\s+i\s+|to\s+)?(?:pay|make\s+(?:the\s+)?payment)|payment\s+(?:method|options?)|(?:where|which)\b.{0,45}\b(?:transfer|bank|account)|bank\s+account)\b',q))
 if re.search(r'เลขบัญชี|โอน.{0,20}บัญชีไหน|\b(?:which|what)\s+bank\s+account\b',q):method=True
 if re.search(r'ไม่จ่าย|ไม่ชำระ|\bwhat happens\b|\bif\b.{0,25}\b(?:not|unpaid)\b',q) and not re.search(r'ช่องทาง|วิธีชำระ|วิธีจ่าย|\bpayment method\b|\bhow do i pay\b',q):method=False
 deadline=payment and bool(re.search(r'ภายใน|กี่นาที|เมื่อไหร่|เมื่อไร|กำหนด|นานเท่าไหร่|\b(?:deadline|how soon|within|immediately|unpaid)\b|\bwhen\s+(?:must|should|do|can|is|does|will|payment)\b|\bhow long\s+(?:do|does)\s+(?:i|one)\s+have\b',q))
 if exceptional_payment(q):method=False;deadline=False
 quota=bool(re.search(r'(?:จอง|การจอง).{0,45}(?:กี่รอบ|กี่ช่วงเวลา|กี่\s*session|จำนวน.{0,12}(?:รอบ|session)|สูงสุด)|(?:กี่|จำนวน|สูงสุด|จำกัด).{0,30}(?:รอบ|session)|\b(?:how many|maximum|max|cap|limit)\b.{0,65}\b(?:sessions?|slots?)\b|\b(?:sessions?|slots?)\b.{0,35}\b(?:cap|limit)\b',q))
 quota=quota and bool(re.search(r'จอง|สูงสุด|\b(?:booking|book|reserve|reservation|maximum|max|cap|limit)\b',q))
 studio=bool(re.search(r'ศูนย์|สตูดิโอ|\b(?:studio|cent(?:er|re))\b',q)) and bool(re.search(r'กฎ|กฏ|ระเบียบ|\b(?:rules|regulations)\b',q))
 if re.search(r'(?:กฎ|กฏ|ระเบียบ).{0,20}(?:เรื่อง|เกี่ยวกับ)|\b(?:rules|regulations)\s+(?:about|on|regarding|for refunds)\b',q):studio=False
 if re.search(r'อนุญาต|ได้ไหม|\b(?:allow|allowed|can i|may i)\b',q):studio=False
 roles=[r for r,ok in [('payment_method',method),('payment_deadline',deadline),('booking_quota',quota),('studio_rules',studio)] if ok]
 qualifiers=[]
 if payment and re.search(r'เงินสด|บัตรเครดิต|บัญชีเพื่อน|\b(?:cash|credit card|friend.s account)\b',q):qualifiers.append('payment_option_not_established_by_general_method')
 daily=bool(re.search(r'ต่อวัน|\b(?:daily|per day)\b',q))
 return [{'role':role,'source_intents':sorted(ROLE_INTENTS[role]),'scope':'per_day' if role=='booking_quota' and daily else 'per_booking' if role=='booking_quota' else 'studio','unconfirmed_qualifiers':qualifiers if role.startswith('payment_') else [],'ignored_topic_spans':ignored,'semantic_correctness_verified':False} for role in roles]
def groups(needs,records):
 return [{**need,'candidate_ids':[rid for rid,r in records.items() if r['kind']=='faq' and value(r,'intent_key') in need['source_intents']]} for need in needs]

def uncovered_parts(question):
 """Compose explicit extra questions, not noun lists or polite prefaces."""
 from .query_contract import semantic_clauses
 clauses=semantic_clauses(question)
 if not 2<=len(clauses)<=4 or not analyze(question):return []
 if any(not analyze(c) and re.search(r'^(?:where|what|how|when|can i|is there|do you)\b|ที่จอด|อยู่ไหน|ได้ไหม|หรือไม่',c) for c in clauses):return clauses
 return []

def contextual_needs(question,history,records):
 """A short time/method follow-up can inherit topic, never answer text."""
 from .dialogue import previous_state
 state=previous_state(history,records)
 if not state:return []
 prior={role for role,keys in ROLE_INTENTS.items() if any(value(records[rid],'intent_key') in keys for rid in state['record_ids'])}
 if not prior&{'payment_method','payment_deadline'}:return []
 q=normalize(question).strip(' ?!.,')
 role=None
 if re.fullmatch(r'(?:(?:and|then|so)\s+)?when|(?:แล้ว)?(?:เมื่อไหร่|เมื่อไร)|(?:แล้ว)?ภายในกี่นาที',q):role='payment_deadline'
 elif re.fullmatch(r'(?:and\s+)?(?:the\s+)?(?:payment\s+)?method|(?:แล้ว)?วิธี(?:ชำระ|จ่าย)?ล่ะ',q):role='payment_method'
 if not role:return []
 return [{'role':role,'source_intents':sorted(ROLE_INTENTS[role]),'scope':'studio','unconfirmed_qualifiers':[],'ignored_topic_spans':[],'semantic_correctness_verified':False,'context_record_ids':state['record_ids'],'context_basis':'server_state_ids_and_current_semantic_metadata_only'}]
