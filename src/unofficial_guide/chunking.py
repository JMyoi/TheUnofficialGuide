from __future__ import annotations

import re

from .models import Chunk, SourceDocument


def split_paragraphs(text: str) -> list[str]:
    return [paragraph.strip() for paragraph in re.split(r"\n\s*\n", text) if paragraph.strip()]


def chunk_document(
    document: SourceDocument,
    chunk_size: int = 350,
    overlap: int = 50,
) -> list[Chunk]:
    paragraphs = split_paragraphs(document.cleaned_text)
    if not paragraphs:
        return []

    chunks: list[Chunk] = []
    current_paragraphs: list[str] = []
    current_start = 0
    current_length = 0
    chunk_index = 0

    def flush_chunk() -> None:
        nonlocal chunk_index, current_paragraphs, current_start, current_length
        if not current_paragraphs:
            return
        chunk_text = "\n\n".join(current_paragraphs).strip()
        if chunk_text:
            chunks.append(
                Chunk(
                    chunk_id=f"{document.source_id}-{chunk_index}",
                    source_id=document.source_id,
                    text=chunk_text,
                    start_char=current_start,
                    end_char=current_start + len(chunk_text),
                    metadata={"source_path": str(document.path)},
                )
            )
            chunk_index += 1
        current_paragraphs = []
        current_length = 0

    for paragraph in paragraphs:
        paragraph_length = len(paragraph)
        if current_paragraphs and current_length + paragraph_length > chunk_size:
            flush_chunk()
            if overlap and chunks:
                previous_text = chunks[-1].text
                overlap_text = previous_text[-overlap:]
                if overlap_text:
                    current_paragraphs = [overlap_text]
                    current_length = len(overlap_text)
                    current_start = max(0, chunks[-1].end_char - overlap)

        if not current_paragraphs:
            current_start = 0 if not chunks else chunks[-1].end_char

        current_paragraphs.append(paragraph)
        current_length += paragraph_length

    flush_chunk()
    return chunks


def chunk_corpus(documents: list[SourceDocument], chunk_size: int = 350, overlap: int = 50) -> list[Chunk]:
    chunks: list[Chunk] = []
    for document in documents:
        chunks.extend(chunk_document(document, chunk_size=chunk_size, overlap=overlap))
    return chunks
