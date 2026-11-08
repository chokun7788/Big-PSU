# ตรวจ36กรณีกติกาแข่งขันที่ไปกฎศูนย์ — แยกคำตอบตรงสาระกับหลักฐานผิดscope

กลุ่ม36keysอ่านคำถาม/คำตอบ/sourceแยกแล้ว บางข้อห้ามinstallตอบNoตรงสาระ แม้sourceผิดรายการ จึงไม่รวมเป็นcontentfalseทั้งกลุ่ม รวมการตรวจทุกไฟล์แล้ว167unique reviewed/probed keys มีตัวอย่างcontent/scope/omissionfailureยืนยัน117 ไม่ใช่จำนวนผิดทั้งหมด และไม่ใช่semanticaccuracy

## สอบถามหน่อยครับ กติกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม ครับ

`b74c2d5a23e53a3faf9277893b8d63678c69495426ef021899701a5d4ce3177a` — confirmed_content_scope_failure

สตรีมเกม: คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม [S1]

วินิจฉัย: ถามดูสตรีม/ใช้บัคระหว่างแข่ง แต่ตอบอนุญาตbroadcastingในศูนย์ทั่วไป ชนกับข้อห้ามwatchingและละส่วนบัคตามคำถามแต่ละkey

- competition_competition_rules_cs2_psu_phuket_2026_section_037 rev4: {"en": "2. The use of hacks is strictly prohibited. No hacks related to map or game engine may be used. Any violation will result in a penalty loss for that round/map, or disqualification.", "th": "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์"}
- competition_competition_rules_cs2_psu_phuket_2026_section_038 rev4: {"en": "3. Watching streams: players are not allowed to watch live streams during competition", "th": "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"}

## ตามกติกาการแข่งขัน CS2 อุปกรณ์ของตัวเองที่เอาเข้าแข่งได้มีอะไร

`a19abbb465d3cbfacdfda1df891c70ae1ea57a025c1edde1079f04bee1083dda` — confirmed_requested_list_omission

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: ถามรายการอุปกรณ์ที่นำเข้าแข่งขันได้ แต่ตอบทั่วไปว่าอุปกรณ์เสริมได้/keyboardmouseต้องแจ้ง ไม่ให้รายการและเงื่อนไขwiredheadphonesตามsource041

- competition_competition_rules_cs2_psu_phuket_2026_section_041 rev5: {"en": "1. Players may bring their own keyboard (wired/wireless), mouse (wired/wireless), mouse cord (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.", "th": "1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้"}

## Could you help me? Under CS2 tournament rules, what food and drinks are permitted in the competition area?

`ab1742f40d390b628a9d43dbba083e1485f5d2307a37839abe8269052ef6a9a4` — confirmed_content_scope_omission

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## Under VALORANT tournamment ruls, what food and beverages are permitted in the competition area?

`e12cb2d213f2594767a67750d9a17acd79fd32503a31d0ac67c8f303a91309d6` — confirmed_content_scope_omission

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งVALORANTแต่ไปกฎศูนย์ ไม่ส่งsealedwater/gum ในsource002 ส่วนmacroที่ตอบได้ไม่ชดเชยส่วนอาหารที่ตกหล่น

- competition_competition_rules_valorant_psu_phuket_2026_section_002 rev5: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"}

## กติกา CS2 ติดตั้งโปรแกรมเองได้ไหม

`f730b122d6f51866995c5d4a8edffda53aac04687c8925acead414687b074635` — literal_core_agrees_tournament_evidence_gap

ติดตั้งเกม โปรแกรม หรือ mod เองได้ไหม?: ผู้ใช้ติดตั้งเกม โปรแกรม หรือ mod เองไม่ได้ครับ หากต้องการเกมเพิ่ม ขอให้ศูนย์พิจารณาเป็นรายรายการได้ [S1]

วินิจฉัย: คำตอบหลักห้ามติดตั้งโปรแกรมตรงกับกติกาCS2 แต่หลักฐานที่ใช้เป็นownerpolicyบริการทั่วไปและมีคำแนะนำขอเพิ่มเกมนอกเรื่อง จึงเป็นscope/evidence/formatgap ไม่เหมารวมเป็นข้อเท็จจริงNoผิดเพราะwrongsourceflag

- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## กติกกา CS2 ในพื้นที่แข่งอนุญาตอาหารเครื่องดื่มอะไรบ้าง

`5dcbde57e44fd0539d836a8e9065b7314ed96b1c719a78d29c241b1cd172d4ee` — confirmed_content_scope_omission

มีข้อความนโยบายหลายฉบับที่ยังไม่ยืนยันขอบเขตหรือฉบับที่ใช้แทนกัน กรุณาตรวจสอบกับศูนย์ก่อนใช้เงื่อนไขที่ต่างกัน
อาหารและเครื่องดื่ม: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## สอบถามหน่อยครับ กติกา CS2 ในพื้นที่แข่งอนุญาตอาหารเครื่องดื่มอะไรบ้าง ครับ

`ccee9d0b6c9782ab0b735de2a0db2dad5c3749bf876c610b4742b54a3275f459` — confirmed_content_scope_omission

มีข้อความนโยบายหลายฉบับที่ยังไม่ยืนยันขอบเขตหรือฉบับที่ใช้แทนกัน กรุณาตรวจสอบกับศูนย์ก่อนใช้เงื่อนไขที่ต่างกัน
อาหารและเครื่องดื่ม: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## สอบถามหน่อยครับ กติกา CS2 ดูสตรีมสดระหว่างแข่งได้ไหม ครับ

`6c34e8d90bd5b8ba4aa3270b2f558def748d9fcfe4ad3dd81dd80615fab4c3c8` — confirmed_content_scope_failure

สตรีมเกม: คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม [S1]

วินิจฉัย: ถามดูสตรีม/ใช้บัคระหว่างแข่ง แต่ตอบอนุญาตbroadcastingในศูนย์ทั่วไป ชนกับข้อห้ามwatchingและละส่วนบัคตามคำถามแต่ละkey

- competition_competition_rules_cs2_psu_phuket_2026_section_037 rev4: {"en": "2. The use of hacks is strictly prohibited. No hacks related to map or game engine may be used. Any violation will result in a penalty loss for that round/map, or disqualification.", "th": "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์"}
- competition_competition_rules_cs2_psu_phuket_2026_section_038 rev4: {"en": "3. Watching streams: players are not allowed to watch live streams during competition", "th": "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"}

## Under CS2 tournament rules, may players install software on the supplied computers?

`e8aaae5ac5a9a5cae9fe199b604c596662d97e0f62d3c1c48f165d7341b99e3f` — literal_core_agrees_tournament_evidence_gap

Users cannot install games, programs or mods themselves. You may ask the studio to consider adding a game. [S1]

วินิจฉัย: คำตอบหลักห้ามติดตั้งโปรแกรมตรงกับกติกาCS2 แต่หลักฐานที่ใช้เป็นownerpolicyบริการทั่วไปและมีคำแนะนำขอเพิ่มเกมนอกเรื่อง จึงเป็นscope/evidence/formatgap ไม่เหมารวมเป็นข้อเท็จจริงNoผิดเพราะwrongsourceflag

- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## กติกกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม

`b831c304a760ed68a4e65048d50685a5cbbaac26f8cc19b9a469dc5371b9993b` — confirmed_content_scope_failure

สตรีมเกม: คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม [S1]

วินิจฉัย: ถามดูสตรีม/ใช้บัคระหว่างแข่ง แต่ตอบอนุญาตbroadcastingในศูนย์ทั่วไป ชนกับข้อห้ามwatchingและละส่วนบัคตามคำถามแต่ละkey

- competition_competition_rules_cs2_psu_phuket_2026_section_037 rev4: {"en": "2. The use of hacks is strictly prohibited. No hacks related to map or game engine may be used. Any violation will result in a penalty loss for that round/map, or disqualification.", "th": "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์"}
- competition_competition_rules_cs2_psu_phuket_2026_section_038 rev4: {"en": "3. Watching streams: players are not allowed to watch live streams during competition", "th": "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"}

