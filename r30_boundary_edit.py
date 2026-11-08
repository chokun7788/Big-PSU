from pathlib import Path
import json
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
    f=p/rel;s=f.read_text(encoding='utf-8');assert s.count(old)==1,(rel,s.count(old));f.write_text(s.replace(old,new),encoding='utf-8')
edit('app/pipeline/structured_tools.py','if explicit is not None and explicit.rows:\n        return list(explicit.rows)','if explicit is not None:\n        return list(explicit.rows)')
edit('app/pipeline/structured_tools.py','    selected_rows = _select_control_rows(query, rows)\n    platform_groups:', '''    selected_rows = _select_control_rows(query, rows)
    if not selected_rows:
        from app.pipeline.control_button_target import explicit_button_selection
        selection = explicit_button_selection(query, rows)
        observed = selection.observed if selection else "ที่ถาม"
        return StructuredToolResult(
            f"ยังไม่พบข้อมูลที่ยืนยันได้ว่าปุ่ม {observed} ของ {display_game_name} ทำหน้าที่อะไรครับ กรุณาตรวจชื่อปุ่มและแพลตฟอร์มอีกครั้ง",
            [], "structured_game_controls_unknown_button_no_answer", 0.98,
            {"game": display_game_name, "requested_button": observed, "no_inferred_mapping": True})
    platform_groups:''')
edit('app/pipeline/vector_retrieval.py','if explicit is not None and explicit.rows:\n        return list(explicit.rows)','if explicit is not None:\n        return list(explicit.rows)')
edit('app/pipeline/vector_retrieval.py','        wants_full_list = _looks_like_full_game_control_query(query)\n        if wants_full_list:', '''        from app.pipeline.control_button_target import explicit_button_selection
        selection = explicit_button_selection(query, explicit_rows)
        if selection is not None and not selection.rows:
            return f"ยังไม่พบข้อมูลที่ยืนยันได้ว่าปุ่ม {selection.observed} ของ {explicit_game} ทำหน้าที่อะไรครับ กรุณาตรวจชื่อปุ่มและแพลตฟอร์มอีกครั้ง"
        wants_full_list = _looks_like_full_game_control_query(query)
        if wants_full_list:''')
edit('app/pipeline/bilingual_english.py','    if button_selection is not None and button_selection.rows:\n        rows = list(button_selection.rows)', '''    if button_selection is not None and not button_selection.rows:
        return _result(
            f"I could not find a verified mapping for the {button_selection.observed} button in {game}. Please check the button name and platform.",
            category="games", intent="game_control_lookup", mode="pipeline:game_controls_unknown_button_no_answer_en",
            confidence=0.98, hits=[], reason="physical identifier is absent from this game's control records",
            answer_type="no_answer")
    if button_selection is not None:
        rows = list(button_selection.rows)''')
# Treat a negated duration as a requested clarification, never a second price option.
edit('app/pipeline/service_fee_alternatives.py','import math','import math,re')
edit('app/pipeline/service_fee_alternatives.py',"    service=services[0]\n    english=locale=='en'",'''    service=services[0]
    english=locale=='en'
    if re.search(r'ไม่(?:เอา|ใช่|ต้องการ)?\\s*$|\\b(?:not|without|except)\\s*$',query[max(0,choices.start-18):choices.start],re.I):
        answer=('Which duration should I price? Your question negates one of the listed durations.' if english else
                'ต้องการให้คิดราคาสำหรับระยะเวลาใดครับ ในคำถามมีการปฏิเสธหนึ่งในระยะเวลาที่ระบุ')
        return StructuredToolResult(answer,[],'duration_alternatives_clarification',.98,{'duration_choices':list(choices.minutes),'reason':'negated_duration'})''')
edit('app/pipeline/closed_query_improvements.py',"if result is not None:return category,result","if result is not None:return ('clarification' if 'clarification' in result.mode else category),result")
edit('app/pipeline/engine.py',"'no_answer' if improved_category == 'no_answer' else 'fact', 'medium'", "'clarification' if improved_category == 'clarification' else 'no_answer' if improved_category == 'no_answer' else 'fact', 'medium'")
print('Boundary edits applied; no source data edited.')
