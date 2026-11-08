from pathlib import Path
import ast, hashlib, json, shutil, difflib, subprocess

W=Path(__file__).parent
R=Path((W/'r37_report_path.txt').read_text(encoding='utf-8').strip())
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
rels=['app/pipeline/competition_conversation_signals.py','app/session/context_resolver.py','app/pipeline/competition_overview.py']
before={rel:(P/rel).read_bytes() for rel in rels}
for rel in rels:
    dst=R/'before'/rel;dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():raise RuntimeError('Snapshot already exists')
    shutil.copy2(P/rel,dst)
oldR=Path((W/'r36_report_path.txt').read_text(encoding='utf-8').strip())
keys=json.loads((oldR/'protected_before.json').read_text(encoding='utf-8'))
protected={rel:hashlib.sha256((P/rel).read_bytes()).hexdigest() for rel in keys}
(R/'protected_before.json').write_text(json.dumps(protected,indent=2),encoding='utf-8')
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','-C',str(P),'status','--short'],capture_output=True,text=True)
(R/'git_status_before.txt').write_text(status.stdout+status.stderr,encoding='utf-8')
changes={}
changes[rels[0]]='''"""Parse bounded competition requests and context-dependent continuations."""
from __future__ import annotations
import re
import unicodedata
from app.core.typo_similarity import osa_distance

_THAI_WORDS = r"(?:ขอ|ดู|เอา|แล้ว|อยากรู้|อยากดู|บอก|สรุป|มี|เรื่อง|ของ|เกมนี้|เกม|กฎ|กติกา|ระเบียบ|การ|ตอน|แข่งขัน|แข่ง|ทัวร์นาเมนต์|อะไร|ไร|บ้าง|มั่ง|อื่น|เพิ่มเติม|เพิ่ม|อีก|ทั้งหมด|ไหม|มั้ย|หน่อย|ครับ|ค่ะ|คับ|\\s|[?!.,])+"
_ENGLISH_WORDS = r"(?:can|could|i|we|you|see|show|tell|give|me|please|pls|what|which|are|is|the|a|an|and|any|about|it|its|this|game|of|for|tournament|competition|rules|rule|regulations|other|more|additional|all|overview|summarize|\\s|[?!.,])+"

def _clean(query: str) -> str:
    q=unicodedata.normalize('NFC',str(query or '')).casefold().strip(' ?!.,')
    return re.sub(r'(?:รายการ)+(?=แข่ง)','รายการ',q).replace('กฏ','กฎ')

def is_rulebook_catalog_request(query: str) -> bool:
    q=re.sub(r'\\s+','',_clean(query))
    thai=re.fullmatch(
        r'(?:ตอนนี้)?(?:มี)?(?:รายการแข่ง|รายการแข่งขัน|เกมแข่ง|เกมแข่งขัน)(?:มี)?(?:อะไรบ้าง|ไรบ้าง|อะไรมั่ง|ไรมั่ง|ไหนบ้าง)(?:ครับ|ค่ะ|คับ)?'
        r'|(?:ตอนนี้)?(?:มี)?เกม(?:อะไร|ไร|ไหน)(?:ให้|ที่)?(?:รายการ)?(?:แข่ง|แข่งขัน)(?:ได้)?(?:บ้าง|มั่ง)?(?:ครับ|ค่ะ|คับ)?'
        r'|(?:ตอนนี้)?(?:รายการ)?(?:แข่ง|แข่งขัน)เกม(?:อะไร|ไร|ไหน)(?:ได้)?(?:บ้าง|มั่ง)(?:ครับ|ค่ะ|คับ)?',q)
    english=re.fullmatch(
        r'(?:what|which) (?:tournaments|competitions|competition games)(?: are (?:there|available|recorded))?'
        r'|list (?:the )?(?:tournaments|competitions|competition games)'
        r'|(?:what|which) games (?:can (?:we|i) compete in|are (?:there|available) for competition)',_clean(query))
    return bool(thai or english)

def _generic_rule_text(query: str) -> str:
    from app.pipeline.competition_targets import resolve_competition_targets,replace_competition_target_mentions
    resolution=resolve_competition_targets(query)
    if resolution.status=='exact':query=replace_competition_target_mentions(query,resolution,'')
    elif resolution.status!='absent':return ''
    q=_clean(query)
    if re.search(r'กฎ|กติกา',q):
        # Repeated courtesy letters carry no policy, edition or entity data.
        q=re.sub(r'(?:ครับ+|ค่ะ+|คับ+)\\s*$','',q).rstrip()
        q=re.sub(r'หน+่?อ+ย+$','หน่อย',q)
        for size in (5,4,6):
            suffix=q[-size:];prefix=q[:-size].rstrip()
            if re.fullmatch(_THAI_WORDS,prefix) and re.search(r'กฎ|กติกา',prefix) and osa_distance(suffix,'หน่อย')<=1:
                q=prefix;break
    # A misspelled rule word requires independent request grammar. Ordinary
    # real words are protected; this is not a global nearest-word rewrite.
    if re.search(r'\\b(?:can|could|show|give|tell|any|other|more|competition|tournament)\\b',q):
        for match in reversed(list(re.finditer(r'[a-z]+',q))):
            word=match.group()
            if word not in {'rules','rule','runes','rues','ruse'} and len(word)>=4 and osa_distance(word,'rules')==1:
                candidate=q[:match.start()]+'rules'+q[match.end():]
                if re.fullmatch(_ENGLISH_WORDS,candidate):q=candidate
    return q.strip(' ?!.,')

def is_broad_rule_request(query: str) -> bool:
    q=_generic_rule_text(query)
    return bool(q and re.search(r'กฎ|กติกา|\\brules?\\b|\\bregulations\\b',q) and (re.fullmatch(_THAI_WORDS,q) or re.fullmatch(_ENGLISH_WORDS,q)))

def is_contextual_more_request(query: str) -> bool:
    """A continuation shape only; the caller must supply an active rulebook."""
    q=_clean(query)
    thai=re.fullmatch(r'(?:แล้ว|ขอ|มี|ข้อ|อัน|อื่น|อีก|เพิ่มเติม|เพิ่ม|ต่อ|หน่อย|ยัง|เหลือ|อะไร|ไร|บ้าง|มั่ง|ไหม|มั้ย|เปล่า|ป่าว|ปะ|ล่ะ|ครับ|ค่ะ|คับ|\\s)+',q)
    english=re.fullmatch(r'(?:anything else|(?:any )?(?:more|other)(?: please| pls)?|(?:please )?(?:continue|go on))',q)
    return bool((thai and re.search(r'อื่น|เพิ่มเติม|เพิ่ม|อีก|ต่อ',q)) or english)

def is_more_rule_request(query: str) -> bool:
    q=_generic_rule_text(query)
    return (is_broad_rule_request(query) and bool(re.search(r'อื่น|เพิ่มเติม|เพิ่ม|อีก|\\b(?:more|other|additional)\\b',q))) or is_contextual_more_request(query)
'''
def replace(s,old,new):
    if s.count(old)!=1:raise RuntimeError('Patch count '+str(s.count(old))+': '+old[:70])
    return s.replace(old,new,1)

