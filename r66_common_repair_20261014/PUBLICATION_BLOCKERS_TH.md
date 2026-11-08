# ข้อที่ยังปิดการเผยแพร่ร่าง Format กลาง

อ้างอิง RELEASE_AUDIT_6.json; candidate 588 records; blocked 588; active release ว่าง ข้อมูลยังอยู่ครบ มิใช่ถูกลบเมื่อไม่ผ่าน gate

## ต้องแยกงานเทคนิคกับ facts ที่ยังไม่ทราบ

- source needs factual review: เป็น trust state ของแหล่งที่ย้ายมา ไม่ได้แปลว่าทุกข้อพิสูจน์แล้วว่าผิด ต้องยืนยันเอกสาร/แหล่งฉบับที่จะใช้งาน ไม่สร้าง owner attestation แทนเจ้าของ
- Time-sensitive content requires confirmed validity: วันที่ได้รับไฟล์ไม่ใช่วันเริ่มใช้ ต้องมีช่วงมีผลของอัตรา/บริการ/รายการที่ไวต่อเวลา
- required before publication: ข้อมูลย้ายมายังไม่ครบ core schema บางช่องเป็น metadata ที่เสนอจาก source ได้ เช่น facet/excerpt completeness; บางช่องเช่น gesture/context ห้ามเดา ต้องเก็บเป็น partial จนมีหลักฐานพอ
- การอ่าน draft ใน eval/Owner preview ได้ ไม่เท่ากับ publish gate ผ่าน; อย่าเปิด evaluation override ในเว็บ production เพื่อหลบ gate

## Core fields ที่ยังขาด (นับ records ที่พบ)

| Field | Records |
|---|---:|
| facet | 104 |
| completeness | 104 |
| input_device | 38 |
| preset | 38 |
| bindings | 38 |
| public_scope | 25 |
| unit | 18 |
| calculation_rule | 18 |
| device_type | 16 |
| operational_status | 14 |
| zone_ids | 10 |
| occupancy_minutes | 8 |
| eligibility | 5 |
| open_periods | 5 |
| resource_ids | 4 |
| coverage | 4 |
| timezone | 1 |
| conditions_all | 1 |

## สาเหตุทั้งหมดและจำนวน (หลายสาเหตุใน record เดียวได้)

| Reason | Occurrences |
|---|---:|
| topic: source needs factual review | 191 |
| question: source needs factual review | 190 |
| answer: source needs factual review | 190 |
| Time-sensitive content requires confirmed validity | 145 |
| game_id: source needs factual review | 112 |
| competition_id: source needs factual review | 104 |
| section_number: source needs factual review | 104 |
| facet: required before publication | 104 |
| heading: source needs factual review | 104 |
| text: source needs factual review | 104 |
| completeness: required before publication | 104 |
| service_id: source needs factual review | 94 |
| name: source needs factual review | 74 |
| offered: source needs factual review | 70 |
| title: source needs factual review | 48 |
| audience_id: source needs factual review | 48 |
| amount_minor: source needs factual review | 48 |
| currency: source needs factual review | 48 |
| platform: source needs factual review | 46 |
| input_device: required before publication | 38 |
| preset: required before publication | 38 |
| bindings: required before publication | 38 |
| limitations: source needs factual review | 38 |
| genre: source needs factual review | 36 |
| summary: source needs factual review | 36 |
| how_to_play: source needs factual review | 36 |
| installed_resource_ids: source needs factual review | 28 |
| display_name: source needs factual review | 25 |
| role: source needs factual review | 25 |
| team: source needs factual review | 25 |
| public_scope: required before publication | 25 |
| zone_ids: source needs factual review | 24 |
| period_label: source needs factual review | 24 |
| equipment_included: source needs factual review | 24 |
| room_seats: source needs factual review | 24 |
| duration_minutes: source needs factual review | 24 |
| persons_min: source needs factual review | 24 |
| persons_max: source needs factual review | 24 |
| unit: required before publication | 18 |
| calculation_rule: required before publication | 18 |
| device_type: required before publication | 16 |
| specifications: source needs factual review | 16 |
| usage: source needs factual review | 16 |
| zone_id: source needs factual review | 14 |
| capacity_persons: source needs factual review | 14 |
| physical_pool_key: source needs factual review | 14 |
| operational_status: required before publication | 14 |
| open_periods: source needs factual review | 12 |
| zone_ids: required before publication | 10 |
| session_minutes: source needs factual review | 8 |
| occupancy_minutes: required before publication | 8 |
| capacity_min: source needs factual review | 8 |
| capacity_max: source needs factual review | 8 |
| reason: source needs factual review | 7 |
| timezone: source needs factual review | 7 |
| weekday: source needs factual review | 7 |
| bookable_periods: source needs factual review | 7 |
| maintenance_periods: source needs factual review | 7 |
| unit: source needs factual review | 6 |
| calculation_rule: source needs factual review | 6 |
| eligibility: required before publication | 5 |
| open_periods: required before publication | 5 |
| open_periods: unresolved conflict | 5 |
| resource_ids: required before publication | 4 |
| event_name: source needs factual review | 4 |
| rulebook_release: source needs factual review | 4 |
| coverage: required before publication | 4 |
| terms: source needs factual review | 4 |
| resource_ids: source needs factual review | 4 |
| local_date: source needs factual review | 3 |
| state: source needs factual review | 3 |
| limitations: English translation needs review or explicit machine-translation status | 2 |
| operator: source needs factual review | 1 |
| address: source needs factual review | 1 |
| building: source needs factual review | 1 |
| floor: source needs factual review | 1 |
| map_url: source needs factual review | 1 |
| timezone: required before publication | 1 |
| subject: source needs factual review | 1 |
| decision: source needs factual review | 1 |
| conditions_all: required before publication | 1 |
| details: source needs factual review | 1 |
| name: English translation needs review or explicit machine-translation status | 1 |

