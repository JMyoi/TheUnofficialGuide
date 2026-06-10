from __future__ import annotations

import importlib
import html
import re
from pathlib import Path
from typing import Iterable

from .models import SourceDocument

SUPPORTED_EXTENSIONS = {".txt", ".md", ".html", ".htm", ".pdf"}


def iter_source_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    return sorted(
        path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def read_pdf_file(path: Path) -> str:
    try:
        pdfplumber = importlib.import_module("pdfplumber")
    except ImportError as exc:  # pragma: no cover - dependency is optional for now
        raise RuntimeError("pdfplumber is required to read PDF sources") from exc

    pages: list[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
    return "\n\n".join(pages)


def strip_html_markup(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?i)<br\s*/?>", "\n", text)
    text = re.sub(r"(?i)</p\s*>", "\n\n", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    return text


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_document(path: Path) -> SourceDocument:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md"}:
        raw_text = read_text_file(path)
        cleaned_text = clean_text(raw_text)
    elif suffix in {".html", ".htm"}:
        raw_text = read_text_file(path)
        cleaned_text = clean_text(strip_html_markup(raw_text))
    elif suffix == ".pdf":
        raw_text = read_pdf_file(path)
        cleaned_text = clean_text(raw_text)
    else:
        raise ValueError(f"Unsupported source file type: {path.suffix}")

    return SourceDocument(
        source_id=path.stem,
        path=path,
        raw_text=raw_text,
        cleaned_text=cleaned_text,
        metadata={"extension": suffix, "relative_path": str(path)},
    )


def load_corpus(root: Path) -> list[SourceDocument]:
    return [load_document(path) for path in iter_source_files(root)]
