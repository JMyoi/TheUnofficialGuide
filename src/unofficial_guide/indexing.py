from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .chunking import chunk_corpus
from .corpus import load_corpus
from .embedding import EmbeddingBackend, SentenceTransformerEmbeddingBackend
from .vector_store import ChromaVectorStore, RetrievedChunk


@dataclass(slots=True)
class IndexResult:
    document_count: int
    chunk_count: int
    persist_dir: Path
    collection_name: str


def index_corpus(
    corpus_dir: Path,
    persist_dir: Path,
    *,
    chunk_size: int = 350,
    overlap: int = 50,
    collection_name: str = "unofficial_guide",
    embedder: EmbeddingBackend | None = None,
    store: ChromaVectorStore | None = None,
) -> IndexResult:
    documents = load_corpus(corpus_dir)
    chunks = chunk_corpus(documents, chunk_size=chunk_size, overlap=overlap)
    embedder = embedder or SentenceTransformerEmbeddingBackend()
    created_store = store is None
    store = store or ChromaVectorStore(persist_dir=persist_dir, collection_name=collection_name)

    try:
        if chunks:
            embeddings = embedder.embed([chunk.text for chunk in chunks])
            store.upsert_chunks(chunks, embeddings)
    finally:
        if created_store:
            store.close()

    return IndexResult(
        document_count=len(documents),
        chunk_count=len(chunks),
        persist_dir=persist_dir,
        collection_name=collection_name,
    )


def search_corpus(
    query: str,
    persist_dir: Path,
    *,
    top_k: int = 4,
    collection_name: str = "unofficial_guide",
    embedder: EmbeddingBackend | None = None,
    store: ChromaVectorStore | None = None,
) -> list[RetrievedChunk]:
    embedder = embedder or SentenceTransformerEmbeddingBackend()
    created_store = store is None
    store = store or ChromaVectorStore(persist_dir=persist_dir, collection_name=collection_name)

    try:
        query_embedding = embedder.embed([query])[0]
        return store.query(query_embedding, top_k=top_k)
    finally:
        if created_store:
            store.close()
