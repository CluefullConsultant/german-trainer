-- Supabase schema for German Trainer
-- Run this in Supabase SQL editor after creating the project

create table exercises (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz default now(),
  topic text not null,
  exercise_type text not null,
  content jsonb not null,
  mentor_notes text
);

create table submissions (
  id uuid primary key default gen_random_uuid(),
  exercise_id uuid references exercises(id) on delete cascade,
  submitted_at timestamptz default now(),
  answer jsonb not null,
  claude_feedback text,
  mentor_feedback text,
  reviewed_at timestamptz,
  error_tags text[]
);

create table vocabulary (
  id uuid primary key default gen_random_uuid(),
  exercise_id uuid references exercises(id) on delete cascade,
  word text not null,
  definition text not null,
  example text not null,
  added_at timestamptz default now()
);
