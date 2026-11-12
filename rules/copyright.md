# Copyright and contributions

This rule covers every file that you create or change in a Refaqt repository, public or private.

Refaqt owns the copyright in its own work. The legal name is **Refaqt (BE 0804.145.539)**.
Contributors keep the copyright in their work and give Refaqt a licence under the
[Refaqt Contributor Licence Agreement](https://github.com/refaqt/.github/blob/main/CLA.md). The
[contributor manual](https://github.com/refaqt/.github/blob/main/CONTRIBUTING.md) explains the
rules for people.

## New files

When you create a text file that we made ourselves, put these two lines at the top, as a comment
in the syntax of that file. Put them after a shebang line (`#!...`) or an XML declaration if the
file has one.

```
SPDX-FileCopyrightText: 2025-2026 Refaqt (BE 0804.145.539) and contributors
SPDX-License-Identifier: <licence of the folder>
```

- Take the licence from the `LICENSE` file of the folder, or of the nearest parent folder:
  `CERN-OHL-S-2.0` for hardware, `GPL-3.0-or-later` for software and firmware, `CC-BY-SA-4.0`
  for documentation and media. In a private repository, use `LicenseRef-Proprietary`.
- Use the current year as the last year: `2025-<this year>`.
- Formats with comments: Python, shell, batch, JavaScript, TypeScript, CSS, HTML (`<!-- -->`),
  Markdown (`<!-- -->`), TOML, YAML, OpenSCAD, FreeCAD macros.
- Formats without comments (JSON, CSV, `.FCStd`, STEP, STL, images, PDF) get no lines. The
  `LICENSE` file of their folder covers them.
- Files that a tool generates, and files that a template copies into another repository as the
  user's own, follow the rules of that tool or template.
- In living docs (`docs/log/`, `docs/decisions/`, `docs/mistakes/`), the folder `LICENSE` is
  enough. Do not add the lines there.

## Changed files

Do not remove or change an existing copyright line or licence line. If a file that we own has a
licence line but no copyright line, you may add the copyright line above it.

## Material from others

Never put the Refaqt notice on material that someone else made: supplier CAD, datasheets, code
from another project, or images from the web. Keep its own notice and licence. Put it in the
folder that the repository uses for it (for example `cad/vendor/` or `docs/datasheets/`), and
record its source and licence there. If the licence does not allow us to use it, do not add it,
and tell the person who asked.

## New repositories

A new Refaqt repository gets, from the start:

- licence files with the copyright notice: run `python doqs/scripts/apply_licenses.py` in a
  repository that uses doqs, or copy the pattern from an existing Refaqt repository;
- a licence section in `README.md` that starts with the copyright notice;
- `.github/workflows/contributor-agreement.yml`, copied from `doqs/templates/contributing/` or
  from `workflow-templates/` in `refaqt/.github`;
- a `CONTRIBUTING.md` that links to the central contributor manual.

## Pull requests from others

Do not merge, and do not advise a person to merge, a pull request whose check
"Contributor agreement" is red. Tell the person what is missing.
