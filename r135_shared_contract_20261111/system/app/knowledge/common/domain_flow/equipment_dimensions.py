"""A recorded total and a per-machine controller count have distinct bases."""
import re

def allows(fact,question):
    if fact.get('facet')!='controllers' or not fact.get('specification_entry'):return True
    per_machine=r'ต่อเครื่อง|\bper (?:machine|console|device)\b'
    if re.search(per_machine,question,re.I):
        return bool(re.search(per_machine,str(fact['specification_entry'].get('unit') or ''),re.I))
    return True
