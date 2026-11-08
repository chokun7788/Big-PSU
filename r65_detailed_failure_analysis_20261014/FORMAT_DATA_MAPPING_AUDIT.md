# ตรวจโครงสร้างข้อมูลที่ย้ายทุกkind

นับheadที่อ่านจริงในR64 ไม่ใช่จำนวนpreparedrecords/revisionsในรายงานรอบก่อน

| kind | records | knownfields | unknownfields | conflictedfields |
|---|---:|---:|---:|---:|
| audience | 5 | 5 | 10 | 0 |
| center | 1 | 5 | 3 | 0 |
| closure | 3 | 9 | 12 | 0 |
| competition | 4 | 12 | 16 | 0 |
| competition_rule | 104 | 416 | 312 | 0 |
| control_set | 38 | 114 | 152 | 0 |
| equipment_model | 16 | 48 | 16 | 0 |
| faq | 190 | 570 | 380 | 0 |
| game | 48 | 156 | 228 | 0 |
| game_service | 70 | 238 | 182 | 0 |
| person | 25 | 75 | 50 | 0 |
| policy | 1 | 4 | 4 | 0 |
| rate | 18 | 126 | 54 | 0 |
| rental_package | 24 | 196 | 44 | 0 |
| resource | 14 | 56 | 28 | 0 |
| schedule | 7 | 15 | 24 | 10 |
| service | 8 | 44 | 20 | 0 |
| zone | 6 | 6 | 18 | 0 |

## competition_rule: แต่ละfield

| field | สถานะ/จำนวน |
|---|---|
| competition_id | known=104 |
| completeness | unknown=104 |
| depends_on_ids | unknown=104 |
| facet | unknown=104 |
| heading | known=104 |
| section_number | known=104 |
| text | known=104 |

## control_set: แต่ละfield

| field | สถานะ/จำนวน |
|---|---|
| bindings | unknown=38 |
| game_id | known=38 |
| game_version | unknown=38 |
| input_device | unknown=38 |
| limitations | known=38 |
| platform | known=38 |
| preset | unknown=38 |

## rate: แต่ละfield

| field | สถานะ/จำนวน |
|---|---|
| amount_minor | known=18 |
| audience_id | known=18 |
| calculation_rule | unknown=18 |
| currency | known=18 |
| duration_minutes | known=18 |
| persons_max | known=18 |
| persons_min | known=18 |
| service_id | known=18 |
| tax_note | unknown=18 |
| unit | unknown=18 |

## schedule: แต่ละfield

| field | สถานะ/จำนวน |
|---|---|
| bookable_periods | conflicted=5; known=2 |
| maintenance_periods | unknown=7 |
| open_periods | conflicted=5; known=2 |
| reason | known=4; unknown=3 |
| timezone | unknown=7 |
| weekday | known=7 |
| zone_ids | unknown=7 |

## game_service: แต่ละfield

| field | สถานะ/จำนวน |
|---|---|
| account_policy_id | unknown=70 |
| game_id | known=70 |
| game_version | unknown=70 |
| installed_resource_ids | unknown=42; known=28 |
| offered | known=70 |
| service_id | known=70 |

## CS2 → service → rate: graphที่ตรวจจากข้อมูลจริง

```json
[
  {
    "game": "game_detail_cs2",
    "game_service_links": [
      {
        "id": "migrated_link_availability_pc_01_02_game_detail_cs2",
        "offered": true,
        "service": "availability_pc_01_02",
        "rates": 0
      },
      {
        "id": "migrated_link_availability_pc_03_10_game_detail_cs2",
        "offered": true,
        "service": "availability_pc_03_10",
        "rates": 0
      }
    ]
  }
]
```

graphนี้พิสูจน์ว่ามีgame_serviceที่offered=trueแต่ต่อไปserviceIDที่ไม่มีrate ไม่ได้พิสูจน์ว่าศูนย์ไม่มีราคาPCจริง ต้องแปลงเส้นเชื่อมbilling/bookingจากsourceเดิมให้ถูก
