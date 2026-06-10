from __future__ import annotations

import argparse
from pathlib import Path

from .chunking import chunk_corpus
from .corpus import load_corpus


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="unofficial-guide")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan a corpus directory and print document stats")
    scan_parser.add_argument("corpus_dir", type=Path)

    chunk_parser = subparsers.add_parser("chunk", help="Chunk a corpus directory and print chunk stats")
    chunk_parser.add_argument("corpus_dir", type=Path)
    chunk_parser.add_argument("--chunk-size", type=int, default=350)
    chunk_parser.add_argument("--overlap", type=int, default=50)

    return parser


def cmd_scan(corpus_dir: Path) -> int:
    documents = load_corpus(corpus_dir)
    print(f"documents={len(documents)}")
    for document in documents:
        print(f"- {document.path} ({len(document.cleaned_text)} chars)")
    return 0


def cmd_chunk(corpus_dir: Path, chunk_size: int, overlap: int) -> int:
    documents = load_corpus(corpus_dir)
    chunks = chunk_corpus(documents, chunk_size=chunk_size, overlap=overlap)
    print(f"documents={len(documents)} chunks={len(chunks)}")
    for chunk in chunks[:10]:
        preview = chunk.text.replace("\n", " ")[:120]
        print(f"- {chunk.chunk_id}: {preview}")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scan":
        return cmd_scan(args.corpus_dir)
    if args.command == "chunk":
        return cmd_chunk(args.corpus_dir, args.chunk_size, args.overlap)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
