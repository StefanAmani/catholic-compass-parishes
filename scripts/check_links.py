#!/usr/bin/env python3
"""Informational website checks. Does not change parish records or assert authenticity."""
import json
import pathlib
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse

root = pathlib.Path(__file__).resolve().parents[1]
data = json.loads((root / "data/parishes.json").read_text(encoding="utf-8"))
parishes = data["parishes"]
# Limit requests to listed parish websites, not diocesan directory source pages.
urls = sorted({p["website"].strip() for p in parishes if p.get("website", "").strip()})
lines = [
    "# Parish website verification queue",
    "",
    f"Directory version: {data['directoryVersion']}",
    f"Records: {len(parishes)}; nonempty website URLs: {len(urls)}",
    "",
    "These are reachability tests, NOT proof that a URL is the correct or official parish website.",
    "403/429, timeouts, and other failures can result from bot protection. Review them manually.",
    "The job never edits or deletes directory entries.",
    "",
]
results = {}
for url in urls:
    try:
        host = urlparse(url).hostname or ""
        if not host:
            raise ValueError("URL has no hostname")
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (compatible; CatholicCompassLinkAudit/1.0)"},
            method="HEAD")
        try:
            resp = urllib.request.urlopen(req, timeout=8)
        except urllib.error.HTTPError as err:
            if err.code not in (403, 405, 501):
                raise
            # HEAD may be refused while GET works; only retrieve a small range.
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0 (compatible; CatholicCompassLinkAudit/1.0)",
                              "Range": "bytes=0-1023"}, method="GET")
            resp = urllib.request.urlopen(req, timeout=8)
        with resp:
            final_url = resp.geturl()
            status = resp.status
        status_text = "reachable" if status < 400 else f"HTTP {status}"
        if url.rstrip("/") != final_url.rstrip("/"):
            status_text += f"; redirects to {final_url}"
    except Exception as exc:
        status_text = f"REVIEW {type(exc).__name__}: {str(exc)[:110]}"
    results[url] = status_text
    time.sleep(0.15)
for parish in parishes:
    url = parish.get("website", "").strip()
    if not url:
        continue
    lines.append(f"- **{parish['name']} ({parish['city']}, {parish['state']})**: {results[url]} — {url}")
(root / "link-check-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote link-check-report.md with {len(urls)} URLs")
