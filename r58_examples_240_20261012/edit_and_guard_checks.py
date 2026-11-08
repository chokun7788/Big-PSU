import json,copy,hashlib,sqlite3,os
from pathlib import Path
import build_and_test as task
def main():
    out=task.BASE/'edit_demo';out.mkdir(exist_ok=False)
    path=out/'DEMO_EDITS_ONLY.sqlite'
    src=sqlite3.connect('file:'+task.DB.as_posix()+'?mode=ro',uri=True);dst=sqlite3.connect(path);src.backup(dst);dst.close();src.close()
    store=task.CommonStore(path);rows=[];ids=[]
    for kind,key in [('game','how_to_play'),('rate','amount_minor'),('policy','details'),('competition_rule','text')]:
        for i in range(1,11):
            rid=task.rid(kind,i);old=store.revision(rid,1);r=copy.deepcopy(old['record']);v=r['fields'][key]['value']
            r['fields'][key]['value']=v+500 if isinstance(v,int) else {'th':v['th']+' — ปรับปรุงเฉพาะตัวอย่าง','en':v['en']+' — updated demo only'}
            snapshot=task.canonical_json({k:f['value'] for k,f in r['fields'].items() if f['status']=='known'});sid='edited_fixture_'+rid
            source={'source_id':sid,'kind':'fixture','path':str(path),'sha256':hashlib.sha256(snapshot.encode()).hexdigest(),'authority_for':[kind],'observed_at':'2026-10-12T00:00:00+07:00','trust':'synthetic','public_url':None}
            store.add_source(source,snapshot,actor=task.ACTOR)
            for k,f in r['fields'].items():
                if f['status']=='known':f['evidence_refs']=[{'source_id':sid,'locator':'/'+k}]
            x=store.save(r,actor=task.ACTOR,expected_version=1,change_note=task.WARNING)
            old_live=store.edit_context(rid)['published']['fields'][key]['value']==v
            store.approve(rid,x['version'],x['hash'],actor=task.ACTOR)
            still_old=store.edit_context(rid)['published']['fields'][key]['value']==v
            rows.append({'record_id':rid,'kind':kind,'field':key,'old_live_after_save':old_live,'old_live_after_approval':still_old,'old_revision_unchanged':store.revision(rid,1)['record']==old['record'],'new_value':r['fields'][key]['value']});ids.append(rid)
    store.publish(ids,actor=task.ACTOR,expected_active=store.snapshot()['active'],request_key='edited-demo-40')
    for r in rows:
        r['new_live_after_publish']=store.edit_context(r['record_id'])['published']['fields'][r['field']]['value']==r['new_value']
        r['passed']=all(r[k] for k in ['old_live_after_save','old_live_after_approval','old_revision_unchanged','new_live_after_publish'])
    task.filejson('EDIT_40_RESULTS.json',rows)
    guard=task.CommonStore(out/'EMPTY_PRODUCTION_GUARD_TEST.sqlite');guard.initialize(allow_demo=False)
    fixture=task.CommonStore(task.DB)
    with fixture.connect() as c:source,snapshot=next(iter(fixture.sources(c).values()))
    try:guard.add_source(source,snapshot,actor='demo-guard-check');raise AssertionError('Synthetic import accepted in non-demo store')
    except ValueError as e:rejection=str(e)
    with guard.connect() as c:empty=c.execute('select count(*) from cc_sources').fetchone()[0]==0
    os.environ['PSU_KNOWLEDGE_DB']=str(task.DB);os.environ['PSU_COMMON_ALLOW_DEMO']='0'
    from app.knowledge.common.answer import try_common_answer
    ignored=try_common_answer('Demo game 01 all details',locale='en',allow_llm=False) is None
    task.filejson('EDIT_AND_GUARD_SUMMARY.json',{'edit_cases':40,'pass':sum(r['passed'] for r in rows),'fail':sum(not r['passed'] for r in rows),'kinds_each_10':['game','rate','policy','competition_rule'],'production_import_rejected':rejection,'empty_production_test_store_remains_empty':empty,'demo_reader_ignored_without_explicit_opt_in':ignored,'all_operations_in_isolated_demo_copies':True})
    print('40 edit cases: '+str(sum(r['passed'] for r in rows))+' passed; fixture guard='+str(empty and ignored),flush=True)
if __name__=='__main__':main()
