---
name: ow-obsidian-markdown
description: Write and repair portable Obsidian Flavored Markdown, including wikilinks, embeds, callouts, properties, tags, block references, math, Mermaid, and footnotes. Use for Obsidian note formatting, wikilink or callout syntax, frontmatter questions, embeds, or explicit `$ow-obsidian-markdown` requests.
---

# OW Obsidian Markdown

Use [references/syntax.md](references/syntax.md) as the canonical syntax reference when creating or editing vault notes.

1. Resolve the vault and read local note conventions before formatting content.
2. Match neighboring frontmatter keys, casing, date formats, and tag style.
3. Prefer portable CommonMark/GFM constructs; use Obsidian extensions only when they add vault value.
4. Use `[[wikilinks]]` for vault notes and normal Markdown links for external URLs.
5. Preserve user content and repair only the requested syntax.
6. Avoid absolute local paths, HTML-only layouts, and plugin-specific syntax unless already established.
