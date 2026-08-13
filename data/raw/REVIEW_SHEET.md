# 材料验证清单（自动生成，勿手改；改材料后重跑 `python3 src/make_review_sheet.py`）

一张表看完所有需要人工判断的地方。脚本已把住的（词数/禁词/条目数/溯源有效性/≥2源）不在此列。


## A. 优缺点权衡对（共 117 处，其中 **38 处需你判断**）

同一事实字段同时支撑一优一缺。判断标准：**权衡**（同一属性的两面，保留）还是**同说法重述**（把同一句话正反说一遍，应改掉其中一条）。

### A1. 需判断（38 处）——优缺点措辞高度重叠

| ✓ | 提示 | 物品 | 字段 | 优点 | 缺点 |
|---|---|---|---|---|---|
| ☐ | · 部分重叠 | c01_espresso_fict | `baskets` | p11 The pressurised baskets suit coffee that is already ground | n02 Coffee has to be ground somewhere else first |
| ☐ | · 部分重叠 | c05_kettle_real | `controls` | p04 The colour screen and dial make the settings obvious | n08 Screen and dial add steps before any water heats |
| ☐ | · 部分重叠 | c06_robovac_fict | `brushes` | p12 The side brush sweeps debris in from along the wall | n08 One side brush leaves the other edge unswept |
| ☐ | ⚠ 同说法重述 | c08_humidifier_fict | `warranty` | p11 Two years of cover comes with the unit | n07 Cover runs out after two years |
| ☐ | ⚠ 同说法重述 | c08_humidifier_fict | `cartridge` | p07 A mineral cartridge sits in the reservoir from the start | n08 The cartridge sits down inside the reservoir to reach |
| ☐ | · 部分重叠 | c08_humidifier_real | `tank` | p01 The 1.1-gallon tank runs a full day between fills | n06 The tank needs refilling every single day |
| ☐ | ⚠ 同说法重述 | c10_chair_fict | `warranty` | p07 Seven years of cover runs on the parts | n07 Cover runs out after seven years |
| ☐ | · 部分重叠 | c10_chair_fict | `back` | p05 Knit mesh stretches over a moulded back frame | n08 The mesh back needs vacuuming to stay clean |
| ☐ | ⚠ 同说法重述 | c10_chair_real | `seat_depth` | p04 Seat depth slides over two and a quarter inches | n05 Seat depth only travels two and a quarter inches |
| ☐ | · 部分重叠 | c11_projector_real | `os` | p05 Android TV runs apps off 16 gigabytes of storage | n05 16 gigabytes fills up after a handful of apps |
| ☐ | · 部分重叠 | c12_headphones_fict | `battery_nc_on` | p01 Twenty-six hours of canceling covers a week of commutes | n07 Twenty-six hours falls short of the thirty-hour class |
| ☐ | · 部分重叠 | c12_headphones_real | `box` | p08 A hard case comes in the box rather than a pouch | n08 The hard case takes up real room in a bag |
| ☐ | · 部分重叠 | c13_ereader_real | `display` | p01 Text sits sharp at 300 pixels per inch | n08 A six-inch page shows less text than larger readers |
| ☐ | ⚠ 同说法重述 | c14_keyboard_real | `polling` | p09 Wired polling runs at a full 1000 hertz | n04 Wireless polling drops to 90 hertz |
| ☐ | · 部分重叠 | c14_keyboard_real | `battery` | p02 With the light off the battery runs 240 hours | n05 Turning on RGB cuts the battery to 72 hours |
| ☐ | · 部分重叠 | c14_keyboard_real | `backlight` | p07 Eighteen backlight patterns run across four brightness levels | n08 Brightness moves in four steps and nothing between |
| ☐ | ⚠ 同说法重述 | c15_powerbank_fict | `dimensions` | p11 It measures 104 millimetres end to end | n07 At 25 millimetres thick it bulks up a bag |
| ☐ | · 部分重叠 | c15_powerbank_real | `indicators` | p04 Four lights on the case report what is left | n08 Four lights give only a rough sense of charge |
| ☐ | ⚠ 同说法重述 | c16_sportwatch_fict | `weight` | p11 At 41 grams it sits light on the wrist | n07 At 41 grams it presses into the wrist overnight |
| ☐ | · 部分重叠 | c17_budgetapp_fict | `free_tier` | p02 Ten envelopes and one account cost nothing | n07 One account is all the free tier allows |
| ☐ | · 部分重叠 | c18_notesapp_real | `free_limits` | p11 Individuals get unlimited blocks on the free plan | n05 The free plan caps uploads at five megabytes |
| ☐ | · 部分重叠 | c18_notesapp_real | `free_limits` | p11 Individuals get unlimited blocks on the free plan | n08 Guests are capped at ten on the free plan |
| ☐ | · 部分重叠 | c19_passwordmgr_fict | `export` | p07 Vaults export as an encrypted archive or plain CSV | n08 CSV export drops the encryption entirely |
| ☐ | ⚠ 同说法重述 | c20_langapp_fict | `trial` | p09 New accounts get fourteen days to try it | n07 Fourteen days is a short window to judge it |
| ☐ | · 部分重叠 | c21_focusapp_fict | `blocking` | p03 It blocks desktop apps and websites during a session | n07 Blocking reaches desktop apps and nothing beyond |
| ☐ | · 部分重叠 | c21_focusapp_fict | `paid_tier` | p11 Scene variants come with the paid tier | n08 Scene variants are held back for paying users |
| ☐ | ⚠ 同说法重述 | c22_backpack_fict | `load_range` | p12 The suspension handles eighteen pounds comfortably | n07 Loads past eighteen pounds overwhelm the suspension |
| ☐ | · 部分重叠 | c22_backpack_real | `load_range` | p10 The framesheet carries twenty pounds without collapsing | n05 Loads past twenty pounds overwhelm the suspension |
| ☐ | · 部分重叠 | c23_tent_fict | `floor_fabric` | p11 The floor is coated to 2500 millimetres | n08 A 2500-millimetre floor is modest under a wet pitch |
| ☐ | · 部分重叠 | c24_bottle_fict | `retention` | p02 Hot drinks hold for sixteen hours | n07 Sixteen hours falls short of the eighteen-hour bottles |
| ☐ | · 部分重叠 | c24_bottle_fict | `exterior` | p11 The loop clips it to the outside of a pack | n08 Powder coating chips where it rubs inside a pack |
| ☐ | ⚠ 同说法重述 | c24_bottle_real | `maintenance` | p09 The body goes on the top rack of a dishwasher | n07 Only the top rack of the dishwasher is safe |
| ☐ | · 部分重叠 | c24_bottle_real | `weight` | p10 At 0.9 pounds it packs without much penalty | n08 It already weighs 0.9 pounds before anything goes in |
| ☐ | ⚠ 同说法重述 | c25_stove_fict | `boil` | p10 Two cups reach a boil in three minutes | n07 Three minutes to boil is slow in cold weather |
| ☐ | ⚠ 同说法重述 | c25_stove_real | `burn_time` | p09 One canister runs about ninety minutes | n07 Ninety minutes per canister runs short on long trips |
| ☐ | ⚠ 同说法重述 | c26_toothbrush_fict | `warranty` | p08 Two years of cover comes with the handle | n07 Cover runs out after two years |
| ☐ | ⚠ 同说法重述 | c26_toothbrush_real | `box` | p10 A brush head ships with the handle | n06 One brush head is all that comes along |
| ☐ | ⚠ 同说法重述 | c26_toothbrush_real | `warranty` | p08 Two years of cover comes with the handle | n07 Cover runs out after two years |

