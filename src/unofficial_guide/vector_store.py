from __future__ import annotations

import gc
from dataclasses import dataclass
from pathlib import Path

from .models import Chunk


@dataclass(slots=True)
class RetrievedChunk:
    chunk_id: str
    source_id: str
    text: str
    score: float
    metadata: dict[str, object]


class ChromaVectorStore:
    def __init__(self, persist_dir: Path, collection_name: str = "unofficial_guide") -> None:
        import chromadb

        self.persist_dir = persist_dir
        self.collection_name = collection_name
        self.client = chromadb.PersistentClient(path=str(persist_dir))
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def close(self) -> None:
        self.collection = None  # type: ignore[assignment]
        self.client = None  # type: ignore[assignment]
        gc.collect()

    def upsert_chunks(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        if len(chunks) != len(embeddings):
            raise ValueError("Chunks and embeddings must have the same length")

        self.collection.upsert(
            ids=[chunk.chunk_id for chunk in chunks],
            documents=[chunk.text for chunk in chunks],
            embeddings=embeddings,
            metadatas=[
                {
                    "chunk_id": chunk.chunk_id,
                    "source_id": chunk.source_id,
                    **chunk.metadata,
                }
                for chunk in chunks
            ],
        )

    def query(self, query_embedding: list[float], top_k: int = 4) -> list[RetrievedChunk]:
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        retrieved: list[RetrievedChunk] = []
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for document, metadata, distance in zip(documents, metadatas, distances, strict=False):
            metadata_dict = dict(metadata or {})
            retrieved.append(
                RetrievedChunk(
                    chunk_id=str(metadata_dict.get("chunk_id", "unknown")),
                    source_id=str(metadata_dict.get("source_id", "unknown")),
                    text=str(document or ""),
                    score=1.0 - float(distance or 0.0),
                    metadata=metadata_dict,
                )
            )

        return retrieved
