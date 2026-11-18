#!/usr/bin/env bash
# API-Finder / Seedance video generation — curl example
# 1) Register free at https://api-finder.com and create an API key
# 2) export API_FINDER_KEY=sk-...
# 3) bash curl.sh
set -euo pipefail

BASE="https://api-finder.com"
MODEL="${MODEL:-seedance-2.5-flash-YH}"   # cheapest Seedance 2.5 line; see README for all IDs
PROMPT="${1:-Dubai skyline at dusk, cinematic drone shot over Sheikh Zayed Road}"

echo "Submitting job (model: $MODEL)..."
RESP=$(curl -s -X POST "$BASE/v1/videos" \
  -H "Authorization: Bearer $API_FINDER_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"$MODEL\", \"prompt\": \"$PROMPT\"}")
echo "$RESP"

ID=$(echo "$RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('id') or d.get('task_id') or '')")
if [ -z "$ID" ]; then echo "No job id in response — check the response above."; exit 1; fi
echo "Job id: $ID"

echo "Polling status..."
for i in $(seq 1 60); do
  STATUS_RESP=$(curl -s "$BASE/v1/videos/$ID" -H "Authorization: Bearer $API_FINDER_KEY")
  STATUS=$(echo "$STATUS_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status',''))" 2>/dev/null || echo "")
  echo "  [$i] status: $STATUS"
  case "$STATUS" in
    succeeded|completed|success|done) break ;;
    failed|error|cancelled|canceled) echo "$STATUS_RESP"; exit 1 ;;
  esac
  sleep 5
done

echo "Downloading video to output.mp4..."
curl -s -L "$BASE/v1/videos/$ID/content" -H "Authorization: Bearer $API_FINDER_KEY" -o output.mp4
echo "Done: output.mp4"
