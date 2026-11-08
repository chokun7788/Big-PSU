from pathlib import Path


project = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
old = "2026.09.26-owner-review-candidate"
new = "2026.09.26-owner-review-candidate-r2"
for relative in (
    "deployment_templates/Start-PSU-Esports-Chatbot.ps1",
    "deployment_templates/README_TH.md",
    "tools/build_owner_local_package.ps1",
):
    path = project / relative
    content = path.read_text(encoding="utf-8")
    if content.count(old) != 1:
        raise RuntimeError(f"Expected one version in {path}; got {content.count(old)}")
    path.write_text(content.replace(old, new), encoding="utf-8")
print(f"Set package version to {new}")
