#!/usr/bin/env python3
"""Generate data/raw/REVIEW_SHEET.md — everything a human must eyeball,
flattened into tables so no file needs opening.

Sections:
  A. pro/con tradeoff pairs (the validate WARNs), text shown side by side
  B. spec-sheet numbers with no matching figure in facts.csv
  C. fictional difference points + mirror sanity
  D. source-quality flags (single-domain consensus, non-official specs, notes)
  E. per-item sign-off table

Run: python3 src/make_review_sheet.py
"""
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
ITEMS = ROOT / "data" / "raw" / "items"
OUT = ROOT / "data" / "raw" / "REVIEW_SHEET.md"


def load(item):
    d = ITEMS / item
    meta = json.loads((d / "meta.json").read_text())
    facts = list(csv.DictReader(open(d / "facts.csv", encoding="utf-8")))
    spec = re.sub(r"<!--.*?-->", "", (d / "spec_draft.md").read_text(), flags=re.S).strip()
    entries = json.loads((d / "entries_draft.json").read_text())
    return meta, facts, spec, entries


STOP = {"the","a","an","of","for","with","and","or","in","on","to","at","by","from",
        "is","are","only","when","than","that","its","per","up","no","not","without"}


def numbers(text):
    """figures that carry factual weight, normalized for comparison"""
    return set(re.findall(r"\d+(?:[.,]\d+)?", text))


def domain(url):
    try:
        h = urlparse(url).netloc.lower()
        return h[4:] if h.startswith("www.") else h
    except Exception:
        return url


