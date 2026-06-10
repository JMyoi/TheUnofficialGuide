from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class EmbeddingBackend(Protocol):
    def embed(self, texts: list[str]) -> list[list[float]]:
        """Convert texts into normalized vector embeddings."""


@dataclass(slots=True)
class SentenceTransformerEmbeddingBackend:
    model_name: str = "all-MiniLM-L6-v2"
    _model: object | None = None

    def _load_model(self) -> object:
        if self._model is None:
            from sentence_transformers import SentenceTransformer

            self._model = SentenceTransformer(self.model_name)
        return self._model

    def embed(self, texts: list[str]) -> list[list[float]]:
        model = self._load_model()
        embeddings = model.encode(texts, normalize_embeddings=True)
        return embeddings.tolist()
