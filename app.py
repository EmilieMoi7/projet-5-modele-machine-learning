import gradio as gr

def predict(text):
    return f"Texte reçu : {text}"

with gr.Blocks() as demo:
    gr.Markdown("# Projet 5 – Modèle ML 🚀")
    inp = gr.Textbox(label="Entrée utilisateur")
    out = gr.Textbox(label="Sortie")
    btn = gr.Button("Prédire")

    btn.click(predict, inp, out)

if __name__ == "__main__":
    demo.launch()

