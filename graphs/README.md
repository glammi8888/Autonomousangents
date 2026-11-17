# 🗺 Knowledge maps (graphify), one per area
Megan, Nov 17: "please have every agent use it" + "just break it off in pieces that will make everything work".
These are maps of what our files say and how they connect. Read your area's map before searching the repo; it's faster and shows links that plain search misses.

| Piece | Who uses it | What's in it |
|---|---|---|
| `team/` | every agent, OPS, the pipeline | CLAUDE.md, our agents, /pipeline, `.pipeline/` (lessons, spec, checklists), installed skills log |
| `product/` | design, the Editor, pipeline planner, Brand | product architecture, onboarding V3, positioning, ICP, brand guide, magazine style, landing copy |
| `marketing/` | Growth, Pinterest, social, ads, Brand + Social Room | marketing plans, UTM map, content formats, Pinterest strategy and queue, ads plans, panel research |
| `app/` | pipeline builder, QA, reviewer | the ISSUE11 app code (`issue11/`) and Framer tools (`tools/`) |

Not mapped on purpose: images (too costly to read one by one), vendored skills, and pin HTML files.

## How to use it (no install needed)
1. Open `graphs/<piece>/GRAPH_REPORT.md`. It lists the key ideas ("god nodes"), the clusters and surprising links, each with its source file.
2. Then open the source files it points to. The map shows where to look; it doesn't replace the file. Always quote the real file.
3. If `graphify` is installed (0.9.111, the scanned version only): `graphify query "<question>" --graph graphs/<piece>/graph.json` (run `export GRAPHIFY_BACKEND=none GRAPHIFY_NO_CTA=1` first).

## Keeping it fresh (every chat, every agent: Megan, Nov 17: "keep doing /graphify in all chats please" + "and for all agents")
```
export GRAPHIFY_BACKEND=none GRAPHIFY_NO_CTA=1
PY=$(head -1 $(which graphify) | tr -d '#!')   # graphify's python
$PY tools/graphs/graphs.py status            # what changed since each map was built
$PY tools/graphs/graphs.py build app         # code changes: free, no AI
$PY tools/graphs/graphs.py todo product      # changed docs: prints the brief for ONE extraction helper
$PY tools/graphs/graphs.py build product     # after the helper wrote its chunk
```
Pieces and their file globs: `graphs/pieces.json`. Raw extractions: `graphs/<piece>/chunks/` (newest chunk wins per file: chunk names must start with YYYYMMDD-HHMMSS, the `todo` command prints one). Add a new area by adding globs there.

### Old note
A map is a snapshot. If you changed a mapped file in a big way, say so in your report; OPS rebuilds the piece (the app piece is free; doc pieces use 1–2 helper runs). Never set a Gemini/Google key, and never run `graphify install` or hook commands (see `.claude/skills/graphify/SKILL.md` → ISSUE11 overrides).
