from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/session/conversation_plan.py','    q = normalize_text(question)\n    active =', '''    q = normalize_text(question)
    from app.pipeline.service_query_completion import split_service_operations
    if len(split_service_operations(question))>1:
        return None  # Preserve raw compound before the server rewrites it.
    active =''')
edit('app/session/conversation_plan.py',"    if new_task:\n        return None", "    if new_task or (BOOKING.search(q) and not price):\n        return None")
edit('app/pipeline/service_query_completion.py',r'(?<![\d.])(\d+(?:\.\d+)?)',r'(?<![\d.,])((?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?)')
edit('app/pipeline/service_query_completion.py',"amount=float(money.group(1))", "amount=float(money.group(1).replace(',',''))")
edit('tests/test_service_repairs_r55.py',"    def test_catalog_totals_and_scopes(self):", '''    def test_server_plan_preserves_compound(self):
        self.assertIsNone(resolve_request_plan('PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่',[]))
        self.assertIsNone(resolve_request_plan('What games are on PC, and how much does two hours cost for a general adult?',[],locale='en'))
    def test_catalog_and_policy_negative_scopes(self):
        for q in ('มีเกม Minecraft ไหม','Can I install games myself?','ขอลงเกมอะไรเพิ่มได้บ้าง','ไม่เอารายการเกมอะไรแล้ว'):
            with self.subTest(q=q):self.assertIsNone(answer_explicit_source_operation(q,'en' if q.isascii() else 'th',RuleMatcher.default()))
        self.assertIn('change_time',answer_user_service_facts('อยากเปลี่ยนรอบที่จอง ต้องทำไง')['trace'][0].metadata['claim_ids'])
        self.assertIn('game_account_policy',answer_user_service_facts('เอา Steam ตัวเองล็อกอินได้ไหม')['validation'].warnings)
    def test_game_scope_task_memory(self):
        from app.session.task_memory import task_from_response,resolve_memory
        task=task_from_response('PC มีเกมอะไรบ้าง',dict(route_category='games',route_intent='game_list',mode='pipeline:source_operation_game_list',request_id='r1'))
        self.assertIsNotNone(task);self.assertEqual(task['operation'],'list')
    def test_budget_group_followup(self):
        history=[dict(role='user',text='I have 100 THB for PC'),dict(role='assistant',text='Which group?',route_category='clarification',route_intent='budget_group')]
        resolved=resolve_question_with_context('general adult',history,locale='en')
        self.assertTrue(resolved.used_context);self.assertIn('100',resolved.resolved_question)
        self.assertEqual(answer_budget(resolved.resolved_question,'en')['trace'][0].metadata['packages'][0]['sessions'],1)
    def test_catalog_totals_and_scopes(self):''')
print('server compound rewrite guarded')