## ราย record

ข้อมูลนี้เป็นรายการที่ต้องจัดการก่อน release ไม่ใช่สิ่งที่ส่งไปเป็นคำตอบให้ผู้ใช้ทุกครั้ง

### game_detail_animal_crossing — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_beat_saber — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_call_of_duty_mw3 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_cs2 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_ea_sports_fc_24 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_final_fantasy_xvi — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_fortnite — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_god_of_war_ragnarok — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_gran_turismo_7 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_hogwarts_legacy — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_horizon_call_of_the_mountain — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_it_takes_two — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_league_of_legends — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_little_nightmares_2 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_luigis_mansion_3 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_mario_kart_8 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_mario_party — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_monster_hunter_rise — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_moving_out_2 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_naruto_x_boruto — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_new_super_mario_bros — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_overcooked_2 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_pubg — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_resident_evil_4 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_resident_evil_village — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_ring_fit_adventure — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_spider_man_2 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_super_mario_odyssey — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_super_smash_bros — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_switch_sports — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_tekken_8 — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_the_last_of_us — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_uncharted — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_valorant — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_warzone — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### game_detail_zelda_breath_of_the_wild — game

- title: source needs factual review
- genre: source needs factual review
- summary: source needs factual review
- how_to_play: source needs factual review

### center_psu_phuket — center

- name: source needs factual review
- operator: source needs factual review
- address: source needs factual review
- building: source needs factual review
- floor: source needs factual review
- map_url: source needs factual review
- timezone: required before publication

### policy_personal_keyboard_mouse — policy

- topic: source needs factual review
- subject: source needs factual review
- decision: source needs factual review
- conditions_all: required before publication
- details: source needs factual review

### audience_external_org — audience

- name: source needs factual review
- eligibility: required before publication
- name: English translation needs review or explicit machine-translation status

### zone_pc — zone

- name: source needs factual review

### rental_pc_external_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### zone_cockpit — zone

- name: source needs factual review

### resource_cockpit_01 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_cockpit_02 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### zone_nintendo — zone

- name: source needs factual review

### availability_nintendo_1_2 — service

- name: source needs factual review
- resource_ids: required before publication
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_game_pok_mon_champions — game

- title: source needs factual review

### migrated_link_availability_nintendo_1_2_migrated_game_pok_mon_champions — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_animal_crossing — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_it_takes_two — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_little_nightmares_2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_luigis_mansion_3 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_mario_kart_8 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_mario_party — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_monster_hunter_rise — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_moving_out_2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_new_super_mario_bros — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_switch_sports — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_game_overcooked — game

- title: source needs factual review

### migrated_link_availability_nintendo_1_2_migrated_game_overcooked — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_overcooked_2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_ring_fit_adventure — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_super_mario_odyssey — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_super_smash_bros — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_2_game_detail_zelda_breath_of_the_wild — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### availability_nintendo_1_4 — service

