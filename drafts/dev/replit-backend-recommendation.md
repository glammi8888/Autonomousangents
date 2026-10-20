# Replit build: old pipeline spec + backend choice
Planner (consult only) · 2026-10-20 · Nothing built, nothing installed, spec.md/request.md untouched.

## 1. Old pipeline spec: keep it as a reference checklist (don't retire it)
**Recommendation:** `.pipeline/spec.md` stops being a build plan and becomes the trust/QA checklist for Replit. Its file paths, folder layout and Expo-router details no longer apply (Replit decides those). Where it conflicts with drafts/replit/ (tabs, names like "My saves", screens), the Replit prompts and approved screens win.
**Why keep it:** the hard parts are tool-agnostic and already thought through. Retiring it means redoing them (rule 6, reuse). What still applies:
- Acceptance criteria sections B (sign-in), C (Scribe), D (photos), E (data security) and G (process). Run them on the Replit build as the QA pass. Skip A (starter cleanup).
- Rules worth pasting into the Replit sign-in/photo prompt: each user sees only her own rows (tested with 2 accounts), private photo bucket, resize + strip location (EXIF) from photos before upload, "in my Issue" off by default, journal never sent to AI without consent, no secrets in the app code.
**Next step (Megan or Manager, 1 min):** add one line at the top of spec.md: "Reference checklist for the Replit build, not a build plan."

## 2. Database, sign-in, photos: Supabase, connected to the Replit Expo app
**Recommendation:** Supabase for all three: sign-in (Apple + email code), Postgres database, private photo storage. Replit Agent builds the app and connects it with 2 values stored in Replit Secrets (project URL + publishable key).
**Why, using rule 11 (easiest first):**
- Replit's built-in options would be easiest *if* they covered the must-haves. I couldn't confirm that they do. As of mid-2026 (my training knowledge): Replit offers a built-in Postgres database, Object Storage and "Replit Auth". Replit Auth is a web-redirect login. I could not confirm (a) native Sign in with Apple inside an Expo iPhone app or (b) fully deleting a user's sign-in account from inside your app. Both are App Store requirements (Guidelines 4.8 and 5.1.1(v)).
- Supabase has documented answers to all four must-haves: native Apple sign-in in Expo (`signInWithIdToken`), per-user row security (RLS), private storage buckets with per-user folders, and an admin call to delete a user. The account-delete function removes her rows, then her photos folder, then her login.
- One provider keeps everything in one dashboard. The old spec and drafts/dev/developer-scope-oct.md already planned it, so nothing gets redone.
- Cost: $0 to build on the free plan. Free projects pause after about a week of no use, so move to Pro (about $25/month, verify on supabase.com/pricing) before TestFlight testers.
**When to switch:** if Megan asks Replit Agent and it can show Replit docs confirming both (a) and (b) for Expo apps, Replit built-in becomes the easier path and I'd recommend it instead.

**Sources:** docs.replit.com was **blocked from this session** (proxy policy 403), so I could **not** verify current Replit features. Check these pages before deciding: docs.replit.com/replitai/integrations (Auth), docs.replit.com/cloud-services/storage-and-databases/sql-database, docs.replit.com/cloud-services/storage-and-databases/object-storage. Supabase: supabase.com/docs/guides/auth/social-login/auth-apple, /docs/guides/storage/security/access-control, /docs/reference/javascript/auth-admin-deleteuser. App Store: developer.apple.com/app-store/review/guidelines (4.8, 5.1.1(v)).

## Megan approves before any of this is built (Production Safety Rule 4)
1. The provider choice (Supabase, or Replit built-in if (a) and (b) are confirmed).
2. Sign-in methods: Apple + email code. Apple setup needs her Apple Developer account. She does it or invites a developer with the Developer role (never her password).
3. What gets stored and where (journal text, photos, profile) and the account-delete flow, including photos.
4. Who holds the Supabase admin (service-role) key. It goes only in the server function's secrets, never in the app or the Replit chat.

## Risks
- Replit Agent may paste keys into code or turn row security off "to make it work". QA must check AC section E and grep for keys.
- Delete account that leaves photos behind fails App Review and breaks trust. Test it with a real account.
- Supabase free-tier pausing during testing. Upgrade before outside testers.
- If Replit later says its own auth does everything, don't switch mid-build. Decide once, before the sign-in prompt.
