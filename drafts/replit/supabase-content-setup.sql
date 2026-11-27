-- ISSUE11 content database setup (Nov 27, 2026)
-- Paste once into Supabase → SQL Editor → New query → Run.
-- Read-only content for the app. No user accounts, no personal data.

-- 1. Content tables
create table if not exists public.journal_questions (
  id bigint generated always as identity primary key,
  question text not null,
  explanation text,
  sort int default 0,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists public.first_actions (
  id bigint generated always as identity primary key,
  topic text not null check (topic in ('love','money','my_own_thing','home','glow_up','peace','travel')),
  action text not null,
  smaller_action text,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists public.editor_suggestions (
  id bigint generated always as identity primary key,
  topic text not null check (topic in ('love','money','my_own_thing','home','glow_up','peace','travel')),
  suggestion text not null,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists public.sessions (
  id bigint generated always as identity primary key,
  title text not null,
  topic text,
  audio_url text,
  duration_seconds int,
  sort int default 0,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists public.explore_images (
  id bigint generated always as identity primary key,
  topic text not null,
  image_url text not null,
  alt_text text,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

-- 2. Lock everything, then allow READ ONLY of active rows (app + anyone)
alter table public.journal_questions  enable row level security;
alter table public.first_actions      enable row level security;
alter table public.editor_suggestions enable row level security;
alter table public.sessions           enable row level security;
alter table public.explore_images     enable row level security;

create policy "public read active" on public.journal_questions  for select to anon, authenticated using (active);
create policy "public read active" on public.first_actions      for select to anon, authenticated using (active);
create policy "public read active" on public.editor_suggestions for select to anon, authenticated using (active);
create policy "public read active" on public.sessions           for select to anon, authenticated using (active);
create policy "public read active" on public.explore_images     for select to anon, authenticated using (active);

revoke all on public.journal_questions, public.first_actions, public.editor_suggestions, public.sessions, public.explore_images from anon, authenticated;
grant select on public.journal_questions, public.first_actions, public.editor_suggestions, public.sessions, public.explore_images to anon, authenticated;

-- 3. Storage folder for audio + images (public to read, only you can upload from the dashboard)
insert into storage.buckets (id, name, public)
values ('media', 'media', true)
on conflict (id) do nothing;

-- 4. One test row so we can check the app reads it (delete later)
insert into public.journal_questions (question, explanation, sort)
values ('What would future you do today?', 'You know, the version of you who''s actually doing the things you''ve been talking about.', 1);
