#!/usr/bin/env python3
"""API-Finder / Seedance video generation — Python example (stdlib only).

1) Register free at https://api-finder.com and create an API key
2) export API_FINDER_KEY=sk-...
3) python3 python_generate.py "Dubai skyline at dusk, cinematic drone shot"
"""
import json
import os
import sys
import time
import urllib.request

BASE = "https://api-finder.com"
KEY = os.environ["API_FINDER_KEY"]
MODEL = os.environ.get("MODEL", "seedance-2.5-flash-YH")  # cheapest 2.5 line
PROMPT = sys.argv[1] if len(sys.argv) > 1 else "Dubai skyline at dusk, cinematic drone shot"


def call(method, path, body=None):
    req = urllib.request.Request(
        BASE + path,
        method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return r.read()


job = json.loads(call("POST", "/v1/videos", {"model": MODEL, "prompt": PROMPT}))
job_id = job.get("id") or job.get("task_id")
print("Job submitted:", job_id)

while True:
    info = json.loads(call("GET", f"/v1/videos/{job_id}"))
    status = info.get("status", "")
    print("status:", status)
    if status in ("succeeded", "completed", "success", "done"):
        break
    if status in ("failed", "error", "cancelled", "canceled"):
        raise SystemExit(f"Job failed: {info}")
    time.sleep(5)

video = call("GET", f"/v1/videos/{job_id}/content")
with open("output.mp4", "wb") as f:
    f.write(video)
print("Saved output.mp4")
