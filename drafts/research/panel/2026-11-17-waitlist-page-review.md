# issue11.app as a pre-launch waitlist page: review (Nov 17, 2026)

Asked by: OPS for Megan ("oh let's do waitlist-page"). Review only: nothing on the live site was changed. Megan has since OKed applying fixes; OPS applies them from the exact before → after table in section 3.
Skills: graphify (product + marketing maps), waitlist-page (P0/P1 gates), cro, marketing-psychology (ethical only), synthetic-crowd (panel).
Already live and NOT re-suggested: everything in `2026-11-16-homepage-fixes/CHANGES.md` (trust line, 7-day trial line, cancel line, phone mockup in hero, stacked 3 steps, founder quote size, softened "actually works" lines).
Kept on purpose: guest-list framing ("Invite-only", "Consider yourself shortlisted", "Approved guests lock in their founding rate"). Per Megan's Nov 16 decision, nothing below advertises guaranteed entry.

> AI personas are not customers. The panel numbers are a screening signal on 12 synthetic people, not a forecast. Read the A vs B differences only.

## Screenshots (all in `2026-11-17-waitlist-page-review/`)
- Phone 390x844: `live-390-fold.png`, `live-390-full.png`
- Small phone 375x667: `live-375x667-fold.png` (the button is below the fold)
- Desktop 1440x900: `live-1440-fold.png`, `live-1440-full.png`
- Thank-you page: `live-390-thank-you.png`, `live-1440-thank-you.png`. I opened https://issue11.app/thank-you directly (status 200), so **no form was submitted**.
- Raw page capture: `live.json` · panel files: `crowd/`

## 1. Findings by area

| Area | Verdict | What I saw |
|---|---|---|
| Hero clarity | Good | The headline lands (yesterday's panel and today's both quote it back). The product mockup sits in the first phone screen. |
| **Primary CTA** | **Weak (biggest issue)** | The hero submit button is white with black text and the same size and shape as the white email field. On a loud gradient, it reads as a second input. Only the header button is black. Today's panel raised "which box do I tap" without being asked: 21 keyword hits on the current version. |
| CTA wording | Inconsistent | Phone header "Get early access" · hero "Request access" · desktop header "Request access" · closing section "Get your invite…" + "Request access". There are three different verbs for the same action. |
| Offer and incentive | True, but buried | The founding rate ($39.99 first year, then $69.99/yr), the Dec 11 beta and invite-only are all real and present. They sit in 6 lines of small grey text under the button, mixed with the trial, streak, cancel and iPhone facts. "Joining the waitlist is free" appears only in the FAQ. Several personas thought tapping the button meant giving a card or paying. |
| Form friction | Good | One field (email, `type=email`, `required`) and honeypot fields for spam. No name field, so emails open with "Hi,". That's fine. |
| Trust and proof | Honest | No fake reviews, counts or countdowns. The FAQ "No app can promise results" stays the strongest trust line. Proof stays limited to mockups until real Issues exist. |
| Urgency | True | It's a real date (Dec 11) and a real first-year rate. There's no countdown and no "spots left", and there is no 1,000 cap (Megan, Nov 7), so none is suggested. |
| Mobile | Mostly good | No horizontal scroll at 390 (scrollWidth 390). At **375x667 (iPhone SE/8/mini size)** the form ends at 704px, so the "Request access" button is below the first screen. That fails the waitlist-page P0 gate ("email input + button fully visible at 375×667"). |
| **Thank-you state** | **Dead end** | "ISSUE11 / FIRST EDITION · Consider yourself shortlisted. · Your request is in. The first Issue is invite-only, and invitations go out in waves. We're saving you a spot. Future you is already in print. · Back to home". The guest-list tone is right. But it never says how she'll hear back (email) or that the email may land in spam (it did in our Nov 8 Resend test). It has no share step, and its only action is "Back to home". |
| Referral/share loop | Missing | There's nothing after signup. A ranked "move up the list" referral would be dishonest here (everyone gets in, and there's no position to show), so only a plain share is suggested. |

