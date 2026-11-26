# refaqt-agents

This repository is the shared agent kit itself. Its rules apply here too: @rules/core.md

Skills live in `skills/<name>/SKILL.md`. Root files for other repositories are generated from
`templates/root/` by `scripts/sync_root.py`: change the template, never a generated copy. Keep
`rules/core.md` under 2.5 KB, and every skill description under 300 characters, because every
session loads them.
