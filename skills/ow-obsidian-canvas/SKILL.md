---
name: ow-obsidian-canvas
description: Create and edit Obsidian JSON Canvas files with note, text, image, PDF, group, and link nodes; perform readable auto-layout and preserve existing IDs and relationships. Use for canvas creation, visual maps, adding vault artifacts to a canvas, zones/groups, or explicit `$ow-obsidian-canvas` requests.
---

# OW Obsidian Canvas

Read [references/canvas-spec.md](references/canvas-spec.md) before editing `.canvas` JSON.

1. Resolve the vault and choose an explicit canvas or an existing locally documented default.
2. Parse the entire JSON before mutation and preserve unknown fields, node IDs, edge IDs, positions, colors, and groups.
3. Support status/list, new canvas, add note, add text, add image, add PDF, add group, connect nodes, and layout operations.
4. Validate referenced files remain vault-relative and exist; use URLs only for deliberate external image nodes.
5. Generate collision-resistant lowercase alphanumeric IDs and ensure uniqueness across nodes and edges.
6. Place new nodes without overlap, using consistent gaps and readable group bounds. Do not relayout existing nodes unless requested.
7. Write valid JSON atomically and reparse it after writing.
8. Summarize added or moved nodes and the canvas-relative path.
