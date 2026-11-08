# วิเคราะห์คำแปล control notes ที่แก้จาก source ทีละจุด

อ่าน Thai/English notes 390 แถวใน 36 records และปรับ 64 จุดตามรายการด้านล่าง นอกจากนี้มี manual numeric override 1/2 ครั้งแยกอีกหนึ่งแถว ไม่ใช่การประเมิน error rate แบบสุ่ม ไม่ใช่ human gold และบางจุดเป็นการเพิ่มความครบ/ความชัด มิใช่ทุกจุดผิดร้ายแรงเท่ากัน

## เหตุที่ literal guard ผ่านแต่ความหมายยังผิด

ประเภทความผิดพลาดยืนยันจากคู่ข้อความได้ แต่คำอธิบายเรื่อง polysemy/prior เป็นข้อสันนิษฐานเชิงภาษา ไม่ใช่การวัดน้ำหนักหรือ attention ภายในโมเดล ส่วน literal/negation guards และลำดับ branch ตรวจได้จากโค้ดและ logs โดยตรง

| กลุ่ม | ตัวอย่าง | ทำไมตัวตรวจเดิมไม่พอ | วิธีแก้ที่ใช้ |
|---|---|---|---|
| สลับสถานะหรือบทบาท | sheathed→equipped, Y global/U team สลับ | ตัวเลข/รูปประโยคยังถูก แต่เงื่อนไขหรือการจับคู่กลับด้าน | เทียบ relation/action กับ source รายแถว; มี regression ผ่าน reader จริง |
| เปลี่ยน gesture | click→hold | ทั้งสองเป็นคำอังกฤษที่ถูกไวยากรณ์ และไม่มี literal number ให้ตรวจ | ไม่อนุมาน gesture; เทียบ trigger/hold/tap กับต้นฉบับ |
| เลือกกริยา/คำนามผิดบริบท | holster→drop, knife→revolver, recoil/aim คำเฉพาะ | polysemy กับ prior ของ local model; schema ไม่ตรวจ lexical entailment | แก้จาก Thai source และรักษา buttons/actions เดิม |
| Negation ผูกผิด predicate | cannot parry→cannot dodge | ยังมีคำ cannot จึงผ่านตัวตรวจคำห้าม แต่ข้อห้ามคนละการกระทำ | ตรวจ predicate และขอบเขตเงื่อนไข คู่ภาษาและสถานการณ์ |
| เพิ่มสิ่งที่ source ไม่บอก | shot→headshot, gun→pistol | ยังดูเป็น gameplay ที่สมเหตุผล แต่ไม่ได้อยู่ใน source | ลบ specificity ที่ไม่มีหลักฐาน ไม่อ้างความรู้เกมแทนข้อมูล |
| ชื่อเฉพาะผิด | Chicago map, Leviathan greatsword | รูปประโยคและตัวเลขไม่เสีย แต่ชื่อหรือชนิดสิ่งของผิด | เทียบ Thai และชื่อจากแหล่งทางการ; ไม่เพิ่ม mechanics |
| สรุปสั้นจนข้อมูลหาย | Tool Ring/NookPhone เหลือชื่อ action | คำสำคัญยังอยู่ แต่รายละเอียดที่ผู้ใช้ถามหายไป | เติม note จาก source ทั้งประโยค ไม่ใช้ action label แทนคำอธิบาย |

ไม่แก้ด้วยการเพิ่ม alias ชื่อเกมหรือ hard-code คำตอบใหม่ใน router: ปรับการนำเข้า/คำแปลร่างและตรวจ source lineage การแก้ source ภาษาอังกฤษต้องเป็น revision ใหม่ เช่นเดียวกับข้อมูลทั่วไป

## รายการครบ 64 จุด

Source เป็น limitations note column; หมายเลข line เป็น zero-based ใน artifact เพื่อเทียบกับ pipe table ได้ตรง ไม่ใช่รหัสปุ่มที่สร้างใหม่

## 1. controls_nintendo_animal_crossing_new_horizons / line 5

**ต้นฉบับไทย:** หยิบไอเทมที่อยู่บนพื้น

**ข้อเสนอโมเดล:** Pick up Item

**ร่างที่แก้:** Pick up an item from the ground.

## 2. controls_nintendo_animal_crossing_new_horizons / line 6

**ต้นฉบับไทย:** เปิดเมนูวงล้อเพื่อเลือกหยิบเครื่องมืออย่างรวดเร็ว

