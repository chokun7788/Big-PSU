"""Source control platform scope and faithful binding projection."""
import re
from .projection import bilingual,value
from .scope import contains

GESTURES={'press':('กด','press'),'hold':('กดค้าง','hold'),'release':('ปล่อย','release'),'double_press':('กดสองครั้ง','double press'),'simultaneous':('กดพร้อมกัน','simultaneous'),'sequence':('กดตามลำดับ','sequence'),'move':('เคลื่อน','move')}

def binding_projection(binding):
    label=binding.get('button_label')
    if label is None:
        join=' + ' if binding.get('gesture')=='simultaneous' else ' → ' if binding.get('gesture')=='sequence' else '; '
        label=join.join(binding.get('buttons') or [])
    buttons=bilingual(label);context=bilingual(binding.get('context') or '');notes=bilingual(binding.get('notes') or '')
    output={}
    for lang in ['th','en']:
        gesture=GESTURES.get(binding.get('gesture'))
        prefix=gesture[lang=='en']+': ' if gesture else ''
        output[lang]=prefix+buttons[lang]+''.join(' — '+s for s in [context[lang],notes[lang]] if s not in {'','None'})
    return buttons,output

def candidates(index,question,pool=None):
    from .dialogue_task import platforms
    requested=set(platforms(index,question));pool=index.bind('C05',question) if pool is None else pool
    if requested:pool=[f for f in pool if requested&set(platforms(index,str(value(index.records[f['record_id']],'platform') or '')))]
    from .requested_output import allows
    pool=[f for f in pool if allows(index,question,f)]
    presets={value(index.records[f['record_id']],'preset') for f in pool if value(index.records[f['record_id']],'preset')}
    named={p for p in presets if contains(question,p)}
    if named:pool=[f for f in pool if value(index.records[f['record_id']],'preset') in named]
    elif re.search(r'\bpreset\b|พรีเซ็ต',question,re.I):return []
    if re.search(r'\b(?:version|patch)\b|เวอร์ชัน|แพตช์',question,re.I):
        versions={value(index.records[f['record_id']],'game_version') for f in pool if value(index.records[f['record_id']],'game_version')}
        named={v for v in versions if re.search(r'(?:\b(?:version|patch)\s*|เวอร์ชัน\s*|แพตช์\s*)'+re.escape(v)+r'(?![\w.])',question,re.I)}
        pool=[f for f in pool if value(index.records[f['record_id']],'game_version') in named]
    return pool

def requested_button_count(index,question):
    from .named_spans import masked
    q=masked(index,question);words={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'หนึ่ง':1,'สอง':2,'สาม':3,'สี่':4,'ห้า':5,'หก':6,'เจ็ด':7,'แปด':8,'เก้า':9,'สิบ':10}
    number=r'-?\d+(?:\.\d+)?|'+'|'.join(words)
    match=re.search(r'(?<![\w.-])('+number+r')\s+buttons?\b|(?:จำนวน|ทั้งหมด|ขอ)\s*('+number+r')\s*ปุ่ม',q,re.I)
    if match:
        text=next(x for x in match.groups() if x is not None).casefold()
        return words[text] if text in words else float(text)
    return None

def physical_subset(index,question,facts=None):
    from .named_spans import masked
    pool=candidates(index,question);count=requested_button_count(index,question)
    available={str(k) for f in pool for k in (f.get('control_binding') or {}).get('buttons',[])}
    q=masked(index,question);marker=re.search(r'\bbuttons?\b\s*[:：]?\s*|ปุ่ม\s*[:：]?\s*',q,re.I);wanted=set();unknown=False
    if marker and available:
        pattern='|'.join(re.escape(k) for k in sorted(available,key=len,reverse=True))
        key=re.compile(r'^('+pattern+r')(?![\w])',re.I);canonical={k.casefold():k for k in available}
        tail=q[marker.end():].lstrip()
        while (match:=key.match(tail)):
            wanted.add(canonical[match[1].casefold()]);tail=tail[match.end():]
            separator=re.match(r'^\s*(?:,\s*(?:and\s+)?|and\s+|และ\s*|\+\s*|/\s*)',tail,re.I)
            if not separator:
                if tail.strip() and not re.match(r'^\s*(?:[?!.]|for\b|in\b|on\b|do\b|does\b|mean\b|perform\b|ใน|ของ|สำหรับ)',tail,re.I):unknown=True
                break
            tail=tail[separator.end():].lstrip()
            if not key.match(tail):unknown=True;break
    expected=[f for f in pool if (keys:=set((f.get('control_binding') or {}).get('buttons',[]))) and keys<=wanted]
    delivered=expected if facts is None else facts
    observed=set().union(*(set((f.get('control_binding') or {}).get('buttons',[])) for f in delivered)) if delivered else set()
    verified=bool(count is not None and count>0 and int(count)==count and wanted and not unknown and len(wanted)==count and observed==wanted and {f['id'] for f in delivered}=={f['id'] for f in expected})
    return {'verified':verified,'count':count,'requested_buttons':sorted(wanted),'source_fact_ids':[f['id'] for f in expected],'basis':'explicit_source_button_names_and_binding_arrays','unknown_requested_button':unknown}
