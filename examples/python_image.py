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
    "model": "gpt-image-2.5-flare",  # ¥0.3313/image on the pricing page; check live rates
    "prompt": "Arabic oud perfume bottle product photo, dark background, gold particles",
}

req = urllib.request.Request(
    BASE + "/v1/images/generations",
    method="POST",
    data=json.dumps(body).encode(),
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as r:
    print(r.read().decode())
