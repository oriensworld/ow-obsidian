#!/usr/bin/env python3
"""Rank Obsidian Markdown passages with dependency-free BM25."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


EXCLUDED_DIRS = {
    ".agents",
    ".claude",
    ".codex",
    ".git",
    ".obsidian",
    ".serena",
    ".spec-workflow",
    "node_modules",
}
TOKEN_RE = re.compile(r"[\w-]+", re.UNICODE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass(frozen=True)
class Passage:
    path: str
    heading: str
    line: int
    text: str


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def is_excluded(path: Path, vault: Path) -> bool:
    relative = path.relative_to(vault)
    return any(part in EXCLUDED_DIRS or part.startswith(".") for part in relative.parts[:-1])


def iter_markdown(vault: Path, roots: list[str]) -> list[Path]:
    search_roots = [vault / root for root in roots] if roots else [vault]
    files: list[Path] = []
    for root in search_roots:
        resolved = root.resolve()
        if not resolved.is_relative_to(vault) or not resolved.exists():
            continue
        for path in resolved.rglob("*.md"):
            if path.is_file() and not is_excluded(path, vault):
                files.append(path)
    return sorted(set(files))


def chunk_file(path: Path, vault: Path) -> list[Passage]:
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError):
        return []

    passages: list[Passage] = []
    heading = path.stem
    start = 1
    buffer: list[str] = []

    def emit() -> None:
        text = "\n".join(buffer).strip()
        if text:
            passages.append(
                Passage(path.relative_to(vault).as_posix(), heading, start, text[:12000])
            )

    for number, line in enumerate(lines, 1):
        match = HEADING_RE.match(line)
        if match:
            emit()
            buffer = []
            heading = match.group(2)
            start = number
        buffer.append(line)
    emit()
    return passages


def rank(passages: list[Passage], query: str) -> list[tuple[float, Passage, dict[str, float]]]:
    query_terms = tokenize(query)
    if not query_terms or not passages:
        return []

    documents = [tokenize(f"{p.path} {p.heading} {p.text}") for p in passages]
    average_length = sum(map(len, documents)) / max(len(documents), 1)
    document_frequency = Counter()
    for document in documents:
        document_frequency.update(set(document))

    results = []
    total = len(documents)
    k1, b = 1.5, 0.75
    for passage, document in zip(passages, documents):
        frequencies = Counter(document)
        contributions: dict[str, float] = {}
        for term in query_terms:
            frequency = frequencies[term]
            if not frequency:
                continue
            idf = math.log(1 + (total - document_frequency[term] + 0.5) / (document_frequency[term] + 0.5))
            denominator = frequency + k1 * (1 - b + b * len(document) / max(average_length, 1))
            contributions[term] = idf * frequency * (k1 + 1) / denominator
        score = sum(contributions.values())
        if score > 0:
            results.append((score, passage, contributions))
    return sorted(results, key=lambda item: (-item[0], item[1].path, item[1].line))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True, type=Path)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--include-root", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    args = parser.parse_args()

    vault = args.vault.resolve()
    if not vault.is_dir():
        parser.error(f"vault is not a directory: {vault}")

    passages = [
        passage
        for path in iter_markdown(vault, args.include_root)
        for passage in chunk_file(path, vault)
    ]
    results = rank(passages, args.query)[: max(args.top, 0)]
    payload = []
    for score, passage, contributions in results:
        item = {
            "score": round(score, 6),
            "path": passage.path,
            "heading": passage.heading,
            "line": passage.line,
            "snippet": re.sub(r"\s+", " ", passage.text)[:500],
        }
        if args.explain:
            item["terms"] = {key: round(value, 6) for key, value in contributions.items()}
        payload.append(item)

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for item in payload:
            print(f"{item['score']:.4f}\t{item['path']}:{item['line']}\t{item['heading']}")
            print(f"  {item['snippet']}")
            if args.explain:
                print(f"  terms={item['terms']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
