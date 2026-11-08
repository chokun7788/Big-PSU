import argparse,json,sqlite3,zlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('key_prefix');p.add_argument('--arm',default='');a=p.parse_args()
c=sqlite3.connect((Path(__file__).parent/'evidence.sqlite').as_uri()+'?mode=ro',uri=True)
for arm,key,raw in c.execute('SELECT arm,key,raw FROM results WHERE key LIKE ? AND (?="" OR arm=?)',(a.key_prefix+'%',a.arm,a.arm)):
 print(arm,key);print(json.dumps(json.loads(zlib.decompress(raw)),ensure_ascii=False,indent=2))
