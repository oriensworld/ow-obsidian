---
name: ow-obsidian-query
description: Answer questions using evidence already stored in an Obsidian vault, with progressive retrieval and wikilink citations. Use for "what does this vault know", "search my notes", "answer from the vault", "query the wiki", comparisons grounded in vault content, or explicit `$ow-obsidian-query` requests.
---

# OW Obsidian Query

Answer from the vault rather than from unstated model memory.

## Workflow

1. Use the `ow-obsidian` vault-resolution workflow and read its `references/vault-contract.md`.
2. Read the configured hot cache when present, then the main index or maps of content.
3. Search note titles, aliases, tags, headings, body text, and wikilinks for the question's key terms and synonyms. Use `ow-obsidian-retrieve` for large vaults or ambiguous queries.
4. Read the smallest set of relevant notes, then follow links needed to verify context or contradictions.
5. Distinguish vault evidence, reasonable synthesis, and information absent from the vault.
6. Answer directly and cite supporting notes with `[[wikilinks]]`. Mention conflicting or stale notes explicitly.
7. Do not change the vault unless the user also asks to preserve the answer or the local vault contract explicitly requires query logging.

## Retrieval discipline

- Prefer hot cache, indexes, and maps before broad full-vault reads.
- Prefer primary/source notes over downstream summaries when both exist.
- Do not claim completeness when relevant folders were excluded or unreadable.
- If the vault lacks enough evidence, say what is missing and offer ingestion or external research as a separate next step.
