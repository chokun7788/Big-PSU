from pathlib import Path
import r46_probe as r
root=r.prior.r.p.ROOT
p=root/'app/pipeline/zone_rental.py'
s=p.read_text(encoding='utf-8')
changes=[
 ('full[ -]?day|whole day|daily|per day','full[ -]?day|whole[ -]?day|daily|per day'),
 ("    excluded=excluded_services(q)\n    return list(dict.fromkeys(t for t in selected if t not in excluded))", "    # Resolve a misspelled service token even inside a long rental sentence.\n    for token in re.findall(r'[a-z]{4,}',_mask_unknown_codes(q),re.I):\n        selected.extend(service_mentions(token,fuzzy=True))\n    excluded=excluded_services(q)\n    if excluded and not selected:selected=list(TARGETS)\n    return list(dict.fromkeys(t for t in selected if t not in excluded))"),
 ('def _asks(q):','def _asks(q, *, default_rates=True):'),
 ('validity|effective date|valid from|expiry','validity|effective date|valid from|expiry|take effect'),
 ("    return list(dict.fromkeys(asks)) or ['rates']", "    if 'effective_date' in asks and re.search(r'\\bwhen\\b.*\\btake effect\\b',q,re.I):\n        asks=[a for a in asks if a!='rates']\n    return list(dict.fromkeys(asks)) or (['rates'] if default_rates else [])"),
 ('half[ -]?day|full[ -]?day|whole day','half[ -]?day|full[ -]?day|whole[ -]?day'),
 ('staff|overtime|available|availability|effective|expiry|seating|capacity|included','staff|overtime|available|availability|effective|expiry|seating|capacity|included|per machine|per device'),
 ('excluding|exclude|not|instead|cost|to','excluding|exclude|not|instead|cost|to|compare|versus|vs|with'),
 ("    information_followup=bool(previous and re.search(r'กี่ชั่วโมง|กี่โมง|ที่นั่ง|อุปกรณ์|รวมอะไร|มีอะไรให้|เจ้าหน้าที่|นอกเวลา|เริ่มใช้|^จอง(?:ยังไง|อย่างไร)|\\b(?:how many hours|seats|equipment|what is included|overtime|effective date|how do i book it)\\b',q,re.I))", "    field_asks=set(_asks(q,default_rates=False))\n    information_followup=bool(previous and field_asks & {'capacity','equipment','duration_definition','effective_date','booking','overtime'} and not re.search(r'เกม|กฎ|แข่งขัน|\\b(?:games?|competition|rules?|controls?)\\b',q,re.I))"),
 ("    pieces=re.split(r'\\s*(?:และ|;|\\band\\b)\\s*',q,flags=re.I)","    clause_pattern=r'\\s*(?:และ|;|\\band\\b|\\bversus\\b|\\bvs\\.?\\b)\\s*'\n    if re.search(r'\\bcompare\\b',q,re.I):clause_pattern=r'\\s*(?:และ|;|\\band\\b|\\bversus\\b|\\bvs\\.?\\b|\\bwith\\b)\\s*'\n    pieces=re.split(clause_pattern,q,flags=re.I)"),
]
for old,new in changes:
    assert old in s,old
    s=s.replace(old,new)
assert p.read_bytes()==(r.OUT/'before/app/pipeline/zone_rental.py').read_bytes(),'Source changed since snapshot'
p.write_text(s,encoding='utf-8')
print(p)
