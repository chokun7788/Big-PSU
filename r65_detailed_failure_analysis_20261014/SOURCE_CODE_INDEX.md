# Source codeที่ใช้ยืนยันสาเหตุ

ลิงก์ไปsnapshotR64ที่ทดสอบจริง; lineเป็นจุดเริ่มอ่าน ตรวจSHAเมื่อเทียบกับproductionหรือpackage

- [runtime NameError](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/retrieval.py:900)
- [ownershipตัวแปรอยู่คนละfunction](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/retrieval.py:679)
- [service guard scope](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/user_service_facts.py:37)
- [map scope exclusion](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/user_service_facts.py:43)
- [exact/fuzzy names](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/answer.py:106)
- [fieldplanอ่านหลังเลือกentity](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/answer.py:258)
- [childrenของcompetition](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/answer.py:389)
- [confidence/validator](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/answer.py:435)
- [semantic correctnessยังfalse](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/read_contract.py:6)
- [schemaและsemanticguard](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/planner.py:51)
- [sourceownership](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/authority.py:20)
- [pricejoin](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/relations.py:46)
- [entitycandidates](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/entity_search.py:20)
- [typo candidate limits](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/knowledge/common/name_candidates.py:27)
- [oldgradeadapter](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/grade_legacy.py:10)
- [outcomeclassifierwhitelist](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/tools/eval_contract_v2.py:18)

- [R63: controlsย้ายไปlimitations](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r63_legacy_migration_20261013/migrate.py:160)
- [R63: facetยังpending](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r63_legacy_migration_20261013/migrate.py:175)
- [R63: calculation_ruleไม่อนุมาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r63_legacy_migration_20261013/migrate.py:270)
- [R64: draftview/fixture/config](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/harness.py:13)
- [R64: การแยกgradebranch](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/grade_legacy.py:10)
