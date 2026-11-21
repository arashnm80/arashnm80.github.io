# Development Rules (Source of Truth for Humans and AI Agents)

Nov 17, 2026 · @Arash Nemat Zadeh

## How to use this document

This is the single source of truth for how code gets written in my projects. Every rule here binds humans and AI agents equally.

**For AI agents:**

1. Read this whole document before planning or writing code.
2. Apply every rule. When a task conflicts with a rule, stop and say which rule it conflicts with, then wait for a decision.
3. When you plan, cite the rule numbers that shaped the plan (for example, "split per R1").
4. Never edit this document unless explicitly asked.

**Priority:** R1 matters most, then R2, R3 and R4 in that order, then the small principles. When rules conflict, the higher one wins.

## R1. Gall's Law: grow complex systems from simple ones that work

**Rule.** Never build a complex system from scratch. Build the smallest version that works end to end, verify it, then evolve it one step at a time.

**Why.** A complex system designed from scratch has too many untested interactions to debug, and it cannot be patched into working (John Gall, *Systemantics*). A working simple system makes every failure traceable to the last step.

**Rules for agents**

1. Start with the smallest working slice: it runs end to end, does one real thing and is verified. Stubs and empty modules don't count.
2. Each step adds one capability and ends working and verified. Don't start the next step on an unverified one; fix or revert a broken step first.
3. Extend a working system, don't rewrite it. Add abstractions, config or frameworks only for a current need.
4. Plan as: Step 0 (the simplest working version), then ordered increments, each with a runnable "done when" check. Detail only the next one.
5. Slice by working behavior, never by layer. A subtask that can't be verified alone is too big: split it.

**Red flags:** nothing runnable until the last step; a "foundation" phase with no behavior; more than one new moving part in a step.

## R2. Document as you go: keep every task resumable

**Rule.** Agent work gets interrupted all the time: laptop off, token limit, lost connection, a new idea, a change of direction. So agents document continuously, and any agent or model can resume from the notes alone, without me re-explaining anything.

**Rules for agents**

1. Before starting a task, create one progress file for it in the project (for example `PROGRESS.md`). One file per task, not many.
2. It holds: the task as I gave it, a checklist (done, in progress, next), the files checked or changed, key decisions and why, open problems, and the next step.
3. Update it after every completed step, not at the end. Write it so a fresh agent with no chat history can continue.
4. Keep it right-sized: enough for a successor to resume, nothing more. No repetition, no play-by-play, no pasted code or logs (point to the file). Aim for one screen; fold finished items into one line each.
5. When I change direction, record the change and why, and mark the replaced items as dropped.
6. When resuming, read the progress file first, check it against the real files, then continue.
7. Use the same standard for documenting code bases, tasks, issues and features. When one is finished, leave a short record: what was done, why, how to verify it, known limits.

**Red flags:** no progress file; notes written only at the end; a successor would have to ask me what happened; a file nobody can read in a minute or two.

## R3. Pareto (80/20): do the vital few first

**Rule.** Roughly 20% of the items drive roughly 80% of the impact. Before working through a set of items, find that 20% and do it first.

**Rules for agents**

1. Survey first: list every candidate (files, packages, bugs, tasks) before fixing any. Keep the survey cheap; it is not a project of its own.
2. Rank by impact (severity, exposure, cost of failure), not by discovery order or file path. State the criteria you used.
3. Work the top of the ranking first. After each batch, re-check what impact remains, and stop or ask when the rest adds little.
4. Don't walk items one by one (file by file, package by package) unless that order is also the impact order.
5. Report what you deferred and why.

**Example.** Fixing vulnerabilities: scan the whole project, rank the findings by severity and exposure, fix the critical few first. Don't open each file or package in turn and fix whatever turns up.

**Red flags:** no ranking exists; low-severity or cosmetic items fixed while critical ones remain; "I'll just go alphabetically".

## R4. Clean code and human readability: write for people first

**Rule.** Every file (code, docs, configs, commit messages) must follow clean code principles and be easy for a human to read, in clear natural language. AI readability comes for free; human readability does not, so protect that one. Clean code principles are a living baseline: today that means Robert C. Martin's *Clean Code*, and the baseline may change as the field and AI tools evolve.

**Rules for agents**

1. Write for the next human reader, who has no context. If a person would need an explanation to follow it, rewrite it.
2. Use plain, specific words. Name things for what they are or do. Define any acronym or jargon the first time it appears.
3. Apply the baseline principles (*Clean Code*): intention-revealing names, small functions that do one thing, no duplicated logic, explicit error handling, comments only where the code can't speak for itself.
4. Prefer obvious code over clever code. If a trick is unavoidable, add a short comment saying what it does and why. Comments and docs explain why, not what.
5. Never format a file for machines at the cost of people (dense one-liners, cryptic abbreviations, prompt-style shorthand). Instead, write normally; agents handle plain text fine.
6. Follow the baseline as written. If you think a principle is outdated or a better practice exists, say so in your plan and keep following the baseline until I update it here.

**Red flags:** you needed to re-read a passage to follow it; names like `data2`, `tmp`, `handleStuff`; a function that does several things; copy-pasted logic; a comment that repeats its code; a document only an agent could parse.

## Small principles

Lowest priority, below R1 to R4. One line each.

- **Boy Scout rule:** leave code better than you found it. If you spot something ugly or against best practice while working on something else, fix it when the fix is simple, cheap and breaks nothing; otherwise mention it in your summary.
- **Style consistency:** match the existing style of the codebase (naming, structure, formatting). If you know a better or more standard style, ask me before using it. If I approve, apply the new style from that point on.
- **DRY (don't repeat yourself):** avoid duplicated logic; extract shared code into one place.
- **KISS (keep it simple):** prefer the simpler solution, as long as it is still best practice and standard.
