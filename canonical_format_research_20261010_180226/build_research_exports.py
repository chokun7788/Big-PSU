from pathlib import Path
import json,csv,html,hashlib
OUT=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
# Titles/years/primary links verified through the web research. These are curated
# metadata, not raw federation output or an RCS-ranked search result.
ROWS=[
 ('sgd','Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset',2020,'https://arxiv.org/abs/1909.05855','schema_dialogue','selected_full_text_sections'),
 ('d3st','Description-Driven Task-Oriented Dialog Modeling',2022,'https://arxiv.org/abs/2201.08904','schema_dialogue','selected_full_text_sections'),
 ('sgdx','SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems',2022,'https://ojs.aaai.org/index.php/AAAI/article/view/21341','schema_dialogue','abstract_metadata'),
 ('grounding_d3st','Grounding Description-Driven Dialogue State Trackers with Knowledge-Seeking Turns',2023,'https://aclanthology.org/2023.sigdial-1.42/','schema_dialogue','selected_full_text_sections'),
 ('sgnlg','Schema-Guided Natural Language Generation',2020,'https://aclanthology.org/2020.inlg-1.35/','schema_dialogue','abstract_metadata'),
 ('rag','Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks',2020,'https://arxiv.org/abs/2005.11401','retrieval','abstract_metadata'),
 ('ratsql','RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers',2020,'https://aclanthology.org/2020.acl-main.677/','structured_retrieval','abstract_metadata'),
 ('dialogkg','DialoKG: Knowledge-Structure Aware Task-Oriented Dialogue Generation',2022,'https://aclanthology.org/2022.findings-naacl.195/','structured_retrieval','abstract_metadata'),
 ('subgraphs','Retrieving Relevant Knowledge Subgraphs for Task-Oriented Dialogue',2025,'https://aclanthology.org/2025.sigdial-1.42/','structured_retrieval','selected_full_text_sections'),
 ('kg2rag','Knowledge Graph-Guided Retrieval Augmented Generation',2025,'https://aclanthology.org/2025.naacl-long.449/','structured_retrieval','selected_full_text_sections'),
 ('msrag','MS-RAG: Simple and Effective Multi-Semantic Retrieval-Augmented Generation',2025,'https://aclanthology.org/2025.emnlp-main.1151/','structured_retrieval','selected_full_text_sections'),
 ('graphrag','From Local to Global: A GraphRAG Approach to Query-Focused Summarization',2024,'https://arxiv.org/abs/2404.16130','structured_retrieval','selected_full_text_sections'),
 ('graphflow','Can Knowledge-Graph-based Retrieval Augmented Generation Really Retrieve What You Need?',2025,'https://arxiv.org/abs/2510.16582','structured_retrieval','selected_full_text_sections'),
 ('core','Toward Structured Knowledge Reasoning: Contrastive Retrieval-Augmented Generation on Experience',2025,'https://aclanthology.org/2025.findings-acl.1224/','structured_retrieval','abstract_metadata'),
 ('kerag','KERAG: Knowledge-Enhanced Retrieval-Augmented Generation for Advanced Question Answering',2025,'https://aclanthology.org/2025.findings-emnlp.329/','structured_retrieval','abstract_metadata'),
 ('picard','PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models',2021,'https://aclanthology.org/2021.emnlp-main.779/','constrained_output','selected_full_text_sections'),
 ('xgrammar','XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models',2024,'https://arxiv.org/abs/2411.15100','constrained_output','selected_full_text_sections'),
 ('xgrammar2','XGrammar-2: Dynamic and Efficient Structured Generation Engine for Agentic LLMs',2026,'https://arxiv.org/abs/2601.04426','constrained_output','selected_full_text_sections_v1'),
 ('lost','Lost in the Middle: How Language Models Use Long Contexts',2024,'https://aclanthology.org/2024.tacl-1.9/','context','abstract_metadata'),
 ('evidentiality','Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks',2022,'https://aclanthology.org/2022.naacl-main.162/','evidence','abstract_metadata'),
 ('alce','Enabling Large Language Models to Generate Text with Citations',2023,'https://aclanthology.org/2023.emnlp-main.398/','evidence','selected_full_text_sections'),
 ('ragas','RAGAs: Automated Evaluation of Retrieval Augmented Generation',2024,'https://aclanthology.org/2024.eacl-demo.16/','evaluation','abstract_and_full_text_introduction'),
 ('miracl','MIRACL: A Multilingual Retrieval Dataset Covering 18 Diverse Languages',2023,'https://aclanthology.org/2023.tacl-1.63/','multilingual','abstract_metadata')]
