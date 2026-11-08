"""Build exports for a manual fallback review; no fabricated bibliometrics."""
from pathlib import Path
import csv
import json
import re
import sys
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parent
papers = json.loads((OUT / "papers.json").read_text(encoding="utf-8"))
report = (OUT / "report.md").read_text(encoding="utf-8")
for paper in papers:
    match = re.search(r"^- \*\*" + paper["paper_id"] + r" [^\n]+", report, re.M)
    if match:
        paper["synopsis_th"] = match.group(0).lstrip("- ")
    paper["tldr"] = paper["applicability"]
(OUT / "papers.json").write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
fields = ["paper_id","title","year","venue","authors","url","doi","theme","manual_relevance","read_sections","applicability","citation_status"]
with (OUT / "papers.csv").open("w",encoding="utf-8-sig",newline="") as fp:
    writer=csv.DictWriter(fp,fieldnames=fields)
    writer.writeheader()
    for p in papers:
        writer.writerow({**{k:p.get(k,"") for k in fields},
                        "authors":"; ".join(p["authors_full"]),
                        "manual_relevance":p["rcs"]})
def bib_escape(value):
    return value.replace("\\","\\textbackslash{}").replace("&","\\&").replace("%","\\%").replace("_","\\_")
bib=[]
ris=[]
for p in papers:
    # @misc and RIS GEN intentionally avoid inventing missing pages or venue DOI.
    lines=["@misc{psu_"+p["paper_id"].lower()+","]
    entries={"title":p["title"],"author":" and ".join(p["authors_full"]),
             "year":str(p["year"]),"howpublished":p["venue"],"url":p["url"],
             "note":"Targeted review; see reading ledger for depth"}
    if p["doi"]:
        entries["doi"]=p["doi"]
    lines += ["  "+k+" = {"+bib_escape(v)+"}," for k,v in entries.items()]
    bib.append("\n".join(lines+["}"]))
    ris += ["TY  - GEN","ID  - "+p["paper_id"],"TI  - "+p["title"]]
    ris += ["AU  - "+a for a in p["authors_full"]]
    ris += ["PY  - "+str(p["year"]),"T2  - "+p["venue"],"UR  - "+p["url"]]
    if p["doi"]:
        ris.append("DO  - "+p["doi"])
    ris += ["N1  - "+p["applicability"],"ER  - ",""]
(OUT / "bibtex.bib").write_text("\n\n".join(bib)+"\n",encoding="utf-8")
(OUT / "ris.ris").write_text("\n".join(ris),encoding="utf-8")
metadata={
    "search_id":OUT.name,"generated_at":datetime.now(timezone.utc).isoformat(),
    "original_user_query":"ลองไป Search ใน Paper ดูว่าปัญหาพวกนี้ควรจะแก้ยังไงดี วิเคราะห์ปัญหากับการตอบต่างๆแล้วไปหา How to มา",
    "search_topic":"Local LLM serving and answer correctness",
    "display_title":"PSU Chatbot: Targeted Research on Serving and Answer Correctness",
    "language":"en","tier":"Targeted fallback (Setup blocked)",
    "papers_evaluated":len(papers),"papers_in_kg":len(papers),
    "stop_reason":"Selected mechanisms covered; saturation not estimated",
    "classification_method":"Manual local relevance; not automated skill classification",
    "coverage_estimate":None
}
(OUT / "metadata.json").write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding="utf-8")
(OUT / "paper_list.json").write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding="utf-8")
(OUT / "chart_data.json").write_text("{}",encoding="utf-8")
prisma={
    "workflow_status":"Manual fallback; not PRISMA compliant",
    "setup":"OpenAlex key and NCBI email unavailable; helper workflow halted",
    "scope":"19 primary papers; targeted mechanisms; Thai report and implementation Flow",
    "coverage":"Unavailable; no saturation estimate",
    "bibliometrics":"Not fetched; any zero shown by UI means missing",
    "classification":"Manual relevance 0–10; not a measured probability",
    "depth":"Relevant source excerpts; reading ledger in papers.json",
    "implementation":"No product source or previous logs modified; no new load test"
}
(OUT / "prisma_log.json").write_text(json.dumps(prisma,ensure_ascii=False,indent=2),encoding="utf-8")
sys.path.insert(0,r"C:\Users\Chokhun\.codex\skills\paper-search-pro")
from scripts.html_renderer_webartifacts import render_html_webartifacts
render_html_webartifacts(OUT,OUT/"report.html",language="en")
html=(OUT/"report.html").read_text(encoding="utf-8")
banner='''<aside style="padding:14px;background:#fff2ce;color:#182234;border-bottom:2px solid #d3ab43;font:15px/1.6 system-ui">
<strong>Targeted fallback review — 19 primary papers.</strong>
Helper setup is incomplete; this is not a completed Standard/systematic search.
Relevance scores are manual. Coverage and citation counts were not retrieved:
any zero displayed by the template is an unavailable-data placeholder.
Original abstracts are not reproduced. Thai analysis:
<a href="report.md">report.md</a> · <a href="FLOW_IMPLEMENTATION.md">Implementation Flow</a>.
No product code changes or new load tests in this research run.</aside>'''
html=re.sub(r"(<body[^>]*>)",lambda m:m.group(1)+banner,html,count=1)
(OUT/"report.html").write_text(html,encoding="utf-8")
validation={
    "papers":len(papers),"unique_ids":len({p["paper_id"] for p in papers}),
    "unique_urls":len({p["url"] for p in papers}),"bib_entries":len(bib),
    "ris_entries":sum(line=="TY  - GEN" for line in ris),
    "abstracts_reproduced":sum(bool(p["abstract"]) for p in papers),
    "html_payload_present":"window.__REPORT_DATA__" in html,
    "fallback_banner_present":"Targeted fallback review — 19" in html,
    "visual_browser_review":"not performed",
    "product_source_mutated":False
}
assert validation["papers"]==validation["unique_ids"]==validation["unique_urls"]==19
assert validation["bib_entries"]==validation["ris_entries"]==19
assert validation["html_payload_present"] and validation["fallback_banner_present"]
(OUT/"ARTIFACT_VALIDATION.json").write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(validation,ensure_ascii=False))
