# JSON Canvas Essentials

Root shape:

```json
{
  "nodes": [],
  "edges": []
}
```

Node common fields: `id`, `type`, `x`, `y`, `width`, `height`, optional `color`. Types:

- `text`: add `text` containing Markdown.
- `file`: add vault-relative `file`, optional `subpath`.
- `link`: add `url`.
- `group`: add optional `label`, `background`, `backgroundStyle`.

Edge common fields: `id`, `fromNode`, `toNode`; optional `fromSide`, `toSide`, `fromEnd`, `toEnd`, `color`, `label`.

Use integers for geometry. Sensible defaults: text `320x180`, note `320x220`, image/PDF `360x260`; gap at least `60`. A group must fully contain its member geometry with padding.

Never duplicate IDs, point edges at missing nodes, use absolute file paths, or overwrite unknown root/node/edge fields.
