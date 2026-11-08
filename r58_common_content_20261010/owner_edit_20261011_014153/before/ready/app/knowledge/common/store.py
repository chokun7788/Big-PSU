"""V3 tables share the existing KnowledgeStore database; V2 pilot tables stay intact."""
from __future__ import annotations
import json, sqlite3, uuid
from pathlib import Path
from app.knowledge.store import KnowledgeStore, Conflict
from app.knowledge.records import canonical_json,digest
from .registry import VERSION,now,validate,source_errors,release_errors,content_hash,CATALOG

class CommonStore(KnowledgeStore):
    def initialize(self,*,allow_demo=False):
        super().initialize(allow_demo=allow_demo)
        with self.connect(write=True) as c:
            for sql in (
                'CREATE TABLE IF NOT EXISTS cc_meta (key TEXT PRIMARY KEY,value TEXT NOT NULL)',
                'CREATE TABLE IF NOT EXISTS cc_names (record_id TEXT NOT NULL,name TEXT NOT NULL,PRIMARY KEY(record_id,name))',
                'CREATE TABLE IF NOT EXISTS cc_sources (source_id TEXT PRIMARY KEY,payload TEXT NOT NULL,snapshot TEXT NOT NULL)',
                'CREATE TABLE IF NOT EXISTS cc_heads (record_id TEXT PRIMARY KEY,kind TEXT NOT NULL,head INTEGER NOT NULL,withdrawn INTEGER NOT NULL DEFAULT 0)',
                'CREATE TABLE IF NOT EXISTS cc_revisions (record_id TEXT NOT NULL,version INTEGER NOT NULL,payload TEXT NOT NULL,hash TEXT NOT NULL,actor TEXT NOT NULL,at TEXT NOT NULL,PRIMARY KEY(record_id,version))',
                'CREATE TABLE IF NOT EXISTS cc_approvals (record_id TEXT NOT NULL,version INTEGER NOT NULL,hash TEXT NOT NULL,actor TEXT NOT NULL,at TEXT NOT NULL,PRIMARY KEY(record_id,version))',
                'CREATE TABLE IF NOT EXISTS cc_releases (release_id TEXT PRIMARY KEY,payload TEXT NOT NULL,hash TEXT NOT NULL,base_release TEXT NOT NULL,request_key TEXT UNIQUE NOT NULL,at TEXT NOT NULL)',
                'CREATE TABLE IF NOT EXISTS cc_audit (id INTEGER PRIMARY KEY,event TEXT NOT NULL,actor TEXT NOT NULL,at TEXT NOT NULL,detail TEXT NOT NULL)'):
                c.execute(sql)
            c.execute("INSERT OR IGNORE INTO cc_meta VALUES ('active','')")
            c.execute("INSERT OR IGNORE INTO cc_meta VALUES ('epoch','0')")
            c.execute("INSERT OR IGNORE INTO cc_meta VALUES ('demo',?)",('1' if allow_demo else '0',))
            c.execute("INSERT OR IGNORE INTO cc_meta VALUES ('registry',?)",(VERSION,))
            for row in c.execute('SELECT payload FROM cc_releases').fetchall():
                for rid,names in json.loads(row[0])['names'].items():
                    c.executemany('INSERT OR IGNORE INTO cc_names VALUES (?,?)',[(rid,n) for n in names])
    @staticmethod
    def audit(c,event,actor,detail):
        if not isinstance(actor,str) or not actor.strip() or len(actor)>100:raise ValueError('Local operator required')
        c.execute('INSERT INTO cc_audit(event,actor,at,detail) VALUES (?,?,?,?)',(event,actor,now(),canonical_json(detail)))
    @staticmethod
    def sources(c):
        return {r['source_id']:(json.loads(r['payload']),r['snapshot']) for r in c.execute('SELECT * FROM cc_sources')}
    def add_source(self,source,snapshot,*,actor):
        with self.connect(write=True) as c:
            demo=c.execute("SELECT value FROM cc_meta WHERE key='demo'").fetchone()[0]=='1'
            errs=source_errors(source,snapshot,demo=demo)
            if errs:raise ValueError('; '.join(errs))
            old=c.execute('SELECT * FROM cc_sources WHERE source_id=?',(source['source_id'],)).fetchone()
            payload=canonical_json(source)
            if old:
                if old['payload']!=payload or old['snapshot']!=snapshot:raise Conflict('Immutable source ID already exists')
                return
            c.execute('INSERT INTO cc_sources VALUES (?,?,?)',(source['source_id'],payload,snapshot))
            self.audit(c,'source',actor,{'source_id':source['source_id'],'sha256':source['sha256']})
    @staticmethod
    def heads(c):
        return {r['record_id']:json.loads(r['payload']) for r in c.execute('SELECT r.* FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')}
    def save(self,record,*,actor,expected_version):
        with self.connect(write=True) as c:
            record=json.loads(canonical_json(record));rid=record.get('record_id')
            old=c.execute('SELECT * FROM cc_heads WHERE record_id=?',(rid,)).fetchone()
            head=old['head'] if old else 0
            if type(expected_version) is not int or expected_version!=head or (old and old['withdrawn']):raise Conflict('Stale or withdrawn revision')
            if old and old['kind']!=record.get('kind'):raise Conflict('Stable ID cannot change kind')
            record.update(revision=head+1,lifecycle='draft',review={'actor_id':None,'reviewed_at':None,'revision_sha256':None})
            if record.get('localization',{}).get('en_status')=='reviewed':
                if record['localization']['source_revision_hash']!=content_hash(record):
                    record['localization'].update(en_status='stale',source_revision_hash=None)
            records=self.heads(c);records[rid]=record
            demo=c.execute("SELECT value FROM cc_meta WHERE key='demo'").fetchone()[0]=='1'
            errs=validate(record,records,self.sources(c),demo=demo)
            if errs:raise ValueError('; '.join(errs))
            h=digest(record)
            c.execute('INSERT INTO cc_revisions VALUES (?,?,?,?,?,?)',(rid,head+1,canonical_json(record),h,actor,now()))
            c.execute('INSERT INTO cc_heads VALUES (?,?,?,0) ON CONFLICT(record_id) DO UPDATE SET head=excluded.head',(rid,record['kind'],head+1))
            c.execute("UPDATE cc_meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
            self.audit(c,'save',actor,{'record_id':rid,'version':head+1,'hash':h})
            return {'record_id':rid,'version':head+1,'hash':h}
    def list_heads(self):
        with self.connect() as c:
            rows=[]
            for row in c.execute('SELECT h.*,r.hash,r.payload,a.hash AS approved_hash FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version LEFT JOIN cc_approvals a ON a.record_id=r.record_id AND a.version=r.version ORDER BY h.kind,h.record_id'):
                item=dict(row);record=json.loads(item.pop('payload'));item['label']=item['record_id']
                for key in ('title','name','display_name','event_name','subject','question','heading'):
                    v=record['fields'].get(key,{})
                    if v.get('status')=='known' and isinstance(v.get('value'),dict):item['label']=v['value'].get('th') or v['value'].get('en') or item['label'];break
                rows.append(item)
            return rows
    def get(self,rid):
        with self.connect() as c:
            r=c.execute('SELECT r.*,h.withdrawn,a.hash AS approved_hash FROM cc_revisions r JOIN cc_heads h ON h.record_id=r.record_id AND h.head=r.version LEFT JOIN cc_approvals a ON a.record_id=r.record_id AND a.version=r.version WHERE r.record_id=?',(rid,)).fetchone()
            if r is None:raise ValueError('Unknown record')
            return {**dict(r),'record':json.loads(r['payload'])}
    def approve(self,rid,version,expected_hash,*,actor):
        with self.connect(write=True) as c:
            r=c.execute('SELECT r.* FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.record_id=? AND r.version=? AND r.version=h.head AND h.withdrawn=0',(rid,version)).fetchone()
            if not r or r['hash']!=expected_hash or digest(json.loads(r['payload']))!=expected_hash:raise Conflict('Approval must match current revision')
            record=json.loads(r['payload']);records=self.heads(c)
            demo=c.execute("SELECT value FROM cc_meta WHERE key='demo'").fetchone()[0]=='1'
            errs=validate(record,records,self.sources(c),publish=True,demo=demo)
            if errs:raise ValueError('; '.join(errs))
            c.execute('INSERT OR IGNORE INTO cc_approvals VALUES (?,?,?,?,?)',(rid,version,expected_hash,actor,now()))
            self.audit(c,'approve',actor,{'record_id':rid,'version':version,'hash':expected_hash})
    def snapshot(self):
        with self.connect() as c:
            meta=dict(c.execute('SELECT key,value FROM cc_meta'))
            row=c.execute('SELECT * FROM cc_releases WHERE release_id=?',(meta['active'],)).fetchone()
            release=json.loads(row['payload']) if row else None
            if row and (digest(release)!=row['hash'] or release['schema_version']!=VERSION):raise ValueError('Release integrity/version mismatch')
            withdrawn=[r[0] for r in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]
            retired_names={}
            if withdrawn and row:
                for name_row in c.execute('SELECT n.* FROM cc_names n JOIN cc_heads h USING(record_id) WHERE h.withdrawn=1'):
                    retired_names.setdefault(name_row['record_id'],[]).append(name_row['name'])
            return {'active':meta['active'],'epoch':int(meta['epoch']),'release':release,'withdrawn':withdrawn,'retired_names':retired_names,'allow_demo':meta['demo']=='1'}
    def publish(self,record_ids,*,actor,expected_active,request_key):
        if not isinstance(record_ids,list) or not record_ids or len(record_ids)>500 or len(set(record_ids))!=len(record_ids):raise ValueError('Select unique records for publication')
        if not isinstance(request_key,str) or not 1<=len(request_key)<=100:raise ValueError('Request key required')
        selection=digest(sorted(record_ids))
        with self.connect(write=True) as c:
            prior=c.execute('SELECT * FROM cc_releases WHERE request_key=?',(request_key,)).fetchone()
            if prior:
                p=json.loads(prior['payload'])
                if prior['base_release']!=expected_active or p['selection_hash']!=selection:raise Conflict('Idempotency key reused for another request')
                return prior['release_id']
            meta=dict(c.execute('SELECT key,value FROM cc_meta'))
            if meta['active']!=expected_active:raise Conflict('Active release changed')
            prev=c.execute('SELECT * FROM cc_releases WHERE release_id=?',(expected_active,)).fetchone()
            records=json.loads(prev['payload'])['records'] if prev else {}
            for rid in record_ids:
                r=c.execute('SELECT r.*,a.hash AS approval_hash FROM cc_revisions r JOIN cc_heads h USING(record_id) LEFT JOIN cc_approvals a ON r.record_id=a.record_id AND r.version=a.version WHERE r.record_id=? AND r.version=h.head AND h.withdrawn=0',(rid,)).fetchone()
                if not r or r['hash']!=r['approval_hash'] or digest(json.loads(r['payload']))!=r['hash']:raise Conflict('All selected revisions must be approved')
                records[rid]=json.loads(r['payload'])
            revoked={r[0] for r in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')}
            records={k:v for k,v in records.items() if k not in revoked}
            sources=self.sources(c)
            errs=release_errors(records,sources,demo=meta['demo']=='1')
            if errs:raise ValueError('; '.join(errs))
            # Full field index and FK graph are built before activation in the same transaction.
            refs={};names={};index=[]
            for rid,r in records.items():
                names[rid]=[v for key in ('name','title','display_name','event_name','question','subject') for v in ([r['fields'][key]['value'].get('th'),r['fields'][key]['value'].get('en')] if key in r['fields'] and r['fields'][key]['status']=='known' and isinstance(r['fields'][key]['value'],dict) else []) if v]+r['aliases']['th']+r['aliases']['en']
                for f in CATALOG[r['kind']]['fields']:
                    unit=r['fields'][f['key']]
                    if unit['status']=='known':index.append({'id':rid+':'+f['key'],'record_id':rid,'field':f['key'],'text':canonical_json(unit['value'])})
                    if unit['status']=='known' and f['reference_kind']:
                        for target in unit['value'] if isinstance(unit['value'],list) else [unit['value']]:refs.setdefault(target,[]).append(rid)
            used={ref['source_id'] for r in records.values() for f in r['fields'].values() for ref in f['evidence_refs']}
            payload={'schema_version':VERSION,'selection_hash':selection,'records':records,'names':names,'reverse_refs':refs,'text_index':index,'sources':{k:sources[k][0] for k in used}}
            for rid,aliases in names.items():c.executemany('INSERT OR IGNORE INTO cc_names VALUES (?,?)',[(rid,n) for n in aliases])
            release=uuid.uuid4().hex
            c.execute('INSERT INTO cc_releases VALUES (?,?,?,?,?,?)',(release,canonical_json(payload),digest(payload),expected_active,request_key,now()))
            c.execute("UPDATE cc_meta SET value=? WHERE key='active'",(release,))
            c.execute("UPDATE cc_meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
            self.audit(c,'publish',actor,{'release':release,'selected':record_ids,'hash':digest(payload)})
            return release
    def withdraw(self,rid,*,actor):
        with self.connect(write=True) as c:
            row=c.execute('SELECT * FROM cc_heads WHERE record_id=?',(rid,)).fetchone()
            if row is None:raise ValueError('Unknown record')
            active=c.execute("SELECT value FROM cc_meta WHERE key='active'").fetchone()[0]
            release=c.execute('SELECT payload FROM cc_releases WHERE release_id=?',(active,)).fetchone()
            if release:
                p=json.loads(release[0]);revoked={x[0] for x in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')}
                if any(x not in revoked and x!=rid for x in p['reverse_refs'].get(rid,[])):raise Conflict('Withdraw referring records first')
            c.execute('UPDATE cc_heads SET withdrawn=1 WHERE record_id=?',(rid,))
            c.execute("UPDATE cc_meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
            self.audit(c,'withdraw',actor,{'record_id':rid})
    def rollback(self,rid,*,actor,expected_active):
        with self.connect(write=True) as c:
            if c.execute("SELECT value FROM cc_meta WHERE key='active'").fetchone()[0]!=expected_active:raise Conflict('Stale rollback')
            r=c.execute('SELECT * FROM cc_releases WHERE release_id=?',(rid,)).fetchone()
            if not r:raise ValueError('Unknown release')
            p=json.loads(r['payload']);revoked={x[0] for x in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')}
            if digest(p)!=r['hash'] or p['schema_version']!=VERSION or revoked & p['records'].keys():raise Conflict('Unsafe or incompatible rollback')
            c.execute("UPDATE cc_meta SET value=? WHERE key='active'",(rid,))
            c.execute("UPDATE cc_meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
            self.audit(c,'rollback',actor,{'release':rid})
    def still_current(self,snapshot):
        with self.connect() as c:
            m=dict(c.execute('SELECT key,value FROM cc_meta'))
            return m['active']==snapshot['active'] and int(m['epoch'])==snapshot['epoch']
