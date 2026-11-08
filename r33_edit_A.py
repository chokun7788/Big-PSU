from pathlib import Path
import json
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
module='''"""Recover supported operation vocabulary only inside independent syntax frames.

This is not a general spelling corrector: entity names, numbers, URLs,
negation and ambiguous real words are never candidates.
"""
from __future__ import annotations
import re
from app.core.typo_similarity import osa_distance
from app.core.keyboard_input_anomaly import GENERIC_ENGLISH_WORDS

_WORDS = GENERIC_ENGLISH_WORDS | frozenset("rice march pay paid laid live love cold old hold hole bold sold rule cost cast coat lost most host post scope cope station nation accommodation damage position role rules pen words keyboard mouse chair monitor smoke sharp object gaming morning monday sunday schedule cancellation transfer overnight expensive different booking reservation studio contact members device best accommodation penalties responsibility policy available the who are you more save have game genre equipment drinks notes heroes score".split())
_LATIN = re.compile(r"[A-Za-z]+")
_RESOURCE = re.compile(r"\\b(?:pc|ps5|vr|cockpit|nintendo|switch|playstation)\\b|เครื่อง|อุปกรณ์",re.I)

def recover_task_frame(text: str):
    """Return (start, observed, canonical, distance, reason), or None."""
    low=text.casefold()
    if '://' in text or '@' in text or len(text)>180:return None
    tokens=list(_LATIN.finditer(text))
    def near(word):
        return any(osa_distance(m.group().casefold(),word)<=1 for m in tokens)
    # Independent grammar/context anchors. Long words permit one edit;
    # short words require an explicit slot, never a global nearest word.
    for m in tokens:
        word=m.group().casefold();before=low[:m.start()];after=low[m.end():]
        if word in _WORDS:continue
        targets=[]
        if re.search(r'\\b(?:the|this|our|esports)\\s+$',before):targets.append('studio')
        if near('studio') and re.search(r'\\b(?:what|rules?|policy|inside|can|penalties|food|noise)\\b',low):
            targets.extend(('studio','rules','policy','damage','smoke','food','sharp','object'))
        if re.search(r'\\b(?:what|which|how|where|who|is|does)\\b',low):
            if near('studio'):targets.extend(('contact','members','manages'))
            if re.match(r'\\s+(?:does|do)\\b',after) and re.search(r'\\bwhat\\s+$',before):targets.append('position')
            if re.search(r'\\b(?:what|which)\\s+$',before) and re.match(r'\\s+(?:is|are)\\b',after):targets.append('device')
        if re.search(r'\\b(?:reservation|booking|book|cancel)\\b',low):targets.extend(('reservation','cancellation','transfer','available'))
        if re.search(r'\\b(?:open|hours?|operating|schedule|days?|morning|sundays?)\\b',low):
            targets.extend(('open','schedule','monday','morning'))
        if re.search(r'\\b(?:keyboard|chair|monitors?|mouse|headset)\\b',low):targets.append('gaming')
        if near('gaming') and re.search(r'\\b(?:used|what|where|equipment|studio)\\b',low):targets.extend(('mouse','chair','keyboard','monitor'))
        if re.search(r'\\b(?:which|more)\\b',low) and _RESOURCE.search(text):targets.extend(('which','expensive'))
        if re.search(r'\\b(?:sessions?|minutes?|hours?)\\b',low) and _RESOURCE.search(text):targets.append('different')
        if re.search(r'\\b(?:play|listed|have|available)\\b',low):targets.append('game')
        if re.search(r'\\baccommodation\\b',low):targets.append('overnight')
        if re.search(r'\\bhow\\s+$',before) and re.match(r'\\s+(?:is|does|do)\\b',after):targets.append('much')
        if re.search(r'\\bwhat\\s+$',before) and re.match(r'\\s+i\\b',after):targets.append('should')
        if re.search(r'\\b(?:should|shuld)\\s+i\\s+$',before) and re.match(r'\\s*[?.]*$',after):targets.append('play')
        if re.match(r'\\s+(?:r[12]|l[12]|a|b|x|y)\\s+button\\b',after) and re.search(r'\\bdoes\\s+$',before):targets.append('the')
        if re.match(r'\\s+(?:ps5|pc|vr|cockpit)\\s+have\\b',after) and re.search(r'\\bwhat\\s+$',before):targets.append('does')
        if re.search(r'\\b(?:ps5|pc|vr|cockpit)\\s+$',before) and re.search(r'\\bwhat\\b',before):targets.append('have')
        if re.match(r'\\s+are\\s+you\\b',after):targets.append('who')
        if re.search(r'\\bwho\\s+$',before) and re.match(r'\\s+you\\b',after):targets.append('are')
        if re.search(r'\\b(?:the|a)\\s+$',before) and re.match(r'\\s*[?.]*$',after):targets.append('equipment')
        winners={t for t in targets if len(word)>=3 and abs(len(t)-len(word))<=1 and osa_distance(word,t)==1}
        if len(winners)==1:
            target=winners.pop();return m.start(),m.group(),target,1,'independent English task frame'
    # A standalone long supported topic is recoverable if uniquely closest.
    if re.fullmatch(r'[A-Za-z]{7,}[?.!]*',text.strip()):
        m=tokens[0];word=m.group().casefold()
        candidates={t for t in ('equipment','reservation','schedule') if osa_distance(word,t)<=2}
        if word not in _WORDS and len(candidates)==1:
            target=candidates.pop();return m.start(),m.group(),target,osa_distance(word,target),'unique standalone supported topic'

    # Thai has no word boundaries. Align only supported question operators,
    # anchored to a surviving topic/interrogative. Do not spellcheck names.
    has_resource=bool(_RESOURCE.search(text))
    from app.pipeline.entity_resolver import resolve_game_entity
    game=resolve_game_entity(text,operation='information')
    has_game=game.is_exact
    frames=[]
    if has_resource or has_game:
        frames += [('ราคาเท่าไหร่',2),('เสียกี่บาท',2),('กี่บาท',1),('ต้องเสียเงินไหม',1),('แพงกว่า',1)]
        if 'เล่น' in text or 'จอง' in text or 'ต้อง' in text:
            frames += [('ต้องจองอะไร',2),('จองยังไง',1),('ต้องทำยังไง',1)]
        if 'ตอน' in text or 'โมง' in text or 'บ่าย' in text:frames += [('ว่างไหม',1),('ว่างมั้ย',2)]
    if has_game:
        frames += [('เป็นเกมแนวไหน',2),('เล่นได้ที่เครื่องไหน',1),('เล่นได้ไหม',1)]
    if 'กี่' in text or 'วันไหน' in text:frames += [('เปิดกี่โมง',2),('เปิดวันไหนบ้าง',1)]
    if re.search(r'ถึง|ต้อง|ลืม|จอง|แนบ',text):frames += [('เช็กอิน',1),('สลิป',1)]
    if re.search(r'เอา|นำ|เข้า|อนุญาต|ได้ไหม',text):frames += [('อาหาร',1),('คีย์บอร์ด',1),('สูบบุหรี่',1)]
    if re.search(r'รับผิดชอบ|เล็กน้อย|อุปกรณ์|ของหาย|ระงับ',text):
        frames += [('เสียหาย',1),('สิทธิ์ชั่วคราว',1),('เปียก',1)]
    if re.search(r'คำพูด|ใช้คำ',text):frames += [('เหมาะสม',2)]
    if re.search(r'นาย|นาง|รศ\\.|ผศ\\.|ตำแหน่ง',text):
        frames += [('ตำแหน่งอะไร',2),('ตำแหน่งเลขานุการ',2)]
    if re.search(r'เกม|อุปกรณ์',text) and 'สุด' in text:frames += [('เกมเยอะสุด',2),('อุปกรณ์',1)]
    if 'ราชการ' in text:frames += [('วันหยุดราชการ',1)]
    candidates=[]
    for target,budget in frames:
        if target in text:continue
        for start in range(len(text)):
            for length in range(max(3,len(target)-budget),len(target)+budget+1):
                observed=text[start:start+length]
                if len(observed)!=length or not re.fullmatch(r'[\\u0e00-\\u0e7f]+',observed):continue
                # Surviving outer letters prevent a word embedded in another
                # source name from being a loose substring candidate.
                if observed[:1]!=target[:1] and observed[-2:]!=target[-2:]:continue
                distance=osa_distance(observed,target)
                if not 0<distance<=budget:continue
                # No dropped negation. A question operator cannot swallow it.
                if any(n in observed and n not in target for n in ('ไม่','ห้าม','อย่า','เกิน')):continue
                candidates.append((distance,abs(length-len(target)),start,observed,target))
    if not candidates:return None
    candidates.sort()
    best=candidates[0]
    if any(c[:2]==best[:2] and (c[2],c[4])!=(best[2],best[4]) for c in candidates[1:]):return None
    distance,_,start,observed,target=best
    return start,observed,target,distance,'supported Thai operator aligned to independent topic'
'''
f=P/'app/core/task_frame_recovery.py';assert not f.exists();f.write_text(module,encoding='utf-8')
f=P/'app/core/intent_cue_recovery.py';s=f.read_text(encoding='utf-8');needle='    contextual = _contextual_task_cue(text)'
assert s.count(needle)==1
s=s.replace(needle,"    from app.core.task_frame_recovery import recover_task_frame\n    framed = recover_task_frame(text)\n    if framed is not None:\n        start, observed, target, edits, reason = framed\n        return CueRecovery(text, text[:start] + target + text[start + len(observed):], observed, target, start, edits, reason)\n"+needle)
f.write_text(s,encoding='utf-8')
for name in ('r32_unit_all.py','r32_full.py','r32_full_corpus.py'):
    src=Path(__file__).with_name(name).read_text(encoding='utf-8').replace('r32_report_path.txt','r33_report_path.txt').replace('r32_full_corpus','r33_full_corpus')
    if name=='r32_full.py':
        src=src.replace("with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation; no real booking oracle',error_code='fixture_offline')):","with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation; no real booking oracle',error_code='fixture_offline')), patch('app.runtime.fast_answer.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation; no real booking oracle',error_code='fixture_offline')):")
    Path(__file__).with_name(name.replace('r32_','r33_')).write_text(src,encoding='utf-8')
