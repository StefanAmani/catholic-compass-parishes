#!/usr/bin/env python3
import json, pathlib, re
from urllib.parse import urlparse
path=pathlib.Path(__file__).resolve().parents[1]/'data'/'parishes.json'
doc=json.loads(path.read_text(encoding='utf-8'))
assert doc['schemaVersion']==1 and isinstance(doc['directoryVersion'],int) and doc['directoryVersion']>=1
rows=doc['parishes'];assert isinstance(rows,list) and len(rows)>0
ids=set();keys=set()
for row in rows:
  for k in ('id','name','street','city','zip','state','website','source'):
    assert k in row and isinstance(row[k],str), f'Missing/invalid {k}: {row}'
  assert row['id'] not in ids, f'Duplicate id: {row["id"]}';ids.add(row['id'])
  assert row['state'] in ('TN','WI')
  assert re.fullmatch(r'\d{5}',row['zip'])
  assert row['name'].strip() and row['city'].strip() and row['street'].strip()
  for key in ('website','source'):
    if row[key]:
      u=urlparse(row[key]);assert u.scheme=='https' and u.hostname, f'Invalid URL: {row[key]}'
  key=(row['state'].lower(),row['city'].lower(),row['name'].lower(),row['street'].lower())
  assert key not in keys,f'Duplicate listing: {key}';keys.add(key)
print(f'OK: {len(rows)} parish records; version {doc["directoryVersion"]}')
