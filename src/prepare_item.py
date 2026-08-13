#!/usr/bin/env python3
"""Materials pipeline for the Ease-of-Retrieval study.

Drives an item through the raw-data stage: skeleton creation, source
fetching/archiving, format validation, and packaging for the style-
neutralization (rewrite) step. Adding a new item = add one entry to
src/items_registry.json, then:

    python3 src/prepare_item.py init c27_newthing_real
    python3 src/prepare_item.py fetch c27_newthing_real      # archive official/review pages
    #   ... fill facts.csv / spec_draft.md / entries_draft.json (researcher or agent) ...
    python3 src/prepare_item.py validate c27_newthing_real
    python3 src/prepare_item.py package-rewrite c27_newthing_real

`--all` runs a subcommand over every registry item. `status` prints the
pipeline state of everything. Stdlib only; no API calls happen here —
model calls (MiniMax rewrite, reviewer checks, norming) are separate
stages that consume the payloads this script emits.
"""

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW_ITEMS = DATA / "raw" / "items"
NEUTRAL_IN = DATA / "neutralization" / "input"
REGISTRY = ROOT / "src" / "items_registry.json"
RULES = ROOT / "src" / "format_rules.json"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

# ---------------------------------------------------------------- helpers


def load_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def registry():
    return load_json(REGISTRY)


def rules():
    return load_json(RULES)


def item_dir(item_id: str) -> Path:
    return RAW_ITEMS / item_id


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'&.-]*", text))


def set_status(item_id: str, status: str):
    meta_path = item_dir(item_id) / "meta.json"
    meta = load_json(meta_path)
    meta["status"] = status
    dump_json(meta_path, meta)


# ---------------------------------------------------------------- init


