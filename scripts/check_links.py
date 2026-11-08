#!/usr/bin/env python3
"""Best-effort connectivity checks only, never auto-edit parish data."""
import json, pathlib, urllib.request, time
root=pathlib.Path(__file__).resolve().parents[1]
doc=json.loads((root/'data'/'parishes.json').read_text(encoding='utf-8'))
urls=sorted({row[k] for row in doc['parishes'] for k in ('source','website') if row.get(k)})
lines=['# Parish website reachability report','',f'Checked {len(urls)} distinct URLs. HTTP errors and blocks can be transient; review manually.','']
for url in urls:
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'CatholicCompassParishDirectory/1.0 (scheduled link checks)'},method='HEAD')
  with urllib.request.urlopen(req,timeout=12) as res: status=res.status
  result='OK' if status<400 else f'HTTP {status}'
 except Exception as exc:result=f'REVIEW: {type(exc).__name__}: {str(exc)[:120]}'
 lines.append(f'- {result} — {url}')
 time.sleep(0.3)
report=root/'link-check-report.md';report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Report saved: {report}')
