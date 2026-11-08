"""Task-specific display. Exact claims and source receipts stay in the result."""
import re
from collections import OrderedDict
from .projection import value,title

def clean_cell(s):return str(s).replace('|','\\|').replace('\n','; ')

def render(index,category,question,lang,selected,claims,computations,metadata,blocks):
    if not selected:return blocks
    if metadata.get('operator')=='compare' or metadata.get('comparison_options'):
        groups=OrderedDict();fields=OrderedDict()
        for i,(f,c) in enumerate(zip(selected,claims),1):
            option=f.get('event_id') if category=='C13' else f['record_id']
            record=index.records.get(option,{})
            caption=title(record)[lang] if record else f['subject'][lang]
            label=f['label'][lang];fields[label]=True
            row=groups.setdefault(str(option),{'caption':caption,'fields':{}})
            row['fields'].setdefault(label,[]).append(c['value']+f' [S{i}]')
        if len(groups)>1:
            columns=list(groups.values());out=['| '+('ข้อมูล' if lang=='th' else 'Field')+' | '+' | '.join(clean_cell(g['caption']) for g in columns)+' |','|'+'---|'*(len(columns)+1)]
            for label in fields:out.append('| '+clean_cell(label)+' | '+' | '.join(clean_cell('; '.join(g['fields'].get(label,[])) or ('ยังไม่มีข้อมูลยืนยัน' if lang=='th' else 'Not confirmed')) for g in columns)+' |')
            notices=[b for b in blocks if re.search(r'^อัตราที่เจ้าของ|^Rates last reaffirmed|effective|ยังไม่ยืนยัน|ไม่รับรอง|validity',b,re.I) and not b.startswith('**')]
            return notices+out
    if category=='C05' and len(selected)>2:
        out=['**'+selected[0]['subject'][lang]+'**','| '+('ปุ่ม | การทำงาน' if lang=='th' else 'Input | Action')+' |','|---|---|']
        for i,f in enumerate(selected,1):
            content=f['value'][lang];button,sep,note=content.partition(' — ')
            action=f['label'][lang]+(' — '+note if sep and note else '')
            out.append('| '+clean_cell(button)+' | '+clean_cell(action)+f' [S{i}] |')
        out.extend(b for b in blocks if not b.startswith(('**','- **')))
        return out
    if category=='C04' and all(f['facet']=='game_catalog' for f in selected):
        if metadata.get('operator') in {'count','group_count'}:return blocks
        groups=OrderedDict()
        for i,f in enumerate(selected,1):
            record=index.records.get(f['record_id'],{});platform=str(value(record,'platform') or f['subject'][lang])
            entry=groups.setdefault(platform,{'games':[],'labels':[],'sets':[]})
            games=[s.strip() for s in f['value'][lang].split(';') if s.strip()]
            entry['games']+=games;entry['labels'].append('S'+str(i));entry['sets'].append(set(games))
        out=[]
        for platform,entry in groups.items():
            games=list(dict.fromkeys(entry['games']));out.append('**'+platform+' — '+str(len(games))+(' เกม' if lang=='th' else ' games')+'**')
            out.extend('- '+g for g in games)
            if len(entry['sets'])>1 and any(s!=entry['sets'][0] for s in entry['sets'][1:]):out.append('รายการเกมต่างกันตามเครื่อง กรุณาระบุเครื่องหากต้องการตรวจเกมเฉพาะเครื่อง' if lang=='th' else 'Game lists differ between machines; specify a station for its exact catalogue.')
            out.append(' '.join('['+s+']' for s in entry['labels']))
        return out
    if category=='C06' and all(f['facet']=='amount' for f in selected):
        groups=OrderedDict();bycalc={c['fact_id']:c for c in computations}
        for i,(f,c) in enumerate(zip(selected,claims),1):
            r=index.records.get(f['record_id'],{});srv=index.records.get(value(r,'service_id'),{});aud=index.records.get(value(r,'audience_id'),{})
            calculation=bycalc.get(f['id']);platform=value(srv,'platform') or title(srv)[lang];audience=title(aud)[lang]
            signature=(str(platform),value(r,'audience_id'),c['numeric'],str(value(r,'duration_minutes')),f.get('billing_unit'),str(r.get('validity')),str(f.get('confirmation_as_of')),calculation.get('billing_quantity') if calculation else None)
            g=groups.setdefault(signature,{'platform':platform,'audience':audience,'text':c['value'],'citations':[],'calculation':calculation})
            g['citations'].append('S'+str(i))
        out=[]
        for g in groups.values():
            out.append('**'+str(g['platform'])+' / '+g['audience']+'**')
            calc=g['calculation'];line=g['text']
            if calc and calc.get('billing_quantity',1)>1:
                line+=(' × '+str(calc['billing_quantity'])+(' คน = ' if lang=='th' else ' people = ')+f"{calc['total_thb']:g}"+(' บาท' if lang=='th' else ' THB'))
            out.append(line+' '+' '.join('['+s+']' for s in g['citations']))
        # Carry validity notices and the verified aggregate from the executor.
        notices=[b for b in blocks if re.search(r'^อัตราที่เจ้าของ|^Rates last reaffirmed|^รวม |^Total|effective|ยังไม่ยืนยัน|ไม่รับรอง|validity',b,re.I) and not b.startswith('**')]
        return notices+out
    if category=='C03' and metadata.get('operator')=='list' and all(f['facet']=='name' for f in selected):
        return [('อุปกรณ์ที่มีข้อมูลในขอบเขตที่ถาม' if lang=='th' else 'Recorded equipment in the requested scope')]+['- '+f['value'][lang]+f' [S{i}]' for i,f in enumerate(selected,1)]
    return blocks
