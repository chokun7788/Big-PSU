import sys,json
from pathlib import Path
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'))
from tests.test_common_content_r58 import record
from app.knowledge.common.translation import translate_draft
r=record('game')
for f in r['fields'].values():
 if f.get('note') is None:f['note']=''
r['fields']['how_to_play']['value']={'th':'เก็บไข่มุกและหาทางออก','en':''}
out=translate_draft(r);english=out['record']['fields']['how_to_play']['value']['en']
passed='collect' in english.casefold() and 'pearl' in english.casefold() and 'exit' in english.casefold()
(B/'TRANSLATION_CONTEXT_CHECK.json').write_text(json.dumps({'source':'เก็บไข่มุกและหาทางออก','field':'how_to_play','english':english,'passed':passed,'fixture_only':True,'automatically_published':False,'previous_ui_output':'Store pearls and find a way out','cause':'Missing record/field context in the translation prompt','human_reviewed':False},ensure_ascii=False,indent=2),encoding='utf-8')
print(english,passed);assert passed
