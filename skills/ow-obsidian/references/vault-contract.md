# Vault Contract

Use this contract for every OW Obsidian operation.

## Resolution order

1. Use a vault path explicitly supplied by the user.
2. Otherwise use the nearest directory at or above the current working directory containing `.obsidian/`.
3. If none exists, treat the current working directory as a candidate only when it contains established Markdown knowledge structures or the user asks to initialize it.
4. If multiple candidates remain, stop before writing and ask for the vault path.

## Instruction precedence

Read applicable instructions in this order, with narrower and explicit instructions winning:

1. The current user request.
2. Repository or directory agent instructions such as `AGENTS.md` and `CLAUDE.md`.
3. Documentation those files explicitly designate as authoritative.
4. `.ow-obsidian.json` path configuration.
5. Existing vault conventions inferred from neighboring notes and indexes.
6. This skill's conservative defaults.

If instructions require a missing file, do not modify vault notes until the requirement is resolved. Plugin development files may still be edited when they are outside the vault-content workflow.

## Optional configuration

`.ow-obsidian.json` uses vault-relative paths:

```json
{
  "version": 1,
  "sourceRoots": ["01-inbox"],
  "noteRoots": ["concepts", "research", "specs"],
  "index": "index.md",
  "log": "log.md",
  "hotCache": "hot-cache.md",
  "templates": "templates"
}
```

Fields may be omitted. Validate configured paths remain inside the resolved vault. Do not follow a configured path outside the vault unless the user explicitly authorizes that external location.

## Conservative discovery

When configuration is absent:

- Source roots: recognize only configured, locally documented, user-identified roots, or strong conventional names: `01-inbox/`, `.raw/`, or `inbox/`. Report "none configured" instead of guessing.
- Note roots: identify non-hidden folders already containing linked Markdown notes; exclude the configured templates directory and do not assume all folders are writable knowledge roots.
- Index: prefer an existing `index.md`, `Home.md`, or locally documented map of content.
- Log: prefer an existing `log.md` or locally documented changelog.
- Hot cache: prefer `hot-cache.md`, then `hot.md`, only when present.
- Templates: prefer an existing `templates/` or `_templates/` directory.
- Exclusions: never infer `.git/`, `.obsidian/`, `.serena/`, `.spec-workflow/`, `.claude/`, `.codex/`, `.agents/`, plugin caches, or other hidden tool/application directories as source or note roots.

Use progressive inspection: read the hot cache and index first; inspect headings or frontmatter from at most one representative note per candidate root only when needed. Do not read the full log, every template, or full representative notes merely to report vault status.

## Mutation invariants

- Treat every source-root file as immutable.
- Create derived notes only in confirmed note roots.
- Preserve portable Markdown and `[[wikilinks]]`.
- Prefer links by unique note title. Use path-qualified wikilinks only when duplicate titles require them.
- Update existing navigation, log, and hot-cache artifacts only when the vault contract calls for them.
- Avoid application-specific metadata unless already established in the vault.
- Report every created or materially updated note by vault-relative path.
- Distinguish pre-existing or tool-created workspace state from files changed by the current OW Obsidian operation.
