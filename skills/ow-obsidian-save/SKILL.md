---
name: ow-obsidian-save
description: Preserve a durable insight, decision, analysis, answer, or conversation as a structured linked note in the current Obsidian vault. Use for "save this", "file this conversation", "keep this insight", "add this answer to the vault", or explicit `$ow-obsidian-save` requests.
---

# OW Obsidian Save

Preserve durable knowledge, not a transcript of the chat.

## Workflow

1. Use the `ow-obsidian` vault-resolution workflow and read its `references/vault-contract.md`.
2. Identify the lasting insight, decision, rationale, evidence, and open questions worth preserving.
3. Search for an existing note that should be updated. Prefer a deliberate merge over duplication.
4. Determine the destination from explicit user direction, local instructions, configured note roots, and neighboring note conventions.
5. Use the user-provided title. If absent, choose a concise descriptive title unless local instructions require asking.
6. Write declarative, self-contained Markdown that a future reader can understand without the conversation.
7. Match established frontmatter and connect related notes with `[[wikilinks]]`.
8. Update configured navigation, log, and hot cache when those artifacts exist and require maintenance.
9. Confirm the saved note using its wikilink and vault-relative path.

## Selection rules

Save decisions with rationale, non-obvious synthesis, reusable analyses, research conclusions, and resolved questions. Skip transient troubleshooting, obvious lookups, secrets, and content already captured without improvement.

Never overwrite an existing note blindly or write into a source root.
