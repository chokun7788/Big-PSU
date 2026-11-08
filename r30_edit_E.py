from pathlib import Path
import json,hashlib
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
def edit(rel,old,new):
    f=p/rel;s=f.read_text(encoding='utf-8');assert s.count(old)==1,(rel,s.count(old))
    dest=r/'before_E'/rel;dest.parent.mkdir(parents=True,exist_ok=True);assert not dest.exists();dest.write_bytes(f.read_bytes());f.write_text(s.replace(old,new),encoding='utf-8')
edit('app/pipeline/validator.py','            price_context\n            and (route.category', '            price_context\n            and route.category != "clarification"\n            and route.answer_type != "clarification"\n            and (route.category')
edit('app/pipeline/protected_intents.py','    price = _has_price_signal(q)\n    usage =', '''    # An explicit all-service table request is complete in scope.
    if re.search(r'แต่ละ(?:เครื่อง|โซน|บริการ)|ตาราง.*ราคา|ค่าบริการ.*ทั้งหมด|ราคา.*ทั้งหมด|ค่าเล่น.*(?:เครื่อง|โซน).*บ้าง|\\b(?:each|all)\\s+(?:service|zone|device|station)s?\\b',q,re.I):
        return False
    price = _has_price_signal(q)
    usage =''')
edit('app/pipeline/closed_query_improvements.py',"has_price_intent(query) or re.search(r'\\b(?:prices?|fees?|costs?)\\b',query,re.I)","has_price_intent(query) or 'ค่าเล่น' in query or re.search(r'\\b(?:prices?|fees?|costs?)\\b',query,re.I)")
with (r/'app_freeze_E.json').open('x',encoding='utf-8') as f:json.dump({str(v.relative_to(p)):hashlib.sha256(v.read_bytes()).hexdigest() for v in (p/'app').rglob('*.py')},f,indent=2)
print('Aligned explicit table requests and price clarification validation.')