## 2. Top 5 fixes, ranked by expected signup impact

1. **Make the hero button look like a button (and say what it does).** Every visitor sees it, and the panel confused it with the field. Effort **S**.
2. **Give the thank-you page a next step: how she'll hear back, a spam-folder note and one "Share ISSUE11" button.** It's the peak-end moment, and right now it's a dead end. Effort **S** for the copy; **M** if the share button is a small code component.
3. **Lead the small print with what she gets: "Free to join, no card needed" + the founding rate, then the facts.** It answers "will I be charged?" next to the button. Effort **S**.
4. **Fit the button on a 375x667 phone screen.** It fails the P0 gate on smaller iPhones. Effort **S**.
5. **Use one CTA label everywhere ("Request my invite").** Three verbs for one action add doubt. Effort **S**.

## 3. Exact before → after (for OPS to apply; all copy is built from words already on the site)

| # | Section · element · breakpoint | Before | After |
|---|---|---|---|
| 1a | Hero · form "Early access form" · submit button (layer "Get early access" → "Submit") · Desktop, Tablet, Phone | Fill white; label "Request access" in black | Fill = the same black token as the header "Get early access" button; label colour = the header button's white label token; label **"Request my invite"**; add the same ↓ arrow icon the header button uses (optional) |
| 1b | Same button · hover state | (whatever is there now) | Slightly lighter black or 0.9 opacity, so it visibly reacts (waitlist-page P1) |
| 2a | /thank-you · body paragraph · all breakpoints | "Your request is in. The first Issue is invite-only, and invitations go out in waves. We're saving you a spot. Future you is already in print." | "Your request is in. The first Issue is invite-only, and invitations go out in waves before the Dec 11 beta. Your invitation will come by email, so keep an eye on your inbox (and your spam folder, just in case). Future you is already in print." |
| 2b | /thank-you · NEW block under the paragraph, above "Back to home" · all breakpoints | (none) | Thin divider · small uppercase label **"KNOW SOMEONE WITH A BOARD FULL OF PLANS?"** · line **"Send her ISSUE11. She can request her own invite."** · solid black button **"Share ISSUE11"**. The button opens the phone's share sheet (`navigator.share({title:'ISSUE11', url:'https://issue11.app'})`); where that isn't available it copies `https://issue11.app` and the label changes to "Link copied". No tracking, no reward, no position number. |
| 2c | /thank-you · "Back to home" | Only action, text link | Keep as is (now secondary, under the share button) |
| 3 | Hero · trust text under the button (2 text layers; 2nd is node SQh312SI4) · all breakpoints | L1: "Private beta opens Dec 11, with invites for the waitlist. Founding members pay $39.99 for the first year (then $69.99/yr). Invite-only." L2: "The yearly plan includes a 7-day free trial. Skip any week, no streaks. Cancel anytime in your iPhone settings. iPhone only." | L1 (dark text colour, body size and weight 500, not the grey small style): **"Free to join, no card needed. Founding rate: $39.99 for your first year (then $69.99/yr). Private beta opens Dec 11."** L2 (keep current small grey style): **"Invite-only. 7-day free trial on the yearly plan. Skip any week, no streaks. Cancel anytime in your iPhone settings. iPhone only."** |
| 4 | Hero · Phone breakpoint only | At 375x667 the form spans 599–704px (button below the fold) | Make the hero shorter by ~70px: top padding 48 → 24px, and the H1 phone font size about 12% smaller. **Acceptance:** Playwright at 375x667 shows the form bottom at ≤ 655px; recheck that the 390x844 fold still shows the mockup uncropped and nothing overlaps. Don't cut the kicker or headline words. |
| 5 | Header button (Phone + Tablet "Get early access", Desktop "Request access") · closing section button "Request access" · /thank-you header button | Mixed labels | All **"Request my invite"**. Keep the closing line "Get your invite before the Dec 11 beta and lock in $39.99 for your first year." as is. |

