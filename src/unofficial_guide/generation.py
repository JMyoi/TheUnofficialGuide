from __future__ import annotations

import os
from dataclasses import dataclass

from .vector_store import RetrievedChunk


@dataclass(slots=True)
class Citation:
    number: int
    chunk_id: str
    source_id: str
    source_path: str | None
    score: float


@dataclass(slots=True)
class GeneratedAnswer:
    answer: str
    citations: list[Citation]


def _chunk_source_path(chunk: RetrievedChunk) -> str | None:
    source_path = chunk.metadata.get("source_path") if chunk.metadata else None
    if source_path is None:
        return None
    return str(source_path)


def build_context(retrieved_chunks: list[RetrievedChunk]) -> tuple[str, list[Citation]]:
    citations: list[Citation] = []
    blocks: list[str] = []

    for number, chunk in enumerate(retrieved_chunks, start=1):
        source_path = _chunk_source_path(chunk)
        citations.append(
            Citation(
                number=number,
                chunk_id=chunk.chunk_id,
                source_id=chunk.source_id,
                source_path=source_path,
                score=chunk.score,
            )
        )
        source_label = source_path or chunk.source_id
        blocks.append(
            f"[{number}] source_id={chunk.source_id} source={source_label} score={chunk.score:.3f}\n"
            f"{chunk.text.strip()}"
        )

    context = "\n\n".join(blocks).strip()
    return context, citations


def generate_answer(
    query: str,
    retrieved_chunks: list[RetrievedChunk],
    *,
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0.2,
    api_key: str | None = None,
    client: object | None = None,
) -> GeneratedAnswer:
    if not retrieved_chunks:
        return GeneratedAnswer(
            answer="I could not find relevant evidence in the indexed CSI corpus.",
            citations=[],
        )

    context, citations = build_context(retrieved_chunks)

    system_prompt = (
        "You are a grounded assistant for the Unofficial Guide to College of Staten Island. "
        "Answer only from the supplied context. If the context does not contain enough evidence, "
        "say 'I don't have enough information on that.' Do not invent details. Every factual claim "
        "must be supported with bracket citations like [1] or [2]. When you mention multiple claims, cite each one. "
        "Keep the answer concise and useful."
    )

    user_prompt = (
        f"Question: {query}\n\n"
        "Use only the following retrieved context:\n\n"
        f"{context}\n\n"
        "Write a direct answer with inline citations. If the evidence is weak or conflicting, "
        "say so explicitly instead of guessing."
    )

    if client is None:
        try:
            from groq import Groq
        except ImportError as exc:  # pragma: no cover - depends on installed environment
            raise RuntimeError("groq is required to generate answers") from exc

        if api_key is not None:
            client = Groq(api_key=api_key)
        elif os.getenv("GROQ_API_KEY"):
            client = Groq()
        else:
            raise RuntimeError("GROQ_API_KEY is not set; cannot generate an answer")

    response = client.chat.completions.create(  # type: ignore[call-arg]
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )

    answer = response.choices[0].message.content or ""
    return GeneratedAnswer(answer=answer.strip(), citations=citations)