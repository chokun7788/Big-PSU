import json,sys,platform
from pathlib import Path
R=Path(__file__).resolve().parent
import torch,transformers,peft,bitsandbytes,accelerate
assert torch.cuda.is_available(),'CUDA training runtime unavailable'
from bitsandbytes.nn import Linear4bit
layer=Linear4bit(32,32,bias=False,compute_dtype=torch.bfloat16,quant_type='nf4').to('cuda')
x=torch.randn(2,32,device='cuda',dtype=torch.bfloat16,requires_grad=True)
loss=layer(x).float().square().mean();loss.backward();assert torch.isfinite(x.grad).all() and x.grad.abs().sum()>0
out={'cuda_available':True,'nf4_forward_backward_passed':True,'gpu':torch.cuda.get_device_name(0),'capability':torch.cuda.get_device_capability(),
 'cuda_runtime':torch.version.cuda,'python':platform.python_version(),'packages':{m.__name__:m.__version__ for m in [torch,transformers,peft,bitsandbytes,accelerate]},
 'vram_free_total':torch.cuda.mem_get_info(),'allocated_bytes':torch.cuda.memory_allocated(),'actual_model_training_started':False}
(R/'CUDA_PREFLIGHT.json').write_text(json.dumps(out,indent=2),'utf8');print(json.dumps(out,indent=2))
