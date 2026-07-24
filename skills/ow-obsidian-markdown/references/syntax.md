# Obsidian Markdown Syntax

## Links and embeds

```markdown
[[Note]]
[[Note|Label]]
[[Note#Heading]]
[[Note#^block-id]]
![[Note#Heading]]
![[image.png|300]]
![[document.pdf]]
```

Use a path-qualified wikilink only to disambiguate duplicate titles. Encode external destinations as `[label](https://example.com)`.

## Callouts

```markdown
> [!note] Optional title
> Body text.

> [!warning]- Collapsed warning
> Hidden until expanded.
```

Common types: `note`, `abstract`, `info`, `todo`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, `example`, `quote`.

## Properties

```yaml
---
title: "Example"
created: 2026-07-24
tags:
  - research
related:
  - "[[Other Note]]"
---
```

Quote values containing wikilinks, colons, `#`, or YAML-significant characters. Do not mix tabs into YAML indentation.

## Other extensions

- Tags: `#tag` or YAML `tags`; follow the vault's existing choice.
- Highlight: `==important==`.
- Block ID: append `^stable-id` to a paragraph.
- Math: `$inline$` or `$$display$$`.
- Mermaid: fenced block with language `mermaid`.
- Footnote: `Text[^1]` with `[^1]: Source.`.

Do not put wikilinks inside inline code, invent links to nonexistent notes without marking them as prospective, or use filesystem backslashes inside wikilinks.
