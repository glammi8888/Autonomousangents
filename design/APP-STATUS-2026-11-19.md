# ISSUE11 app: what's left before the ONE Replit update (Dec 11 private beta)
🎨🩵 Design Room · Nov 19, 2026 · checklist only (no new screens, no Replit prompt yet)
Asked by Megan via OPS (Nov 18, "Sure"). Order she set: app first → hooks + carousels → video formats.

**How to read the %:** design % = logic approved + screens drawn + screens approved (a third each). Replit = what the Oct 21 read-only audit proved (`drafts/dev/replit-build-audit-2026-10-21.md`). Nothing newer proves what's in Replit; Megan to confirm anything she built after Oct 21.

## 1. Per area (tab-bar order)

| Area | Logic approved? | Screens drawn | Screens approved? | Design % | In Replit? (Oct 21 audit) |
|---|---|---|---|---|---|
| **Onboarding** (38 screens + 37b) | ✅ Locked Oct 8 ("I'm happy") | ✅ onboarding-v3-designed | ✅ (locked) | **100%** | ✅ all 38 + 37b, locked order/copy. Sign-in, paywall, AI = honest stubs. 1 extra end screen not in V3. |
| **Paywall** (37 + 37b) | ✅ Prices Nov 7 ("Ok let's do that") | ✅ in onboarding | ✅ | **90%** (build spec not approved) | 🟡 stub: "Pricing will be shown when billing is connected" |
| **Home** | ✅ v4 Oct 23 ("Ok good options") | ✅ boards 27 + 28 | ❌ not approved (CURRENT FACTS Nov 7) | **67%** | 🟡 OLD Home (long page, flashback, saves strip, latest pages). Needs the new Home. |
| **Explore** | ✅ Oct 23 ("Saves should live in Explore…", "6. endless explore") | ✅ boards 25, 27, 28 | ❌ | **67%** | 🟡 OLD chips (For you · Sessions · My Saves), shelves. Tap session → player ✅. |
| **Issue** | ✅ v7 Oct 23 ("it'll look less cluttered that way") | ✅ boards 27 + 28 | ❌ | **60%** (final layout templates not designed) | 🟡 40-slot grid, reader, ready-to-print, order ($29.99, shipping) ✅. No "+ New page", layout picker or unlocks. |
| **Journal** | ✅ Oct 23 (Megan: "I think Journal is great so far") | ✅ board 27 | ❌ | **67%** | 🟡 OLD Journal (live pull quote, one fixed prompt). Needs the wall + Write. |
| **You** | ✅ Oct 23 (feedback row = Megan's idea) | ✅ boards 27 + 28 | ❌ | **67%** | 🟡 all rows exist, most open a placeholder. Delete account = placeholder (must be real for Apple 5.1.1(v)). |
| **The Editor (floating 11)** | 🟡 Architecture = PROPOSAL "waiting for Megan's approval" since Oct 3 (design/LUCKY-STAR-ARCHITECTURE.md). Floating + draggable ✅ (Oct 23). 3 commands removed ✅ (Nov 5, "Yes, remove"). | 🟡 old Lucky Star A–G screens only | ❌ | **40%** | 🟡 floating 11 ✅ (drags, remembers spot, no edge snap). AI = "NOT CONNECTED". Shows a chat thread (rule = one card). |

**Overall design ≈ 70%. Replit has the old version of every tab after onboarding.**

## 2. Outdated by later decisions (fix in the one update)
1. **"Lucky Star" → "The Editor"** (Oct 21): still in Replit (A–G, "Lucky Star & AI" row), in the handoff folder `06-lucky-star/`, and on onboarding screen 34 "Meet Lucky Star" (locked: needs Megan's OK, decision 3).
2. **"My saves" (Oct 16) → Explore "Saved" tab** (Oct 23, boards in Explore). CLAUDE.md, PRODUCT-ARCHITECTURE and Replit still say "My saves". Keep one name: **"Saved"** in the app (default, low risk), function name stays Your World internally.
3. **Removed Editor commands** (Nov 5): `design/lucky-star-spec.md` still lists "Rewrite this", "Create a ritual / to-do", "Turn this into actions". Remove there and in any prompt.
4. **Pages unlock anytime** (Nov 7, "2. Ok"): the first-day state "Fill page 9 · your first move" and "page 9 glowing" (V1-SIMPLIFIED) tie a page to the move. Reword to "Make your next page" (no lock). Layout/sticker unlocks every 5 pages (Oct 23) are fine: those are extras, not pages.
5. **Prices** (Nov 7): Monthly $9.99 (no trial) · Yearly **$69.99** (7-day trial) · founding **$39.99 first year** for approved guests. Outdated: $59.99 in `drafts/dev/signin-payments-spec-v1.md` body, "yearly TBD" in `drafts/replit/handoff/00-READ-ME-FIRST.md` + `04-print-purchase.md`.
6. **No "becoming her"** (Oct 7, re-logged Nov 18): reference image `drafts/replit/handoff/06-lucky-star/04-listen-session.png` shows a session called "BECOME HER". Rename the sample session; sweep the app copy file (03-app-copy.md) before sending.
7. **Fonts** (Nov 7: Archivo Black discarded, Inter Tight): Replit still loads Archivo Black, Archivo Narrow, IBM Plex Mono. Boards 21d–28 are all Inter Tight ✅. Onboarding's look will change font with it (copy/order untouched).
8. **Electric Soft gradient** (Nov 7): allowed only on a few special screens (proposed: welcome/first open, "Your Issue is ready", paywall). Not on boards yet; everyday screens stay white ✅.
9. **Two 11s on the boards**: boards 26–28 show the 11 in the header AND floating. Megan (Oct 23): "Yes I want to keep the floating 11 draggable" → header 11 goes, floating stays.
10. **Old screens still in Replit code**: session detail page (cut Oct 20), eyes-closed, how-do-you-feel, listen tab, ritual, progress, streak page. Delete in the cleanup.
11. **Replit handoff prompt** `drafts/replit/handoff/01-app-flow-prompt.md` is half old (Journal "studio open · Day 33", "↻ Another look", old Explore chips, Lucky Star look). It gets rewritten from boards 26–28, not patched.

## 3. Megan's decisions (max 3, recommended answer first)
1. **Approve boards 26 (logic) + 27 + 28 (screens) as the beta design?** → **Yes, with fix #9 (floating 11 only).** Replit can't start until screens are approved (Nov 7 rule: unapproved screens never ship), and every tab after onboarding is waiting on this one OK.
2. **Approve the 2 specs that touch user data: sign-in + payments (`drafts/dev/signin-payments-spec-v1.md`) and the Editor (`design/LUCKY-STAR-ARCHITECTURE.md`)?** → **Approve sign-in + payments now; for the Dec 11 beta keep the Editor on its written suggestions (no live AI) and approve its AI spec after the beta.** Safety Rule 4 needs your OK before building. Beta testers need to sign in and keep their Issue; live AI adds cost, privacy review and risk for 3 weeks of build.
3. **Rename onboarding screen 34 "Meet Lucky Star" → "Meet the Editor"?** (onboarding is locked, so only you can) → **Yes, name only, nothing else on the screen changes.** Every other screen says "the Editor"; a different name on the consent screen would confuse testers right where we explain AI.

Parked by default (no answer needed now): the 11:11 daily surprise from the Editor → after the beta. "Finish my Issue digitally" at 40 pages → after the beta.

## 4. Order (so nothing gets redone)
1. **Megan:** decisions 1–3 above. *(Blocks everything below.)*
2. **Design Room:** logic map v8 (Editor row: GUIDE/ASSIST per tab with the KNOWN → RETRIEVE → ASK → GENERATE → KEEP steps; first-day state per #4; gradient screens per #8) → Megan's OK.
3. **Design Room:** fix boards 27–28 (one floating 11, first-day state, gradient screens, Editor sheet in the new look) → Megan's OK. Run design/VISUAL-QA.md.
4. **🖋 The Editor agent:** ~12 open page layouts + the unlockables as templates (design/magazine/MISE-EN-PAGE.md). Replit can start with 6 placeholder JSON templates, so this can run in parallel with step 5.
5. **Design Room:** ONE Replit prompt + screens + zip rebuilt from boards 26–28, including the cleanup list (#1, #2, #3, #5, #6, #7, #10). Snapshot Replit's files first so the result can be diffed (lesson Oct 21).
6. **Megan:** sends it to Replit (she builds). **🩵 Build Room:** read-only check of the result, like Oct 21.
7. After the build: real delete account, bundle id `com.issue11.app`, sign-in + payments per the approved spec, then App Store screenshots with the real screens (Megan, Oct 15). Megan alone does TestFlight / App Store.

Not done in this checklist: no screens drawn, no Replit prompt written, nothing in Replit touched. The `onboarding` and `paywalls` skills were not loaded; onboarding and the paywall were checked by hand against ONBOARDING-V3 (locked) and the Nov 7 prices. No skill covers Replit.
