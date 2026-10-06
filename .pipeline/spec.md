# Spec: Core loop 1 (foundation · sign-in · Your World mechanics · Scribe)

**Planner · 2026-10-06** · Branch for the build: `feature/core-loop-1` (Builder creates it Fri Oct 9) · App: `issue11/` (Expo SDK 57, expo-router, TypeScript strict)
**Status: WAITING FOR MEGAN'S SPEC APPROVAL** (target Wed Oct 8). This slice touches Authentication, User data, Database migrations, Permissions, API keys, Security and infrastructure. Under the Production Safety Rule, nothing gets built until Megan approves this spec.

Scope as of request.md (Oct 6, four updates from Megan): onboarding is out (placeholder entry point only). Your World is mechanics only. Scribe covers free writing, writing-prompt answers and gratitude entries, each with a per-entry "in my Issue" choice. Prompt wording is data, not code.

---

## Summary
Replace the Expo starter with ISSUE11's shell: four native tabs (Your World · Audio · Scribe · Publish), the 11 sticker as a Lucky Star placeholder, and one design-token system that holds every color, font, size, radius and placeholder image. Add account creation and sign-in (Sign in with Apple + email one-time code) on Supabase. Inside that shell, build Your World mechanics: pick your own photos, save them privately and show them in a simple grid. Build Scribe: write freely, answer a writing prompt or write a gratitude entry. All three are Scribe entries she can edit and delete, each with an "include in my Issue" choice that is off by default. Prompts are loaded from a database table so their wording (drafted separately) can change without an app release. The data is shaped so Publish can later read World photos and only the chosen Scribe entries.

**Explicitly out of scope:** onboarding screens and questions (a single placeholder entry point only) · Home and Explore tabs · writing prompt *content* (drafted separately; this slice ships the mechanism and an empty table) · Audio content (tab is a placeholder) · Publish/magazine/AI (tab is a placeholder) · Lucky Star behaviour (sticker opens a placeholder sheet) · paywall/RevenueCat · curated or suggested images, categories, final World layout · camera capture · voice/mic dictation · Night mode · notifications · account deletion (next slice, see "Slices after this one") · app icon and final splash art.

### Build order inside this slice (QA can check each milestone)
1. **M1 Foundation:** design system, navigation, placeholders, starter removed.
2. **M2 Sign-in:** Supabase client, auth gate, Apple + email code, sign-out, profile row.
3. **M3 Scribe:** list, free write, prompt answer, gratitude, edit, delete, include-in-Issue toggle, prompts loaded from data, local draft safety.
4. **M4 Your World:** picker, resize + strip metadata, private upload, grid, viewer, delete.

### Slices after this one (recommended order, not specced here)
1. **Account + trust:** You/Account screen, in-app **account deletion** (needs a server function holding the service-role key, so it is a sensitive area), privacy policy link. Required before any tester outside Megan and before App Review.
2. **Publish v0:** reads `world_items` + `scribe_entries where include_in_issue`, plus the AI consent screen (design/magazine-ai-spec.md). Waits for Megan's Lucky Star answers and layout keep/cut pass.
3. **Onboarding** (when Megan finalizes it): plugs into `src/app/(auth)/onboarding.tsx`.
4. **Audio.** 5. **Lucky Star** (replaces the placeholder sheet). 6. **Paywall/RevenueCat.**
Timeline risk: Publish on Megan's phone by ~Oct 23 only works if this slice is approved Oct 8 and the Supabase project exists by Oct 9 (Open question 2).

---

## 🧭 Loop stage
**DESIRE → IMAGINE.** Your World lets her collect the images of the life she wants (DESIRE + IMAGINE). Scribe lets her put what she wants into her own words (DESIRE). Prompts help when she doesn't know where to start, and gratitude notices what is already good (a gentle start on BECOME/Proof). and the "include in my Issue" choice marks what becomes part of her magazine (IMAGINE, feeding Publish). Sign-in exists only so this material is kept safely, and the foundation is infrastructure.
**Megan's test:** does it help her move from wanting the future to becoming it? Yes, indirectly. It captures the raw material (her images and words) that the magazine, Audio and Lucky Star later turn into the IMAGINE/EMBODY/BECOME experience. Nothing here is a task, goal or tracker. There are no streaks, counts-as-goals or productivity features, and the loop is not shown as navigation.

---

## Files to modify / create
All paths are relative to `issue11/`.

