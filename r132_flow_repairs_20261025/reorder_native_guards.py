"""Keep decomposition ahead of single-action shortcuts in the repair candidate."""
from pathlib import Path
p=Path(__file__).resolve().parent/'system/app/knowledge/common/domain_flow/native_intents.py'
s=p.read_text('utf8')
start=s.index('    if _split:\n');end=s.index('    # Do not collapse unresolved independent needs',start)
guard_end=s.index("    if re.search(r'มีอะไร",end)
block=s[start:guard_end]
s=s[:start]+s[guard_end:]
where=s.index('    from app.pipeline.protected_intents import _is_public_access')
s=s[:where]+block+s[where:]
s=s.replace("        parts=[s.strip(' ,') for s in re.split", "        from .routing import split_needs\n        parts=split_needs(question,index)\n        if len(parts)==1:parts=[s.strip(' ,') for s in re.split",1)
p.write_text(s,'utf8')
print('Compound decomposition precedes single-purpose shortcuts.')