## Could you help me? Under CS2 tournament rules, may players install software on the supplied computers?

`74e24b78b08691d9fc21558d2cd024a3917cde621146baef7e0614a1738d6001` — literal_core_agrees_tournament_evidence_gap

Users cannot install games, programs or mods themselves. You may ask the studio to consider adding a game. [S1]

วินิจฉัย: คำตอบหลักห้ามติดตั้งโปรแกรมตรงกับกติกาCS2 แต่หลักฐานที่ใช้เป็นownerpolicyบริการทั่วไปและมีคำแนะนำขอเพิ่มเกมนอกเรื่อง จึงเป็นscope/evidence/formatgap ไม่เหมารวมเป็นข้อเท็จจริงNoผิดเพราะwrongsourceflag

- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## Under VALORANT tournament rules, are macros permitted and what food or beverages are allowed?

`b7831ac28d3f72d91ef8a5d20fd7cc16ea9f5364b53d35579543aab535f92a42` — confirmed_content_scope_omission

**under valorant tournament rules, are macros permitted**

**PSU Phuket VALORANT 2026 Tournament**
Competition Rules and Format for VALORANT
PSU Phuket VALORANT Tournament 2026
Update: 17/02/2026
English below
Equipment and Accessories
In LAN competitions, players must strictly adhere to equipment specifications to ensure fairness.
* Self-provided equipment: Keyboard (wired/wireless), Mouse (wired/wireless), Mouse bungee cord, Mouse pad, In-ear headphones (wired), Wired headset
* Equipment provided by organizers: Organizers will provide PCs, monitors, headsets with microphones, tables, and chairs
* Allowed keyboard technologies: Snap Tap, SOCD, or equivalent technologies are permitted, unless otherwise instructed by officials
* Prohibited items:
* Macros (both software- and hardware-programmed) are strictly prohibited
* Installing any unauthorized programs on the provided computers is prohibited
* Accessing social media or any communication websites on competition computers is prohibited except for programs provided by organizers [S1]

**what food or beverages are allowed?**

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S2]
Food and drinks are allowed only in designated areas. [S3]

วินิจฉัย: ถามอาหารในพื้นที่แข่งVALORANTแต่ไปกฎศูนย์ ไม่ส่งsealedwater/gum ในsource002 ส่วนmacroที่ตอบได้ไม่ชดเชยส่วนอาหารที่ตกหล่น

- competition_competition_rules_valorant_psu_phuket_2026_section_002 rev5: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"}

## แข่ง CS2 ใช้อุปกรณ์ของตัวเองได้ไหม

`ea2f371db7fbaa9285dd40c7b365dae80cf27dab3569b7ea0324f4b7ab2f2b97` — permission_conditions_and_tournament_evidence_review_required

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: sourceCS2อนุญาตอุปกรณ์บางชนิด จึงยังไม่ตัดสินว่าYesทั่วไปเป็นfactfalse แต่ไม่แสดงขอบเขตที่นำมาได้ครบและอ้างpolicyผิดรายการ ต้องแยกpermissiontruthจากevidencecompleteness

- competition_competition_rules_cs2_psu_phuket_2026_section_041 rev5: {"en": "1. Players may bring their own keyboard (wired/wireless), mouse (wired/wireless), mouse cord (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.", "th": "1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้"}

## กติกา CS2 ใช้มาโครได้ไหม แล้วติดตั้งโปรแกรมเองได้ไหม

`63ffc68336435d8b569368650eae28d632b6c5866ef0dfe9c5bf897f21c5b1c5` — confirmed_multi_need_omission

ติดตั้งเกม โปรแกรม หรือ mod เองได้ไหม?: ผู้ใช้ติดตั้งเกม โปรแกรม หรือ mod เองไม่ได้ครับ หากต้องการเกมเพิ่ม ขอให้ศูนย์พิจารณาเป็นรายรายการได้ [S1]

วินิจฉัย: ตอบห้ามติดตั้งโปรแกรมเท่านั้น ไม่ตอบข้อห้ามใช้macroโดยเฉพาะhardwaremacroซึ่งไม่เท่ากับติดตั้งsoftware มีsource046/047ครบแต่แผนpolicyเดียวละneed

