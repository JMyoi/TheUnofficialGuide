from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class SourceDocument:
    source_id: str
    path: Path
    raw_text: str
    cleaned_text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Chunk:
    chunk_id: str
    source_id: str
    text: str
    start_char: int
    end_char: int
    metadata: dict[str, Any] = field(default_factory=dict)
