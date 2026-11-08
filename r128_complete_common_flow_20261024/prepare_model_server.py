from pathlib import Path
import shutil
R=Path(__file__).resolve().parent;P=R.parent/'r124_legacy_guided_parity_20261023'
shutil.copy2(P/'context_contract.py',R/'context_contract.py')
s=(P/'serve_model.py').read_text('utf8')
s=s.replace("manifest={'pid':os.getpid()", "manifest={'serving_protocol':'r128-bounded-context-v1','pid':os.getpid()")
s=s.replace("   if context:wire=messages(user['original_question'])", """   if context:wire=messages(user['original_question'])
   # R121 adapter accepts a resolved question. Session facts never live in the weights.
   input_question=user['original_question'] if context else ''
   input_sha=hashlib.sha256(input_question.encode()).hexdigest() if context else None
   options=data.get('options') or {}
   requested_tokens=int(options.get('num_predict',512 if context else 640))
   max_tokens=max(1,min(requested_tokens,512 if context else 640))
   request_timeout=max(1.,min(float(data.get('request_timeout_sec',90)),180.))
   record.update(requested_tokens=requested_tokens,effective_max_new_tokens=max_tokens,request_timeout_sec=request_timeout,effective_input_sha256=input_sha,context_protocol=data.get('context_protocol','legacy-r121-resolved-question'))""")
# The inserted block must not split the existing if/else that selects the wire.
a=s.index("   # R121 adapter accepts");b=s.index("   else:\n    wire=[dict(m) for m in wire]",a)
block=s[a:b];s=s[:a]+s[b:];pos=s.index("   prompt=tok.apply_chat_template");s=s[:pos]+block+s[pos:]
s=s.replace("    inputs=tok(prompt", "    remaining=request_timeout-(time.monotonic()-before)\n    if remaining<=0:raise TimeoutError('model_request_expired_in_queue')\n    inputs=tok(prompt")
s=s.replace("max_new_tokens=850 if context else 640,do_sample=False", "max_new_tokens=max_tokens,max_time=remaining,do_sample=False")
s=s.replace("'quantization':'NF4','profile_digest':digests[profile]", "'quantization':'NF4','profile_digest':digests[profile],'serving_protocol':'r128-bounded-context-v1','effective_input_sha256':input_sha,'effective_max_new_tokens':max_tokens")
(R/'serve_model.py').write_text(s,'utf8')
import ast
ast.parse(s);print('Prepared bounded model transport; weights unchanged')
