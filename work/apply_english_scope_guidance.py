"""Apply a narrow, review-grounded English scope response without resetting repo state."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\bilingual_english.py")
BACKUP = ROOT / "work/bilingual_english_before_scope_20260926.py"
original = TARGET.read_bytes()
source = original.decode("utf-8")
if b"\r\n" in original:
    raise RuntimeError("Unexpected line endings; edit needs review")

old_mode = '        "pipeline:chatbot_greeting_en",\n        "pipeline:english_no_answer",'
new_mode = '        "pipeline:chatbot_greeting_en",\n        "pipeline:english_scope_guidance_en",\n        "pipeline:english_no_answer",'
if source.count(old_mode) != 1:
    raise RuntimeError("Mode insertion anchor changed")
source = source.replace(old_mode, new_mode, 1)

anchor = '\ndef answer_english_supported(\n'
helper = '''
def _answer_english_scope_guidance(query: str) -> EnglishSupportResult | None:
    """Help with clear scope questions from the reviewed bilingual corpus."""
    q = query.casefold()
    if re.search(r"\\b(?:is the weather good today|will it rain|weather today|weather tomorrow)\\b", q):
        answer = (
            "I do not have verified weather information in this studio assistant. "
            "I can help with PSU Esports Studio bookings, equipment, hours, games, and rules."
        )
        intent = "outside_scope_weather"
        category = "no_answer"
    elif re.search(r"\\b(?:ask|question)\\b.{0,25}\\b(?:something unrelated|unrelated topics?)\\b", q):
        answer = (
            "I can answer questions about PSU Esports Studio, including bookings, "
            "equipment, hours, games, prices, and rules. Please ask a studio-related question."
        )
        intent = "studio_scope_boundary"
        category = "knowledge"
    elif re.search(r"\\b(?:do not|don't|dont) know what to ask\\b", q):
        answer = (
            "You can ask about booking a slot, whether a station is available, "
            "equipment, games, opening hours, prices, or studio rules."
        )
        intent = "suggest_studio_topics"
        category = "knowledge"
    else:
        return None
    return _result(
        answer,
        category=category,
        intent=intent,
        mode="pipeline:english_scope_guidance_en",
        confidence=0.99,
        hits=[],
        reason="clear English scope question with an answer grounded in the reviewed Thai guidance",
        answer_type="no_answer" if category == "no_answer" else "summary",
    )


'''
if source.count(anchor) != 1:
    raise RuntimeError("Function insertion anchor changed")
source = source.replace(anchor, "\n" + helper + "def answer_english_supported(\n", 1)

old_call = '''    if safe_rule is not None:
        return safe_rule
    # These requests either ask for personal data, explicitly state that no
'''
new_call = '''    if safe_rule is not None:
        return safe_rule
    scope_guidance = _answer_english_scope_guidance(query)
    if scope_guidance is not None:
        return scope_guidance
    # These requests either ask for personal data, explicitly state that no
'''
if source.count(old_call) != 1:
    raise RuntimeError("Call insertion anchor changed")
source = source.replace(old_call, new_call, 1)

with BACKUP.open("xb") as handle:
    handle.write(original)
TARGET.write_bytes(source.encode("utf-8"))
print(TARGET)
