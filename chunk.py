import sys
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pdfplumber

# Force stdout to utf-8 so special PDF characters don't crash on Windows
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DATA_DIR = Path("data")
CHUNK_SIZE = 500
CHUNK_OVERLAP = 75


def load_documents():
    texts = []
    metadatas = []

    for filepath in sorted(DATA_DIR.iterdir()):
        if filepath.suffix == ".txt":
            text = filepath.read_text(encoding="utf-8")
            texts.append(text)
            metadatas.append({"source": filepath.name})

        elif filepath.suffix == ".pdf":
            pages = []
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        pages.append(page_text)
            texts.append("\n".join(pages))
            metadatas.append({"source": filepath.name})

    return texts, metadatas


def main():
    texts, metadatas = load_documents()
    print(f"Loaded {len(texts)} documents from {DATA_DIR}/\n")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.create_documents(texts, metadatas=metadatas)
    total = len(chunks)
    print(f"Total chunks: {total}\n")

    # Print 5 representative chunks spread across the full list
    indices = [0, total // 4, total // 2, (3 * total) // 4, total - 1]
    print("=" * 60)
    print("5 REPRESENTATIVE CHUNKS")
    print("=" * 60)
    for i, idx in enumerate(indices, 1):
        chunk = chunks[idx]
        print(f"\n--- Chunk {i} (index {idx}) | source: {chunk.metadata['source']} ---")
        print(chunk.page_content)
        print(f"[{len(chunk.page_content)} chars]")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
