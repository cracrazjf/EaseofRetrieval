# 材料验证清单（自动生成，勿手改；改材料后重跑 `python3 src/make_review_sheet.py`）

一张表看完所有需要人工判断的地方。脚本已把住的（词数/禁词/条目数/溯源有效性/≥2源）不在此列。


## A. 优缺点权衡对（共 0 处，其中 **0 处需你判断**）

同一事实字段同时支撑一优一缺。判断标准：**权衡**（同一属性的两面，保留）还是**同说法重述**（把同一句话正反说一遍，应改掉其中一条）。

### A1. 需判断（0 处）——优缺点措辞高度重叠

| ✓ | 提示 | 物品 | 字段 | 优点 | 缺点 |
|---|---|---|---|---|---|

<details><summary>A2. 已判定为正常权衡（0 处，抽查即可）</summary>

| 物品 | 字段 | 优点 | 缺点 |
|---|---|---|---|

</details>

## B. 说明书中未在事实表出现的数字（20 个物品）

说明书里的数字应当能在 facts.csv 找到对应。下列数字未匹配——多为拼写形式差异（如 `9-1/2` vs `9.5`）或转述单位，**请确认不是凭空写入的事实**。

| ✓ | 物品 | 未匹配的数字 |
|---|---|---|
| ☐ | c01_espresso_real | 65, 685 |
| ☐ | c02_airfryer_fict | 5 |
| ☐ | c03_ricecooker_fict | 6 |
| ☐ | c04_blender_fict | 5 |
| ☐ | c04_blender_real | 30, 310, 60 |
| ☐ | c07_airpurifier_fict | 2 |
| ☐ | c07_airpurifier_real | 300 |
| ☐ | c08_humidifier_real | 350 |
| ☐ | c09_standingdesk_fict | 2 |
| ☐ | c09_standingdesk_real | 7 |
| ☐ | c11_projector_fict | 4 |
| ☐ | c12_headphones_real | 1000, 4 |
| ☐ | c13_ereader_fict | 2 |
| ☐ | c14_keyboard_real | 2 |
| ☐ | c15_powerbank_fict | 10 |
| ☐ | c15_powerbank_real | 10 |
| ☐ | c16_sportwatch_fict | 40 |
| ☐ | c16_sportwatch_real | 55 |
| ☐ | c26_toothbrush_fict | 230 |
| ☐ | c26_toothbrush_real | 1000 |

## C. 虚构物品的差异点（26 个）

**判断标准：是功能差异（有无某特性、布局不同）还是品质差异（更差的版本）**。品质差异会让 real/fictional 对比混入优劣，必须改。

