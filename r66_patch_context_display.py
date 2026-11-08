from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
def replace(old,new):
 global t
 assert t.count(old)==1,(t.count(old),old[:60]);t=t.replace(old,new)
replace("        if value(r,k) is not None:return text(value(r,k),lang)","        if value(r,k) is not None:\n            v=value(r,k);shown=text(v,lang)\n            if r['kind']=='game' and lang=='th' and isinstance(v,dict) and v.get('en') and v.get('en')!=v.get('th'):shown+=' ('+v['en']+')'\n            return shown")
replace("                msg=('เกมที่มีให้เล่น' if lang=='th' else 'Offered games')+': '+str(len(lines))+'\\n'+'\\n'.join(lines)","                caption=' / '.join(title(records[rid],lang) for rid in roots)\n                msg=('เกมที่มีให้เล่น' if lang=='th' else 'Offered games')+(' — '+caption if caption else '')+': '+str(len(lines))+'\\n'+'\\n'.join(lines)")
replace("        if method=='common_rental_scope' and not requested and not broad:","        if query_operation=='equipment' and not requested and not broad:requested=['specifications','usage']\n        if method=='common_rental_scope' and not requested and not broad:")
replace("        for r in selected.values():\n            if r['kind']=='competition':", "        if method=='common_procedure_topic' and scope_ids:\n            blocks.append(('บริการที่ถาม: ' if lang=='th' else 'Selected service/game: ')+ ' / '.join(title(records[rid],lang) for rid in scope_ids))\n        for r in selected.values():\n            if r['kind']=='game':blocks.append(('ข้อมูลเกม: ' if lang=='th' else 'Game: ')+title(r,lang))\n            if r['kind']=='competition':")
p.write_text(t,encoding='utf-8');print('context captions, game identity and equipment projection')
