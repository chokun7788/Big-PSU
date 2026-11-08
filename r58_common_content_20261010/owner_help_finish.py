from pathlib import Path
import json
OUT=Path(__file__).resolve().parent
p=json.loads((OUT/'owner_help_latest.json').read_text(encoding='utf-8'));stage=Path(p['stage'])
js=(stage/'owner.js').read_text(encoding='utf-8')
js=js.replace("let x=i.value.trim().replace(/,/g,'');if(!/^\\d+(\\.\\d{1,2})?$/.test(x))", "let raw=i.value.trim();if(!/^(\\d+|\\d{1,3}(,\\d{3})+)(\\.\\d{1,2})?$/.test(raw))")
js=js.replace("let [a,b='']=x.split('.')", "let [a,b='']=raw.replace(/,/g,'').split('.')")
js=js.replace("valueEditor(f.value_schema,unit.value??defaults(f.value_schema),f.reference_kind,f.key)", "valueEditor(f.value_schema,f.key==='amount_minor'?unit.value:(unit.value??defaults(f.value_schema)),f.reference_kind,f.key)")
(stage/'owner.js').write_text(js,encoding='utf-8')
for base in (OUT/'ready_package/PSU_Esports_Chatbot_Local',OUT/'system/PSU_Esports_Chatbot_Local'):
    (base/'app/knowledge/common/ui/owner.js').write_text(js,encoding='utf-8')
print('Price comma grouping checked; unknown price remains blank rather than defaulting to free.')