- competition_competition_rules_cs2_psu_phuket_2026_section_046 rev4: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"}
- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## Could you help me? Under CS2 tournament rules, how many players may prepare and what food or drinks are permitted?

`3e14ad6239c4133e7de4f823eb71598cb9104584ab1cbacb20aafbcad1844294` — confirmed_content_scope_omission

**could you help me? under cs2 tournament rules, how many players may prepare**

The checking service is unavailable; this detail cannot be confirmed.

**what food or drinks are permitted?**

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## Under CS2 tournamment ruls, what food and drinks are permitted in the competition area?

`5138ecee0ccc363050678920d69b00e051adfa505247721d3913723e3b729370` — confirmed_content_scope_omission

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## ตามกติกกาการแข่งขัน CS2 อุปกรณ์ของตัวเองที่เอาเข้าแข่งได้มีอะไร

`8e6f5c28cc732c618739595955c2c17786368398b372387fca6e1bb21d42d3d2` — confirmed_requested_list_omission

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: ถามรายการอุปกรณ์ที่นำเข้าแข่งขันได้ แต่ตอบทั่วไปว่าอุปกรณ์เสริมได้/keyboardmouseต้องแจ้ง ไม่ให้รายการและเงื่อนไขwiredheadphonesตามsource041

- competition_competition_rules_cs2_psu_phuket_2026_section_041 rev5: {"en": "1. Players may bring their own keyboard (wired/wireless), mouse (wired/wireless), mouse cord (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.", "th": "1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้"}

## กติกกา CS2 ดูสตรีมสดระหว่างแข่งได้ไหม

`280d0b3aa6249ffdb78b04485dae752e156b522d2977e703705053233a50efa4` — confirmed_content_scope_failure

สตรีมเกม: คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม [S1]

วินิจฉัย: ถามดูสตรีม/ใช้บัคระหว่างแข่ง แต่ตอบอนุญาตbroadcastingในศูนย์ทั่วไป ชนกับข้อห้ามwatchingและละส่วนบัคตามคำถามแต่ละkey

- competition_competition_rules_cs2_psu_phuket_2026_section_037 rev4: {"en": "2. The use of hacks is strictly prohibited. No hacks related to map or game engine may be used. Any violation will result in a penalty loss for that round/map, or disqualification.", "th": "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์"}
- competition_competition_rules_cs2_psu_phuket_2026_section_038 rev4: {"en": "3. Watching streams: players are not allowed to watch live streams during competition", "th": "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"}

## กติกา CS2 ในพื้นที่แข่งอนุญาตอาหารเครื่องดื่มอะไรบ้าง

`35997d9fa4f9c26af9f76d5caec7477ec80d40226628f01f55926ce691ef2af6` — confirmed_content_scope_omission

มีข้อความนโยบายหลายฉบับที่ยังไม่ยืนยันขอบเขตหรือฉบับที่ใช้แทนกัน กรุณาตรวจสอบกับศูนย์ก่อนใช้เงื่อนไขที่ต่างกัน
อาหารและเครื่องดื่ม: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## กติกา CS2 ดูสตรีมสดระหว่างแข่งได้ไหม

`bfdd2e2c31817f886389621fba02d1646ae7deb1ba25de9b44c56cdfb7f3d214` — confirmed_content_scope_failure

สตรีมเกม: คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม [S1]

วินิจฉัย: ถามดูสตรีม/ใช้บัคระหว่างแข่ง แต่ตอบอนุญาตbroadcastingในศูนย์ทั่วไป ชนกับข้อห้ามwatchingและละส่วนบัคตามคำถามแต่ละkey

- competition_competition_rules_cs2_psu_phuket_2026_section_037 rev4: {"en": "2. The use of hacks is strictly prohibited. No hacks related to map or game engine may be used. Any violation will result in a penalty loss for that round/map, or disqualification.", "th": "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์"}
- competition_competition_rules_cs2_psu_phuket_2026_section_038 rev4: {"en": "3. Watching streams: players are not allowed to watch live streams during competition", "th": "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"}

## กติกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม

`0c25d981c16244f8fe17020eaa9c404ed3481cb7c21cd832073e36db18f420d5` — confirmed_content_scope_failure

สตรีมเกม: คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม [S1]

วินิจฉัย: ถามดูสตรีม/ใช้บัคระหว่างแข่ง แต่ตอบอนุญาตbroadcastingในศูนย์ทั่วไป ชนกับข้อห้ามwatchingและละส่วนบัคตามคำถามแต่ละkey

- competition_competition_rules_cs2_psu_phuket_2026_section_037 rev4: {"en": "2. The use of hacks is strictly prohibited. No hacks related to map or game engine may be used. Any violation will result in a penalty loss for that round/map, or disqualification.", "th": "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์"}
- competition_competition_rules_cs2_psu_phuket_2026_section_038 rev4: {"en": "3. Watching streams: players are not allowed to watch live streams during competition", "th": "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"}

## Under CS2 tournament rules, are macros allowed and may I install software?

`08ad10b9b25964f2e8805dfe752c1de5dd639e4485f6a7bef5c56dc0142cae2f` — confirmed_multi_need_omission

Users cannot install games, programs or mods themselves. You may ask the studio to consider adding a game. [S1]

วินิจฉัย: ตอบห้ามติดตั้งโปรแกรมเท่านั้น ไม่ตอบข้อห้ามใช้macroโดยเฉพาะhardwaremacroซึ่งไม่เท่ากับติดตั้งsoftware มีsource046/047ครบแต่แผนpolicyเดียวละneed

- competition_competition_rules_cs2_psu_phuket_2026_section_046 rev4: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"}
- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## สอบถามหน่อยครับ กติกา CS2 ติดตั้งโปรแกรมเองได้ไหม ครับ

`eb1c4e139d12a326353abd9743427c74b823b8f9d29b3e33d357af981de169d8` — literal_core_agrees_tournament_evidence_gap

ติดตั้งเกม โปรแกรม หรือ mod เองได้ไหม?: ผู้ใช้ติดตั้งเกม โปรแกรม หรือ mod เองไม่ได้ครับ หากต้องการเกมเพิ่ม ขอให้ศูนย์พิจารณาเป็นรายรายการได้ [S1]

วินิจฉัย: คำตอบหลักห้ามติดตั้งโปรแกรมตรงกับกติกาCS2 แต่หลักฐานที่ใช้เป็นownerpolicyบริการทั่วไปและมีคำแนะนำขอเพิ่มเกมนอกเรื่อง จึงเป็นscope/evidence/formatgap ไม่เหมารวมเป็นข้อเท็จจริงNoผิดเพราะwrongsourceflag

- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## Could you help me? Under VALORANT tournament rules, what food and beverages are permitted in the competition area?

`45c39c8b860ced3fe7f63ddb59b60f7c4116b6522c2de71814aad4ca08ef4e3b` — confirmed_content_scope_omission

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งVALORANTแต่ไปกฎศูนย์ ไม่ส่งsealedwater/gum ในsource002 ส่วนmacroที่ตอบได้ไม่ชดเชยส่วนอาหารที่ตกหล่น

- competition_competition_rules_valorant_psu_phuket_2026_section_002 rev5: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"}

## สอบถามหน่อยครับ กติกา CS2 นำอุปกรณ์ของตัวเองอะไรมาได้ แล้วใครรับผิดชอบคุณภาพและความพร้อมของอุปกรณ์ ครับ

`aa7f166a403ba83e38f159861e98ed2134d7a43c7f498b7f1c42349db96348a8` — confirmed_multi_need_omission

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: ถามทั้งalloweditemsและใครรับผิดชอบquality/readiness แต่ตอบpermissionศูนย์ทั่วไป ละรายการและresponsibilityที่มีใน041/042

- competition_competition_rules_cs2_psu_phuket_2026_section_041 rev5: {"en": "1. Players may bring their own keyboard (wired/wireless), mouse (wired/wireless), mouse cord (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.", "th": "1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้"}
- competition_competition_rules_cs2_psu_phuket_2026_section_042 rev4: {"en": "2. Players are responsible for the quality and availability of their own equipment", "th": "2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง"}

