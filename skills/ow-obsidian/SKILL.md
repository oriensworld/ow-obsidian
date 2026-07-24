---
name: ow-obsidian
description: Inspect, configure, or orchestrate an existing Obsidian knowledge vault without imposing a fixed folder layout. Use for vault setup, status, structure discovery, workflow routing, index or hot-cache maintenance, "set up Obsidian", "inspect this vault", "continue the wiki", or explicit `$ow-obsidian` requests. Do not use merely to edit this plugin's source repository.
---

# OW Obsidian

Maintain the user's current Obsidian vault as a portable Markdown knowledge base. Treat chat as the interface and linked notes as the durable artifact.

## Resolve the vault

Read [references/vault-contract.md](references/vault-contract.md) before reading or changing vault content.

1. Resolve the vault root from an explicit user path first; otherwise use the current working directory or nearest ancestor containing `.obsidian/`.
2. Refuse to treat the installed plugin directory as a vault unless the user explicitly identifies it and it contains `.obsidian/`.
3. Read applicable local instructions before inspecting notes.
4. Load `.ow-obsidian.json` when present; otherwise infer existing source, note, index, log, hot-cache, and template paths.
5. Preserve the current structure. Do not migrate or scaffold a new taxonomy unless requested.
6. Exclude hidden tool/application directories from source and note discovery.

## Route the request

- Ingest sources: use `ow-obsidian-ingest`.
- Answer from vault knowledge: use `ow-obsidian-query`.
- Audit vault health: use `ow-obsidian-lint`.
- Preserve an insight or conversation: use `ow-obsidian-save`.
- Research and file external sources: use `ow-obsidian-research`.
- Retrieve ranked passages: use `ow-obsidian-retrieve`.
- Work with Obsidian Markdown, Bases, or Canvas: use the matching `ow-obsidian-*` skill.
- Configure methodology, transport, or log folding: use `ow-obsidian-mode`, `ow-obsidian-cli`, or `ow-obsidian-fold`.
- Inspect or configure the vault: continue here.

## Inspect or configure

1. Confirm the root and whether `.obsidian/` exists.
2. Read the hot cache and index first, then report the discovered contract: source roots, note roots, index, log, hot cache, and templates.
3. If discovery is ambiguous, propose `.ow-obsidian.json`; do not write it without the user's request.
4. If the vault is new and the user requests setup, ask only for the vault purpose and preferred organization when local instructions do not already answer them.
5. Create the smallest useful structure, keeping source roots separate from derived notes.
6. Use portable Markdown, relative assets, and Obsidian wikilinks.

## Session continuity

Read the configured hot cache first when it exists. Refresh it after material vault changes, following its current format and size. Do not invent a hot cache when the vault has not requested one.

## Safety

- Never alter files under configured or inferred source roots.
- Never overwrite an existing note without inspecting it and merging deliberately.
- Never initialize Git, install Obsidian, enable plugins, or change `.obsidian/` settings without explicit user authorization.
- Keep unrelated vault content untouched.