def cmd_init(item_id: str):
    reg = registry()
    if item_id not in reg["items"]:
        sys.exit(f"[init] {item_id} not in registry — add it to src/items_registry.json first")
    entry = reg["items"][item_id]
    d = item_dir(item_id)
    if (d / "meta.json").exists():
        print(f"[init] {item_id}: already initialized, skipping")
        return
    d.mkdir(parents=True, exist_ok=True)
    (d / "sources_archive").mkdir(exist_ok=True)

    dump_json(d / "meta.json", {
        "item_id": item_id,
        "category_num": entry["category_num"],
        "category": entry["category"],
        "category_pair_id": f"c{entry['category_num']:02d}",
        "item_type": entry["item_type"],
        "name": entry["name"],
        "paired_item": entry["paired_item"],
        "difference_points": entry.get("difference_points"),
        "status": "registered",
    })

    dump_json(d / "sources.json", {
        "official": [
            {"url": u, "fetch_status": "pending", "accessed_date": None}
            for u in entry.get("official_urls", [])
        ],
        "reviews": [
            {"url": u, "fetch_status": "pending", "accessed_date": None}
            for u in entry.get("review_urls", [])
        ],
    })

    with open(d / "facts.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["field", "value", "source_type", "source_url", "accessed_date", "note"])

    (d / "spec_draft.md").write_text(
        "<!-- 150±10 words. Field order: positioning sentence -> 5-6 specs -> "
        "accessories -> maintenance. No evaluative words (see src/format_rules.json). "
        "Every figure must have a row in facts.csv. -->\n",
        encoding="utf-8",
    )

    dump_json(d / "entries_draft.json", {"pros": [], "cons": []})
    print(f"[init] {item_id}: skeleton created")


# ---------------------------------------------------------------- fetch


def cmd_fetch(item_id: str):
    d = item_dir(item_id)
    sources_path = d / "sources.json"
    sources = load_json(sources_path)
    today = date.today().isoformat()
    n_ok = n_fail = 0
    for group in ("official", "reviews"):
        for src in sources.get(group, []):
            url = src["url"]
            slug = re.sub(r"[^a-z0-9]+", "_", url.lower())[:80]
            out = d / "sources_archive" / f"{group}_{slug}.html"
            try:
                req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    body = resp.read()
                out.write_bytes(body)
                src["fetch_status"] = "archived"
                src["accessed_date"] = today
                src["archive_file"] = out.name
                src["sha256"] = hashlib.sha256(body).hexdigest()
                n_ok += 1
            except Exception as e:  # bot walls, timeouts, 403s — record and move on
                src["fetch_status"] = f"blocked: {type(e).__name__}"
                src["accessed_date"] = today
                n_fail += 1
    dump_json(sources_path, sources)
    meta = load_json(d / "meta.json")
    if meta["status"] == "registered":
        set_status(item_id, "sourcing")
    print(f"[fetch] {item_id}: {n_ok} archived, {n_fail} blocked "
          f"(blocked pages: fetch via browser and drop the text into "
          f"{d / 'sources_archive'}/ manually, then note it in sources.json)")


# ---------------------------------------------------------------- validate


def _load_entries(d: Path):
    entries = load_json(d / "entries_draft.json")
    return entries.get("pros", []), entries.get("cons", [])


def _fact_fields(d: Path):
    fields = set()
    with open(d / "facts.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            fields.add(row["field"])
    return fields


def cmd_validate(item_id: str):
    d = item_dir(item_id)
    r = rules()
    problems, warnings = [], []

    meta = load_json(d / "meta.json")
    if meta["item_type"] == "fictional" and not meta.get("difference_points"):
        problems.append("fictional item must declare 2-3 difference_points in meta.json")

    # --- spec sheet ---
    spec = re.sub(r"<!--.*?-->", "", (d / "spec_draft.md").read_text(encoding="utf-8"),
                  flags=re.S).strip()
    if not spec:
        problems.append("spec_draft.md is empty")
    else:
        wc = word_count(spec)
        lo, hi = r["spec_word_range"]
        if not lo <= wc <= hi:
            problems.append(f"spec sheet word count {wc} outside [{lo}, {hi}]")
        for bad in r["banned_words"]:
            if re.search(rf"\b{re.escape(bad)}\b", spec, re.I):
                problems.append(f"spec sheet contains banned word: '{bad}'")
        for pat in r.get("banned_attribution_patterns", []):
            m = re.search(pat, spec, re.I)
            if m:
                problems.append(f"briefing attributes a fact ('{m.group(0).strip()}') — state it "
                                f"directly; fictional items have no reviewers, so attribution "
                                f"marks an item as real")

    # --- facts ---
    fact_fields = _fact_fields(d)
    if not fact_fields:
        problems.append("facts.csv has no rows")
    with open(d / "facts.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["source_type"] in ("official", "review_consensus") and not row["source_url"]:
                problems.append(f"fact '{row['field']}' ({row['source_type']}) lacks source_url")
            if row["source_type"] == "review_consensus" and len(row["source_url"].split(";")) < 2:
                problems.append(f"fact '{row['field']}' claims review consensus with <2 sources")

    # --- grounding: which fact rows the briefing states or implies ---
    in_spec = {}
    with open(d / "facts.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            in_spec[row["field"]] = (row.get("in_spec") or "").strip() or "no"

    # --- entries ---
    pros, cons = _load_entries(d)
    core8 = [p for p in pros if p.get("tier") == "core8"]
    extra4 = [p for p in pros if p.get("tier") == "extra4"]
    if (len(core8), len(extra4), len(cons)) != (8, 4, 8):
        problems.append(f"entry counts wrong: core8={len(core8)} extra4={len(extra4)} "
                        f"cons={len(cons)} (need 8/4/8)")
    lo, hi = r["entry_word_range"]
    pro_fields, con_fields = set(), set()
    for e in pros + cons:
        text = e.get("text_draft", "")
        wc = word_count(text)
        if not lo <= wc <= hi:
            problems.append(f"{e.get('entry_id', '?')} word count {wc} outside [{lo}, {hi}]: {text!r}")
        for bad in r["banned_words"]:
            if re.search(rf"\b{re.escape(bad)}\b", text, re.I):
                problems.append(f"{e.get('entry_id', '?')} contains banned word '{bad}'")
        ff = e.get("fact_field")
        if not ff:
            problems.append(f"{e.get('entry_id', '?')} has no fact_field")
        elif ff not in fact_fields:
            problems.append(f"{e.get('entry_id', '?')} fact_field '{ff}' not in facts.csv")
        elif in_spec.get(ff, "no") == "no":
            problems.append(f"{e.get('entry_id', '?')} rests on '{ff}', which the briefing "
                            f"does not state or imply (no tier-3 entries allowed)")
        (pro_fields if e in pros else con_fields).add(ff)
    hedges = r.get("hedge_words", [])
    def hcount(entries):
        return sum(1 for e in entries
                   if any(re.search(rf"\b{re.escape(h)}\b", e.get("text_draft",""), re.I)
                          for h in hedges))
    hp, hc = hcount(pros), hcount(cons)
    if abs(hp / max(1, len(pros)) - hc / max(1, len(cons))) > 0.34:
        warnings.append(f"hedging asymmetry: {hp}/{len(pros)} pros vs {hc}/{len(cons)} cons "
                        f"use hedge words — cons must not read softer than pros (E6 confound)")

    core = [e for e in pros if e.get("tier") == "core8"] + cons
    n_core = len(set(e.get("fact_field") for e in core if e.get("fact_field")))
    if n_core < r.get("min_distinct_core16", 16):
        problems.append(f"only {n_core} distinct fact_fields across the 8 core pros and 8 cons "
                        f"(need {r['min_distinct_core16']}) — core entries are recycling facts")
    n_distinct = len(set(e.get("fact_field") for e in pros + cons if e.get("fact_field")))
    if n_distinct < 20:
        warnings.append(f"extra4 fallback in use: {n_distinct}/20 distinct fields "
                        f"(extra4 pros reuse core fields; item is lower priority for E4)")
    n_shared = len(set(f for f in pro_fields if f) & set(f for f in con_fields if f))
    if n_shared > r.get("max_shared_pro_con_fields", 2):
        problems.append(f"{n_shared} fields support both a pro and a con "
                        f"(max {r['max_shared_pro_con_fields']})")

    both = (pro_fields & con_fields) - set(r.get("contradiction_whitelist", []))
    for ff in sorted(x for x in both if x):
        warnings.append(f"fact_field '{ff}' used by both a pro and a con — check no contradiction")

    for w in warnings:
        print(f"[validate] {item_id} WARN: {w}")
    if problems:
        for p in problems:
            print(f"[validate] {item_id} FAIL: {p}")
        return False
    set_status(item_id, "validated")
    print(f"[validate] {item_id}: OK ({len(warnings)} warnings)")
    return True


# ---------------------------------------------------------------- package-rewrite


def cmd_package_rewrite(item_id: str):
    d = item_dir(item_id)
    meta = load_json(d / "meta.json")
    if meta["status"] not in ("validated", "rewrite_packaged"):
        sys.exit(f"[package-rewrite] {item_id} status is '{meta['status']}', must pass validate first")
    r = rules()
    spec = re.sub(r"<!--.*?-->", "", (d / "spec_draft.md").read_text(encoding="utf-8"),
                  flags=re.S).strip()
    facts = list(csv.DictReader(open(d / "facts.csv", encoding="utf-8")))
    pros, cons = _load_entries(d)

    payload = {
        "item_id": item_id,
        "task": "style_neutralization",
        "instructions": {
            "role": "You rewrite draft research materials so no authoring model's style "
                    "remains. Preserve every fact exactly; change only wording.",
            "entry_constraints": [
                f"each entry {r['entry_word_range'][0]}-{r['entry_word_range'][1]} words",
                "start with a noun phrase",
                "no evaluative/marketing words: " + ", ".join(r["banned_words"]),
                "do not add, drop, or alter any factual content",
            ],
            "spec_constraints": [
                f"{r['spec_word_range'][0]}-{r['spec_word_range'][1]} words",
                "keep field order: positioning sentence, specs, accessories, maintenance",
                "no evaluative/marketing words",
                "every figure must remain identical",
            ],
            "return_format": {
                "spec": {"text_neutralized": "...", "changed": "bool"},
                "entries": [{"entry_id": "...", "text_neutralized": "...",
                             "changed": "bool", "rewrite_note": "..."}],
            },
        },
        "spec_draft": spec,
        "entries": [
            {"entry_id": e["entry_id"], "valence": e["valence"], "tier": e.get("tier"),
             "text_draft": e["text_draft"],
             "fact": next((f for f in facts if f["field"] == e.get("fact_field")), None)}
            for e in pros + cons
        ],
        "source_hash": hashlib.sha256(
            (spec + json.dumps(pros + cons, sort_keys=True)).encode()).hexdigest(),
    }
    dump_json(NEUTRAL_IN / f"{item_id}.json", payload)
    set_status(item_id, "rewrite_packaged")
    print(f"[package-rewrite] {item_id}: payload -> data/neutralization/input/{item_id}.json")


# ---------------------------------------------------------------- status


def cmd_status():
    reg = registry()
    counts = {}
    for item_id in sorted(reg["items"]):
        meta_path = item_dir(item_id) / "meta.json"
        st = load_json(meta_path)["status"] if meta_path.exists() else "(not initialized)"
        counts[st] = counts.get(st, 0) + 1
        print(f"{item_id:28s} {st}")
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))


# ---------------------------------------------------------------- main

COMMANDS = {
    "init": cmd_init,
    "fetch": cmd_fetch,
    "validate": cmd_validate,
    "package-rewrite": cmd_package_rewrite,
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=list(COMMANDS) + ["status"])
    ap.add_argument("item_id", nargs="?", help="item id, or use --all")
    ap.add_argument("--all", action="store_true", help="run over every registry item")
    args = ap.parse_args()

    if args.command == "status":
        cmd_status()
        return
    fn = COMMANDS[args.command]
    if args.all:
        results = [fn(item_id) for item_id in sorted(registry()["items"])]
        if args.command == "validate" and not all(r is not False for r in results):
            sys.exit(1)
    elif args.item_id:
        fn(args.item_id)
    else:
        sys.exit("need an item_id or --all")


if __name__ == "__main__":
    main()
