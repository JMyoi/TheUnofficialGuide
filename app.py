import gradio as gr
from query import ask


def handle_query(question: str):
    if not question.strip():
        return "", ""
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources


with gr.Blocks(title="CSI CS Assistant") as demo:
    gr.Markdown("## CSI Computer Science Assistant")
    gr.Markdown("Ask anything about the CS department at College of Staten Island — courses, faculty, programs, and more.")

    inp = gr.Textbox(label="Your question", placeholder="e.g. What are the core courses in the CS major?", lines=2)
    btn = gr.Button("Ask", variant="primary")
    answer = gr.Textbox(label="Answer", lines=10, interactive=False)
    sources = gr.Textbox(label="Retrieved from", lines=4, interactive=False)

    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

if __name__ == "__main__":
    demo.launch()
