import collections,hashlib,json,os,statistics
from pathlib import Path
R=Path(__file__).resolve().parent
os.environ.update(HF_HUB_OFFLINE='1',HF_HUB_DISABLE_TELEMETRY='1',TOKENIZERS_PARALLELISM='false')
from transformers import AutoTokenizer
TOKENIZER=Path('D:/CodexTraining/psu-r121-20261022/model')
tok=AutoTokenizer.from_pretrained(TOKENIZER,local_files_only=True,trust_remote_code=False)
out={};stats={}
for split in ['train','validation','test']:
 xs=list(map(json.loads,(R/(split+'.jsonl')).open(encoding='utf8')));packed=[]
 for x in xs:
  prompt=tok.apply_chat_template(x['messages'][:-1],tokenize=False,add_generation_prompt=True,enable_thinking=False)
  full=tok.apply_chat_template(x['messages'],tokenize=False,add_generation_prompt=False,enable_thinking=False)
  assert full.startswith(prompt),('template_prompt_mismatch',x['key'])
  p=tok(prompt,add_special_tokens=False)['input_ids'];ids=tok(full,add_special_tokens=False)['input_ids']
  assert ids[:len(p)]==p and len(ids)>len(p)
  packed.append({'key':x['key'],'input_ids':ids,'prompt_len':len(p),'completion_len':len(ids)-len(p)})
 lengths=[len(x['input_ids']) for x in packed];completions=[x['completion_len'] for x in packed]
 stats[split]={'rows':len(xs),'min':min(lengths),'max':max(lengths),'median':statistics.median(lengths),'completion_max':max(completions),'truncated':0}
 (R/('TOKENIZED_'+split+'.json')).write_text(json.dumps(packed,separators=(',',':')),'utf8')
 out[split]=packed
(R/'TOKEN_STATS.json').write_text(json.dumps(stats,indent=2),'utf8')
assert max(s['max'] for s in stats.values())<=2048,'Review prompt and full examples; never silently truncate targets'
print(json.dumps(stats,indent=2))
