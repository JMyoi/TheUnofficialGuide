import sys
import os
from dotenv import load_dotenv
from groq import Groq
from retrieve import retrieve

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

load_dotenv()

GROQ_MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """You are a helpful assistant for students at CUNY College of Staten Island's Computer Science department.
Answer the question using ONLY the information in the provided document excerpts.
Do not use any outside knowledge.
If the documents don't contain enough information to answer, say exactly: "I don't have enough information on that."
At the end of your answer, list the source files you used on a line starting with "Sources:"."""

_client = None


def _get_client() -> Groq:
    global _client
    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Copy .env.example to .env and add your key.")
        _client = Groq(api_key=api_key)
    return _client


def ask(question: str) -> dict:
    """Retrieve relevant chunks and generate a grounded answer.

    Returns {"answer": str, "sources": list[str]}.
    """
    chunks = retrieve(question, k=8)

    # Build context block with labeled sources
    context_parts = []
    for chunk in chunks:
        context_parts.append(f"[Source: {chunk['source']}]\n{chunk['text']}")
    context = "\n\n".join(context_parts)

    user_message = f"Document excerpts:\n\n{context}\n\nQuestion: {question}"

    response = _get_client().chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
    )

    answer_text = response.choices[0].message.content.strip()

    # Deduplicate source filenames from retrieved chunks
    seen = set()
    unique_sources = []
    for chunk in chunks:
        if chunk["source"] not in seen:
            seen.add(chunk["source"])
            unique_sources.append(chunk["source"])

    return {"answer": answer_text, "sources": unique_sources}


if __name__ == "__main__":
    print("CSI CS Assistant — type a question and press Enter (Ctrl+C to quit)\n")
    while True:
        try:
            question = input("Question: ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not question:
            continue
        print("\nThinking...\n")
        result = ask(question)
        print("Answer:")
        print(result["answer"])
        print("\nRetrieved from:")
        for src in result["sources"]:
            print(f"  • {src}")
        print()
