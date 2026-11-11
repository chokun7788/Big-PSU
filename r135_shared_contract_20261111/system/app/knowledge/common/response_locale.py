"""Explicit answer-language instructions, separate from a policy about language."""
import re
def requested_output(question):
    matches=[]
    for m in re.finditer(r'(?:ตอบ|อธิบาย|สรุป|แสดง|แปล).{0,100}?เป็น(?:ภาษา)?(อังกฤษ|ไทย)|\b(?:answer|explain|summarize|respond|translate)\b.{0,100}?\bin\s+(english|thai)\b',question,re.I):
        language=(m[1] or m[2]).casefold();matches.append('en' if language in {'อังกฤษ','english'} else 'th')
    return matches[-1] if matches else None
