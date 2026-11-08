from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=ROOT/'app/pipeline/service_query_completion.py';s=p.read_text(encoding='utf-8');s=s.replace("game_list=bool(re.search(r'", "game_list=bool(re.search(r'เกม.{0,18}กี่เกม|")
s=s.replace('        from app.pipeline.entity_resolver import resolve_game_entity\n','        from app.pipeline.entity_resolver import resolve_game_entity\n        from app.runtime.fast_answer import is_known_unsupported_game_query\n        if is_known_unsupported_game_query(q):return None\n');p.write_text(s,encoding='utf-8')
p=ROOT/'app/pipeline/competition_conversation_signals.py';s=p.read_text(encoding='utf-8');s=s.replace('|about|it|its|this|','|about|with|page|pages|it|its|this|');s=s.replace('(?:please )?(?:continue|go on))','(?:please )?(?:continue|go on)|(?:the )?next page)');p.write_text(s,encoding='utf-8')
p=ROOT/'tests/test_service_repairs_r55.py';s=p.read_text(encoding='utf-8');s=s.replace("self.assertTrue(is_more_rule_request('ต่อ เอากฎที่เหลือ'))", "self.assertTrue(is_more_rule_request('ต่อ เอากฎที่เหลือ'))\n        self.assertTrue(is_more_rule_request('Continue with the remaining rules.'))")
s=s.replace("('ศูนย์มีเกมทั้งหมดกี่เกม','th','',42)", "('ศูนย์มีเกมทั้งหมดกี่เกม','th','',42),('ที่ศูนย์มีเกมให้เล่นทั้งหมดกี่เกม','th','',42)");p.write_text(s,encoding='utf-8')
print('explicit game-count grammar and English continuation fixed')
