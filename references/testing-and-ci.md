# Testing and CI

## Select suitable checks

Use the repository's actual scripts and toolchain. For a typical TypeScript web project, consider linting, type checking, unit tests, integration tests, production build, and browser end-to-end tests. Do not assume scripts exist. Avoid installing or replacing major test frameworks without project need.

## Troubleshooting steps

1. Identify the failing command, error, and corresponding commit SHA.
2. Reproduce locally or in the provided execution environment when possible.
3. Fix the smallest root cause that addresses the user-facing requirement.
4. Rerun the failing check, then relevant adjacent checks.
5. Inspect the latest GitHub Actions workflow run for the current PR head.

For a calendar drag-and-drop change, test the changed date in the interface, the saved date in the application state or API, and the date after refresh. Check keyboard or mobile alternatives if required by the feature.

## Reporting

A useful summary distinguishes `passed`, `failed`, `not run`, and `unavailable`. A previous successful run is insufficient if code changed afterward. If the current execution environment cannot run a browser or access CI, report exactly what was and was not checked.

## GitHub Actions

Configure appropriate `push` and `pull_request` events in the target project. Use the project's lockfile and supported runtime version. Pin external actions to suitable trusted versions or commit SHAs according to the project's security policies. Keep secrets in repository or deployment-provider secret storage; never in checked-in workflow files.

This skill repository includes an example for Node-based applications at `templates/node-ci.yml`. It requires adjustment to the target project and should not be copied without checking its package manager and scripts.
