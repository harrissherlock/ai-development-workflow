# Compatibility with background development agents

The current workflow is interactive: a person asks an agent to develop a feature and reviews a PR. The project can later add OpenHands or another background agent without rebuilding its GitHub-centered collaboration process.

## Shared records

- **Issue:** request, acceptance conditions, links to discussion and assets.
- **Ownership:** one active writer for each task branch.
- **Branch:** isolated implementation for one task.
- **PR:** changes, executed checks, review feedback, preview references.
- **Commit SHA:** key to locating corresponding checks and deployment.
- **AGENTS.md:** project-specific commands, constraints, architecture, and test instructions readable by multiple agents.

## Suggested handoff data

```yaml
task_id: 123
repository: owner/repository
branch: feature/calendar-view
head_sha: <current-commit-sha>
owner: chatgpt-work
status: awaiting-review
checks:
  - name: unit-tests
    result: passed
next_action: review PR and preview
```

This is an example of human-readable metadata, not a required external API.

## Future components, only when required

A background agent needs its own runtime and permissions. Automated Issue pickup, concurrent task allocation, CI-failure retries, progress persistence and cost limits require appropriate agent functionality or a separate scheduler. This skill does not itself schedule work, listen to GitHub webhooks, or run after the conversation ends.

When control passes between agents, fetch latest files and head SHA first, preserve user edits, and avoid two writers updating the same branch concurrently.
