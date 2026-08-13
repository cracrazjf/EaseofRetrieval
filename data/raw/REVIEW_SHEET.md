# 材料验证清单（自动生成，勿手改；改材料后重跑 `python3 src/make_review_sheet.py`）

一张表看完所有需要人工判断的地方。脚本已把住的（词数/禁词/条目数/溯源有效性/≥2源）不在此列。


## A. 优缺点权衡对（共 117 处，其中 **56 处需你判断**）

同一事实字段同时支撑一优一缺。判断标准：**权衡**（同一属性的两面，保留）还是**同说法重述**（把同一句话正反说一遍，应改掉其中一条）。

### A1. 需判断（56 处）——优缺点措辞高度重叠

| ✓ | 提示 | 物品 | 字段 | 优点 | 缺点 |
|---|---|---|---|---|---|
| ☐ | · 部分重叠 | c01_espresso_fict | `tank` | p03 Removable 1.0-liter tank with level indicator | n01 Small 1.0-liter tank needs frequent refills |
| ☐ | · 部分重叠 | c01_espresso_fict | `baskets` | p11 Pressurized baskets suit pre-ground coffee | n02 No grinder requires separately ground coffee |
| ☐ | ⚠ 同说法重述 | c04_blender_fict | `weight` | p09 Weight of 11.2 pounds anchors base | n08 Weight of 11.2 pounds when moving |
| ☐ | · 部分重叠 | c04_blender_real | `controls` | p10 Speed dial for gradual control | n06 No preset programs on the dial |
| ☐ | ⚠ 同说法重述 | c04_blender_real | `cord` | p11 Cord length of 4.5 feet | n07 Cord limits placement to 4.5 feet |
| ☐ | · 部分重叠 | c05_kettle_real | `controls` | p04 Full-color screen with dial control | n08 Screen and dial add setup steps |
| ☐ | ⚠ 同说法重述 | c06_robovac_fict | `brushes` | p12 Side brush reaches along edges | n08 Single side brush along edges |
| ☐ | ⚠ 同说法重述 | c07_airpurifier_fict | `coverage` | p11 Coverage of 960 square feet hourly | n08 Coverage of 200 square feet at 4.8 |
| ☐ | · 部分重叠 | c07_airpurifier_real | `dimensions` | p10 Footprint under nine inches square | n08 Height of 14.2 inches on floors |
| ☐ | · 部分重叠 | c08_humidifier_fict | `dimensions` | p10 Footprint under eleven inches wide | n06 Height of 13.8 inches on tables |
| ☐ | ⚠ 同说法重述 | c08_humidifier_fict | `warranty` | p11 Two year limited warranty | n07 Warranty covers only two years |
| ☐ | ⚠ 同说法重述 | c08_humidifier_fict | `cartridge` | p07 Mineral cartridge included in reservoir | n08 Cartridge sits inside the reservoir |
| ☐ | · 部分重叠 | c08_humidifier_real | `tank` | p01 Tank of 1.1 gallons per fill | n06 Tank needs refilling every day |
| ☐ | ⚠ 同说法重述 | c09_standingdesk_fict | `noise` | p08 Sound under 55 decibels while moving | n07 Sound reaches 55 decibels in travel |
| ☐ | · 部分重叠 | c09_standingdesk_real | `speed` | p08 Travel speed near 1.5 inches per second | n06 Travel speed limits quick repositioning |
| ☐ | ⚠ 同说法重述 | c10_chair_fict | `warranty` | p07 Seven year warranty on parts | n07 Warranty covers parts for seven years |
| ☐ | · 部分重叠 | c10_chair_fict | `back` | p05 Knit mesh back over molded frame | n08 Mesh back needs periodic vacuuming |
| ☐ | ⚠ 同说法重述 | c10_chair_real | `seat_depth` | p04 Seat depth adjusting 2-1/4 inches | n05 Seat depth range only 2-1/4 inches |
| ☐ | · 部分重叠 | c11_projector_fict | `os` | p03 Storage of 32 gigabytes onboard | n08 Memory of 2 gigabytes for apps |
| ☐ | · 部分重叠 | c11_projector_real | `os` | p05 Android TV 11 with 16 gigabytes | n05 Storage limited to 16 gigabytes |
| ☐ | · 部分重叠 | c11_projector_real | `os` | p05 Android TV 11 with 16 gigabytes | n06 Memory of 2 gigabytes for apps |
| ☐ | · 部分重叠 | c12_headphones_fict | `battery_nc_on` | p01 Battery up to 26 hours canceling | n07 Battery shorter than 30 hour class |
| ☐ | · 部分重叠 | c12_headphones_real | `battery_nc_on` | p02 Battery up to 30 hours canceling | n05 Battery drops sharply using LDAC |
| ☐ | ⚠ 同说法重述 | c13_ereader_fict | `buttons` | p03 Physical page-turn buttons on bezel | n07 Buttons only on the left bezel |
| ☐ | · 部分重叠 | c13_ereader_real | `storage` | p04 Storage of 16 gigabytes onboard | n07 Storage fixed with no card slot |
| ☐ | ⚠ 同说法重述 | c13_ereader_real | `display` | p01 Screen at 300 pixels per inch | n08 Six-inch screen limits page area |
| ☐ | · 部分重叠 | c14_keyboard_fict | `switches` | p03 Hot-swappable sockets accept other switches | n08 Switches not included with board |
| ☐ | ⚠ 同说法重述 | c14_keyboard_real | `polling` | p09 Wired polling at 1000 hertz | n04 Wireless polling drops to 90 hertz |
| ☐ | ⚠ 同说法重述 | c14_keyboard_real | `battery` | p02 Battery lasting 240 hours unlit | n05 RGB backlight cuts battery to 72 hours |
| ☐ | · 部分重叠 | c14_keyboard_real | `backlight` | p07 Backlight with 18 selectable patterns | n08 Backlight brightness has four steps |
| ☐ | · 部分重叠 | c15_powerbank_fict | `dimensions` | p11 Footprint of 104 millimetres long | n07 Thickness of 25 millimetres in bags |
| ☐ | ⚠ 同说法重述 | c15_powerbank_real | `included` | p05 Cable included in the box | n04 Included cable only six inches |
| ☐ | ⚠ 同说法重述 | c15_powerbank_real | `indicators` | p04 Four indicator lights report charge | n08 Charge state shown by four lights |
| ☐ | ⚠ 同说法重述 | c16_sportwatch_fict | `weight` | p11 Weight of 41 grams on wrist | n07 Weight of 41 grams during sleep |
| ☐ | · 部分重叠 | c17_budgetapp_fict | `free_tier` | p02 Free tier covering ten envelopes | n07 Free tier limited to one account |
| ☐ | ⚠ 同说法重述 | c17_budgetapp_real | `sharing` | p03 Subscription covering up to six people | n08 Sharing capped at six people |
| ☐ | ⚠ 同说法重述 | c18_notesapp_fict | `storage` | p03 Optional encrypted sync between installations | n07 Sync is optional and separately enabled |
| ☐ | · 部分重叠 | c19_passwordmgr_fict | `export` | p07 Export as encrypted archive or CSV | n08 Plain CSV export leaves data unencrypted |
| ☐ | ⚠ 同说法重述 | c20_langapp_fict | `trial` | p09 Fourteen day trial on new accounts | n07 Trial lasts only fourteen days |
| ☐ | · 部分重叠 | c20_langapp_fict | `courses` | p04 Graded reading and listening tracks | n08 No math or music tracks |
| ☐ | · 部分重叠 | c20_langapp_fict | `courses` | p10 Twelve languages with matched tracks | n08 No math or music tracks |
| ☐ | ⚠ 同说法重述 | c20_langapp_real | `courses` | p01 Over 280 courses across languages | n08 Course depth varies across languages |
| ☐ | · 部分重叠 | c21_focusapp_fict | `blocking` | p03 Blocks desktop applications and websites | n07 Blocking applies to desktop only |
| ☐ | · 部分重叠 | c21_focusapp_fict | `paid_tier` | p08 Paid tier adds unlimited history | n08 Scene variants require the paid tier |
| ☐ | ⚠ 同说法重述 | c21_focusapp_fict | `paid_tier` | p11 Scene variants on the paid tier | n08 Scene variants require the paid tier |
| ☐ | · 部分重叠 | c22_backpack_fict | `closure` | p02 Roll top adjusts height to contents | n08 Pack height changes as contents shift |
| ☐ | ⚠ 同说法重述 | c23_tent_fict | `floor_fabric` | p11 Floor coated to 2500 millimetres | n08 Floor coating rated 2500 millimetres |
| ☐ | ⚠ 同说法重述 | c24_bottle_fict | `retention` | p02 Hot retention rated sixteen hours | n07 Retention shorter than eighteen hours |
| ☐ | ⚠ 同说法重述 | c24_bottle_fict | `retention` | p03 Cold retention rated twenty-two hours | n07 Retention shorter than eighteen hours |
| ☐ | ⚠ 同说法重述 | c24_bottle_real | `maintenance` | p09 Dishwasher safe on top rack | n07 Top rack only in dishwasher |
| ☐ | ⚠ 同说法重述 | c24_bottle_real | `weight` | p10 Weight of 0.9 pounds when filled | n08 Weight of 0.9 pounds empty |
| ☐ | ⚠ 同说法重述 | c25_stove_fict | `boil` | p10 Two cups boil in three minutes | n07 Boil time near three minutes |
| ☐ | · 部分重叠 | c25_stove_real | `burn_time` | p09 Runs 1.5 hours per canister | n07 Canister lasts about ninety minutes |
| ☐ | ⚠ 同说法重述 | c26_toothbrush_fict | `warranty` | p08 Two year warranty on handle | n07 Warranty covers only two years |
| ☐ | ⚠ 同说法重述 | c26_toothbrush_real | `box` | p10 Brush head supplied with handle | n06 Single brush head in box |
| ☐ | ⚠ 同说法重述 | c26_toothbrush_real | `warranty` | p08 Two year warranty on handle | n07 Warranty covers only two years |