## แข่ง RoV ใช้อุปกรณ์ของตัวเองได้ไหม

`5f3c3fa6e221faaa1ec5029d2a47f60be5c616b0abb457d6333c7cd768b93b5b` — confirmed_unsupported_permission_scope

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: กติกาRoVกำหนดmobilephone/internet/chargingและห้ามอุปกรณ์ที่ไม่ใช่โทรศัพท์ตามข้อกำหนด แต่คำตอบทั่วไปอ้างkeyboard/mouseและpersonalaccessoriesว่าใช้ได้โดยแจ้ง จึงให้สิทธิ์จากsourceผิดscope ไม่ใช่การยืนยันอุปกรณ์แข่งRoV

- competition_competition_rules_rov_blueket_2025_men_section_010 rev4: {"en": "5. Competition kits and equipment\n5.1. Personal mobile phones and internet access, and/or university-provided internet\n5.2. Power adapters and personal charging devices\n5.3. Tablets or iPads, as well as any other equipment other than a mobile phone (Mobile Phone), are not permitted for use during competition. If detected, the team will be immediately disqualified", "th": "5. ชุดแข่งขันและอุปกรณ์การแข่งขัน\n5.1. อุปกรณ์โทรศัพท์มือถือและอินเตอร์เน็ตส่วนตัว และ/หรืออินเทอร์เน็ตของทางมหาวิทยาลัย\n5.2. ปลั๊กพ่วงและอุปกรณ์ชาร์จแบตส่วนตัว\n5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที"}

## สอบถามหน่อยครับ กติกา CS2 ใช้มาโครได้ไหม แล้วติดตั้งโปรแกรมเองได้ไหม ครับ

`ec26461eff16947d6a799f754d13880c4b847e29c63f58d39eecfccc2b190e68` — confirmed_multi_need_omission

ติดตั้งเกม โปรแกรม หรือ mod เองได้ไหม?: ผู้ใช้ติดตั้งเกม โปรแกรม หรือ mod เองไม่ได้ครับ หากต้องการเกมเพิ่ม ขอให้ศูนย์พิจารณาเป็นรายรายการได้ [S1]

วินิจฉัย: ตอบห้ามติดตั้งโปรแกรมเท่านั้น ไม่ตอบข้อห้ามใช้macroโดยเฉพาะhardwaremacroซึ่งไม่เท่ากับติดตั้งsoftware มีsource046/047ครบแต่แผนpolicyเดียวละneed

- competition_competition_rules_cs2_psu_phuket_2026_section_046 rev4: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"}
- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## แข่ง VALORANT ใช้อุปกรณ์ของตัวเองได้ไหม

`45a04c34704313422852c0dd6e2d8ee83232b0e23fc969a3f31b333e1cad4d23` — permission_conditions_and_tournament_evidence_review_required

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: sourceVALORANTอนุญาตอุปกรณ์ตามรายการ คำตอบYesบริการทั่วไปยังไม่ยืนยันเงื่อนไขการแข่งขันครบ ไม่เหมาว่าYesผิดทั้งหมดหรือยอมรับว่าpermissionครบแล้ว

