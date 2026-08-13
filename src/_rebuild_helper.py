import csv, json, re
from pathlib import Path
AD="2026-08-13"
def build(iid, briefing, newfacts, pros, cons):
    """briefing: str ~300w | newfacts: [(field,value,src_type,url,note)] appended
       pros/cons: [(entry_id, text, fact_field)]"""
    d=Path(f"data/raw/items/{iid}")
    t=" ".join(briefing.split())
    n=len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'&.-]*", t))
    (d/"spec_draft.md").write_text(t+"\n")
    if newfacts:
        p=d/"facts.csv"; rows=list(csv.DictReader(open(p,encoding="utf-8")))
        cols=list(rows[0].keys())
        have={r["field"] for r in rows}
        for f,v,st,u,note in newfacts:
            if f in have:
                for r in rows:
                    if r["field"]==f: r["value"]=v; r["source_type"]=st; r["source_url"]=u; r["note"]=note
            else:
                rows.append({"field":f,"value":v,"source_type":st,"source_url":u,
                             "accessed_date":AD,"note":note,"in_spec":""})
        with open(p,"w",encoding="utf-8",newline="\n") as fh:
            w=csv.DictWriter(fh,fieldnames=cols,lineterminator="\n"); w.writeheader()
            for r in rows: w.writerow({c:r.get(c,"") for c in cols})
    have={r["field"] for r in csv.DictReader(open(d/"facts.csv",encoding="utf-8"))}
    miss=sorted({x[2] for x in pros+cons}-have)
    if miss: print(f"{iid}: MISSING FACT ROWS -> {miss}")
    e={"pros":[{"entry_id":i,"valence":"pro","tier":"core8" if k<8 else "extra4",
                "text_draft":t_,"fact_field":ff} for k,(i,t_,ff) in enumerate(pros)],
       "cons":[{"entry_id":i,"valence":"con","tier":"core8","text_draft":t_,"fact_field":ff}
               for i,t_,ff in cons]}
    (d/"entries_draft.json").write_text(json.dumps(e,ensure_ascii=False,indent=2)+"\n")
    dist=len({x[2] for x in pros}|{x[2] for x in cons})
    sh=len({x[2] for x in pros}&{x[2] for x in cons})
    flag = "" if (285<=n<=320 and dist>=18 and sh<=2) else f"  << w={n} distinct={dist} shared={sh}"
    print(f"{iid}: {n}w distinct={dist} shared={sh}{flag}")

# Usage from a script run at repo root:
#   import sys; sys.path.insert(0,'src'); from _rebuild_helper import build
#   build(item_id, briefing_text, [(field,value,source_type,url,note), ...],
#         [(entry_id, text, fact_field) x12], [(entry_id, text, fact_field) x8])
# build() prints word count, distinct-field count, shared count, and any
# fact_field referenced by an entry that has no row in facts.csv.