- name: source needs factual review
- resource_ids: required before publication
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_link_availability_nintendo_1_4_migrated_game_pok_mon_champions — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_animal_crossing — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_it_takes_two — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_little_nightmares_2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_luigis_mansion_3 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_mario_kart_8 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_mario_party — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_monster_hunter_rise — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_moving_out_2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_new_super_mario_bros — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_switch_sports — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_migrated_game_overcooked — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_overcooked_2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_ring_fit_adventure — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_super_mario_odyssey — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_super_smash_bros — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_nintendo_1_4_game_detail_zelda_breath_of_the_wild — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### resource_pc_01 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_02 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_03 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_04 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_05 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_06 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_07 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_08 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_09 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_pc_10 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### zone_ps5 — zone

- name: source needs factual review

### resource_ps5_01 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### resource_ps5_02 — resource

- name: source needs factual review
- zone_id: source needs factual review
- capacity_persons: source needs factual review
- physical_pool_key: source needs factual review
- operational_status: required before publication

### migrated_game_delta_force — game

- title: source needs factual review

### migrated_game_efootball — game

- title: source needs factual review

### migrated_game_the_finals — game

- title: source needs factual review

### migrated_game_the_last_of_us_part_i — game

- title: source needs factual review

### migrated_game_the_last_of_us_part_ii_remastered — game

- title: source needs factual review

### zone_vr — zone

- name: source needs factual review

### availability_vr_30 — service

- name: source needs factual review
- resource_ids: required before publication
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_link_availability_vr_30_game_detail_beat_saber — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_vr_30_game_detail_horizon_call_of_the_mountain — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_vr_30_game_detail_resident_evil_4 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_vr_30_game_detail_resident_evil_village — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### availability_vr_60 — service

- name: source needs factual review
- resource_ids: required before publication
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_link_availability_vr_60_game_detail_beat_saber — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_vr_60_game_detail_horizon_call_of_the_mountain — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_vr_60_game_detail_resident_evil_4 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_link_availability_vr_60_game_detail_resident_evil_village — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review

### migrated_faq_rule_booking_advance — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_booking_cancel_invalid_info — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_booking_max_sessions — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_booking_non_transferable — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_booking_session_and_payment — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_booking_steps — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_cancel_advance — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_checkin_advance — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_checkin_late — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_edit_booking — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_booking_required_information — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_booking_steps_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_cancel_booking — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_checkin_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_payment_deadline_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_payment_method_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_payment_10_minutes — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_payment_and_late_checkin — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_payment_bank — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_refund_policy — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_reservation_quick_summary — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_afternoon_time — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_friday_maintenance — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_friday_maintenance_general — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_monday_morning — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_monday_morning_specific — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_monday_open_close — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_monday_play_window — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_morning_time — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_schedule_not_24_hours — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_service_schedule — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_user_info_and_slip — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### competition_competition_rules_cs2_psu_phuket_2026 — competition

- Time-sensitive content requires confirmed validity
- game_id: source needs factual review
- event_name: source needs factual review
- rulebook_release: source needs factual review
- coverage: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_001 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_002 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_003 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_004 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_005 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_006 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_007 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_008 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_009 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_010 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_011 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_012 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_013 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_014 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_015 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_016 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_017 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_018 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_019 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_020 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_021 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_022 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_023 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_024 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_025 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_026 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_027 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_028 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_029 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_030 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_031 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_032 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_033 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_034 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_035 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_036 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_037 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_038 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_039 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_040 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_041 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_042 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_043 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_044 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_045 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_046 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_047 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_048 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_049 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_050 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_051 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_052 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_053 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_054 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_055 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_056 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_057 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_cs2_psu_phuket_2026_section_058 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### migrated_game_arena_of_valor_rov — game

- title: source needs factual review

### competition_competition_rules_tekken8_psu_esports — competition

- Time-sensitive content requires confirmed validity
- game_id: source needs factual review
- event_name: source needs factual review
- rulebook_release: source needs factual review
- coverage: required before publication

### competition_competition_rules_tekken8_psu_esports_section_001 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_tekken8_psu_esports_section_002 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_tekken8_psu_esports_section_003 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_tekken8_psu_esports_section_004 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_tekken8_psu_esports_section_005 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_tekken8_psu_esports_section_006 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_tekken8_psu_esports_section_007 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_tekken8_psu_esports_section_008 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026 — competition

