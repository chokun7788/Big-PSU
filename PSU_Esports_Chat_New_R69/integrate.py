"""Patch this new installation only; no old source file is edited."""
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system'
p=H/'app/pipeline/engine.py';s=p.read_text('utf8')
old="        self.matcher = RuleMatcher.default()"
new="        from app.knowledge.common.migrated_view import enabled as migrated_chat_enabled\n        self.matcher = None if migrated_chat_enabled() else RuleMatcher.default()"
assert old in s;s=s.replace(old,new,1)
old="            from app.knowledge.common.answer import try_common_answer"
new="""            from app.knowledge.common.migrated_view import enabled as migrated_chat_enabled
            if migrated_chat_enabled():
                from app.pipeline.migrated_chat import answer as migrated_answer
                return migrated_answer(question, locale=resolved_locale, history=recent_history,
                    allow_llm=env_experimental_llm_default() if experimental_allow_llm is None else bool(experimental_allow_llm))
            from app.knowledge.common.answer import try_common_answer"""
assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf8')
p=H/'app/web_api/server.py';s=p.read_text('utf8')
old="                if turn.get('context_resolution'):"
new="""                from app.knowledge.common.migrated_view import enabled as migrated_chat_enabled
                if migrated_chat_enabled():
                    # The common reader resolves delivered common_read_state from
                    # this new chat's own server history, using the original input.
                    resolved = ResolvedQuestion(question, question, False, reason='migrated_common_server_history')
                    request_plan = None
                elif turn.get('context_resolution'):"""
assert old in s;s=s.replace(old,new,1)
old='        "profile": os.getenv("PSU_RUNTIME_PROFILE", "ad-hoc"),'
new=old+'\n        "knowledge_profile": os.getenv("PSU_COMMON_CHAT_PROFILE", "published"),\n        "knowledge_draft_preview": os.getenv("PSU_COMMON_CHAT_PROFILE") == "r69-migration-preview",'
assert old in s;s=s.replace(old,new,1)
old='                    "answer": result.answer,'
new=old+'\n                    "knowledge": (result.decision_artifact or {}).get("migration", {}),'
assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf8')
p=H/'app/knowledge/common/build_info.py';s=p.read_text('utf8').replace('common-r68-source-completion','common-r69-isolated-chat');p.write_text(s,encoding='utf8')
p=H/'web_chat/index.html';s=p.read_text('utf8').replace('<title>PSU Esports Chatbot Demo</title>','<title>PSU Esports — แชทข้อมูลชุดใหม่ R69</title>').replace('<h1 id="page-title">Chatbot Demo</h1>','<h1 id="page-title">แชทข้อมูลชุดใหม่</h1>')
needle='        <div class="demo-layout">';assert needle in s
s=s.replace(needle,'        <div class="migration-banner" role="status">ข้อมูลชุดย้าย R69 — กำลังตรวจสอบก่อนเผยแพร่<br><span lang="en">Migrated data preview — not yet published</span></div>\n'+needle)
for heading in ['metrics-heading','runtime-heading']:
 needle='<section class="side-section"'+(' aria-live="polite"' if heading=='runtime-heading' else '')+'>\n              <h2 id="'+heading+'">'
 if needle in s:s=s.replace(needle,needle.replace('class="side-section"','class="side-section technical-panel"'))
p.write_text(s,encoding='utf8')
p=H/'web_chat/styles.css';p.write_text(p.read_text('utf8')+'\n/* The migrated-data status is visible independently of debug controls. */\n.migration-banner{padding:12px 20px;background:#fff3cd;color:#574000;border-bottom:1px solid #e3ca77;line-height:1.6}.migration-banner span{font-size:.85rem}.technical-panel{display:none}\n',encoding='utf8')
p=H/'web_chat/app.js';s=p.read_text('utf8').replace('psu-chat-','psu-r69-chat-').replace('เริ่มถามได้เลย ระบบจะแสดงคำตอบพร้อม route, mode และแหล่งข้อมูลที่ใช้','ถามเรื่องเกม อุปกรณ์ ราคา การจอง กติกา หรือการใช้บริการได้เลย').replace('Ask a question to see the answer, route, mode, and verified sources.','Ask about games, equipment, prices, booking, rules or studio services.');p.write_text(s,encoding='utf8')
print('Connected the new chat API, copied common reader, independent sessions and visible migration status')