**ข้อเสนอโมเดล:** Tool Ring

**ร่างที่แก้:** Open the tool wheel to select a tool quickly.

## 3. controls_nintendo_animal_crossing_new_horizons / line 7

**ต้นฉบับไทย:** สลับไปถือเครื่องมือชิ้นอื่นในกระเป๋าซ้ายหรือขวา

**ข้อเสนอโมเดล:** Change Tool

**ร่างที่แก้:** Switch to another tool in your pockets by cycling left or right.

## 4. controls_nintendo_animal_crossing_new_horizons / line 8

**ต้นฉบับไทย:** เก็บเครื่องมือในมือลงกระเป๋าทันที

**ข้อเสนอโมเดล:** Store Tool

**ร่างที่แก้:** Immediately put the tool you are holding back into your pockets.

## 5. controls_nintendo_animal_crossing_new_horizons / line 9

**ต้นฉบับไทย:** เรียกดูแอปพลิเคชันใน NookPhone

**ข้อเสนอโมเดล:** NookPhone

**ร่างที่แก้:** Open the applications on the NookPhone.

## 6. controls_nintendo_luigi_s_mansion_3 / line 2

**ต้นฉบับไทย:** เรียก สลับตัว หรือเก็บกูอิจิ (Gooigi) ซึ่งเป็นคู่หูร่างเยลลี่สำหรับช่วยแก้ปริศนา

**ข้อเสนอโมเดล:** Call, swap, or collect Gooigi, Luigi's jellyfriend companion for solving puzzles

**ร่างที่แก้:** Summon, switch to, or put away Gooigi, a jelly-like companion who helps solve puzzles.

## 7. controls_nintendo_luigi_s_mansion_3 / line 5

**ต้นฉบับไทย:** ฉายแสงพิเศษเพื่อเปิดเผยสิ่งของที่ซ่อนอยู่ ล่องหน หรือถูกคำสาป

**ข้อเสนอโมเดล:** Cast a special light to reveal hidden objects, ghosts, or cursed items.

**ร่างที่แก้:** Shine a special light to reveal hidden, invisible, or cursed objects.

## 8. controls_nintendo_luigi_s_mansion_3 / line 6

**ต้นฉบับไทย:** ยิงจุกยางติดสิ่งของหรือโล่ผี เพื่อใช้เครื่องดูดดึงทำลายสิ่งกีดขวาง

**ข้อเสนอโมเดล:** Shoot a suction nozzle attached to an object or ghost barrier to use the vacuum to clear obstacles.

**ร่างที่แก้:** Shoot a plunger onto an object or a ghost's shield, then use the vacuum to pull it and break obstacles.

## 9. controls_nintendo_super_smash_bros_ultimate / line 5

**ต้นฉบับไทย:** กางโล่เพื่อป้องกันการโจมตี สามารถกดพร้อมอนาล็อกซ้ายเพื่อกลิ้งหลบได้

**ข้อเสนอโมเดล:** Raise shield to block attacks. Can slide backward by pressing shield and left analog simultaneously.

**ร่างที่แก้:** Raise a shield to block attacks; combine it with the left stick to dodge-roll.

## 10. controls_nintendo_super_smash_bros_ultimate / line 6

**ต้นฉบับไทย:** จับคู่ต่อสู้เพื่อทุ่ม ใช้แก้ทางคู่ต่อสู้ที่กำลังกางโล่ได้ดี

**ข้อเสนอโมเดล:** Pair up to counterattack. Effective against opponents raising their shields.

**ร่างที่แก้:** Grab an opponent to throw them; this is effective against opponents who are shielding.

## 11. controls_nintendo_the_legend_of_zelda_breath_of_the_wild / line 0

**ต้นฉบับไทย:** บังคับการเดิน หรือเดินสไลด์หลบเมื่อกดล็อกเป้าหมาย

**ข้อเสนอโมเดล:** Walk or slide to dodge when aiming

**ร่างที่แก้:** Control walking, or sidestep while locked onto a target.

## 12. controls_nintendo_the_legend_of_zelda_breath_of_the_wild / line 5

**ต้นฉบับไทย:** กดเก็บอาวุธ หรือกดค้างเพื่อวิ่งโดยใช้หลอดสตามิน่า

**ข้อเสนอโมเดล:** Press to store weapon or hold to run using the Staminic Torch