<details><summary>A2. 已判定为正常权衡（61 处，抽查即可）</summary>

| 物品 | 字段 | 优点 | 缺点 |
|---|---|---|---|
| c01_espresso_fict | `baskets` | p11 Pressurized baskets suit pre-ground coffee | n05 No ESE pod compatibility limits options |
| c01_espresso_real | `tank` | p03 Removable 1.1-liter tank with level indicator | n08 Modest 1.1-liter capacity between refills |
| c03_ricecooker_real | `menus` | p01 Eleven menu settings across grain types | n07 Menu list adds selection steps |
| c04_blender_real | `accessories` | p09 Mini-tamper included with base | n05 Single container with no smaller vessel |
| c05_kettle_fict | `temp_range` | p01 Five preset temperatures on the panel | n08 Five presets limit temperature choices |
| c05_kettle_real | `materials` | p05 Body in 304 stainless steel | n07 Descaling needed on a schedule |
| c07_airpurifier_fict | `noise` | p10 Sleep mode near the noise floor | n07 Reaches 56 decibels at top speed |
| c07_airpurifier_real | `filtration` | p01 Three-stage filtration with carbon layer | n07 Pre-filter needs regular vacuuming |
| c08_humidifier_real | `filter` | p06 Wicking filter captures water minerals | n07 Filter must be replaced seasonally |
| c09_standingdesk_fict | `frame` | p05 Powder-coated steel frame construction | n08 Column bolts need periodic checking |
| c09_standingdesk_fict | `frame` | p12 Frame accepts a separate desktop | n08 Column bolts need periodic checking |
| c09_standingdesk_real | `noise` | p11 Sound under 50 decibels while moving | n04 Motor sound audible in shared rooms |
| c09_standingdesk_real | `frame` | p07 Carbon steel frame with BIFMA certification | n08 Column bolts need periodic checking |
| c10_chair_fict | `assembly_req` | p11 Assembly tool included in box | n06 Base and cylinder assemble on arrival |
| c10_chair_real | `capacity` | p01 Rated to 400 pounds of load | n06 Caster housings need periodic checking |
| c10_chair_real | `arms` | p02 Arms adjusting in four directions | n08 Headrest is a separate purchase |
| c11_projector_fict | `focus` | p05 Manual focus ring on the barrel | n07 Keystone correction applied digitally only |
| c11_projector_fict | `os` | p12 Android TV app platform included | n08 Memory of 2 gigabytes for apps |
| c11_projector_real | `ports` | p06 Four wired ports including HDMI 2.0 | n07 Single HDMI input for sources |
| c11_projector_real | `throw` | p04 Image between 40 and 200 inches | n08 Throw ratio needs distance for size |
| c12_headphones_fict | `bluetooth` | p07 Bluetooth 5.2 with AAC support | n08 Single device pairing at a time |
| c12_headphones_real | `bluetooth` | p04 LDAC codec at 990 kilobits | n06 Multipoint limited to standard codecs |
| c12_headphones_real | `bluetooth` | p05 Multipoint connection to two devices | n06 Multipoint limited to standard codecs |
| c12_headphones_real | `box` | p08 Carrying case included in box | n08 Case adds bulk when packed |
| c12_headphones_real | `box` | p12 In-flight plug adaptor supplied | n08 Case adds bulk when packed |
| c13_ereader_fict | `materials` | p10 Textured back aids one-handed grip | n08 Housing in polymer rather than metal |
| c13_ereader_real | `display` | p01 Screen at 300 pixels per inch | n05 No page-turn buttons on the body |
| c13_ereader_real | `battery` | p11 Battery lasting weeks per charge | n06 Battery stated without a capacity figure |
| c14_keyboard_real | `keycaps` | p04 Mac and Windows keycaps included | n07 ABS keycaps wear smoother over time |
| c16_sportwatch_fict | `sensors` | p01 Barometric altimeter recording elevation during activities | n08 No satellite system beyond two |
| c16_sportwatch_fict | `sensors` | p12 Elevation profiles from the altimeter | n08 No satellite system beyond two |
| c16_sportwatch_real | `materials` | p09 Quick release band at 20 millimetres | n08 Band material limited to silicone |
| c17_budgetapp_fict | `method` | p01 Envelope method with automatic rollover | n08 Rollover requires monthly reconciliation |
| c17_budgetapp_real | `export` | p06 Export as CSV or TSV | n05 Export limited to the web app |
| c17_budgetapp_real | `bank_sync` | p02 Automatic transaction import from linked accounts | n07 Manual reconciliation still required regularly |
| c18_notesapp_fict | `storage` | p01 Local-first storage on the device | n07 Sync is optional and separately enabled |
| c18_notesapp_real | `free_limits` | p11 Unlimited blocks for individual users | n05 Free plan caps uploads at 5 megabytes |
| c18_notesapp_real | `free_limits` | p11 Unlimited blocks for individual users | n06 Page history limited to seven days |
| c18_notesapp_real | `offline` | p09 Pages markable available for offline reading | n07 Formulas do not recalculate offline |
| c18_notesapp_real | `free_limits` | p11 Unlimited blocks for individual users | n08 Guest access capped on free plan |
| c19_passwordmgr_real | `free_tier` | p01 Free tier storing unlimited passwords | n07 Free sharing limited to one user |
| c19_passwordmgr_real | `free_tier` | p02 Sync across unlimited devices | n07 Free sharing limited to one user |
| c20_langapp_real | `format` | p05 Short lessons fit brief sessions | n07 Lesson format favours recognition over production |
| c20_langapp_real | `format` | p11 Exercises span reading, listening, speaking | n07 Lesson format favours recognition over production |
| c20_langapp_real | `courses` | p07 Math, music, and chess tracks | n08 Course depth varies across languages |
| c22_backpack_fict | `load_range` | p12 Designed for loads to 18 pounds | n07 Load range tops out at 18 |
| c22_backpack_real | `load_range` | p10 Framesheet supports loads to 20 pounds | n05 Load range tops out near 20 pounds |
| c22_backpack_real | `volume` | p01 Volume of 22 litres in larger size | n06 Two size options rather than adjustable |
| c22_backpack_real | `pockets` | p08 Two zippered hipbelt pockets | n08 Mesh pocket exposed to abrasion |
| c22_backpack_real | `pockets` | p09 External hydration sleeve behind the panel | n08 Mesh pocket exposed to abrasion |
| c23_tent_fict | `capacity` | p09 Head end stands without stakes | n07 Semi-freestanding pitch needs soft ground |
| c23_tent_real | `floor` | p05 Floor area of 29 square feet | n06 Floor width of 50 inches for two |
| c24_bottle_fict | `exterior` | p07 Powder-coated exterior with carry loop | n08 Powder coat can chip in packs |
| c24_bottle_fict | `exterior` | p11 Loop for clipping to a pack | n08 Powder coat can chip in packs |
| c24_bottle_real | `maintenance` | p09 Dishwasher safe on top rack | n06 Stopper threads need separate drying |
| c25_stove_fict | `fuel` | p11 Accepts butane and isobutane mixes | n06 Pure propane canisters not supported |
| c25_stove_real | `fuel` | p12 Accepts three common fuel mixes | n04 Pure propane canisters not supported |
| c26_toothbrush_fict | `head_compat` | p07 Accepts three head shapes | n08 Heads limited to one maker |
| c26_toothbrush_real | `battery` | p11 Handle recharges on the stand | n05 Cell chemistry not stated officially |
| c26_toothbrush_real | `box` | p09 Charging stand included in box | n06 Single brush head in box |
| c26_toothbrush_real | `head_compat` | p04 Accepts seven replacement head types | n08 Head must be replaced regularly |

