import hashlib,re
def stable(s):
 v=re.sub('[^a-z0-9_:-]','_',s.lower())
 return v if len(v)<=100 else v[:78]+'_'+hashlib.sha256(s.encode()).hexdigest()[:20]
def sid(s):return re.sub('[^a-z0-9_]+','_',s.lower()).strip('_')
