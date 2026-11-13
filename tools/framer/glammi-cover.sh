#!/usr/bin/env bash
# Glammi blog cover (Megan, Nov 13: chrome visuals + "they both work" for H and G).
# usage: tools/framer/glammi-cover.sh <source-image> <out.jpg> [H|G] [crop-y]
#   H (default) = white script "glammi" logo + "DISCOVERABILITY × DESIRABILITY" (bold grotesk)
#   G           = logo only (use when the top of the image is too busy for two lines)
#   crop-y      = top offset of the 3:2 crop on the source (default: centered)
# Output: 1600x1067 JPG. LOOK at it before using it.
set -euo pipefail
src="$1"; out="$2"; mode="${3:-H}"; y="${4:-}"
root="$(cd "$(dirname "$0")/../.." && pwd)"
logo="$root/drafts/glammi-blog/images/glammi-logo-script-white.png"
font="$(fc-match -f '%{file}' 'Inter Display:black')"   # stand-in for Akzidenz-Grotesk Bold (brief font, paid)
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
w=$(identify -format '%w' "$src[0]"); h=$(identify -format '%h' "$src[0]")
ch=$(( w * 2 / 3 )); cw=$w
if [ "$ch" -gt "$h" ]; then ch=$h; cw=$(( h * 3 / 2 )); fi
if [ -z "$y" ]; then y=$(( (h - ch) / 2 )); fi
x=$(( (w - cw) / 2 ))
convert "$src[0]" -crop "${cw}x${ch}+${x}+${y}" +repage -resize 1600x1067! "$tmp/base.jpg"
convert "$logo" -resize 260x "$tmp/l.png"
convert "$tmp/l.png" \( +clone -background black -shadow 60x6+0+2 \) +swap -background none -layers merge +repage "$tmp/ls.png"
if [ "$mode" = "G" ]; then
  convert "$tmp/base.jpg" \( -size 1600x360 gradient:'rgba(0,0,0,0.55)'-'rgba(0,0,0,0)' \) -gravity north -composite \
    "$tmp/ls.png" -gravity northwest -geometry +50+36 -composite -quality 90 "$out"
else
  convert "$tmp/base.jpg" \( -size 1600x380 gradient:'rgba(0,0,0,0.55)'-'rgba(0,0,0,0)' \) -gravity north -composite \
    "$tmp/ls.png" -gravity northwest -geometry +50+36 -composite \
    -font "$font" -pointsize 64 -kerning -3 -interline-spacing -16 -fill white -gravity northwest \
    -annotate +56+160 $'DISCOVERABILITY\n× DESIRABILITY' -quality 90 "$out"
fi
echo "cover: $out ($mode)"
