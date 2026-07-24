---
name: ow-obsidian-cli
description: Detect and use the safest available transport for reading, searching, creating, appending, and updating Obsidian vault notes, preferring an available Obsidian CLI and falling back to direct filesystem operations. Use for Obsidian CLI, vault transport, backlinks, properties, daily notes, or explicit `$ow-obsidian-cli` requests.
---

# OW Obsidian CLI

1. Resolve the vault through `ow-obsidian` before running a transport operation.
2. Detect an Obsidian CLI with the host shell's command lookup; inspect its live `--help` before assuming command syntax because releases differ.
3. Prefer the CLI for operations that require Obsidian semantics such as resolved search, backlinks, daily-note behavior, or Base views.
4. Prefer direct filesystem reads and writes for portable note mutation when the CLI is absent or provides no material advantage.
5. Use configured MCP vault tools only when they are already available and scoped to the resolved vault.
6. Validate every path remains inside the vault and outside immutable source roots before mutation.
7. Preview destructive or overwrite operations and preserve existing frontmatter and line endings.
8. Do not install software, start Obsidian, enable plugins, or persist transport configuration without explicit authorization.

Fallback order: explicit user choice, locally documented choice, suitable Obsidian CLI, existing vault MCP, filesystem.
