import gradio as gr

def greet(name):
    return f"Hello {name}!"

textbox = gr.Textbox(label="Type your name here:", placeholder="John Doe", lines=2)
demo = gr.Interface(fn=greet, inputs=textbox, outputs="text")

demo.launch()