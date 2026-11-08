import hashlib,json
from pathlib import Path
from r28_fixture import PROJECT,REPORT
path=PROJECT/'app/pipeline/answer_contracts.py'
snap=REPORT/'before/app/pipeline/answer_contracts.py';snap.parent.mkdir(parents=True,exist_ok=True)
with snap.open('xb') as f:f.write(path.read_bytes())
manifest=json.loads((REPORT/'before_manifest.json').read_text(encoding='utf-8'));manifest['app/pipeline/answer_contracts.py']=hashlib.sha256(path.read_bytes()).hexdigest()
(REPORT/'before_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
s=path.read_text(encoding='utf-8')
needle='    return types\n'
assert needle in s
s=s.replace(needle,'    # A source-backed partial reply must still satisfy fact/evidence gates.\n    if "competition_rule_detail_partial_source" in mode_key:\n        types.difference_update({"no_answer", "clarification"})\n'+needle,1)
path.write_text(s,encoding='utf-8')

path=PROJECT/'app/pipeline/competition_detail.py';s=path.read_text(encoding='utf-8')
s=s.replace("semifinals?|finals?'", "\\bsemifinals?\\b|\\bfinals\\b|\\bfinal (?:match|round|stage)\\b'")
s=s.replace('No scripts or macros|use of macros.*prohibited','No scripts or macros|Macros.*prohibited')
s=s.replace('customization.*prohibited|customization.*not allowed','No character customization|customization.*prohibited|customization.*not allowed')
path.write_text(s,encoding='utf-8')

path=PROJECT/'app/pipeline/competition_source_gaps.py';s=path.read_text(encoding='utf-8')
s=s.replace('I could not find a complete verified text','I could not find verified complete text').replace('I could not find a complete verified clause','I could not find verified complete clause')
s=s.replace('I could not find a registration fee','I could not find verified registration-fee information')
s=s.replace('I could not find a minimum age requirement','I could not find verified minimum-age information')
path.write_text(s,encoding='utf-8')

path=PROJECT/'tests/test_competition_composition_r28_20261001.py';s=path.read_text(encoding='utf-8')
s=s.replace("self.assertIn('install',result.answer);self.assertIn('prohibited',result.answer)","self.assertIn('install',result.answer);self.assertIn('Do not install',result.answer)")
s=s.replace("self.assertIn('could not find a registration fee',result.answer)","self.assertIn('could not find verified registration-fee information',result.answer)")
s+='''
    def test_final_decision_is_not_the_final_match(self):
        result=answer('Under CS2 tournament rules, whose decisions are final?','en')
        self.assertIn('Judgment authority',result.answer.splitlines()[0])
        self.assertNotIn('Semifinals',result.answer)

    def test_partial_reply_does_not_bypass_foreign_game_evidence(self):
        from app.pipeline.validator import validate_answer
        from app.pipeline.retrieval import load_curated_rows,hit_from_curated
        q='Under CS2 tournament rules, are scripts allowed and what is the registration fee?'
        result=answer(q,'en')
        foreign=next(r for r in load_curated_rows() if str(r.get('id','')).startswith('competition_rules_valorant_psu_phuket_2026_s01'))
        validation=validate_answer(q,result.answer,result.route,result.entities,hits=[hit_from_curated(foreign)],mode=result.mode)
        self.assertFalse(validation.ok)
'''
path.write_text(s,encoding='utf-8')

data=json.loads((REPORT/'composition_fixture_v2.json').read_text(encoding='utf-8'));audit=[]
for case in data['cases']:
    if case['anchor']=='valorant-outside' and case['locale']=='en':
        removed=[x for x in case['clauses'] if x.startswith('Agent abilities: Cypher')]
        assert len(removed)==1
        case['clauses']=[x for x in case['clauses'] if x not in removed]
        audit.append({'id':case['id'],'removed_unrequested_clause':removed[0],'reason':'EN expected-pattern Abilities.*not also matched the Agent abilities: Cypher prefix. The single question asks outside-boundary use, not camera texture placement. General prohibition and KAY/O exception remain required. Composite Cypher+outside cases keep all three clauses.'})
with (REPORT/'composition_fixture_v3.json').open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
with (REPORT/'oracle_revision_audit.json').open('x',encoding='utf-8') as f:json.dump(audit,f,ensure_ascii=False,indent=2)
print('Fixed source phrasing, final-vs-finals and safe/partial outcome contracts; oracle audit preserves v1/v2')
