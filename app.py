import gradio as gr
from groq import Groq 
import os
import retriever
import ingest
from dotenv import load_dotenv

load_dotenv()
client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

def build_prompt(question):
    return f"""
        Answer the question using only the information in the provided documents. If the documents don't contain enough information to answer, say 'I don't have enough information on that. Additionally, cite the source(s) used to help generate the response.
        
        {question}

        Answer:
        """

def ask(question):
    
    ret = retriever.evaluate(question)
    retrieved_docs = build_prompt(ret["prompt"])
    
    prompt = f"""
    
    {retrieved_docs}

    Answer:
    """

    #calling groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": ret["source"],  # Assuming this is a list of strings/filenames
        "prompt": retrieved_docs
    }

def handle_query(question):
    result = ask(question)

    # If retriever.evaluate() returns a list of strings, this will format them perfectly:
    if isinstance(result["sources"], list):
        sources = "\n".join(f"• {s}" for s in result["sources"])
    else:
        # Just in case retriever.evaluate() returns one big block of text string
        sources = str(result["sources"])
        
    return result["answer"], sources, result["prompt"]

retriever.load_vector_db()

with gr.Blocks() as demo:
    inp = gr.Textbox(label="Your question")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    chunks = gr.Textbox(label="Chunks", lines=8)
    btn.click(handle_query, inputs=inp, outputs=[answer, sources, chunks])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources, chunks])

demo.launch()