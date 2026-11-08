from pathlib import Path
R=Path(__file__).resolve().parent;D=R/'system/app/knowledge/common/domain_flow'
p=D/'engine.py';s=p.read_text('utf8');needle="        if not blocks:blocks=[messages.get(plan.status,messages['missing_source'])[lang=='en']]"
assert needle in s;s=s.replace(needle,"""        details={
          'player_mode_source_not_recorded':('ยังไม่มีข้อมูลจำนวนผู้เล่นพร้อมกันแยกตามเกมและโหมดที่ยืนยันได้ จึงยังระบุรายชื่อเกมตามจำนวนคนนี้ไม่ได้ครับ','Confirmed player counts by game and mode are not recorded, so games matching this player count cannot yet be listed.'),
          'requested_player_mode_not_recorded':('ยังไม่พบโหมดเกมที่ยืนยันว่ารองรับจำนวนผู้เล่นและเงื่อนไขที่ถามครับ','No recorded game mode confirms the requested player count and conditions.'),
          'entity_not_bound':('ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม','The requested game, machine or topic is not identified. Please specify the target.'),
          'requested_operation_not_satisfied':('พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ','Related records exist, but the requested detail is not established.'),
        }
        if not blocks:blocks=[details.get(plan.reason,messages.get(plan.status,messages['missing_source']))[lang=='en']]""",1)
needle="        return {'answer':'\\n'.join(blocks),'status':status"
assert needle in s;s=s.replace(needle,"        from .customer_render import render as render_customer\n        blocks=render_customer(self.index,category,question,lang,selected,claims,computations,plan.metadata,blocks)\n"+needle,1);p.write_text(s,'utf8')
# The native booking cancellation operation must retain its object even with intervening particles.
p=D/'vocabulary.py';s=p.read_text('utf8');s=s.replace('(?:ยกเลิกการจอง|ยกเลิกจอง|ยกเลิก.*ล่วงหน้า)','(?:ยกเลิก.*การจอง|ยกเลิกจอง|ยกเลิก.*ล่วงหน้า)');p.write_text(s,'utf8')
# Preserve source-declared English identification wording before general visitor rules.
p=D/'native_intents.py';s=p.read_text('utf8');needle="    for cat,domain in [('C08'";assert needle in s;s=s.replace(needle,"""    if re.search(r'\\bwhat (?:id|documents?|identification)\\b',q,re.I) and re.search(r'visitor|arrival|check.in|studio',q,re.I):
        return Understanding([MeaningTask(question,'reservation','C08','detail','owner_policy')],True,'canonical_checkin_documents',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    for cat,domain in [('C08'""",1);p.write_text(s,'utf8')
print('Presentation patched')