**ร่างที่แก้:** Put away your weapon, or hold to run using the stamina gauge.

## 13. controls_nintendo_the_legend_of_zelda_breath_of_the_wild / line 10

**ต้นฉบับไทย:** ส่งเสียงผิวปากเพื่อเรียกม้าให้วิ่งมาหา

**ข้อเสนอโมเดล:** Press the trigger to summon a horse and make it charge toward you.

**ร่างที่แก้:** Whistle to call your horse so it runs toward you.

## 14. controls_nintendo_the_legend_of_zelda_breath_of_the_wild / line 15

**ต้นฉบับไทย:** เปิดแผนที่ชีคาห์เพื่อดูเส้นทาง

**ข้อเสนอโมเดล:** Open the Chicago map to view the route

**ร่างที่แก้:** Open the Sheikah map to check your route.

## 15. controls_pc_counter_strike_2 / line 0

**ต้นฉบับไทย:** W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา

**ข้อเสนอโมเดล:** W move forward, A turn left, S back up, D turn right

**ร่างที่แก้:** W moves forward, A moves left, S moves backward, and D moves right.

## 16. controls_pc_counter_strike_2 / line 14

**ต้นฉบับไทย:** Y แชทรวม, U แชททีม

**ข้อเสนอโมเดล:** Y for team chat, U for global chat

**ร่างที่แก้:** Y opens global chat; U opens team chat.

## 17. controls_pc_league_of_legends / line 0

**ต้นฉบับไทย:** คลิกขวาเพื่อเดินหรือสั่งโจมตีเป้าหมาย

**ข้อเสนอโมเดล:** Right-click to move or target

**ร่างที่แก้:** Right-click to move or command an attack on a target.

## 18. controls_pc_league_of_legends / line 7

**ต้นฉบับไทย:** กดค้างเพื่อให้กล้องตาม champion ตัวเอง

**ข้อเสนอโมเดล:** Hold to follow champion

**ร่างที่แก้:** Hold to make the camera follow your champion.

## 19. controls_pc_pubg_battlegrounds / line 3

**ต้นฉบับไทย:** นอนหมอบ

**ข้อเสนอโมเดล:** Squat

**ร่างที่แก้:** Lie prone.

## 20. controls_pc_pubg_battlegrounds / line 13

**ต้นฉบับไทย:** เก็บอาวุธที่ถืออยู่

**ข้อเสนอโมเดล:** Drop current weapon

**ร่างที่แก้:** Holster the weapon you are holding.

## 21. controls_pc_valorant / line 0

**ต้นฉบับไทย:** W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา

**ข้อเสนอโมเดล:** W move forward, A turn left, S move backward, D turn right

**ร่างที่แก้:** W moves forward, A moves left, S moves backward, and D moves right.

## 22. controls_pc_valorant / line 8

**ต้นฉบับไทย:** ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์

**ข้อเสนอโมเดล:** Use with Spike such as placing or retrieving depending on situation

**ร่างที่แก้:** Use the Spike, such as planting or defusing it, depending on the situation.

## 23. controls_ps5_call_of_duty_warzone / line 9

**ต้นฉบับไทย:** ยกปืนเล็งศูนย์

**ข้อเสนอโมเดล:** Raise weapon to sight zero

**ร่างที่แก้:** Raise the weapon to aim down its sights.

## 24. controls_ps5_call_of_duty_warzone / line 10

**ต้นฉบับไทย:** ลั่นไกปืน

**ข้อเสนอโมเดล:** Shoot with pistol

**ร่างที่แก้:** Pull the trigger to fire the weapon.

## 25. controls_ps5_call_of_duty_warzone / line 12

**ต้นฉบับไทย:** โจมตีด้วยพานท้ายปืน

**ข้อเสนอโมเดล:** Attack with shotgun

**ร่างที่แก้:** Strike with the butt of the weapon.

## 26. controls_ps5_ea_sports_fc_24 / line 1

**ต้นฉบับไทย:** โยนบอลยาวข้ามหัว เปิดบอลจากริมเส้น หรือโหม่งเคลียร์บอล

**ข้อเสนอโมเดล:** Long throw over the head, clear from the sideline, or header clear

**ร่างที่แก้:** Lob the ball overhead, cross from the wing, or make a headed clearance.

## 27. controls_ps5_ea_sports_fc_24 / line 3

