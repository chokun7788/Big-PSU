from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system'
p=H/'app/web_api/server.py';s=p.read_text('utf8');old='    def do_POST(self) -> None:\n';assert old in s
new='''    def do_POST(self) -> None:
        # Only the launcher that owns this separate loopback server can stop it.
        if urlparse(self.path).path == '/api/shutdown':
            import hmac
            from app.knowledge.common.migrated_view import enabled as migrated_chat_enabled
            token = os.getenv('PSU_R69_LAUNCH_TOKEN', '')
            if not migrated_chat_enabled() or self.client_address[0] != '127.0.0.1' or not token or not hmac.compare_digest(self.headers.get('X-PSU-Launch-Token', ''), token):
                self._send_json({'ok': False, 'error': 'launcher_token_required'}, 403)
                return
            self._send_json({'ok': True, 'status': 'stopping'})
            threading.Thread(target=self.server.shutdown, daemon=True).start()
            return
'''
s=s.replace(old,new,1);p.write_text(s,encoding='utf8')
p=H/'web_chat/app.js';s=p.read_text('utf8');old='''    const meta = [
      data.mode || "unknown",
      data.route_category && data.route_intent ? `${data.route_category}/${data.route_intent}` : "no-route",'''
assert old in s;s=s.replace(old,'''    const meta = [
      uiLocale === "en" ? "Assistant" : "ผู้ช่วย",''',1);p.write_text(s,encoding='utf8')
print('Added owned graceful stop and simplified chat reply labels')
