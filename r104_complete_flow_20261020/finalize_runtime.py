"""Finish deployment/readiness interfaces before the single integrated batch."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent;C=R/'system/app/knowledge/common'
def edit(p,old,new):
 t=p.read_text('utf8')
 if t.count(old)!=1:raise ValueError((p.name,old[:55],t.count(old)))
 p.write_text(t.replace(old,new),'utf8')
p=C/'schemas/claim_binding.ui.json';s=json.loads(p.read_text('utf8'));s['properties']['actor_scope']['properties']['value']['x-reference-kind']='audience';p.write_text(json.dumps(s,ensure_ascii=False,indent=2),'utf8')
edit(C/'task_registry.py'," return {'version':VERSION,'kind':kind", " from .claim_bindings import references\n mapping_readiness=[]\n for b in record.get('claim_bindings',[]):\n  missing=[k for k in ('conditions_status','exceptions_status') if b.get(k)!='known']\n  if b['actor_scope']['status']!='known':missing.append('actor_scope')\n  if b['applicability']['status']!='known':missing.append('applicability')\n  missing.extend('reference:'+k for k in references({**record,'claim_bindings':[b]}) if k not in scope)\n  mapping_readiness.append({'binding_id':b['binding_id'],'status':'needs_data' if missing else 'data_ready','missing':missing,'approval_created':False})\n return {'claim_mapping_readiness':mapping_readiness,'version':VERSION,'kind':kind")
edit(C/'migrated_view.py',"PUBLISHED_PROFILE='common-r101-published'", "PUBLISHED_PROFILE='common-r102-published'")
p=C/'build_info.py';t=p.read_text('utf8').replace('common-r101-shared-graph-flow','common-r102-complete-contract-flow');p.write_text(t,'utf8')
src=(R/'Start-R101.ps1').read_text('utf8').replace('common-r101-published','common-r102-published').replace('R101','R102').replace('8122','8132').replace('8121','8131');(R/'Start-R102.ps1').write_text(src,'utf8')
for mode in ['Preview','Published','Owner']:
 (R/f'Open-{mode}.cmd').write_text('@echo off\r\npowershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-R102.ps1" -Mode '+mode+'\r\npause\r\n','utf8')
p=R/'system/app/web_api/server.py';t=p.read_text('utf8');old="                log_record['delivery_status'] = 'server_written'";assert t.count(old)==1;t=t.replace(old,old+"\n                log_record['common_flow_delivery'] = {'stage':'S17_delivery','status':'server_written','visible_to_user_verified':False}");p.write_text(t,'utf8')
# Keep public draft/published labels tied to the actual returned profile.
p=R/'system/web_chat/index.html';t=p.read_text('utf8').replace('R101','R102');p.write_text(t,'utf8')
print('Readiness, release profile, launchers and actual delivery audit finished')
