import json,hashlib
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
name='app/pipeline/vector_retrieval.py';data=(project/name).read_bytes();p=report/'before'/name;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(data)
with (report/'before_vector_manifest.json').open('x',encoding='utf-8') as f:json.dump({name:hashlib.sha256(data).hexdigest()},f,indent=2)
p=project/'app/pipeline/structured_tools.py';text=p.read_text(encoding='utf-8')
with (report/'candidate_C_structured_tools.py').open('x',encoding='utf-8') as f:f.write(text)
start=text.index('    if best:\n        return best[2]\n    # Never replace')
end=text.index('\n\n\ndef _detect_equipment_item',start)
block=text[start:end]
text=text[:start]+'    return best[2] if best else None'+text[end:]
start=text.index('def _member_person_match(');end=text.index('\n\n\n@dataclass',start)
part=text[start:end];assert part.count('    return best[2] if best else None')==1
part=part.replace('    return best[2] if best else None',block)
text=text[:start]+part+text[end:];p.write_text(text,encoding='utf-8')
print('Moved the suggestion to the member resolver; retained failed intermediate implementation and vector original.')