papers=[dict(zip(('key','title','year','url','theme','reading_level'),r),rcs=None,citation_count=None) for r in ROWS]
(OUT/'papers.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding='utf-8')
with (OUT/'papers.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(papers[0]));w.writeheader();w.writerows(papers)
(OUT/'papers.bib').write_text('\n\n'.join('@misc{'+p['key']+',\n  title = {'+p['title']+'},\n  year = {'+str(p['year'])+'},\n  url = {'+p['url']+'}\n}' for p in papers)+'\n',encoding='utf-8')
(OUT/'papers.ris').write_text('\n'.join('TY  - GEN\nTI  - '+p['title']+'\nPY  - '+str(p['year'])+'\nUR  - '+p['url']+'\nER  - \n' for p in papers),encoding='utf-8')
plan={'search_topic':'Schema-guided owner-maintained structured knowledge for grounded task-oriented dialogue','display_title':'Schema-Guided Knowledge Maintenance for Grounded Service Dialogue','requested_depth':'deep','executed_mode':'focused_manual_primary_source_web_fallback','search_language':'English scholarly literature; Thai design deliverables','year_min':None,'year_max':2026,'concept_strategies':[
 {'query':'("schema-guided" OR "description-driven") AND (dialogue OR dialog) AND (generalization OR robustness)'},
 {'query':'("structured knowledge" OR "knowledge graph" OR relational) AND (retrieval OR "task-oriented dialogue")'},
 {'query':'("structured generation" OR "constrained decoding") AND (schema OR "tool calling")'},
 {'query':'("retrieval augmented generation") AND (citations OR completeness OR evidentiality)'},
 {'query':'(multilingual OR Thai) AND (retrieval OR "dialogue state tracking")'}],
 'web_queries_executed_examples':['site.aclanthology.org schema guided dialogue dataset 2020 unseen services','site.aclanthology.org description driven task oriented dialogue modeling D3ST','site.aclanthology.org retrieval augmented generation tables structured knowledge dialogue','site.aclanthology.org "PICARD" constrained decoding SQL','site.aclanthology.org "Enabling Large Language Models to Generate Text with Citations"','site.aclanthology.org "RAGAs" automated evaluation retrieval','site.arxiv.org "Lost in the Middle" long contexts','site.aclanthology.org Thai multilingual dense retrieval MIRACL benchmark','site.aclanthology.org "RAT-SQL: Relation-Aware Schema Encoding"','site.arxiv.org "XGrammar" flexible efficient structured generation engine','site.aclanthology.org "Knowledge Graphs" "Retrieval-Augmented Generation" survey 2025'],
 'inclusion':'Primary studies relevant to schema/dialogue, relational retrieval, constrained plans, evidence, multilingual retrieval; official standards for engineering','exclusion':'Unrelated robustness papers, secondary summaries as claim support, general chat use cases, unverified performance extrapolation'}
(OUT/'query_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
log={'date_local':'2026-10-10','timezone':'Asia/Bangkok','skill':'paper-search-pro','skill_pipeline_status':'halted_at_setup_missing_keys','key_presence':{'openalex':False,'semantic_scholar':False,'ncbi':False,'crossref':False},'fallback':'web search and direct primary source reading plus read-only local audit','retained_bibliography_count':len(papers),'coverage_estimate':None,'rcs_scores':None,'citation_rank':None,'not_systematic_review':True,
 'automated_steps_not_run':['OpenAlex multi-sort/seminal/reviews','arXiv/OpenReview bulk helpers','federated KG resolver','parallel RCS classifier agents','saturation curve and citation expansion','SS/CrossRef enrichment','Shadcn materialization renderer','PRISMA-S automated logger'],
 'loss':'No automated multi-index recall, bibliometric enrichment, measured search saturation or standard skill HTML/PRISMA-S workflow. The curated bibliography does not imply field completeness.',
 'recovery':'Configure paper-search-pro via references/setup.md then rerun federation/screening/enrichment; compare novel evidence with current design. Do not paste API secrets into the chat.',
 'not_needed':['PubMed medical scope absent','Chinese databases not requested','journal quartile filter not requested','external database Boolean export not required for implementation decision'],
 'local_validation':'45 research prototype checks; no full chatbot test or integration/deployment','original_project_writes':False,'report_renderer':'custom offline HTML fallback; not the skill Shadcn renderer'}
(OUT/'execution_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
summary='''แนะนำฟอร์มเจ้าของแยกหมวดที่บันทึกลงข้อมูลกลางแบบมีชนิดและstableIDs/relations พร้อมsource, validity, approvalและtranslationrevision จากนั้นให้เครื่องมืออ่าน/คำนวณค่าจริงและให้LLMตีความคำถามและเรียบเรียงเฉพาะหลักฐาน งานSGD/D3STสนับสนุนschema descriptions; SGD-Xชี้schema sensitivity; MS-RAGชี้ปัญหาgraph extractionและประโยชน์ของข้อมูลหลายระดับ; ALCEช่วยแยกความถูกต้องกับcitation support

แบบที่จัดเตรียมมี24record types/155fields ครอบคลุมหมวดเดิม มี24drafttemplatesและ6ตัวอย่างจากข้อมูลจริง ตัวตรวจต้นแบบผ่าน45checks แต่ยังไม่เชื่อมกับเว็บจริง ไม่ได้อ้างว่าformatเพียงอย่างเดียวแก้คำถามทุกแบบได้ ขั้นแรกควรพิสูจน์เพิ่มเกมชื่อใหม่แล้วgenericruntimeอ่านได้โดยไม่patchชื่อเกม

ค้นงานต้นฉบับและจัดbibliography23งานพร้อม5เอกสารมาตรฐาน ระดับอ่านแยกในpapers.json ใช้เว็บแทนpipelinepaper-search-proเพราะไม่มีAPIconfiguration ไม่มีRCS/coverageestimateหรือsystematicreviewclaim ไฟล์ข้อมูลที่audit488ไฟล์มีhashสำหรับตรวจการรักษาต้นฉบับ
'''
(OUT/'summary.md').write_text(summary,encoding='utf-8')
# Offline browsable summary. It deliberately does not claim to be the skill's renderer.
cards=''.join('<tr><td>'+str(p['year'])+'</td><td><a href="'+html.escape(p['url'],quote=True)+'">'+html.escape(p['title'])+'</a></td><td>'+html.escape(p['theme'])+'</td><td>'+html.escape(p['reading_level'])+'</td></tr>' for p in papers)
links=''.join('<li><a href="'+name+'">'+label+'</a></li>' for name,label in [('FORMAT_AND_FLOW_COMPLETE_TH.md','คู่มือและFlowฉบับสมบูรณ์'),('OWNER_FIELD_GUIDE_TH.md','รายละเอียด155ช่องที่เจ้าของกรอก'),('FLOW_IMPLEMENTATION_TH.md','ลำดับพัฒนาและGate'),('RESEARCH_EVIDENCE_TH.md','วิเคราะห์งานวิจัยและข้อจำกัด'),('examples/actual_source_drafts.bundle.json','ตัวอย่าง6Draftจากข้อมูลจริง'),('FIELD_CATALOG.json','Fieldcatalog'),('VALIDATION_RESULTS.json','ผลตรวจต้นแบบ45เคส'),('execution_log.json','ขอบเขตการค้นและขั้นตอนที่ไม่ได้รัน'),('papers.csv','BibliographyCSV'),('papers.bib','BibTeX'),('papers.ris','RIS')])
page='''<!doctype html><html lang="th"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PSU Esports — Canonical Format Research</title><style>body{font:16px/1.65 system-ui,sans-serif;background:#f6f8fc;color:#18304f;margin:auto;max-width:1180px;padding:32px}h1{font-size:30px}h2{margin-top:36px}a{color:#124f99}section{background:white;padding:24px;border-radius:12px;margin:20px 0;border:1px solid #dbe3ef}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;vertical-align:top;padding:10px;border-bottom:1px solid #dbe3ef}input{padding:12px;width:min(600px,95%);font-size:16px}.notice{background:#fff5d8;padding:16px;border-radius:8px}code{background:#edf2fa;padding:2px 4px}li{margin:8px 0}</style><h1>Format กลางสำหรับข้อมูลเจ้าของศูนย์</h1><p>PSU Esports Studio - Phuket · Research/design · 10 October 2026</p><div class="notice">ยังไม่ได้เชื่อมruntimeจริง · สกิลไม่มีAPIconfigurationจึงใช้เว็บค้นต้นฉบับต่อ · ไม่มีRCS/coverageestimate</div><section><h2>ข้อเสนอ</h2><p>ฟอร์มเจ้าของ → typedrecords + stableIDs/relations → source/validity/review → release → genericlookup/calculators + hybridretrieval → boundedLLM + coveragefinalizer</p><p>24record types · 155fields · 6ตัวอย่างจริงแบบDraft · 45/45prototypechecks</p><ul>'''+links+'''</ul></section><section><h2>Bibliographyที่คัดใช้ (23งาน)</h2><p>Selected sectionsและabstractแยกกัน; จำนวนไม่ใช่หลักฐานว่าค้นครบ</p><input id="search" placeholder="ค้นชื่อ/หัวข้อ/ปี"><table><thead><tr><th>ปี</th><th>Paperต้นฉบับ</th><th>หมวด</th><th>ระดับการอ่าน</th></tr></thead><tbody>'''+cards+'''</tbody></table></section><script>document.querySelector('#search').addEventListener('input',e=>{let q=e.target.value.toLowerCase();document.querySelectorAll('tbody tr').forEach(r=>r.hidden=!r.textContent.toLowerCase().includes(q));});</script></html>'''
(OUT/'report.html').write_text(page,encoding='utf-8')
before=json.loads((OUT/'SOURCE_HASHES_BEFORE.json').read_text(encoding='utf-8'))
changed=[]
for item in before:
 p=ROOT/item['path']
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:changed.append(item['path'])
result={'scope':'488 audited JSON/JSONL data and dashboard configuration files. No project mutation commands were used. Logs and other excluded files were not independently hashed.','checked':len(before),'changed_or_missing':changed,'unchanged':not changed}
(OUT/'SOURCE_PRESERVATION_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'bibliography':len(papers),'source_preservation':result},ensure_ascii=False))
