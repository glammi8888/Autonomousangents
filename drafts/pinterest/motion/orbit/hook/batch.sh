#!/bin/bash
# Approved orbit pins + polarizing pattern-interrupt hooks (Megan Nov 24: "more polarizing and more pattern interrupt" -> "ok this is much better").
cd "$(dirname "$0")/../.."
M=/tmp/claude-0/-home-user/6b57fdf0-2086-518b-b6d3-8931c0653270/scratchpad/spatial; I=../../issue11-gift/rebrand-kit/img
while IFS='|' read -r id photo ita big cap hook; do
  [ -z "$id" ] && continue; [ -f orbit/hook/$id.mp4 ] && { echo "have $id"; continue; }
  HOOK="$hook" OUTLINE=1 TEXT_SWING=0 CYCLES=2 timeout 500 python3 spatial_orbit.py $I/$photo.jpg $M/depth.onnx $M/modnet.onnx orbit/hook/$id.mp4 "$big" "$ita" "$cap" "" </dev/null >/dev/null 2>/dev/null && echo "ok $id" || echo "FAIL $id"
done <<'LIST'
OR02|e37|your|glow up|the glow up issue|skincare isn't a glow up. it's a hobby. here's the real one
OR04|e25|law of|assumption|the law of assumption issue|if you're not a little delusional, the law of assumption won't work
OR05|e35|my|word of the year|the word of the year issue|resolutions are for people who quit in february. pick one word instead
OR07|n16|be|that girl|the that girl issue|that girl is a myth. this 30-day plan isn't
OR08|e33|the|self love|the self love issue|your affirmations are lies. say these instead
OR09|e27|journaling|prompts|the journaling issue|journaling is making your overthinking worse. do this instead
LIST