- Time-sensitive content requires confirmed validity
- game_id: source needs factual review
- event_name: source needs factual review
- rulebook_release: source needs factual review
- coverage: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_001 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_002 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_003 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_004 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_005 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_006 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_007 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_008 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_009 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_010 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_011 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_012 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_013 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_014 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_015 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_016 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_017 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_018 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_019 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_020 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_021 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_022 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_023 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_024 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_025 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_valorant_psu_phuket_2026_section_026 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### controls_nintendo_animal_crossing_new_horizons — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_luigi_s_mansion_3 — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_mario_kart_8_deluxe — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### migrated_game_mario_kart_live_home_circuit — game

- title: source needs factual review

### controls_nintendo_mario_party_superstars — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_moving_out_2 — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_new_super_mario_bros_u_deluxe — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_nintendo_switch_sports — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_ring_fit_adventure — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_super_mario_odyssey — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_super_smash_bros_ultimate — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_nintendo_the_legend_of_zelda_breath_of_the_wild — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_pc_counter_strike_2 — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_pc_league_of_legends — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_pc_pubg_battlegrounds — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_pc_valorant — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_call_of_duty_modern_warfare_iii — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_call_of_duty_warzone — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_ea_sports_fc_24 — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_final_fantasy_xvi — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review
- limitations: English translation needs review or explicit machine-translation status

### controls_ps5_fortnite — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### migrated_game_god_of_war_ragnar_k — game

- title: source needs factual review

### controls_ps5_gran_turismo_7 — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_hogwarts_legacy — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_it_takes_two — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_little_nightmares_ii — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_marvel_s_spider_man_2 — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_monster_hunter_rise — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_naruto_x_boruto_ultimate_ninja_storm_connections — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_overcooked — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### migrated_game_resident_evil_4_remake — game

- title: source needs factual review

### controls_ps5_resident_evil_village — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_tekken_8 — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_the_last_of_us_part_i — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### migrated_game_the_last_of_us_part_ii — game

- title: source needs factual review

### controls_ps5_uncharted_legacy_of_thieves_collection — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_vr_beat_saber — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_vr_horizon_call_of_the_mountain — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### migrated_faq_curated_booking_no_edit — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_booking_non_transferable — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_booking_steps — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_cancel_1_hour — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_checkin_30_minutes — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_checkin_id_required — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_checkin_late_cancel — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_contact_email — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_contact_facebook — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_contact_location — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_contact_phone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_damage_minor — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_damage_moderate — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_damage_severe — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_games_pc — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_games_popular — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_games_ps5 — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_games_switch — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_games_vr — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_overview_identity — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_overview_mission — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_payment_10_minutes — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_payment_bank — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_penalty_appeal — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_penalty_temp_suspension — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_penalty_warning_suspension — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_refund_policy — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_advance_time — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_max_sessions — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_belongings — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_food_drinks — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_lost_items — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_move_equipment — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_noise_language — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_power_outlet — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_return_equipment — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_smoking_alcohol_drugs — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_weapons_gambling — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_schedule_afternoon — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_schedule_morning — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_time_change_policy — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_user_info_required — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### member_0629f0033d3d9b24 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_17d23bd43ffdcfb0 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_18a751d710b9b30c — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_1d37816f5d904797 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_1d884f11f3890dea — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_2035485e1198bd6d — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_453ecaf47e840388 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_4e005eeca4b538a1 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_68e4915433f294b7 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_704fe601a50d54d0 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_832e24bbcd11737e — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_930bf12e4f38f6ff — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_9e9cb3b178e5d76c — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_a19d2197ce8e1a38 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_a2e050f57fcf6d7a — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_a69fd942fc2537c2 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_acb83e6fddde5334 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_b71d33c7b6468ebc — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_b898853273feb841 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_bf43feb569776b8b — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_c0944fdade08a06c — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_ce4590ddc09c0f4e — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_d7fc7da21ef72803 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_df4264b9c7e37a23 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### member_f90051b3c68e16b4 — person

- display_name: source needs factual review
- role: source needs factual review
- team: source needs factual review
- public_scope: required before publication

