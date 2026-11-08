from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system';p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
old="hits.append({'id':r['record_id']+':'+key+':'+citation,'title':";assert t.count(old)==1;t=t.replace(old,"hits.append({'id':r['record_id']+':'+key+':'+citation,'record_id':r['record_id'],'field':key,'title':")
old="hits.append({'id':rid+':title','title':";assert t.count(old)==1;t=t.replace(old,"hits.append({'id':rid+':title','record_id':rid,'field':'title','title':")
old="        for hit in hits:hit['metadata']={'common_approved':True,'title':hit['title'],'release_id':snap['active']}"
new="""        view='evaluation_draft' if snap.get('evaluation_draft_only') else 'synthetic_demo' if snap.get('allow_demo') else 'published'
        from .evidence import enrich_hit
        hits=[enrich_hit(hit,snap,self.store) for hit in hits]
        for hit in hits:
            if view!='published':hit['title']=('ร่างข้อมูลที่ใช้ทดสอบ' if lang_for_status(answer)=='th' else 'Evaluation draft information') if view=='evaluation_draft' else 'Synthetic fixture information'
            hit['metadata']={**hit.get('metadata',{}),'common_approved':view=='published','content_view':view,'title':hit['title'],'release_id':snap['active']}"""
assert t.count(old)==1;t=t.replace(old,new)
# Locale is not an argument to finish; status title need not guess locale from
# answer text. Use a bilingual caption, clearly different from factual approval.
t=t.replace("('ร่างข้อมูลที่ใช้ทดสอบ' if lang_for_status(answer)=='th' else 'Evaluation draft information')", "'ร่างข้อมูลทดสอบ / Evaluation draft information'")
t=t.replace("'validation_scope':'selected fields and evidence, not human intent correctness'}", "'validation_scope':'selected fields and evidence, not human intent correctness','content_view':view,'production_publication_verified':view=='published'}")
p.write_text(t,encoding='utf-8');print('FK-backed evidence identity and accurate draft/demo/publication labels')
