#!/bin/bash
# 10 orbit pins (Megan Nov 23: "let's add some orbit pins! 10 of them"). Terms from real Pinterest search data
# (drafts/pinterest/*keywords*.json). Text locked (TEXT_SWING=0), 2 swings per 6s loop.
cd "$(dirname "$0")/.."
M=/tmp/claude-0/-home-user/6b57fdf0-2086-518b-b6d3-8931c0653270/scratchpad/spatial; I=../../issue11-gift/rebrand-kit/img
while IFS='|' read -r id photo ita big cap; do
  [ -z "$id" ] && continue
  TEXT_SWING=0 CYCLES=2 timeout 400 python3 spatial_orbit.py $I/$photo.jpg $M/depth.onnx $M/modnet.onnx orbit/$id.mp4 "$big" "$ita" "$cap" "starting now" >/dev/null 2>orbit/$id.err && echo "ok $id" || echo "FAIL $id"
done <<'LIST'
OR01|n14|winter|arc|the winter arc issue
OR02|e37|glow|up|the glow up issue
OR03|e19|money|affirmations|the money issue
OR04|e25|law of|assumption|the law of assumption issue
OR05|e36|word of the|year|the word of the year issue
OR06|e34|2027|vision board|the 2027 vision board issue
OR07|n16|that|girl|the that girl issue
OR08|e33|self|love|the self love issue
OR09|e27|journaling|prompts|the journaling issue
OR10|e29|manifestation|journal|the manifestation issue
LIST
