"""Identify explicit correction objects, never a remedy or an owner policy.

These are language-level distinctions. Profile subjects come from records;
no source ID, price, or studio rule is embedded here. Unrecognized wording
keeps the existing bounded proposal/confirmation path.
"""
import re
from .query_contract import normalize

def subject_types(text):
    q=normalize(text);found=set()
    if re.search(r'บัตรประชาชน|บัตรนักศึกษา|บัตรนักเรียน|พาสปอร์ต|หนังสือเดินทาง|ยืนยันตัวตน|เอกสารประจำตัว|\b(?:identity|identification|passport|student\s+id|national\s+id|id\s+(?:card|document))\b',q):found.add('identity_document')
    if re.search(r'ยอดเงิน|ยอด(?:จ่าย|ชำระ|โอน)|จำนวนเงิน|(?:จ่าย|โอน|ชำระ).{0,15}(?:ยอด|จำนวน)|\b(?:payment\s+amount|amount\s+(?:paid|transferred|i\s+paid)|(?:wrong|incorrect)\s+amount)\b',q):found.add('payment_amount')
    # A payment event alone is not an image/document.
    if re.search(r'สลิป|\bslips?\b',q) or (re.search(r'ชำระ|โอนเงิน|จ่ายเงิน|\b(?:payment|transfer|transaction)\b',q) and re.search(r'รูป|ภาพ|หลักฐาน|ไฟล์|เอกสาร|\b(?:proof|image|photo|picture|attachment|attachement|receipt|document)\b',q)):found.add('payment_evidence')
    return found

def compatible(question,profile):
    if profile.get('task')!='correction':return True
    wanted=subject_types(question)
    available=set().union(*(subject_types(' '.join(s for s in subject.values() if isinstance(s,str))) for subject in profile.get('subjects',[])))
    # Unknown subjects are not semantic matches. This guard only rejects a
    # concrete conflict, and cannot authorize reading any profile facts.
    return not wanted or not available or wanted<=available

def unresolved_topic(question):
    q=normalize(question)
    if not re.search(r'ผิด|แก้|\b(?:wrong|incorrect|mistak\w*|fix|correct|correction|correcting)\b',q):return None
    subjects=subject_types(q)
    if subjects=={'identity_document'}:return 'identity_correction'
    if subjects=={'payment_amount'}:return 'wrong_amount'
    return None
