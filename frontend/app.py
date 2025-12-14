import gradio as gr
from api_client import ai_query
import pandas as pd


def run_ai_query(question):
    try:
        result = ai_query(question)

        # If tabular data
        if isinstance(result, list):
            return pd.DataFrame(result)

        # If string → extract final answer
        if isinstance(result, str):
            lines = result.strip().split("\n")

            # Heuristic: last meaningful line
            final_answer = lines[-1]

            return pd.DataFrame(
                [{"answer": final_answer}]
            )

        return pd.DataFrame(
            [{"message": str(result)}]
        )

    except Exception as e:
        return pd.DataFrame(
            [{"error": f"{str(e)}"}]
        )


with gr.Blocks(title="E-commerce AI Dashboard") as demo:
    gr.Markdown("## 🛒 E-commerce AI Query Interface")
    gr.Markdown(
        "Ask questions in natural language and get answers directly from the database."
    )

    query_input = gr.Textbox(
        label="Ask a question about your database",
        placeholder="e.g. Show top 5 users"
    )

    # Example Prompts (STEP 4)
    gr.Examples(
        examples=[
            "Show top 5 users",
            "List all products under category Electronics",
            "Give orders of user 101",
            "Show top 5 products by price"
        ],
        inputs=query_input
    )

    run_btn = gr.Button("Run Query")

    # STEP 5 — Dataframe Output
    output = gr.Dataframe(
        label="Query Result",
        wrap=True,
        interactive=False
    )

    run_btn.click(
        fn=run_ai_query,
        inputs=query_input,
        outputs=output
    )

demo.launch()
