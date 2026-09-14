# Living documentation

One file per entry. Do not put everything into one growing document.

Write these files in B2 English. Follow [communication.md](communication.md). Keep file names, units, and official names exact.

| Location | Purpose | Update trigger |
| --- | --- | --- |
| `docs/log/YYYY-MM-DD_topic.md` | What was done (any role), in date order | A working session worth recording |
| `docs/decisions/YYYY-MM-DD_topic.md` | Why a choice was made | A real technical choice |
| `docs/mistakes/YYYY-MM-DD_topic.md` | Errors and prevention rules | After a mistake or a failed approach |
| `.agents-local/skills/patterns/SKILL.md` | Reusable project-specific coding patterns | A pattern proves useful or changes |

Templates live in this kit under `bootstrap/docs/` and `templates/` (for example `templates/adr.md`). Each folder has a `README.md` index. **Update the index when you add a file**, or the entry is hard to find.

`docs/architecture.md` is a short overview. Detail about a component belongs next to its code, in that module's `README.md`.
