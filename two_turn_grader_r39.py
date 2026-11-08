"""Grade both turns, requested operation and scope using one oracle for both versions."""
import json
from pathlib import Path

OUT = Path((Path(__file__).parent / 'two_turn_current_path.txt').read_text(encoding='utf-8'))

def grade(case, first, second, status=200):
    mode = first.get('mode', '')
    initial_ok = not case['requires_clarification'] or (
        first.get('route_category') == 'clarification' or any(k in mode for k in (
            'clarification', 'missing_game_context', 'service_broad_choice', 'games_family')))
    category = second.get('route_category') == case['expected_category']
    if case['expected_category'] == 'game_control':
        category = second.get('route_category') == 'games' and second.get('route_intent') == 'game_control_lookup' and 'structured_game_controls' in second.get('mode','')
    content = all(s.casefold() in second.get('answer', '').casefold() for s in case['expected_contains'])
    content = content and all(s.casefold() not in second.get('answer', '').casefold() for s in case.get('forbidden_contains', []))
    if '-pc-domain-games' in case['id']:
        content = content and all(s not in second.get('answer', '') for s in ['Nintendo Switch Zone', 'PlayStation 5 Zone'])
    scope = not case['full_detail'] or (second.get('rule_coverage') or {}).get('detail_level') == 'full_sections'
    if '-cod-' in case['id']:
        initial_ok = initial_ok and 'games_family' in mode
        category = category and second.get('route_intent') == 'game_detail_lookup'
    if case.get('expected_intent'):
        category = category and second.get('route_intent') == case['expected_intent']
    price_ok=True
    if '-price-' in case['id']:
        contract=second.get('price_contract') or next((t['metadata'] for t in second.get('trace',[]) if t.get('stage')=='conversation_contract'),{})
        rows=contract.get('rows',[])
        gold={'pc':(25,70),'ps5':(50,150),'nintendo_switch_1_2':(50,140),'nintendo_switch_3_4':(100,280),'cockpit':(65,200),'vr_30':(190,525),'vr_60':(375,1050)}
        price_ok=bool(rows) and {r['group_id'] for r in rows}=={'general_student','general_adult'}
        price_ok=price_ok and set(contract.get('expected_ids',[]))==set(contract.get('returned_ids',[])) and not contract.get('missing_ids')
        price_ok=price_ok and all(r['unit_price']==gold[r['package_id']][r['group_id']=='general_adult'] for r in rows)
    checks = dict(first_question=initial_ok, category_and_operation=category, content=content, scope=scope, price_groups_and_recorded_rates=price_ok, http=status == 200)
    return dict(case=case, passed=all(checks.values()), checks=checks, first_mode=mode,
                second_mode=second.get('mode'), second_intent=second.get('route_intent'),
                resolved_question=second.get('resolved_question'), answer=second.get('answer'))

def regrade(raw, cases):
    turns = {}
    for line in raw.read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        turns.setdefault(r['case_id'], []).append(r)
    results = []
    for c in cases:
        a, b = turns[c['id']]
        results.append(grade(c, a['response'], b['response'], b['status']))
    return dict(raw=raw.name, conversations=len(results), requests=sum(map(len,turns.values())),
                passed=sum(x['passed'] for x in results), results=results)

if __name__ == '__main__':
    cases = json.loads((OUT/'cases.json').read_text(encoding='utf-8'))
    raw = OUT/'api_8093_000042.jsonl'
    result = regrade(raw, cases)
    (OUT/'baseline_final_oracle_regrade_r38_5.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Baseline strict:',result['passed'],'/',result['conversations'])
    for x in result['results']:
        if not x['passed']:print(x['case']['id'], x['checks'])
