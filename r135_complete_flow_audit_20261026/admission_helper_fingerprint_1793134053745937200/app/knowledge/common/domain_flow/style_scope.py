"""Narrow presentation modifiers, preserving offsets and source entity labels.

Masking is for scope decisions only; the original request remains immutable.
Unrecognised language is not discarded or declared semantically understood.
"""
import re

COMMAND=re.compile(
 r'(?<![a-z])(?:please\s+)?(?:'
 r'(?:answer|respond|reply|explain|summari[sz]e)\s+(?:(?:it|that|this)\s+)?(?:briefly|concisely|only\s+(?:that|this)\s+(?:point|topic))'
 r'|keep\s+(?:it|that|this|the\s+answer)\s+(?:brief|short|concise)'
 r')\b'
 r'|(?:ช่วย|กรุณา)?(?:ตอบ(?:เฉพาะประเด็น(?:นั้น|นี้)|สั้น\s*ๆ?|โดยย่อ)|ขอคำตอบแบบเดียวกัน)',re.I)

def spans(question,index=None):
 protected=[]
 if index is not None:
  from .named_spans import spans as names
  protected=names(index,question)
 return [{'start':m.start(),'end':m.end(),'text':m[0],'basis':'explicit_presentation_modifier'} for m in COMMAND.finditer(question) if not any(h['start']<=m.start() and m.end()<=h['end'] for h in protected)]

def masked(question,index=None):
 chars=list(question)
 for hit in spans(question,index):chars[hit['start']:hit['end']]=' '*(hit['end']-hit['start'])
 return ''.join(chars)

def only(question):
 return bool(spans(question)) and not masked(question).strip(' \t\r\n?!.,:;')
