"""Exact website-citation admission and natural common-answer delivery controls."""
import copy
import json
import time
from verification_support import R, snapshot
from app.knowledge.common.public_citations import REGISTRY, apply
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.web_api.server import _source_list

snap = snapshot()
entries = json.loads(REGISTRY.read_text(encoding='utf-8'))['entries']
entry = next(e for e in entries if e['record_id']=='migrated_faq_rule_cancel_advance' and e['field']=='owner_policy')
rid = entry['record_id']
text = snap['release']['records'][rid]['fields']['answer']['value']['th']
hit = {'id':'fixture:S1','record_id':rid,'field':'owner_policy','text':text,
       'citation_label':'S1', **entry['evidence'][0]}
checks = {}

def denied(name, h=hit, s=snap, e=entries):
 answer, hits = apply(text+' [S1]', [h], s, e)
 checks[name] = '[S1]' not in answer and not hits[0]['source_url'] and not _source_list(hits)

answer, hits = apply(text+' [S1]', [hit], snap, entries)
checks['verified_link_delivered'] = '[S1]' in answer and _source_list(hits)[0]['url']==entry['url']
checks['internal_identity_retained'] = all(hits[0][k]==hit[k] for k in ('record_id','field','source_id','snapshot_sha256','locator'))
checks['does_not_grant_publication'] = hits[0]['metadata'].get('common_approved') is not True
denied('unknown_record', {**hit,'record_id':'another_center'})
denied('wrong_field', {**hit,'field':'amount'})
denied('forged_output', {**hit,'text':text+' FREE ALL SERVICES'})
denied('wrong_source', {**hit,'source_id':'forged'})
denied('wrong_locator', {**hit,'locator':'/unrelated'})
denied('wrong_hash', {**hit,'snapshot_sha256':'0'*64})
denied('empty_registry', e=[])
s=copy.deepcopy(snap);s['release']['records'][rid]['revision']+=1;denied('owner_revision_invalidates',s=s)
s=copy.deepcopy(snap);s['release']['records'][rid]['fields']['answer']['value']['th']='เปลี่ยนแล้ว';denied('owner_value_invalidates',s=s)
s=copy.deepcopy(snap);del s['release']['records'][rid];denied('withdrawal_invalidates',s=s)
s=copy.deepcopy(snap);p=s['source_pairs'][hit['source_id']];s['source_pairs'][hit['source_id']]=(p[0],p[1]+' ');denied('forged_source_snapshot',s=s)
denied('metadata_url_cannot_bypass', {**hit,'text':'UNVERIFIED','metadata':{'url':entry['url'],'source_url':entry['url']}})

view = MigratedView(R/'system/data/knowledge/common.sqlite')
pinned = view.snapshot()
class PinnedView:
 path=view.path
 def snapshot(self): return pinned
 def still_current(self,s): return True
 def connect(self,**kwargs): return view.connect(**kwargs)

reader=CommonAnswerer(PinnedView())
natural=[]
for lang,q in [('th','ยกเลิกการจองต้องทำล่วงหน้ากี่ชั่วโมง'),('en','Can I smoke inside the studio?'),('th','นักศึกษา PSU เล่น PC ราคาเท่าไหร่')]:
 result=reader.answer(q,locale=lang)
 natural.append({'question':q,'answer':result.answer,'sources':_source_list(result.hits),'artifact':result.decision_artifact})
 if 'ยกเลิก' in q:
  checks['natural_th_link']=any(x['url']==entry['url'] for x in _source_list(result.hits)) and '[S' in result.answer
 elif lang=='en':
  checks['natural_en_link']=any(x['url']==entry['url'] for x in _source_list(result.hits)) and '[S' in result.answer
 else:
  checks['zero_price_not_cited_as_image']=not _source_list(result.hits)
  checks['zero_price_still_delivered']='0 บาท' in result.answer and bool(result.hits)
 checks['draft_not_approved_'+lang+str(len(natural))]=all(h.get('metadata',{}).get('common_approved') is False for h in result.hits)
out=R/('public_citations_'+str(time.time_ns()));out.mkdir()
report={'all_passed':all(checks.values()),'checks':checks,
        'harness_amendments':['Initial harness lacked PinnedView.path; natural execution did not start. Added real copied database path.'],
        'scope':'source-only natural common answerer plus exact citation mutations; no HTTP/model/full semantic acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'DETAILS.json').write_text(json.dumps(natural,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(out),**report},ensure_ascii=False))
assert report['all_passed']
