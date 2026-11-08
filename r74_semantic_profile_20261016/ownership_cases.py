CASES=[
 dict(group='ownership_anchor',locale='en',question='Can I use the studio keyboard for my booking?',need=[],forbid=['Personal keyboards and mice are not allowed'],expected_source='!migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='ownership_anchor',locale='en',question='Can I use my keyboard?',need=['not allowed'],forbid=[],expected_source='migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='ownership_anchor',locale='th',question='ใช้คีย์บอร์ดของศูนย์ได้ไหม ผมจองไว้แล้ว',need=[],forbid=['ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัว'],expected_source='!migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='ownership_anchor',locale='en',question='Can I bring my own keyboards and mice?',need=['not allowed'],forbid=[],expected_source='migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='task_anchor',locale='en',question='Can I clean my own keyboard in the studio?',need=[],forbid=['Personal keyboards and mice are not allowed'],expected_source='!migrated_owner_claim_personal_keyboard_mouse'),
 dict(group='task_anchor',locale='th',question='ล้างคีย์บอร์ดส่วนตัวได้ไหม',need=[],forbid=['ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัว'],expected_source='!migrated_owner_claim_personal_keyboard_mouse'),
]
