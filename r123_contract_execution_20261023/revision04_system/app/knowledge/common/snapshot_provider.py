"""Read-only owner draft snapshots for the same dispatcher as public chat."""
import json
from .store import CommonStore
from .registry import CATALOG,value

class DraftSnapshotView:
 def __init__(self,store):self.store=store;self.path=store.path
 def connect(self,*,write=False):
  if write:raise ValueError('Draft preview exposes read-only evidence access')
  return self.store.connect()
 @staticmethod
 def sources(connection):return CommonStore.sources(connection)
 def snapshot(self):
  with self.store.connect() as c:
   meta=dict(c.execute('SELECT key,value FROM cc_meta'))
   records=CommonStore.heads(c);sources={sid:pair[0] for sid,pair in CommonStore.sources(c).items()}
   withdrawn=[r[0] for r in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]
   historical=dict(c.execute('SELECT record_id,kind FROM cc_heads'))
  from .answer import title
  names={rid:list(dict.fromkeys(r['aliases']['th']+r['aliases']['en']+[title(r,'th'),title(r,'en')])) for rid,r in records.items()}
  refs={};index=[]
  for rid,r in records.items():
   for f in CATALOG[r['kind']]['fields']:
    v=value(r,f['key'])
    if v is None:continue
    index.append({'id':rid+':'+f['key'],'record_id':rid,'field':f['key'],'text':json.dumps(v,ensure_ascii=False)})
    if f['reference_kind']:
     for target in v if isinstance(v,list) else [v]:refs.setdefault(target,[]).append(rid)
  from .claim_bindings import references,index as claim_index
  for rid,r in records.items():
   for target in references(r):refs.setdefault(target,[]).append(rid)
  return {'active':'owner-draft-preview','epoch':int(meta['epoch']),
   'release':{'records':records,'sources':sources,'names':names,'reverse_refs':refs,'text_index':index,'claim_index':claim_index(records)},
   'withdrawn':withdrawn,'historical_names':{},'retired_names':{},'historical_kinds':historical,
   'allow_demo':meta.get('demo')=='1','evaluation_draft_only':True,'owner_draft_preview':True,
   'actual_active_release':meta.get('active','')}
 def still_current(self,snap):
  with self.store.connect() as c:row=c.execute("SELECT value FROM cc_meta WHERE key='epoch'").fetchone()
  return row is not None and int(row[0])==snap['epoch']

class PinnedSnapshotView:
 """One coherent revision set across compound parts and dialogue repair."""
 def __init__(self,store):
  self.store=store;self.path=store.path;self._snapshot=store.snapshot()
  self.migration_preview_only=bool(self._snapshot.get('migration_preview_only'))
 def snapshot(self):return self._snapshot
 def connect(self,*,write=False):
  if write:raise ValueError('Question snapshots are read only')
  return self.store.connect()
 def sources(self,connection):return self.store.sources(connection)
 def still_current(self,snap):return self.store.still_current(snap)
