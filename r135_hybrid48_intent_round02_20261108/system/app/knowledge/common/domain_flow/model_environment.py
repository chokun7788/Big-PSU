"""Selected local serving environment; never select or mutate model weights."""
import importlib.metadata,importlib.util,sys
from pathlib import Path

PYTHON=Path('D:/CodexTraining/psu-r121-20261022/venv/Scripts/python.exe')
PACKAGES={'torch':'2.7.1+cu128','transformers':'4.56.2','peft':'0.17.1',
          'bitsandbytes':'0.48.1','accelerate':'1.10.1','safetensors':'0.8.0'}

def inspect_environment():
    packages={};issues=[]
    for package,expected in PACKAGES.items():
        try:actual=importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:actual=None
        spec=importlib.util.find_spec(package)
        packages[package]={'version':actual,'expected':expected,'module_origin':spec.origin if spec else None}
        if actual!=expected or spec is None:issues.append('missing_or_different_package:'+package)
        elif not spec.origin or not Path(spec.origin).resolve().is_relative_to((PYTHON.parent.parent/'Lib/site-packages').resolve()):issues.append('package_outside_selected_environment:'+package)
    if sys.version_info[:2]!=(3,12):issues.append('python_abi_not_312')
    return {'selected_runtime_compatible':not issues,'python_executable':sys.executable,
            'python_version':sys.version,'packages':packages,'issues':issues,
            'model_loaded':False,'inference_performed':False,'weights_or_packages_modified':False}

def inspect_accelerator(observation):
    if not observation['selected_runtime_compatible']:return observation
    try:
        import torch,transformers,peft,bitsandbytes
        observation['cuda_available']=torch.cuda.is_available()
        observation['torch_cuda_version']=torch.version.cuda
        if not observation['cuda_available']:observation['issues'].append('selected_cuda_accelerator_unavailable')
        if torch.version.cuda!='12.8':observation['issues'].append('selected_torch_cuda_version_differs')
    except Exception as exc:observation['issues'].append('selected_runtime_import_failed:'+type(exc).__name__)
    observation['selected_runtime_compatible']=not observation['issues']
    return observation