**ต้นฉบับไทย:** ง้างเท้ายิงประตู โหม่งทำประตู หรือวอลเลย์

**ข้อเสนอโมเดล:** Lunge and shoot, header goal, or volley

**ร่างที่แก้:** Shoot at goal, head the ball toward goal, or volley.

## 28. controls_ps5_ea_sports_fc_24 / line 9

**ต้นฉบับไทย:** กดค้างเพื่อย่อตัวคุมเชิงในเกมรับ หรือพิงบังบอลขณะเลี้ยง

**ข้อเสนอโมเดล:** Hold down to crouch and control the inside during defense, or use your body to shield the ball while dribbling

**ร่างที่แก้:** Hold to jockey when defending, or shield the ball while dribbling.

## 29. controls_ps5_ea_sports_fc_24 / line 10

**ต้นฉบับไทย:** กดค้างเพื่อกระชากบอลและวิ่งด้วยความเร็วสูงสุด

**ข้อเสนอโมเดล:** Hold to pull the ball and sprint at maximum speed

**ร่างที่แก้:** Hold to push the ball forward and sprint at maximum speed.

## 30. controls_ps5_god_of_war_ragnar_k / line 5

**ต้นฉบับไทย:** ง้างอาวุธเตรียมขว้าง

**ข้อเสนอโมเดล:** Swing weapon to throw

**ร่างที่แก้:** Ready your weapon to throw it.

## 31. controls_ps5_god_of_war_ragnar_k / line 9

**ต้นฉบับไทย:** เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1

**ข้อเสนอโมเดล:** Draw blade back into hand or charge elemental power into weapon with L1 held

**ร่างที่แก้:** Recall the axe to your hand, or charge the weapon with elemental power while holding L1.

## 32. controls_ps5_god_of_war_ragnar_k / line 13

**ต้นฉบับไทย:** ชักขวาน Leviathan

**ข้อเสนอโมเดล:** Draw Leviathan's greatsword

**ร่างที่แก้:** Draw the Leviathan Axe.

## 33. controls_ps5_god_of_war_ragnar_k / line 15

**ต้นฉบับไทย:** ชักหอก Draupnir Spear

**ข้อเสนอโมเดล:** Draupnir Spear

**ร่างที่แก้:** Draw the Draupnir Spear.

## 34. controls_ps5_god_of_war_ragnar_k / line 16

**ต้นฉบับไทย:** สลับลูกธนูของคู่หู

**ข้อเสนอโมเดล:** Swap Companion Bow

**ร่างที่แก้:** Switch your companion's arrow type.

## 35. controls_ps5_gran_turismo_7 / line 5

**ต้นฉบับไทย:** ดึงเบรกมือเพื่อสไลด์หรือดริฟต์

**ข้อเสนอโมเดล:** Release handbrake to slide or drift

**ร่างที่แก้:** Pull the handbrake to slide or drift.

## 36. controls_ps5_hogwarts_legacy / line 8

**ต้นฉบับไทย:** กางโล่ Protego ป้องกันการโจมตี หากกดค้างจะสวนกลับด้วย Stupefy

**ข้อเสนอโมเดล:** Hold to activate Protego shield; hold longer to counterattack with Stupefy

**ร่างที่แก้:** Activate the Protego shield to defend against attacks; hold to counterattack with Stupefy.

## 37. controls_ps5_hogwarts_legacy / line 9

**ต้นฉบับไทย:** กลิ้งหลบการโจมตีที่ไม่สามารถปัดป้องได้ (มีเตือนสีแดง)

**ข้อเสนอโมเดล:** Roll away from attacks that cannot be dodged (red warning)

**ร่างที่แก้:** Roll to dodge attacks that cannot be parried, indicated by a red warning.

## 38. controls_ps5_hogwarts_legacy / line 15

**ต้นฉบับไทย:** ดื่มน้ำยาเพิ่มพลังชีวิต (Wiggenweld Potion)

**ข้อเสนอโมเดล:** Drink the Life-Boosting Potion (Wiggenweld Potion)

**ร่างที่แก้:** Drink a healing potion (Wiggenweld Potion).

## 39. controls_ps5_it_takes_two / line 10

**ต้นฉบับไทย:** ใช้เหวี่ยงตะขอสลิงเพื่อโหนเชือกข้ามไปยังจุดต่างๆ ในฉากที่กำหนดไว้

