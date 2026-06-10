from __future__ import annotations

from pathlib import Path

import gradio as gr

from src.unofficial_guide.generation import GeneratedAnswer, generate_answer
from src.unofficial_guide.indexing import search_corpus


DEFAULT_PERSIST_DIR = Path("chroma_db")
DEFAULT_TOP_K = 4


def ask(question: str, persist_dir: str = str(DEFAULT_PERSIST_DIR), top_k: int = DEFAULT_TOP_K) -> tuple[str, str]:
    query = question.strip()
    if not query:
        return "Please enter a question.", ""

    results = search_corpus(query, Path(persist_dir), top_k=top_k)
    generated = generate_answer(query, results)
    return generated.answer.strip(), format_sources(generated)


def format_sources(generated: GeneratedAnswer) -> str:
    if not generated.citations:
        return "No sources retrieved."

    lines: list[str] = []
    for citation in generated.citations:
        source = citation.source_path or citation.source_id
        lines.append(
            f"[{citation.number}] {source} | chunk={citation.chunk_id} | score={citation.score:.3f}"
        )
    return "\n".join(lines)


def build_demo() -> gr.Blocks:
    with gr.Blocks(title="The Unofficial Guide") as demo:
        gr.Markdown("# The Unofficial Guide\nAsk a question about the indexed CSI corpus.")
        question = gr.Textbox(label="Your question", placeholder="What do students say about Professor Keshtgar?")
        ask_button = gr.Button("Ask")
        answer = gr.Textbox(label="Answer", lines=8)
        sources = gr.Textbox(label="Retrieved from", lines=6)

        ask_button.click(ask, inputs=question, outputs=[answer, sources])
        question.submit(ask, inputs=question, outputs=[answer, sources])

    return demo


def main() -> None:
    demo = build_demo()
    demo.launch()


if __name__ == "__main__":
    main()