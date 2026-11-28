# Rules for AI Agents: Documentation

## How to use this document

These rules say how AI agents write and organize technical documentation in any project. They extend the general [development rules](https://arashnm80.com/ai-rules/development) (R1 to R5), mainly R2 (document as you go), R4 (human readability) and R5 (long-term maintainability). When the two conflict, the general rules win. A project may add its own rules on top (for example, which tracker and docs site it uses); it may not lower these.

Two words used below: the **docs home** is the one place documentation lives (a docs repository or a `docs/` folder), and the **tracker** is the issue tracker (Linear, Jira, GitHub Issues). Cite rules as D1, D2 and so on.

## D1. One docs home, organized by purpose

**Rule.** Keep all technical documentation in one docs home, in folders by purpose, with an index page and navigation that reach every page.

**Rules for agents**

1. Default layout: `projects/<repo>/` (one repository), `projects/workspace/` (knowledge that spans repositories, including the glossary and the server inventory), `issues/open/` and `issues/done/` (task folders, D2), `decisions/` (D8), `api/` (API specs or collections), `templates/`, and `skills/` and `rules/` for agents.
2. Keep the index and navigation in sync with the files in the same change that adds, removes, renames or moves a page. Generate navigation from the folder tree when the tooling allows it.
3. One fact lives in one place. Link to it instead of copying it.

**Red flags:** a page nothing links to; a broken link; two pages that state the same fact differently.

## D2. Task folders follow the task lifecycle

**Rule.** Every task gets one folder holding its whole written record, and the folder moves from open to done when the task ships.

**Rules for agents**

1. Name it `<ISSUE-ID>-<slug>` for a tracker issue, otherwise `YYYY-MM-DD-<slug>`, with a lowercase kebab-case slug. Check that no folder for that issue exists yet.
2. Files, each only when needed, started from `templates/`: `draft.md` (before work, one screen), `breakdown.md` (big tasks: subtasks A, B, C split per R1, each with scope, "done when", dependencies), `plan.md` (before code), `doc.md` (during and after work, D4).
3. A big task gets one subfolder per subtask with its own `plan.md` and `doc.md`. The parent `doc.md` is an index table plus the final state (what was merged and deployed).
4. When the task ships: finish `doc.md`, update the living pages (D5), move the folder to done, update the index, close the issue.

**Red flags:** one task in both open and done; two folders for one issue; a shipped task still under open; a task file that matches no template.

## D3. Every document stands alone

**Rule.** A reader with no chat history and no tracker access can understand, continue or reproduce the work from the docs alone.

**Rules for agents**

1. Copy the exact requirements (title, description, acceptance criteria, key comments) from the tracker once, into the task's first document. Later documents link to that copy instead of repeating it. Still link to the issue.
2. Start every document with a title (`<ISSUE-ID> — <title>`), and links to its parent task, its plan and the issue.

**Red flags:** "see the ticket" as the only explanation; requirements pasted into several files that now disagree.

## D4. doc.md is a runbook of the final version

**Rule.** `doc.md` records what was actually done, so another person can reproduce, operate or undo it. It shows only the final, working version; git keeps the history.

**Rules for agents**

1. Past tense, with the exact commands, configs, paths, versions, branches and commit hashes. Leave out facts anyone can look up.
2. For a service, deploy or server change, include how to start, stop, update, verify and troubleshoot it.
3. Record where the work differed from the plan and why. Don't narrate failed attempts; delete replaced approaches, and leave a one-line pointer in any doc that still describes the old one.
4. End with the result: how it was verified, and its known limits (R2.7). Update it after each step, not only at the end (R2.3).

**Red flags:** "configured the server" with no command; "first we tried X"; future tense in a finished doc.

## D5. Living pages describe the system as it is now

**Rule.** Task records say what happened; living pages say how the system works today. Every lasting fact ends up on a living page, so nobody has to replay old tasks to understand the system.

**Rules for agents**

1. Give each living page one job: tutorial (learn), how-to (do one task), reference (look up facts) or explanation (understand why). Don't mix them on one page.
2. When a task changes how something works, update or create the living page in the same task, and link it from the task's `doc.md`.
3. Put an owner and a `Last reviewed: YYYY-MM-DD` line under the title of each living page. Update the date whenever you check the page against reality.
4. Generate reference (API specs, config lists) from the code when possible, instead of writing it by hand.

**Red flags:** "read tasks A to O to see how payments work"; a living page older than the code it describes; a page that is half tutorial, half reference.

## D6. Code commits and docs are linked

**Rule.** Every code change is traceable from its docs, and docs change in the same task as the code they describe.

**Rules for agents**

1. Commit the code first. Then add a commit table to `doc.md` (repository and branch, short and full hash, message, files), and commit the docs once.
2. Stage only files that belong to the task.
3. In the same task, update every doc the change affects: living pages, API specs, setup guides.
4. Write docs commit messages as `docs: <verb> <what>`.

**Red flags:** a shipped change with no hash in its doc; an API change with an outdated spec; a docs commit titled "update".

## D7. Problem first, short and scannable

**Rule.** Readers scan before they read. Plans, drafts and issues open with the problem; records and answers open with a summary. Structure carries the rest.

**Rules for agents**

1. Right after the title of a plan, draft or issue, state the problem in plain language: what happens today, who it affects, what is missing. Requirements and steps come after.
2. Use tables for structured facts, numbered steps for procedures, and copy-ready code blocks for every command.
3. Keep drafts and progress notes to about one screen. Use plain words (R4), and define each domain term once in the glossary.

**Red flags:** a plan that opens with steps; a wall of prose where a table fits; a command inside a sentence.

## D8. Decisions and incidents keep their reasons

**Rule.** The final-version rule removes failed attempts, not reasons. Lasting decisions and production incidents get records that keep the why.

**Rules for agents**

1. Record each decision that is costly to reverse (architecture, vendor, data model, security) as an ADR (architecture decision record): `decisions/NNNN-<slug>.md` with context, options considered, decision, consequences. Never rewrite an accepted ADR; supersede it with a new one and link both ways.
2. For a production incident, `doc.md` also covers impact, timeline, root cause and follow-up actions, without blame. Each follow-up becomes a tracker issue or a task folder.

**Red flags:** nobody knows why a choice was made; the same incident happens twice; a postmortem that names a person as the cause.

## D9. No secrets or personal data in docs

**Rule.** Documentation gets copied, published and indexed. It holds no secrets and no personal data.

**Rules for agents**

1. Write where a secret lives (an `.env` path, a secret manager entry), never its value.
2. Refer to customers by internal ID, never by name, phone number or email. Staff contact details go only in the one access-control page.
3. Keep server addresses in the server inventory page and refer to servers by name elsewhere.

**Red flags:** a password, token or key value; a customer's phone number; an IP address repeated across task docs.

## D10. Checks enforce the rules, and the bar only rises

**Rule.** What can be checked by a machine is checked on every change, and the documentation gets more standard over time, never less.

**Rules for agents**

1. Run the docs checks before committing: site build or validate, broken links, pages missing from navigation, secret scan. Fix the doc, never weaken the check.
2. Every new page meets the current rules. When you edit an old page, bring the part you touch up to the current rules (Boy Scout rule); list larger cleanups as tasks instead.
3. When a rule is missing, unclear or keeps getting broken, propose a rule or a new check in your summary. The owner decides; agents don't change the rules themselves.

**Red flags:** a check disabled to make a commit pass; new pages copying an outdated pattern; the same review comment made twice with no rule added.
