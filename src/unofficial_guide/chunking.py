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
    current_start_paragraph = 0
    current_length = 0
    chunk_index = 0

    def paragraph_block_length(block: list[str]) -> int:
        if not block:
            return 0
        return sum(len(paragraph) for paragraph in block) + 2 * (len(block) - 1)

    def build_overlap_block(source_paragraphs: list[str]) -> list[str]:
        if overlap <= 0 or not source_paragraphs:
            return []

        overlap_block: list[str] = []
        overlap_length = 0
        for paragraph in reversed(source_paragraphs):
            overlap_block.insert(0, paragraph)
            overlap_length = paragraph_block_length(overlap_block)
            if overlap_length >= overlap:
                break
        return overlap_block

    def flush_chunk() -> None:
        nonlocal chunk_index, current_paragraphs, current_start_paragraph, current_length
        if not current_paragraphs:
            return
        chunk_text = "\n\n".join(current_paragraphs).strip()
        if chunk_text:
            chunks.append(
                Chunk(
                    chunk_id=f"{document.source_id}-{chunk_index}",
                    source_id=document.source_id,
                    text=chunk_text,
                    start_char=0,
                    end_char=len(chunk_text),
                    metadata={"source_path": str(document.path)},
                )
            )
            chunk_index += 1
        current_paragraphs = []
        current_length = 0

    for paragraph_index, paragraph in enumerate(paragraphs):
        paragraph_length = len(paragraph)
        if current_paragraphs and current_length + paragraph_length > chunk_size:
            flush_chunk()
            if chunks:
                previous_paragraphs = split_paragraphs(chunks[-1].text)
                current_paragraphs = build_overlap_block(previous_paragraphs)
                current_length = paragraph_block_length(current_paragraphs)
                current_start_paragraph = max(0, paragraph_index - len(current_paragraphs))

        if not current_paragraphs:
            current_start_paragraph = paragraph_index

        current_paragraphs.append(paragraph)
        current_length += paragraph_length

    flush_chunk()
    return chunks


def chunk_corpus(documents: list[SourceDocument], chunk_size: int = 350, overlap: int = 50) -> list[Chunk]:
    chunks: list[Chunk] = []
    for document in documents:
        chunks.extend(chunk_document(document, chunk_size=chunk_size, overlap=overlap))
    return chunks
