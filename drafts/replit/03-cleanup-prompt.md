# Replit prompt 03: clean-up (change 1 of 4, Oct 21, 2026)
Made by 🩶 Manager from drafts/dev/replit-build-audit-2026-10-21.md. Megan OK'd the plan + removing the extra onboarding end screen (Oct 21: "ok sounds good").
How to use: paste the block below into Replit Agent in the "ISSUE11 mobile app". Afterwards the Manager re-reads the code to verify (acceptance criteria at the bottom).

```
Clean-up only. Don't change the design, colors, copy or any other screen.

1. Delete these screens and every link, button, route or import that points to them:
   app/session.tsx (session detail page: tapping a session must keep opening Now Playing directly),
   app/eyes-closed.tsx, app/how-do-you-feel.tsx, app/listen.tsx and the hidden (tabs)/listen tab,
   app/ritual.tsx, app/progress.tsx, app/streak.tsx (and its feature flag).
2. Onboarding: remove ONLY the extra screen at the very end ("Your first Issue starts here" with START AGAIN). After the last onboarding screen, go straight to the app as it does for a returning user. Don't change any other onboarding screen, its order or its words.
3. Remove anything that only those deleted screens used (unused components, strings, sample data), but nothing else.
4. Run the typecheck and the tests and fix anything this clean-up broke.
5. Tell me: which files you deleted, which files you edited, and whether typecheck + tests pass.

Don't publish or deploy anything.
```

## Acceptance criteria (Manager verifies by reading the code)
1. None of the 7 screen files exist; no remaining imports/links/routes to them (search: session, eyes-closed, how-do-you-feel, listen, ritual, progress, streak).
2. Tapping a session in Explore still opens Now Playing; the 5 tabs are unchanged.
3. Onboarding = the locked 38 screens + 37b, with no extra end screen; nothing else in onboarding changed.
4. Typecheck and tests pass (per Replit's report, then spot-check the files).
Limits: max 2 attempts (CLAUDE.md "How OPS runs a task" for app work: /pipeline limits, 3 build↔QA rounds).