- competition_competition_rules_valorant_psu_phuket_2026_section_001 rev5: {"en": "Competition Rules and Format for VALORANT\nPSU Phuket VALORANT Tournament 2026\nUpdate: 17/02/2026\nEnglish below\nEquipment and Accessories\nIn LAN competitions, players must strictly adhere to equipment specifications to ensure fairness.\n* Self-provided equipment: Keyboard (wired/wireless), Mouse (wired/wireless), Mouse bungee cord, Mouse pad, In-ear headphones (wired), Wired headset\n* Equipment provided by organizers: Organizers will provide PCs, monitors, headsets with microphones, tables, and chairs\n* Allowed keyboard technologies: Snap Tap, SOCD, or equivalent technologies are permitted, unless otherwise instructed by officials\n* Prohibited items:\n* Macros (both software- and hardware-programmed) are strictly prohibited\n* Installing any unauthorized programs on the provided computers is prohibited\n* Accessing social media or any communication websites on competition computers is prohibited except for programs provided by organizers", "th": "กฎระเบียบและรูปแบบการแข่งขัน VALORANT\nรายการ PSU Phuket VALORANT 2026 Tournament\nUpdate: 17/02/2026\nEnglish below\nอุปกรณ์และอุปกรณ์ต่อพ่วง\nในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม\n* อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)\n* อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้\n* เทคโนโลยีคีย์บอร์ด อนุญาตใ

## Could you help me? Under VALORANT tournament rules, are macros permitted and what food or beverages are allowed?

`647eb83671b627d6f9ce883b92ec9e53dc88d9f4380ebe91bbbe61c40bba52c6` — confirmed_content_scope_omission

**could you help me? under valorant tournament rules, are macros permitted**

**PSU Phuket VALORANT 2026 Tournament**
Competition Rules and Format for VALORANT
PSU Phuket VALORANT Tournament 2026
Update: 17/02/2026
English below
Equipment and Accessories
In LAN competitions, players must strictly adhere to equipment specifications to ensure fairness.
* Self-provided equipment: Keyboard (wired/wireless), Mouse (wired/wireless), Mouse bungee cord, Mouse pad, In-ear headphones (wired), Wired headset
* Equipment provided by organizers: Organizers will provide PCs, monitors, headsets with microphones, tables, and chairs
* Allowed keyboard technologies: Snap Tap, SOCD, or equivalent technologies are permitted, unless otherwise instructed by officials
* Prohibited items:
* Macros (both software- and hardware-programmed) are strictly prohibited
* Installing any unauthorized programs on the provided computers is prohibited
* Accessing social media or any communication websites on competition computers is prohibited except for programs provided by organizers [S1]

**what food or beverages are allowed?**

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S2]
Food and drinks are allowed only in designated areas. [S3]

วินิจฉัย: ถามอาหารในพื้นที่แข่งVALORANTแต่ไปกฎศูนย์ ไม่ส่งsealedwater/gum ในsource002 ส่วนmacroที่ตอบได้ไม่ชดเชยส่วนอาหารที่ตกหล่น

- competition_competition_rules_valorant_psu_phuket_2026_section_002 rev5: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"}

## Under CS2 tournament rules, what food and drinks are permitted in the competition area?

`26e576a44c55d6e8b13351b6346b4960162c14a8f52e84e5bba00df5bed461a0` — confirmed_content_scope_omission

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## Could you help me? Under CS2 tournament rules, are macros allowed and may I install software?

`e3d2f2e558e5f0f5ca930737f4c46fa495164408f50e371250a7e9c90d60617e` — confirmed_multi_need_omission

Users cannot install games, programs or mods themselves. You may ask the studio to consider adding a game. [S1]

วินิจฉัย: ตอบห้ามติดตั้งโปรแกรมเท่านั้น ไม่ตอบข้อห้ามใช้macroโดยเฉพาะhardwaremacroซึ่งไม่เท่ากับติดตั้งsoftware มีsource046/047ครบแต่แผนpolicyเดียวละneed

- competition_competition_rules_cs2_psu_phuket_2026_section_046 rev4: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"}
- competition_competition_rules_cs2_psu_phuket_2026_section_047 rev4: {"en": "4. No self-installed programs are allowed on the designated computers.", "th": "4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"}

## Under VALORANT tournament rules, what food and beverages are permitted in the competition area?

`5e39450eb8ad01a2fe62eb3d069101a955605aa5458226fd4c761f56f89dc23d` — confirmed_content_scope_omission

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งVALORANTแต่ไปกฎศูนย์ ไม่ส่งsealedwater/gum ในsource002 ส่วนmacroที่ตอบได้ไม่ชดเชยส่วนอาหารที่ตกหล่น

- competition_competition_rules_valorant_psu_phuket_2026_section_002 rev5: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"}

## แข่ง Tekken 8 ใช้อุปกรณ์ของตัวเองได้ไหม