**ข้อเสนอโมเดล:** Use the sling lever to swing the rope across various points in the designated scene

**ร่างที่แก้:** Use a grappling hook to swing across designated points in the scene.

## 40. controls_ps5_marvel_s_spider_man_2 / line 1

**ต้นฉบับไทย:** เกาะบนจุดแคบๆ หรือพุ่งตัวดิ่งลงพื้นขณะอยู่กลางอากาศ

**ข้อเสนอโมเดล:** Climb narrow surfaces or dive down from the air mid-flight

**ร่างที่แก้:** Perch on a narrow point, or dive toward the ground while in mid-air.

## 41. controls_ps5_monster_hunter_rise / line 4

**ต้นฉบับไทย:** กดค้างเพื่อวิ่งสปรินต์ (ทำได้เมื่อเก็บอาวุธอยู่)

**ข้อเสนอโมเดล:** Hold to sprint (available when weapon is equipped)

**ร่างที่แก้:** Hold to sprint; this is available when your weapon is sheathed.

## 42. controls_ps5_monster_hunter_rise / line 5

**ต้นฉบับไทย:** ใช้เพื่อย่อตัว กลิ้งหลบการโจมตี หรือกระโดด

**ข้อเสนอโมเดล:** Use to shrink, roll away from attacks, or jump

**ร่างที่แก้:** Crouch, roll to dodge attacks, or jump.

## 43. controls_ps5_monster_hunter_rise / line 7

**ต้นฉบับไทย:** กดเพื่อใช้ไอเทมที่เลือกไว้ หรือกดเพื่อเก็บอาวุธเข้าฝัก

**ข้อเสนอโมเดล:** Press to use the selected item or press to equip weapons

**ร่างที่แก้:** Use the selected item, or sheath your weapon.

## 44. controls_ps5_naruto_x_boruto_ultimate_ninja_storm_connections / line 3

**ต้นฉบับไทย:** รีดเร้นจักระเพื่อใช้คาถาหรือท่าไม้ตายลับ (Secret Technique)

**ข้อเสนอโมเดล:** Draw the seal to use a hidden jutsu or secret technique (Secret Technique)

**ร่างที่แก้:** Channel chakra to use ninjutsu or a Secret Technique.

## 45. controls_ps5_overcooked / line 3

**ต้นฉบับไทย:** พุ่งตัวไปข้างหน้าเพื่อเพิ่มความเร็วในการเคลื่อนที่

**ข้อเสนอโมเดล:** Jump forward to increase movement speed.

**ร่างที่แก้:** Dash forward to increase movement speed.

## 46. controls_ps5_resident_evil_village / line 3

**ต้นฉบับไทย:** กดเพื่อย่อตัวลงต่ำ ใช้สำหรับลอดช่องแคบ ซ่อนตัว หรือหลบการโจมตีระดับสายตา

**ข้อเสนอโมเดล:** Crouch to lower your character, use for squeezing through narrow spaces, hiding, or dodging sight-based attacks

**ร่างที่แก้:** Crouch to pass through narrow spaces, hide, or avoid attacks at eye level.

## 47. controls_ps5_resident_evil_village / line 6

**ต้นฉบับไทย:** เหนี่ยวไกยิงปืนที่กำลังถืออยู่ หรือเหวี่ยงอาวุธประชิด (เช่น มีด) เพื่อโจมตีศัตรู

**ข้อเสนอโมเดล:** Grab the gun you're holding or swing melee weapons (such as a knife) to attack enemies

**ร่างที่แก้:** Pull the trigger to fire the weapon you are holding, or swing a melee weapon such as a knife.

## 48. controls_ps5_tekken_8 / line 2

**ต้นฉบับไทย:** ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู

**ข้อเสนอโมเดล:** Use the left leg kick to block or attack, creating openings for enemies

**ร่างที่แก้:** Kick with the left leg to intercept or attack and create an opening in the opponent's defense.

## 49. controls_ps5_tekken_8 / line 3

**ต้นฉบับไทย:** ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง

**ข้อเสนอโมเดล:** Use a powerful right leg swing — typically used for clearing range or cutting off high-damage attacks

**ร่างที่แก้:** Deliver a powerful right-leg kick, often for range control or a high-damage low sweep.

## 50. controls_ps5_tekken_8 / line 7

**ต้นฉบับไทย:** ขยับทิศทางของตัวละคร بشكلทั่วไป หรือใช้โยกทิศทางในการเคลื่อนที่และเดินหน้าถอยหลัง