Copy checks: "you" voice, plain "ISSUE11", no promised results, no productivity or chatbot framing, no "becoming her", no new claims. "Free to join" and "no card needed" are true: the FAQ says "Joining the waitlist is free" and the form collects only an email. The trial and cancel facts are unchanged. The fix 2a wording is slightly reworded from the tested version: "We'll email you, so check your inbox" became "Your invitation will come by email…". The new wording stays true even if no instant confirmation email goes out (see Needs Megan).

Ethics (marketing-psychology): the changes use clarity (Hick's law, one obvious action), regret-aversion facts that are true (free, no card, cancel line) and a peak-end thank-you. There's no fake scarcity, no countdown, no invented proof and no referral leaderboard.

## 4. Panel results (synthetic-crowd, haiku, the same 12 personas as Nov 16, seed 11, `crowd/personas.json`)

The panel covers 6 manifestation stages × 3 budgets × 4 life moments × 4 arrival paths, all millennial US women (`crowd/dims.json`, from design/ICP.md + LEXICON). 72 isolated calls, 0 failed, about $0.08 API-equivalent.
Hero question: "Do you type your email and tap the button? join now / maybe later / no, why, and what happens after you tap?" Thank-you question: "What do you do next? Would you send ISSUE11 to a friend right now?"

| Fix | A (current) consider / ignore | B (fix) consider / ignore | Who moved (same personas) | Main objection left in B |
|---|---|---|---|---|
| 1 Button | 8 / 4 | **9 / 3** | +2 (rebrand #1, disappointed #6), −1 (journaler #8) | "What happens after I tap?" rose (16 → 23 keyword hits), along with $69.99 renewal for an app she can't see yet. "Which box?" fell from 21 hits to 0. |
| 2 Thank-you next step + share | 3 / 9 | **7 / 5** | +4 (journalers #0 #8, disappointed #6, newcomer #10), 0 moved down | Share intent stayed near zero in both: "I'm not sending this to a friend until someone tells me what it actually does." The gain came from knowing what happens next, not from sharing. |
| 3 Offer line (two versions) | 8 / 4 | 8 / 4 (founding-rate line) · 8 / 4 ("Free to join, no card needed" line) | 2 up and 2 down in each version, so no net change | The button confusion still dominated ("I'm not typing my email into two identical white boxes"), and many still read it as a yearly charge. |

How to read this:
- **Fix 1 helps a little and removes the confusion.** One caveat: the "current" description had to state my Visual QA finding (the two white boxes look alike), so part of this result echoes that description. The real check is the live click rate after the change.
- **Fix 2 is the clearest panel win** (+4, no reversals). Expect it to help trust and inbox placement, not referrals. Pre-launch, people won't share what they haven't seen. Keep the share button as a cheap, honest option, not as a growth bet.
- **Fix 3 showed nothing on its own,** because the button problem was still in that variant and masked it. It's true, cheap and answers a repeated "will I be charged" worry, so apply it with fix 1. Re-run A vs (1+3) on this same panel if OPS wants a combined read.
- The same segments stayed cold as yesterday: both burned skeptics ignored every version. Price objections ($69.99 renewal, "can't see it working") persist across all versions. Copy won't fix them before the product exists; real screens and real Issues will.

## 5. Needs Megan (only she can answer)
1. **Does an automatic "request received" email go out the moment someone signs up?** *Recommended:* if yes, change 2a to "Check your inbox for a note from us." Seeing the email arrive confirms the signup worked. If no (CSV waves), keep the wording in 2a, which is true either way.
2. **Share button on /thank-you: native share sheet with no tracking.** *Recommended:* yes. It costs nothing, and it's honest because it carries no reward and no fake "spots" number. Skip it if she'd rather keep the page minimal; fix 2a alone carries the panel gain.

## 6. Limits
- These are AI personas reading text descriptions of the page, so visual fixes (button colour, fold position) are only roughly testable this way. Fix 4 was not panel-tested (it's a layout check with a pass/fail number).
- The form was never submitted. The thank-you page was viewed by direct URL, so the real redirect after submit was not observed.
- Nothing was changed on the live site.