### equipment_driving_force_shifter — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_gaming_chair — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_gaming_headset — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_gaming_keyboard — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_gaming_monitor — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_gaming_mouse — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_gaming_pc — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_logitech_g923 — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_nintendo_switch_oled — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_playstation_5_slim — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_pulse_elite_headset — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_racezone_cockpit_v3 — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_sofa_2_seats — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_sony_playstation_vr2 — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_tv_65 — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### equipment_tv_86 — equipment_model

- name: source needs factual review
- device_type: required before publication
- specifications: source needs factual review
- usage: source needs factual review

### migrated_faq_rule_cockpit_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_cockpit_gran_turismo — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_contact_email — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_contact_facebook — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_contact_location — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_contact_phone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_damage_responsibility — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_contact_location_question — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_contact_methods — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_damage_responsibility_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_food_drink_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_general_damage_penalties — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_general_studio_rules — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_overview_operator — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_report_problem_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_en_smoking_alcohol_natural — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_equipment_pc_zone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_food_drink — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_lost_personal_items — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_minor_damage — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_mixed_food_noise_damage — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_mixed_lost_and_damage — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_moderate_damage — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_noise_language — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_overview_founder — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_overview_identity — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_overview_mission — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_pc_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_pc_specific_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_penalty_temp_suspension — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_ps5_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_ps5_specific_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_report_problem — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_return_equipment_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_severe_damage — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_smoking_alcohol — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_switch_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_switch_specific_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_vr_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_vr_specific_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_rule_weapons_gambling — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### schedule_closure_2026-07-28 — closure

- local_date: source needs factual review
- zone_ids: required before publication
- state: source needs factual review
- reason: source needs factual review

### schedule_closure_2026-07-29 — closure

- local_date: source needs factual review
- zone_ids: required before publication
- state: source needs factual review
- reason: source needs factual review

### schedule_closure_2026-07-30 — closure

- local_date: source needs factual review
- zone_ids: required before publication
- state: source needs factual review
- reason: source needs factual review

### migrated_faq_curated_service_fee_2026_full_table — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_user_group_alias_general_adult — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_user_group_alias_general_student — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_user_group_alias_psu_student_staff — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_home_equipment_pc_zone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_home_equipment_cockpit_zone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_home_equipment_nintendo_zone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_home_equipment_ps5_zone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_home_equipment_vr_zone — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_home_popular_games_list — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_games_cockpit — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_service_nintendo_capacity — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_service_pc_duration — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_service_vr_duration — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_service_cockpit_game — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_service_ps5_duration — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_schedule_monday_morning — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_schedule_friday_maintenance — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_reservation_cancel_invalid_info — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_trash_personal_items — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_report_problem — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_rule_cleanliness — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_penalty_permanent_suspension — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_penalty_violation_record — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_penalty_booking_suspension — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_knowledge_esports_definition — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_knowledge_esports_origin — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_knowledge_esports_categories — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_knowledge_current_popular_games — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_knowledge_esports_careers — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_knowledge_overcooked2_skills — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_knowledge_naruto_connections_summary — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_news_cs2_2026 — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_news_valorant_2026 — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_news_surat_smash_tekken8 — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_news_chinese_students_game_based_learning — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_news_game_on_thaimuang — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_about_members_president — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_about_members_dean — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_about_members_manager — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_about_members_club_president — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_about_gallery_categories — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_service_fee_pc_unknown — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_service_fee_ps5_rates — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_service_fee_nintendo_1_2_rates — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_service_fee_nintendo_3_4_rates — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_service_fee_cockpit_rates — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_service_fee_vr_30_rates — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_faq_curated_service_fee_vr_60_rates — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_university — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_membership — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_spectators — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_walk_in — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_location — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_map — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_parking — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_contact — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_four_people — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_player_identity — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_checkin_documents — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_change_machine — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_change_time — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_personal_keyboard_mouse — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_wrong_slip — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_combined_transfer — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_group_checkin — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_owner_claim_rest_seating — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_public_access_general — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_public_access_booking — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_public_access_booking_required — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_public_access_documents — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_public_access_membership — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_checkin_required_general — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_personal_power_general — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### migrated_policy_text_food_bring_general — faq

- question: source needs factual review
- answer: source needs factual review
- topic: source needs factual review

### audience_internal_org — audience

- name: source needs factual review
- eligibility: required before publication

### zone_all_zones — zone

- name: source needs factual review

### rental_all_zones_external_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review
- terms: source needs factual review

### rental_all_zones_external_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review
- terms: source needs factual review

