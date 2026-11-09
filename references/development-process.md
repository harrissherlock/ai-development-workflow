# Development procedure

## Discover existing state

- Confirm the repository identifier and available permissions.
- Read `AGENTS.md`, `README.md`, package manifests, application structure, test scripts, and existing CI and deployment configuration.
- If the request refers to an Issue or PR, inspect its latest description, comments, head SHA, changed files, and checks before editing.
- Avoid restoring text or files the user removed after a previous edit. Fetch again when remote state differs from your last read.

## Plan the change

Write practical acceptance conditions: what a user does, what should happen, persistence, failures, responsive layout if relevant, and how to verify it. Identify affected components and tests.

## Develop

1. Use the existing task branch when continuing a PR; otherwise create a branch with a descriptive name such as `feature/calendar-view`.
2. Implement a focused change. Follow the project's established architecture and conventions.
3. Run formatter, linter, type checks, tests, and build steps that the repository supports. Add focused tests where warranted.
4. For user-facing features, check the core workflow through the application or browser when the environment allows.
5. Investigate any failures, correct the code, and rerun affected tests.
6. Commit and push changes through available tools; prepare an Issue or PR summary as appropriate.
7. Re-read the remote branch head and review CI and deployment results for that exact commit.

## GitHub integration

Use Issues for tasks and acceptance conditions, branches for isolated changes, and PRs for review. Avoid multiple agents writing to the same branch simultaneously. If a task changes owners, leave a readable handoff that includes task identifier, owner, branch, head SHA, outstanding actions, and test status.

## Completion report

Include:

- Feature or fix delivered, with a concise explanation of actual behavior.
- Repository, branch and PR URL when created.
- Tests executed and their actual outcomes; note unexecuted checks plainly.
- CI result for the latest commit and Vercel preview URL only if verified.
- Blocking permissions or outstanding items, if any.

Do not merge into the production branch or release to production without explicit direction.

## Example: FocusOS calendar

User: Add monthly and weekly calendars, drag tasks to another date, and synchronize with the existing task model.

Agent: inspect current task schema and UI; implement date updates and both views; test persistence after refresh; open PR; inspect latest CI; check Vercel preview; report verified links.

User follow-up: Add a weekly timeline and compact task cards.

Agent: fetch the same PR's current head and latest files, apply the follow-up, rerun tests, and recheck the new preview.
