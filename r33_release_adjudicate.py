import json,urllib.request,uuid
from pathlib import Path
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
original=json.loads((R/'RELEASE_FINAL_I_VERIFICATION.json').read_text(encoding='utf-8'))
case=next(x for x in original['rows'] if x['question']=='สามารถถามอะไรดไ้บ้าง')
payload={'question':'สามารถถามอะไรได้บ้าง','locale':'th','recent_history':[],'client_session_id':'r33-release-control-'+uuid.uuid4().hex,'debug':True}
clean=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8090/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30))
answer=case['response']['answer']
passed=answer==clean['answer'] and 'ค่าบริการ' in answer and 'จอง' in answer and clean['validation_ok']
result=dict(original_literal_passed=original['passed'],original_total=original['total'],reviewed_case=case['question'],source_review_passed=passed,reason='The original new smoke oracle required ราคา literally. The approved capability answer says ค่าบริการ, includes booking, and the typo input returns exactly the clean capability answer. Runtime and old Gold are unchanged; preserve the original 9/10 literal result.',clean_response=clean,noisy_response=case['response'],reviewed_smoke_passed=original['passed']+int(passed),reviewer='assistant source/clean-control review, not human or owner approval')
with (R/'RELEASE_FINAL_I_CONTENT_ADJUDICATION.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(dict(passed=passed,answer=answer,reviewed_total=result['reviewed_smoke_passed']),ensure_ascii=False))
assert passed
