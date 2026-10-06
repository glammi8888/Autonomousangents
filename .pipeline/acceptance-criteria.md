# Acceptance criteria: Core loop 1 (foundation · sign-in · Your World mechanics · Scribe)
Spec: `.pipeline/spec.md` · Planner · 2026-10-06 · All paths relative to `issue11/`.

**How to verify.** "Web" = `npx expo start --web` + a Playwright iPhone viewport (cloud rooms can't reach a phone). "Device" = an iOS development build on Megan's iPhone or the Xcode simulator. Where a criterion says *Device only*, QA marks it **NOT VERIFIABLE IN CLOUD** (not PASS) if no device/simulator is available. "Backend" criteria need a Supabase dev project with the migration applied (Megan applies it), or a local `supabase start`. Without either, QA marks them NOT VERIFIABLE, never PASS.

## A. Foundation and design system (M1)
- **AC-1** No Expo starter content remains: the files listed under "Remove" in the spec are gone, no screen shows Expo/React logos or starter text, and `package.json` has no `reset-project` script.
- **AC-2** `npx tsc --noEmit`, `npx expo lint` and `npm test` all exit 0 on the final commit.
- **AC-3** `src/design/no-hardcoded-styles` test exists and passes: no file under `src/` outside `src/design/` contains a hex color, `rgb(`/`rgba(`, or a `fontFamily:` string literal. QA confirms the test actually fails by temporarily adding `color: '#ff0000'` to a component (then reverting).
- **AC-4** Changing one value in `src/design/tokens.ts` (e.g. `colors.accent`) changes it everywhere it is used, with no other file edited (QA checks on web with one token).
- **AC-5** Changing a path in `src/design/images.ts` (e.g. `placeholder.worldEmpty`) changes the image shown in the World empty state with no component edit.
- **AC-6** All user-facing strings of the new screens come from `src/copy/strings.ts`. Grep finds no literal UI sentences in `src/app/**` or `src/components/**` (accessibility labels included).
- **AC-7** Text renders in Archivo Black (display roles), Archivo Narrow (body) and IBM Plex Mono (mono roles), and the splash screen stays up until fonts are loaded (no flash of system font on launch).
- **AC-8** Signed in, the tab bar shows exactly four tabs in this order: Your World · Audio · Scribe · Publish. There is no Home, Explore, Issue or You tab.
- **AC-9** The 11 sticker is visible on every one of the four tab screens. Tapping it opens a Lucky Star modal sheet with the sticker, the title and one line of copy; it closes with a swipe down or close button. It makes no network request and has no text input (QA checks the network log on web).
- **AC-10** Audio and Publish tabs show a `PlaceholderScreen` (placeholder image, title, one neutral line) with no lorem ipsum, broken buttons or "Spring 2025"-style stale text.
- **AC-11** The account button in the tab header opens an Account modal that shows the signed-in email (and name if known) and a Sign out button.
- **AC-12** `app.json` has `userInterfaceStyle: "light"`, `ios.usesAppleSignIn: true`, the `expo-image-picker` plugin with the photos purpose string from the spec, and the splash `backgroundColor` equal to the `page` token value.

## B. Sign-up / sign-in (M2) ⚠️ Authentication
- **AC-13** Launching while signed out shows Welcome. CONTINUE goes to the Sign-in screen. Code check: `onboardingEntry()` returns `/sign-in` while `ONBOARDING_ENABLED` is `false`, and returns `/onboarding` when it is `true` (unit test).
- **AC-14** `src/app/(auth)/onboarding.tsx` exists, renders no UI and redirects to `/sign-in`. No onboarding questions, answers, screens or tables exist anywhere in the diff.
- **AC-15** Sign-in screen shows "Continue with email" on all platforms. "Continue with Apple" is shown only where Apple sign-in is available: hidden on web (Web), shown on iOS (Device only). The screen shows the Terms/Privacy line.
- **AC-16** Email: an invalid email (e.g. `megan@`) shows an inline error and sends nothing. A valid email sends a code and moves to the code screen (Backend).
- **AC-17** Entering the correct 6-digit code signs her in and lands on the Your World tab (Backend). A wrong code shows "That code didn't work" style copy and stays on the screen. Non-digit or non-6-length input can't be submitted.
- **AC-18** "Resend code" is disabled for 60 s after a send, then works. A Supabase rate-limit error shows a friendly "try again in a few minutes" message, not a raw error (QA can simulate with the memory/mocked auth).
- **AC-19** Sign in with Apple on a device creates the account and lands on Your World. Cancelling the Apple sheet returns to Sign-in with no error message (Device only).
- **AC-20** After the first successful sign-in, a `profiles` row exists with `id = auth.uid()` (Backend). If Apple supplied a name, `display_name` is set.
- **AC-21** Closing and reopening the app keeps her signed in (no sign-in screen) (Web reload + Device).
- **AC-22** Sign out returns to Welcome. After sign-out, protected routes (e.g. typing `/scribe` or `/world/<id>` in the web URL) redirect to the auth flow. Scribe drafts are cleared from device storage (unit test on `drafts.clearAll` being called).
- **AC-23** With env vars missing, the app shows the "not configured" screen instead of crashing, and no env value is printed to the console or UI.
- **AC-24** With the network off, sending a code shows a "No connection" message within 20 s and keeps the typed email.

## C. Scribe (M3) ⚠️ User data
- **AC-25** Scribe tab with no entries shows the empty state (placeholder image + copy) and the Write and Gratitude actions.
- **AC-26** Free writing: Write → type a body → Save → the entry appears at the top of the list with today's date and the "free" kind label. After an app reload it is still there (Backend).
- **AC-27** Save is disabled while the body is empty or whitespace only. A body over 20,000 characters can't be saved, and the counter appears after 18,000.
- **AC-28** The "Put this in my Issue" toggle (copy from `strings.ts`) is **off** when creating a free entry, a prompt answer and a gratitude entry (all three checked). Saving without touching it stores `include_in_issue = false` (Backend: row check; unit: repo call).
- **AC-29** Turning the toggle on and saving stores `include_in_issue = true`, and the list row shows the "In my Issue" marker. Turning it off again and saving removes the marker and stores `false`.
- **AC-30** `ScribeRepo.listForIssue()` returns only entries with `includeInIssue = true`, of any kind, newest first (unit test with memory repo; Backend query check optional).
- **AC-31** Prompts from data: with at least one active `writing` row in `scribe_prompts`, the Today's prompt card shows that row's text. Changing the row's text in the table (no app rebuild) shows the new text after Scribe regains focus (Backend). Grep finds no prompt wording in `src/` outside test fixtures.
- **AC-32** With no active writing prompts (empty table), the prompt card is hidden, and Write and Gratitude still work.
- **AC-33** `promptOfDay` unit tests pass: the same date returns the same prompt, the next date returns the next prompt (wrapping around), inactive prompts are never returned, and an empty list returns `null`.
- **AC-34** "Another" on the prompt card shows a different active prompt (when 2+ exist). "Answer" opens the editor with the prompt text shown read-only above the body. Saving stores `kind = 'prompt'`, `prompt_id`, and `prompt_text` equal to the wording shown.
- **AC-35** Snapshot: after answering a prompt, editing or deleting that prompt row does not change the saved entry's `prompt_text`. A deleted prompt leaves `prompt_id = null` and the entry still opens (Backend).
- **AC-36** Gratitude: with an active gratitude prompt, the editor heading shows it and the entry saves with `kind = 'gratitude'` + that prompt. With none, the heading shows `strings.scribe.gratitudeHeading` and saves with `prompt_id`/`prompt_text` null. The list shows the gratitude kind label.
- **AC-37** Editing an existing entry (title, body, toggle) saves the changes, `updated_at` changes, and `created_at` and the kind/prompt do not.
- **AC-38** Delete asks for confirmation. Cancel keeps the entry; confirm removes it from the list and from the database (Backend).
- **AC-39** Draft safety: type in a new entry, reload the app (or kill it on a device) before saving → reopening the same editor restores the text with a "Draft restored" note. After a successful save the draft is gone.
- **AC-40** Offline save: with the network off, Save shows an error banner with Retry, the typed text stays in the editor, and Retry after reconnecting saves exactly **one** entry (no duplicate rows).
- **AC-41** Double-tapping Save creates one entry, not two.
- **AC-42** The list loads 50 entries per page and loads more on scroll (QA seeds 60+ entries in the memory repo or the dev DB).
- **AC-43** The editor works with the keyboard open on a 375 pt-wide screen: Save and the toggle stay reachable, and the body scrolls (Web iPhone SE viewport + Device).

## D. Your World mechanics (M4) ⚠️ User data · Permissions
- **AC-44** Your World with no photos shows the empty state (placeholder image from `images.ts` + copy) and an "Add photos" button. No curated, suggested or stock images, categories or captions appear anywhere.
- **AC-45** "Add photos" opens the system photo picker, allows multiple selection, and caps a single pick at 10 (Device; Web uses the browser file picker).
- **AC-46** Picked photos appear in the grid at once as "uploading" tiles, then as normal tiles. After an app reload they are still there, newest first (Backend).
- **AC-47** Each uploaded file is a JPEG at most 3000 px on its long edge, stored at `world/<user_id>/<id>.jpg`, with a matching `world_items` row (width/height filled in). Uploaded files contain no EXIF GPS data (QA checks one uploaded file from a geotagged photo, or a unit test asserts the manipulator re-encode path is always used).
- **AC-48** Cancelling the picker changes nothing and shows no error.
- **AC-49** If photo access is denied, the app shows an explanation with an "Open Settings" button and keeps working (Device only, or unit test with a mocked `'denied'` result).
- **AC-50** An upload failure (network off) shows the tile with Retry and Remove. Retry after reconnecting produces exactly one row and one file. Remove discards it.
- **AC-51** Tapping a tile opens the full-screen viewer. Delete asks for confirmation; confirming removes the tile, the row and the storage file (Backend).
- **AC-52** Grid columns adapt to width: `columnsForWidth` unit test gives 3 columns at 375 and 430 pt, and more at ≥ 700 pt. On a wide web viewport the layout has no fixed phone width (content centred within `layout.maxContentWidth`).
- **AC-53** Images display through signed URLs (no public bucket URL works: QA requests `.../storage/v1/object/public/world/<path>` and gets an error) (Backend).
- **AC-54** Grid paging: 60 items per page, more on scroll (memory repo seed).

## E. Database, security and data integrity ⚠️ Migrations · Security
- **AC-55** `supabase/migrations/20261009000000_core_loop_1.sql` exists and creates `profiles`, `scribe_prompts`, `scribe_entries`, `world_items`, the indexes in the spec, the `updated_at` triggers, RLS enabled on all four tables, the policies listed in the spec, and the private `world` bucket with its storage policies. It contains **no** `insert into public.scribe_prompts` rows and no `security definer` functions.
- **AC-56** The migration applies cleanly to an empty Supabase database and has a rollback note (local `supabase start` or Megan's dev project; else NOT VERIFIABLE).
- **AC-57** RLS isolation: user B, signed in, cannot select, update or delete user A's `scribe_entries`, `world_items` or `profiles`, cannot read or list files under `world/<A's id>/`, and cannot insert rows with `user_id = A` (Backend, two test accounts).
- **AC-58** Unauthenticated (anon key, no session) requests return no rows from any of the four tables and cannot upload to `world` (Backend).
- **AC-59** A signed-in user cannot insert, update or delete `scribe_prompts` rows, and cannot read rows with `active = false` (Backend).
- **AC-60** DB constraints reject: an empty/whitespace body, a title over 120 chars, a `kind = 'free'` row with `prompt_text`, a `kind = 'prompt'` row without `prompt_text`, and a `world_items.storage_path` not starting with the owner's id (Backend, SQL check).
- **AC-61** No secret values are committed: the diff contains no `.env` file, no Supabase keys/URLs, and no service-role key. Env vars appear by name only (`EXPO_PUBLIC_SUPABASE_URL`, `EXPO_PUBLIC_SUPABASE_PUBLISHABLE_KEY`) in code and README.
- **AC-62** No code logs entry text, email addresses, tokens or image URLs (grep for `console.` in `src/` shows none of these).
- **AC-63** No network request goes to any AI service or analytics/tracking SDK (dependency list + web network log).

## F. Mobile and accessibility
- **AC-64** Every screen in this slice renders without clipped or overlapping content at 375×667 (iPhone SE) and 430×932 (Pro Max) viewports, respecting safe areas (Web Playwright screenshots attached by QA).
- **AC-65** Every tappable control (tabs, 11 sticker, account, buttons, tiles, toggle) is at least 44×44 pt and has an accessibility label.
- **AC-66** With the largest standard Dynamic Type size (Device) or 200 % browser text zoom (Web), buttons and the toggle label remain readable and tappable.

## G. Process (Production Safety Rule)
- **AC-67** All work is on `feature/core-loop-1`. Nothing is merged to `main`, no EAS submit/TestFlight upload, and the migration is not applied to any hosted database by an agent (implementation log + git log check).
- **AC-68** `README.md` lists how to run, test, the env var names, and the steps for Megan to apply the migration and add prompt rows. The implementation log records which 11-sticker placement was used (tab-bar centre or header fallback) and why.