| ✓ | 物品 | 名称 | 声明的差异点 | facts.csv 中标记的差异字段 |
|---|---|---|---|---|
| ☐ | c01_espresso_fict | Vestrino M2 | no ESE pod support / two buttons plus steam dial / no top cup rest | `controls, baskets, no_cuprest, portafilter_size, hardness_strip, no_ese, steam_dial` |
| ☐ | c02_airfryer_fict | Farnholt A5 | no app or wireless control (dial and button panel only) / round basket instead of square / 8 presets instead of 12 | `capacity, presets, controls` |
| ☐ | c03_ricecooker_fict | Hamura GR-6 | no delay timer / seven menu settings instead of eleven / monochrome LCD instead of colored panel | `menus, no_timer, controls, no_extended_warm` |
| ☐ | c04_blender_fict | Quarvel BX5 | preset program buttons instead of pulse-only control / 64-ounce container instead of 48 / no tamper included | `container, controls, accessories, programs, no_pulse` |
| ☐ | c05_kettle_fict | Tessro Kettle | preset temperature buttons instead of to-the-degree dial / 1.2 L capacity instead of 0.9 L / no scheduling or stopwatch functions | `capacity, temp_range, functions, no_schedule, no_stopwatch` |
| ☐ | c06_robovac_fict | Orvia Petrel | no self-emptying base / gyroscope navigation instead of camera mapping / single side brush instead of dual rubber brushes | `navigation, mapping, brushes, dock, no_voice, no_camera` |
| ☐ | c07_airpurifier_fict | Arvelia A2 | air quality sensor with auto mode / rectangular tower body instead of cylinder / no timer function | `dimensions, sensor, modes, no_timer` |
| ☐ | c08_humidifier_fict | Halvira H1 | ultrasonic mist instead of evaporative wick / built-in humidistat with target setting / top-fill opening instead of removable tank | `type, humidistat, fill, quiet_run` |
| ☐ | c09_standingdesk_fict | Ostreno D2 | single motor instead of dual / two memory presets instead of four / no anti-collision sensing | `motors, no_anticollision, two_presets` |
| ☐ | c10_chair_fict | Tarnwell C1 | fixed-height arms instead of 4D arms / manual tension knob instead of weight-activated recline / no seat depth adjustment | `no_seat_depth, recline, arms, no_headrest` |
| ☐ | c11_projector_fict | Previk PJ4 | internal battery for cordless playback / 1080p resolution instead of 720p / manual focus ring instead of auto focus | `resolution, battery, focus, storage` |
| ☐ | c12_headphones_fict | Wrenfeld NX40 | physical buttons instead of touch controls / IPX4 splash resistance / no multipoint pairing | `bluetooth, controls, water, no_app` |
| ☐ | c13_ereader_fict | Lireon Q2 | physical page-turn buttons on the bezel / 7 inch screen instead of 6 / no water resistance rating | `display, buttons, no_water, no_library` |
| ☐ | c14_keyboard_fict | Kelvane Slate 65 | 65 percent layout without a function row / PBT keycaps instead of ABS / wired only, no wireless | `layout, keycaps, connectivity, no_software` |
| ☐ | c15_powerbank_fict | Ardento PB10 | integrated cable attached to the housing / digital percentage display instead of LED lights / single USB-C port with no USB-A | `ports, integrated_cable, display, no_low_current` |
| ☐ | c16_sportwatch_fict | Veltrun R40 | barometric altimeter included / button-only controls with no touchscreen / no third-party phone app pairing | `sensors, controls, connectivity, altimeter` |
| ☐ | c17_budgetapp_fict | Voskell | envelope method with rollover instead of zero-based assignment / manual CSV import instead of bank linking / free tier with limited categories | `method, import, free_tier` |
| ☐ | c18_notesapp_fict | Trelbin | local-first storage with optional sync instead of cloud workspaces / outline documents instead of block databases / no guest sharing | `structure, storage, no_guests, no_web, file_format` |
| ☐ | c19_passwordmgr_fict | Cryptavo | local vault file with user-managed sync instead of hosted sync / hardware key required for unlock / no browser extensions, desktop and mobile only | `storage, unlock, no_extensions, no_autofill, no_account` |
| ☐ | c20_langapp_fict | Quenlo | spaced repetition scheduling instead of streak-based lessons / twelve languages instead of forty / no free tier beyond a trial | `courses, method, trial` |
| ☐ | c21_focusapp_fict | Stillbrook | ambient scene that fills in rather than a tree that dies / no group sessions / desktop-first with no phone blocking | `mechanic, blocking, no_group, no_account, no_realtree, no_schedule` |
| ☐ | c22_backpack_fict | Cendric Ridge 28 | roll-top closure instead of a zippered lid / 28 litre volume instead of 22 / single size with an adjustable torso strap | `volume, closure, suspension, no_rain_cover` |
| ☐ | c23_tent_fict | Torvik Basin 2 | single vestibule and one door instead of two / semi-freestanding, requiring stakes at the foot / integrated footprint included | `capacity, vestibule, doors, footprint, no_gutters` |
| ☐ | c24_bottle_fict | Tavro Flask | screw-off cap with no pour-through stopper / 20 oz capacity instead of 16 / carry loop instead of a side handle | `capacity, stopper, exterior, loop, no_cupholder` |
| ☐ | c25_stove_fict | Fyrren S1 | fixed pot supports that fold rather than detach / no built-in igniter / remote canister feed with a hose | `no_igniter, supports, remote_feed, low_stance, inverted_use` |
| ☐ | c26_toothbrush_fict | Dovrell 230 | sonic vibration instead of oscillating rotation / travel case included / USB charging instead of an induction stand | `action, charging, case, quiet, battery_indicator, soft_start` |

