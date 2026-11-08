"""Finite behavioral check for the optimized evaluator against production names."""
import sys,json,random,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B/'system'),str(B)]
from app.knowledge.common import answer as module
from harness import equivalent_name_pruning
original=module.named
names={'g1':['Overcooked'],'g2':['Cockpit'],'g3':['Starfish Quest'],'g4':['Novel game 8'],'r1':['PC #01'],'r2':['PC #02'],'th':['ดาวทะเลผจญภัย'],'th2':['สวัสดีทดสอบ']}
queries=['cooperative education','Overcookedly','Cockpits','PC #011 controls','PC #01 controls','Novel game 9 controls','Novel game 8 controls','cockpik ว่างไหม','Starfish Quesst controls','Starfish Quest controls','สวัสดีทดสอบ','ดาวทะเลผจญภยเล่นยังไง','PC #99','what games are offered?']
rng=random.Random(66)
for alias in [a for values in names.values() for a in values]:
 for _ in range(40):
  at=rng.randrange(len(alias));op=rng.randrange(4)
  v=alias[:at]+alias[at+1:] if op==0 else alias[:at]+alias[at]+alias[at:] if op==1 else alias[:at]+'k'+alias[at+1:] if op==2 else alias[:at]+alias[at:at+2][::-1]+alias[at+2:]
  queries.extend([v+' controls','xx'+v+'zz'])
expected=[original(q,names) for q in queries];equivalent_name_pruning();mismatches=[]
for q,want in zip(queries,expected):
 actual=module.named(q,names)
 if actual!=want:mismatches.append({'question':q,'production':want,'evaluator':actual})
out=B/('EVALUATOR_EQUIVALENCE_'+str(len(list(B.glob('EVALUATOR_EQUIVALENCE_*.json')))+1)+'.json');out.write_text(json.dumps({'questions':len(queries),'harness_sha256':hashlib.sha256((B/'harness.py').read_bytes()).hexdigest(),'mismatches':mismatches,'scope':'finite behavioral comparison, not a proof of every string'},ensure_ascii=False,indent=2),encoding='utf-8');print(out,len(mismatches));raise SystemExit(bool(mismatches))