flow='''# r33: แก้ให้ใช้งานได้โดยอ้างอิงข้อมูลจริง

1. เก็บ snapshot code/tests และ hash owner/Gold ก่อนแก้ (เสร็จแล้ว)
2. วิเคราะห์ 107 คู่ที่ clean ผ่านแต่ noisy ไม่ผ่าน: แยกข้อมูลมีจริง, ข้อมูลไม่พอ, คำกำกวม และ oracle ไม่ยืนยัน
3. กู้เฉพาะคำบอกงานในกรอบไวยากรณ์หรือหัวข้อที่มีหลักฐาน ไม่แก้ชื่อ เลข วัน เวลา คำปฏิเสธ หรือคำจริงที่กำกวม
4. ตรวจคำถามหลายส่วนและการเลือกบุคคล: ต้องผูกคำตอบกับต้นฉบับและไม่แสดง directory ทั้งหมดแทนบุคคลที่ไม่รู้จัก
5. ทดสอบชุดเดิมและกรณีใหม่พร้อม negative controls; เก็บ trace, คำที่กู้, คำตอบ, เงื่อนไขให้คะแนน และความต่างจาก r32
6. วิเคราะห์ regression ใหม่แล้วปรับเฉพาะเหตุที่พิสูจน์ได้; ไม่แก้ Gold เพื่อให้ตัวเลขผ่าน
7. ทดสอบผ่าน HTTP ของ package จริงรวมเนื้อหากฎ TH/EN และเว็บ; แยกเชื่อมได้จากคำตอบตรงเนื้อหา
8. ออก package ใหม่, สลับเฉพาะ process ที่ตรวจสอบว่าเป็นของงานนี้, ตรวจ 8090 ซ้ำ
9. สรุปผลจริงพร้อมข้อจำกัด: human review/owner approval/real occupancy ยังไม่ได้ยืนยัน

## เกณฑ์รับงาน
- คำถามที่มีข้อมูลต้องตอบหัวข้อถูกและครบ ไม่พึ่ง route/status อย่างเดียว
- คำกำกวมและข้อมูลขาดต้องถามกลับหรือเปิดเผยส่วนที่ยังไม่ทราบ
- Owner/Gold hashes ต้องตรงก่อนแก้; ไม่เขียนทับ log/package เดิม
- Real WordPress occupancy collection ยังพักตามคำสั่งผู้ใช้
'''
(R/'FLOW_R33_TH.md').write_text(flow,encoding='utf-8')
print('created contextual operator recovery, runners, flow')
