from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
p=H/'answer.py';s=p.read_text('utf8')
old="        if any(records[rid]['kind']=='competition' for rid in ids):\n            from app.pipeline.competition_taxonomy import detect_competition_facet\n            if (detect_competition_facet(raw_query) or query_operation=='rules') and not (broad and not re.search"
new="        if any(records[rid]['kind']=='competition' for rid in ids):\n            from app.pipeline.competition_taxonomy import detect_competition_facet\n            document_keys={f['key'] for f in CATALOG['competition']['fields']}\n            explicit_document_fields=bool(requested) and set(requested)<=document_keys and not broad\n            if not explicit_document_fields and (detect_competition_facet(raw_query) or query_operation=='rules') and not (broad and not re.search"
assert old in s;s=s.replace(old,new)
old="        secondary_audit=None;secondary_ids=None"
new="""        # A short FAQ alias such as 'location' cannot own an explicit studio
        # attribute that the FAQ schema has no field for.
        center_keys=field_requests(question,{'center'})
        if ids and all(records[rid]['kind']=='faq' for rid in ids) and set(center_keys)&{'timezone','operator','building','floor','map_url'} and re.search(r'ศูนย์|สตูดิโอ|\\b(?:studio|cent(?:er|re))\\b',normal(question)):
            centers=[rid for rid,r in records.items() if r['kind']=='center' and effective(r,at,records)]
            if len(centers)==1:ids=centers;scope_ids=list(ids);method='common_typed_attribute_scope'
        secondary_audit=None;secondary_ids=None"""
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf8')
p=H/'query_contract.py';s=p.read_text('utf8');old="def live_request(q):\n    q=normalize(q)"
new="def live_request(q):\n    q=normalize(q)\n    # This participle describes a booking mistake, not live occupancy. Other\n    # availability/status clauses stay in q and still reach the live adapter.\n    q=re.sub(r'\\b(?:wrongly|incorrectly|mistakenly)\\s+booked\\b',' ',q)"
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf8')
print('Fixed document attributes, studio attribute ownership, booking-error participles')
