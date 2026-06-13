import sys
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

COLLECTION_NAME = "csi_cs_docs"
CHROMA_PATH = "./chroma_db"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

_client = None
_collection = None


def _get_collection():
    global _client, _collection
    if _collection is None:
        ef = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
        _client = chromadb.PersistentClient(path=CHROMA_PATH)
        _collection = _client.get_collection(
            name=COLLECTION_NAME, embedding_function=ef
        )
    return _collection


def retrieve(query: str, k: int = 5) -> list[dict]:
    """Return the top-k most relevant chunks for a query.

    Each result dict has: text, source, chunk_index, distance.
    """
    collection = _get_collection()
    results = collection.query(query_texts=[query], n_results=k)

    chunks = []
    for text, meta, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        chunks.append(
            {
                "text": text,
                "source": meta["source"],
                "chunk_index": meta["chunk_index"],
                "distance": round(distance, 4),
            }
        )
    return chunks


if __name__ == "__main__":
    print("CSI CS Retrieval Test — type a query and press Enter (Ctrl+C to quit)\n")
    while True:
        try:
            query = input("Query: ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not query:
            continue
        print("=" * 60)
        print(f"QUERY: {query}")
        print("=" * 60)
        results = retrieve(query)
        for rank, r in enumerate(results, 1):
            print(f"\n[{rank}] source: {r['source']}  |  chunk_index: {r['chunk_index']}  |  distance: {r['distance']}")
            print(r["text"])
        print()
