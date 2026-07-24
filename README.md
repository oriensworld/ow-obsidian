# ow-obsidian

Portable Obsidian knowledge workflows for Claude Code and Codex. The plugin is installed separately from the vaults it maintains.

## Capabilities

- Discover and describe an existing Obsidian vault without imposing a folder scheme.
- Ingest immutable source material into derived, linked Markdown notes.
- Answer questions from vault evidence with wikilink citations.
- Save durable conversation insights into the vault.
- Audit broken links, orphans, duplicate titles, and stale navigation.

## Use

Open Claude Code or Codex in the actual vault directory.

| Workflow | Claude Code | Codex |
|---|---|---|
| Inspect/setup | `/ow-obsidian` | `$ow-obsidian` |
| Ingest | `/obsidian-ingest <source>` | `$ow-obsidian-ingest` |
| Query | `/obsidian-query <question>` | `$ow-obsidian-query` |
| Save | `/obsidian-save [title]` | `$ow-obsidian-save` |
| Lint | `/obsidian-lint` | `$ow-obsidian-lint` |

Natural-language requests can also activate the skills.

## Vault configuration

Configuration is optional. Add `.ow-obsidian.json` to a vault root when auto-discovery is ambiguous:

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

Local `AGENTS.md`, `CLAUDE.md`, or other explicitly referenced vault documentation overrides these defaults.

## Install from source

Claude users can install the plugin from the `oriensworld/ow-marketplace` marketplace. Codex users can load the repository as a local plugin or install its individual skills using the supported Codex plugin/skills workflow.

## Attribution

This project is inspired by the MIT-licensed [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) project and Andrej Karpathy's LLM Wiki pattern. It is an independent, vault-agnostic implementation.