### rental_all_zones_internal_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review
- terms: source needs factual review

### rental_all_zones_internal_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review
- terms: source needs factual review

### rental_cockpit_external_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_cockpit_external_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_cockpit_internal_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_cockpit_internal_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_vr_external_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_vr_external_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_vr_internal_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_vr_internal_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_nintendo_switch_external_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_nintendo_switch_external_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_nintendo_switch_internal_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_nintendo_switch_internal_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_ps5_external_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_ps5_external_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_ps5_internal_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_ps5_internal_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_pc_external_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_pc_internal_full_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### rental_pc_internal_half_day — rental_package

- Time-sensitive content requires confirmed validity
- name: source needs factual review
- zone_ids: source needs factual review
- audience_id: source needs factual review
- period_label: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- equipment_included: source needs factual review
- room_seats: source needs factual review

### audience_psu_student_staff — audience

- name: source needs factual review
- eligibility: required before publication

### audience_psu_alumni_general_student — audience

- name: source needs factual review
- eligibility: required before publication

### audience_general_adult — audience

- name: source needs factual review
- eligibility: required before publication

### migrated_rate_nintendo_switch_60_1_2_psu_student_staff — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_nintendo_switch_60_1_2_general_adult — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_nintendo_switch_60_3_4_psu_student_staff — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_nintendo_switch_60_3_4_general_adult — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_vr_30_1_5_psu_student_staff — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_vr_30_1_5_psu_alumni_general_student — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_vr_30_1_5_general_adult — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_vr_60_1_5_psu_student_staff — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_vr_60_1_5_psu_alumni_general_student — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_vr_60_1_5_general_adult — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_schedule_0 — schedule

- Time-sensitive content requires confirmed validity
- timezone: source needs factual review
- zone_ids: required before publication
- weekday: source needs factual review
- open_periods: required before publication
- open_periods: unresolved conflict
- open_periods: source needs factual review
- open_periods: source needs factual review
- bookable_periods: source needs factual review
- maintenance_periods: source needs factual review
- reason: source needs factual review

### migrated_schedule_1 — schedule

- Time-sensitive content requires confirmed validity
- timezone: source needs factual review
- zone_ids: required before publication
- weekday: source needs factual review
- open_periods: required before publication
- open_periods: unresolved conflict
- open_periods: source needs factual review
- open_periods: source needs factual review
- bookable_periods: source needs factual review
- maintenance_periods: source needs factual review

### migrated_schedule_2 — schedule

- Time-sensitive content requires confirmed validity
- timezone: source needs factual review
- zone_ids: required before publication
- weekday: source needs factual review
- open_periods: required before publication
- open_periods: unresolved conflict
- open_periods: source needs factual review
- open_periods: source needs factual review
- bookable_periods: source needs factual review
- maintenance_periods: source needs factual review

### migrated_schedule_3 — schedule

- Time-sensitive content requires confirmed validity
- timezone: source needs factual review
- zone_ids: required before publication
- weekday: source needs factual review
- open_periods: required before publication
- open_periods: unresolved conflict
- open_periods: source needs factual review
- open_periods: source needs factual review
- bookable_periods: source needs factual review
- maintenance_periods: source needs factual review

### migrated_schedule_4 — schedule

- Time-sensitive content requires confirmed validity
- timezone: source needs factual review
- zone_ids: required before publication
- weekday: source needs factual review
- open_periods: required before publication
- open_periods: unresolved conflict
- open_periods: source needs factual review
- open_periods: source needs factual review
- bookable_periods: source needs factual review
- maintenance_periods: source needs factual review
- reason: source needs factual review

### migrated_schedule_5 — schedule

- Time-sensitive content requires confirmed validity
- timezone: source needs factual review
- zone_ids: required before publication
- weekday: source needs factual review
- open_periods: source needs factual review
- bookable_periods: source needs factual review
- maintenance_periods: source needs factual review
- reason: source needs factual review

### migrated_schedule_6 — schedule

- Time-sensitive content requires confirmed validity
- timezone: source needs factual review
- zone_ids: required before publication
- weekday: source needs factual review
- open_periods: source needs factual review
- bookable_periods: source needs factual review
- maintenance_periods: source needs factual review
- reason: source needs factual review

### availability_cockpit_01_02 — service

- name: source needs factual review
- resource_ids: source needs factual review
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_link_availability_cockpit_01_02_game_detail_gran_turismo_7 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### availability_pc_01_02 — service