**ข้อเสนอโมเดล:** Move the character in general directions or use directional shifts for walking and turning around

**ร่างที่แก้:** Move the character in general directions, including moving forward and backward.

## 51. controls_ps5_the_last_of_us_part_i / line 0

**ต้นฉบับไทย:** บังคับทิศทางการเดินและการย่องเคลื่อนที่ของตัวละคร

**ข้อเสนอโมเดล:** Move and strafe the character

**ร่างที่แก้:** Control walking and sneaking movement.

## 52. controls_ps5_the_last_of_us_part_i / line 3

**ต้นฉบับไทย:** กดคลิกลงไปตรงๆ เพื่อเปิดหรือปิดไฟฉายในพื้นที่มืด (และใช้เขย่าจอยเมื่อไฟฉายดับ)

**ข้อเสนอโมเดล:** Press and hold to toggle flashlight in dark areas (and shake the controller when flashlight turns off)

**ร่างที่แก้:** Click to toggle the flashlight in dark areas; shake the controller when the flashlight goes out.

## 53. controls_ps5_the_last_of_us_part_i / line 7

**ต้นฉบับไทย:** กดเพื่อรีโหลดกระสุน หรือกดค้างเพื่อใช้ไอเทมรักษา แต่ถ้ากดตอนเล็งปืนอยู่จะเป็นการเหนี่ยวไกยิง

**ข้อเสนอโมเดล:** Press to reload ammunition, or hold to use healing items; however, pressing while aiming will trigger a headshot

**ร่างที่แก้:** Press to reload, or hold to use a healing item; pressing while aiming fires the weapon.

## 54. controls_ps5_the_last_of_us_part_i / line 13

**ต้นฉบับไทย:** เปิดหน้าต่างกระเป๋าหลังเพื่อตรวจสอบไอเทม อัปเกรดตัวละคร หรือคราฟต์ระเบิด/มีดพก

**ข้อเสนอโมเดล:** Open the back inventory panel to check items, upgrade characters, or craft explosives/revolvers.

**ร่างที่แก้:** Open the backpack to inspect items, upgrade the character, or craft explosives and pocket knives.

## 55. controls_ps5_the_last_of_us_part_ii / line 0

**ต้นฉบับไทย:** บังคับทิศทางการเดิน การย่อง หรือการวิ่งของตัวละครไปตามฉาก

**ข้อเสนอโมเดล:** Move the character forward, sidestep, or sprint in the direction of the scene.

**ร่างที่แก้:** Control walking, sneaking, or running through the scene.

## 56. controls_ps5_the_last_of_us_part_ii / line 5

**ต้นฉบับไทย:** กดค้างไว้เพื่อยกอาวุธปืน คันธนู หรือไอเทมประเภทระเบิดขว้างขึ้นมาเตรียมพร้อมเล็งยิง

**ข้อเสนอโมเดล:** Hold to raise the pistol, bow, or throwable item for aiming.

**ร่างที่แก้:** Hold to raise a firearm, bow, or throwable explosive for aiming.

## 57. controls_ps5_the_last_of_us_part_ii / line 8

**ต้นฉบับไทย:** ใช้สำหรับเปิดประตู เก็บไอเทมวัตถุดิบตามฉาก แทรกตัวเข้าช่องแคบ หรือใช้จับศัตรูจากทางด้านหลัง

**ข้อเสนอโมเดล:** Use to open doors, collect scene-based raw materials, squeeze into narrow passages, or ambush enemies from behind.

**ร่างที่แก้:** Open doors, gather crafting materials, squeeze through narrow passages, or grab an enemy from behind.

## 58. controls_ps5_the_last_of_us_part_ii / line 9

**ต้นฉบับไทย:** กดหนึ่งครั้งเพื่อย่อตัวย่องเงียบหลบสายตา หรือกดค้างไว้เพื่อหมอบคลานไปกับพื้นราบ/พงหญ้าเพื่อซ่อนตัว

**ข้อเสนอโมเดล:** Tap once to crouch and move silently out of sight, or hold to crouch and crawl along flat surfaces or grass for concealment.

**ร่างที่แก้:** Press once to crouch and sneak out of sight, or hold to lie prone and crawl along the ground or through grass to hide.

## 59. controls_ps5_the_last_of_us_part_ii / line 10

