# Framer scripts (no keys in here)
Keys are read from env only: FRAMER_API_KEY_ISSUE11landing (ISSUE11), FRAMER_API_KEY_GLAMMI (Glammi).
Setup: npm i --ignore-scripts framer-api@5.1.0 (scanned version).
- i11-fields.mjs: list ISSUE11 collections; `add` adds the FAQ Schema field to Blog Posts if missing.
- i11-add-post.mjs <html> <slug> <date> <imageUrl|""> "<alt>": adds/updates an ISSUE11 Blog Posts item, ALWAYS as a draft.
- glammi-list.mjs: lists Glammi blog items (LIVE/DRAFT, cover), pages, unpublished page changes. Read only.
- glammi-add-post.mjs <html> <slug> <date>: adds a Glammi article as a draft; refuses live items.
- glammi-publish-one.mjs <slug>: sets ONE item live and deploys; aborts on unpublished page changes or a missing cover.
- i11-publish-one.mjs <slug>: sets ONE ISSUE11 item live and deploys; aborts if issue11.app still shows NexApp template content, on unpublished page changes, or if the cover is missing.
