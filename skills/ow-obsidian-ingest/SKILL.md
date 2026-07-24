---
name: ow-obsidian-ingest
description: Convert one or more immutable source files or user-supplied source locations into derived, linked Obsidian Markdown notes while preserving source material. Use for "ingest", "process this source", "add this to the vault", "turn this into notes", batch ingestion, or explicit `$ow-obsidian-ingest` requests.
---

# OW Obsidian Ingest

Create durable knowledge from sources without modifying them.

## Workflow

1. Use the `ow-obsidian` vault-resolution workflow and read its `references/vault-contract.md`.
2. Resolve each requested source. Confirm it is inside a configured source root or explicitly supplied by the user.
3. Read relevant existing indexes and search for notes covering the same concepts, entities, or claims.
4. Inspect representative destination notes to match frontmatter, filenames, headings, and wikilink conventions.
5. Extract claims, concepts, entities, decisions, questions, and source metadata. Separate direct evidence from synthesis.
6. Prefer updating a relevant existing note over creating a duplicate. Create new notes only in confirmed note roots.
7. Link derived notes to the source using the vault's established citation style and connect related notes with `[[wikilinks]]`.
8. Update configured navigation, log, and hot cache when those artifacts exist and their conventions require it.
9. Report created and updated paths plus unresolved contradictions or missing metadata.

## Rules

- Never edit, rename, move, delete, or normalize the source file.
- Never fabricate bibliographic data or claims.
- Preserve uncertainty and conflicting accounts explicitly.
- Do not force a fixed number of notes; create the smallest coherent set.
- Do not create folders or taxonomies just because they exist in another vault.
- For multiple sources, process them sequentially unless the user or applicable instructions explicitly request parallel agents.
