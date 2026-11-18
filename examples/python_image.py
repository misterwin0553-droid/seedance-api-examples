#!/usr/bin/env python3
"""API-Finder image generation — OpenAI-compatible endpoint.

POST /v1/images/generations accepts the OpenAI Images payload, so the
official OpenAI SDK works too: just point base_url at
https://api-finder.com/v1 and use your API-Finder key.

This example uses raw HTTP (stdlib only).
"""
import json
import os
import urllib.request

BASE = "https://api-finder.com"
KEY = os.environ["API_FINDER_KEY"]

body = {
    "model": "gpt-image-2.5-flare",  # per-image billing; check live rates on the pricing page
    "prompt": "Arabic oud perfume bottle product photo, dark background, gold particles",
    "n": 1,
    "size": "1024x1024",
    "response_format": "b64_json",  # recommended; the sync call can take 35-65s, set timeouts >=150s
}

req = urllib.request.Request(
    BASE + "/v1/images/generations",
    method="POST",
    data=json.dumps(body).encode(),
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as r:
    print(r.read().decode())
