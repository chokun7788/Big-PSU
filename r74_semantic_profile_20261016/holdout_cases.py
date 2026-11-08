CASES=[
 dict(group='unseen_permission',locale='en',question='Would I be permitted to play with my personal keyboard?',need=['not allowed'],forbid=[],expected_source='migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='unseen_permission',locale='en',question='Is using my mouse permitted in the studio?',need=['not allowed'],forbid=[],expected_source='migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='unseen_permission',locale='th',question='พอดีมีเมาส์ตัวเอง ขอเอาไปใช้ได้มั้ย',need=['ไม่อนุญาต'],forbid=[],expected_source='migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='unseen_correction',locale='en',question='The slip I attached was incorrect. Please tell me how to correct it.',need=['Facebook'],forbid=[],expected_source='procedure_wrong_slip'),
 dict(group='unseen_correction',locale='th',question='รูปสลิปที่แนบตอนจองไม่ถูกต้อง อยากแก้ต้องทำอย่างไร',need=['ส่งสลิป'],forbid=[],expected_source='procedure_wrong_slip'),
 dict(group='semantic_synonym',locale='en',question='I attached the incorrect proof of payment. How do I fix it?',need=['Facebook'],forbid=['10 minutes'],expected_source='procedure_wrong_slip'),
 dict(group='unseen_unknown',locale='en',question='My booking payment was too low. What should I do?',need=['does not confirm','underpayments'],forbid=['within 10 minutes'],expected_topic='underpayment'),
 dict(group='unseen_ownership',locale='en',question="Could I use the studio's mouse for my session?",need=[],forbid=['Personal keyboards and mice are not allowed'],expected_source='!migrated_owner_claim_personal_keyboard_mouse'),
]