</details>

## B. 说明书中未在事实表出现的数字（21 个物品）

说明书里的数字应当能在 facts.csv 找到对应。下列数字未匹配——多为拼写形式差异（如 `9-1/2` vs `9.5`）或转述单位，**请确认不是凭空写入的事实**。

| ✓ | 物品 | 未匹配的数字 |
|---|---|---|
| ☐ | c01_espresso_fict | 14.5, 31, 32 |
| ☐ | c01_espresso_real | 14.9, 30.5, 33, 4.2, 685 |
| ☐ | c02_airfryer_fict | 5 |
| ☐ | c03_ricecooker_fict | 6 |
| ☐ | c04_blender_fict | 5 |
| ☐ | c04_blender_real | 310 |
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
| ☐ | c01_espresso_fict | Vestrino M2 | no ESE pod support / two buttons plus steam dial / no top cup rest | `controls, baskets, no_cuprest` |
| ☐ | c02_airfryer_fict | Farnholt A5 | no app or wireless control (dial and button panel only) / round basket instead of square / 8 presets instead of 12 | `capacity, presets, controls` |
| ☐ | c03_ricecooker_fict | Hamura GR-6 | no delay timer / seven menu settings instead of eleven / monochrome LCD instead of colored panel | `menus, no_timer, controls` |
| ☐ | c04_blender_fict | Quarvel BX5 | preset program buttons instead of pulse-only control / 64-ounce container instead of 48 / no tamper included | `container, speeds, controls, accessories` |
| ☐ | c05_kettle_fict | Tessro Kettle | preset temperature buttons instead of to-the-degree dial / 1.2 L capacity instead of 0.9 L / no scheduling or stopwatch functions | `capacity, temp_range, functions` |
| ☐ | c06_robovac_fict | Orvia Petrel | no self-emptying base / gyroscope navigation instead of camera mapping / single side brush instead of dual rubber brushes | `navigation, mapping, brushes, dock` |
| ☐ | c07_airpurifier_fict | Arvelia A2 | air quality sensor with auto mode / rectangular tower body instead of cylinder / no timer function | `dimensions, sensor, modes, no_timer` |
| ☐ | c08_humidifier_fict | Halvira H1 | ultrasonic mist instead of evaporative wick / built-in humidistat with target setting / top-fill opening instead of removable tank | `type, humidistat, fill` |
| ☐ | c09_standingdesk_fict | Ostreno D2 | single motor instead of dual / two memory presets instead of four / no anti-collision sensing | `motors, keypad, no_anticollision` |
| ☐ | c10_chair_fict | Tarnwell C1 | fixed-height arms instead of 4D arms / manual tension knob instead of weight-activated recline / no seat depth adjustment | `no_seat_depth, recline, arms` |
| ☐ | c11_projector_fict | Previk PJ4 | internal battery for cordless playback / 1080p resolution instead of 720p / manual focus ring instead of auto focus | `resolution, battery, focus` |
| ☐ | c12_headphones_fict | Wrenfeld NX40 | physical buttons instead of touch controls / IPX4 splash resistance / no multipoint pairing | `bluetooth, controls, water` |
| ☐ | c13_ereader_fict | Lireon Q2 | physical page-turn buttons on the bezel / 7 inch screen instead of 6 / no water resistance rating | `display, buttons, no_water` |
| ☐ | c14_keyboard_fict | Kelvane Slate 65 | 65 percent layout without a function row / PBT keycaps instead of ABS / wired only, no wireless | `layout, keycaps, connectivity` |
| ☐ | c15_powerbank_fict | Ardento PB10 | integrated cable attached to the housing / digital percentage display instead of LED lights / single USB-C port with no USB-A | `ports, integrated_cable, display` |
| ☐ | c16_sportwatch_fict | Veltrun R40 | barometric altimeter included / button-only controls with no touchscreen / no third-party phone app pairing | `sensors, controls, connectivity` |
| ☐ | c17_budgetapp_fict | Voskell | envelope method with rollover instead of zero-based assignment / manual CSV import instead of bank linking / free tier with limited categories | `method, import, free_tier` |
| ☐ | c18_notesapp_fict | Trelbin | local-first storage with optional sync instead of cloud workspaces / outline documents instead of block databases / no guest sharing | `structure, storage, no_guests` |
| ☐ | c19_passwordmgr_fict | Cryptavo | local vault file with user-managed sync instead of hosted sync / hardware key required for unlock / no browser extensions, desktop and mobile only | `storage, unlock, no_extensions` |
| ☐ | c20_langapp_fict | Quenlo | spaced repetition scheduling instead of streak-based lessons / twelve languages instead of forty / no free tier beyond a trial | `courses, method, trial` |
| ☐ | c21_focusapp_fict | Stillbrook | ambient scene that fills in rather than a tree that dies / no group sessions / desktop-first with no phone blocking | `mechanic, blocking, no_group` |
| ☐ | c22_backpack_fict | Cendric Ridge 28 | roll-top closure instead of a zippered lid / 28 litre volume instead of 22 / single size with an adjustable torso strap | `volume, closure, suspension` |
| ☐ | c23_tent_fict | Torvik Basin 2 | single vestibule and one door instead of two / semi-freestanding, requiring stakes at the foot / integrated footprint included | `capacity, vestibule, doors, footprint` |
| ☐ | c24_bottle_fict | Tavro Flask | screw-off cap with no pour-through stopper / 20 oz capacity instead of 16 / carry loop instead of a side handle | `capacity, stopper, exterior` |
| ☐ | c25_stove_fict | Fyrren S1 | fixed pot supports that fold rather than detach / no built-in igniter / remote canister feed with a hose | `no_igniter, supports, remote_feed` |
| ☐ | c26_toothbrush_fict | Dovrell 230 | sonic vibration instead of oscillating rotation / travel case included / USB charging instead of an induction stand | `action, charging, case` |

