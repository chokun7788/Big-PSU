from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
old="            localized=[rid for rid in procedure_ids if (value(records[rid],'answer') or {}).get(lang)]\n            ids=(localized or procedure_ids)[:1];method='common_procedure_topic';query_operation='booking'"
new="""            localized=[rid for rid in procedure_ids if (value(records[rid],'answer') or {}).get(lang)]
            from .provenance import owner_basis
            from .entity_search import grams
            candidates=localized or procedure_ids
            candidates.sort(key=lambda rid:(owner_basis(records[rid],self.store,rel),len(grams(question)&grams(text(value(records[rid],'question') or {},lang)))),reverse=True)
            ids=candidates[:1];method='common_procedure_topic'
            if query_operation!='checkin':query_operation='booking'"""
assert t.count(old)==1;p.write_text(t.replace(old,new),encoding='utf-8');print('FAQ source priority with byte-verified owner lineage; no approval upgrades')
