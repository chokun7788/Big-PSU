import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
assert (r/'final_G2_all_summary.json').exists(),'Do not change source while G2 full sweep is active.'
f=p/'app/core/locale.py';dest=r/'before_G3/app/core/locale.py';dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open('xb') as out:out.write(f.read_bytes())
s=f.read_text(encoding='utf-8');s=s.replace('import os\n','import os\nimport json\nfrom functools import lru_cache\nfrom pathlib import Path\n',1)
marker='def _detected_from_text(text: str) -> tuple[str, float, str]:\n    clean = _without_protected_spans(text)\n'
assert s.count(marker)==1
helper='''@lru_cache(maxsize=1)
def _catalog_title_pattern() -> re.Pattern[str] | None:
    """Source names are protected spans, not English sentence evidence.

    Use exact multiword names/aliases of currently listed games. No fuzzy
    correction, inferred title, or user-log training enters locale selection.
    """
    curated = Path(__file__).resolve().parents[2] / 'data' / 'curated'
    def rows(name):
        file = curated / name
        if not file.exists():
            return []
        return [json.loads(line) for line in file.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    def key(value):
        return re.sub(r'[^a-z0-9]', '', value.casefold())
    titles = {str(game) for row in rows('service_game_availability.jsonl') for game in row.get('games', [])}
    active_keys = {key(title) for title in titles}
    for row in rows('game_title_aliases.jsonl'):
        if key(str(row.get('game') or '')) in active_keys:
            titles.update(str(alias) for alias in row.get('aliases', []))
    names = [title for title in titles if title.isascii() and len(_LATIN_TOKEN_RE.findall(title)) >= 2]
    if not names:
        return None
    alternatives = [re.escape(name).replace(r'\\ ', r'\\s+') for name in sorted(names, key=len, reverse=True)]
    return re.compile(r'(?<![a-z0-9])(?:' + '|'.join(alternatives) + r')(?![a-z0-9])', re.I)


'''
new=helper+marker+'''    # In mixed input, words such as "The", "of", and "It" inside a game
    # name must not outvote the language of the user's actual question.
    # Latin-only input retains the existing English/identifier behavior.
    named_title_removed = False
    if _THAI_RE.search(clean) and _LATIN_TOKEN_RE.search(clean):
        title_pattern = _catalog_title_pattern()
        if title_pattern is not None:
            without_titles = title_pattern.sub(' ', clean)
            named_title_removed = without_titles != clean
            clean = without_titles
'''
s=s.replace(marker,new)
old='    if thai_chars:\n        return "th", min(0.99, 0.82 + min(thai_chars, 20) / 120), "thai_script"'
assert s.count(old)==1
s=s.replace(old,'    if thai_chars:\n        if named_title_removed:\n            return "mixed", 0.88, "mixed_named_title_thai_script"\n        return "th", min(0.99, 0.82 + min(thai_chars, 20) / 120), "thai_script"')
s=s.replace('elif reason == "mixed_thai_function_words":','elif reason in {"mixed_thai_function_words", "mixed_named_title_thai_script"}:')
f.write_text(s,encoding='utf-8',newline='\n')
with (p/'tests/test_r30_mixed_game_title_locale.py').open('x',encoding='utf-8') as out:out.write('''import unittest
from app.core.locale import resolve_locale
class R30MixedTitleLocaleTests(unittest.TestCase):
    def test_thai_task_survives_english_function_words_in_source_titles(self):
        for q in ['The Last of Us Part I / Part II ราคาเท่าไหร่', 'Horizon Call of the Mountain ราคาเท่าไหร่', 'The Legend of Zelda: Breath of The Wild ราคาเท่าไหร่', 'It Takes Two ปุ่มอะไรบ้าง']:
            with self.subTest(q=q):self.assertEqual(resolve_locale(q,requested='auto').effective,'th')
    def test_english_sentences_keep_english_with_a_thai_noun(self):
        for q in ['Can I play เกม at the studio?', 'What are the ปุ่ม in The Last of Us Part II?', 'Is The Last of Us Part II available?']:
            with self.subTest(q=q):self.assertEqual(resolve_locale(q,requested='auto').effective,'en')
    def test_explicit_language_toggle_is_preserved(self):
        q='The Last of Us Part I / Part II ราคาเท่าไหร่'
        self.assertEqual(resolve_locale(q,requested='en').effective,'en')
        self.assertEqual(resolve_locale(q,requested='th').effective,'th')
''')
manifest={str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')}
with (r/'app_freeze_G3.json').open('x',encoding='utf-8') as out:json.dump(manifest,out,indent=2)
print(json.dumps({'changed':['app/core/locale.py'],'new_tests':3}))
