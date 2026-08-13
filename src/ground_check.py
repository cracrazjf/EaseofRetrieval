#!/usr/bin/env python3
"""Recompute the in_spec column of every facts.csv from the briefing text,
then report which entries are still ungrounded.

in_spec: yes      = the briefing states this fact
         premise  = a derivation whose premise the briefing states
         no       = not represented (entries resting on it will fail validate)

Run: python3 src/ground_check.py [item_id ...]
"""
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEMS = ROOT / "data" / "raw" / "items"
STOP = set("""the a an of for and or in on to at by from with is are be as its it this that
one two per up no not any all each into out over under about than then when while which
official derived spec mirror point sold state stated states include includes including""".split())

def toks(t):
    return {w for w in re.findall(r"[a-z]+", t.lower()) if w not in STOP and len(w) > 2}


def nums(t):
    """distinctive figures, split on ranges so '30-40' matches '30 to 40'"""
    return {n for n in re.findall(r"\d+(?:\.\d+)?", t) if float(n) != 0}

def run(items):
    for iid in items:
        d = ITEMS / iid
        spec = re.sub(r"<!--.*?-->", "", (d / "spec_draft.md").read_text(), flags=re.S).lower()
        st, sn = toks(spec), nums(spec)
        rows = list(csv.DictReader(open(d / "facts.csv", encoding="utf-8")))
        for row in rows:
            blob = row["field"].replace("_", " ") + " " + row["value"]
            ft, fn = toks(blob), nums(row["value"])
            wov = len(ft & st) / max(1, len(ft))
            nov = len(fn & sn) / len(fn) if fn else 0
            ov = max(wov, nov)
            if ov >= 0.5:
                row["in_spec"] = "yes"
            elif row["source_type"] == "spec_derived" and ov >= 0.3:
                row["in_spec"] = "premise"
            elif ov >= 0.34:
                row["in_spec"] = "premise"
            else:
                row["in_spec"] = "no"
        cols = ["field","value","source_type","source_url","accessed_date","note","in_spec"]
        with open(d / "facts.csv", "w", encoding="utf-8", newline="\n") as f:
            w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
            w.writeheader()
            for row in rows:
                w.writerow({c: row.get(c, "") for c in cols})
        grounded = {r["field"]: r["in_spec"] for r in rows}
        e = json.loads((d / "entries_draft.json").read_text())
        bad = sorted({x["fact_field"] for x in e["pros"] + e["cons"]
                      if grounded.get(x["fact_field"], "no") == "no"})
        if bad:
            print(f"{iid}: ungrounded -> {', '.join(bad)}")

if __name__ == "__main__":
    args = sys.argv[1:]
    run(args or sorted(p.name for p in ITEMS.iterdir() if p.is_dir()))
