แนะนำฟอร์มเจ้าของแยกหมวดที่บันทึกลงข้อมูลกลางแบบมีชนิดและstableIDs/relations พร้อมsource, validity, approvalและtranslationrevision จากนั้นให้เครื่องมืออ่าน/คำนวณค่าจริงและให้LLMตีความคำถามและเรียบเรียงเฉพาะหลักฐาน งานSGD/D3STสนับสนุนschema descriptions; SGD-Xชี้schema sensitivity; MS-RAGชี้ปัญหาgraph extractionและประโยชน์ของข้อมูลหลายระดับ; ALCEช่วยแยกความถูกต้องกับcitation support

แบบที่จัดเตรียมมี24record types/155fields ครอบคลุมหมวดเดิม มี24drafttemplatesและ6ตัวอย่างจากข้อมูลจริง ตัวตรวจต้นแบบผ่าน45checks แต่ยังไม่เชื่อมกับเว็บจริง ไม่ได้อ้างว่าformatเพียงอย่างเดียวแก้คำถามทุกแบบได้ ขั้นแรกควรพิสูจน์เพิ่มเกมชื่อใหม่แล้วgenericruntimeอ่านได้โดยไม่patchชื่อเกม

ค้นงานต้นฉบับและจัดbibliography23งานพร้อม5เอกสารมาตรฐาน ระดับอ่านแยกในpapers.json ใช้เว็บแทนpipelinepaper-search-proเพราะไม่มีAPIconfiguration ไม่มีRCS/coverageestimateหรือsystematicreviewclaim ไฟล์ข้อมูลที่audit488ไฟล์มีhashสำหรับตรวจการรักษาต้นฉบับ
