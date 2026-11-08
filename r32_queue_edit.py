from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert old in s,rel;p.write_text(s.replace(old,new,1),encoding='utf-8')
helper='''/* Bounded retry for rejected queue admission only. A timeout, network failure,
 * server exception or successful answer is never replayed automatically. */
(function (root) {
  async function requestChat(payload, options = {}) {
    const fetchImpl = options.fetchImpl || root.fetch.bind(root);
    const sleep = options.sleep || ((ms) => new Promise((resolve) => setTimeout(resolve, ms)));
    const now = options.now || (() => Date.now());
    const started = now();
    const body = JSON.stringify(payload);
    for (let attempt = 0; attempt < 3; attempt += 1) {
      const response = await fetchImpl('/api/chat', {method: 'POST', headers: {'Content-Type': 'application/json'}, body});
      const raw = await response.text();
      let data;
      try { data = raw ? JSON.parse(raw) : {}; }
      catch (_) { throw new Error(`API returned non-JSON (${response.status}): ${raw.slice(0,160) || 'empty response'}`); }
      const queueRejected = response.status === 503 && data.ok === false && data.retryable === true
        && ['server_busy', 'pipeline_worker_restarting'].includes(data.error);
      const suggested = Number(data.retry_after_ms);
      const delay = Number.isFinite(suggested) && suggested > 0 ? Math.min(1500, Math.max(250,suggested)) : 500;
      if (!queueRejected || attempt === 2 || now() - started + delay > 12000) return {response, data};
      if (options.onRetry) options.onRetry(data, attempt + 1);
      await sleep(delay);
    }
  }
  root.PSUChatRequest = {requestChat};
  if (typeof module !== 'undefined' && module.exports) module.exports = root.PSUChatRequest;
})(typeof globalThis !== 'undefined' ? globalThis : this);
'''
(P/'web_chat/chat_request.js').write_text(helper,encoding='utf-8')
edit('web_chat/index.html','    <script src="/app.js"></script>','    <script src="/chat_request.js"></script>\n    <script src="/app.js"></script>')
edit('web_chat/app.js','    answering: "กำลังตอบ",','    answering: "กำลังตอบ",\n    queueWaiting: "มีผู้ใช้งานพร้อมกัน กำลังรอคิวและลองส่งคำถามอีกครั้ง...",')
edit('web_chat/app.js','    answering: "Answering",','    answering: "Answering",\n    queueWaiting: "Other requests are being answered. Waiting briefly and retrying your question...",')
p=P/'web_chat/app.js';s=p.read_text(encoding='utf-8');start=s.index('    const response = await fetch("/api/chat", {',s.index('async function ask('));end=s.index('    if (!response.ok || !data.ok)',start)
s=s[:start]+'''    const {response, data} = await PSUChatRequest.requestChat({
      question: cleanQuestion,
      client_session_id: clientSessionId,
      recent_history: outgoingHistory,
      locale: selectedLocale,
      debug: true,
      experimental_rag_fallback: experimentalRagFallback,
      experimental_allow_llm: experimentalAllowLlm,
    }, {onRetry: (busy) => {
      const lang = busy.language?.effective || uiLocale;
      setStatus(true, (localeCopy[lang] || copy()).queueWaiting);
    }});

'''+s[end:];p.write_text(s,encoding='utf-8')
edit('app/web_api/server.py','*, content_language: str | None = None) -> None:\n        self.send_response(status)', '*, content_language: str | None = None, retry_after_ms: int | None = None) -> None:\n        self.send_response(status)')
edit('app/web_api/server.py','        self.end_headers()\n        self.wfile.write(body)', '''        if status == 503 and retry_after_ms is not None:
            self.send_header("Retry-After", str(max(1, (retry_after_ms + 999) // 1000)))
        self.end_headers()
        self.wfile.write(body)''')
edit('app/web_api/server.py','        self._send_bytes(code, body, "application/json; charset=utf-8", content_language=content_language)', '''        retry_ms = 500 if code == 503 and payload.get("retryable") is True else None
        self._send_bytes(code, body, "application/json; charset=utf-8", content_language=content_language, retry_after_ms=retry_ms)''')
edit('app/web_api/server.py','                    "retry_after_ms": 250,\n                    "message":', '                    "retry_after_ms": 250,\n                    "retryable": True,\n                    "message":')
print('bounded queue retry with localized status, HTTP retry header')
