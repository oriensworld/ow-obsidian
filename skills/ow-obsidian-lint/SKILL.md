---
name: ow-obsidian-lint
description: Audit an Obsidian knowledge vault for broken wikilinks, orphan notes, duplicate titles, malformed frontmatter, stale navigation, source-boundary violations, and structural inconsistencies. Use for "lint the vault", "vault health check", "find broken links", "find orphan notes", or explicit `$ow-obsidian-lint` requests.
---

# OW Obsidian Lint

Inspect first and report findings before making repairs.

## Workflow

1. Use the `ow-obsidian` vault-resolution workflow and read its `references/vault-contract.md`.
2. Inventory Markdown notes while excluding application state, plugin caches, Git internals, and configured immutable sources from repair targets.
3. Check, in priority order:
   - source-root modifications implied by derived-note conventions;
   - broken or ambiguous wikilinks and missing embeds;
   - duplicate note titles or aliases;
   - orphan notes outside intentional inbox/archive areas;
   - malformed or inconsistent frontmatter relative to neighboring notes;
   - index entries pointing nowhere or significant notes absent from navigation;
   - stale hot-cache claims or log/index disagreement;
   - portability problems such as absolute local paths.
   - hidden tool/application directories incorrectly treated as knowledge or source roots.
4. Report findings by severity with vault-relative file and line references when available.
5. Include counts, assumptions, and excluded paths.
6. Make repairs only when the user explicitly asks for fixes. Never repair immutable sources.

If no findings exist, say so and identify residual checks that were not possible.
