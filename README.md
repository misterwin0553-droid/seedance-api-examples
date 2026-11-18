# Seedance API Examples — API-Finder

Minimal, copy-paste examples for generating AI videos with the **Seedance 2.0 / 2.5**
models through the [API-Finder](https://api-finder.com) REST API.

- **Per-second billing** — no monthly fee, no minimum spend
- **Failed jobs are refunded automatically**
- **Pay with Stripe or USDT** (top-up from $10)
- **Free to register** — grab a key in the console and run an example below
- Support: Telegram [@APIFinder_Support](https://t.me/APIFinder_Support) · api-finder@foxmail.com

> Prices below are indicative — always check the live [pricing page](https://api-finder.com/pricing).

## Quickstart (3 steps)

```text
1. POST /v1/videos            → submit a job, get an id
2. GET  /v1/videos/{id}       → poll status (~every 5s): queued → in_progress → completed / failed
3. GET  /v1/videos/{id}/content → download the finished video
```

Submit body: `model` + `prompt` are required; `seconds` (default 5),
`resolution` (default 720p) and `ratio` are optional — see the
[official docs](https://api-finder.com/docs).

Base URL: `https://api-finder.com` · Auth: `Authorization: Bearer sk-...`

## Examples

| File | What it does |
|---|---|
| [`examples/curl.sh`](examples/curl.sh) | Submit → poll → download, pure bash + curl |
| [`examples/python_generate.py`](examples/python_generate.py) | Same flow in Python (stdlib only, no pip installs) |
| [`examples/node_generate.mjs`](examples/node_generate.mjs) | Same flow in Node.js 18+ (built-in fetch) |
| [`examples/python_image.py`](examples/python_image.py) | Image generation via the OpenAI-compatible endpoint |

## Models (IDs as listed on the pricing page, 2026-11-19)

Video — per-second lines (YH):

| Model ID | Notes |
|---|---|
| `seedance-2.5-YH` | Seedance 2.5, 4–30s |
| `seedance-2.5-stable-YH` | Seedance 2.5 Stable |
| `seedance-2.5-flash-YH` | Seedance 2.5 Flash — cheapest 2.5 line |
| `seedance-2.0-YH` | Seedance 2.0, 4–15s |
| `seedance-2.0-fast-YH` | Seedance 2.0 Fast |
| `seedance-2.0-mini-YH` | Seedance 2.0 Mini — cheapest 2.0 line |
| `wan3-YH` | Wan 3.0 — cheapest overall |

Video — official token-billed lines (docs IDs, `doubao-` prefix):
`doubao-seedance-2-5-261111`, `doubao-seedance-2-0-261111`,
`doubao-seedance-2-0-fast-261111`, `doubao-seedance-2-0-mini-261111`
(the 2.0 official line is the only one with 4K, and can generate audio).

Image (per image): `gpt-image-2.5-flare`, `gpt-image-2.5-flare-02`,
`gpt-image-2.5-sunburst`, `gpt-image-2.6-01` — via
`POST /v1/images/generations` (OpenAI Images compatible; the OpenAI SDK works
with `base_url="https://api-finder.com/v1"`).

## بالعربية

أمثلة جاهزة للنسخ لتوليد فيديوهات بالذكاء الاصطناعي (Seedance 2.0/2.5) عبر API موقع
[api-finder.com](https://api-finder.com):

- الدفع بالثانية — بدون اشتراك شهري وبدون حد أدنى، والمهام الفاشلة تُسترد تلقائياً
- الدفع عبر Stripe أو USDT، والتسجيل مجاني — أنشئ مفتاح API من لوحة التحكم وجرّب أحد الأمثلة بالأعلى
- ثلاث خطوات فقط: أرسل المهمة `POST /v1/videos`، تابع الحالة `GET /v1/videos/{id}`، ثم حمّل الفيديو `GET /v1/videos/{id}/content`
- الدعم على تيليجرام: [@APIFinder_Support](https://t.me/APIFinder_Support)

## Notes

- Keep your API key in an environment variable (`API_FINDER_KEY`), never in code.
- This is a community examples repo for API-Finder users; the service itself
  lives at [api-finder.com](https://api-finder.com).
