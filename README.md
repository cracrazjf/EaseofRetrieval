# Ease of Retrieval as Information in Large Language Models

研究 LLM 在多轮对话中，是否会把前一轮生成过程留下的**困难痕迹**（犹豫、停顿、耗尽措辞）当作关于判断对象的信息使用——即认知心理学中 ease-of-retrieval / feelings-as-information 效应在语言模型上的机制性检验。

核心问题不是"能不能在 LLM 上复刻一个经典效应"，而是：**利用 LLM 独有的解耦操纵**（痕迹可伪造、可隐藏、可归属给他人），检验该理论三十年来在人类被试上无法分离的机制主张。

---

## 文档

| 文档 | 内容 |
|---|---|
| [proposal_motivation_background_related_work.md](proposal_motivation_background_related_work.md) | 为什么做、理论背景、相关工作、规范基准（何时是偏差、何时是合理推断） |
| [experimental_design.md](experimental_design.md) | 八个实验 E1–E8、每个证明什么、预注册假设、分析计划、可证伪格局表 |
| [data_design_and_validation_protocol.md](data_design_and_validation_protocol.md) | 材料构造、数据 schema、六层质量门、预算与运行规范、pilot 决策树 |
| [assumptions_register.md](assumptions_register.md) | 全部未言明假设的登记表，及每条的验证方式与失败处置 |

---

## 实验一览

| 实验 | 回答什么 | 关键判据 |
|---|---|---|
| **E1** 自然两阶段 | 效应存在吗？方向？（RQ1、RQ5 存在性） | n ∈ {3…50} 的剂量斜率；超量条件下的编造与方向翻转 |
| **E1b** 编造移植 | 编造条目被当作证据吗？（RQ5 机制） | 编造占比 F0/F4/F8 不降低判断 |
| **E2** 痕迹剂量-反应 ★承重墙 | 痕迹单独够不够？由哪个成分携带？（RQ2a） | 插槽式**等长**构造下的斜率；过程标记 vs 结尾声明正交分解 |
| **E3** 归属 | 自己的困难比别人的更重要吗？ | Δ_self vs Δ_other（**交互**，非主效应） |
| **E4** 内容量 × 痕迹 | 内容量单独值多少？（RQ2b） | 2×2 正交分离 |
| **E5** 任务结构知识 | 仅凭"知道被要求列 12 条"够吗？（RQ2c） | 合理推断成分的上界 |
| **E6** 效价诊断 ★ | 是 ease 还是消极语域传染？（RQ2′） | 难列**缺点**时判断是否**上升** |
| **E7** 归因 ★ | Discounting？Augmentation？（RQ3） | D > C 且 B > A |
| **E8** 披露阶梯 | 涌现机制还是记忆再现？ | covert < aware < demand |

★ = 理论杠杆最高 / 优先执行

---

## 状态

- 阶段：**设计中**（v0.2），尚未开始数据收集
- 下一步：pilot（D1–D4 + 分叉 A 归属检查 + E2/E6 pilot）→ 功效分析重算 → OSF 预注册 → 主实验
- 预算：优化后预期 $1,000–2,000，封顶 $3,200
- 计划中的人类平行对照：材料冻结后，Prolific，N ≈ 300
