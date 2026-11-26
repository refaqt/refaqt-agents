---
name: github-actions
description: >-
  Use when you add or change a GitHub Actions workflow (.github/workflows/*.yml). Gives the rule to use actions on Node 24, how to check a version, and what to read after the first run.
---

# GitHub Actions workflows

- **Use actions that run on Node 24.** GitHub has deprecated Node 20 for actions, and every run
  that still uses one shows a warning. Before you add or change a `uses:` line, find the newest
  major tag (`git ls-remote --tags https://github.com/actions/<name>.git`) and check `runs.using`
  in its `action.yml`. It must say `node24`, or `composite` with only Node 24 actions inside.
  Read the breaking changes of each major version you skip.
- Known good on 2026-11-26: `checkout@v7`, `setup-python@v7`, `setup-node@v7`,
  `configure-pages@v6`, `upload-pages-artifact@v5`, `deploy-pages@v5`.
- `setup-node@v5` and newer cache by default. Set `package-manager-cache: false` in a job that
  can deploy or holds secrets.
- A job that needs the shared kit or doqs checks out submodules: `submodules: recursive`.
- After a workflow change, open the first run and read its annotations, not only its result. A
  green run can still carry a deprecation warning.
- `ubuntu-latest` moved to Ubuntu 26 on 2026-10-19. If a job breaks, check the runner image change
  first.
