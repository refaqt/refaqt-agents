# Core

- Follow user, tool, system, and skill instructions completely. Use real shell and tools. Do not give up after one failure.
- Follow [communication.md](communication.md) for every reply and every file you write.
- When you write a pull request, a commit message, a comment or review reply on GitHub, an issue, or a log entry, follow [reporting.md](reporting.md). Write it for a manager, not for a developer.
- At the start of each task, read `docs/mistakes/` and briefly say which prevention rules apply before you edit.
- Before larger work, read `docs/architecture.md`. Before new solutions, check `.agents-local/skills/patterns/SKILL.md` if it exists. Use the `maintain-patterns` skill when you add or change patterns.
- If a required living-doc folder is missing (`docs/log/`, `docs/decisions/`, `docs/mistakes/`, `docs/architecture.md`), create it from `.agents/bootstrap/docs/` (or `templates/`). A short first entry is fine. Missing folders are not.
- Keep living documentation up to date during the work, not only at the end. Follow the living-docs rule and the `mistake-log` / `log` skills when they apply.
- Read the existing code before you write. Prefer editing existing files and patterns. When you are not sure, do less and ask.
- Keep diffs small: match local style, do not refactor extra files, and do not add unrelated markdown outside the `docs/` convention files.