- name: source needs factual review
- resource_ids: source needs factual review
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_link_availability_pc_01_02_game_detail_tekken_8 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_01_02_game_detail_cs2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_01_02_game_detail_league_of_legends — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_01_02_game_detail_pubg — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_01_02_game_detail_valorant — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### availability_pc_03_10 — service

- name: source needs factual review
- resource_ids: source needs factual review
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_link_availability_pc_03_10_game_detail_warzone — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_03_10_game_detail_cs2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_03_10_game_detail_league_of_legends — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_03_10_game_detail_pubg — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_pc_03_10_game_detail_valorant — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### availability_ps5_01_02 — service

- name: source needs factual review
- resource_ids: source needs factual review
- platform: source needs factual review
- session_minutes: source needs factual review
- occupancy_minutes: required before publication
- capacity_min: source needs factual review
- capacity_max: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_call_of_duty_mw3 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_migrated_game_delta_force — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_ea_sports_fc_24 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_migrated_game_efootball — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_final_fantasy_xvi — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_fortnite — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_god_of_war_ragnarok — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_hogwarts_legacy — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_spider_man_2 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_naruto_x_boruto — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_resident_evil_4 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_resident_evil_village — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_tekken_8 — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_migrated_game_the_finals — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_migrated_game_the_last_of_us_part_i — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_migrated_game_the_last_of_us_part_ii_remastered — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### migrated_link_availability_ps5_01_02_game_detail_uncharted — game_service

- game_id: source needs factual review
- service_id: source needs factual review
- offered: source needs factual review
- installed_resource_ids: source needs factual review

### competition_competition_rules_rov_blueket_2025_men — competition

- Time-sensitive content requires confirmed validity
- game_id: source needs factual review
- event_name: source needs factual review
- rulebook_release: source needs factual review
- coverage: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_001 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_002 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_003 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_004 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_005 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_006 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_007 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_008 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_009 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_010 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_011 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### competition_competition_rules_rov_blueket_2025_men_section_012 — competition_rule

- Time-sensitive content requires confirmed validity
- competition_id: source needs factual review
- section_number: source needs factual review
- facet: required before publication
- heading: source needs factual review
- text: source needs factual review
- completeness: required before publication

### controls_nintendo_mario_kart_live_home_circuit — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_god_of_war_ragnar_k — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### controls_ps5_resident_evil_4_remake — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review
- limitations: English translation needs review or explicit machine-translation status

### controls_ps5_the_last_of_us_part_ii — control_set

- game_id: source needs factual review
- platform: source needs factual review
- input_device: required before publication
- preset: required before publication
- bindings: required before publication
- limitations: source needs factual review

### migrated_rate_playstation_5_60_1_2_psu_student_staff — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_playstation_5_60_1_2_psu_alumni_general_student — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_playstation_5_60_1_2_general_adult — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_cockpit_60_1_1_psu_student_staff — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_cockpit_60_1_1_psu_alumni_general_student — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### migrated_rate_cockpit_60_1_1_general_adult — rate

- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: required before publication
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: required before publication

### rate_recovered_pc_availability_pc_01_02_psu_student_staff — rate

- Time-sensitive content requires confirmed validity
- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: source needs factual review
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: source needs factual review

### rate_recovered_pc_availability_pc_01_02_general_student — rate

- Time-sensitive content requires confirmed validity
- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: source needs factual review
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: source needs factual review

### rate_recovered_pc_availability_pc_01_02_general_adult — rate

- Time-sensitive content requires confirmed validity
- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: source needs factual review
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: source needs factual review

### rate_recovered_pc_availability_pc_03_10_psu_student_staff — rate

- Time-sensitive content requires confirmed validity
- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: source needs factual review
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: source needs factual review

### rate_recovered_pc_availability_pc_03_10_general_student — rate

- Time-sensitive content requires confirmed validity
- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: source needs factual review
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: source needs factual review

### rate_recovered_pc_availability_pc_03_10_general_adult — rate

- Time-sensitive content requires confirmed validity
- service_id: source needs factual review
- audience_id: source needs factual review
- amount_minor: source needs factual review
- currency: source needs factual review
- unit: source needs factual review
- duration_minutes: source needs factual review
- persons_min: source needs factual review
- persons_max: source needs factual review
- calculation_rule: source needs factual review

