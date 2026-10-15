# Starter prompt

This is the first thing you send to Claude after opening this folder in Claude Code.

## What to do

1. "Copy everything below this line."
2. Paste it into the Claude Code chat.
3. Send it.

That's it. Claude takes over from there.

---

## Copy everything below this line

---

Hi Claude. I just opened the `brain-starter/` folder. This is the scaffolding for my second brain — an AI-readable wiki for my work.

I'm a first-time user. Today is my onboarding session.

Here's what I'd like you to do, in order:

**1. Read the setup files first.**
- Open `_system/CLAUDE.md` — this tells you how the brain is organized and what your job is.
- Open `_system/schema.md` — this tells you the 5 types of pages the brain holds.
- Open `_system/domains.md` — this is currently a stub. You'll rewrite it in step 2.
- Open `START-HERE.md` — this is what I'm reading; it tells you where I am in the setup.

**2. Customize the brain to my work.**
Ask me 5-10 short questions to understand what I do. Useful things to ask about:
- My role / what I do for work
- The 2-3 projects I'm running right now
- The 3-5 people I work with most
- The tools / platforms I use (calendar, notes, transcription, etc.)
- The kinds of decisions I make often
- What I'd most want the brain to help me with

Keep questions short. Don't ask all at once — go one or two at a time so I can answer easily.

Use my answers to rewrite `_system/domains.md`. Show me the draft before saving. Once I approve, write it.

**3. Walk me through ingesting my first source.**
After `domains.md` is set, ask me to drop a file into `raw/transcripts/`, `raw/articles/`, or `raw/voice/`. Once I confirm the file is in, use the `ingest-source` skill on it.

**4. Show me the draft.**
The `ingest-source` skill writes the synthesis to `_outputs/`. Show me what was generated. Let me approve before it moves to `wiki/sources/`.

**5. Help me ask my first question.**
Once the source is in `wiki/`, suggest 2-3 questions I could ask about it. Then answer the one I pick, with citations from the source page.

---

**Rules you must follow:**

- Never write to `wiki/` without showing me a draft in `_outputs/` first. I review, then we commit.
- Never modify anything in `raw/`. That's my input layer; it's immutable.
- Keep your responses short. I'm a first-time user — long explanations slow me down.
- If you're unsure about something, ask. Don't guess.
- If I get confused, point me at the relevant step in `START-HERE.md`.

Ready when you are. Start with step 1.
