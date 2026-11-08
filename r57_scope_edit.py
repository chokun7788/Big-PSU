import datetime,json,shutil,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');OLD=Path((BASE/'r56_current_path.txt').read_text());OUT=BASE/('r57_studio_scope_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));OUT.mkdir();(BASE/'r57_current_path.txt').write_text(str(OUT),encoding='utf-8')
for name in ('app/pipeline/engine.py','app/pipeline/experimental_fallback.py'):
 p=ROOT/name;b=OUT/'before'/name;b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,b)
owners=json.loads((OLD/'owner_hashes_before.json').read_text());assert all(hashlib.sha256((ROOT/k).read_bytes()).hexdigest()==v for k,v in owners.items());(OUT/'owner_hashes_before.json').write_text(json.dumps(owners,indent=2))
p=ROOT/'app/pipeline/experimental_fallback.py';t=p.read_text(encoding='utf-8');needle='def _general_llm_fallback(\n'
helper='''def build_studio_scope_fallback(question: str, *, reason: str = 'outside_supported_studio_information') -> ExperimentalFallback:
    """Product boundary: no unsourced general-purpose generation."""
    answer = (
        'I answer questions about PSU Esports Studio - Phuket using the available studio information: games, equipment, prices, bookings, opening hours, service policies and competition rules.'
        if effective_locale() == 'en' else
        'ผมช่วยตอบข้อมูลของ PSU Esports Studio - Phuket จากข้อมูลที่มีครับ เช่น เกม อุปกรณ์ ราคา การจอง เวลาเปิดบริการ ข้อกำหนดการใช้บริการ และกฎการแข่งขัน')
    return ExperimentalFallback(answer, [], 'studio_scope_no_answer', .99,
        PipelineTrace('studio_information_scope', 'no_unverified_general_generation', .99, reason,
            {'allow_llm': False, 'llm_attempted': False, 'source_policy': 'available_studio_information_only'}))


'''
assert needle in t;t=t.replace(needle,helper+needle,1)
start=t.index('    # General concepts, translations, and short writing requests do not gain',t.index('def build_experimental_fallback('));end=t.index('    # A miss from Rule/Fast/Structured',start)
t=t[:start]+'''    # General writing/knowledge is outside this studio product, even when it
    # mentions games. Verified studio requests may still retrieve evidence.
    if route.category == 'general' and (
        looks_like_clear_general_request(question) or not _looks_like_psu_specific_question(question)
    ):
        return build_studio_scope_fallback(question)

'''+t[end:]
old='''            return _general_llm_fallback(
                question,
                details=tuple((*details, "no_verified_rag_context")),
                mode="general_llm_after_rag_miss",
                decision="general_llm_after_rag_miss",
            )'''
assert old in t;t=t.replace(old,"            return build_studio_scope_fallback(question, reason='no_verified_studio_context')",1);p.write_text(t,encoding='utf-8')
p=ROOT/'app/pipeline/engine.py';t=p.read_text(encoding='utf-8');start=t.index("            if translation and translation['source']:",t.index('    def answer('));end=t.index('            from app.pipeline.request_focus import explicit_request_focus',start)
t=t[:start]+'''            from app.pipeline.query_signals import looks_like_explicit_creation_request
            if (translation and translation['source']) or looks_like_explicit_creation_request(question):
                from app.pipeline.experimental_fallback import build_studio_scope_fallback
                result = build_studio_scope_fallback(question, reason='generic_translation_or_creation_outside_studio_operations')
                return self._build_result(result.answer, [], started, 'pipeline:' + result.mode, result.confidence,
                    PipelineRoute('no_answer', 'studio_information_scope', .99, 'no_answer', 'low', 'studio information only'),
                    EntityBundle(), ValidationResult(ok=True), [*entry_timings, result.trace])
'''+t[end:];p.write_text(t,encoding='utf-8')
(OUT/'FLOW_SCOPE.md').write_text('''# Scope ของ Chatbot ศูนย์ · r57

ผู้ใช้ยืนยันใหม่: ตอบให้ครบเฉพาะข้อมูลบริการร้านเกม/ศูนย์ที่มี ไม่ต้องตอบความรู้ทั่วไป งานเขียนเรื่องเล่นเกม หรือคำถามชีวิตประจำวัน

1. เก็บ context และเลือก operation ของบริการ: เกม/อุปกรณ์/ราคา/จอง/เวลา/กฎ/การใช้งาน/ที่ตั้ง/การชำระเงิน
2. รับคำถามหลายส่วนและตอบแต่ละส่วนจาก source พร้อมเงื่อนไขสำคัญ ราคาและหน่วยต้องครบ
3. คำสั้นหลังถามยืนยัน เช่น PC/ทั้งหมด ต้องต่อกับงานเดิม ไม่เปิดหัวข้อใหม่เอง
4. ถ้าข้อมูลบริการขาด ให้ระบุว่าไม่ยืนยันเฉพาะเรื่องนั้น ไม่สร้างนโยบาย
5. ใช้ภาษาไทย/อังกฤษตอบข้อมูลศูนย์ตาม locale/source เดิม; การแปลทั่วไปและแต่งข้อความเป็น free-form task ไม่อยู่ใน product scope นี้
6. ไม่เรียก general LLM เพื่อเติมข้อเท็จจริงที่ไม่มี source หรือเพื่อคำถามไก่กับไข่/กินอะไร/บทความ/คำเชิญ แม้คำขอเขียนจะมีคำว่าเกม
7. LLM สำหรับคำตอบศูนย์ที่มี verified retrieval context ยังใช้ได้ตามระบบเดิม ขอบเขตไม่ได้หมายถึงปิดการใช้ LLM ทั้งหมด
8. ทดสอบคำถามนอกเรื่องทั้ง TH/EN และคำถามบริการหลายส่วน/context; ตรวจ mode, mandatory facts และไม่มี generic model generation
9. เก็บ raw results/diffs/owner hashes; ไม่ใช้ creative80words เป็นเกณฑ์ผ่านของสินค้าอีก

ส่วนที่เกิน6งาน/กำกวมมาก/source gap/owner policy ยังเป็นข้อจำกัดเดิม ไม่สรุปว่าทั้งหมดปิดแล้ว
''',encoding='utf-8')
print(OUT)
