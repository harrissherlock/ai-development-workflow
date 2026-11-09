---
name: ai-development-workflow
description: Develop and improve software projects with a traceable GitHub Issue, branch, PR, automated checks, and deployment previews. Use when a user requests implementation, bug fixes, tests, code review preparation, or continued changes to an existing PR. Supports ChatGPT Work and other compatible coding agents.
---

# AI Development Workflow

Use this skill to execute a software-development request through a GitHub-centered workflow. Prefer the tools already connected to the current agent, such as GitHub, a terminal, and Vercel. Do not assume those tools or their permissions are available.

## Operating principles

1. **Identify the target and latest state.** Determine the repository, current branch/PR/Issue, relevant files, runtime, build scripts, tests, deployment configuration, and `AGENTS.md`. Re-read files before editing, especially when the user or another agent may have changed them.
2. **Interpret the requested behavior.** Record observable requirements and completion criteria. Avoid unrelated features, dependencies, or refactoring. When the task is actionable, proceed without unnecessary confirmation.
3. **Choose an owner and branch.** Continue the existing task branch and PR when appropriate. For new work, create a dedicated branch and, if useful, an Issue. One active writer owns a task branch at a time. Avoid force pushing or overwriting another contributor's work.
4. **Implement and verify.** Make the smallest coherent changes, run relevant tests and builds, investigate failures, correct the implementation, then repeat checks. Test important user interactions with a browser when available. Never present an unexecuted check as passing.
5. **Create or update the PR.** Describe behavior changed, key files, executed checks, and remaining limitations. Link the Issue if one exists. Confirm the PR contains the latest intended commits.
6. **Inspect CI and preview for the current commit.** Check GitHub Actions results against the PR head SHA. When a real Vercel preview exists, verify that the deployment corresponds to the current head and inspect the target behavior. Do not invent preview URLs or claim unavailable CI or deployment results.
7. **Deliver concrete outcomes.** Return the PR URL, test results, preview URL when verified, and any unresolved blocker. Merge or publish to production only when the user has explicitly instructed it.

## Decision guide

- **Request without a repository:** use the existing conversation context, if sufficient; otherwise ask for the repository address only when essential.
- **Repository exists and write tools are available:** edit code, test, push changes, and create or update a PR.
- **Read-only connection or missing execution tools:** perform every available check, record specific limits, and supply ready-to-apply changes where possible. Never imply remote changes were made.
- **Existing PR:** fetch the latest head, changed files, and comments; respect subsequent user changes and update that PR instead of creating a duplicate.
- **Failure in CI or browser:** inspect the failed step/log, reproduce when possible, fix the cause, rerun checks, and review the new head SHA.
- **Preview deployment pending:** verify its status; give an actual preview link only when the deployment can be identified.

## Guides and reusable resources

Read only the guides relevant to the current request:

- [Development procedure](references/development-process.md): task intake, branches, PRs, and safe continuation.
- [Testing and CI](references/testing-and-ci.md): validation strategy, failure diagnosis, and result reporting.
- [Vercel previews](references/vercel-previews.md): preview identification, commit matching, and browser verification.
- [Future-agent interoperability](references/agent-compatibility.md): shared contracts for an eventual background agent.
- [Security and permissions](references/security.md): credential handling, untrusted input, and approval boundaries.
- [Project AGENTS.md template](templates/AGENTS.md): project-specific instructions to copy and adapt.
- [Issue template](templates/ISSUE_TEMPLATE.md) and [PR template](templates/PULL_REQUEST_TEMPLATE.md): task specification and review summaries.
- [Example Node CI workflow](templates/node-ci.yml): a starting example, not a universal project configuration.

## Example request

> Use ai-development-workflow on `owner/repository`. Add a calendar with month/week views and drag-to-change task dates. Save the updated date in the existing task model, test the interaction, open a PR, and provide the matching Vercel preview if available.

For output structure and completion checks, see [Development procedure](references/development-process.md).