## D. 来源质量提示（共 59 条，其中 **5 条需你判断**）

### D1. 需判断（5 条）——来源独立性或权威性存疑

| ✓ | 物品 | 字段 | 类型 | 详情 |
|---|---|---|---|---|
| ☐ | c02_airfryer_real | `(多个字段)` | official row on third-party host | manuals.plus |
| ☐ | c06_robovac_real | `(多个字段)` | official row on third-party host | manua.ls |
| ☐ | c20_langapp_real | `(多个字段)` | official row on third-party host | apps.apple.com |
| ☐ | c22_backpack_real | `(多个字段)` | official row on third-party host | outdoorsports.com |
| ☐ | c23_tent_real | `(多个字段)` | official row on third-party host | cascadedesigns.com |

<details><summary>D2. 已在 note 中记录的矛盾与回避（54 条，抽查即可）</summary>

| 物品 | 字段 | note |
|---|---|---|
| c01_espresso_real | `cup_height` | US page says 13 cm; EN structured spec table taken; discrepancy recorded |
| c02_airfryer_real | `dimensions` | manual mirrors differ slightly on dims; official page lacks a spec table; discrepancy recorded |
| c02_airfryer_real | `footprint_con` | con; sibling-model coverage caveat |
| c02_airfryer_real | `preheat_speed` | praise claim; sibling-model coverage caveat |
| c03_ricecooker_real | `weight` | omitted from spec sheet |
| c06_robovac_real | `battery` | batch discrepancy: some listings claim 120 min runtime; 75 min taken; verify before freeze; also grounds runti |
| c06_robovac_real | `dustbin` | batch discrepancy: 0.4 vs 0.3 L across listings; 0.4 taken; verify before freeze; also grounds frequent-emptyi |
| c06_robovac_real | `noise_con` | con; spec claims 58 dB vs 65-68 measured; discrepancy recorded; noise kept out of spec sheet |
| c06_robovac_real | `bags_con` | con; batch also flags price, omitted per no-price rule |
| c08_humidifier_real | `noise_high` | con; same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c08_humidifier_real | `filter_cost` | con; same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c08_humidifier_real | `wick_mold` | con; same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c08_humidifier_real | `basic_controls` | con; same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c08_humidifier_real | `clean_ease` | same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c08_humidifier_real | `no_dust` | same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c08_humidifier_real | `humidify_rate` | measured performance; same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c08_humidifier_real | `self_regulating` | same publisher caveat: techgearlab and babygearlab share one publisher (GearLab) |
| c09_standingdesk_real | `height_range` | conflict: one source lists 48.8 in max; 48.4 taken; verify before freeze |
| c09_standingdesk_real | `warranty` | conflict: one source lists a 5/5/2 year split; verify before freeze |
| c09_standingdesk_real | `no_app` | con; absence recorded from the official spec listing, which lists keypad control only; verify before freeze; r |
| c09_standingdesk_real | `frame_width` | flexispot.com 403s; value from search snippet of the official URL; verify before freeze |
| c10_chair_real | `seat_height` | con: range fixed at order; exact figures came from a partially extracted spec PDF and are kept out of the brie |
| c12_headphones_real | `weight` | official spec page reached only via search-index snapshot; direct fetch blocked (403); one review measured 251 |
| c12_headphones_real | `driver` | official spec page reached only via search-index snapshot; direct fetch blocked (403) |
| c12_headphones_real | `bluetooth` | official spec page reached only via search-index snapshot; direct fetch blocked (403) |
| c12_headphones_real | `frequency` | official spec page reached only via search-index snapshot; direct fetch blocked (403) |
| c12_headphones_real | `ldac` | official spec page reached only via search-index snapshot; direct fetch blocked (403) |
| c12_headphones_real | `multipoint` | official spec page reached only via search-index snapshot; direct fetch blocked (403) |
| c12_headphones_real | `frequency_ldac` | official spec page reached only via search-index snapshot; direct fetch blocked (403) |
| c15_powerbank_real | `output_a` | official text also appends 15 W max per port; internally inconsistent |
| c15_powerbank_real | `dimensions` | official pages do not state dimensions or weight; retailer figures conflict; deliberately absent from the brie |
| c17_budgetapp_real | `tier_note` | prices omitted per DECISIONS |
| c18_notesapp_real | `tiers` | prices omitted per DECISIONS |
| c19_passwordmgr_real | `paid_tier` | tier is named Premium officially; renamed to paid tier in materials because the brand word is on the banned ev |
| c20_langapp_real | `paid_tier` | prices vary by region and platform; omitted per DECISIONS |
| c21_focusapp_fict | `paid_tier` | prices omitted per DECISIONS |
| c22_backpack_real | `volume` | official specs mirrored by an authorized retailer; osprey.com blocked automated access |
| c22_backpack_real | `weight` | one review measured 38.4 oz; discrepancy recorded |
| c22_backpack_real | `dimensions` | same source caveat |
| c22_backpack_real | `main_fabric` | same source caveat |
| c22_backpack_real | `attachments` | same source caveat |
| c22_backpack_real | `pockets` | same source caveat |
| c23_tent_real | `capacity` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures |
| c23_tent_real | `packed_weight` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures; con |
| c23_tent_real | `floor` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures |
| c23_tent_real | `peak_height` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures; 2022 version lis |
| c23_tent_real | `doors` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures |
| c23_tent_real | `rainfly` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures; con |
| c23_tent_real | `poles` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures; 2022 version use |
| c23_tent_real | `accessories` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures |
| c23_tent_real | `floor_width` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures; con |
| c23_tent_real | `min_weight_basis` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures; con |
| c23_tent_real | `no_gear_loft` | NX generation specs used per DECISIONS; renamed Hubba Hubba 2 in 2022 with different figures; gear loft sold a |
| c26_toothbrush_real | `modes` | official page states three modes; earlier production units shipped with one; mid-cycle refresh; omitted per DE |

