# Data Directory Layout

材料按生产阶段单向流动：`raw → neutralization → frozen → norming → main`。
每个阶段只读上一阶段的产物；**回改必须回到 raw 重走全程**（保证任何冻结版都可从 raw 复现）。

```
data/
├── raw/                          # 阶段 0：采集与起草（唯一允许人工编辑的区域）
│   ├── items/<item_id>/
│   │   ├── meta.json             # 物品元数据（类别、配对、差异点、状态）
│   │   ├── facts.csv             # 事实表：field,value,source_type,source_url,accessed_date,note
│   │   ├── sources.json          # 来源档案（官方页 + 评测 URL + 抓取状态）
│   │   ├── spec_draft.md         # 说明书草稿（150±10 词，禁评价词）
│   │   ├── entries_draft.json    # 12 优 + 8 缺草稿（每条挂 fact_field 溯源）
│   │   └── sources_archive/      # 抓取到的页面快照（html/txt，防来源失效）
│   └── slot_units/               # 插槽单元库（S/N/E/X/A；待 D1 校准后入驻）
├── neutralization/               # 阶段 1：MiniMax 风格中和
│   ├── input/<item_id>.json      # 喂给改写模型的打包 payload（脚本生成，勿手改）
│   ├── output/<item_id>.json     # 改写模型返回
│   ├── checks/<item_id>.json     # 评审模型的语义等价核对返回
│   └── log/<item_id>.json       # neutralization_log（草稿→改写→核对→人工裁决全链路）
├── frozen/                       # 阶段 2：版本冻结
│   └── v<N>/<item_id>/           # 通过中和 + 校验的最终材料，附 manifest（内容 hash）
│                                 # D2 评审与主实验只准读这里；发现问题 → 回 raw 重走
├── norming/                      # 阶段 3：D2
│   ├── input/                    # 组装好的刺激物 payload（frozen 材料 + 槽单元拼装）
│   ├── ratings/                  # 逐次评审原始记录（jsonl：stim_id, question_id, reviewer, sample_idx, rating…）
│   └── aggregates/               # 聚合统计与通过/不通过判定
└── main/                         # 阶段 4：D5 主实验数据（schema 见协议 §1）
```

## 角色与写权限

| 阶段 | 谁写入 | 模型 |
|---|---|---|
| raw | 采集脚本 + 研究者 | （采集 agent 只贡献事实与 URL，不留成句文风） |
| neutralization/output | 改写模型 | **MiniMax**（版本冻结；烧掉家族，永不被试） |
| neutralization/checks | 等价核对 | Gemini/Mistral（只读只判，不留字） |
| norming/ratings | 评审模型 | Gemini + Mistral（专职打分） |
| frozen | 脚本（哈希 + tag） | — |

## item_id 命名

`c<两位类别号>_<类别slug>_<real|fict>`，如 `c01_espresso_real`、`c01_espresso_fict`。
类别注册表：`src/items_registry.json`（26 类 × 2 = 52 个物品，含官方 URL 与状态字段）。

## 状态机（meta.json 的 status 字段）

`registered → sourcing → drafted → validated → rewrite_packaged → neutralized → frozen → normed`

推进方式见 `src/prepare_item.py`（init / fetch / validate / package-rewrite / status）。
