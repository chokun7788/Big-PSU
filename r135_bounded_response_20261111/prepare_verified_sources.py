"""Import observed official booking policy into a NEW candidate database only."""
import copy,hashlib,json,sqlite3,sys,urllib.request
from datetime import datetime,timezone
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now
from app.knowledge.records import canonical_json
from app.knowledge.common.public_citations import digest,text_digest

DB=P/'system/data/knowledge/verified_sources.sqlite'
OUT=P/'source_update_20261111'
IDS=['migrated_faq_rule_booking_max_sessions','migrated_faq_curated_reservation_max_sessions','migrated_faq_rule_booking_session_and_payment']

def main():
 assert not DB.exists() and not OUT.exists(),'Never overwrite or silently retry a source import'
 OUT.mkdir()
 url='https://esports.computing.psu.ac.th/'
 raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
 page=raw.decode('utf-8')
 assert 'maximum of 6 sessions' in page and '10 minutes' in page,'Changed website requires a new review'
 (OUT/'page.html').write_bytes(raw)
 before=sqlite3.connect((P/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
 target=sqlite3.connect(DB);before.backup(target);target.close();before.close()
 store=CommonStore(DB)
 current={rid:store.get(rid)['record'] for rid in IDS}
 answers={rid:{'th':'การจอง 1 ครั้งสามารถจองได้สูงสุด 6 Sessions','en':'One booking can include a maximum of 6 sessions.'} for rid in IDS}
 answers[IDS[2]]={'th':'การจอง 1 ครั้งจองได้สูงสุด 6 Sessions และหลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก',
                  'en':'One booking can include up to 6 sessions. Payment is due immediately after booking; if it is not paid within 10 minutes, the booking is cancelled.'}
 scope={'th':'กฎของระบบจอง PSU Esports Studio – Phuket ตามหน้าเว็บที่ตรวจ ณ วันนี้ ไม่ใช่กฎของหน่วยงานอื่น และไม่ใช่สถานะว่างจริง',
        'en':'PSU Esports Studio – Phuket reservation policy as observed; not another organization or live availability.'}
 mapped={rid:{'answer':answers[rid],'related_ids':['center_psu_phuket'],'scope_note':scope} for rid in IDS}
 payload={'url':url,'page_sha256':hashlib.sha256(raw).hexdigest(),'observed_at':now(),
          'section':'Rules and Regulations 1.2 / 1.3','subject':'PSU Esports Studio – Phuket Reservation System',
          'review':'Manual source-to-field review; no confirmed effective date, no publication approval.', 'mapped_records':mapped}
 snapshot=canonical_json(payload);sid='web_reservation_'+hashlib.sha256(snapshot.encode()).hexdigest()[:24]
 src={'source_id':sid,'kind':'official_page','path':url,'sha256':hashlib.sha256(snapshot.encode()).hexdigest(),
      'authority_for':['faq'],'observed_at':payload['observed_at'],'trust':'official','public_url':url}
 store.add_source(src,snapshot,actor='candidate-web-import')
 changes=[];entries=json.loads((P/'system/data/knowledge/verified_web_citations.json').read_text(encoding='utf-8'))
 for rid,old in current.items():
  record=copy.deepcopy(old)
  for field,value in mapped[rid].items():
   record['fields'][field]={'status':'known','value':value,'evidence_refs':[{'source_id':sid,'locator':'/mapped_records/'+rid+'/'+field}],
                            'note':'Observed official reservation website; draft only, effective interval not established'}
  record['localization'].update(source_language='mixed',en_status='agent_translated',source_revision_hash=None)
  result=store.save(record,expected_version=old['revision'],actor='candidate-web-import',change_note='Official page now says 6 sessions, replacing legacy 3 in candidate only; retain history')
  new=store.get(rid)['record']
  for field in ('answer','owner_policy'):
   entries['entries'].append({'record_id':rid,'field':field,'record_sha256':digest(new),
    'text_sha256':[text_digest(v) for v in answers[rid].values()],
    'evidence':[{'source_id':sid,'snapshot_sha256':src['sha256'],'locator':'/mapped_records/'+rid+'/answer'}],
    'url':url,'title':'PSU Esports Studio — Booking limits and payment','section':payload['section'],
    'checked_at':payload['observed_at'],'access':'live HTTP 200','page_sha256':payload['page_sha256'],'approval_effect':'none; website observation only'})
  changes.append({'record_id':rid,'old_revision':old['revision'],'new_revision':new['revision'],'old_answer':old['fields']['answer']['value'],'new_answer':answers[rid],
                  'related_ids':['center_psu_phuket'],'lifecycle':new['lifecycle'],'validity':new['validity']})
 (P/'system/data/knowledge/verified_web_citations.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')
 (OUT/'SOURCE_SNAPSHOT.json').write_text(snapshot,encoding='utf-8')
 report={'database':str(DB),'source':src,'changes':changes,'original_common_database_modified':False,
         'published':False,'price_changed':False,'scope':'3 booking-policy drafts only; not all fields or model semantics'}
 (OUT/'IMPORT_RECEIPT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'records_changed':len(changes),'source_id':sid,'database':str(DB),'published':False}))

if __name__=='__main__':main()