## D. 来源质量提示（共 44 条，其中 **5 条需你判断**）

### D1. 需判断（5 条）——来源独立性或权威性存疑

| ✓ | 物品 | 字段 | 类型 | 详情 |
|---|---|---|---|---|
| ☐ | c02_airfryer_real | `(多个字段)` | official row on third-party host | manuals.plus |
| ☐ | c06_robovac_real | `(多个字段)` | official row on third-party host | manua.ls |
| ☐ | c20_langapp_real | `(多个字段)` | official row on third-party host | apps.apple.com |
| ☐ | c22_backpack_real | `(多个字段)` | official row on third-party host | outdoorsports.com |
| ☐ | c23_tent_real | `(多个字段)` | official row on third-party host | cascadedesigns.com |

<details><summary>D2. 已在 note 中记录的矛盾与回避（39 条，抽查即可）</summary>

| 物品 | 字段 | note |
|---|---|---|
| c01_espresso_real | `cup_height` | US page says 13 cm; EN structured spec table taken; discrepancy recorded |
| c02_airfryer_real | `dimensions` | manual mirrors differ slightly on dims; official page lacks a spec table; discrepancy recorded |
| c02_airfryer_real | `footprint_con` | con; sibling-model coverage caveat |
| c03_ricecooker_real | `weight` | omitted from spec sheet |
| c06_robovac_real | `battery` | batch discrepancy: some listings claim 120 min runtime; 75 min taken; verify before freeze; also grounds runti |
| c06_robovac_real | `dustbin` | batch discrepancy: 0.4 vs 0.3 L across listings; 0.4 taken; verify before freeze; also grounds frequent-emptyi |
| c06_robovac_real | `noise_con` | con; spec claims 58 dB vs 65-68 measured; discrepancy recorded; noise kept out of spec sheet |
| c06_robovac_real | `bags_con` | con; batch also flags price, omitted per no-price rule |
| c08_humidifier_real | `filter_cost` | con; same publisher caveat |
| c08_humidifier_real | `wick_mold` | con; same publisher caveat |
| c08_humidifier_real | `basic_controls` | con; same publisher caveat |
| c09_standingdesk_real | `height_range` | one source lists 48.8 in max; discrepancy recorded |
| c10_chair_real | `seat_height` | exact figures from a partially extracted spec PDF; verify before freeze; omitted from spec sheet |
| c12_headphones_real | `weight` | official spec page reached via search index; direct fetch blocked; one review measured 251 g |
| c12_headphones_real | `driver` | low-confidence source as above |
| c12_headphones_real | `bluetooth` | low-confidence source as above |
| c12_headphones_real | `frequency` | low-confidence source as above |
| c14_keyboard_real | `dimensions` | same source caveat |
| c14_keyboard_real | `height` | same source caveat |
| c14_keyboard_real | `weight` | same source caveat |
| c15_powerbank_real | `output_a` | official text also appends 15 W max per port; internally inconsistent |
| c15_powerbank_real | `dimensions` | retailer and review figures conflict; omitted from spec sheet |
| c17_budgetapp_real | `tier_note` | prices omitted per DECISIONS |
| c18_notesapp_fict | `tiers` | prices omitted per DECISIONS |
| c18_notesapp_real | `tiers` | prices omitted per DECISIONS |
| c19_passwordmgr_real | `paid_tier` | tier is named Premium officially; renamed to paid tier in materials because the brand word is on the banned ev |
| c20_langapp_real | `paid_tier` | prices vary by region; omitted per DECISIONS |
| c21_focusapp_fict | `paid_tier` | prices omitted per DECISIONS |
| c22_backpack_real | `volume` | official specs mirrored by an authorized retailer; osprey.com blocked automated access |
| c22_backpack_real | `weight` | one review measured 38.4 oz; discrepancy recorded |
| c22_backpack_real | `dimensions` | same source caveat |
| c22_backpack_real | `main_fabric` | same source caveat |
| c22_backpack_real | `bottom_fabric` | same source caveat |
| c22_backpack_real | `suspension` | same source caveat |
| c22_backpack_real | `attachments` | same source caveat |
| c22_backpack_real | `pockets` | same source caveat |
| c22_backpack_real | `load_range` | same source caveat |
| c23_tent_real | `capacity` | NX generation specs; renamed Hubba Hubba 2 in 2022 with different figures; NX archived specs used per DECISION |
| c26_toothbrush_real | `modes` | official page states three modes; earlier production units shipped with one; mid-cycle refresh; omitted per DE |

