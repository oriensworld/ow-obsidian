---
name: ow-obsidian-fold
description: Roll up a bounded set of vault log entries into a traceable extractive summary with links to every child entry. Use for log folding, rollups, compaction of a long activity log, dry-run fold previews, or explicit `$ow-obsidian-fold` requests.
---

# OW Obsidian Fold

Read [references/fold-template.md](references/fold-template.md), then resolve the configured log and destination.

1. Default to dry-run. Require explicit approval for commit mode.
2. Select a bounded contiguous set of entries; accept a count or `k` where count is `2^k`.
3. Parse entries according to the existing log format and retain their order and identifiers.
4. Follow referenced notes only as needed, with a fixed read bound.
5. Produce an extractive summary: every outcome, decision, and open question must trace to at least one child.
6. Generate a deterministic ID from the entry boundary plus content hash or use the vault's existing convention.
7. Self-check child count, links, duplicate coverage, unsupported claims, and destination collision.
8. In commit mode, create the fold note and update the log/index only as local conventions require. Do not delete or rewrite child entries.
