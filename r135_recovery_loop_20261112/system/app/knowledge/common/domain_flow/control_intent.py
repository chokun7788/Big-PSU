"""A named-game button-function predicate does not request console usage."""
import re

def request(index,question):
    from .named_spans import masked
    from .dialogue_task import mentions
    from .routing import split_needs
    q=masked(index,question)
    if len(split_needs(question,index))!=1:return None
    controller_use=bool(re.search(r'ใช้\s*(?:จอย|เกมแพด)\s*(?:ยังไง|อย่างไร)|\bhow\b[^?.;]{0,45}\b(?:use|play)\b[^?.;]{0,45}\b(?:controller|gamepad)\b',q,re.I))
    if not controller_use and not re.search(r'ปุ่ม|\b(?:buttons?|controls?|bindings?)\b',q,re.I):return None
    if re.search(r'ราคา|กี่บาท|แข่ง|กติกา|อนุญาต|ห้าม|\b(?:price|cost|fee|tournament|competition|rules?|allowed|banned|remap)\b',q,re.I):return None
    if not (index.bind('C05',question) or mentions(index,question,{'game'})):return None
    action_query=bool(re.search(r'\b(?:which|what)\s+buttons?\s+(?:trigger|perform|activate|execute)\b',q,re.I))
    return {'operation':'list' if not action_query and (controller_use or re.search(r'ทั้งหมด|ปุ่มอะไร|อะไรบ้าง|อะไรมั่ง|\b(?:all|buttons|controls|bindings)\b',q,re.I)) else 'control',
            'basis':'named_game_control_predicate_before_platform_equipment_usage'}
