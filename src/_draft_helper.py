"""Helper for writing raw item drafts. Used by the batch drafting scripts.

write_item(item_id, facts, spec, pros12, cons8) writes facts.csv,
spec_draft.md and entries_draft.json in the canonical format. Pros are
supplied as 12 tuples; the first 8 become tier "core8", the last 4
"extra4".
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data" / "raw" / "items"
AD = "2026-08-13"


def write_item(item_id, facts, spec, pros12, cons8):
    """facts: list of (field, value, source_type, source_url, note)
       spec: str (140-160 words)
       pros12/cons8: list of (entry_id, text, fact_field)"""
    d = D / item_id
    with open(d / "facts.csv", "w", encoding="utf-8", newline="\n") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["field", "value", "source_type", "source_url", "accessed_date", "note"])
        for row in facts:
            field, value, st, url, note = row
            w.writerow([field, value, st, url, AD, note])
    (d / "spec_draft.md").write_text(spec.strip() + "\n", encoding="utf-8")
    entries = {
        "pros": [{"entry_id": eid, "valence": "pro",
                  "tier": "core8" if i < 8 else "extra4",
                  "text_draft": t, "fact_field": ff}
                 for i, (eid, t, ff) in enumerate(pros12)],
        "cons": [{"entry_id": eid, "valence": "con", "tier": "core8",
                  "text_draft": t, "fact_field": ff}
                 for (eid, t, ff) in cons8],
    }
    with open(d / "entries_draft.json", "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
        f.write("\n")


def set_diffs(item_id, diffs):
    p = D / item_id / "meta.json"
    m = json.loads(p.read_text(encoding="utf-8"))
    m["difference_points"] = diffs
    p.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def P(*rows):
    """shorthand: build pro/con tuple lists"""
    return list(rows)
