# Flow ทดลอง shared need contract

Parent: r135_bounded_response_20261111. รุ่นก่อนหน้าและfrozen evaluationsเก็บไว้แยก

1. ตรึงraw question,reference time,snapshotและruntime identity
2. ใช้bounded typo recoveryเดิม พร้อมprotectednames/numbers/polarityและvalidatedderivation
3. แบ่งทุกcoordinatorในครั้งเดียวเป็นexact raw need spans โดยป้องกันsource names/literals และเก็บqualifiersไว้กับงานที่เกี่ยว
4. Native plannerและindependent need observationใช้lexical boundariesร่วม แต่ยังตรวจsemantic needs/targets/slots/sourceแยกกัน ไม่รับรองwhole-requestsemanticsจากการแบ่งตรงกัน
5. ตรวจบริบทซ้ำโดยrecompute source basis และใช้compiler/source/receipt guardsเดิม ไม่ใช้audit tagsเป็นauthority
6. อ่านtyped facts/ราคา/ขั้นตอนที่ทำด้วยโค้ดได้ก่อน;เมื่อmodelbudgetหมดไม่ทิ้งverifiedsiblings
7. ส่งส่วนที่ผ่านพร้อมpartial/unresolved reasons และpubliccitationsที่exactpinsผ่าน ไม่อ้างทำธุรกรรมสำเร็จ
8. ตรวจfinaldelivery+regressionsก่อนbroadrun ดูIMPLEMENTATION_REPORT_TH.md และFINAL_MANIFEST.json

Preview8143 R135-Shared-contract-working;ไม่เปลี่ยนproductionหรือweights ไม่รัน200/2111ใหม่รอบนี้
