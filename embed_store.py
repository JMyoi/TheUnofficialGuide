import sys
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from chunk import load_documents

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 75
COLLECTION_NAME = "csi_cs_docs"
CHROMA_PATH = "./chroma_db"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def build_index():
    # Load and chunk documents
    texts, metadatas = load_documents()
    print(f"Loaded {len(texts)} documents.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.create_documents(texts, metadatas=metadatas)
    print(f"Total chunks to embed: {len(chunks)}")

    # Set up ChromaDB with sentence-transformers embedding function
    ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    # Delete existing collection so re-runs start fresh
    try:
        client.delete_collection(COLLECTION_NAME)
        print("Cleared existing collection.")
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"},
    )

    # Build lists for batch upsert
    ids = []
    documents = []
    metadatas_out = []

    for i, chunk in enumerate(chunks):
        source = chunk.metadata["source"]
        ids.append(f"{source}_chunk_{i}")
        documents.append(chunk.page_content)
        metadatas_out.append({"source": source, "chunk_index": i})

    # ChromaDB recommends batches ≤ 5000; 175 chunks is fine in one shot
    print("Embedding and storing chunks (this may take a moment)...")
    collection.add(ids=ids, documents=documents, metadatas=metadatas_out)

    final_count = collection.count()
    print(f"\nDone. Collection '{COLLECTION_NAME}' now has {final_count} chunks.")
    print(f"Persisted to: {Path(CHROMA_PATH).resolve()}")


if __name__ == "__main__":
    build_index()
