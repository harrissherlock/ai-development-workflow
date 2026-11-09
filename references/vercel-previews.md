# Vercel previews

1. Confirm that the application is linked to the intended Vercel project. Do not confuse this skill's repository with the target application repository.
2. Check that the PR's latest head SHA matches the SHA of the deployment being inspected.
3. Confirm the deployment reports success and capture its actual preview URL through a trusted provider tool or the GitHub deployment status.
4. Open the preview, when browsing is available, and exercise the relevant interactions. Where authentication is needed, use authorized credentials or report the access limitation.
5. After any further code change, repeat the SHA and deployment checks. A preview of an earlier commit is not the latest result.

Vercel may not be enabled for some repositories or may be restricted by access controls. In those cases report the available build and test results and describe the missing preview without guessing its address.

Production deployment and PR preview are separate states. Production publication requires the user's approval and a project-specific release process.
