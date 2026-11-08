# หลักฐานวิจัยสำหรับ schema และการตอบข้อมูลศูนย์

## วิธีค้นและขอบเขตการอ่าน

โจทย์: owner-maintained structured knowledge สำหรับ task-oriented chatbot ที่ต้องเพิ่มข้อมูลใหม่ ตอบหลายหมวด/หลายเทิร์น/หลายภาษา และคงข้อเท็จจริง เวลา เงื่อนไข และความครบของคำตอบ

เลือกความลึกDeepตามคำขอ ไม่จำกัดปีและเสริมงาน2025–2026 แหล่งหลักคือACL Anthology, AAAI, arXiv, หน้าผู้วิจัย และเอกสารมาตรฐานทางการ ค้น4แกน: schema-guided dialogue/generalization; structured/relational retrieval; constrained plans/evidence/completeness; multilingual/provenance/validation

สกิลpaper-search-proไม่มีAPIconfiguration จึงหยุด automated federation และใช้webค้นเฉพาะแหล่งต้นฉบับต่อ รายงานนี้เป็นfocused technical research ไม่ใช่การค้นตามจำนวน180–400ของautomatedDeep ไม่ใช่systematicreviewและไม่มีcoverageestimate/RCS/dualreview ไม่อ้างว่าอ่านทุกหน้าทุกpaper บางงานอ่านabstract/metadataเพื่อเปรียบเทียบ ส่วนงานแกนหลักอ่านmethods/results/limitationsที่เกี่ยวข้องผ่านPDF/HTML

รายชื่อ23งานเป็นbibliographyที่คัดใช้ประกอบแบบ จำนวนไม่ใช่ตัวชี้ความครบ รายละเอียดระดับการอ่านอยู่ในpapers.json งานนอกโจทย์ที่เจอ เช่น URLACL2022.acl-long.386ซึ่งจริงเป็นFlooding-X ถูกตัดออกหลังตรวจชื่อ ไม่ใช่D3ST และไม่ถูกใช้สนับสนุนข้อเสนอ

## 1. Schema-guided dialogue: มีformatแล้วจะเพิ่มข้อมูลโดยไม่ดักชื่อได้อย่างไร