<details><summary>A2. 已判定为正常权衡（79 处，抽查即可）</summary>

| 物品 | 字段 | 优点 | 缺点 |
|---|---|---|---|
| c01_espresso_fict | `tank` | p03 The 1.0-litre tank lifts out and shows the water level | n01 The 1.0-litre tank runs dry after a few drinks |
| c01_espresso_fict | `baskets` | p11 The pressurised baskets suit coffee that is already ground | n05 ESE pods do not fit the filter holder at all |
| c01_espresso_real | `tank` | p03 The 1.1-litre tank lifts out and shows the water level | n08 The 1.1-litre tank runs dry after a few drinks |
| c03_ricecooker_real | `menus` | p01 Eleven settings cover white, brown, sushi, porridge, and more | n07 Working through eleven settings adds steps to each meal |
| c04_blender_fict | `weight` | p09 At 11.2 pounds the base stays planted while running | n08 At 11.2 pounds it is awkward to lift onto a shelf |
| c04_blender_real | `accessories` | p09 A mini-tamper comes with the base for thick mixtures | n05 One container size covers every job, large or small |
| c04_blender_real | `controls` | p10 The speed dial moves gradually rather than in jumps | n06 The dial carries no preset programs at all |
| c04_blender_real | `cord` | p11 The cord reaches 4.5 feet to the nearest outlet | n07 A 4.5-foot cord limits where the base can sit |
| c05_kettle_fict | `temp_range` | p01 Five preset temperatures cover the common brewing points | n08 Five presets rule out anything between them |
| c05_kettle_real | `materials` | p05 The body is 304 stainless rather than coated steel | n07 Scale builds up and needs descaling on a schedule |
| c07_airpurifier_fict | `noise` | p10 Sleep mode drops close to the noise floor of a room | n07 On full speed it climbs to 56 decibels |
| c07_airpurifier_fict | `coverage` | p11 It turns over the air in 960 square feet hourly | n08 Rated coverage drops to 200 square feet at real turnover |
| c07_airpurifier_real | `filtration` | p01 Three stages catch particles and odour before the air returns | n07 The pre-filter needs vacuuming or it clogs |
| c07_airpurifier_real | `dimensions` | p10 The base takes up less than nine inches square | n08 At 14.2 inches tall it stands out in a small room |
| c08_humidifier_fict | `dimensions` | p10 The base takes up less than eleven inches across | n06 At 13.8 inches tall it dominates a side table |
| c08_humidifier_real | `filter` | p06 The wick traps minerals so they never reach the air | n07 The filter has to be swapped on a schedule |
| c09_standingdesk_fict | `noise` | p08 It stays under 55 decibels while moving | n07 The motors reach 55 decibels in a shared room |
| c09_standingdesk_fict | `frame` | p05 Powder-coated steel holds the columns together | n08 Column bolts need checking every so often |
| c09_standingdesk_fict | `frame` | p12 The frame takes whatever desktop the buyer supplies | n08 Column bolts need checking every so often |
| c09_standingdesk_real | `noise` | p11 It stays under 50 decibels while moving | n04 The motors are audible in a shared room |
| c09_standingdesk_real | `speed` | p08 It travels about an inch and a half per second | n06 Travel is slow enough to notice when switching often |
| c09_standingdesk_real | `frame` | p07 Carbon steel and BIFMA certification back the frame | n08 Column bolts need checking every so often |
| c10_chair_fict | `assembly_req` | p11 An assembly tool comes in the box | n06 Base, cylinder, and seat all assemble on arrival |
| c10_chair_real | `capacity` | p01 It is rated to 400 pounds, well past most task chairs | n06 Caster housings collect hair and need clearing |
| c10_chair_real | `arms` | p02 The arms move in four directions to meet the desk | n08 A headrest costs extra and adds little |
| c11_projector_fict | `focus` | p05 A focus ring on the barrel sharpens the image by hand | n07 Keystone correction is digital, so pixels get squeezed |
| c11_projector_fict | `os` | p03 32 gigabytes holds a decent library of apps | n08 2 gigabytes of memory slows the interface down |
| c11_projector_fict | `os` | p12 Android TV brings the usual streaming apps along | n08 2 gigabytes of memory slows the interface down |
| c11_projector_real | `os` | p05 Android TV runs apps off 16 gigabytes of storage | n06 2 gigabytes of memory slows the interface down |
| c11_projector_real | `ports` | p06 Four wired ports include full HDMI 2.0 | n07 One HDMI input means swapping cables between sources |
| c11_projector_real | `throw` | p04 The image scales anywhere from 40 to 200 inches | n08 A 1.2:1 throw needs real distance for a big image |
| c12_headphones_fict | `bluetooth` | p07 Bluetooth 5.2 handles AAC on top of the basic codec | n08 Swapping devices means unpairing and pairing again |
| c12_headphones_real | `battery_nc_on` | p02 Thirty hours of canceling covers a week of commutes | n05 Switching to LDAC nearly halves the battery life |
| c12_headphones_real | `bluetooth` | p04 LDAC pushes audio at up to 990 kilobits | n06 Two-device pairing drops back to the basic codec |
| c12_headphones_real | `bluetooth` | p05 It holds two devices at once and swaps between them | n06 Two-device pairing drops back to the basic codec |
| c12_headphones_real | `box` | p12 A plug adaptor covers in-flight entertainment systems | n08 The hard case takes up real room in a bag |
| c13_ereader_fict | `buttons` | p03 Buttons on the bezel turn pages without touching the screen | n07 The page buttons sit on the left side only |
| c13_ereader_fict | `materials` | p10 The textured back stops it sliding out of one hand | n08 A polymer shell feels less solid than metal |
| c13_ereader_real | `display` | p01 Text sits sharp at 300 pixels per inch | n05 There are no page-turn buttons on the body |
| c13_ereader_real | `battery` | p11 A charge lasts weeks rather than days | n06 Kobo never states an actual battery capacity |
| c13_ereader_real | `storage` | p04 Sixteen gigabytes holds thousands of books at once | n07 Storage is fixed with no card slot to add more |
| c14_keyboard_fict | `switches` | p03 Hot-swap sockets take any switch without soldering | n08 Switches are bought separately from the board |
| c14_keyboard_real | `keycaps` | p04 Both Windows and Mac keycaps come in the box | n07 ABS keycaps go shiny where fingers land most |
| c15_powerbank_real | `included` | p05 A cable comes in the box rather than sold separately | n04 The bundled cable measures only six inches |
| c16_sportwatch_fict | `sensors` | p01 The altimeter records elevation through every run | n08 Only two satellite systems are supported |
| c16_sportwatch_fict | `sensors` | p12 Elevation profiles come out of the barometric sensor | n08 Only two satellite systems are supported |
| c16_sportwatch_real | `materials` | p09 Standard 20-millimetre bands swap in seconds | n08 Silicone is the only band material offered |
| c17_budgetapp_fict | `method` | p01 Envelopes roll unspent money into the next month | n08 Rollover only works if envelopes get reconciled |
| c17_budgetapp_real | `export` | p06 Plan data exports as CSV or TSV | n05 Exports only come out of the web app |
| c17_budgetapp_real | `bank_sync` | p02 Linked accounts pull transactions in on their own | n07 Reconciling still takes hand work every week |
| c17_budgetapp_real | `sharing` | p03 One subscription covers a household of six | n08 Sharing stops at six people per plan |
| c18_notesapp_fict | `storage` | p01 Documents live on the device rather than a server | n07 Sync has to be switched on and set up separately |
| c18_notesapp_fict | `storage` | p03 Encrypted sync copies documents between installs when wanted | n07 Sync has to be switched on and set up separately |
| c18_notesapp_real | `free_limits` | p11 Individuals get unlimited blocks on the free plan | n06 Page history disappears after seven days |
| c18_notesapp_real | `offline` | p09 Pages can be marked to read offline later | n07 Formulas stop recalculating the moment it goes offline |
| c19_passwordmgr_real | `free_tier` | p01 The free tier stores as many passwords as needed | n07 Free sharing reaches exactly one other person |
| c19_passwordmgr_real | `free_tier` | p02 Free accounts sync across as many devices as wanted | n07 Free sharing reaches exactly one other person |
| c20_langapp_fict | `courses` | p04 Every language pairs a reading and listening track | n08 There is nothing here but languages |
| c20_langapp_fict | `courses` | p10 Twelve languages each get matched tracks | n08 There is nothing here but languages |
| c20_langapp_real | `format` | p05 Lessons are short enough for a bus ride | n07 Tapping answers builds recognition rather than production |
| c20_langapp_real | `format` | p11 Exercises mix reading, listening, and speaking | n07 Tapping answers builds recognition rather than production |
| c20_langapp_real | `courses` | p01 Over 280 courses span more than forty languages | n08 Course depth varies wildly between languages |
| c20_langapp_real | `courses` | p07 Math, music, and chess sit alongside the languages | n08 Course depth varies wildly between languages |
| c21_focusapp_fict | `paid_tier` | p08 The paid tier lifts the history limit entirely | n08 Scene variants are held back for paying users |
| c22_backpack_fict | `closure` | p02 The roll top shrinks the pack down to what is inside | n08 Pack height changes as the contents shift around |
| c22_backpack_real | `volume` | p01 Twenty-two litres swallows a full day of gear | n06 Two fixed sizes rather than one adjustable pack |
| c22_backpack_real | `pockets` | p08 Two zippered pockets sit on the hipbelt | n08 The stretch mesh pocket abrades against rock |
| c22_backpack_real | `pockets` | p09 A hydration sleeve hides behind the backpanel | n08 The stretch mesh pocket abrades against rock |
| c23_tent_fict | `capacity` | p09 The head end stands up before any stake goes in | n07 Hard ground leaves the foot end sagging |
| c23_tent_real | `floor` | p05 Twenty-nine square feet holds two sleeping pads | n06 Fifty inches across is tight for two adults |
| c24_bottle_fict | `retention` | p03 Cold drinks hold for twenty-two hours | n07 Sixteen hours falls short of the eighteen-hour bottles |
| c24_bottle_fict | `exterior` | p07 A powder-coated shell carries a loop for clipping on | n08 Powder coating chips where it rubs inside a pack |
| c24_bottle_real | `maintenance` | p09 The body goes on the top rack of a dishwasher | n06 The stopper threads have to dry separately |
| c25_stove_fict | `fuel` | p11 It burns butane and isobutane mixes | n06 Pure propane canisters cannot be used |
| c25_stove_real | `fuel` | p12 It burns butane, isobutane, and propane mixes | n04 Pure propane canisters cannot be used |
| c26_toothbrush_fict | `head_compat` | p07 Three head shapes fit the same handle | n08 Heads come from one maker and nowhere else |
| c26_toothbrush_real | `battery` | p11 The handle sits on the stand to recharge | n05 Oral-B never states what cell is inside |
| c26_toothbrush_real | `box` | p09 The charging stand comes in the box | n06 One brush head is all that comes along |
| c26_toothbrush_real | `head_compat` | p04 Seven Oral-B head types fit the same handle | n08 Heads wear out and have to be replaced regularly |

</details>

## B. 说明书中未在事实表出现的数字（21 个物品）

说明书里的数字应当能在 facts.csv 找到对应。下列数字未匹配——多为拼写形式差异（如 `9-1/2` vs `9.5`）或转述单位，**请确认不是凭空写入的事实**。

| ✓ | 物品 | 未匹配的数字 |
|---|---|---|
| ☐ | c01_espresso_real | 65, 685 |
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
| ☐ | c12_headphones_real | 1000, 16, 4 |
| ☐ | c13_ereader_fict | 2 |
| ☐ | c14_keyboard_real | 2 |
| ☐ | c15_powerbank_fict | 10 |
| ☐ | c15_powerbank_real | 10 |
| ☐ | c16_sportwatch_fict | 40 |
| ☐ | c16_sportwatch_real | 55 |
| ☐ | c25_stove_real | 02, 2, 27, 4 |
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
