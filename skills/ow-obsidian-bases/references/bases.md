# Bases Reference

Minimal shape:

```yaml
filters:
  and:
    - 'file.ext == "md"'
    - 'file.inFolder("research")'
formulas:
  age_days: '(now() - file.mtime).days'
properties:
  file.name:
    displayName: Note
views:
  - type: table
    name: Research
    order:
      - file.name
      - status
      - formula.age_days
    sort:
      - property: file.mtime
        direction: DESC
```

Useful predicates include `file.hasTag("tag")`, `file.inFolder("path")`, and `file.hasLink("Note")`. Compose filters with `and`, `or`, and `not`.

Supported view families include `table`, `cards`, and `list`; exact options vary by Obsidian version. Formula keys must not collide with source property keys. Quote full filter/formula expressions so YAML does not reinterpret punctuation.

Embed a Base in Markdown with `![[dashboard.base]]` when the vault uses embeds.