**ต้นฉบับไทย:** ออกอาวุธโจมตีระยะประชิดทันที ไม่ว่าจะเป็นการรัวหมัด ต่อย ตบ หรือหวดด้วยอาวุธมีคม/ไม้หน้าสามที่ถืออยู่

**ข้อเสนอโมเดล:** Draw and attack immediately with melee strikes, punches, kicks, or swings using the three weapons held.

**ร่างที่แก้:** Immediately attack in melee by punching, slapping, or swinging the bladed weapon or wooden plank you are holding.

## 60. controls_ps5_the_last_of_us_part_ii / line 13

**ต้นฉบับไทย:** เปิดหน้าต่างกระเป๋าหลังเพื่อเข้าไปดูไอเทมทั้งหมด ผสมของ (คราฟต์ไอเทม) และกดใช้แต้มอัปเกรดสกิลตัวละคร

**ข้อเสนอโมเดล:** Open the back inventory panel to view all items, crafting materials, and use skill upgrade points.

**ร่างที่แก้:** Open the backpack to inspect all items, craft items, or spend skill upgrade points.

## 61. controls_ps5_uncharted_legacy_of_thieves_collection / line 4

**ต้นฉบับไทย:** กดค้างเพื่อยกปืนขึ้นเล็ง หรือใช้เป็นปุ่มเหยียบเบรกชะลอความเร็ว/ถอยหลังเมื่อขับรถ

**ข้อเสนอโมเดล:** Hold to raise weapon to aim or use as brake pedal to slow down/rollback when driving

**ร่างที่แก้:** Hold to raise the weapon and aim, or brake to slow down or reverse when driving.

## 62. controls_ps5_uncharted_legacy_of_thieves_collection / line 5

**ต้นฉบับไทย:** กดโยนเชือกตะขอเกี่ยวเพื่อโหนตัวข้ามเหว ไต่กำแพง หรือใช้ดึงลากสิ่งของในฉาก

**ข้อเสนอโมเดล:** Press the throw rope to swing across gaps, climb walls, or pull objects in scenes.

**ร่างที่แก้:** Throw a grappling hook to swing across gaps, climb walls, or pull objects in the scene.

## 63. controls_ps5_uncharted_legacy_of_thieves_collection / line 9

**ต้นฉบับไทย:** กดตอนเคลื่อนที่เพื่อม้วนตัวกลิ้งหลบ หรือกดเมื่ออยู่ใกล้สิ่งกีดขวางเพื่อเอาตัวเข้าพิงกำแพงหลบกระสุน

**ข้อเสนอโมเดล:** Press while moving to roll away, or press when near obstacles to crouch behind walls and dodge gunfire.

**ร่างที่แก้:** Press while moving to dodge-roll, or press near an obstacle to take cover against a wall.

## 64. controls_vr_horizon_call_of_the_mountain / line 2

**ต้นฉบับไทย:** หน้าเกมทางการระบุว่า PS VR2 Sense controllers มี grip button สำหรับจับวัตถุในเกม

**ข้อเสนอโมเดล:** The game menu specifies that PS VR2 Sense controllers have a grip button for grabbing objects in games

**ร่างที่แก้:** The official game page states that PS VR2 Sense controllers have a grip button for grabbing in-game objects.

## การเก็บหลักฐาน

- [Model proposals ดิบ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/CONTROL_NOTE_PROPOSALS) และ CALLS.jsonl เก็บผลที่ rejected ด้วย ไม่เขียนทับ
- [Reviewed copies](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/CONTROL_NOTE_REVIEWED) มี hash ใน CONTROL_NOTE_AGENT_REVIEW.json
- [Source-bound draft revisions](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/CONTROL_NOTE_TRANSLATION_REPAIRS.json) ไม่ได้ publish/approve

ชื่อเฉพาะเทียบ [Nintendo: Sheikah Slate และ map](https://zelda.nintendo.com/features/) และ [PlayStation: Leviathan Axe](https://www.playstation.com/en-us/god-of-war) ไม่ใช้เว็บเพิ่มปุ่มจาก patch ใหม่หรือแทนนโยบายศูนย์

คำแปลผ่าน agent review รอบนี้ยังไม่พิสูจน์ว่าเนื้อหา gameplay ใน Thai source ถูกต้องกับทุก preset/patch หรือว่าคำแปลทุกช่องในระบบผ่าน semantic review แล้ว
