from __future__ import annotations

import argparse
from pathlib import Path

from .chunking import chunk_corpus
from .corpus import load_corpus
from .generation import generate_answer
from .indexing import index_corpus, search_corpus


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="unofficial-guide")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan a corpus directory and print document stats")
    scan_parser.add_argument("corpus_dir", type=Path)

    chunk_parser = subparsers.add_parser("chunk", help="Chunk a corpus directory and print chunk stats")
    chunk_parser.add_argument("corpus_dir", type=Path)
    chunk_parser.add_argument("--chunk-size", type=int, default=350)
    chunk_parser.add_argument("--overlap", type=int, default=50)

    index_parser = subparsers.add_parser("index", help="Build a persistent vector index for the corpus")
    index_parser.add_argument("corpus_dir", type=Path)
    index_parser.add_argument("--persist-dir", type=Path, default=Path("chroma_db"))
    index_parser.add_argument("--chunk-size", type=int, default=350)
    index_parser.add_argument("--overlap", type=int, default=50)

    search_parser = subparsers.add_parser("search", help="Search the persistent index with a text query")
    search_parser.add_argument("query", type=str)
    search_parser.add_argument("--persist-dir", type=Path, default=Path("chroma_db"))
    search_parser.add_argument("--top-k", type=int, default=4)

    ask_parser = subparsers.add_parser("ask", help="Search the index and generate a grounded answer")
    ask_parser.add_argument("query", type=str)
    ask_parser.add_argument("--persist-dir", type=Path, default=Path("chroma_db"))
    ask_parser.add_argument("--top-k", type=int, default=4)
    ask_parser.add_argument("--model", type=str, default="llama-3.3-70b-versatile")

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


def cmd_index(corpus_dir: Path, persist_dir: Path, chunk_size: int, overlap: int) -> int:
    result = index_corpus(
        corpus_dir,
        persist_dir,
        chunk_size=chunk_size,
        overlap=overlap,
    )
    print(
        f"indexed documents={result.document_count} chunks={result.chunk_count} "
        f"persist_dir={result.persist_dir} collection={result.collection_name}"
    )
    return 0


def cmd_search(query: str, persist_dir: Path, top_k: int) -> int:
    results = search_corpus(query, persist_dir, top_k=top_k)
    print(f"query={query!r} results={len(results)}")
    for item in results:
        preview = item.text.replace("\n", " ")[:160]
        print(f"- {item.chunk_id} score={item.score:.3f} source={item.source_id}: {preview}")
    return 0


def cmd_ask(query: str, persist_dir: Path, top_k: int, model: str) -> int:
    results = search_corpus(query, persist_dir, top_k=top_k)
    generated = generate_answer(query, results, model=model)

    print(generated.answer)
    if generated.citations:
        print("\nSources:")
        for citation in generated.citations:
            source = citation.source_path or citation.source_id
            print(
                f"- [{citation.number}] {citation.chunk_id} score={citation.score:.3f} "
                f"source={source}"
            )
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scan":
        return cmd_scan(args.corpus_dir)
    if args.command == "chunk":
        return cmd_chunk(args.corpus_dir, args.chunk_size, args.overlap)
    if args.command == "index":
        return cmd_index(args.corpus_dir, args.persist_dir, args.chunk_size, args.overlap)
    if args.command == "search":
        return cmd_search(args.query, args.persist_dir, args.top_k)
    if args.command == "ask":
        return cmd_ask(args.query, args.persist_dir, args.top_k, args.model)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
