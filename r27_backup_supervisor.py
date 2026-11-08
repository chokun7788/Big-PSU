from r27_fixture import PROJECT,REPORT
for relative in ['app/web_api/pipeline_supervisor.py','deployment_templates/Start-PSU-Esports-Chatbot.ps1']:
    dst=REPORT/'before'/relative;dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('xb') as f:f.write((PROJECT/relative).read_bytes())
