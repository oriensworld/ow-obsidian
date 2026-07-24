---
name: ow-obsidian-mode
description: Configure or explain an optional vault organization methodology—existing/custom, generic, LYT, PARA, or Zettelkasten—and route new notes without migrating existing content. Use for vault mode, switch to PARA, use LYT, Zettelkasten setup, filing methodology, or explicit `$ow-obsidian-mode` requests.
---

# OW Obsidian Mode

Read [references/modes.md](references/modes.md), then resolve the vault.

1. Infer and preserve the existing/custom mode when the vault already has a coherent organization.
2. Explain the supported modes and tradeoffs when the user wants a change.
3. Never switch modes or migrate notes implicitly. Confirm the chosen mode and scope.
4. Store an explicit mode in the optional `.ow-obsidian.json` `mode` field only when requested.
5. Route new content through configured `noteRoots`, local instructions, and mode rules; an explicit destination always wins.
6. Validate generated names, reject traversal/reserved paths, and avoid collisions.
7. Treat switching mode as prospective: existing notes remain where they are unless a separate migration is approved.
