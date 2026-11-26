#!/bin/bash
# Orbit pins for QUEUE.md briefs (4h Pinterest run, Nov 26). Orbit style approved by Megan ("This is excellent!").
# Text locked, 2 swings per loop, outline of hidden letters, no hook box (Megan rejected it). Big type = the brief's keyword.
cd "$(dirname "$0")/../.."
M=/tmp/claude-0/-home-user/6b57fdf0-2086-518b-b6d3-8931c0653270/scratchpad/spatial; I=../../issue11-gift/rebrand-kit/img
while IFS='|' read -r id photo ita big cap; do
  [ -z "$id" ] && continue; [ -f orbit/briefs/$id.mp4 ] && { echo "have $id"; continue; }
  OUTLINE=1 TEXT_SWING=0 CYCLES=2 timeout 500 python3 spatial_orbit.py $I/$photo.jpg $M/depth.onnx $M/modnet.onnx orbit/briefs/$id.mp4 "$big" "$ita" "$cap" "starting now" </dev/null >/dev/null 2>/dev/null && echo "ok $id" || echo "FAIL $id"
done <<'LIST'
Q01|n17|2027|vision board ideas|the vision board issue
Q06|e24|real|vision board examples|the vision board issue
Q11|e26|how to|stop overthinking|the overthinking issue
LIST
