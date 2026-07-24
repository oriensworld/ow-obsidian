# Organization Modes

- `existing`: preserve the vault's current custom structure and templates. Default for established vaults.
- `generic`: use confirmed source, note, index, log, and cache roots without another methodology.
- `lyt`: use maps of content plus atomic linked notes; folders are secondary.
- `para`: route by actionability into projects, areas, resources, and archives.
- `zettelkasten`: create atomic, densely linked notes with stable unique IDs.

Optional configuration:

```json
{
  "version": 1,
  "mode": "existing"
}
```

Mode does not override explicit paths, local instructions, immutable source roots, or existing filename conventions. Do not create upstream-specific `wiki/` paths unless the consuming vault already uses them.
