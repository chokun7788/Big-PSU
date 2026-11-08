"""Materialize manually screened primary-source references. No network calls."""
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent

ROWS = [
    ('P01','Description-Driven Task-Oriented Dialog Modeling',2022,'arXiv','Jeffrey Zhao','https://arxiv.org/html/2201.08904v1','10.48550/arXiv.2201.08904','schema descriptions, indexed intent/slot selection','methodology and abstract'),
    ('P02','Show, Don’t Tell: Demonstrations Outperform Descriptions for Schema-Guided Task-Oriented Dialogue',2022,'NAACL','Raghav Gupta','https://aclanthology.org/2022.naacl-main.336/','10.18653/v1/2022.naacl-main.336','schema demonstrations and dialogue state','abstract and publication metadata'),
    ('P03','RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers',2020,'ACL','Bailin Wang','https://aclanthology.org/2020.acl-main.677/','10.18653/v1/2020.acl-main.677','schema linking and relation encoding','abstract and publication metadata'),
    ('P04','PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models',2021,'EMNLP','Torsten Scholak','https://aclanthology.org/2021.emnlp-main.779/','10.18653/v1/2021.emnlp-main.779','formal output constraints; syntax versus semantics','abstract and introduction excerpt'),
    ('P05','Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions',2023,'ACL','Harsh Trivedi','https://aclanthology.org/2023.acl-long.557/','10.18653/v1/2023.acl-long.557','dependent retrieval for multi-step questions','abstract and introduction excerpt'),
    ('P06','Sufficient Context: A New Lens on Retrieval Augmented Generation Systems',2025,'ICLR','Hailey Joren','https://arxiv.org/html/2411.06037v3','10.48550/arXiv.2411.06037','context sufficiency, selective generation, false abstention','definition, methods, experimental discussion; author repository confirms ICLR 2025'),
    ('P07','Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs',2025,'Findings of NAACL','Michael JQ Zhang','https://aclanthology.org/2025.findings-naacl.306/','10.18653/v1/2025.findings-naacl.306','material ambiguity and clarification utility','abstract and publication metadata'),
    ('P08','RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation',2024,'NeurIPS Datasets and Benchmarks','Dongyu Ru','https://arxiv.org/html/2408.08067v1','10.48550/arXiv.2408.08067','claim-level retrieval/generation diagnosis','metrics, experimental findings, Appendix H limitations; author repository confirms venue'),
    ('P09','Beyond Accuracy: Behavioral Testing of NLP Models with CheckList',2020,'ACL','Marco Tulio Ribeiro','https://aclanthology.org/2020.acl-main.442/','10.18653/v1/2020.acl-main.442','minimum functionality, invariance, directional tests','abstract and test-method excerpt'),
    ('P10','Semantic Answer Similarity for Evaluating Question Answering Models',2021,'MRQA','Julian Risch','https://aclanthology.org/2021.mrqa-1.15/','10.18653/v1/2021.mrqa-1.15','lexical versus semantic evaluation','abstract and publication metadata'),
    ('P11','FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation',2024,'Findings of ACL','Tu Vu','https://aclanthology.org/2024.findings-acl.813/','10.18653/v1/2024.findings-acl.813','time-sensitive facts and false premises','abstract and introduction/evaluation excerpt'),
    ('P12','Lost in the Middle: How Language Models Use Long Contexts',2024,'TACL','Nelson F. Liu','https://aclanthology.org/2024.tacl-1.9/','10.1162/tacl_a_00638','context position and length sensitivity','abstract and publication metadata'),
    ('P13','M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation',2024,'Findings of ACL','Jianlv Chen','https://aclanthology.org/2024.findings-acl.137/','10.18653/v1/2024.findings-acl.137','multilingual dense/sparse/multi-vector retrieval','abstract and contribution excerpt'),
    ('P14','Corrective Retrieval Augmented Generation',2024,'arXiv','Shi-Qi Yan','https://arxiv.org/html/2401.15884v3','10.48550/arXiv.2401.15884','retrieval-quality evaluation and corrective actions','abstract; HTML accessed, not a full-method reproduction'),
    ('P15','Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection',2024,'ICLR','Akari Asai','https://arxiv.org/abs/2310.11511','10.48550/arXiv.2310.11511','trained reflection and on-demand retrieval','abstract and ICLR paper section 3 excerpt'),
]