### Remove (Expo starter)
- `src/app/index.tsx`, `src/app/explore.tsx`
- `src/components/{web-badge,external-link,animated-icon,animated-icon.web,hint-row,app-tabs,app-tabs.web,themed-view,themed-text}.tsx`, `src/components/animated-icon.module.css`, `src/components/ui/collapsible.tsx`
- `src/hooks/use-theme.ts`, `src/hooks/use-color-scheme.ts`, `src/hooks/use-color-scheme.web.ts`
- `src/constants/theme.ts`, `src/global.css`
- `scripts/reset-project.js` and the `reset-project` script in `package.json`
- Starter images in `assets/images/`: `react-logo*`, `expo-logo.png`, `expo-badge*.png`, `logo-glow.png`, `tutorial-web.png`, `tabIcons/` (keep `icon.png`, `favicon.png`, `splash-icon.png`, android icons until the real icon slice)

### Modify
- `package.json`: new deps (see Dependencies); add scripts `"test": "jest"`, `"typecheck": "tsc --noEmit"`; `jest` config `{ "preset": "jest-expo" }`.
- `app.json`:
  - `userInterfaceStyle: "light"` (Night mode is a later slice; avoids an untested dark look).
  - `ios.usesAppleSignIn: true`.
  - plugins: `expo-apple-authentication`, `expo-font` (if the font packages need it per current docs), `expo-image-picker` with `photosPermission: "ISSUE11 uses the photos you choose to build Your World."`, and camera/microphone permissions disabled if the plugin supports it (we don't use them). The Builder checks the exact option names in the SDK 57 docs.
  - `expo-splash-screen` `backgroundColor` → the `page` token value (`#FFFFFF`), not Expo blue.
- `README.md`: replace starter text with how to run, test, and the required env var **names** (`EXPO_PUBLIC_SUPABASE_URL`, `EXPO_PUBLIC_SUPABASE_PUBLISHABLE_KEY`), plus how Megan applies the migration. No values.

### Create: design system (the one place the look lives)
- `src/design/tokens.ts`: `colors`, `type`, `spacing`, `radius`, `layout` (see Architecture). **The only file allowed to contain hex colors or raw font sizes.**
- `src/design/fonts.ts`: font family map + `useAppFonts()` hook (loads Archivo Black, Archivo Narrow 400/600/700, IBM Plex Mono 400/500).
- `src/design/images.ts`: registry of brand and placeholder images: `brand.wordmark`, `brand.eleven`, `placeholder.worldEmpty`, `placeholder.scribeEmpty`, `placeholder.tab` (Audio/Publish). Swapping an image = replacing the file or one line here.
- `src/design/index.ts`: re-exports.
- `src/copy/strings.ts`: every user-facing string in one object (`strings.world.emptyTitle`, …) so Megan can change wording in one file.
- `assets/brand/issue11-wordmark-black.png` (exported from `../brand/logo/issue11-wordmark-black.webp` or the `.svg`) and `assets/brand/eleven-sticker.png` (from `../design/claude-design/v1-prototype/assets/0bb93fbeaae4f5c1075c630112490891.png`, the LOGO11 used in the prototype).
- `assets/placeholders/world-empty.png`, `scribe-empty.png`, `tab.png`: plain flat tiles in the `cream` token color (no photos, no stock imagery).

### Create: UI primitives (`src/components/ui/`)
`Text.tsx`, `Button.tsx`, `Screen.tsx`, `TextField.tsx`, `Toggle.tsx`, `EmptyState.tsx`, `ErrorBanner.tsx`, `TabHeader.tsx`, `ElevenSticker.tsx`, `PlaceholderScreen.tsx`. All styles come from `src/design`.

### Create: routes (`src/app/`)
```
_layout.tsx                 root: fonts, splash, AuthProvider, Stack, auth gate
(auth)/_layout.tsx          Stack, headerless
(auth)/welcome.tsx          wordmark, line "See it. Write it. Become it.", CONTINUE → onboardingEntry()
(auth)/onboarding.tsx       PLACEHOLDER entry point: renders nothing, <Redirect href="/sign-in" />
(auth)/sign-in.tsx          "Continue with Apple" (iOS only) + "Continue with email" + Terms/Privacy line
(auth)/email.tsx            email field → send code
(auth)/verify.tsx           6-digit code field → verify; resend after 60 s
(app)/_layout.tsx           protected Stack: (tabs) + modal routes
(app)/(tabs)/_layout.tsx    NativeTabs: world · audio · scribe · publish (+ 11, see Architecture)
(app)/(tabs)/world.tsx      Your World grid
(app)/(tabs)/audio.tsx      PlaceholderScreen
(app)/(tabs)/scribe.tsx     Scribe list
(app)/(tabs)/publish.tsx    PlaceholderScreen
(app)/scribe/[id].tsx       editor; id = "new" or an entry uuid
(app)/world/[id].tsx        full-screen photo viewer + delete
(app)/lucky-star.tsx        modal sheet placeholder
(app)/account.tsx           modal: name, email, sign out
```

### Create: logic
- `src/lib/env.ts`: `getEnv(): { supabaseUrl: string; supabasePublishableKey: string }`. Throws `MissingConfigError` if a var is missing.
- `src/lib/supabase.ts`: single Supabase client, session persisted per the **current** Supabase Expo quickstart (verify; AsyncStorage or expo-sqlite localStorage), `autoRefreshToken` tied to AppState as that guide shows.
- `src/lib/ids.ts`: `newId(): string` (UUID v4 via `expo-crypto`).
- `src/features/auth/AuthProvider.tsx`, `src/features/auth/useAuth.ts`
- `src/features/auth/onboarding.ts`: `ONBOARDING_ENABLED = false`, `onboardingEntry(): Href`
- `src/features/auth/validation.ts`: `isValidEmail(s)`, `isValidCode(s)`
- `src/data/types.ts`, `src/data/repos.ts` (interfaces), `src/data/supabaseRepos.ts`, `src/data/memoryRepos.ts` (in-memory fakes for tests), `src/data/RepoProvider.tsx` (`useRepos()`)
- `src/features/scribe/useScribeEntries.ts`, `src/features/scribe/drafts.ts`
- `src/features/scribe/usePrompts.ts`, `src/features/scribe/promptOfDay.ts`
- `src/features/world/useWorldItems.ts`, `src/features/world/pickAndPrepare.ts`, `src/features/world/grid.ts`
- `supabase/migrations/20261009000000_core_loop_1.sql`

### Create: tests (`src/**/__tests__/`)
- `design/__tests__/no-hardcoded-styles.test.ts`: scans `src/` (excluding `src/design/`) and fails on hex colors (`/#[0-9a-fA-F]{3,8}\b/`), `rgb(`/`rgba(`, or `fontFamily:` string literals.
- `features/auth/__tests__/onboarding.test.ts`, `validation.test.ts`
- `data/__tests__/memoryRepos.test.ts` (contract tests the Supabase repo also follows)
- `features/scribe/__tests__/editor.test.tsx` (toggle default off for all three kinds, save, edit, draft restore, prompt text shown and snapshotted)
- `features/scribe/__tests__/promptOfDay.test.ts` (stable per date, rotates, empty list → null, inactive excluded)
- `features/world/__tests__/grid.test.ts`, `pickAndPrepare.test.ts` (with mocked picker/manipulator)

---

## Architecture

### Design tokens (`src/design/tokens.ts`)
Start values come from `design/claude-design/V4-TOKENS.md` (the look is not locked; values change here only).
```ts
export const colors = {
  ink: '#0d0d0d', page: '#FFFFFF', cream: '#F5EEE0', pink: '#F65AAD', blush: '#FCD2DD',
  grey100: '#F2F2F2', grey300: '#D0D0D0', grey400: '#BDBDBD', sand: '#BDB6AA',
  danger: '#D40806',
  // semantic aliases used by components (components use ONLY these):
  text: ink, textMuted: '#555555', background: page, surface: grey100, border: grey400,
  accent: pink, onAccent: page, overlay: 'rgba(13,13,13,0.6)',
} as const;
export const fontFamily = { display: 'ArchivoBlack_400Regular', body: 'ArchivoNarrow_400Regular',
  bodySemi: 'ArchivoNarrow_600SemiBold', bodyBold: 'ArchivoNarrow_700Bold', mono: 'IBMPlexMono_400Regular' };
export const type = {           // role → { fontFamily, fontSize, lineHeight, letterSpacing, textTransform }
  hero, display, title, body, bodyLarge, label, mono,   // display roles uppercase with tight tracking
};
export const spacing = { xxs: 2, xs: 4, sm: 8, md: 16, lg: 24, xl: 32, xxl: 64 } as const;
export const radius = { image: 3, card: 16, pill: 22, capsule: 40 } as const;
export const layout = { screenPadding: spacing.md, maxContentWidth: 720, gridGap: 6,
  gridMinTile: 110, hitSlop: 44 } as const;
```
`Text` takes `variant: keyof typeof type` and `tone?: 'default'|'muted'|'accent'|'danger'`. `Button` takes `variant: 'primary'|'secondary'`, `label`, `onPress`, `loading?`, `disabled?`. Every touch target is at least 44×44 pt.

### Navigation and the 11 sticker
- Root `_layout.tsx`: `SplashScreen.preventAutoHideAsync()`; wait for `useAppFonts()` and the initial auth state, then hide the splash. Use the expo-router SDK 57 pattern for protected routes (check docs, e.g. `Stack.Protected guard={...}` or redirect in group layout): signed out → `(auth)`, signed in → `(app)`.
- Tabs: `NativeTabs` (already used by the starter: `expo-router/unstable-native-tabs`; check current API). Order follows the UX rule *build your world → experience it → write it → publish*: **Your World · Audio · Scribe · Publish**. Icons are SF Symbols via `expo-symbols`/NativeTabs icon support (photo.on.rectangle, waveform, pencil.line, book.closed).
- **11 sticker:** preferred placement is the centre of the tab bar (Megan's V4 design). If the SDK 57 NativeTabs API cannot open a modal from a trigger without navigating to a tab screen, fall back to `ElevenSticker` in `TabHeader` (top-right, on every tab). The Builder records which one was used in the implementation log. Either way, tapping it opens `/lucky-star` as a modal sheet with the sticker, the title "Lucky Star" and one neutral line from `strings.luckyStar.placeholder`. There is no AI call, no input and no data access.
- `TabHeader`: wordmark left; account button (initial in a circle) right → `/account`.
- `PlaceholderScreen` (Audio, Publish): `placeholder.tab` image, tab title, one neutral line from `strings`. **These are internal-build placeholders. They must be completed or hidden before any App Store submission (checklist 2.1).**

### Auth (`AuthProvider`, `useAuth`)
```ts
type AuthState = { status: 'loading' | 'signedOut' | 'signedIn'; user: User | null };
useAuth(): AuthState & {
  signInWithApple(): Promise<Result>;               // iOS only
  sendEmailCode(email: string): Promise<Result>;    // supabase.auth.signInWithOtp({ email, options: { shouldCreateUser: true } })
  verifyEmailCode(email: string, code: string): Promise<Result>; // supabase.auth.verifyOtp({ email, token: code, type: 'email' })
  signOut(): Promise<void>;
}
type Result = { ok: true } | { ok: false; error: 'cancelled'|'network'|'rate_limited'|'invalid_code'|'expired_code'|'unknown'; message: string };
```
- **Apple:** `expo-apple-authentication` → identity token → `supabase.auth.signInWithIdToken({ provider: 'apple', token, nonce? })`. Follow the current Supabase "Login with Apple / Expo" guide for nonce handling. Hide the Apple button where `AppleAuthentication.isAvailableAsync()` is false (web, Android). If Apple returns `fullName` (first sign-in only), store it as `profiles.display_name`.
- **Email:** one-time 6-digit code (no magic links, so no deep-link setup). Requires Megan to switch the Supabase email template to include the token (dashboard; listed in Open questions).
- **Profile:** after any sign-in, `upsert` `profiles { id: user.id, display_name? }` (RLS-guarded; no database trigger, no `security definer` function).
- **Sign out:** `supabase.auth.signOut()`, clear Scribe drafts (`drafts.clearAll()`), clear the expo-image memory/disk cache, route to `/welcome`.
- **Onboarding placeholder:** `welcome` CONTINUE → `onboardingEntry()` returns `/onboarding` when `ONBOARDING_ENABLED` is true, else `/sign-in`. `(auth)/onboarding.tsx` today is only `<Redirect href="/sign-in" />`. This is the single plug-in point, matching the locked flow (onboarding before "save your issue" sign-in). No onboarding questions, answers or tables are built.
- Missing env vars: root layout shows a plain `ConfigErrorScreen` ("App is not configured") instead of crashing. Values are never printed.

### Data layer
```ts
// src/data/types.ts
type EntryKind = 'free' | 'prompt' | 'gratitude';
type ScribeEntry = { id: string; kind: EntryKind; promptId: string | null; promptText: string | null; title: string | null; body: string; includeInIssue: boolean; createdAt: string; updatedAt: string };
type ScribePrompt = { id: string; kind: 'writing' | 'gratitude'; text: string; sortOrder: number };
type WorldItem   = { id: string; storagePath: string; width: number; height: number; createdAt: string };
// src/data/repos.ts
interface ScribeRepo {
  list(opts?: { before?: string; limit?: number }): Promise<ScribeEntry[]>;   // newest first, default limit 50
  get(id: string): Promise<ScribeEntry | null>;
  upsert(e: { id: string; kind: EntryKind; promptId: string | null; promptText: string | null; title: string | null; body: string; includeInIssue: boolean }): Promise<ScribeEntry>; // id from newId(): retries never duplicate
  setIncludeInIssue(id: string, value: boolean): Promise<void>;
  remove(id: string): Promise<void>;
  listForIssue(): Promise<ScribeEntry[]>;  // include_in_issue = true; for Publish later; unit-tested now, no UI
}
interface PromptRepo {
  listActive(): Promise<ScribePrompt[]>;   // active prompts, ordered by sort_order, id; cached on device for offline
}
interface WorldRepo {
  list(opts?: { before?: string; limit?: number }): Promise<WorldItem[]>;     // newest first, default limit 60
  add(file: PreparedImage, id: string): Promise<WorldItem>; // upload to storage, then insert row; idempotent on id
  remove(item: WorldItem): Promise<void>;                    // delete row, then storage object (retry once; orphan is logged, cleaned by account deletion later)
  displayUrls(paths: string[]): Promise<Record<string, string>>; // batched signed URLs, 1 h expiry
}
```
- `RepoProvider` supplies Supabase repos in the app and memory repos in tests.
- Hooks (`useScribeEntries`, `useWorldItems`) hold `{ items, status: 'loading'|'ready'|'error', error, refresh(), loadMore() }`, refresh on screen focus, and apply optimistic updates with rollback on error. No new state library.

### Scribe
- **Three ways in (`scribe.tsx`, top of the screen):**
  1. **Write**: free writing → `/scribe/new?kind=free`.
  2. **Today's prompt card**: shows the writing prompt of the day (`promptOfDay(prompts, 'writing', localDate)`), a small "Another" button that steps to the next active prompt, and "Answer" → `/scribe/new?kind=prompt&promptId=<id>`. **Hidden** when there are no active writing prompts (empty table, or offline with no cache). Free writing and gratitude still work.
  3. **Gratitude**: → `/scribe/new?kind=gratitude`. If an active gratitude prompt exists, the gratitude prompt of the day is shown in the editor as its heading (`promptId` saved). If none exists, the heading is `strings.scribe.gratitudeHeading` and `promptId`/`promptText` are null.
- **List:** entries newest first. Each row shows the date (mono), a kind label (`strings.scribe.kind.*`), the title or first line, a 2-line preview and a small "In my Issue" marker when included. Empty state (no entries) uses `placeholder.scribeEmpty` + `strings.scribe.emptyTitle`, with the three ways in still visible above it. Pull to refresh, infinite scroll.
- **Editor (`scribe/[id].tsx`, id = `new` or uuid):** for prompt/gratitude entries, the prompt text is shown read-only above the body. Optional title (max 120). Multiline body (1–20,000 chars after trim, required). A `Toggle` labelled `strings.scribe.includeInIssue`, **off by default for every kind**. Save is disabled while the body is empty or a save is in flight. Save sends `{ id: newId() or existing, kind, promptId, promptText }`. `promptText` is a **snapshot** of the wording at save time, so editing or retiring a prompt later never changes her past entry, and Publish can show the question with the answer. Kind and prompt can't be changed after creation. If `promptId` in the route isn't in the loaded prompt list, the editor opens as a free entry (never saves an unknown prompt). Delete (existing entries only) asks for confirmation first.
- **Prompts from data (`usePrompts`, `promptOfDay`):** `PromptRepo.listActive()` reads table `scribe_prompts`. The result is cached on the device (same storage as drafts) and refreshed when Scribe gains focus. `promptOfDay(prompts: ScribePrompt[], kind, localDateISO: string): ScribePrompt | null` filters by kind, orders by `sortOrder, id`, and picks index = days since 2026-01-01 mod n (stable all day, changes at local midnight). **No prompt wording lives in app code.** Megan (or a content agent, with her approval) adds and edits rows in the Supabase table editor. The migration creates the table **empty**. Test prompts exist only in test fixtures/memory repos, never in a migration or seed shipped to her project.
- **Draft safety (`drafts.ts`):** `saveDraft(key, {title, body, includeInIssue})` debounced 500 ms while typing, `loadDraft(key)`, `clearDraft(key)`, `clearAll()`. Key = `scribe:new:<kind>:<promptId|none>` or `scribe:<id>`. Stored on the device. Cleared after a successful save. On opening the editor, a newer draft is restored and a small "Draft restored" note is shown. This covers offline, crash and backgrounding.
- Concurrency: last write wins (`updated_at` set by a trigger). One user, so no conflict UI.

### Your World (mechanics only)
- **Grid (`world.tsx`):** square tiles, `expo-image` `contentFit="cover"`, radius `radius.image`. Columns are computed by `columnsForWidth(width, layout.gridMinTile, layout.gridGap)` (3 on iPhone portrait, more on wide/foldable screens; never a fixed phone width). The header shows an "Add photos" button. The empty state uses `placeholder.worldEmpty` + `strings.world.emptyTitle` + "Add photos". No curated library, categories, captions, favourites or final layout.
- **Add flow (`pickAndPrepare.ts`):**
  `pickImages(): Promise<PickedAsset[] | 'cancelled' | 'denied'>` uses `ImagePicker.launchImageLibraryAsync({ mediaTypes: images only, allowsMultipleSelection: true, selectionLimit: 10 })`. On iOS this is the system picker; check the SDK 57 docs on whether a permission request is needed. If access is denied, show an explanation with an "Open Settings" button (`Linking.openSettings()`).
  `prepareImage(asset): Promise<PreparedImage>` uses `expo-image-manipulator` to resize so the long edge is at most 3000 px (keeps print quality for later), encode JPEG at quality 0.85, and **re-encode, which drops EXIF/GPS metadata**.
  Then for each image: `id = newId()`, `path = <user_id>/<id>.jpg`, upload to bucket `world`, insert row. Tiles show as "uploading" (dimmed + spinner) at once. On failure the tile shows "Retry" / "Remove". Up to 3 uploads run at a time.
- **Viewer (`world/[id].tsx`):** full-screen image (contain), close, Delete (with confirmation). After delete, return to the grid without the item.
- Swapping the look later: tile size, gap, radius and colours come from tokens. Empty and placeholder art comes from `src/design/images.ts`. No component edits needed.

### Data for Publish later
Publish (a later slice) reads: `profiles.display_name`, every `world_items` row (her own chosen photos, via signed URLs or a server function), and `scribe_entries where include_in_issue = true` (`listForIssue()`, served by a partial index), any kind, with `prompt_text` available as the question for prompt answers. **`include_in_issue` is not AI consent.** The separate AI consent screen in magazine-ai-spec.md is still required before any entry is sent to an AI service.

---

## Database changes
New migration `issue11/supabase/migrations/20261009000000_core_loop_1.sql`. **The Builder writes it and never applies it to a live/hosted database.** Megan applies it (Supabase SQL editor or `supabase db push`) after approving the result. A local Supabase (`supabase start`) may be used only if it is already available in the environment.

```sql
-- profiles
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text check (display_name is null or char_length(display_name) <= 80),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
-- scribe_prompts (content table; created EMPTY, rows added by Megan in the dashboard)
create table public.scribe_prompts (
  id uuid primary key default gen_random_uuid(),
  kind text not null check (kind in ('writing','gratitude')),
  text text not null check (char_length(btrim(text)) between 1 and 300),
  active boolean not null default true,
  sort_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index scribe_prompts_active_idx on public.scribe_prompts (kind, sort_order) where active;
-- scribe_entries
create table public.scribe_entries (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  kind text not null default 'free' check (kind in ('free','prompt','gratitude')),
  prompt_id uuid references public.scribe_prompts(id) on delete set null,
  prompt_text text check (prompt_text is null or char_length(prompt_text) <= 300),
  title text check (title is null or char_length(title) <= 120),
  body text not null check (char_length(btrim(body)) between 1 and 20000),
  include_in_issue boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint scribe_entries_kind_prompt_chk check (
    (kind = 'free' and prompt_id is null and prompt_text is null)
    or (kind = 'prompt' and prompt_text is not null)
    or (kind = 'gratitude')
  )
);
create index scribe_entries_user_created_idx on public.scribe_entries (user_id, created_at desc);
create index scribe_entries_issue_idx on public.scribe_entries (user_id, created_at desc) where include_in_issue;
-- world_items
create table public.world_items (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  storage_path text not null unique check (storage_path like (user_id::text || '/%')),
  width int not null check (width > 0), height int not null check (height > 0),
  created_at timestamptz not null default now()
);
create index world_items_user_created_idx on public.world_items (user_id, created_at desc);
-- updated_at trigger (plain trigger function, NOT security definer) on profiles, scribe_prompts, scribe_entries
-- RLS: enable on all three tables; policies `to authenticated` only:
--   scribe_prompts: select for authenticated using (active); NO insert/update/delete policies (only the dashboard/service role can write)
--   profiles: select/insert/update using/with check (id = auth.uid())          (no delete policy)
--   scribe_entries: select/insert/update/delete using/with check (user_id = auth.uid())
--   world_items: select/insert/delete using/with check (user_id = auth.uid())  (no update policy)
-- Storage: private bucket 'world' (public = false, file_size_limit 15 MB, allowed_mime_types {image/jpeg});
--   storage.objects policies for bucket_id = 'world' and (storage.foldername(name))[1] = auth.uid()::text:
--   select, insert, delete for `authenticated`. No update, no anon access.
```
Rollback note in the migration header: drop the four tables, the policies and the bucket (dev only).

## Dependencies
All installed with `npx expo install` (SDK-matched versions). Check each against the SDK 57 docs.
- `@supabase/supabase-js`: auth, database, storage (the planned stack backend).
- Session/draft storage as the current Supabase Expo guide recommends (`@react-native-async-storage/async-storage` or `expo-sqlite`), plus whatever polyfill that guide requires (e.g. `react-native-url-polyfill` if still needed).
- `expo-apple-authentication`: Sign in with Apple (App Store 4.8; primary sign-in).
- `expo-image-picker`: system photo picker.
- `expo-image-manipulator`: resize + JPEG re-encode (strips location metadata).
- `expo-crypto`: client-generated UUIDs (idempotent retries).
- `@expo-google-fonts/archivo-black`, `@expo-google-fonts/archivo-narrow`, `@expo-google-fonts/ibm-plex-mono`: brand fonts (OFL licence).
- Dev: `jest-expo`, `jest`, `@testing-library/react-native`, `@types/jest`.
Already present and reused: expo-router, expo-image, expo-symbols, expo-font, expo-splash-screen, react-native-safe-area-context.

## Edge cases
- **Empty:** no entries → Scribe empty state. No active prompts → prompt card hidden, gratitude uses the default heading, free writing unaffected. No photos → World empty state. Both have one clear action.
- **Offline / slow network:** Scribe drafts persist on the device, a save failure shows `ErrorBanner` with Retry, and the text is never lost. A World upload failure leaves a tile with Retry/Remove. Lists show cached items plus a banner. Prompts use the last cached list. Sign-in shows "No connection" and keeps the email typed in. All network calls time out after 20 s and surface an error (no endless spinner).
- **Duplicates:** client UUIDs + upsert mean a retried save or upload never creates two rows. Save/Add buttons are disabled while in flight (double-tap safe). Picking the same photo twice is allowed (her choice).
- **Concurrent edits** (two devices): last write wins. The list refreshes on focus. A prompt edited or deactivated while she is answering it → her entry keeps the snapshot she saw. A deleted prompt → `prompt_id` becomes null, `prompt_text` is kept.
- **Large data:** paging (50 entries / 60 photos per page). Body capped at 20,000 chars (counter shown after 18,000). 10 photos per pick. Images capped at 3000 px / JPEG, 15 MB bucket limit. Signed URLs are batched per page. expo-image `cachePolicy` uses `storage_path` as the cache key so rotating URLs don't re-download.
- **Auth:** Apple cancelled → silent return, no error. Email typo → inline validation. Wrong/expired code → clear message + resend (60 s cooldown). Rate limit (Supabase's default email sender allows only a few emails per hour) → friendly "Try again in a few minutes". An expired session is refreshed automatically, and a failed refresh → sign-in screen with drafts kept until sign-out.
- **Permissions:** photos denied/limited → explanation + Open Settings, and the app keeps working.
- **Mobile sizes:** iPhone SE (375 pt) through Pro Max and the iPhone Duo open fold. Flex layouts with `layout.maxContentWidth` centring on wide screens, grid columns from width, keyboard-avoiding editor (Save visible above the keyboard), safe areas respected, Dynamic Type scaling on (`allowFontScaling` default) without clipping buttons. Orientation stays portrait (app.json) in this slice; Duo landscape/spread is flagged for a later slice.
- **Sign-out on a shared phone:** drafts and image cache cleared, so the next account sees nothing from the previous one.

## Security considerations
- **Auth:** Supabase Auth only. Apple identity tokens are verified by Supabase. Email codes expire (Supabase default). No passwords stored.
- **Row-level access:** RLS on every table. `scribe_prompts` is read-only to signed-in users (active rows only) and writable by no app user. All other policies are `to authenticated` with `auth.uid()` ownership. Storage objects confined to `<uid>/` and the bucket is private (signed URLs, 1 h). No `security definer` functions and no service-role key anywhere in the app.
- **Input validation:** client (email format, 6-digit code, body/title length) **and** database CHECK constraints (lengths, path prefix). Text is rendered as plain text (no HTML/markdown rendering).
- **Secrets:** only `EXPO_PUBLIC_SUPABASE_URL` and `EXPO_PUBLIC_SUPABASE_PUBLISHABLE_KEY` (public by design, protected by RLS). They are referenced by name only, come from env/EAS env, and are never committed or printed. The service-role key never enters this repo or app.
- **Privacy:** photo re-encode strips GPS/EXIF. No analytics, tracking or third-party AI SDKs. The session token is stored in app storage per the Supabase guide (note: not the Keychain, because SecureStore's size limit; acceptable for v1, revisit in the trust slice).
- **Logging:** never log entry text, emails, tokens or image URLs.

## ⚠️ Sensitive areas touched
- **Authentication:** new sign-up/sign-in (Apple + email code), sessions, sign-out.
- **User data:** private journal text and personal photos stored in Supabase.
- **Database migrations:** four new tables (incl. the read-only `scribe_prompts` content table), RLS policies, a storage bucket and policies (applied by Megan only).
- **Security:** RLS and storage policies are the only barrier between users' private data.
- **API keys/secrets:** new Supabase URL + publishable key env vars (names only in repo). The Apple Sign-in provider is configured in the Supabase dashboard by Megan.
- **Permissions:** iOS photo library access + purpose string, and the Sign in with Apple capability.
- **Production infrastructure:** creates the Supabase project usage, auth provider/email template settings and the storage bucket that production will rely on.
- **Account deletion:** *not built*, but creating accounts makes it mandatory (App Store 5.1.1(v)). It is scheduled as the next slice and must ship before anyone besides Megan uses the app.
- Payments, RevenueCat/subscriptions: None.

## 🍎 App Store compliance
- **4.8 Login:** Sign in with Apple is the primary option, with email as the alternative. There is no Google login. Review notes later need a demo account (email code flow → provide a test account in the account slice).
- **5.1.1(v) Account deletion:** required once accounts exist. Deferred to the next slice, **blocks external TestFlight/App Review** until done.
- **5.1 Privacy:** photo purpose string is clear and asked only when she adds photos. Privacy policy link: sign-in shows the Terms/Privacy line; real URLs are needed before external testing (none exist in the repo yet). Privacy nutrition label: will declare email, user content (photos, text), not linked to tracking. No ATT (no tracking).
- **Privacy manifests:** Expo modules ship their own. The Builder runs `npx expo-doctor` and notes any SDK without one.
- **AI rule:** no data goes to any AI service in this slice. `include_in_issue` is explicitly not AI consent.
- **2.1 Completeness:** Audio, Publish and Lucky Star placeholders are acceptable for internal TestFlight only and must be completed or hidden before submission. No lorem ipsum. All copy is in `strings.ts`.
- **4.2 Not a website:** native tabs (iOS 26/27 Liquid Glass via NativeTabs), system photo picker, native Apple sign-in.
- **HIG / iPhone Duo:** no fixed widths, responsive grid, 44 pt targets, Dynamic Type. Duo landscape/spread comes later.
- **Wellness wording:** no health/therapy claims in any string or prompt row. Prompt content is reviewed against this before Megan adds it.

## Open product questions (max 3, for Megan)
1. **Tabs for now:** this slice uses the 4 functions as tabs (Your World · Audio · Scribe · Publish) with the 11 sticker, and **no Home tab yet**. Home (Lucky Star's Guide card) arrives with Lucky Star. The V4 design's Home · Explore · 11 · Issue · You comes back when those exist. *Recommend: yes, 4 function tabs now.*
2. **Supabase + Apple setup (only you can do this, needed by Fri Oct 9):** is there an ISSUE11 Supabase project? *Recommend: a separate free "issue11-dev" project for this slice.* In it: enable the Apple provider (client ID `com.issue11.app`), set the email template to send the 6-digit code, and share only the URL + publishable key as env vars. Prompt wording then goes in as rows in the `scribe_prompts` table (dashboard table editor), with no app release needed. Sign in with Apple also needs the capability turned on for `com.issue11.app` in your Apple Developer account.
3. **Copy for the Scribe switch:** *Recommend "Put this in my Issue"* (off by default), with a list marker "In my Issue". Change it if you prefer other wording; it lives in one file.
