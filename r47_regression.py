import sys,re
import r46_regression as old
old_cases=old.current.prior.r.p.cases
old_grade=old.current.prior.grade
import r47_probe as new

def cases():
    return old_cases()+new.cases()

def grade(c,rs):
    if 'kind' in c:return new.grade(c,rs)
    b=rs[-1]['response'];q=rs[-1]['payload']['question'];answer=b.get('answer','')
    if c['id']=='en-venue-location':return new.grade({**c,'kind':'location'},rs)
    if c['id']=='en-venue-hours':return new.grade({**c,'kind':'other','category':'schedule','required':['09:00-12:00','13:00-16:00','12:00-13:00','maintenance','Monday','Friday'],'forbidden':[new.ADDRESS_EN]},rs)
    result=old_grade(c,rs)
    if c.get('negative'):
        if 'hourly-shift' in c['id'] or 'pc-price-shift' in c['id']:
            result['checks'].update(correct_category=b.get('route_category')=='service_fee',pc_source='local://service_fee/pc_price_update_20260727' in answer,pc_25_and_70=bool(re.search(r'25\s*(?:THB|บาท)',answer)) and bool(re.search(r'70\s*(?:THB|บาท)',answer)))
        elif 'games-shift' in c['id'] or c['id']=='en-topic-games':
            source_url='https://esports.computing.psu.ac.th/' if c['locale']=='th' else 'https://esports.phuket.psu.ac.th/Services/our-games'
            result['checks'].update(correct_category=b.get('route_category')=='games',pc_catalog_content=all(x in answer for x in ['PC Zone','VALORANT','Counter-Strike 2']),no_other_zone=not any(x in answer for x in ['VR Zone','PlayStation 5 Zone','Nintendo Switch Zone']),catalog_source=source_url in answer)
        elif c['id']=='en-topic-rules':
            result['checks'].update(correct_category=b.get('route_category')=='competition_rules',cs2_rule_content='Counter-Strike 2' in answer and 'Single Elimination' in answer and '5 players' in answer,correct_rulebook='local://competition_rules/competition_rules_cs2_psu_phuket_2026' in answer)
    result['passed']=all(result['checks'].values())
    return result

new.prior.prior.r.p.cases=cases;new.prior.prior.r.p.grade=grade
if __name__=='__main__':new.prior.prior.r.p.run(sys.argv[1],sys.argv[2])
