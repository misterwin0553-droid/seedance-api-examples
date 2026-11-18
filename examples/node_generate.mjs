#!/usr/bin/env node
// API-Finder / Seedance video generation — Node.js 18+ example (built-in fetch).
// 1) Register free at https://api-finder.com and create an API key
// 2) export API_FINDER_KEY=sk-...
// 3) node node_generate.mjs "Dubai skyline at dusk, cinematic drone shot"
import { writeFile } from "node:fs/promises";

const BASE = "https://api-finder.com";
const KEY = process.env.API_FINDER_KEY;
const MODEL = process.env.MODEL || "seedance-2.5-flash-YH"; // cheapest 2.5 line
const PROMPT = process.argv[2] || "Dubai skyline at dusk, cinematic drone shot";

const headers = { Authorization: `Bearer ${KEY}`, "Content-Type": "application/json" };

const job = await (
  await fetch(`${BASE}/v1/videos`, {
    method: "POST",
    headers,
    body: JSON.stringify({ model: MODEL, prompt: PROMPT, seconds: 5, resolution: "720p", ratio: "16:9" }),
  })
).json();
const id = job.id || job.task_id;
console.log("Job submitted:", id);

while (true) {
  const info = await (await fetch(`${BASE}/v1/videos/${id}`, { headers })).json();
  console.log("status:", info.status);
  if (["succeeded", "completed", "success", "done"].includes(info.status)) break;
  if (["failed", "error", "cancelled", "canceled"].includes(info.status)) {
    throw new Error(`Job failed: ${JSON.stringify(info)}`);
  }
  await new Promise((r) => setTimeout(r, 5000));
}

const res = await fetch(`${BASE}/v1/videos/${id}/content`, { headers });
await writeFile("output.mp4", Buffer.from(await res.arrayBuffer()));
console.log("Saved output.mp4");
