import gradio as gr
from pydantic import BaseModel, Field, ConfigDict, ValidationError

# Validation Pydantic des entrées
class PredictRequest(BaseModel):
    age: int = Field(..., ge=16, le=100)
    genre: str
    revenu_mensuel: float
    anciennete_entreprise: int
    satisfaction_employe: int = Field(..., ge=1, le=5)

    model_config = ConfigDict(extra="forbid")


# Fonction de prédiction (API via Gradio)
def predict(age, genre, revenu_mensuel, anciennete_entreprise, satisfaction_employe):
    try:
        payload = PredictRequest(
            age=age,
            genre=genre,
            revenu_mensuel=revenu_mensuel,
            anciennete_entreprise=anciennete_entreprise,
            satisfaction_employe=satisfaction_employe,
        )
    except ValidationError as e:
        raise gr.Error(f"Entrée invalide : {e.errors()}")

    return payload.model_dump()



with gr.Blocks() as demo:
    gr.Markdown("# Projet 5 – Modèle ML 🚀")
    age = gr.Number(label="Âge", precision=0)
    genre = gr.Dropdown(["Homme", "Femme"], label="Genre")
    revenu = gr.Number(label="Revenu mensuel")
    anciennete = gr.Number(label="Ancienneté (années)", precision=0)
    satisfaction = gr.Slider(1, 5, step=1, label="Satisfaction employé")

    out = gr.JSON(label="Résultat")
    btn = gr.Button("Prédire")

    btn.click(
     predict,
     inputs=[age, genre, revenu, anciennete, satisfaction],
     outputs=out,
)


if __name__ == "__main__":
    demo.launch()


