#!/usr/bin/env python3
"""Report directory gaps without inventing parish coverage or overwriting records."""
import collections
import json
import pathlib

root=pathlib.Path(__file__).resolve().parents[1]
d=json.loads((root/"data/parishes.json").read_text(encoding="utf-8"))
rows=d["parishes"]
domains={
 "TN": [
  ("Nashville","dioceseofnashville.com"),
  ("Knoxville","dioknox.org"),
  ("Memphis","cdom.org")],
 "WI": [
  ("Milwaukee","archmil.org"),
  ("Madison","madisondiocese.org"),
  ("Green Bay","gbdioc.org"),
  ("La Crosse","diolc.org"),
  ("Superior","catholicdos.org")]}
lines=[
 "# Catholic Compass coverage & quality audit","",
 f"Directory version: {d['directoryVersion']}",
 f"Total listings: {len(rows)}",
 "",
 "**Important:** Record counts are not evidence that a diocese is complete.",
 "Parishes with multiple church buildings may legitimately have multiple records.",
 "No record must be removed or marked closed solely from these checks.",
 "",
 "## Records attributed to diocesan sources","",
 "| State | Diocese | Records |",
 "|---|---|---:|"]
for state, pairs in domains.items():
 for name,domain in pairs:
  count=sum(domain in r["source"].lower() for r in rows if r["state"]==state)
  lines.append(f"| {state} | {name} | {count} |")
lines+=["","## Missing official parish websites",""]
missing=[p for p in rows if not p.get("website","").strip()]
lines.append(f"{len(missing)} of {len(rows)} listings have no parish website recorded. These should not show a guessed website link.")
lines+=["","## Repeated street addresses to review (may be legitimate)",""]
by_address=collections.defaultdict(list)
for p in rows:
 key=(p["state"],p["city"].casefold().strip(),p["street"].casefold().strip())
 by_address[key].append(p["name"])
repeated=[(key,names) for key,names in by_address.items() if len(names)>1]
if not repeated:lines.append("None.")
for (state,city,street),names in repeated:
 lines.append(f"- {city.title()}, {state}, {street}: {' / '.join(names)}")
lines+=["","## Required human verification","",
"- Compare ALL church buildings, missions, parish mergers and parish names with all eight current diocesan directories.",
"- Check each proposed website against parish identity and address; a HTTP 200 response alone is not enough.",
"- Confirm diocesan directory licensing/terms before automated harvesting.",
"- Do not claim statewide completeness until the directory-by-directory reconciliation is signed off.",
""]
(root/"coverage-audit.md").write_text("\n".join(lines),encoding="utf-8")
print(f"Coverage audit: {len(rows)} records, {len(missing)} missing websites, {len(repeated)} shared addresses")
