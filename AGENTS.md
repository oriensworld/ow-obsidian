# OW Obsidian Agent Instructions

This repository contains a portable Claude/Codex plugin. It is not an Obsidian vault.

## Development rules

- Keep shared workflows in `skills/<name>/SKILL.md` using portable Agent Skills frontmatter.
- Keep Claude slash commands in `commands/` as thin adapters to the shared skills.
- Do not add vault notes, source documents, or a sample knowledge base to this repository.
- Do not assume a fixed vault layout. Follow `skills/ow-obsidian/references/vault-contract.md`.
- Treat source roots in a consuming vault as immutable unless that vault explicitly says otherwise.
- Preserve portable Markdown and Obsidian wikilinks in generated notes.
- Update both `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` when release metadata changes.

## Validation

Run the skill validator for every folder under `skills/`, then run the Codex plugin validator against the repository root. Parse both JSON manifests before committing.