</details>

## E. 逐物品签字表

| ✓ | 物品 | 名称 | 类型 | 事实行 | 官方 | 评测共识 |
|---|---|---|---|---|---|---|
| ☐ | c01_espresso_fict | Vestrino M2 | fictional | 18 | 0 | 0 |
| ☐ | c01_espresso_real | De'Longhi Dedica EC685 | real | 23 | 15 | 8 |
| ☐ | c02_airfryer_fict | Farnholt A5 | fictional | 18 | 0 | 0 |
| ☐ | c02_airfryer_real | Cosori Pro II 5.8QT | real | 17 | 10 | 2 |
| ☐ | c03_ricecooker_fict | Hamura GR-6 | fictional | 17 | 0 | 0 |
| ☐ | c03_ricecooker_real | Zojirushi NS-ZCC10 | real | 18 | 12 | 6 |
| ☐ | c04_blender_fict | Quarvel BX5 | fictional | 18 | 0 | 0 |
| ☐ | c04_blender_real | Vitamix E310 | real | 17 | 11 | 6 |
| ☐ | c05_kettle_fict | Tessro Kettle | fictional | 17 | 0 | 0 |
| ☐ | c05_kettle_real | Fellow Stagg EKG | real | 16 | 10 | 6 |
| ☐ | c06_robovac_fict | Orvia Petrel | fictional | 18 | 0 | 0 |
| ☐ | c06_robovac_real | iRobot Roomba i7 | real | 17 | 10 | 7 |
| ☐ | c07_airpurifier_fict | Arvelia A2 | fictional | 18 | 0 | 0 |
| ☐ | c07_airpurifier_real | Levoit Core 300 | real | 18 | 11 | 7 |
| ☐ | c08_humidifier_fict | Halvira H1 | fictional | 17 | 0 | 0 |
| ☐ | c08_humidifier_real | Honeywell HCM-350 | real | 17 | 11 | 6 |
| ☐ | c09_standingdesk_fict | Ostreno D2 | fictional | 18 | 0 | 0 |
| ☐ | c09_standingdesk_real | FlexiSpot E7 | real | 17 | 7 | 10 |
| ☐ | c10_chair_fict | Tarnwell C1 | fictional | 16 | 0 | 0 |
| ☐ | c10_chair_real | Steelcase Series 1 | real | 16 | 10 | 6 |
| ☐ | c11_projector_fict | Previk PJ4 | fictional | 20 | 0 | 0 |
| ☐ | c11_projector_real | XGIMI MoGo 2 | real | 20 | 14 | 6 |
| ☐ | c12_headphones_fict | Wrenfeld NX40 | fictional | 17 | 0 | 0 |
| ☐ | c12_headphones_real | Sony WH-1000XM4 | real | 17 | 10 | 7 |
| ☐ | c13_ereader_fict | Lireon Q2 | fictional | 19 | 0 | 0 |
| ☐ | c13_ereader_real | Kobo Clara 2E | real | 19 | 13 | 6 |
| ☐ | c14_keyboard_fict | Kelvane Slate 65 | fictional | 19 | 0 | 0 |
| ☐ | c14_keyboard_real | Keychron K2 | real | 18 | 13 | 5 |
| ☐ | c15_powerbank_fict | Ardento PB10 | fictional | 17 | 0 | 0 |
| ☐ | c15_powerbank_real | Belkin BoostCharge 10K | real | 17 | 13 | 4 |
| ☐ | c16_sportwatch_fict | Veltrun R40 | fictional | 18 | 0 | 0 |
| ☐ | c16_sportwatch_real | Garmin Forerunner 55 | real | 20 | 13 | 7 |
| ☐ | c17_budgetapp_fict | Voskell | fictional | 16 | 0 | 0 |
| ☐ | c17_budgetapp_real | YNAB | real | 16 | 10 | 6 |
| ☐ | c18_notesapp_fict | Trelbin | fictional | 16 | 0 | 0 |
| ☐ | c18_notesapp_real | Notion | real | 15 | 8 | 7 |
| ☐ | c19_passwordmgr_fict | Cryptavo | fictional | 16 | 0 | 0 |
| ☐ | c19_passwordmgr_real | Bitwarden | real | 16 | 10 | 6 |
| ☐ | c20_langapp_fict | Quenlo | fictional | 14 | 0 | 0 |
| ☐ | c20_langapp_real | Duolingo | real | 15 | 8 | 7 |
| ☐ | c21_focusapp_fict | Stillbrook | fictional | 14 | 0 | 0 |
| ☐ | c21_focusapp_real | Forest | real | 18 | 11 | 3 |
| ☐ | c22_backpack_fict | Cendric Ridge 28 | fictional | 16 | 0 | 0 |
| ☐ | c22_backpack_real | Osprey Talon 22 | real | 17 | 9 | 8 |
| ☐ | c23_tent_fict | Torvik Basin 2 | fictional | 18 | 0 | 0 |
| ☐ | c23_tent_real | MSR Hubba Hubba NX | real | 18 | 12 | 6 |
| ☐ | c24_bottle_fict | Tavro Flask | fictional | 16 | 0 | 0 |
| ☐ | c24_bottle_real | Thermos Stainless King | real | 15 | 10 | 5 |
| ☐ | c25_stove_fict | Fyrren S1 | fictional | 17 | 0 | 0 |
| ☐ | c25_stove_real | SOTO WindMaster | real | 18 | 11 | 7 |
| ☐ | c26_toothbrush_fict | Dovrell 230 | fictional | 15 | 0 | 0 |
| ☐ | c26_toothbrush_real | Oral-B Pro 1000 | real | 15 | 9 | 6 |