`0b4a89e0d1b7470c63bc2b8c6918093219164c52db54552a1c201333fced411f` — tournament_permission_source_review_required

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: sourceที่ตรวจยืนยันPS5/formatยังไม่ให้หลักฐานสิทธิ์keyboardmouseส่วนตัวเฉพาะรายการ การอ้างownerpolicyศูนย์ไม่พอ จึงคงreview_requiredไม่เดาว่าอนุญาตหรือห้ามจริงทุกอุปกรณ์

- competition_competition_rules_tekken8_psu_esports_section_002 rev5: {"en": "Competition rules\n* Offline competition.\n* PlayStation 5 is used.\n* Singles (1v1).\n* Competition format:\n* FT2: the winner is the first to win 2 games.\n* Each game uses R3 (3 rounds per game) and 60S (60 seconds per round).\n* At a 1-1 tie, a deciding game must be played.", "th": "กติกาการแข่งขัน\n* แข่งขันแบบ ออฟไลน์ (Offline)\n* ใช้เครื่องเกม PlayStation 5\n* แข่งขันแบบ เดี่ยว (1v1)\n* รูปแบบการแข่งขัน:\n* FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน\n* ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)\n* หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน"}

## Under CS2 tournament rules, how many players may prepare and what food or drinks are permitted?

`371be50e98e5ca284403c057b39453d45402a0fd6689abe8829cd0f0de631523` — confirmed_content_scope_omission

**under cs2 tournament rules, how many players may prepare**

The checking service is unavailable; this detail cannot be confirmed.

**what food or drinks are permitted?**

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S1]
Food and drinks are allowed only in designated areas. [S2]

วินิจฉัย: ถามอาหารในพื้นที่แข่งCS2 แต่ตอบdesignatedareasของศูนย์พร้อมconflictwarning ไม่ส่งสาระเฉพาะน้ำภาชนะปิด/หมากฝรั่งที่sourceยืนยัน ถ้าถามMatchPrepด้วยยังมีส่วนจำนวนคนที่ไม่ตอบ

- competition_competition_rules_cs2_psu_phuket_2026_section_050 rev4: {"en": "1. Personnel during preparation: no more than 6 players are allowed.", "th": "1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน"}
- competition_competition_rules_cs2_psu_phuket_2026_section_053 rev5: {"en": "4. Only drinking water in sealed containers and chewing gum are permitted.", "th": "4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น"}

## กติกา CS2 นำอุปกรณ์ของตัวเองอะไรมาได้ แล้วใครรับผิดชอบคุณภาพและความพร้อมของอุปกรณ์

`780e5b6c4d205678de0a96f7485412589c44d51a2e30534f12c192279c476b01` — confirmed_multi_need_omission

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: ถามทั้งalloweditemsและใครรับผิดชอบquality/readiness แต่ตอบpermissionศูนย์ทั่วไป ละรายการและresponsibilityที่มีใน041/042

- competition_competition_rules_cs2_psu_phuket_2026_section_041 rev5: {"en": "1. Players may bring their own keyboard (wired/wireless), mouse (wired/wireless), mouse cord (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.", "th": "1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้"}
- competition_competition_rules_cs2_psu_phuket_2026_section_042 rev4: {"en": "2. Players are responsible for the quality and availability of their own equipment", "th": "2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง"}

## ตามกติกกาการแข่่งขัน CS2 อุปกรณ์ของตัวเองที่เอาเข้าแข่งได้มีอะไร

`9120edfcaef8ce35067db5551cddf1d92320416db8f6ac9727255df3ff30866c` — confirmed_requested_list_omission

อุปกรณ์ส่วนตัว: อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง [S1]

วินิจฉัย: ถามรายการอุปกรณ์ที่นำเข้าแข่งขันได้ แต่ตอบทั่วไปว่าอุปกรณ์เสริมได้/keyboardmouseต้องแจ้ง ไม่ให้รายการและเงื่อนไขwiredheadphonesตามsource041

- competition_competition_rules_cs2_psu_phuket_2026_section_041 rev5: {"en": "1. Players may bring their own keyboard (wired/wireless), mouse (wired/wireless), mouse cord (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.", "th": "1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้"}