</details>

## E. 逐物品签字表

| ✓ | 物品 | 名称 | 类型 | 事实行 | 官方 | 评测共识 |
|---|---|---|---|---|---|---|
| ☐ | c01_espresso_fict | Vestrino M2 | fictional | 29 | 0 | 0 |
| ☐ | c01_espresso_real | De'Longhi Dedica EC685 | real | 35 | 22 | 10 |
| ☐ | c02_airfryer_fict | Farnholt A5 | fictional | 21 | 0 | 0 |
| ☐ | c02_airfryer_real | Cosori Pro II 5.8QT | real | 22 | 11 | 5 |
| ☐ | c03_ricecooker_fict | Hamura GR-6 | fictional | 22 | 0 | 0 |
| ☐ | c03_ricecooker_real | Zojirushi NS-ZCC10 | real | 27 | 15 | 7 |
| ☐ | c04_blender_fict | Quarvel BX5 | fictional | 24 | 0 | 0 |
| ☐ | c04_blender_real | Vitamix E310 | real | 22 | 11 | 7 |
| ☐ | c05_kettle_fict | Tessro Kettle | fictional | 21 | 0 | 0 |
| ☐ | c05_kettle_real | Fellow Stagg EKG | real | 27 | 15 | 6 |
| ☐ | c06_robovac_fict | Orvia Petrel | fictional | 25 | 0 | 0 |
| ☐ | c06_robovac_real | iRobot Roomba i7 | real | 25 | 15 | 7 |
| ☐ | c07_airpurifier_fict | Arvelia A2 | fictional | 22 | 0 | 0 |
| ☐ | c07_airpurifier_real | Levoit Core 300 | real | 26 | 16 | 8 |
| ☐ | c08_humidifier_fict | Halvira H1 | fictional | 24 | 0 | 0 |
| ☐ | c08_humidifier_real | Honeywell HCM-350 | real | 24 | 14 | 8 |
| ☐ | c09_standingdesk_fict | Ostreno D2 | fictional | 27 | 0 | 0 |
| ☐ | c09_standingdesk_real | FlexiSpot E7 | real | 28 | 14 | 11 |
| ☐ | c10_chair_fict | Tarnwell C1 | fictional | 27 | 0 | 0 |
| ☐ | c10_chair_real | Steelcase Series 1 | real | 27 | 19 | 7 |
| ☐ | c11_projector_fict | Previk PJ4 | fictional | 30 | 0 | 0 |
| ☐ | c11_projector_real | XGIMI MoGo 2 | real | 30 | 24 | 6 |
| ☐ | c12_headphones_fict | Wrenfeld NX40 | fictional | 25 | 0 | 0 |
| ☐ | c12_headphones_real | Sony WH-1000XM4 | real | 28 | 17 | 8 |
| ☐ | c13_ereader_fict | Lireon Q2 | fictional | 24 | 0 | 0 |
| ☐ | c13_ereader_real | Kobo Clara 2E | real | 28 | 19 | 7 |
| ☐ | c14_keyboard_fict | Kelvane Slate 65 | fictional | 24 | 0 | 0 |
| ☐ | c14_keyboard_real | Keychron K2 | real | 28 | 22 | 5 |
| ☐ | c15_powerbank_fict | Ardento PB10 | fictional | 24 | 0 | 0 |
| ☐ | c15_powerbank_real | Belkin BoostCharge 10K | real | 24 | 19 | 4 |
| ☐ | c16_sportwatch_fict | Veltrun R40 | fictional | 29 | 0 | 0 |
| ☐ | c16_sportwatch_real | Garmin Forerunner 55 | real | 24 | 16 | 8 |
| ☐ | c17_budgetapp_fict | Voskell | fictional | 25 | 0 | 0 |
| ☐ | c17_budgetapp_real | YNAB | real | 24 | 16 | 8 |
| ☐ | c18_notesapp_fict | Trelbin | fictional | 22 | 0 | 0 |
| ☐ | c18_notesapp_real | Notion | real | 21 | 14 | 7 |
| ☐ | c19_passwordmgr_fict | Cryptavo | fictional | 22 | 0 | 0 |
| ☐ | c19_passwordmgr_real | Bitwarden | real | 25 | 19 | 6 |
| ☐ | c20_langapp_fict | Quenlo | fictional | 22 | 0 | 0 |
| ☐ | c20_langapp_real | Duolingo | real | 24 | 15 | 9 |
| ☐ | c21_focusapp_fict | Stillbrook | fictional | 22 | 0 | 0 |
| ☐ | c21_focusapp_real | Forest | real | 25 | 15 | 5 |
| ☐ | c22_backpack_fict | Cendric Ridge 28 | fictional | 23 | 0 | 0 |
| ☐ | c22_backpack_real | Osprey Talon 22 | real | 26 | 15 | 9 |
| ☐ | c23_tent_fict | Torvik Basin 2 | fictional | 23 | 0 | 0 |
| ☐ | c23_tent_real | MSR Hubba Hubba NX | real | 22 | 16 | 6 |
| ☐ | c24_bottle_fict | Tavro Flask | fictional | 26 | 0 | 0 |
| ☐ | c24_bottle_real | Thermos Stainless King | real | 24 | 16 | 6 |
| ☐ | c25_stove_fict | Fyrren S1 | fictional | 22 | 0 | 0 |
| ☐ | c25_stove_real | SOTO WindMaster | real | 23 | 15 | 8 |
| ☐ | c26_toothbrush_fict | Dovrell 230 | fictional | 23 | 0 | 0 |
| ☐ | c26_toothbrush_real | Oral-B Pro 1000 | real | 24 | 17 | 7 |
