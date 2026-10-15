# Welcome — let's build your second brain

You're one hour away from having an AI that knows your work.

By the end:
- You'll have a folder on your desktop that your AI reads and writes to.
- You'll have ingested your first source (a meeting note, an article, or a voice memo).
- You'll have asked your AI a question about your own work — and gotten a sourced answer back.

No coding. No terminal. If you can download a file and open an app, you can do this.

---

## Before you start — install 2 free apps (~5 min)

You need both. They look at the same folder and do different jobs.

1. **Claude Code (desktop app)** — your AI. Download: https://claude.com/claude-code/download
2. **Obsidian** — to see your brain visually. Download: https://obsidian.md/download

Install both. Don't open them yet.

---

## Step 1 — Open your brain in both apps (~3 min)

You already have the `brain-starter` folder on your desktop. We're going to point both apps at it.

**In Obsidian:**
1. Open Obsidian.
2. Click **"Open folder as vault"** (or the icon with a folder).
3. Pick the `brain-starter` folder. Click Open.
4. Trust the folder when prompted.

You should now see a sidebar showing folders like `raw/`, `wiki/`, `_system/`. That's your brain.

**In Claude Code:**
1. Open Claude Code.
2. Click **"Open Folder"**.
3. Pick the same `brain-starter` folder.
4. You should see Claude greet you with the folder loaded.

Both apps are now looking at the same folder. Obsidian is your reading view. Claude Code is the AI.

---

## Step 2 — Talk to your AI for the first time (~15 min)

In Claude Code, open the file called `STARTER-PROMPT.md` (it's in the root of `brain-starter/`).

Copy everything below the line that says "Copy everything below this line."

Paste it into the Claude Code chat. Send it.

What happens next:
- Claude reads your `_system/` files (these tell Claude how your brain is organized).
- Claude reads this `START-HERE.md` so it knows where you are.
- Claude asks you 5-10 questions about your work — your role, your projects, the people you work with, the tools you use.
- Claude uses your answers to customize a file called `_system/domains.md`. This file becomes the AI's understanding of YOUR specific work.

**Just answer Claude's questions honestly.** Short answers are fine. Claude will tell you when you're done.

When Claude finishes customizing `domains.md`, it'll show you a draft. Read it. If it looks right, say "looks good." If something's off, tell Claude what to change.

---

## Step 3 — Ingest your first source (~15 min)

Now you have a customized brain. Time to put something in it.

Pick ONE of these (whichever is easiest right now):

- **A meeting transcript** — export from Granola, Otter, Fireflies, or any meeting tool. Drop it into `raw/transcripts/`.
- **An article you saved** — copy the text into a `.md` or `.txt` file. Drop it into `raw/articles/`.
- **A voice memo** — drop the `.m4a` or `.mp3` file into `raw/voice/`.

In Claude Code, say: **"Ingest this for me."**

Claude will:
1. Read the file.
2. Pull out what matters (the TL;DR, the key claims, the people mentioned, the concepts).
3. Write a clean summary into `_outputs/` — that's the drafts folder.
4. Show you the draft.

Look at the draft in Obsidian. Read it. Check if it captured what you cared about.

If it looks good, tell Claude: **"Looks good. Move it to wiki/."**
If something's off, tell Claude what to fix first.

When you approve, Claude moves the draft from `_outputs/` to `wiki/sources/`. That's where your brain stores its real knowledge.

---

## Step 4 — Ask your AI a question (~5 min)

Now the magic part. Ask Claude a question about what you just ingested.

Examples:
- "What's the most important thing from that meeting?"
- "Who was mentioned, and what was their position?"
- "What did the author argue, in plain English?"
- "What questions does this raise for me?"

Claude will pull the answer from the source page it just created, and cite where the info came from.

That's your second brain working.

---

## You did it.

Your brain has 1 source in it. Within a month of dropping things in — meetings, articles, voice memos, anything you read — Claude will know your work the way you do.

A few things to try this week:

- Ingest 3 more sources. Different kinds: a meeting, an article, a voice memo.
- Ask Claude: "Across everything I've put in, what's the pattern?" Claude will write a `synthesis` page — its own take, citing the sources.
- Open Obsidian, click the graph view (left sidebar icon that looks like a constellation). Watch your brain take shape as you add more.

---

## What's in this folder (reference)

You don't need to know this to use the brain. But if you're curious:

- `raw/` — what you drop in. Claude reads, never modifies.
- `wiki/` — what Claude writes. Read it, ask Claude to update it.
- `_outputs/` — drafts before they go to `wiki/`. Claude shows you drafts here; you approve.
- `_system/` — the rules and customization. Set up once, mostly forget.
- `.claude/skills/` — Claude's tools (ingest, lint, link). You don't touch these.

---

## Stuck?

DM **@paugrowths** on Instagram. I see every DM. Tell me which step you're on and what you're seeing.

Or just ask Claude — Claude knows this folder better than I do.