QUERIES = [
    'schema guided dialogue state tracking D3ST description driven dialogue state tracking paper',
    'PICARD parsing incrementally constrained auto regressive decoding text to SQL EMNLP 2021',
    'Sufficient Context A New Lens on Retrieval Augmented Generation Systems paper',
    'RAGChecker fine grained diagnosis retrieval augmented generation paper',
    'site.aclanthology.org "Description-Driven Task-Oriented Dialog Modeling"',
    'site.aclanthology.org "Show, Don’t Tell" "Schema"',
    'site.aclanthology.org "Beyond Accuracy" "CheckList"',
    'site.aclanthology.org "Interleaving Retrieval" "Chain-of-Thought"',
    '"Description-Driven Task-Oriented Dialog Modeling" Zhao 2022 ACL',
    '"Show, Don’t Tell: Demonstrations Outperform Descriptions" schema dialogue',
    '"RAT-SQL" relation aware schema encoding ACL 2020',
    '"Lost in the Middle" long contexts TACL 2024',
    'Corrective Retrieval Augmented Generation CRAG 2401.15884',
    'Self-RAG Learning to Retrieve Generate Critique Self Reflection 2024',
    'FreshLLMs Refreshing Large Language Models Search Engine Augmentation FreshQA',
    'When to Ask for Clarification Conversational Search 2020',
    'BGE M3 Embedding Multi Lingual Multi Functionality Multi Granularity arxiv 2024',
    'MIRACL multilingual retrieval 18 languages Thai 2023',
    'Evaluating Question Answering Evaluation Transformers semantic similarity exact match 2021',
    'Benchmarking Large Language Models in Retrieval Augmented Generation RGB 2023 2024',
]

papers = [dict(zip(['id','title','year','venue','first_author','url','doi','relevance','reading_depth'],r)) for r in ROWS]
log = {
    'date_local':'2026-10-19','timezone':'Asia/Bangkok',
    'purpose':'Research for a schema-based studio chatbot repair plan, linked to retained failure logs',
    'method':'targeted primary-source web search; not completed paper-search-pro tier workflow',
    'skill_setup':{'openalex_api_key_present':False,'ncbi_email_present':False,'helper_workflow_halted':True},
    'query_plan':{'year_filter':None,'language_space':'English research; Thai synthesis','queries':QUERIES},
    'sources_used':['ACL Anthology','arXiv','author research repositories','OpenReview paper PDF excerpt'],
    'excluded_as_evidence':['Reddit and blogs','unverified secondhand claims','retrieved but not selected papers'],
    'selection':'relevance to schema/task linking, evidence sufficiency, multi-need execution, abstention, evaluation, time-sensitive facts',
    'selected_unique_papers':len(papers),'papers':papers,
    'search_limitations':[
        'No exhaustive database search, PRISMA, citation saturation estimate or numeric literature coverage claim',
        'No full-text reading of every selected paper; reading depth recorded per paper',
        'OpenReview forum request for Self-RAG returned HTTP 429; arXiv abstract and earlier primary PDF excerpt were available',
        'No automatic classifier, citation-count ranking, journal metrics or skill HTML/BibTeX/RIS pipeline run',
        'BibTeX below is a manually screened reference export, with first author and others, not a full bibliographic metadata crawl',
        'No claim of applicability gains on Thai/Typhoon 4B without future experiments',
    ],
    'runtime_changed':False,'chatbot_tests_run':0,'model_calls_made_by_analysis':0,
}
(OUT/'LITERATURE_AND_SEARCH_LOG.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
bib=[]
for p in papers:
    bib.append('@misc{r96'+p['id']+',\n  title = {'+p['title']+'},\n  author = {'+p['first_author']+' and others},\n  year = {'+str(p['year'])+'},\n  howpublished = {'+p['venue']+'},\n  doi = {'+p['doi']+'},\n  url = {'+p['url']+'}\n}')
(OUT/'papers.bib').write_text('\n\n'.join(bib)+'\n',encoding='utf-8')
print(json.dumps({'papers':len(papers),'queries':len(QUERIES)}))