| งานต้นฉบับ | พบอะไรที่ใช้กับโจทย์นี้ | นำมาใช้ | ข้อจำกัด/สิ่งที่ยังต้องพิสูจน์ |
|---|---|---|---|
| [SGD — Rastogi et al., 2020](https://arxiv.org/abs/1909.05855) | ใช้intents/slotsแบบdynamicพร้อมdescriptionsเพื่อgeneralizeบริการ/APIใหม่ | registryfield/toolมีคำอธิบาย ไม่ผูกคำถามทุกแบบกับชื่อรายการ | เป็นdatasetและtrainedDST ผลzero-shotไม่รับรองบอท4Bของเรา |
| [D3ST — Zhao et al., 2022](https://arxiv.org/abs/2201.08904) | ใช้natural-language schema descriptionsและindexpicking; ตัวอย่างanalysisชี้meaninglessnamesทำให้generalizationแย่ และprefixยาวกระทบmodelบางsetting | fielddescriptionTH/EN+examplevalues, เลือกactivecategoriesก่อนprompt | ใช้T5finetuning ไม่ได้พิสูจน์ว่าแค่promptLLMปัจจุบันจะได้คะแนนเดียวกัน |
| [SGD-X — Lee et al., 2022](https://ojs.aaai.org/index.php/AAAI/article/view/21341) | schemaชื่อ/คำอธิบายที่paraphraseทำให้DSTไวต่อรูปแบบภาษา | holdoutdescriptionsและparaphrases ไม่ใช้aliaslistเป็นทั้งหมดของintent | benchmarkEnglish; ต้องตรวจไทยและชื่ออุปกรณ์ของเราเอง |
| [Grounding D3ST — Coca et al., 2023](https://aclanthology.org/2023.sigdial-1.42/) | knowledge-seekingturnsช่วยgroundความหมายของfieldsและเพิ่มrobustness; limitationsกล่าวถึงการเลือกturnsด้วยคน | เก็บตัวอย่างถาม/เติมslotที่ระดับfield/tool ไม่ต้องFAQทุกเกม | งานมีfinetuningและselectionstrategy; ไม่ได้เท่ากับownerfillJSONแล้วzeroerror |
| [Schema-Guided NLG — Du et al., 2020](https://aclanthology.org/2020.inlg-1.35/) | meaningrepresentationพร้อมrichschemaช่วยgenerationในหลายsetting | EvidenceBundleมีsemanticlabelsและdata-to-textrendererตามชนิด | อ่านabstract/metadata; ไม่ใช้เป็นหลักฐานผลเชิงตัวเลขในบอทเรา |

**ข้อเสนอจากการสังเคราะห์:** มีschemaข้อมูลเจ้าของและschemaQueryPlanคนละชั้น Descriptionsอธิบายความหมาย; stableIDsเก็บidentity; ตัวอย่างบทสนทนาสอนวิธีใช้fields การเพิ่มrecordใหม่ในkindเดิมจึงควรเป็นการเพิ่มข้อมูล ส่วนเพิ่มoperationหรือkindใหม่ยังต้องมีadapterที่ใช้ความหมายใหม่ได้

## 2. Structured knowledge + retrieval: เชื่อมข้อมูลแล้วตอบครบได้แค่ไหน

| งานต้นฉบับ | หลักการ/ผลที่เกี่ยวข้อง | ใช้กับศูนย์อย่างไร | ข้อจำกัด |
|---|---|---|---|
| [RAG — Lewis et al., 2020](https://arxiv.org/abs/2005.11401) | generationใช้retrievednon-parametricmemoryประกอบ | externalapprovedfacts+passages เปลี่ยนknowledgeผ่านrelease/index | ต้นฉบับใช้trainedretriever/generatorและWikipedia ไม่ใช่productionCRUDscheme |
| [RAT-SQL — Wang et al., 2020](https://aclanthology.org/2020.acl-main.677/) | relational schema encoding/linkingช่วยเชื่อมquestionกับdatabase | explicitgame/service/resource/audiencerelations; typedfilters | ไม่แนะนำเปิดfreeSQLเพียงเพราะมีpaper; executedSQLยังมีwrongconditionsได้ |
| [DialoKG — 2022](https://aclanthology.org/2022.findings-naacl.195/) | task-orientedgenerationใช้structuralrelationalknowledgeช่วยเลือกข้อมูล | evidenceของdialogueเก็บrelationที่ใช้จริง | อ่านabstract/metadata; architectureไม่ใช่drop-inสำหรับruntimeเดิม |
| [Task-oriented subgraph retrieval — Walker et al., 2025](https://aclanthology.org/2025.sigdial-1.42/) | ดึงconnectedsubgraphที่relevantและเล็กตามcontext; fixedtop-kอาจตัดตัวเชื่อม | boundedjoins/dependenciesของgame→service→resource/rate | dataset/userstudyเล็ก และuser-scorecomparisonบางส่วนไม่statisticallysignificant; ไม่อ้างว่าKGดีที่สุดทุกcase |
| [KG²RAG — Zhu et al., 2025](https://aclanthology.org/2025.naacl-long.449/) | semanticseed→KGexpansion→organizedchunks และทดสอบtripletdrop | entityfilteredretrievalแล้วดึงexception/relatedsectionที่จำเป็น | ทดลองบนHotpotQA ไม่ใช่การคำนวณเงินหรือtruthของpolicy |
| [MS-RAG — You et al., 2025](https://aclanthology.org/2025.emnlp-main.1151/) | รวมentity/relation/chunkindexes; graphextractionผิดทำnode/edgeหาย; vectorช่วยครอบส่วนที่กราฟขาด | owner-reviewedrelations+passagesคู่กัน ไม่ใช้LLMextractgraphเป็นแหล่งเดียว | retrievalbenchmarksกับLLMต่างจากเครื่องนี้ ไม่แปลงspeedgainเป็นเวลาบอทโดยไม่วัด |
| [GraphRAG — Edge et al., 2024](https://arxiv.org/abs/2404.16130) | communitysummariesช่วยglobalqueriesเหนือcorpusใหญ่มาก | พิจารณาภายหลังเมื่อมีglobaldocumentquestionsจริง | query-focusedglobalanalysisต่างจากlookupราคา/availability; เพิ่มindexingcalls/cost |
| [GraphFlow — Yu et al., 2025](https://arxiv.org/abs/2510.16582) | complexretrievalต้องใช้ทั้งrelationและtext/diversecandidates; ทดลองSTaRK | “ทั้งหมด”ต้องsetretrievalตามfilters+textfacets ไม่เดินpathเดียวแล้วหยุด | learnedretrievalpolicyเพิ่มความซับซ้อน; ใช้เป็นเหตุผลระวังgraph-onlyก่อน ไม่จำเป็นต้องtrainในระยะแรก |
| [CoRE — Gu et al., 2025](https://aclanthology.org/2025.findings-acl.1224/) | structuredtasksมีimplicitrelationsที่LLMใช้ไม่ดี; experience/contrastiveICLช่วยTableQA/Text-to-SQL | ตัวอย่างplanที่ถูกกับผิดและunit/conditionต่างกันเป็นholdoutreasoningtests | อ่านabstract; experienceaugmentationไม่ทดแทนtypedpricecalculator |
| [KERAG — 2025](https://aclanthology.org/2025.findings-emnlp.329/) | KGQAที่schemaเข้มยังมีlowcoverage/semanticambiguity จึงรวมstructuralและtextualknowledge | คงpassagesสำหรับexceptionsและunmodeledexplanations | อ่านabstract/metadata; ไม่ใช่เหตุผลให้fallbackgeneralworldknowledge |

**ข้อเสนอ:** เริ่มSQLiteFK/joinsกับhybridtext/entityretrieval ตามrelationsที่เจ้าของเลือกและตรวจได้ ไม่ต้องใช้Neo4j/RDF/GraphFlow/communitysummariesเพื่อให้มีdata-drivenruntimeได้ เก็บgraphconceptเป็นlogicalrelationsก่อน เพิ่มgraphalgorithmเมื่อfocusedbenchmarkแสดงประโยชน์ที่คุ้มlatency

## 3. การบังคับoutputกับการตรวจคำตอบเป็นคนละปัญหา

| งาน | สิ่งที่ช่วย | สิ่งที่ยังไม่รับประกัน |
|---|---|---|
| [PICARD — Scholak et al., 2021](https://aclanthology.org/2021.emnlp-main.779/) | incrementalparsingกันtokens/SQLstructureไม่ถูกต้อง รวมschemaidentifierchecks | validSQLอาจเลือกservice/audience/dateผิดความต้องการผู้ใช้ |
| [XGrammar — Dong et al., 2024/2025](https://arxiv.org/abs/2411.15100) | grammar/tokenmaskingทำstructuredgenerationมีoverheadต่ำในexperiment | JSONvalidไม่พิสูจน์sourceหรือmeaning; benchmarkGPUไม่ใช่hardwareเรา |
| [XGrammar 2 — Li et al., 2026](https://arxiv.org/abs/2601.04426) | dynamicstructured/toolformats, adaptivecaching และfunction-calltests | รุ่นpreprintที่อ่านv1; ต้องดูbackendintegrationจริงและทำownBFCL-likefocusedtests |
| [Lost in the Middle — Liu et al., 2024](https://aclanthology.org/2024.tacl-1.9/) | performanceขึ้นกับpositionของrelevantcontentและlongcontext | longcontextwindowไม่แปลว่าตอบทุกfieldครบ |
| [Evidentiality-guided generation — Asai et al., 2022](https://aclanthology.org/2022.naacl-main.162/) | retrievedpassageอาจไม่รองรับoutput การใช้evidentialityช่วยtrainedgeneration | อ่านabstract; citationที่มีURLไม่เท่ากับsupportจริง |
| [ALCE — Gao et al., 2023](https://aclanthology.org/2023.emnlp-main.398/) | แยกcorrectnessกับcitationrecall/precision ใช้claim-levelsupportและNLI | automaticjudgesยังมีข้อผิดพลาด ควรใช้exactvaluesสำหรับเงิน/เวลา/IDs |
| [RAGAs — Es et al., 2024](https://aclanthology.org/2024.eacl-demo.16/) | ประเมินretrieval/faithfulness/answerqualityแยกส่วน | LLM-basedscoreเป็นตัวช่วย ไม่แทนownertruthหรือtestoracleที่ยืนยัน |

**ข้อเสนอ:** LLMส่งQueryPlanที่ผ่านschema/semanticconstraints; executeด้วยtypedtools; finalizerเทียบfieldvalues/IDcount/obligationcoverage/source ทั้งก่อนและหลังgeneration สำหรับราคา/เวลา/ปุ่มใช้rendererที่รักษาค่าตรง ส่วนexplanationให้LLMเรียบเรียงด้วยclaimbinding การรับJSONสำเร็จต้องไม่ถูกนับเป็นตอบถูก

## 4. ภาษาและหลักฐานการตรวจข้อมูล

[MIRACL — Zhang et al., 2023](https://aclanthology.org/2023.tacl-1.63/) มี18ภาษาและไทยในretrievalbenchmark สนับสนุนการประเมินแยกภาษาร่วมกับlexical/dense/hybrid จุดที่ไม่ได้ทดสอบแทนเรา: slang/typosหลายตำแหน่ง, policytranslationและmulti-turnของศูนย์ ดังนั้นEnglishinputไม่ควรสร้างอีกknowledgebaseหนึ่ง ใช้IDs/machinevaluesเดียวและlocalizedtextที่bindrevision

เอกสารทางการ5รายการใช้สำหรับimplementation ไม่ใช่paperexperiment:

1. [JSON Schema Core2020-12](https://json-schema.org/draft/2020-12/json-schema-core): reusabletypedcontractsและapplicators
2. [JSON Schema Validation2020-12](https://json-schema.org/draft/2020-12/json-schema-validation): required/type/enums/ranges/format behavior ต้องเลือกvalidatorและเปิดformatchecksเอง
3. [PROV-O](https://www.w3.org/TR/prov-o/): entity/activity/agentเพื่ออธิบายการเกิดและที่มาของข้อมูล
4. [SHACL](https://www.w3.org/TR/shacl/): graphconstraintvalidationถ้าเลือกRDFในอนาคต; SQLitephaseแรกใช้applicationvalidator/FKได้
5. [Ollama Structured Outputs](https://docs.ollama.com/capabilities/structured-outputs): ใส่JSONschemaในformatfieldและใช้validation; ยังต้องทดสอบschema/model/backendจริง

## 5. Research gapและสิ่งที่ต้องวัดก่อนclaimผล

- ไม่มีpaperชุดนี้ที่ทดสอบschema24types/ownerpolicies/WordPressของPSU Esports Studio - Phuketโดยตรง
- Schema-generalizationบนEnglish/finetunedT5ไม่เท่ากับThai4Bprompt-only
- Correctretrievalไม่เท่ากับcompleteanswerหรือvalidcurrentprice; การตอบทั้งหมดต้องมีID/countoracle
- Structuredoutputไม่เท่ากับcorrectquery; sourcehashไม่เท่ากับclaimtruth
- Entitynamesใหม่และการถามต่อสั้นๆอาจยังเข้าใจผิด ต้องมีholdoutnewrecords/near-negative/contexttests
- Ownerข้อมูลครบบางfacetแต่ไม่ครบpolicyvalidity/exception; schemaช่วยเปิดให้เห็นmissingdata ไม่เติมความจริงให้เอง
- มากขึ้นทุกหมวดในpromptเดียวเสี่ยงcontextbudget/latency ใช้active-schemaselectionและboundedjoinsก่อน
- Schemaflexibilityมากเกินไปทำunknownkeys/opaqueJSONกลับมา Schemaแข็งเกินไปทำimportไม่ได้ จึงมีcorefields+unknown/draft+versionedextensionsที่ผ่านadaptergate

## 6. ข้อสรุปทางวิศวกรรม

แนวทางที่แนะนำคือ **typedcommonenvelope + kind-specificfields + stableIDs/relations + source/temporal/approvalmetadata + generictools + boundedLLM + coveragefinalizer** ข้อเสนอ24types/155fieldsอยู่ในคู่มือและschemas; milestoneแรกควรพิสูจน์การเพิ่มเกมชื่อใหม่ผ่านownerflowโดยไม่แก้code แล้วค่อยขยายไปหมวดราคาที่ผิดแล้วมีผลมากกว่า

ไม่เลือกfinetuningหรือgraphreasoninglearningเป็นงานแรก เพราะยังต้องแก้dataownership/relations/adaptersและsourcecompletenessก่อน หลังมีgenericpipelineแล้วจึงวัดparser/retrievalfailuresจริงว่าจำเป็นต้องtrainหรือเพิ่มmodelหรือไม่
