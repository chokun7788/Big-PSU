"""Candidate-only generation transport migration; original measurements untouched."""
from pathlib import Path
R=Path(__file__).resolve().parent
stages={'experimental_fallback':'general_answer','facts_composer':'facts_composition','llm_tool_router':'tool_selection','universal_intent':'intent_understanding','shadow_critic':'shadow_review','llm_health':'preflight'}
for name,stage in stages.items():
 p=R/'system/app/pipeline'/f'{name}.py';s=p.read_text(encoding='utf8')
 marker='from __future__ import annotations\n'
 if 'gateway_open =' not in s:
  assert marker in s,name
  s=s.replace(marker,marker+"from app.knowledge.common.domain_flow.model_gateway import legacy_open as _gateway_open\nfrom functools import partial as _gateway_partial\ngateway_open = _gateway_partial(_gateway_open,stage="+repr(stage)+")\n",1)
  assert 'urllib.request.urlopen(request,' in s,name
  s=s.replace('urllib.request.urlopen(request,','gateway_open(request,')
  p.write_text(s,encoding='utf8')