def main():
    items = sorted(p.name for p in ITEMS.iterdir() if p.is_dir())
    tradeoffs, orphan_nums, diffs, flags, signoff = [], [], [], [], []

    for it in items:
        meta, facts, spec, entries = load(it)
        fact_by_field = {f["field"]: f for f in facts}
        pros, cons = entries["pros"], entries["cons"]

        # --- A. pro/con sharing a fact_field ---
        pro_ff = {}
        for p in pros:
            pro_ff.setdefault(p["fact_field"], []).append(p)
        for c in cons:
            for p in pro_ff.get(c["fact_field"], []):
                pw = set(re.findall(r"[a-z]+", p["text_draft"].lower())) - STOP
                cw = set(re.findall(r"[a-z]+", c["text_draft"].lower())) - STOP
                overlap = len(pw & cw) / max(1, min(len(pw), len(cw)))
                sev = "⚠ 同说法重述" if overlap >= 0.5 else ("· 部分重叠" if overlap >= 0.3 else "")
                tradeoffs.append((sev, it, c["fact_field"],
                                  f'{p["entry_id"]} {p["text_draft"]}',
                                  f'{c["entry_id"]} {c["text_draft"]}'))

        # --- B. numbers in spec with no home in facts.csv ---
        fact_nums = set()
        for f in facts:
            fact_nums |= numbers(f["value"])
        loose = sorted(n for n in numbers(spec) - fact_nums
                       if len(n) > 1 or n in {"2", "3", "4", "5", "6", "7", "8", "9"})
        if loose:
            orphan_nums.append((it, ", ".join(loose)))

        # --- C. fictional difference points ---
        if meta["item_type"] == "fictional":
            dps = meta.get("difference_points") or []
            dp_rows = [f["field"] for f in facts if f["source_type"] == "difference_point"]
            diffs.append((it, meta["name"], " / ".join(dps), ", ".join(dp_rows) or "—"))

        # --- D. source-quality flags ---
        for f in facts:
            if f["source_type"] == "review_consensus":
                doms = {domain(u) for u in f["source_url"].split(";") if u.strip()}
                if len(doms) < 2:
                    flags.append((it, f["field"], "consensus from <2 distinct domains",
                                  "; ".join(sorted(doms))))
            if f["note"] and re.search(r"verify|discrepanc|conflict|inconsistent|low-confidence|blocked|caveat|omitted|renamed",
                                       f["note"], re.I):
                flags.append((it, f["field"], "note flag", f["note"][:110]))
            if meta["item_type"] == "real" and f["source_type"] == "official":
                host = domain(f["source_url"])
                brand = re.split(r"[ \-]", meta["name"])[0].lower().replace("'", "")
                if brand and brand[:5] not in host.replace("-", ""):
                    flags.append((it, "(多个字段)", "official row on third-party host", host))

        n_official = sum(1 for f in facts if f["source_type"] == "official")
        n_rc = sum(1 for f in facts if f["source_type"] == "review_consensus")
        signoff.append((it, meta["name"], meta["item_type"], len(facts), n_official, n_rc))

    L = []
    L.append("# 材料验证清单（自动生成，勿手改；改材料后重跑 `python3 src/make_review_sheet.py`）\n")
    L.append("一张表看完所有需要人工判断的地方。脚本已把住的（词数/禁词/条目数/溯源有效性/≥2源）不在此列。\n")

    susp = [t for t in tradeoffs if t[0]]
    clean = [t for t in tradeoffs if not t[0]]
    L.append(f"\n## A. 优缺点权衡对（共 {len(tradeoffs)} 处，其中 **{len(susp)} 处需你判断**）\n")
    L.append("同一事实字段同时支撑一优一缺。判断标准：**权衡**（同一属性的两面，保留）还是"
             "**同说法重述**（把同一句话正反说一遍，应改掉其中一条）。\n")
    L.append(f"### A1. 需判断（{len(susp)} 处）——优缺点措辞高度重叠\n")
    L.append("| ✓ | 提示 | 物品 | 字段 | 优点 | 缺点 |")
    L.append("|---|---|---|---|---|---|")
    for sev, it, ff, p, c in susp:
        L.append(f"| ☐ | {sev} | {it} | `{ff}` | {p} | {c} |")
    L.append(f"\n<details><summary>A2. 已判定为正常权衡（{len(clean)} 处，抽查即可）</summary>\n")
    L.append("| 物品 | 字段 | 优点 | 缺点 |")
    L.append("|---|---|---|---|")
    for sev, it, ff, p, c in clean:
        L.append(f"| {it} | `{ff}` | {p} | {c} |")
    L.append("\n</details>")

    L.append(f"\n## B. 说明书中未在事实表出现的数字（{len(orphan_nums)} 个物品）\n")
    L.append("说明书里的数字应当能在 facts.csv 找到对应。下列数字未匹配——多为拼写形式差异"
             "（如 `9-1/2` vs `9.5`）或转述单位，**请确认不是凭空写入的事实**。\n")
    L.append("| ✓ | 物品 | 未匹配的数字 |")
    L.append("|---|---|---|")
    for it, ns in orphan_nums:
        L.append(f"| ☐ | {it} | {ns} |")

    L.append(f"\n## C. 虚构物品的差异点（{len(diffs)} 个）\n")
    L.append("**判断标准：是功能差异（有无某特性、布局不同）还是品质差异（更差的版本）**。"
             "品质差异会让 real/fictional 对比混入优劣，必须改。\n")
    L.append("| ✓ | 物品 | 名称 | 声明的差异点 | facts.csv 中标记的差异字段 |")
    L.append("|---|---|---|---|---|")
    for it, name, dps, rows in diffs:
        L.append(f"| ☐ | {it} | {name} | {dps} | `{rows}` |")

    seen = set()
    uniq = [f for f in flags if not (f[:3] in seen or seen.add(f[:3]))]
    prio = {"consensus from <2 distinct domains": 0, "official row on third-party host": 1, "note flag": 2}
    uniq.sort(key=lambda f: (prio.get(f[2], 9), f[0]))
    hard = [f for f in uniq if f[2] != "note flag"]
    soft = [f for f in uniq if f[2] == "note flag"]
    L.append(f"\n## D. 来源质量提示（共 {len(uniq)} 条，其中 **{len(hard)} 条需你判断**）\n")
    L.append(f"### D1. 需判断（{len(hard)} 条）——来源独立性或权威性存疑\n")
    L.append("| ✓ | 物品 | 字段 | 类型 | 详情 |")
    L.append("|---|---|---|---|---|")
    for it, ff, kind, detail in hard:
        L.append(f"| ☐ | {it} | `{ff}` | {kind} | {detail} |")
    L.append(f"\n<details><summary>D2. 已在 note 中记录的矛盾与回避（{len(soft)} 条，抽查即可）</summary>\n")
    L.append("| 物品 | 字段 | note |")
    L.append("|---|---|---|")
    for it, ff, kind, detail in soft:
        L.append(f"| {it} | `{ff}` | {detail} |")
    L.append("\n</details>")

    L.append("\n## E. 逐物品签字表\n")
    L.append("| ✓ | 物品 | 名称 | 类型 | 事实行 | 官方 | 评测共识 |")
    L.append("|---|---|---|---|---|---|---|")
    for it, name, typ, n, no, nr in signoff:
        L.append(f"| ☐ | {it} | {name} | {typ} | {n} | {no} | {nr} |")

    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(tradeoffs)} tradeoffs, "
          f"{len(orphan_nums)} items with loose numbers, {len(diffs)} fictional, "
          f"{len(uniq)} source flags, {len(signoff)} items")


if __name__ == "__main__":
    main()