rel=rels[1];s=before[rel].decode('utf-8-sig').replace('\r\n','\n')
s=replace(s,'    generic = is_broad_rule_request(original)\n    more = is_more_rule_request(original)', '    more = is_more_rule_request(original)\n    generic = is_broad_rule_request(original) or more')
s=replace(s,'    choice_target = resolve_competition_targets(choice)', '''    competition_anchor = is_competition or is_rulebook_catalog_request(prior)
    # Use the existing bounded long-name recovery with a competition cue
    # supplied by the prior task, before a bare misspelling becomes game detail.
    choice_target = resolve_competition_targets(("competition rules " if competition_anchor else "") + choice)''')
s=replace(s,'    if bare_target and (pending or is_competition):','    if bare_target and (pending or competition_anchor):')
s=replace(s,'if user_target.status == "exact" or is_broad_rule_request(user_text):','if user_target.status == "exact" or is_broad_rule_request(user_text) or is_more_rule_request(user_text):')
s=replace(s,'if user_target.status != "absent" or not is_broad_rule_request(user_text):','if user_target.status != "absent" or not (is_broad_rule_request(user_text) or is_more_rule_request(user_text)):')
s=replace(s,'    competition_followup = _resolve_competition_followup(original, recent_history)', '''    # An explicit rejection followed by a complete new request changes the
    # task. Removing only this bounded preface prevents its rule word from
    # routing the new game-identity request back into a competition rulebook.
    declined = re.fullmatch(r"(?:ไม่เอา|ไม่ต้อง(?:การ)?|ไม่อยาก(?:ดู|รู้))(?:กฎ|กฏ|กติกา)(?:แล้ว)?\\s+(.+)", original)
    if declined:
        remainder = declined.group(1).strip()
        if detect_game(remainder) and re.search(r"คือ(?:เกม)?อะไร|เป็นเกมอะไร", remainder):
            return ResolvedQuestion(original, remainder, False, detect_game(remainder), context_domain="games", context_operation="game_detail", reason="explicitly_declined_rules_and_requested_game_identity")

    competition_followup = _resolve_competition_followup(original, recent_history)''')
changes[rel]=s
rel=rels[2];s=before[rel].decode('utf-8-sig').replace('\r\n','\n')
s=replace(s,"        tournament = (approved_localization(row, 'tournament') or str(row['tournament'])) if english else str(row['tournament'])",'''        tournament = str(row['tournament'])
        if english:
            localized = approved_localization(row, 'tournament')
            if localized:
                tournament = localized
            elif re.search(r'[\\u0e00-\\u0e7f]', tournament):
                # Reuse the source-backed game/year identity when no English
                # event-title field exists. Never pass untranslated Thai prose
                # through an English-only answer or invent an approved title.
                years = re.findall(r'\\b20\\d{2}\\b', tournament)
                tournament = target.label + (' / ' + ', '.join(dict.fromkeys(years)) if years else '')''')
changes[rel]=s

for rel,s in changes.items():ast.parse(s,filename=rel)
for rel,s in changes.items():
    if (P/rel).read_bytes()!=before[rel]:raise RuntimeError('Concurrent edit')
    out=s.replace('\n','\r\n') if b'\r\n' in before[rel] else s
    (P/rel).write_text(out,encoding='utf-8',newline='')
    dest=R/'diff'/Path(rel).with_suffix('.diff');dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(''.join(difflib.unified_diff(before[rel].decode('utf-8-sig').splitlines(True),out.splitlines(True),fromfile='before/'+rel,tofile='after/'+rel)),encoding='utf-8')
assert all(hashlib.sha256((P/rel).read_bytes()).hexdigest()==sha for rel,sha in protected.items())
(R/'changes.json').write_text(json.dumps({'files':list(changes),'syntax':'valid','protected_unchanged':len(protected)},indent=2),encoding='utf-8')
print(json.dumps({'changed':list(changes),'protected_unchanged':len(protected)}))
