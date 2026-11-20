# ISSUE11 app: what's left before the ONE Replit update

## ⚠️ RE-PLAN Nov 20: Dec 11 = PUBLIC App Store launch (not a beta)
Megan, word for word: "No I want it to be on App Store on dec 11". Goal now = **Apple-approvable v1, not complete.** Back-plan (OPS): Paid Apps Agreement ~Nov 27 · finished build Dec 3 · submit Fri Dec 4 · release Dec 11. Sections 1–4 below are the Nov 19 checklist; where they differ, this block wins.

### What ships Dec 11 (v1) vs v1.1
| Area | v1 (Dec 11) | Moves to v1.1 |
|---|---|---|
| Onboarding | As built (locked), screen 34 renamed if Megan says yes | — |
| Paywall + sign-in | Sign in with Apple + email code, Monthly $9.99 · Yearly $69.99 (7-day trial) · 37b founding $39.99 first year, Restore, Terms + Privacy links | Duo/Family, weekly/intro tests |
| Home | Issue on top · Monday "Pick this week's move" (3 suggestions + write my own) · "I did it" → page lands · "Not yet" → smaller step · "Week N · showing up" · Skip this week | 11:11 surprise, monthly recap |
| Explore | Images · Sessions · Saved (boards) · tap session = plays · Search · "What visuals are we missing?" card | — |
| Issue | Reader · "+ New page" (words optional + photos) · "Let the Editor decide" + 4 layouts from **6 real templates** · Edit (layout / swap photo / my words) · progress "15 of 40" | "More layouts" library, layout unlocks, stickers, in-app print checkout (see Print) |
| Print | At 40 pages: "Order my print" opens the print order page on issue11.app; Megan prints by hand (approved Nov 5). Physical goods may be paid outside in-app purchase (guideline 3.1.5(a), verify at build) | In-app Apple Pay checkout, order tracking |
| Journal | Your wall (today's prompt + her lines) · Write · Add to my issue / Keep in Journal | — |
| You | Name + pages · one list · Restore purchases · Delete account (real) · Help & support · "Help us improve" = opens an email to support@issue11.app (no new data stored) | My Issues shelf (nobody has a printed Issue yet), app icon picker if not built, widgets |
| The Editor (11) | Floating, draggable · one card per screen with **written suggestions only (no live AI)** · "AI off" wording not needed | Live AI (needs LUCKY-STAR-ARCHITECTURE approval + privacy review) |
| Brand | Inter Tight everywhere, white everyday screens, Electric Soft only on welcome / paywall | — |

### Progress (Nov 20)
- ✅ Decision 1 DONE: Megan approved boards 26–28 ("i approve them just add them"), floating 11 only.
- ✅ Step 2 drafted: logic map v8 (board 26): v1 vs v1.1 tags, Editor row (one card per tab, written suggestions only, steps KNOWN → RETRIEVE → ASK → GENERATE → KEEP for v1.1), first-day state without a page lock, Electric Soft only on first open + paywall, final prices, print = order page on issue11.app, feedback = email. **Waiting for Megan's OK.**
- ✅ Step 3 done: boards 27–28 v2: header 11 removed everywhere (10 screens), floating 11 on every screen and never over a button or sheet, v1/v1.1 captions (print, My Issues, More layouts, unlock line, Help us improve).
- ⏳ Decisions 2 (sign-in + payments spec, Editor spec) and 3 (screen 34 rename) still open.
- Next: step 5, the ONE Replit prompt + screens + zip, by Tue Nov 24 (starts right after the v8 OK).

### Dates (each step must finish by)
| By | Step | Owner |
|---|---|---|
| **Sat Nov 21** | Megan's 3 decisions (section 3) | Megan |
| **Mon Nov 23** | Logic map v8 with the v1 cuts + board fixes (one floating 11, first-day state, gradient screens) → Megan's OK | Design Room → Megan |
| **Tue Nov 24** | ONE Replit prompt + screens + zip (includes the cleanup list #1–#11) | Design Room |
| **Thu Nov 26** | 6 real page templates (MISE-EN-PAGE) | 🖋 The Editor agent |
| **Fri Nov 27** | Paid Apps Agreement + bank + tax active; subscriptions created in App Store Connect | Megan |
| **Mon Nov 30** | **First test build to TestFlight from Replit/Expo** (catches signing, bundle id `com.issue11.app` and in-app purchase setup early) | Megan · Build Room checks read-only |
| **Tue Dec 1** | Real content in: sessions with real audio (Replit had demo audio only on Oct 21) and Explore images Megan owns; all Pinterest placeholder images gone · privacy policy + terms live on issue11.app · support page live | Megan (content) · web agents (pages) |
| **Thu Dec 3** | Build finished: sign-in, subscriptions, restore, delete account working · App Store screenshots from the real screens (2.3.14) · privacy labels + review notes + demo account drafted | Megan · ASO Scout · Design Room drafts |
| **Fri Dec 4** | Submit for App Review | Megan |
| **Thu Dec 11** | Release | Megan |

### Apple requirements still missing (as of the Oct 21 audit; Megan to confirm anything newer)
1. **Account deletion inside the app** (5.1.1(v)): placeholder only. Must delete her Issues and photos too.
2. **Restore purchases** + real in-app subscriptions (3.1): not wired. Paywall must show price, renewal period, trial terms, how to cancel, Terms (EULA) + Privacy links.
3. **Sign in with Apple** (needed if email or social login is offered): not wired.
4. **Privacy policy** (5.1): draft only (`drafts/legal/issue11-privacy-DRAFT.md`), waiting on the iPostal1 mailing address. Must be live on issue11.app and linked in the app + App Store Connect.
5. **App Privacy "nutrition labels"** in App Store Connect: not done. With no live AI in v1 they get much simpler.
6. **Demo account + review notes** (login required): not done. Needs a test account that skips the paywall or a sandbox purchase path explained in the notes.
7. **Support URL**: support@issue11.app is live, but App Store Connect needs a web page. Make issue11.app/support (FAQ + email).
8. **Bundle id** `com.issue11.app` missing from app.json (Oct 21).
9. **No demo or placeholder content** (2.1 completeness): demo audio, "preview" stubs, "not available in this preview" text and unfinished rows must all be gone or hidden.
10. **Screenshots with the real UI** (2.3.14), only after the build exists.

### Biggest risk
The path from Replit to TestFlight (Expo build + signing + in-app purchases) has never been tested. That's why the first test build is set for Nov 30: if it fails, there are still 4 days to fix it before Dec 4.

---
*(Nov 19 checklist below. Its "private beta" wording is outdated.)*
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
2. **Approve the 2 specs that touch user data: sign-in + payments (`drafts/dev/signin-payments-spec-v1.md`) and the Editor (`design/LUCKY-STAR-ARCHITECTURE.md`)?** → **Approve sign-in + payments now; for the Dec 11 launch keep the Editor on its written suggestions (no live AI) and approve its AI spec for v1.1.** Safety Rule 4 needs your OK before building. Apple won't approve a paid app without working sign-in, subscriptions and restore; live AI adds cost, privacy labels and review risk to a 10-day build.
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
