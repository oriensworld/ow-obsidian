---
name: ow-obsidian-retrieve
description: Retrieve and rank relevant Markdown passages from an Obsidian vault using deterministic local BM25 search, with explainable scores and no external data egress. Use for large-vault search, ranked passages, retrieval debugging, BM25, evidence discovery, or explicit `$ow-obsidian-retrieve` requests.
---

# OW Obsidian Retrieve

Use `scripts/retrieve.py` for deterministic local retrieval.

1. Resolve the vault through `ow-obsidian` and preserve its exclusion and source rules.
2. Run the script with the absolute vault root and the user's query:

   ```powershell
   python scripts/retrieve.py --vault <vault> --query <query> --top 10
   ```

3. Use `--explain` when inspecting scoring, `--json` for structured consumption, and repeated `--include-root` to restrict search to confirmed note roots.
4. Read the top passages, then follow their wikilinks only as needed to verify context and contradictions.
5. Treat rankings as candidates, not truth. Cite the underlying notes in the final answer.
6. Fall back to `rg` title/tag/body search when Python is unavailable.
7. Never send vault content to an external reranker without explicit authorization.

The helper ignores hidden tool/application directories, chunks Markdown by headings, and does not write indexes or caches.
