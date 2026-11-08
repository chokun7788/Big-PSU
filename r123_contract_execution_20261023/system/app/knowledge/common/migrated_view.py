"""Explicit, read-only draft view for this separate migration chat installation."""
from __future__ import annotations
from pathlib import Path
from .store import CommonStore
from .registry import CATALOG,value

PROFILE='r69-migration-preview'
PUBLISHED_PROFILE='common-r102-published'
SYSTEM_ROOT=Path(__file__).resolve().parents[3]

def enabled():
 import os
 return os.getenv('PSU_COMMON_CHAT_PROFILE') in {PROFILE,PUBLISHED_PROFILE}

class MigratedView:
 def __init__(self,path):
  self.path=Path(path).resolve()
  if not self.path.is_relative_to(SYSTEM_ROOT/'data/knowledge'):
   raise ValueError('The migration chat may only read its own copied knowledge database')
  self.store=CommonStore(self.path)
 def connect(self,*,write=False):
  if write:raise ValueError('The chat knowledge view is read-only')
  return self.store.connect()
 @staticmethod
 def sources(connection):return CommonStore.sources(connection)
 def snapshot(self):
  # One SQLite read transaction keeps heads, sources and epoch consistent when
  # the separate owner editor saves a revision during a question.
  with self.store.connect() as c:
   # CommonStore.connect already begins the SQLite read transaction.
   meta=dict(c.execute('SELECT key,value FROM cc_meta'))
   records=CommonStore.heads(c);sources={sid:pair[0] for sid,pair in CommonStore.sources(c).items()}
   withdrawn=[row[0] for row in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]
   historical={row[0]:row[1] for row in c.execute('SELECT record_id,kind FROM cc_heads')}
  if meta.get('demo')!='0':raise ValueError('Synthetic data cannot enter this migrated-data profile')
  from .answer import title
  names={rid:list(dict.fromkeys(r['aliases']['th']+r['aliases']['en']+[title(r,'th'),title(r,'en')])) for rid,r in records.items()}
  refs={};index=[]
  for rid,r in records.items():
   for spec in CATALOG[r['kind']]['fields']:
    v=value(r,spec['key'])
    if v is not None:
     import json
     index.append({'id':rid+':'+spec['key'],'record_id':rid,'field':spec['key'],'text':json.dumps(v,ensure_ascii=False)})
     if spec['reference_kind']:
      for key in v if isinstance(v,list) else [v]:refs.setdefault(key,[]).append(rid)
  return {'active':'migration-preview-r69','epoch':int(meta['epoch']),'release':{'records':records,'sources':sources,'names':names,'reverse_refs':refs,'text_index':index},'withdrawn':withdrawn,'retired_names':{},'historical_names':{},'historical_kinds':historical,'allow_demo':False,'evaluation_draft_only':True,'migration_preview_only':True,'actual_active_release':meta.get('active','')}
 def still_current(self,snapshot):
  with self.store.connect() as c:row=c.execute("SELECT value FROM cc_meta WHERE key='epoch'").fetchone()
  return row is not None and int(row[0])==snapshot['epoch']
