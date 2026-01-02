import gradio as gr
from pydantic import BaseModel, Field, ConfigDict, ValidationError

# Validation Pydantic des entrées
class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Texte non vide")
    model_config = ConfigDict(extra="forbid")

# Fonction de prédiction (API via Gradio)
def predict(text):
    try:
        payload = PredictRequest(text=text)
    except ValidationError as e:
        raise gr.Error(f"Entrée invalide : {e.errors()}")

    return f"Texte reçu : {payload.text}"

with gr.Blocks() as demo:
    gr.Markdown("# Projet 5 – Modèle ML 🚀")
    inp = gr.Textbox(label="Entrée utilisateur")
    out = gr.Textbox(label="Sortie")
    btn = gr.Button("Prédire")

    btn.click(predict, inp, out)

if __name__ == "__main__":
    demo.launch()


